

# Generated at 2026-10-24 11:19:35.476681
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from .fourtube import PornerBrosIE, FourTubeBaseIE

    # No custom __init__ - uses InfoExtractor / FourTubeBaseIE constructor
    assert PornerBrosIE.__init__ is FourTubeBaseIE.__init__

    # Can construct with no args and with explicit downloader
    ie = PornerBrosIE()
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornerBrosIE(None)
    assert isinstance(ie_with_none, PornerBrosIE)

    class DummyDownloader(object):
        pass

    ie_with_dl = PornerBrosIE(DummyDownloader())
    assert isinstance(ie_with_dl, PornerBrosIE)

    # Class-level config set correctly
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._VALID_URL is not None

    # _VALID_URL matches expected forms
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://www.pornerbros.com/videos/test-video_181369')
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')

# Generated at 2026-10-24 11:19:37.903911
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:19:40.322311
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:19:42.742892
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:19:45.163388
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:19:47.582946
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:19:50.001222
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:19:52.417166
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:19:54.833911
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:19:57.251722
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:19:59.668208
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:20:02.088209
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:20:04.503866
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:20:06.921903
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:20:09.341988
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:20:11.761677
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:20:14.180908
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:20:16.598465
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:20:19.015493
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:20:37.327336
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() is None
    assert ie.IE_NAME is None
    assert ie._VALID_URL is None
    assert ie._URL_TEMPLATE is None
    assert ie._TKN_HOST is None

# Generated at 2026-10-24 11:20:49.901748
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:21:16.033892
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:21:18.460880
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:21:20.876377
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:21:22.414826
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():ie = FourTubeBaseIE()

# Generated at 2026-10-24 11:21:23.923697
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 11:21:37.843945
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 11:21:39.162369
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:21:40.480979
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:21:41.805857
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:21:43.133786
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:21:44.417679
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:21:45.736109
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:21:47.111905
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:21:48.456259
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:21:49.772133
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:22:09.243564
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:22:11.667170
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:22:14.130587
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:22:16.554270
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:22:18.973313
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 11:22:21.551578
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 11:22:23.967366
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 11:22:26.385573
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 11:22:41.286691
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():from youtube_dl.extractor.fourtube import FourTubeBaseIE, PornerBrosIE

# Generated at 2026-10-24 11:22:42.617740
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:23:16.150464
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    for test in PornTubeIE._TESTS:
        url = test['url']
        assert ie.suitable(url), 'PornTubeIE should handle %s' % url
        expected_id = test.get('info_dict', {}).get('id')
        if expected_id:
            matched = ie._match_id(url)
            assert matched == expected_id, (
                'PornTubeIE extracted id %r from %s, expected %r'
                % (matched, url, expected_id))

    for url in (
        'https://www.porntube.com/',
        'https://example.com/videos/teen-couple-doing-anal_7089759',
        'https://www.porntube.com/videos/teen-couple-doing-anal',
        'https://www.porntube.com/embed/',
    ):
        assert not ie.suitable(url), 'PornTubeIE should not handle %s' % url

# Generated at 2026-10-24 11:23:17.463732
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:23:18.794145
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:23:20.120230
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:23:21.443710
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:23:23.870690
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:23:26.288357
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:23:28.707536
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:23:31.125778
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:23:33.547211
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:23:58.864021
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-24 11:24:00.190102
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:24:01.614444
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:24:02.941224
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:24:04.265622
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:24:05.640490
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    for test in PornTubeIE._TESTS:
        url = test['url']
        assert ie.suitable(url), 'PornTubeIE should handle %s' % url
        expected_id = test.get('info_dict', {}).get('id')
        if expected_id:
            matched = ie._match_id(url)
            assert matched == expected_id, (
                'PornTubeIE extracted id %r from %s, expected %r'
                % (matched, url, expected_id))

    for url in (
        'https://www.porntube.com/',
        'https://example.com/videos/teen-couple-doing-anal_7089759',
        'https://www.porntube.com/videos/teen-couple-doing-anal',
        'https://www.porntube.com/embed/',
    ):
        assert not ie.suitable(url), 'PornTubeIE should not handle %s' % url

# Generated at 2026-10-24 11:24:06.968086
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:24:08.377254
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:24:09.700628
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:24:11.144155
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:24:13.729668
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:24:16.147865
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:24:18.568887
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:24:21.142252
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:24:23.557528
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:24:25.972976
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:24:28.389751
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:24:30.808538
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:24:33.226751
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:24:35.640273
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:24:37.096101
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 11:24:45.461921
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:24:46.781754
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:24:48.125170
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:24:49.455808
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:24:50.832739
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:25:07.211817
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    for test in PornTubeIE._TESTS:
        url = test['url']
        assert ie.suitable(url), 'PornTubeIE should handle %s' % url
        expected_id = test.get('info_dict', {}).get('id')
        if expected_id:
            matched = ie._match_id(url)
            assert matched == expected_id, (
                'PornTubeIE extracted id %r from %s, expected %r'
                % (matched, url, expected_id))

    for url in (
        'https://www.porntube.com/',
        'https://example.com/videos/teen-couple-doing-anal_7089759',
        'https://www.porntube.com/videos/teen-couple-doing-anal',
        'https://www.porntube.com/embed/',
    ):
        assert not ie.suitable(url), 'PornTubeIE should not handle %s' % url

# Generated at 2026-10-24 11:25:08.553725
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:25:10.019063
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:25:12.596791
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:25:15.103397
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:25:17.634229
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:25:20.203682
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:25:22.826772
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:25:25.256483
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:25:27.673616
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:25:30.093678
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:25:32.513523
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:25:34.931894
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:25:37.352874
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:25:39.784320
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:25:42.206526
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:26:07.669746
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 11:26:24.261774
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    for test in PornTubeIE._TESTS:
        url = test['url']
        assert ie.suitable(url), 'PornTubeIE should handle %s' % url
        expected_id = test.get('info_dict', {}).get('id')
        if expected_id:
            matched = ie._match_id(url)
            assert matched == expected_id, (
                'PornTubeIE extracted id %r from %s, expected %r'
                % (matched, url, expected_id))

    for url in (
        'https://www.porntube.com/',
        'https://example.com/videos/teen-couple-doing-anal_7089759',
        'https://www.porntube.com/videos/teen-couple-doing-anal',
        'https://www.porntube.com/embed/',
    ):
        assert not ie.suitable(url), 'PornTubeIE should not handle %s' % url

# Generated at 2026-10-24 11:26:25.720757
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:26:27.034597
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:26:28.366254
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:26:29.790453
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:26:31.924070
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:26:33.578006
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:26:50.067077
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    for test in PornTubeIE._TESTS:
        url = test['url']
        assert ie.suitable(url), 'PornTubeIE should handle %s' % url
        expected_id = test.get('info_dict', {}).get('id')
        if expected_id:
            matched = ie._match_id(url)
            assert matched == expected_id, (
                'PornTubeIE extracted id %r from %s, expected %r'
                % (matched, url, expected_id))

    for url in (
        'https://www.porntube.com/',
        'https://example.com/videos/teen-couple-doing-anal_7089759',
        'https://www.porntube.com/videos/teen-couple-doing-anal',
        'https://www.porntube.com/embed/',
    ):
        assert not ie.suitable(url), 'PornTubeIE should not handle %s' % url

# Generated at 2026-10-24 11:26:51.402132
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:26:52.828272
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    for test in PornTubeIE._TESTS:
        url = test['url']
        assert ie.suitable(url), 'PornTubeIE should handle %s' % url
        expected_id = test.get('info_dict', {}).get('id')
        if expected_id:
            matched = ie._match_id(url)
            assert matched == expected_id, (
                'PornTubeIE extracted id %r from %s, expected %r'
                % (matched, url, expected_id))

    for url in (
        'https://www.porntube.com/',
        'https://example.com/videos/teen-couple-doing-anal_7089759',
        'https://www.porntube.com/videos/teen-couple-doing-anal',
        'https://www.porntube.com/embed/',
    ):
        assert not ie.suitable(url), 'PornTubeIE should not handle %s' % url

# Generated at 2026-10-24 11:26:54.181410
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:26:55.532876
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:26:56.860770
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:26:58.180304
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:26:59.547450
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:27:03.405137
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:27:04.728891
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:27:06.060567
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:27:07.383952
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:27:08.721723
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:27:10.114230
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:27:11.447689
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 11:27:12.769741
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:27:14.104584
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:27:15.423922
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:27:23.759664
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 11:27:26.183591
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 11:27:28.605993
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 11:27:31.025609
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:27:33.444355
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:27:35.868467
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 11:27:38.290028
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:27:40.710517
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:27:43.127129
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:27:45.536250
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:27:47.955615
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:27:50.378915
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 11:27:52.796970
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:27:55.218128
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:27:57.637265
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:28:00.052002
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:28:02.470234
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:28:04.889120
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 11:28:07.310159
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 11:28:15.761454
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.IE_NAME == 'Fux'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/some-video')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m == ('195359', 'awesome-fucking-kitchen-ends-cum-swallow')

    m = ie._match_id('https://www.fux.com/embed/195359')
    assert m == ('195359', None)

    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

# Generated at 2026-10-24 11:28:17.103509
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:28:18.543072
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:28:19.908114
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    for test in PornTubeIE._TESTS:
        url = test['url']
        assert ie.suitable(url), 'PornTubeIE should handle %s' % url
        expected_id = test.get('info_dict', {}).get('id')
        if expected_id:
            matched = ie._match_id(url)
            assert matched == expected_id, (
                'PornTubeIE extracted id %r from %s, expected %r'
                % (matched, url, expected_id))

    for url in (
        'https://www.porntube.com/',
        'https://example.com/videos/teen-couple-doing-anal_7089759',
        'https://www.porntube.com/videos/teen-couple-doing-anal',
        'https://www.porntube.com/embed/',
    ):
        assert not ie.suitable(url), 'PornTubeIE should not handle %s' % url

# Generated at 2026-10-24 11:28:34.999556
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:28:36.322184
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:28:37.698566
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:28:39.121471
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:28:40.465366
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 11:28:41.786597
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 11:28:43.160689
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 11:29:08.139491
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert extractor.suitable('https://www.porntube.com/embed/7089759')

# Generated at 2026-10-24 11:29:10.735962
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() is None
    assert ie.IE_NAME is None
    assert ie._VALID_URL is None
    assert ie._URL_TEMPLATE is None
    assert ie._TKN_HOST is None

# Generated at 2026-10-24 11:29:12.402071
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')