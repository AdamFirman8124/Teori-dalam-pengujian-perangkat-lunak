

# Generated at 2022-06-14 18:09:12.649202
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    name = 'XAttrMetadataPP'
    ydl = FileDownloader(params={'verbose': True, 'logger': FileDownloaderNoOpLogger()})
    xattr_metadata_pp = XAttrMetadataPP(ydl)
    assert name == xattr_metadata_pp.name
    assert xattr_metadata_pp._downloader == ydl

# Generated at 2022-06-14 18:09:24.746800
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os.path
    import tempfile

    from ..downloader import DEFAULT_OUTTMPL
    from ..utils import compat_xattr

    class FakeInfo():
        def __init__(self, filepath):
            self.filepath = filepath
            self.uploader = 'Test name'
            self.title = 'Test title'
            self.upload_date = '2019-01-01'
            self.description = 'Test description'
            self.webpage_url = 'www.example.com/upload'
            self.format = 'Test format'

    class FakeDl():
        def __init__(self, outtmpl):
            self.params = {'outtmpl': outtmpl,
                           'forcefilename': False}
            self.to_screen = print


# Generated at 2022-06-14 18:09:27.863622
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from ..utils import XAttrMetadataError

    from .common import FileDownloader

    # TODO: simulate a 'NO_SPACE' exception

# Generated at 2022-06-14 18:09:37.861122
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from io import BytesIO

    class FakeInfo(dict):
        pass

    class FakeYDL:
        def report_error(self, msg):
            pass

        def report_warning(self, msg):
            pass

    def fake_write_xattr(filename, xattrname, byte_value):
        return

    info = FakeInfo()
    info['format'] = 'mp4'
    info['webpage_url'] = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    info['title'] = 'test title'
    info['description'] = 'test description'
    info['upload_date'] = '20130630'
    info['uploader'] = 'uploader'

    ydl_obj = FakeYDL()

    dest = BytesIO()
    info['filepath']

# Generated at 2022-06-14 18:09:43.497356
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import pytest

    # test1: check if class constructor is working properly
    try:
        XAttrMetadataPP(None)
    except:
        raise AssertionError()

    # test2: check if constructor raises exception when argument is of wrong type
    with pytest.raises(AssertionError):
        XAttrMetadataPP(1)

# Generated at 2022-06-14 18:09:52.871985
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import io
    import sys
    import tempfile
    import unittest
    from .ppty import InfoExtractor

    # We must disable xattr support
    class TestIE(InfoExtractor):
        def __init__(self, *args, **kwargs):
            InfoExtractor.__init__(self, *args, **kwargs)
            self.xattr_title = None

        def add_default_extra_info(self, *args, **kwargs):
            return {'xattr_title': self.xattr_title}

        def report_warning(self, msg):
            sys.stderr.write('WARNING: ' + msg + '\n')

    class FakeYDL(object):
        def __init__(self, **kwargs):
            self.params = kwargs


# Generated at 2022-06-14 18:09:53.464573
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:10:03.973790
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    class FakeDownloader:

        def to_screen(self, string):
            pass

        def report_error(self, msg):
            pass

        def report_warning(self, msg):
            pass

    class FakeInfoExtractor:

        def __init__(self):
            self.info = {}
            self.info['title'] = 'video_title'
            self.info['upload_date'] = '20180301'
            self.info['description'] = 'video_description'
            self.info['uploader'] = 'uploader'
            self.info['webpage_url'] = 'www.youtube.com'
            self.info['fulltitle'] = 'video_title'
            self.info['filesize'] = 10000
            self.info['format'] = 'mp4'

# Generated at 2022-06-14 18:10:09.919480
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #
    # Unit test for method run of class XAttrMetadataPP
    #
    # To run this test use (for example):
    #   youtube-dl --postprocessor-args="['-v', '--test-XAttrMetadataPP-run']" \
    #   --match-filter="duration <= 300 && age <= 604800" --get-url \
    #   --test-XAttrMetadataPP-run
    #
    # then:
    #   python -m unittest test_XAttrMetadataPP

    import tempfile
    import os

    import unittest
    import unittest.mock as mock
    from youtube_dl.Downloader import Downloader

    import xattr

    class FakeInfo(dict):
        def __init__(self, meta, filename):
            self.meta

# Generated at 2022-06-14 18:10:11.123002
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass

# Generated at 2022-06-14 18:10:17.281847
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


# Generated at 2022-06-14 18:10:27.209549
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import DOWNLOADER_NAME
    from ..extractor import gen_extractors

    def report_error_mock(self, msg):
        self.msg = msg

    def report_warning_mock(self, msg):
        self.msg = msg

    def to_screen_mock(self, msg):
        pass

    def gen_extractor_mock(self, ie_name, url):
        return ie_name

    class MockDownloader():
        def __init__(self):
            # Set attributes
            self._ies = gen_extractors()
            self.params = {}
            self.params['writethumbnail'] = True
            self.params['outtmpl'] = '%(id)s.%(ext)s'
            self.params['restrictfilenames'] = True

            #

# Generated at 2022-06-14 18:10:36.506279
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # Create a temporary file
    import tempfile
    (fd, fname) = tempfile.mkstemp(prefix="XAttrMetadataPPtest-")
    os.close(fd)

    # Try to write to this file's extended attributes
    metadata = {'date': '2017.12.31', 'title': 'Test video'}

    pp = XAttrMetadataPP(None)
    pp.run(metadata, fname)

    # Clean up
    os.remove(fname)

if __name__ == "__main__":
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:10:40.079336
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    context = {
        'filename': 'test.flv',
    }
    postprocessor = XAttrMetadataPP(context)
    assert postprocessor

# Generated at 2022-06-14 18:10:43.864359
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


if __name__ == '__main__':
    import sys
    sys.exit(test_XAttrMetadataPP_run())

# Generated at 2022-06-14 18:10:45.285454
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #import pyxattr
    #pyxattr.EOVERFLOW
    assert True

# Generated at 2022-06-14 18:10:56.323919
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import sys
    import tempfile
    from .common import FileDownloader
    from ..extractor import youtube_dl

    filename = tempfile.NamedTemporaryFile(delete=False).name

    test_info = {
        'filepath' : filename,
        'webpage_url' : 'http://youtube.com/watch?v=BaW_jenozKc',
        'title' : 'youtube-dl test video "\'/\\ä↭𝕐',
        'upload_date' : '20010101',
        'description' : 'test chars:"\\\'/ä↭',
        'uploader' : 'xäx',
        'format' : 'format',
    }


# Generated at 2022-06-14 18:10:58.099466
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    return True

# Generated at 2022-06-14 18:10:59.471099
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP._avconv_available() == False
    assert XAttrMetadataPP._ffmpeg_available() == False

# Generated at 2022-06-14 18:11:07.971299
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    ff = XAttrMetadataPP({'upldate': '20130813', 'title': '"coucou"', 'webpage_url': 'http://goo/'})
    assert ff.get_info({}).get('xattrs', {}) == {
        'user.xdg.referrer.url': 'http://goo/',
        'user.dublincore.title': '"coucou"',
        'user.dublincore.date': '2013-08-13',  # get_info will format the date
    }


post_processor_class = XAttrMetadataPP

# Generated at 2022-06-14 18:11:21.420916
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    XAttrMetadataPP(ydl)

if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:11:34.538502
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    if compat_os_name == 'nt':
        print('Extended attributes not supported on Windows. Skipping xattr metadata unit test.')
    else:
        import tempfile, os, xattr


# Generated at 2022-06-14 18:11:44.921743
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    filename = 'abcdefg.mp3'
    info = {
        'filepath': filename,
        'upload_date': '20140721',
        'description': 'this is a very long description',
        'webpage_url': 'https://www.youtube.com/watch?v=HGJU3q3U8I8',
        'uploader': 'John Doe',
        'title': 'ABC',
        'format': 'audio/webm',
    }

    def _read_xattr(filename, xattr):
        if xattr == 'user.xdg.referrer.url':
            return 'https://www.youtube.com/watch?v=HGJU3q3U8I8'
        elif xattr == 'user.dublincore.title':
            return 'ABC'


# Generated at 2022-06-14 18:11:47.058900
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    return XAttrMetadataPP(None)

if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-14 18:11:57.955041
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile

    from ..utils import (
        XAttrMetadataError,
        read_xattr,
    )

    class FakeYDL:
        def report_warning(self, msg): print(msg)
        def report_error(self, msg): print(msg)
        def to_screen(self, msg): print(msg)

    # Create a temporary empty file
    with tempfile.NamedTemporaryFile() as tmp:
        # filename = tmp.name

        dl = FakeYDL()

# Generated at 2022-06-14 18:12:08.012807
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .deprecated import FileDownloader
    import os.path

    class FakeInfo:
        def __init__(self):
            self.filepath = '/tmp/file'
            self.webpage_url = 'http://webpage.url'
            self.title = 'title'
            self.upload_date = '2012-10-29'
            self.description = 'description'
            self.uploader = 'uploader'
            self.format = 'format'

    class FakeDownloader:
        def to_screen(self, message):
            print(message)

        def report_warning(self, message):
            print('[warn] ' + message)

        def report_error(self, message):
            print('[error] ' + message)

    # ok
    xattr_mapping = FakeInfo()
    downloader

# Generated at 2022-06-14 18:12:17.540737
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    #Creating an XAttrMetadataPP object to test its method run
    xattr_metadata_pp = XAttrMetadataPP()

    #Test with a correct value of info
    info = {'title':'test_title',
            'upload_date':'test_upload_date',
            'description':'test_description',
            'uploader':'test_uploader',
            'format':'test_format',
            'webpage_url':'test_webpage_url'}
    errors1, info1 = xattr_metadata_pp.run(info)
    #Checking that it returns the correct value
    # (an empty list of errors and the same info)
    assert errors1 == []
    assert info == info1

    #Test with an incorrect value of info

# Generated at 2022-06-14 18:12:21.004969
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Currently not possible to unit test method run of class XAttrMetadataPP.
    # Need to find a way to emulate a filesystem supporting xattrs for this.
    return True


# Generated at 2022-06-14 18:12:32.900652
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Test that in case of an XAttrMetadataError, the error is correctly logged
    class DummyYDL:
        def __init__(self, downloads):
            self.to_screen = lambda *x: None
            self.report_error = lambda *x: None
            self.report_warning = lambda *x: None
            self.downloads = downloads

    class DummyInfo:
        def __init__(self, filepath, webpage_url, description, title, upload_date, uploader, format):
            self.filepath = filepath
            self.webpage_url = webpage_url
            self.description = description
            self.title = title
            self.upload_date = upload_date
            self.uploader = uploader
            self.format = format

    import sys

# Generated at 2022-06-14 18:12:41.859256
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    # Test xattr writing with a reference file
    fname = './extended_attributes_reference_file'

# Generated at 2022-06-14 18:13:14.057331
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    # This code tests the constructor.
    # We will call this unit test from the "intelligent" test suite.
    #
    # Should be OK:
    attr_pp = XAttrMetadataPP(None)
    assert attr_pp.name == 'xattr'
    #
    attr_pp = XAttrMetadataPP(None, name='xattr-test')
    assert attr_pp.name == 'xattr-test'
    #
    # Should throw an exception, 'name' is required:
    try:
        attr_pp = XAttrMetadataPP(None, True)
        assert False, 'Should never reach here, it should have thrown an exception'
    except TypeError as e:
        assert str(e) == 'argument "name" is required'
    #
    # Should throw an exception

# Generated at 2022-06-14 18:13:23.496738
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    if compat_os_name == 'nt':
        import pytest
        pytest.skip('Extended attributes are only available on Linux and macOS.')
    from __main__ import parseOpts, FileDownloader
    from .common import PostProcessorTest
    from ..utils import write_xattr, get_xattr

    # import os, sys

    # fake downloader instance, just for testing
    class FakeDownloader(FileDownloader):
        def to_screen(self, msg):  pass
        def report_warning(self, msg):  pass
        def report_error(self, msg):  pass

    class FakeXAttrMetadataPP(XAttrMetadataPP, PostProcessorTest):
        def __init__(self):
            XAttrMetadataPP.__init__(self, FakeDownloader())
            PostProcessorTest

# Generated at 2022-06-14 18:13:31.402953
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    from .common import TestPostProcessorBase

    class TestXAttrMetadataPP(TestPostProcessorBase):
        def __init__(self, results):
            super(TestXAttrMetadataPP, self).__init__()
            self._results = results

        def check_xattr(self, name, path, expected):
            value = self._results.get((name, path))
            if value is None:
                raise AssertionError('Expected value for %s on file %s not found' % (repr(name), repr(path)))
            if value != expected:
                raise AssertionError('Expected %s for %s on file %s, got %s' % (repr(expected), repr(name), repr(path), repr(value)))

    import os
    import tempfile
    test_dir = tempfile

# Generated at 2022-06-14 18:13:38.087543
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    writable_filepath = './testXAttrMetadataPP.test_run'

    # Create a file
    try:
        f = open(writable_filepath, 'w')
        f.close()
    except IOError as e:
        return (False, 'Unable to create file %s' % writable_filepath + ': ' + str(e))


# Generated at 2022-06-14 18:13:40.892484
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


# Generated at 2022-06-14 18:13:49.584073
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    print('TEST XAttrMetadataPP run:')

    class my_XAttrMetadataPP(XAttrMetadataPP):
        def __init__(self):
            self.counter = 0
            self.max_local_xattr_size = 5 # byte

        def to_screen(self, *args, **kargs):
            print(*args, **kargs)

        def report_error(self, *args, **kargs):
            print(*args, **kargs)

        def report_warning(self, *args, **kargs):
            print(*args, **kargs)

        def write_local_xattr(self, filename, xattrname, byte_value):
            print('write_local_xattr: ' + filename + ' ' + xattrname + ' ' + byte_value)


# Generated at 2022-06-14 18:13:51.446017
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_pp = XAttrMetadataPP()
    assert xattr_pp.run() == ([], {})

# Generated at 2022-06-14 18:13:56.419925
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..downloader import Downloader
    ydl = Downloader({})
    # if XAttrMetadataPP is called with ydl=None, then get_info_extractor returns None
    # and XAttrMetadataPP.run() will be called with info = None
    pp = XAttrMetadataPP(ydl=ydl)
    assert pp.ydl is not None

# Generated at 2022-06-14 18:14:04.355345
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import tempfile

    # fake 'info_dict'
    info_dict = {
        'filepath': 'test.mp4',
        'title': 'title',
        'uploader': 'uploader',
        'format': 'format',
        'webpage_url': 'webpage_url',
        'description': 'description',
        'upload_date': 'upload_date',
    }


# Generated at 2022-06-14 18:14:06.708243
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_pp = XAttrMetadataPP()


# Test function for function run of class XAttrMetadataPP

# Generated at 2022-06-14 18:14:49.424232
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattr_metadata = XAttrMetadataPP()
    assert isinstance(xattr_metadata, PostProcessor)
    assert xattr_metadata.run is not None

# Generated at 2022-06-14 18:14:59.532102
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    import os
    import re
    import locale

    from ..compat import compat_os_name

    from .test_utils import fake_getprogpath

    if compat_os_name == 'nt':
        return
    if not os.path.exists('/usr/bin/getfattr'):
        return
    if not os.path.exists('/usr/bin/setfattr'):
        return

    # Test try/except XAttrUnavailableError
    with fake_getprogpath('/usr/bin/git'):
        XAttrMetadataPP().run({})

    with fake_getprogpath('/usr/bin/git'):
        with open(os.path.join(os.path.dirname(__file__), 'test.webm'), 'rb') as f:
            XAtt

# Generated at 2022-06-14 18:15:08.541007
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import time
    from collections import namedtuple

    from ..utils import sanitize_open, xattr_write, set_filesystem_errors

    XAttr = namedtuple('XAttr', ['name', 'value'])


# Generated at 2022-06-14 18:15:12.377709
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    """ test_XAttrMetadataPP """
    xattr_pp = XAttrMetadataPP()
    assert xattr_pp


if __name__ == '__main__':
    test_XAttrMetadataPP()

# Generated at 2022-06-14 18:15:13.328152
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    pass

# Generated at 2022-06-14 18:15:25.030802
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import tempfile

    from io import BytesIO
    from ..utils import encodeFilename

    # Create a dummy file to write xattrs on
    handle, tempfilename = tempfile.mkstemp()
    os.close(handle)

    # Create the info dict
    info = {
        'filepath': encodeFilename(tempfilename),
        'title': 'Test title',
        'upload_date': '20140701',
        'description': 'Test description',
        'uploader': 'Test uploader',
        'webpage_url' : 'http://example.com',
        'format': 'Test format',
    }

    # Create a XAttrMetadataPP object, run the method and check that all the xattrs are written
    pp = XAttrMetadataPP(None)
    _, info = pp.run(info)

# Generated at 2022-06-14 18:15:34.929044
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import unittest

    from .common import PostProcessorTestCase

    class XAttrTestCase(PostProcessorTestCase):

        def setUp(self):
            # Don't write metadata to file's xattrs
            # Don't remove versions of youtube_dl
            self.setUpPostProcessor(XAttrMetadataPP, {'writeinfojson': False, 'outtmpl': '%(id)s%(ext)s', 'writethumbnail': False, 'min_filesize': 1})

        def test_test(self):
            self.test_post_processor(['2Dk9gYXN82Y'])

    unittest.main(argv=['first-arg-is-ignored'], defaultTest='XAttrTestCase', exit=False)

# Generated at 2022-06-14 18:15:42.108072
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():

    import sys
    import os
    from ytdl.utils import FileDownloader


# Generated at 2022-06-14 18:15:43.856876
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP

# Generated at 2022-06-14 18:15:55.751493
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Test with file that can have xattr written
    import tempfile
    import shutil
    import os
    import sys

    test_dir = tempfile.mkdtemp()


# Generated at 2022-06-14 18:17:23.309304
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    try:
        import xattr
    except ImportError:
        return
    else:
        # Make sure the constructor works with any arguments
        XAttrMetadataPP(None)

# Generated at 2022-06-14 18:17:25.022540
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    assert XAttrMetadataPP(None).is_disabled() == True

# Generated at 2022-06-14 18:17:37.268681
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    import os
    import tempfile
    import shutil
    import pytest
    from ..utils import (
        write_json_file,
        read_json_file,
    )
    from .common import FileDownloader
    from .xattr import write_xattr, XAttrMetadataError

    # Create a temporary directory for the test
    test_dir = tempfile.mkdtemp()

    # Create and write a temporary test file in that directory
    temp_file = tempfile.NamedTemporaryFile(dir=test_dir, delete=False)
    temp_file.close()

    # Create the test info dict

# Generated at 2022-06-14 18:17:39.446274
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    pass


if __name__ == '__main__':
    test_XAttrMetadataPP_run()

# Generated at 2022-06-14 18:17:48.625956
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    # Test with one simple info from one video
    postprocessor = XAttrMetadataPP()
    postprocessor._downloader = MockYDL()

    # Test if exception is raised for unsupported file system
    info = {}
    with pytest.raises(XAttrMetadataError):
        postprocessor.run(info)

    # Test if exception is raised for unsupported file system
    info = {}
    postprocessor._raise_xattr_unavailable = True
    with pytest.raises(XAttrUnavailableError):
        postprocessor.run(info)

    # Test if warning is thrown when there is no space left
    info = {}
    postprocessor._raise_no_space = True
    postprocessor.run(info)

    ## Test if warning is thrown when value is too long
    info = {}
    postprocessor._raise_value_

# Generated at 2022-06-14 18:17:50.776248
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    from ..YoutubeDL import YoutubeDL

    ydl = YoutubeDL({})

    pp = XAttrMetadataPP(ydl)

    assert pp.get_id() == "metadata"

# Generated at 2022-06-14 18:18:03.187301
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():

    import io

    import pytest

    import youtube_dl.YoutubeDL
    import postprocessor.xattrs

    # Create dummy file
    filename = 'dummy_file.webm'
    f = io.open(filename, 'wb')
    f.close()

    # Fill info with some reasonable data
    info = {
        'filepath': filename,
        'title': 'Dummy title',
        'upload_date': '20160731',
        'uploader': 'Uploader',
        'description': 'Very useful',
        'webpage_url': 'https://example.com/watch?v=dQw4w9WgXcQ',
        'format': 'webm',
    }

    # Create a new XAttrMetadataPP object with a YoutubeDL object
    postProcessor = postprocessor.x

# Generated at 2022-06-14 18:18:13.338313
# Unit test for method run of class XAttrMetadataPP
def test_XAttrMetadataPP_run():
    mapping = {
        'user.xdg.referrer.url': 'webpage_url',
        'user.dublincore.title': 'title',
        'user.dublincore.date': 'upload_date',
        'user.dublincore.description': 'description',
        'user.dublincore.contributor': 'uploader',
        'user.dublincore.format': 'format',
    }

    import tempfile
    import os
    import xattr

    # Create a temporary file for testing
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()

    #
    # Test 'run' method without errors
    #

# Generated at 2022-06-14 18:18:20.004755
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    xattrmetadata = XAttrMetadataPP()

    test_dict = {
        'webpage_url': 'http://youtube.com',
        'title': 'video title',
        'upload_date': '20130325',
        'description': 'video description',
        'uploader': 'username',
        'format': 'video/mp4',
    }

    result, info = xattrmetadata.run(test_dict)
    for key in test_dict:
        if key == 'upload_date':
            assert test_dict['upload_date'] == '20130325' == info['upload_date']
            assert test_dict['upload_date'] == hyphenate_date(test_dict['upload_date'])
        else:
            assert test_dict[key] == info[key]



# Generated at 2022-06-14 18:18:22.155043
# Unit test for constructor of class XAttrMetadataPP
def test_XAttrMetadataPP():
    x = XAttrMetadataPP()
    assert x is not None
