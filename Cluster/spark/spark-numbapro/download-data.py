import subprocess

AWS_KEY = ''
AWS_SECRET = ''

s3_path = 's3n://{0}:{1}@blaze-data/dogs-cats-img/images'.format(AWS_KEY, AWS_SECRET)
cmd = ['hadoop', 'distcp', s3_path, 'hdfs:///tmp/dogs-cats']
subprocess.call(cmd)
