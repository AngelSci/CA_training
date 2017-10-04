import unittest
import coords
import numpy as np

class TestCoordsMethods(unittest.TestCase):

    def test_sphere_dist(self):
        # Reference output. For your own computations, are there canonical
        # test problems or analytical solutions you can use for test values?
        ref = 5879.701488581639

        dist = coords.sphere_dist((51.5, -0.1), (40.7, -74.0))

        # Note: choice of precision somewhat arbitrary - when testing
        # floating-point results, you must decide on an appropriate
        # tolerance for your tests. Default relative tolerance for
        # allclose is 1e-7.
        #
        # assert_allclose works for scalars or ndarrays.
        np.testing.assert_allclose(dist, ref)

if __name__ == '__main__':
    unittest.main()
