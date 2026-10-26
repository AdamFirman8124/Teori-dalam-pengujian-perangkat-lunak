

# Generated at 2026-10-25 14:19:28.819052
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 14:19:38.446181
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    downloader = object()

    extractor = FourTubeIE(downloader)

    assert isinstance(extractor, FourTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_NAME == '4tube'
    assert extractor._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 14:20:06.963329
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    extractor = FourTubeIE()

    assert isinstance(extractor, FourTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor.IE_NAME == '4tube'
    assert extractor._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert extractor._TKN_HOST == 'token.4tube.com'
    assert extractor.suitable(
        'https://www.4tube.com/videos/209733/example-video')

# Generated at 2026-10-25 14:20:09.881909
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 14:20:40.396704
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert re.match(
        extractor._VALID_URL,
        'https://www.fux.com/video/195359/example-video')

# Generated at 2026-10-25 14:20:48.781109
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-25 14:20:58.626878
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor.ie_key() == 'PornTube'

# Generated at 2026-10-25 14:21:15.320286
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # 1. Constructor works with no args (downloader=None by InfoExtractor)
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. Constructor stores optional downloader
    sentinel = object()
    ie_with_dl = PornTubeIE(downloader=sentinel)
    assert ie_with_dl._downloader is sentinel

    # 3. Class configuration specific to PornTubeIE
    assert PornTubeIE._TKN_HOST == 'tkn.porntube.com'
    assert PornTubeIE._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert PornTubeIE._URL_TEMPLATE % '7089759' == \
        'https://www.porntube.com/videos/video_7089759'

    # 4. URL matcher extracts id / display_id
    m = PornTubeIE._VALID_URL.match if hasattr(PornTubeIE._VALID_URL, 'match') else None
    import re
    mobj = re.match(
        PornTubeIE._VALID_URL,
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    )
    assert mobj is not None
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'

    mobj = re.match(
        PornTubeIE._VALID_URL,
        'https://www.porntube.com/embed/7089759'
    )
    assert mobj is not None
    assert mobj.group('id') == '7089759'

    assert re.match(
        PornTubeIE._VALID_URL,
        'https://m.porntube.com/videos/teen-couple-doing-anal_7089759'
    ) is not None

    # 5. Does not match sibling extractors' domains
    assert re.match(
        PornTubeIE._VALID_URL,
        'https://www.4tube.com/videos/209733/video'
    ) is None
    assert re.match(
        PornTubeIE._VALID_URL,
        'https://www.fux.com/video/195359/video'
    ) is None

# Generated at 2026-10-25 14:21:20.521939
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:21:30.084148
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-25 14:21:31.493820
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 14:21:41.428352
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    extractor = FourTubeIE()

    assert isinstance(extractor, FourTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == '4tube'
    assert extractor._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert extractor._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 14:21:42.869278
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 14:22:11.431890
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 14:22:27.926195
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import re
    ie = FuxIE()

    # Constructor created a usable instance with class-level config intact
    assert ie._VALID_URL is not None
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    # _VALID_URL matches a normal video URL and captures id + display_id
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    m = re.match(FuxIE._VALID_URL, url)
    assert m is not None
    assert m.group('id') == '195359'
    assert m.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'
    assert m.group('kind') is None

    # Embed and mobile URLs also match (kind = 'm' for mobile)
    assert re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    m = re.match(FuxIE._VALID_URL, 'https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m is not None and m.group('kind') == 'm'

    # Foreign URLs must not match
    assert re.match(FuxIE._VALID_URL, 'https://www.4tube.com/videos/209733/x') is None
    assert re.match(FuxIE._VALID_URL, 'https://www.fux.com/other/195359') is None

# Generated at 2026-10-25 14:22:55.397539
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    ie = PornTubeIE(downloader)

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is downloader
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 14:23:06.115424
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-25 14:23:07.547719
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 14:23:08.980259
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor produces a working instance of the right hierarchy
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class attributes are wired correctly
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie.IE_NAME is None  # inherited default; not overridden
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/whatever')
    assert not ie.suitable('https://www.porntube.com/videos/')

    # _VALID_URL captures id / display_id / kind groups correctly
    m = re.match(PornTubeIE._VALID_URL,
                 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'
    assert m.group('kind') is None

    m = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m.group('id') == '7089759'
    assert m.group('display_id') is None


# Generated at 2026-10-25 14:23:25.467217
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 14:23:36.731552
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-25 14:23:38.164576
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import re
    ie = FuxIE()

    # Constructor created a usable instance with class-level config intact
    assert ie._VALID_URL is not None
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    # _VALID_URL matches a normal video URL and captures id + display_id
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    m = re.match(FuxIE._VALID_URL, url)
    assert m is not None
    assert m.group('id') == '195359'
    assert m.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'
    assert m.group('kind') is None

    # Embed and mobile URLs also match (kind = 'm' for mobile)
    assert re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    m = re.match(FuxIE._VALID_URL, 'https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m is not None and m.group('kind') == 'm'

    # Foreign URLs must not match
    assert re.match(FuxIE._VALID_URL, 'https://www.4tube.com/videos/209733/x') is None
    assert re.match(FuxIE._VALID_URL, 'https://www.fux.com/other/195359') is None

# Generated at 2026-10-25 14:24:04.584350
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 14:24:27.831884
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Constructor should work with no args (downloader=None)
    ie = FourTubeIE()

    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level config specific to 4tube
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # _VALID_URL must be defined and match expected URL forms
    assert ie._VALID_URL
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/video')
    assert m is not None
    assert m.group('id') == '209733'

# Generated at 2026-10-25 14:24:53.844988
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 14:24:59.299324
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:25:01.712293
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:25:04.125901
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:25:06.541758
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:25:12.024911
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:25:14.439634
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:25:16.854564
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:25:19.269794
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:25:21.686093
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:25:24.098377
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:25:26.513701
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:25:28.926409
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:25:31.341062
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:25:33.757062
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:25:36.174648
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:25:38.586786
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:25:41.004075
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:25:43.419028
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:25:45.833485
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:25:48.250139
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:25:50.664166
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:25:53.079864
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:25:55.495312
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:25:57.909734
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:26:00.325143
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:26:02.744131
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:26:05.158746
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:26:07.574504
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:26:09.986949
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:26:12.401589
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:26:14.816395
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:26:17.230635
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:26:19.644988
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:26:22.060158
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:26:24.474096
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:26:26.950598
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:26:29.364857
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:26:31.781244
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:26:34.196571
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:26:36.611377
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:26:39.026027
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:26:41.443151
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:26:43.859879
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:26:46.274587
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:26:48.688471
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:26:51.102854
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:26:53.517557
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:26:55.931536
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:26:58.345978
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:00.759182
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:03.177436
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:05.676552
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:27:08.078132
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:27:10.493005
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:27:15.937973
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:27:18.355891
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:27:20.771417
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:27:23.187342
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:27:25.601144
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:27:28.015166
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:27:30.429123
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:32.843985
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:35.259646
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:37.673741
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:27:40.088282
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:27:42.505929
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:27:44.922647
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:47.335794
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:49.750501
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:27:52.166394
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:27:54.581476
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:27:56.995871
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:27:59.409987
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:28:01.829106
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:28:04.247617
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:28:06.660104
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:28:09.075874
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:28:11.517702
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:28:13.933673
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:28:16.348350
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:28:18.763608
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 14:28:21.177366
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:23.594893
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:26.011449
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:28.425696
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:30.842593
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:33.262274
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:35.673823
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:28:38.090456
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:28:40.507689
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 14:28:42.924715
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:28:45.342391
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:28:47.756115
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:28:50.169437
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:52.584403
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:54.998919
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 14:28:57.413990
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:28:59.827831
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:29:02.246582
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:29:04.663614
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:29:07.078815
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:29:09.493210
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 14:29:11.907211
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:29:14.321777
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 14:29:19.767482
# Unit test for constructor of class FuxIE