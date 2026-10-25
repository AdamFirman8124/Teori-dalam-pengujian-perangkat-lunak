

# Generated at 2026-10-25 05:16:02.875052
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:16:28.522445
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 05:16:30.586511
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:16:48.255896
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:16:50.683613
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:16:53.115421
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:16:55.585939
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:16:58.437425
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:00.966349
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:03.418992
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:05.836400
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:08.269061
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:10.688399
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:13.106105
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:15.524746
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:17.943184
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:17:20.366045
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:17:22.783116
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:17:25.201566
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:27.620213
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:30.049073
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:32.467854
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:17:34.897355
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:17:37.308403
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:17:39.728924
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:42.147314
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:44.566280
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:46.982970
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:49.401296
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:51.821247
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:17:54.238722
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:56.660440
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:17:59.080605
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:18:01.502698
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:18:03.923539
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:18:06.343951
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:18:08.767257
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:18:11.194086
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:18:13.612016
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:18:16.031565
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:18:18.451349
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:18:20.868490
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:18:23.286913
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:25.705466
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:28.126576
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:30.545564
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:32.963778
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:35.382562
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:37.801742
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:18:40.220692
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:18:42.638727
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:18:45.056658
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:47.475842
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:49.900928
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:52.317292
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:54.735101
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:57.174590
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:18:59.573049
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:19:01.990936
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:19:04.409202
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:19:14.052960
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 05:19:15.438826
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:19:24.369575
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 05:19:25.750815
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:19:27.341126
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:19:56.875904
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None

    # Verify that the initialized extractor uses its URL pattern correctly.
    assert extractor._match_id('mtg:418113') == '418113'
    assert extractor._match_id(
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113'
    ) == '418113'

# Generated at 2026-10-25 05:19:58.365539
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:20:09.842226
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # ViafreeIE inherits its constructor from InfoExtractor
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

    downloader = object()
    extractor = ViafreeIE(downloader)

    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 05:20:12.445048
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:20:14.878185
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:20:17.286241
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:20:19.708150
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:22.122897
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:24.549808
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:26.967761
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:29.386672
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:31.804901
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:34.225804
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:20:36.645465
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:20:39.064937
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 05:20:41.484214
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:43.905723
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:46.322143
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:48.739286
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:51.156879
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:53.576780
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:20:55.037136
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:21:16.940352
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None

# Generated at 2026-10-25 05:21:18.343296
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:21:41.382333
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 05:21:43.804255
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:21:46.223070
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:21:48.647974
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:21:51.066833
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:21:53.488159
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:21:56.047424
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:21:58.463811
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 05:22:03.296694
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

# Generated at 2026-10-25 05:22:04.709135
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:22:14.764760
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 05:22:25.311203
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 05:22:34.425159
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-25 05:22:53.383299
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-25 05:22:55.801732
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 05:23:03.306104
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE(None)

# Generated at 2026-10-25 05:23:21.548102
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('mtg:418113')
    assert not ie.suitable('http://www.example.com/video/418113')
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'

# Generated at 2026-10-25 05:23:44.676058
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None
    assert extractor.suitable('mtg:418113')
    assert extractor.suitable(
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113')

# Generated at 2026-10-25 05:23:53.591426
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-25 05:24:18.687175
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()

    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 05:24:27.596903
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._GEO_BYPASS is False
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-25 05:24:29.266975
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:24:39.049758
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 05:24:46.935755
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 05:24:48.470052
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:24:57.584223
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-25 05:25:21.648919
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 05:25:23.042012
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # constructor should work with and without downloader
    ie = TVPlayHomeIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # no custom __init__ -> uses InfoExtractor.__init__(downloader=None)
    assert ie._downloader is None

    downloader = object()
    ie_with_dl = TVPlayHomeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # _VALID_URL / _match_id behaviour
    assert ie._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

    assert ie._match_id(
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ) == '10280317'

    assert TVPlayHomeIE.suitable(
        'https://play.tv3.lt/aferistai-10047125'
    )
    assert TVPlayHomeIE.suitable(
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317'
    )
    assert not TVPlayHomeIE.suitable(
        'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    )

# Generated at 2026-10-25 05:25:30.455889
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False