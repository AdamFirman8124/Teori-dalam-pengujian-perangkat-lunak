

# Generated at 2026-10-25 10:07:44.223720
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 10:07:45.641236
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

# Generated at 2026-10-25 10:07:58.964411
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

# Generated at 2026-10-25 10:08:01.381711
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:08:04.142566
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:08:06.557253
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:08:08.971985
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:08:11.387222
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:08:13.804415
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:08:16.217693
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:08:18.638791
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:08:21.048670
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:08:23.464099
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:08:25.879083
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:08:28.294251
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:08:31.019321
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:08:42.837293
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()
assert isinstance(ie, FourTubeBaseIE)
assert ie._TKN_HOST == 'token.pornerbros.com'
assert ie._URL_TEMPLATE % '181369' == 'https://www.pornerbros.com/videos/video_181369'
assert ie._VALID_URL is not None

# Generated at 2026-10-25 10:08:44.327609
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

# Generated at 2026-10-25 10:09:01.237832
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:09:18.628926
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()
assert isinstance(ie, FourTubeBaseIE)
assert ie._TKN_HOST == 'token.pornerbros.com'
assert ie._URL_TEMPLATE % '181369' == 'https://www.pornerbros.com/videos/video_181369'
assert ie._VALID_URL is not None

# Generated at 2026-10-25 10:09:21.204667
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:09:23.619310
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:09:26.039524
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:09:28.450367
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:09:30.865866
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:09:33.280210
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:09:36.192802
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:09:54.455608
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()
assert isinstance(ie, FourTubeBaseIE)
assert ie._TKN_HOST == 'token.pornerbros.com'
assert ie._URL_TEMPLATE % '181369' == 'https://www.pornerbros.com/videos/video_181369'
assert ie._VALID_URL is not None

# Generated at 2026-10-25 10:09:55.830574
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

# Generated at 2026-10-25 10:10:07.476117
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # default construction should succeed without downloader
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # inherited constructor accepts optional downloader
    downloader = object()
    ie_with_dl = FourTubeBaseIE(downloader)
    assert ie_with_dl._downloader is downloader

    # base class provides extraction helpers
    assert callable(getattr(ie, "_extract_formats", None))
    assert callable(getattr(ie, "_real_extract", None))

# Generated at 2026-10-25 10:10:09.012758
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # default construction should succeed without downloader
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # inherited constructor accepts optional downloader
    downloader = object()
    ie_with_dl = FourTubeBaseIE(downloader)
    assert ie_with_dl._downloader is downloader

    # base class provides extraction helpers
    assert callable(getattr(ie, "_extract_formats", None))
    assert callable(getattr(ie, "_real_extract", None))

# Generated at 2026-10-25 10:10:10.446039
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

# Generated at 2026-10-25 10:10:18.433905
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

# Generated at 2026-10-25 10:10:22.029289
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

# Generated at 2026-10-25 10:10:23.661308
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

# Generated at 2026-10-25 10:10:26.305013
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:10:29.087968
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:10:31.504309
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:10:33.926731
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:10:36.334685
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:10:38.753128
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:10:40.158724
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

# Generated at 2026-10-25 10:10:43.046022
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:10:44.545448
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()
assert isinstance(ie, FourTubeBaseIE)
assert ie._TKN_HOST == 'token.pornerbros.com'
assert ie._URL_TEMPLATE % '181369' == 'https://www.pornerbros.com/videos/video_181369'
assert ie._VALID_URL is not None

# Generated at 2026-10-25 10:10:46.081691
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

# Generated at 2026-10-25 10:10:59.700324
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 10:11:01.123433
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

# Generated at 2026-10-25 10:11:09.114096
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

# Generated at 2026-10-25 10:11:25.606288
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # default construction should succeed without downloader
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # inherited constructor accepts optional downloader
    downloader = object()
    ie_with_dl = FourTubeBaseIE(downloader)
    assert ie_with_dl._downloader is downloader

    # base class provides extraction helpers
    assert callable(getattr(ie, "_extract_formats", None))
    assert callable(getattr(ie, "_real_extract", None))

# Generated at 2026-10-25 10:11:42.197859
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # default construction should succeed without downloader
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # inherited constructor accepts optional downloader
    downloader = object()
    ie_with_dl = FourTubeBaseIE(downloader)
    assert ie_with_dl._downloader is downloader

    # base class provides extraction helpers
    assert callable(getattr(ie, "_extract_formats", None))
    assert callable(getattr(ie, "_real_extract", None))

# Generated at 2026-10-25 10:11:44.238022
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

# Generated at 2026-10-25 10:11:45.663034
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

# Generated at 2026-10-25 10:11:48.529684
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 10:11:49.980070
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

# Generated at 2026-10-25 10:11:51.412884
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # default construction should succeed without downloader
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # inherited constructor accepts optional downloader
    downloader = object()
    ie_with_dl = FourTubeBaseIE(downloader)
    assert ie_with_dl._downloader is downloader

    # base class provides extraction helpers
    assert callable(getattr(ie, "_extract_formats", None))
    assert callable(getattr(ie, "_real_extract", None))

# Generated at 2026-10-25 10:12:09.333092
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 10:12:12.199496
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:12:21.830073
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()
assert isinstance(ie, FourTubeBaseIE)
assert ie._TKN_HOST == 'token.pornerbros.com'
assert ie._URL_TEMPLATE % '181369' == 'https://www.pornerbros.com/videos/video_181369'
assert ie._VALID_URL is not None

# Generated at 2026-10-25 10:12:24.512582
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:12:26.931754
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:12:29.344507
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:12:31.760420
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:34.176665
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:36.692172
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:39.095456
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:12:41.510132
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:12:43.924623
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:12:46.338337
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:48.751923
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:51.166133
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:53.581063
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:55.995340
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:12:58.409818
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:00.825519
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:13:03.260960
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:13:05.678067
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:13:08.092661
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:13:10.508057
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:13:12.923819
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:13:15.340381
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:13:17.759040
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:13:20.175223
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:13:22.587938
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:13:25.001195
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:13:27.419951
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:13:29.833333
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:13:32.250968
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:13:34.662542
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:13:37.077244
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:39.493754
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:41.908908
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:44.326314
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:46.741598
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:49.165841
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:51.574623
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:53.990093
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:56.406135
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 10:13:58.822140
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:14:01.236487
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:14:03.650690
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 10:14:06.126243
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:08.541930
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:10.955350
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:13.369615
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:14:15.784015
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:14:18.197800
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 10:14:20.613221
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:23.028239
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:25.441278
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:27.854919
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:14:30.267277
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:14:32.683137
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 10:14:35.236695
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:37.619645
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:40.035214
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:42.450268
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:14:44.866336
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 10:15:28.296850
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():from youtube_dl.extractor.fourtube import FourTubeBaseIE

# Generated at 2026-10-25 10:15:45.193532
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # default construction should succeed without downloader
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # inherited constructor accepts optional downloader
    downloader = object()
    ie_with_dl = FourTubeBaseIE(downloader)
    assert ie_with_dl._downloader is downloader

    # base class provides extraction helpers
    assert callable(getattr(ie, "_extract_formats", None))
    assert callable(getattr(ie, "_real_extract", None))

# Generated at 2026-10-25 10:16:09.770411
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 10:16:11.306374
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

# Generated at 2026-10-25 10:16:32.401004
# Unit test for constructor of class PornerBrosIE