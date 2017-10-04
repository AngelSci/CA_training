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

        # NOTE: Further tests (other values, edge cases, etc) ought to also
        # be tested. See methods below for examples of more thorough testing

    def test_deg_to_rad(self):
        # A selection of values over an expected range and some "edge cases"
        values = np.asarray([0.0, 45.0, 90.0, 135.0, 180.0, 360.0, 361.0,
                             -1.0, 1.0, 360000000.0])
        ref = np.zeros_like(values)
        ref = np.array([ 0.00000000e+00,   7.85398163e-01,   1.57079633e+00,
                         2.35619449e+00,   3.14159265e+00,   6.28318531e+00,
                         6.30063860e+00,  -1.74532925e-02,   1.74532925e-02,
                         6.28318531e+06])

        # Test with scalar values
        for i, v in enumerate(values):
            rad = coords.deg_to_rad(v)
            np.testing.assert_allclose(rad, ref[i])

        # Test vectorized operation
        rad = coords.deg_to_rad(values)
        np.testing.assert_allclose(rad, ref)

    def test_bad_deg_to_rad(self):
        with self.assertRaises(ValueError):
            coords.deg_to_rad(np.float64('nan'))
        with self.assertRaises(ValueError):
            coords.deg_to_rad(np.float64('inf'))

    def test_spherical_to_cartesian(self):
        points = [(0.0, 0.0), (90.0, 180.0), (0.0, 180.0), (90.0, 0.0),
                  (-90.0, -180.0), (-90, 180.0), (1.0, 1.0), (45.0, 90.0)]
        ref = np.asarray([ [1.0, 0.0, 1.0], [0.0, 0.0, 0.0], [-1.0, 0.0, 1.0],
                           [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0],
                           [0.99969541, 0.01744975, 0.9998477],
                           [4.32978028e-17, 7.07106781e-01, 7.07106781e-01] ])

        for i, p in enumerate(points):
            cartesian = coords.spherical_to_cartesian(*p)
            # Example of specifying a looser absolute tolerance here - needed
            # because of proximity to 0 of several results, which "blows up"
            # the relative tolerance metric
            np.testing.assert_allclose(cartesian, ref[i], atol=1e-15)

    def test_spherical_to_cartesian_bad_lat(self):
        for p in ((-91.0, 0.0), (91.0, 0.0)):
            with self.assertRaises(ValueError):
                coords.spherical_to_cartesian(*p)

    def test_spherical_to_cartesian_bad_lon(self):
        for p in ((0.0, -181.0), (0.0, 181.0)):
            with self.assertRaises(ValueError):
                coords.spherical_to_cartesian(*p)


if __name__ == '__main__':
    unittest.main()
