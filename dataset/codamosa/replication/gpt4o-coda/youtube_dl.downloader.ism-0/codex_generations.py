

# Generated at 2024-06-04 22:06:57.430549
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:07:01.062099
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:07:05.026271
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:07:06.480670
# Unit test for constructor of class IsmFD
def test_IsmFD():    ism_fd = IsmFD()

# Generated at 2024-06-04 22:07:09.705859
# Unit test for function write_piff_header

# Generated at 2024-06-04 22:07:11.688097
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:07:14.849018
# Unit test for function write_piff_header

# Generated at 2024-06-04 22:07:19.627800
# Unit test for function write_piff_header

# Generated at 2024-06-04 22:07:23.368551
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    ismfd = IsmFD()

# Generated at 2024-06-04 22:07:27.008679
# Unit test for function extract_box_data
def test_extract_box_data():    # Test data
    test_data = (
        u32.pack(32) + b'ftyp' + b'isml' + u32.pack(1) + b'piff' + b'iso2' +  # ftyp box
        u32.pack(24) + b'moov' +  # moov box
        u32.pack(16) + b'trak' + b'testtrak'  # trak box inside moov
    )

    # Test case 1: Extract 'ftyp' box
    result = extract_box_data(test_data, [b'ftyp'])
    assert result == b'isml' + u32.pack(1) + b'piff' + b'iso2', f"Expected 'ftyp' box data, got {result}"

    # Test case 2: Extract 'moov' -> 'trak' box

# Generated at 2024-06-04 22:07:41.572031
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:07:45.713793
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:07:46.802316
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:07:50.337407
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:07:53.386996
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:07:56.731019
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:07:57.633421
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:08:01.721974
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:08:02.635993
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:08:07.626768
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:08:31.054440
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:08:34.980747
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:08:38.028038
# Unit test for function write_piff_header

# Generated at 2024-06-04 22:08:41.732220
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:08:42.781045
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:08:46.477209
# Unit test for function extract_box_data
def test_extract_box_data():    data = (
        u32.pack(16) + b'ftyp' + b'isml' + u32.pack(1) + b'piff' + b'iso2' +
        u32.pack(24) + b'moov' + u32.pack(16) + b'mvhd' + b'\x00' * 8 +
        u32.pack(16) + b'trak' + u32.pack(8) + b'tkhd' + b'\x00' * 8
    )

# Generated at 2024-06-04 22:08:50.097972
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:08:53.063892
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:08:53.988342
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:08:57.346349
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:09:39.417837
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:09:42.878193
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:09:48.244552
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:09:51.609471
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:09:54.838099
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:10:00.454361
# Unit test for function write_piff_header

# Generated at 2024-06-04 22:10:01.314903
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:10:06.804097
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:10:09.804234
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:10:12.740430
# Unit test for function extract_box_data
def test_extract_box_data():    # Test case 1: Extracting a single box
    data = box(b'test', b'1234')
    assert extract_box_data(data, [b'test']) == b'1234'

    # Test case 2: Extracting a nested box
    nested_data = box(b'outer', box(b'inner', b'5678'))
    assert extract_box_data(nested_data, [b'outer', b'inner']) == b'5678'

    # Test case 3: Extracting a deeply nested box
    deep_nested_data = box(b'level1', box(b'level2', box(b'level3', b'91011')))
    assert extract_box_data(deep_nested_data, [b'level1', b'level2', b'level3']) == b'91011'

    # Test case 4: Box not found

# Generated at 2024-06-04 22:10:56.258153
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:10:59.696842
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:11:03.370655
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:11:06.481049
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:11:09.705176
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:11:12.822849
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:11:16.271827
# Unit test for function write_piff_header

# Generated at 2024-06-04 22:11:19.596119
# Unit test for function write_piff_header

# Generated at 2024-06-04 22:11:21.522705
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:11:25.029870
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:12:59.384206
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:13:00.449554
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:13:04.358787
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:13:07.820705
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:13:08.577309
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD(None, None)

# Generated at 2024-06-04 22:13:13.513530
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    ismfd = IsmFD()

# Generated at 2024-06-04 22:13:14.463730
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:13:15.679068
# Unit test for constructor of class IsmFD
def test_IsmFD():    ismfd = IsmFD()

# Generated at 2024-06-04 22:13:18.770191
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:13:22.388172
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():    import io

# Generated at 2024-06-04 22:16:40.427079
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()

# Generated at 2024-06-04 22:16:44.397735
# Unit test for function write_piff_header
def test_write_piff_header():    stream = io.BytesIO()