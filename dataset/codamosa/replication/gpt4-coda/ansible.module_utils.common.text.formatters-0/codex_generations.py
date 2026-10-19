

# Generated at 2024-03-18 01:11:37.910646
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='K') == 2097152

    # Test with units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176

    # Test with bits
    assert human_to

# Generated at 2024-03-18 01:11:42.632743
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024

    # Test with different units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776

    # Test with lowercase units
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1m') == 1048576
    assert human_to_bytes('1g') == 1073741824
    assert human_to_bytes('1t') == 1099511627776

    # Test with decimal values
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 262144

# Generated at 2024-03-18 01:11:46.833398
# Unit test for function human_to_bytes
def test_human_to_bytes():import pytest


# Generated at 2024-03-18 01:11:51.969472
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'G') == 10737418240

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to

# Generated at 2024-03-18 01:11:58.305200
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to_bytes('1M', isbits=True) == 1048576

    # Test with default unit
    assert human_to_bytes(10, default_unit='K') == 10240

# Generated at 2024-03-18 01:12:04.345182
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'G') == 10737418240

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to

# Generated at 2024-03-18 01:12:08.824156
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with default unit
    assert human_to_bytes('10', 'K') == 10240
    assert human_to_bytes('5', 'M') == 5242880

    # Test with unit in string
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('3M') == 3145728

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    # Test with floating point
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5G') == 2684354560



# Generated at 2024-03-18 01:12:13.652470
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('5', default_unit='M') == 5242880

    # Test with bits
    assert human_to_bytes('1', isbits=True) == 1
    assert human_to_bytes('1024', isbits=True) == 1024
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    # Test with bytes
    assert human_to_bytes('1B') == 1
    assert human_to_bytes('1KB') == 1024

# Generated at 2024-03-18 01:12:18.167492
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:12:41.439547
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024

    # Test with different units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with lowercase units
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1m') == 1048576
    assert human_to_bytes('1g') == 1073741824

    # Test with float values
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240

    # Test with bits
   

# Generated at 2024-03-18 01:12:52.823039
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:12:58.840693
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:13:07.880288
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:13:14.211903
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:13:21.565306
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='K') == 2097152

    # Test with unit
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2M') == 2097152
    assert human_to_bytes('1G') == 1073741824

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    # Test with floating point
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with invalid input

# Generated at 2024-03-18 01:13:26.762369
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:13:34.020515
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:13:41.978866
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='K') == 2097152

    # Test with units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176

    # Test with bits
    assert human_to

# Generated at 2024-03-18 01:13:47.696919
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:13:54.705320
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:14:04.198858
# Unit test for function human_to_bytes
def test_human_to_bytes():import pytest


# Generated at 2024-03-18 01:14:16.880272
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'G') == 10737418240

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human

# Generated at 2024-03-18 01:14:22.855276
# Unit test for function bytes_to_human
def test_bytes_to_human():    # Test with bytes
    assert bytes_to_human(0) == '0.00 Bytes'
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1048576) == '1.00 MB'
    assert bytes_to_human(1073741824) == '1.00 GB'
    assert bytes_to_human(1099511627776) == '1.00 TB'
    assert bytes_to_human(1125899906842624) == '1.00 PB'
    assert bytes_to_human(1152921504606846976) == '1.00 EB'
    assert bytes_to_human(1180591620717411303424) == '1.00 ZB'
    assert bytes_to_human(1208925819614629174706176) == '1.00 YB'

    # Test

# Generated at 2024-03-18 01:14:28.796295
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:14:36.314880
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:14:42.825363
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to_bytes('1M', isbits=True) == 1048576

    # Test with default unit
    assert human_to_bytes(10, default_unit='K') == 10240

# Generated at 2024-03-18 01:14:47.741741
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:14:55.569617
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='K') == 2097152

    # Test with units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176

    # Test with bits
    assert human_to

# Generated at 2024-03-18 01:15:02.844362
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='K') == 2097152

    # Test with units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176

    # Test with bits
    assert human_to

# Generated at 2024-03-18 01:15:09.108686
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:15:31.486591
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:15:36.729717
# Unit test for function human_to_bytes
def test_human_to_bytes():import pytest


# Generated at 2024-03-18 01:15:43.145024
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:15:47.788147
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:15:53.763022
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:15:59.880993
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='B') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    # Test with float
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5Gb') == 2684354560

    # Test with invalid input

# Generated at 2024-03-18 01:16:06.622295
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:16:11.773443
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:16:18.558581
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:16:26.071309
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:16:41.722244
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to_bytes('1M', isbits=True) == 1048576

    # Test with default unit
    assert human_to_bytes(10, default_unit='K') == 10240

# Generated at 2024-03-18 01:16:50.053385
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:16:54.909078
# Unit test for function human_to_bytes
def test_human_to_bytes():import pytest


# Generated at 2024-03-18 01:17:01.284853
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'G') == 10737418240

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to

# Generated at 2024-03-18 01:17:09.670479
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='K') == 2097152

    # Test with unit
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2M') == 2097152
    assert human_to_bytes('1G') == 1073741824

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    # Test with floating point
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with invalid input

# Generated at 2024-03-18 01:17:16.520190
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes

# Generated at 2024-03-18 01:17:23.601758
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:17:29.324226
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:17:34.962503
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:17:41.372817
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:18:09.477798
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024

    # Test with different units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776

    # Test with float values
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human

# Generated at 2024-03-18 01:18:15.368858
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:18:22.641754
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:18:27.208013
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:18:32.212688
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'G') == 10737418240

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to

# Generated at 2024-03-18 01:18:37.458025
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:18:42.782508
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024

    # Test with different units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776

    # Test with lowercase units
    assert human_to_bytes('1k') == 1024
    assert human_to_bytes('1m') == 1048576
    assert human_to_bytes('1g') == 1073741824
    assert human_to_bytes('1t') == 1099511627776

    # Test with float values
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 262144

# Generated at 2024-03-18 01:18:50.260005
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'G') == 10737418240

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human

# Generated at 2024-03-18 01:18:55.328950
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:19:01.967589
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:19:33.292661
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to_bytes('1M', isbits=True) == 1048576

    # Test with default unit
    assert human_to_bytes(10, default_unit='K') == 10240

# Generated at 2024-03-18 01:19:41.032501
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048', default_unit='K') == 2097152

    # Test with unit
    assert human_to_bytes('2K') == 2048
    assert human_to_bytes('2M') == 2097152
    assert human_to_bytes('1G') == 1073741824

    # Test with bits
    assert human_to_bytes('1Kb', isbits=True) == 1024
    assert human_to_bytes('1Mb', isbits=True) == 1048576

    # Test with float
    assert human_to_bytes('1.5K') == 1536

    # Test with invalid input
    try:
        human_to_bytes('2X')
        assert False, "Should raise ValueError for invalid unit"
    except ValueError:
        pass


# Generated at 2024-03-18 01:19:45.308982
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:19:52.266907
# Unit test for function human_to_bytes
def test_human_to_bytes():import pytest


# Generated at 2024-03-18 01:19:57.215973
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:20:03.772607
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']

# Generated at 2024-03-18 01:20:08.378556
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes('10', default_unit='K') == 10240
    assert human_to_bytes('10', default_unit='M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:20:13.559025
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024

    # Test with different units
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824
    assert human_to_bytes('1T') == 1099511627776
    assert human_to_bytes('1P') == 1125899906842624
    assert human_to_bytes('1E') == 1152921504606846976
    assert human_to_bytes('1Z') == 1180591620717411303424
    assert human_to_bytes('1Y') == 1208925819614629174706176

    # Test with lowercase units
    assert human_to_bytes('1k') == 1024

# Generated at 2024-03-18 01:20:20.986639
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'M') == 10485760
    assert human_to_bytes(10, 'G') == 10737418240

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to

# Generated at 2024-03-18 01:20:27.147356
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with default unit
    assert human_to_bytes(10, 'K') == 10240
    assert human_to_bytes(10, 'M') == 10485760

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024

# Generated at 2024-03-18 01:21:21.303884
# Unit test for function human_to_bytes
def test_human_to_bytes():    # Test with no unit
    assert human_to_bytes('1024') == 1024
    assert human_to_bytes('2048') == 2048

    # Test with unit
    assert human_to_bytes('1K') == 1024
    assert human_to_bytes('1M') == 1048576
    assert human_to_bytes('1G') == 1073741824

    # Test with unit and decimal
    assert human_to_bytes('1.5K') == 1536
    assert human_to_bytes('2.5M') == 2621440

    # Test with bits
    assert human_to_bytes('1K', isbits=True) == 1024
    assert human_to_bytes('1M', isbits=True) == 1048576

    # Test with default unit
    assert human_to_bytes(10, default_unit='K') == 10240

# Generated at 2024-03-18 01:21:37.644949
# Unit test for function lenient_lowercase
def test_lenient_lowercase():    assert lenient_lowercase(['A', 'B', 'C']) == ['a', 'b', 'c']