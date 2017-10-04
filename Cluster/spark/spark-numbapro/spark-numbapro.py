import time
import numpy as np
from pyspark import SparkConf
from pyspark import SparkContext

sc = SparkContext('yarn-client', 'spark-numbapro')


def load_images(image):
    from PIL import Image
    import numpy as np
    from StringIO import StringIO
    img = Image.open(StringIO(image[1]))
    rgb = np.asarray(img, dtype=np.uint8)
    return np.sum(rgb.astype(np.int), axis=2) / 3

images = sc.binaryFiles("hdfs:///tmp/dogs-cats/dog.[0-9].jpg").map(load_images)


def cpu_convolution(image):
    from scipy.signal import fftconvolve
    laplacian_pts = '''
    -1 -1 -1
    -1 5 -1
    -1 -1 -1
    '''.split()
    laplacian = np.array(laplacian_pts, dtype=np.float32).reshape(3, 3)
    cvimage_cpu = fftconvolve(image, laplacian, mode='same')
    return cvimage_cpu

cpu_ret = images.map(cpu_convolution)

start_time = time.time()
cpu_ret.collect()
cpu_time = time.time() - start_time
print cpu_time


def gpu_convolution(image):
    import numpy as np
    from numbapro import cuda
    from numbapro.cudalib import cufft

    def best_grid_size(size, tpb):
        bpg = np.ceil(np.array(size, dtype=np.float) / tpb).astype(np.int).tolist()
        return tuple(bpg)

    if hasattr(cuda, 'mult_inplace'):
        mult_inplace = cuda.mult_inplace
    else:
        @cuda.jit('void(complex64[:,:], complex64[:,:])')
        def mult_inplace(img, resp):
            i, j = cuda.grid(2)
            if j < img.shape[0] and i < img.shape[1]:
                img[j, i] *= resp[j, i]
        cuda.mult_inplace = mult_inplace

    laplacian_pts = '''
    -1 -1 -1
    -1 5 -1
    -1 -1 -1
    '''.split()
    laplacian = np.array(laplacian_pts, dtype=np.float32).reshape(3, 3)

    threadperblock = 32, 8
    blockpergrid = best_grid_size(tuple(reversed(image.shape)), threadperblock)

    response = np.zeros_like(image)
    response[:3, :3] = laplacian

    image_complex = image.astype(np.complex64)
    response_complex = response.astype(np.complex64)

    stream1 = cuda.stream()
    stream2 = cuda.stream()

    fftplan1 = cufft.FFTPlan(shape=image.shape, itype=np.complex64,
                             otype=np.complex64, stream=stream1)
    fftplan2 = cufft.FFTPlan(shape=image.shape, itype=np.complex64,
                             otype=np.complex64, stream=stream2)

    # pagelock memory
    with cuda.pinned(image_complex, response_complex):
        # We can overlap the transfer of response_complex with the forward FFT
        # on image_complex.
        d_image_complex = cuda.to_device(image_complex, stream=stream1)
        d_response_complex = cuda.to_device(response_complex, stream=stream2)

        fftplan1.forward(d_image_complex, out=d_image_complex)
        fftplan2.forward(d_response_complex, out=d_response_complex)

        stream2.synchronize()

        mult_inplace[blockpergrid, threadperblock, stream1](d_image_complex,
                                                            d_response_complex)
        fftplan1.inverse(d_image_complex, out=d_image_complex)

        # implicitly synchronizes the streams
        cvimage_gpu = d_image_complex.copy_to_host().real / np.prod(image.shape)

    return cvimage_gpu

gpu_ret = images.map(gpu_convolution)

start_time = time.time()
gpu_ret.collect()
gpu_time = time.time() - start_time
print gpu_time

print '10 images'
print 'CPU: %s' % cpu_time
print 'GPU: %s' % gpu_time

images = sc.binaryFiles("hdfs:///tmp/dogs-cats/dog.[0-4][0-9][0-9].jpg").map(load_images)

cpu_ret = images.map(cpu_convolution)

start_time = time.time()
cpu_ret.collect()
cpu_time = time.time() - start_time
print cpu_time

gpu_ret = images.map(gpu_convolution)

start_time = time.time()
gpu_ret.collect()
gpu_time = time.time() - start_time
print gpu_time

print '500 images'
print 'CPU: %s' % cpu_time
print 'GPU: %s' % gpu_time
