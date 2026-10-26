

# Generated at 2026-10-25 07:47:00.375447
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')

# Generated at 2026-10-25 07:47:02.792596
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:47:05.208140
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:47:07.623580
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:47:10.039517
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:47:12.451125
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:47:14.863497
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:47:17.277794
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:19.691505
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:22.106614
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:24.522601
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:26.936407
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:29.357916
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:31.774669
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:47:34.194552
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:47:36.612198
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:47:39.026272
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:47:41.441367
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:47:43.855753
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:47:46.270013
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:48.684120
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:51.099492
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:53.579014
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:55.943750
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:47:58.360185
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:48:00.779217
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:48:03.193281
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:48:05.610033
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:48:08.023418
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:48:10.437830
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:48:12.853100
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:48:15.267483
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:48:22.295292
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():extractor = FourTubeBaseIE()

# Generated at 2026-10-25 07:48:39.406360
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:48:45.029167
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:48:46.464643
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:48:47.871876
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:48:56.497850
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()

    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 07:49:04.961921
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor created an instance of the right class
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes set correctly
    assert ie.IE_NAME == 'porntube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches expected URL forms and captures groups
    m = ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m
    match = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('id') == '7089759'
    assert match.group('display_id') == 'teen-couple-doing-anal'
    assert match.group('kind') is None

    # Embed and mobile URLs also match
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('kind') in (None, 'www', 'm')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')
    assert not ie.suitable('https://www.porntube.com/videos/')

    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()

# Generated at 2026-10-25 07:49:07.316875
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:49:09.855530
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:49:12.273260
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:49:14.687302
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:49:17.098939
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:49:19.513185
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:49:21.927353
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:49:24.342081
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:49:26.760284
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:49:29.170385
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:49:31.583702
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:49:39.198308
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():extractor = FourTubeBaseIE(None)

# Generated at 2026-10-25 07:49:40.631462
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor created an instance of the right class
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes set correctly
    assert ie.IE_NAME == 'porntube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches expected URL forms and captures groups
    m = ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m
    match = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('id') == '7089759'
    assert match.group('display_id') == 'teen-couple-doing-anal'
    assert match.group('kind') is None

    # Embed and mobile URLs also match
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('kind') in (None, 'www', 'm')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')
    assert not ie.suitable('https://www.porntube.com/videos/')

    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()

# Generated at 2026-10-25 07:49:48.620707
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()

    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-25 07:49:56.514171
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert isinstance(ie, FuxIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert re.match(
        ie._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-25 07:50:03.352566
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow')
    assert extractor.suitable('https://www.fux.com/embed/195359')

# Generated at 2026-10-25 07:50:04.800967
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:50:06.158880
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:50:07.598980
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:50:08.999457
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:50:10.633718
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:50:12.069986
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:50:14.489791
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:50:17.016658
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:50:19.650633
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:50:22.065065
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:50:24.479616
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:50:26.898371
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:50:29.521044
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:50:31.935993
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:50:39.102091
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE(None)

# Generated at 2026-10-25 07:50:40.537338
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:50:41.957377
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:50:52.722922
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()

    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 07:50:54.088721
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor created an instance of the right class
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes set correctly
    assert ie.IE_NAME == 'porntube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches expected URL forms and captures groups
    m = ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m
    match = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('id') == '7089759'
    assert match.group('display_id') == 'teen-couple-doing-anal'
    assert match.group('kind') is None

    # Embed and mobile URLs also match
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('kind') in (None, 'www', 'm')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')
    assert not ie.suitable('https://www.porntube.com/videos/')

    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()

# Generated at 2026-10-25 07:50:55.487832
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor created an instance of the right class
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes set correctly
    assert ie.IE_NAME == 'porntube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches expected URL forms and captures groups
    m = ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m
    match = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('id') == '7089759'
    assert match.group('display_id') == 'teen-couple-doing-anal'
    assert match.group('kind') is None

    # Embed and mobile URLs also match
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('kind') in (None, 'www', 'm')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')
    assert not ie.suitable('https://www.porntube.com/videos/')

    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()

# Generated at 2026-10-25 07:51:04.663324
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 07:51:06.097842
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

# Generated at 2026-10-25 07:51:07.837491
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

# Generated at 2026-10-25 07:51:18.692571
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert isinstance(ie, FuxIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow'
    )

# Generated at 2026-10-25 07:51:28.215734
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()

    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._VALID_URL == FuxIE._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 07:51:30.669228
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:51:36.958026
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():extractor = FourTubeBaseIE(None)

# Generated at 2026-10-25 07:51:38.391860
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor created an instance of the right class
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes set correctly
    assert ie.IE_NAME == 'porntube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches expected URL forms and captures groups
    m = ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m
    match = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('id') == '7089759'
    assert match.group('display_id') == 'teen-couple-doing-anal'
    assert match.group('kind') is None

    # Embed and mobile URLs also match
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('kind') in (None, 'www', 'm')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')
    assert not ie.suitable('https://www.porntube.com/videos/')

    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()

# Generated at 2026-10-25 07:51:39.834304
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:51:41.238392
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:51:51.689056
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:51:56.606931
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE(None)

# Generated at 2026-10-25 07:51:58.055267
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

# Generated at 2026-10-25 07:51:59.697193
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

# Generated at 2026-10-25 07:52:01.245302
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor created an instance of the right class
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes set correctly
    assert ie.IE_NAME == 'porntube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches expected URL forms and captures groups
    m = ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m
    match = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('id') == '7089759'
    assert match.group('display_id') == 'teen-couple-doing-anal'
    assert match.group('kind') is None

    # Embed and mobile URLs also match
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('kind') in (None, 'www', 'm')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')
    assert not ie.suitable('https://www.porntube.com/videos/')

    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()

# Generated at 2026-10-25 07:52:09.932031
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert isinstance(ie, FuxIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie.ie_key() == 'Fux'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow'
    )

# Generated at 2026-10-25 07:52:11.460740
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

# Generated at 2026-10-25 07:52:14.195335
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:52:16.804549
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:52:19.218377
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:52:21.632668
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:52:24.049325
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:52:26.463205
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:52:28.878197
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:52:31.466592
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:52:33.881628
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:52:36.293473
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:52:38.727870
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:52:41.139375
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:52:43.559448
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:52:45.973560
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:52:54.782406
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-25 07:52:56.215806
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

# Generated at 2026-10-25 07:53:05.024682
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

# Generated at 2026-10-25 07:53:12.395833
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert re.match(
        extractor._VALID_URL,
        'https://www.fux.com/video/195359/example-video',
    )

# Generated at 2026-10-25 07:53:14.660976
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

# Generated at 2026-10-25 07:53:24.274788
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')

# Generated at 2026-10-25 07:53:25.709358
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor created an instance of the right class
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes set correctly
    assert ie.IE_NAME == 'porntube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches expected URL forms and captures groups
    m = ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m
    match = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('id') == '7089759'
    assert match.group('display_id') == 'teen-couple-doing-anal'
    assert match.group('kind') is None

    # Embed and mobile URLs also match
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert match.group('kind') in (None, 'www', 'm')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/video')
    assert not ie.suitable('https://www.porntube.com/videos/')

    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()

# Generated at 2026-10-25 07:53:44.141316
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-25 07:53:46.739482
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:53:49.155885
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:53:56.018045
# Unit test for constructor of class FuxIE
def test_FuxIE():extractor = FuxIE()

# Generated at 2026-10-25 07:54:09.733463
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s'
    )

# Generated at 2026-10-25 07:54:11.235013
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:54:12.699996
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:54:14.132056
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

# Generated at 2026-10-25 07:54:22.735782
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 07:54:32.609161
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 07:54:35.174369
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:54:37.587817
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:54:40.005008
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:54:42.420801
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:54:44.852789
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:54:47.264389
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 07:54:49.678047
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:54:52.092443
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:54:54.506863
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:54:56.920583
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:55:07.801480
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():ie = FourTubeBaseIE()

# Generated at 2026-10-25 07:55:16.812394
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow'
    )

# Generated at 2026-10-25 07:55:18.451019
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

# Generated at 2026-10-25 07:55:20.093364
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

# Generated at 2026-10-25 07:55:21.439770
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 07:55:26.247183
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    m_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m_embed is not None
    assert m_embed.group('id') == '209733'
    assert m_embed.group('display_id') is None

    m_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-slug')
    assert m_mobile is not None
    assert m_mobile.group('kind') == 'm'
    assert m_mobile.group('id') == '209733'

    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/slug') is None

    assert ie.suitable('http://www.4tube.com/embed/209733') is True
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe') is True
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False

# Generated at 2026-10-25 07:55:38.624845
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s'
    )

# Generated at 2026-10-25 07:55:45.191804
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:55:47.605208
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:55:50.074866
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 07:55:52.521002
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:55:54.934920
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:55:57.350350
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 07:56:05.452601
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 07:56:06.991386
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

# Generated at 2026-10-25 07:56:17.740736
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._VALID_URL == FuxIE._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 07:56:19.174382
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

# Generated at 2026-10-25 07:56:29.761126
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()

    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._VALID_URL == FuxIE._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 07:56:40.883451
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')

# Generated at 2026-10-25 07:56:43.301045
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:56:45.963615
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:56:48.384277
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:56:50.794912
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:56:53.209673
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 07:56:55.624402
# Unit test for constructor of class FourTubeBaseIE