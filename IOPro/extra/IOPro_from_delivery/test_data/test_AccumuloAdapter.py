import iopro
import unittest
import numpy as np
import pytest

class TestAccumulo(unittest.TestCase):
    
    hostname = '172.17.0.1'
    port = 42424
    username = 'root'
    password = 'secret'

    def test_connection(self):
        with pytest.raises(IOError):
            adapter = iopro.AccumuloAdapter('bad hostname',
                                            TestAccumulo.port,
                                            TestAccumulo.username,
                                            TestAccumulo.password,
                                            'ints')
        with pytest.raises(IOError):
            adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                            TestAccumulo.port,
                                            'bad username',
                                            TestAccumulo.password,
                                            'ints')
        with pytest.raises(IOError):
            adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                            TestAccumulo.port,
                                            TestAccumulo.username,
                                            TestAccumulo.password,
                                            'bad table name')

    def test_uints(self):
        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'uints',
                                        'u8')
        result = adapter[:]
        expected = np.arange(100000, dtype='u8')
        np.testing.assert_array_equal(expected, result)

    def test_ints(self):
        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'ints',
                                        'i8')
        result = adapter[:]
        expected = np.arange(-50000, 50000, dtype='i8')
        np.testing.assert_array_equal(expected, result)

    def test_floats(self):
        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'floats')
        result = adapter[:]
        expected = np.arange(-50000, 50000, dtype='f8') + 0.5
        np.testing.assert_almost_equal(expected, result)

    def test_strings(self):
        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'strings',
                                        'S10')
        result = adapter[:]
        expected = np.empty(100000, dtype='S10')
        for i in range(100000):
            expected[i] = 'xxx' + str(i)
        np.testing.assert_equal(expected, result)

    def test_slicing(self):
        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'uints',
                                        'u8')
        result = adapter[0:10000]
        expected = np.arange(10000, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        result = adapter[9990:10010]
        expected = np.arange(9990, 10010, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        result = adapter[10000:]
        expected = np.arange(10000, 100000, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        result = adapter[:]
        expected = np.arange(100000, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        result = adapter[0:10000:2]
        expected = np.arange(0, 10000, 2, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        result = adapter[10000:50000:2]
        expected = np.arange(10000, 50000, 2, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        result = adapter[0:10000:3]
        expected = np.arange(0, 10000, 3, dtype='u8')
        np.testing.assert_array_equal(expected, result)

    def test_start_stop_keys(self):
        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'uints',
                                        'u8')
        adapter.start_key = 'row000010'
        result = adapter[:]
        expected = np.arange(10, 100000, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        adapter.start_key_inclusive = False
        result = adapter[:]
        expected = np.arange(11, 100000, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        adapter.start_key = None
        adapter.stop_key = 'row000020'
        result = adapter[:]
        expected = np.arange(20, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        adapter.stop_key_inclusive = True
        result = adapter[:]
        expected = np.arange(21, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        adapter.start_key = 'row000010'
        adapter.stop_key = 'row000020'
        adapter.start_key_inclusive = True
        adapter.stop_key_inclusive = False
        result = adapter[:]
        expected = np.arange(10, 20, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        adapter.start_key = 'row000010'
        adapter.stop_key = 'row000015'
        result = adapter[0:10]
        expected = np.arange(10, 15, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        adapter.start_key = 'row000010'
        adapter.stop_key = 'row000020'
        result = adapter[5:20]
        expected = np.arange(15, 20, dtype='u8')
        np.testing.assert_array_equal(expected, result)

        adapter.start_key = 'row000010'
        adapter.start_key_inclusive = False
        adapter.stop_key = 'row000020'
        adapter.stop_key_inclusive = True
        result = adapter[:]
        expected = np.arange(11, 21, dtype='u8')
        np.testing.assert_array_equal(expected, result)

    def test_missing_data(self):
        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'missing_data',
                                        'u8')
        adapter.missing_values = ['NA', 'nan']
        adapter.fill_value = 999
        result = adapter[:]
        expected = np.arange(12, dtype='u8')
        expected[expected % 2 == 0] = 999
        expected[expected % 3 == 0] = 999
        np.testing.assert_array_equal(expected, result)

        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'missing_data',
                                        'f8')
        adapter.missing_values = ['NA', 'nan']
        adapter.fill_value = np.NaN
        result = adapter[:]
        expected = np.array([np.NaN, 1.0, np.NaN, np.NaN, np.NaN, 5.0,
                             np.NaN, 7.0, np.NaN, np.NaN, np.NaN, 11.0], dtype='f8')
        np.testing.assert_array_equal(expected, result)

        adapter = iopro.AccumuloAdapter(TestAccumulo.hostname,
                                        TestAccumulo.port,
                                        TestAccumulo.username,
                                        TestAccumulo.password,
                                        'missing_data',
                                        'S10')
        adapter.missing_values = None
        adapter.fill_value = None
        result = adapter[:]
        expected = np.array(['NA', '000001', 'NA', 'nan', 'NA', '000005', 'NA',
                             '000007', 'NA', 'nan', 'NA', '000011'], dtype='S10')
        np.testing.assert_array_equal(expected, result)

def run(verbosity=2):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAccumulo)
    return unittest.TextTestRunner(verbosity=verbosity).run(suite)

if __name__ == '__main__':
    run()
