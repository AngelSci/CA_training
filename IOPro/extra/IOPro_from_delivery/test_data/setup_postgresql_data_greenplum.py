import psycopg2
import numpy as np
import string

CASTS_TEST_NUM_RECORDS = 23456

if __name__ == '__main__':
    conn = psycopg2.connect('host=localhost dbname=postgres user=jayvius')
    conn.set_isolation_level(0)
    cursor = conn.cursor()
    cursor.execute('create database unit_tests')
    conn.set_isolation_level(1)
    conn.close()

    conn = psycopg2.connect('host=localhost dbname=unit_tests user=jayvius')

    cursor = conn.cursor()

    cursor.execute('create table ints_test (int2 smallint, int4 integer, int8 bigint)')
    cmd = 'insert into ints_test (int2, int4, int8) values ({0}, {1}, {2})'
    cursor.execute(cmd.format(np.iinfo(np.int16).min, np.iinfo(np.int32).min, np.iinfo(np.int64).min))
    cursor.execute(cmd.format(0, 0, 0))
    cursor.execute(cmd.format(np.iinfo(np.int16).max, np.iinfo(np.int32).max, np.iinfo(np.int64).max))

    cursor.execute('create table floats_test (float4 real, float8 double precision)')
    cmd = 'insert into floats_test (float4, float8) values ({0}, {1})'
    cursor.execute(cmd.format(np.finfo(np.float32).min, np.finfo(np.float64).min))
    cursor.execute(cmd.format(0.0, 0.0))
    cursor.execute(cmd.format(-1.1, 1.1))

    cursor.execute('create table numeric_test (numeric1 numeric(20, 10), numeric2 decimal(20, 10))')
    cmd = 'insert into numeric_test (numeric1, numeric2) values ({0}, {1})'
    cursor.execute(cmd.format(1234567890.0123456789, 1234567890.0123456789))

    cursor.execute('create table fixed_strings_test (fixed char(10))')
    cmd = "insert into fixed_strings_test (fixed) values ('{0}')"
    cursor.execute(cmd.format('aaa'))
    cursor.execute(cmd.format('bbb'))
    cursor.execute(cmd.format('ccc'))

    cursor.execute('create table var_strings_test (varchar varchar(10), text text)')
    cmd = "insert into var_strings_test (varchar, text) values ('{0}', '{1}')"
    cursor.execute(cmd.format('aaa', string.ascii_lowercase))
    cursor.execute(cmd.format('bbb', string.ascii_uppercase))
    cursor.execute(cmd.format('ccc', string.ascii_letters))

    cursor.execute('create table unicode_strings_test (fixed char(10), text text)')
    cursor.execute(u"insert into unicode_strings_test (fixed, text) values ('\u4242xxx', 'xxx\u4242')")

    cursor.execute(u'create table unicode_table_name_test (name\u4242 text)')
    cursor.execute(u"insert into unicode_table_name_test (name\u4242) values ('foo')")

    cursor.execute('create table casts_test (char char(10), int4 int4, float8 double precision)')
    cmd = "insert into casts_test (char, int4, float8) values ('{0}', {0}, {0}.{0})"
    for i in range(CASTS_TEST_NUM_RECORDS):
        cursor.execute(cmd.format(i))

    cursor.execute('create table missing_values_test (char char(5), int4 int4, float4 real, '
                 'point point, path path, polygon polygon)')

    cursor.execute('insert into missing_values_test default values')

    cursor.execute('create table empty_test (dummy int4)')

    conn.commit()
    cursor.close()
    conn.close()
