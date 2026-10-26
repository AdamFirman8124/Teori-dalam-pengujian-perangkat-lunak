

# Generated at 2026-10-25 11:19:49.929015
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

# Generated at 2026-10-25 11:20:07.644794
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 11:20:52.492097
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:21:15.020709
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie.ie_key() is None or isinstance(ie.ie_key(), str)
    assert isinstance(ie._VALID_URL, str)

    match = re.match(
        PornerBrosIE._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match is not None
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    match_embed = re.match(PornerBrosIE._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert match_embed is not None
    assert match_embed.group('id') == '181369'

# Generated at 2026-10-25 11:21:16.543474
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

# Generated at 2026-10-25 11:21:24.645605
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

# Generated at 2026-10-25 11:21:29.404739
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

# Generated at 2026-10-25 11:21:30.793483
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

# Generated at 2026-10-25 11:21:32.538027
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

# Generated at 2026-10-25 11:21:33.961524
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

# Generated at 2026-10-25 11:21:36.830803
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:21:41.353727
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie.ie_key() is None or isinstance(ie.ie_key(), str)
    assert isinstance(ie._VALID_URL, str)

    match = re.match(
        PornerBrosIE._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match is not None
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    match_embed = re.match(PornerBrosIE._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert match_embed is not None
    assert match_embed.group('id') == '181369'

# Generated at 2026-10-25 11:21:58.540077
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

# Generated at 2026-10-25 11:22:01.060571
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

# Generated at 2026-10-25 11:22:03.972438
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:22:06.624392
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:22:09.042216
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:22:11.456904
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:22:13.875237
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:22:16.289565
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:22:18.704453
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:22:21.151619
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:22:23.953258
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:22:26.372222
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:22:28.782292
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:22:31.198607
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:22:33.617085
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:22:36.033586
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:22:38.448641
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:22:40.861055
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:22:43.278354
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:22:45.693869
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:22:48.112276
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:22:50.528593
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:22:52.947882
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:22:55.362432
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:22:57.773243
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:23:00.190008
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:23:06.322506
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 11:23:39.691837
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 11:23:58.453272
# Unit test for constructor of class FuxIE
def test_FuxIE():ie = FuxIE()

# Generated at 2026-10-25 11:23:59.884752
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

# Generated at 2026-10-25 11:24:16.373217
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

# Generated at 2026-10-25 11:24:18.793472
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:24:21.205757
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:24:23.621751
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:24:26.036064
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:24:28.450626
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:24:30.992012
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:24:33.406561
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:24:35.821085
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:24:50.760102
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 11:24:52.211698
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

# Generated at 2026-10-25 11:25:10.117702
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 11:25:12.533660
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:25:14.950490
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:25:17.367724
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:25:19.784303
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:25:22.197339
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:25:24.611668
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:25:27.026772
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:25:29.443652
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:25:31.857683
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:25:34.270176
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:25:36.684401
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:25:39.098542
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:25:41.516363
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:25:43.929281
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:25:46.346023
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:25:48.864605
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:25:51.212025
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:25:53.652523
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:25:56.067137
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:25:58.483170
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:26:00.899823
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:26:03.377574
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:05.779173
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:08.193264
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:10.608319
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:26:13.024541
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:26:15.441761
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:26:17.860857
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:20.270573
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:22.688137
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:25.102714
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:26:27.517307
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:26:29.937277
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:26:32.355681
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:34.767419
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:37.182706
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:26:39.597930
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:42.043136
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:44.431455
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:46.844058
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:49.258032
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:51.799842
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:54.135891
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:56.550270
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:26:58.966566
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:27:01.383461
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:03.797076
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:06.211061
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:08.625598
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:11.040541
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:13.457670
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:15.874886
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:27:18.290395
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:27:20.704221
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:27:23.119275
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:25.533112
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:27.947353
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:30.366065
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:27:32.814698
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:27:35.195307
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:27:37.609276
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:27:43.136606
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 11:27:44.652092
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

# Generated at 2026-10-25 11:28:12.334316
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

# Generated at 2026-10-25 11:28:14.919002
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:17.476211
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:19.893379
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:22.305384
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:28:24.721420
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:28:27.390548
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:28:30.882975
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:33.300885
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:35.714870
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:38.128952
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:40.543680
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:42.958620
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:45.372836
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:28:47.788639
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:28:50.205650
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:28:52.617669
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:55.034381
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:57.446962
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 11:28:59.860810
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:29:02.276925
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:29:04.688396
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 11:29:07.103652
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:09.520642
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:11.933952
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:14.348676
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:29:16.765315
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:29:19.179097
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:29:21.592716
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:29:24.008071
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:29:26.422633
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 11:29:28.837476
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:29:31.252011
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:29:33.666035
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 11:29:36.080231
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:38.495910
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:40.910745
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:47.197533
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:49.611893
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 11:29:52.024063
# Unit test for constructor of class FourTubeBaseIE