

# Generated at 2022-06-14 18:09:11.600729
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO Add unit tests
    from .common import FileDownloader  # pylint: disable=protected-access
    from .common import MockedFileDownloader  # pylint: disable=protected-access
    from .common import PostProcessingError  # pylint: disable=protected-access
    from .dash import DASHDownloader  # pylint: disable=protected-access
    from .dash import DASHIE_MP4_VIDEO_HIGH_DASH_Template
    from .dash import DASHIE_MP4_VIDEO_LOW_DASH_Template
    from .dash import DASHIE_MP4_VIDEO_LOW_DASH_WIDEVINE_Template
    from .dash import DASHIE_WEBM_VIDEO_HIGH_DASH_Template
    from .dash import DASHIE_WEBM_VIDEO_

# Generated at 2022-06-14 18:09:14.536773
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:09:19.063892
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP("test")
    assert isinstance(x, XAttrMetadataPP)
    assert x.name == "test"

# Generated at 2022-06-14 18:09:28.381478
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """ Unit test for method run of class XAttrMetadataPP
    
        This test only tests whether an exception is raised (run() returns normally in this case)
        or not. Testing if xattrs have been correctly set is not possible because xattr support is
        not available on all platforms.
    """
    
    import os
    xattr_available = True
    try:
        import xattr
    except ImportError:
        xattr_available = False

    def fake_run_downloader():
        pass
    
    def fake_to_screen(txt):
        print(txt)
    
    def fake_report_warning(txt):
        print('WARNING: ' + txt)
    
    def fake_report_error(txt):
        print('ERROR: ' + txt)
    
    fake_filepath = os.path

# Generated at 2022-06-14 18:09:32.181847
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    test_instance = XAttrMetadataPP()
    assert isinstance(test_instance, PostProcessor)


# Generated at 2022-06-14 18:09:42.724391
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import InfoExtractor
    from .common import PostProcessor
    import unittest
    import sys
    import os
    import tempfile
    from ..utils import write_xattr

    # Temporary file to hold the video
    filename = tempfile.mkstemp()[1]
    # Meaningless data to be written on `filename`
    byte_value = b'variable byte value'

    # Extractor to retrieve metadata

# Generated at 2022-06-14 18:09:44.826390
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from youtube_dl import downloader

    pp = XAttrMetadataPP(downloader)

    assert pp != None


# Generated at 2022-06-14 18:09:46.216788
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP._get_supported_subtitles("none") is None

# Generated at 2022-06-14 18:09:47.769812
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    return XAttrMetadataPP('test_XAttrMetadataPP')

# Generated at 2022-06-14 18:09:51.360421
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    success = True
        # Create an instance of XAttrMetadataPP class
    instance = XAttrMetadataPP("scrapinghub.yml")
    # Check parameters of init function
    if instance.filepath != "scrapinghub.yml":
        success = False
    return success


# Generated at 2022-06-14 18:09:59.829409
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    ytdl = XAttrMetadataPP()
    assert (ytdl.available() is True)


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:06.636240
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Calling XAttrMetadataPP() should raise an exception on non-Unix-like systems,
    None otherwise.
    """
    if compat_os_name == 'nt':
        # Windows system
        import pytest
        with pytest.raises(EnvironmentError):
            XAttrMetadataPP()
        return
    elif compat_os_name == 'mac':
        # MacOS system
        from .mac_metadata import XAttrMetadataPP
        import pytest
        with pytest.raises(EnvironmentError):
            XAttrMetadataPP()
        return
    # Unix system
    XAttrMetadataPP()

# Generated at 2022-06-14 18:10:07.981280
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


# Generated at 2022-06-14 18:10:18.086364
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os

    # We don't need any info to set xattrs
    info = {
        'id': 'abc',
        'ext': 'mp4',
        'title': 'a title',
        'description': 'a description',
        'uploader': 'an uploader',
        'upload_date': '20150101',
        'webpage_url': 'http://www.youtube.com/watch?v=abc',
        'format': 'mp4',
        'format_id': 'mp4',
        'thumbnail': 'http://img.youtube.com/vi/abc/abc.jpg',
        'duration': 10,
    }
    # We need a fake filename
    filename = '/tmp/test-file'
    # We need the XAttrMetadataPP singleton instance
    from .common import postprocessors

# Generated at 2022-06-14 18:10:27.468119
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import tempfile
    import os
    from ..utils import compat_str
    from .common import FileDownloader
    from .external import ExternalFD

    def temp_fd(filename, mode):
        return open(os.path.join(temp_dir, filename), mode)

    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-14 18:10:38.843348
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import sys
    sys.path.append('../../')

    from ydl.downloader import YoutubeDL

    info_dict = {
        'id': 'Q0sT4f4Gj4w',
        'webpage_url': 'https://www.youtube.com/watch?v=Q0sT4f4Gj4w',
        'title': 'Spooky Scary Skeletons',
        'upload_date': '19961231',
        'description': 'Just dance!',
        'uploader': 'Andrew Gold',
        'format': 'MP4',
        'url': 'http://google.com/videos.mp4',
    }

    def reported_warnings(obj):
        return '\n'.join(obj.report_warnings)


# Generated at 2022-06-14 18:10:41.881804
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    assert True

# Generated at 2022-06-14 18:10:44.580494
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    XAttrMetadataPP(None).run({'filepath': ''})

if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-14 18:10:45.594859
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    return XAttrMetadataPP

# Generated at 2022-06-14 18:10:47.379224
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """
    Test XAttrMetadataPP constructor.
    """
    assert XAttrMetadataPP('youtube-dl')

# Generated at 2022-06-14 18:11:08.115384
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    import stat
    import youtube_dl
    from youtube_dl.utils import XAttrUnavailableError

    class FakeInfoDict(dict):
        def __init__(self, infodict={}):
            self.infodict = infodict
            self.infodict['filepath'] = tempfile.mktemp()
            dict.__init__(self, self.infodict)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            if os.path.isfile(self.infodict['filepath']):
                os.remove(self.infodict['filepath'])

    # Please note:
    # This unit test is not complete, and not enough reliable for now
    # (due

# Generated at 2022-06-14 18:11:10.674445
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..utils import check_executable

    if check_executable('xattr'):
        return XAttrMetadataPP()
    else:
        return None

# Generated at 2022-06-14 18:11:22.307588
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import encodeFilename

    # Create temp file and directory
    import os
    import tempfile
    import shutil
    from .test_common import FakeInfoExtractor
    from .test_extractor_common import TestIE

    tempdir = tempfile.mkdtemp()
    tempfilepath = os.path.join(tempdir, encodeFilename('foo.webm'))
    with open(tempfilepath, 'wb') as tempfile:
        tempfile.write(b'foo')

    # Prepare the info object

# Generated at 2022-06-14 18:11:34.801314
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import PostProcessingError
    from .common import FilePostProcessor
    from .extractaudio import ExtractAudioPP
    from .ffmpegmetadata import FFmpegMetadataPP
    from .xattrs import XAttrMetadataPP
    from ..YoutubeDL import YoutubeDL

    info = {
        'id': 'abc',
        'title': 'def',
        'webpage_url': 'ghi',
        'description': 'jkl',
        'uploader': 'mno',
        'upload_date': 'pqr',
        'format': 'stu'}

    def _test_filename(filename):
        pass

    def _work(*args):
        raise PostProcessingError('postprocessing error')

    def _make_ready(*args):
        return info


# Generated at 2022-06-14 18:11:47.159807
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os.path
    from .test import (
        FakeYDL,
    )
    from .f4m import F4mPP
    from .ism import IsmPP
    from .verbose import VerbosePP
    from .xattr_pp import XAttrMetadataPP

    class FakeFile(object):
        """ Class used as a fake file to be passed to XAttrMetadataPP """

        def __init__(self, xattrs_list):
            self.xattrs_list = xattrs_list

        def getxattr(self, path, xattrname, nofollow=False):
            return self.xattrs_list[xattrname]

        def listxattr(self, path, nofollow=False):
            return list(self.xattrs_list.keys())


# Generated at 2022-06-14 18:11:58.056510
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile
    import os


# Generated at 2022-06-14 18:12:03.264299
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    class FakeInfo(object):
        def get(self, field):
            if field == 'title':
                return 'A Fake Title'
            elif field == 'format':
                return 'a fake format'
            else:
                return None

    x = XAttrMetadataPP()
    assert x.run(FakeInfo()) == ([], FakeInfo())



# Generated at 2022-06-14 18:12:15.181117
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    try:
        from .common import FileDownloader
    except ImportError:
        from youtube_dl.downloader.common import FileDownloader
    dl = FileDownloader({})
    pp = XAttrMetadataPP(dl)
    md = {
        'webpage_url': 'https://www.youtube.com/watch?v=MJo8uZ7vfH0',
        'title': 'Kedi (2016) - Full Movie [720p]',
        'description': 'Kedi is a 2016 Turkish documentary film about the street cats of Istanbul.',
        'upload_date': '20171002',
        'uploader': 'Turkey Home',
        'format': 'Video/Moving image',
    }

    # test XAttrUnavailableError
    open('/proc/version', 'a').close()  # make it unw

# Generated at 2022-06-14 18:12:26.241551
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import unittest
    import os
    import tempfile
    from .common import FileDownloader
    from ..compat import compat_os_name
    from ..utils import (
            XAttrUnavailableError,
            XAttrMetadataError,
        )
    from .test_files import (
            valid_info,
        )

    # Add xattr support on windows
    if compat_os_name == 'nt':
        import win_xattr
    else:
        win_xattr = None

    valid_info['title'] = 'This is a test ä 这是一个test'
    valid_info['format'] = 'This is a test ä 这是一个test'
    valid_info['upload_date'] = '2012-01-01'

# Generated at 2022-06-14 18:12:30.768081
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    metadata = {'title': 'Test'}
    pp = XAttrMetadataPP()
    # This test doesn't check whether extended attributes are actually written
    # to files. It only checks whether run method of XAttrMetadataPP class
    # raises any exceptions.
    pp.run(metadata)

# Generated at 2022-06-14 18:12:51.531760
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert True

# Generated at 2022-06-14 18:13:03.427718
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..downloader.common import FileDownloader
    from ..downloader.http.http import HTTPDownloader
    from ..extractor import CommonIE

    class FakeFileDownloader(FileDownloader):
        def __init__(self, params, outtmpl='', ydl=None):
            super(FakeFileDownloader, self).__init__(ydl, params)
            self.to_screen = ydl.to_screen if ydl and hasattr(ydl, 'to_screen') else print
            self.report_warning = lambda msg: self.to_screen('WARNING: %s' % msg)
            self.report_error = lambda msg: self.to_screen('ERROR: %s' % msg)


# Generated at 2022-06-14 18:13:15.108490
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    # Create a downloader
    downloader = YoutubeDL(params={'writethumbnail': True})

    # Create a XAttrMetadataPP
    pp = XAttrMetadataPP(downloader)

    # Create a video info

# Generated at 2022-06-14 18:13:24.043430
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # In Python 3, we need to create a new VideoInfo object
    # because `filepath` attribute is set by PostProcessor
    video_info = {
        'webpage_url': 'https://www.youtube.com/watch?v=BaW_jenozKc',
        'description': 'test description',
        'title': 'test title',
        'upload_date': '20010101',
        'uploader': 'test uploader',
        'format': 'test format',
    }

    video_info_bytes = video_info.copy()
    video_info_bytes['filepath'] = b'video_info.flv'

    XAttrMetadataPP(None, None).run(video_info_bytes)
    XAttrMetadataPP(None, None).run(video_info)


# Generated at 2022-06-14 18:13:26.238164
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None)

# Generated at 2022-06-14 18:13:33.856892
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader
    from ..utils import (
        determine_xattr_file_support,
        XAttrUnavailableError,
        XAttrMetadataError,
    )

    if not determine_xattr_file_support():
        raise XAttrUnavailableError('No xattr filesystem support')

    filepath = './XAttrMetadataPP_run.txt'
    fd = open(filepath, 'w')
    fd.close()

    def report_warning(msg):
        print(msg)

    def report_error(msg):
        print(msg)


# Generated at 2022-06-14 18:13:34.518428
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:13:38.095795
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ Unit tests for XAttrMetadataPP """
    from ..downloader import YoutubeDL
    # Test for VideoInfo
    ydl = YoutubeDL({})
    assert ydl.postproc is not None
    assert ydl.postproc.__class__ is XAttrMetadataPP

# Generated at 2022-06-14 18:13:41.748215
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    assert isinstance(pp, XAttrMetadataPP)

# Generated at 2022-06-14 18:13:50.043726
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ Unit test for constructor of class XAttrMetadataPP """

    from ..YoutubeDL import YoutubeDL
    import os

    def _test(infostr, expected_output):
        """
        Test helper method
        infostr:        info dictionary as JSON string
        expected_output:    expected output
        """

        info_dict = json.loads(infostr)
        config = {
            'writedescription': True,
            'writeinfojson': True,
            'outtmpl': 'whatever'
        }

        def _log(msg):
            return

        ydl = YoutubeDL(config)
        ydl.params['logger'] = _log
        ydl.to_stdout = _log
        ydl.to_stderr = _log
        ydl.process_ie_result(info_dict)

# Generated at 2022-06-14 18:14:33.190532
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    '''
    Test the XAttrMetadataPP.run function.
    '''

    import mock
    from ..utils import xattr

    filename = "test_filename"

    write_xattr = lambda filename, xattrname, byte_value: None

    info = {
        'webpage_url': 'webpage_url',
        'description': 'description',
        'title': 'title',
        'upload_date': 'upload_date',
        'uploader': 'uploader',
        'format': 'format',
    }
    postprocessor = XAttrMetadataPP()
    postprocessor.run(info)

# Generated at 2022-06-14 18:14:44.060161
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import FileDownloader
    import os.path
    from ..utils import (
        encodeFilename,
        XAttrMetadataError,
        XAttrUnavailableError,
    )


# Generated at 2022-06-14 18:14:55.651197
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    """Run method of XAttrMetadataPP.

    Test if the XAttrMetadataPP implementation of the run method is working correctly.
    """
    from ..utils import DateRange
    from ..extractor import gen_extractors

    pp_class = PostProcessor
    for ie in gen_extractors():
        ie.suitable(ie.ie_key())


# Generated at 2022-06-14 18:14:59.081814
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    module = sys.modules['__main__']
    setattr(module, 'FileDownloader', object)
    setattr(module, 'YoutubeDL', object)
    XAttrMetadataPP(object)

# Generated at 2022-06-14 18:15:08.262540
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    class TestDownloader(object):
        def to_screen(self, msg):
            print(msg)
        def report_warning(self, msg):
            print('WARNING: ' + msg)
        def report_error(self, msg):
            print('ERROR: ' + msg)
    class TestInfo(dict):
        def __init__(self):
            self['title'] = 'TITLE'
            self['description'] = 'DESCRIPTION'
            self['upload_date'] = 'UPLOAD_DATE'
            self['uploader'] = 'UPLOADER'
            self['format'] = 'FORMAT'
            self['filepath'] = '/tmp/test'
            self['webpage_url'] = 'http://example.url/'

    downloader = TestDownloader()
    info = TestInfo()

    xattr

# Generated at 2022-06-14 18:15:19.346281
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Check if the extension is available
    try:
        import xattr
    except ImportError:
        pytest.skip('The xattr extension is not available')

    import os
    import tempfile
    import urllib.request

    # Download a test file
    output_dir = tempfile.mkdtemp()
    yt_test_file = os.path.join(output_dir, 'test.flv')
    urllib.request.urlretrieve('http://www.youtube.com/get_video?video_id=EwTZ2xpQwpA', yt_test_file)

    # Copy test file to test the actual script
    output_file = os.path.join(output_dir, 'test2.flv')

# Generated at 2022-06-14 18:15:20.781775
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP is not None


# Generated at 2022-06-14 18:15:31.737763
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..extractor import gen_extractors
    from ..compat import compat_xattr

    def get_xattrs(filename):
        """ Get all xattrs of filename """
        try:
            return {
                name.decode('utf-8'): value.decode('utf-8')
                for name, value in compat_xattr.listxattr(filename).items()
            }
        except AttributeError:
            return {}

    def clear_xattrs(filename):
        """ Delete all xattrs of filename """
        try:
            for xattrname in compat_xattr.listxattr(filename):
                compat_xattr.removexattr(filename, xattrname)
        except AttributeError:
            pass

    class TestDownloader(object):
        def __init__(self):
            self

# Generated at 2022-06-14 18:15:37.367118
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass
    #pp = XAttrMetadataPP('name', 'downloader')

    #import subprocess
    #subprocess.call(['touch', 'test.txt'])

    #subprocess.call(['attr', '-s', 'user.dublincore.title', '-V', 'this is the title' , 'test.txt'])

    #subprocess.call(['getfattr', '-d', 'test.txt'])

# Generated at 2022-06-14 18:15:41.945602
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pproc = XAttrMetadataPP()
    assert isinstance(pproc, XAttrMetadataPP)


# Generated at 2022-06-14 18:17:07.608533
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Constructor of class XAttrMetadataPP
    XAttrMetadataPP(None)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Generated at 2022-06-14 18:17:08.350288
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass #TODO

# Generated at 2022-06-14 18:17:10.640592
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xp = XAttrMetadataPP()
    assert xp is not None

# vim:sw=4:ts=4:et:

# Generated at 2022-06-14 18:17:11.380924
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

# Generated at 2022-06-14 18:17:15.379140
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import pytest
    from youtube_dl.YoutubeDL import YoutubeDL
    options = {
        'writeinfojson': True,
        'writethumbnail': True,
        'writesubtitles': True,
    }
    ydl = YoutubeDL(options)
    pp = XAttrMetadataPP()
    pp.set_downloader(ydl)
    assert pp.downloader == ydl
    assert pp.name == 'xattrs'

# Generated at 2022-06-14 18:17:17.827538
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # TODO: implement unit test
    return

if __name__ == "__main__":
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:17:25.729778
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from ydl.downloader import HttpFD
    from ydl.postprocessor.ffmpeg import FFmpegPostProcessor
    from ydl.compat import compat_tempfile

    import os

    def pp_run(fd, info):
        dl = HttpFD(info['url'])
        fd.write(dl.read())

    tempfile = compat_tempfile.NamedTemporaryFile()

# Generated at 2022-06-14 18:17:37.886376
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    from .common import FileDownloader
    from .dash import DASH
    from .hls import HLS
    from .http import HTTP
    from .rtmp import RTMP
    from .smoothstreams import SmoothStreams
    from ..extractor import gen_extractors

    #############################################################################################
    #
    # Mocking FFMPEGPostProcessor
    #

    class FFMPEGPostProcessorMock:

        def run(self, *args):
            return
    FFMPEGPostProcessor = FFMPEGPostProcessorMock()

    #
    # Mocking FFMPEGPostProcessor (END)
    #
    #############################################################################################


# Generated at 2022-06-14 18:17:40.159685
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pp = XAttrMetadataPP(None)
    return (pp.__class__ == XAttrMetadataPP)

# Generated at 2022-06-14 18:17:41.151299
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    a = XAttrMetadataPP()
    pass