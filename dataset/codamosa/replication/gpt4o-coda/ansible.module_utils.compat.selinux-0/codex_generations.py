

# Generated at 2024-05-31 01:32:28.614933
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = "/path/to/file"

# Generated at 2024-05-31 01:32:30.649361
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:32.707704
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:34.875708
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = "/path/to/file"

# Generated at 2024-05-31 01:32:37.261448
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:39.348352
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:42.432101
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:44.637046
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:47.999018
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:50.134151
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = to_bytes('/some/test/path')

# Generated at 2024-05-31 01:32:54.704342
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:56.540681
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:32:59.668816
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:01.754585
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:07.402427
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:11.726991
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'

# Generated at 2024-05-31 01:33:14.678681
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:17.806002
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:19.793077
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:23.597458
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_result = [0, 'system_u:object_r:default_t:s0']

# Generated at 2024-05-31 01:33:32.468166
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:35.526961
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:39.384774
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'
    _selinux_lib.lgetfilecon_raw = lambda path, con: (con.__setitem__(0, c_char_p(to_bytes(expected_context))), 0)[1]
    result = lgetfilecon_raw(path)
    assert result == [0, expected_context], f"Expected [0, '{expected_context}'], got {result}"

    # Test

# Generated at 2024-05-31 01:33:42.577512
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a sample path
    path = "/some/path"
    expected_result = [0, None]
    result = lgetfilecon_raw(path)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    # Restore the original functions
    _selinux_lib.lgetfilecon_raw = original_lgetfilecon_raw
    _selinux_lib.freecon = original_freecon


# Generated at 2024-05-31 01:33:44.521672
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:46.584544
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = to_bytes('/path/to/file')

# Generated at 2024-05-31 01:33:49.522619
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:51.694514
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:33:53.588312
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = to_bytes('/path/to/file')

# Generated at 2024-05-31 01:33:57.814984
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'

# Generated at 2024-05-31 01:34:11.200450
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:34:13.100817
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:34:15.032524
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = "/path/to/file"

# Generated at 2024-05-31 01:34:19.496666
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'

# Generated at 2024-05-31 01:34:21.304340
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:34:24.542860
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'
    _selinux_lib.lgetfilecon_raw = lambda path, con: (con.__setitem__(0, c_char_p(to_bytes(expected_context))), 0)[1]
    result = lgetfilecon_raw(path)
    assert result == [0, expected_context], f"Expected [0, '{expected_context}'], got {result}"

    # Test

# Generated at 2024-05-31 01:34:26.289759
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:34:29.305144
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'

# Generated at 2024-05-31 01:34:33.096016
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:34:34.963338
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:34:59.120009
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'

# Generated at 2024-05-31 01:35:01.382700
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:35:03.324768
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:35:06.210541
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:35:09.299298
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    result = lgetfilecon_raw(path)
    assert result == [0, ''], f"Expected [0, ''], but got {result}"

    # Restore the original functions
    _selinux_lib.lgetfilecon_raw = original_lgetfilecon_raw
    _selinux_lib.freecon = original_freecon


# Generated at 2024-05-31 01:35:11.423766
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:35:14.630639
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'
    _selinux_lib.lgetfilecon_raw = lambda path, con: (con.__setattr__('value', to_bytes(expected_context)), 0)[1]
    result = lgetfilecon_raw(path)
    assert result == [0, expected_context], f"Expected [0, '{expected_context}'], got {result}"

    # Test with an invalid

# Generated at 2024-05-31 01:35:17.562303
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:35:20.788680
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test path
    test_path = b'/test/path'

    # Expected result
    expected_result = [0, 'mocked_context']

    # Mock the c_char_p value
    con = c_char_p(b'mocked_context')

    # Call the function
    result = lgetfilecon_raw(test_path)

    # Check the result
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    # Restore the original functions
    _selinux_lib.lgetfile

# Generated at 2024-05-31 01:35:24.701862
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:36:09.093720
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:36:11.133984
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = to_bytes('/path/to/file')

# Generated at 2024-05-31 01:36:13.533729
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = "/path/to/file"

# Generated at 2024-05-31 01:36:15.847384
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:36:19.152071
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = "/path/to/file"

# Generated at 2024-05-31 01:36:21.134464
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:36:24.330221
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:36:28.548861
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'

# Generated at 2024-05-31 01:36:31.514584
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_result = [0, 'system_u:object_r:default_t:s0']

# Generated at 2024-05-31 01:36:34.658016
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:02.267099
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:03.968476
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:05.937801
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:07.840976
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:11.048970
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    result = lgetfilecon_raw(path)
    assert result == [0, ''], f"Expected [0, ''], but got {result}"

    # Restore the original functions
    _selinux_lib.lgetfilecon_raw = original_lgetfilecon_raw
    _selinux_lib.freecon = original_freecon


# Generated at 2024-05-31 01:38:13.037881
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:14.815644
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:18.514044
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    expected_context = 'system_u:object_r:default_t:s0'
    _selinux_lib.lgetfilecon_raw = lambda path, con: (con.__setitem__(0, c_char_p(to_bytes(expected_context))), 0)[1]
    result = lgetfilecon_raw(path)
    assert result == [0, expected_context], f"Expected [0, '{expected_context}'], got {result}"

    # Test

# Generated at 2024-05-31 01:38:22.653362
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:38:26.392438
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a valid path
    path = to_bytes('/valid/path')
    result = lgetfilecon_raw(path)
    assert result == [0, ''], f"Expected [0, ''], but got {result}"

    # Restore the original functions
    _selinux_lib.lgetfilecon_raw = original_lgetfilecon_raw
    _selinux_lib.freecon = original_freecon


# Generated at 2024-05-31 01:41:18.957128
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = "/path/to/file"

# Generated at 2024-05-31 01:41:20.951746
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:41:24.650666
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    # Mock the _selinux_lib.lgetfilecon_raw function
    original_lgetfilecon_raw = _selinux_lib.lgetfilecon_raw
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0

    # Mock the _selinux_lib.freecon function
    original_freecon = _selinux_lib.freecon
    _selinux_lib.freecon = lambda con: None

    # Test with a sample path
    path = b'/some/path'
    expected_result = [0, 'mocked_context']
    
    # Mock the to_native function to return a fixed value
    original_to_native = to_native
    to_native = lambda x: 'mocked_context'

    result = lgetfilecon_raw(path)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    # Restore the original functions
    _selinux_lib.lgetfilecon_raw

# Generated at 2024-05-31 01:41:26.570945
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():    path = to_bytes('/path/to/file')

# Generated at 2024-05-31 01:41:33.920307
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:41:35.907255
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:41:39.672977
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:41:42.142239
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:41:44.368716
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"

# Generated at 2024-05-31 01:41:48.225193
# Unit test for function matchpathcon
def test_matchpathcon():    path = "/etc/passwd"