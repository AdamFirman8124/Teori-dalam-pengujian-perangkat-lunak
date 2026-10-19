

# Generated at 2024-06-04 21:26:59.284067
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x02'  # quality_entry_count
        b'quality1\x00'
        b'quality2\x00'
        b'\x00\x00\x00\x02'  # segment_run_count
        b'\x00\x00\x00\x01'  # first_segment
        b'\x00\x00\x00\x05'  # fragments_per_segment
        b'\x00\x00\x00\x02'  # first_segment
        b'\x00\x00\x00\x03'  # fragments_per_segment
    )

# Generated at 2024-06-04 21:27:02.915185
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2024-06-04 21:27:04.256089
# Unit test for function write_flv_header
def test_write_flv_header():    stream = io.BytesIO()

# Generated at 2024-06-04 21:27:08.911447
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x02'  # quality_entry_count
        b'quality1\x00'
        b'quality2\x00'
        b'\x00\x00\x00\x02'  # segment_run_count
        b'\x00\x00\x00\x01'  # first_segment
        b'\x00\x00\x00\x05'  # fragments_per_segment
        b'\x00\x00\x00\x02'  # first_segment
        b'\x00\x00\x00\x03'  # fragments_per_segment
    )

# Generated at 2024-06-04 21:27:11.176833
# Unit test for constructor of class F4mFD
def test_F4mFD():    f4mfd = F4mFD()

# Generated at 2024-06-04 21:27:14.511731
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():    import io

# Generated at 2024-06-04 21:27:15.774096
# Unit test for function write_flv_header
def test_write_flv_header():    stream = io.BytesIO()

# Generated at 2024-06-04 21:27:19.243018
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:27:23.090360
# Unit test for function get_base_url
def test_get_base_url():    manifest_with_base_url = compat_etree_fromstring('''
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
            <baseURL>http://example.com/</baseURL>
        </manifest>
    ''')

# Generated at 2024-06-04 21:27:27.559310
# Unit test for function build_fragments_list
def test_build_fragments_list():    boot_info = {
        'segments': [{'segment_run': [(1, 3), (2, 2)]}],
        'fragments': [{'fragments': [
            {'first': 1, 'ts': 0, 'duration': 1000, 'discontinuity_indicator': None},
            {'first': 4, 'ts': 3000, 'duration': 1000, 'discontinuity_indicator': None}
        ]}],
        'live': False
    }

# Generated at 2024-06-04 21:28:16.967671
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x00\x00\x00\x01'  # time scale
        b'\x01'  # quality entry count
        b'quality\x00'  # quality segment url modifier
        b'\x00\x00\x00\x01'  # fragments count
        b'\x00\x00\x00\x01'  # first
        b'\x00\x00\x00\x00\x00\x00\x00\x01'  # first_ts
        b'\x00\x00\x00\x02'  # duration
        b'\x00'  # discontinuity indicator
    )

# Generated at 2024-06-04 21:28:21.180437
# Unit test for function get_base_url
def test_get_base_url():    from xml.etree.ElementTree import Element

    # Test case 1: Base URL present in version 1.0 namespace

# Generated at 2024-06-04 21:28:25.575789
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():    import io

# Generated at 2024-06-04 21:28:26.596970
# Unit test for constructor of class F4mFD
def test_F4mFD():    f4mfd = F4mFD()

# Generated at 2024-06-04 21:28:30.318205
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x00\x00\x00\x01'  # time scale
        b'\x01'  # quality entry count
        b'quality\x00'  # quality segment url modifier
        b'\x00\x00\x00\x01'  # fragments count
        b'\x00\x00\x00\x01'  # first
        b'\x00\x00\x00\x00\x00\x00\x00\x01'  # first_ts
        b'\x00\x00\x00\x01'  # duration
    )

# Generated at 2024-06-04 21:28:35.254518
# Unit test for function get_base_url
def test_get_base_url():    from xml.etree.ElementTree import Element

    # Test case 1: Base URL present in version 1.0 namespace

# Generated at 2024-06-04 21:28:39.672887
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x02'  # quality_entry_count
        b'quality1\x00'
        b'quality2\x00'
        b'\x00\x00\x00\x02'  # segment_run_count
        b'\x00\x00\x00\x01'  # first_segment
        b'\x00\x00\x00\x05'  # fragments_per_segment
        b'\x00\x00\x00\x02'  # first_segment
        b'\x00\x00\x00\x03'  # fragments_per_segment
    )

# Generated at 2024-06-04 21:28:40.737582
# Unit test for constructor of class F4mFD
def test_F4mFD():    downloader = F4mFD()

# Generated at 2024-06-04 21:28:45.490187
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:28:49.375744
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():    import io

# Generated at 2024-06-04 21:31:17.838523
# Unit test for function get_base_url
def test_get_base_url():    from xml.etree.ElementTree import Element

    # Test case 1: Base URL present in version 1.0 namespace

# Generated at 2024-06-04 21:31:21.971053
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:31:25.762676
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:31:30.216266
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():    import io

# Generated at 2024-06-04 21:31:32.302409
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():    data = (
        b'\x00\x00\x00\x10'  # size = 16
        b'test'              # type = 'test'
        b'\x01\x02\x03\x04\x05\x06\x07\x08'  # data
    )

# Generated at 2024-06-04 21:31:35.939483
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:31:40.372099
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:31:43.466213
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():    from xml.etree.ElementTree import Element

    # Test case 1: No encrypted media

# Generated at 2024-06-04 21:31:48.692863
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():    import io

# Generated at 2024-06-04 21:31:52.262536
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x00\x00\x00\x01'  # time scale
        b'\x01'  # quality entry count
        b'quality_entry\x00'  # quality segment URL modifier
        b'\x00\x00\x00\x01'  # fragments count
        b'\x00\x00\x00\x01'  # first
        b'\x00\x00\x00\x00\x00\x00\x00\x01'  # first_ts
        b'\x00\x00\x00\x01'  # duration
    )

# Generated at 2024-06-04 21:33:11.886196
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x02'  # quality_entry_count
        b'quality1\x00'
        b'quality2\x00'
        b'\x00\x00\x00\x02'  # segment_run_count
        b'\x00\x00\x00\x01'  # first_segment
        b'\x00\x00\x00\x05'  # fragments_per_segment
        b'\x00\x00\x00\x02'  # first_segment
        b'\x00\x00\x00\x03'  # fragments_per_segment
    )

# Generated at 2024-06-04 21:33:15.500890
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():    data = (
        b'\x00\x00\x00\x10'  # size = 16
        b'test'              # type = 'test'
        b'\x01\x02\x03\x04\x05\x06\x07\x08'  # data
    )

# Generated at 2024-06-04 21:33:20.474515
# Unit test for function get_base_url
def test_get_base_url():    from xml.etree.ElementTree import Element

    # Test case 1: Base URL present in version 1.0 namespace

# Generated at 2024-06-04 21:33:24.786446
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:33:28.839657
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():    data = (
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x00\x00\x00\x01'  # time scale
        b'\x01'  # quality entry count
        b'quality_entry\x00'  # quality segment URL modifier
        b'\x00\x00\x00\x01'  # fragments count
        b'\x00\x00\x00\x01'  # first
        b'\x00\x00\x00\x00\x00\x00\x00\x01'  # first_ts
        b'\x00\x00\x00\x01'  # duration
    )

# Generated at 2024-06-04 21:33:32.480534
# Unit test for function build_fragments_list
def test_build_fragments_list():    boot_info = {
        'segments': [{'segment_run': [(1, 3), (2, 2)]}],
        'fragments': [{'fragments': [
            {'first': 1, 'ts': 0, 'duration': 1000, 'discontinuity_indicator': None},
            {'first': 4, 'ts': 3000, 'duration': 1000, 'discontinuity_indicator': None}
        ]}],
        'live': False
    }

# Generated at 2024-06-04 21:33:35.991284
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:33:39.940840
# Unit test for method read_abst of class FlvReader

# Generated at 2024-06-04 21:33:43.211025
# Unit test for function build_fragments_list
def test_build_fragments_list():    boot_info = {
        'segments': [{'segment_run': [(1, 3), (2, 2)]}],
        'fragments': [{'fragments': [
            {'first': 1, 'ts': 0, 'duration': 1000, 'discontinuity_indicator': None},
            {'first': 4, 'ts': 3000, 'duration': 1000, 'discontinuity_indicator': None}
        ]}],
        'live': False
    }

# Generated at 2024-06-04 21:33:47.435581
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():    import io