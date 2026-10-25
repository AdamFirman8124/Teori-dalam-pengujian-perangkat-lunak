

# Generated at 2026-10-25 04:26:15.961307
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:26:18.372378
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:26:20.787351
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:26:27.904209
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

# Generated at 2026-10-25 04:26:37.517867
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 04:26:49.427308
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

# Generated at 2026-10-25 04:26:51.845086
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:26:54.529673
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:26:56.945334
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:26:59.500786
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:27:01.915808
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:27:04.331043
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:27:06.746661
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:09.162233
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:11.577625
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:13.992940
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:16.411637
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:18.831557
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:21.247192
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:23.662054
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:26.076709
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:27:28.492375
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:27:30.908120
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:27:33.325018
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:27:35.751222
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:27:46.238056
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE(None)

# Generated at 2026-10-25 04:27:47.670855
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

# Generated at 2026-10-25 04:27:57.195373
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-25 04:27:58.576860
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

# Generated at 2026-10-25 04:27:59.955325
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

# Generated at 2026-10-25 04:28:01.368047
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

# Generated at 2026-10-25 04:28:09.177696
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-25 04:28:11.595122
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:28:14.009797
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:28:16.424821
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:28:18.840051
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:28:21.255298
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:28:23.671846
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:28:26.086860
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:28:28.501860
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:28:30.916879
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:28:33.332443
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:28:35.748043
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:28:43.003484
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE(None)

# Generated at 2026-10-25 04:28:51.375021
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-25 04:28:52.797778
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

# Generated at 2026-10-25 04:29:10.916590
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:29:13.332040
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:29:15.746870
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:29:18.161119
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:29:20.575338
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:29:23.160318
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:29:25.674850
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:29:28.090456
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:29:30.505735
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:29:32.920661
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:29:35.335358
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:29:37.753881
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:29:40.167153
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:29:45.645835
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 04:29:54.037849
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

    extractor_without_downloader = ViafreeIE()
    assert extractor_without_downloader._downloader is None
    assert extractor_without_downloader._ready is False

# Generated at 2026-10-25 04:29:55.467397
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

# Generated at 2026-10-25 04:30:03.662198
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-25 04:30:14.104863
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 04:30:16.523596
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:30:18.938580
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:30:21.355421
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:30:23.946099
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:26.372557
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:28.778190
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:31.193848
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:30:33.609699
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:30:36.028055
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:30:38.449971
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:40.871188
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:43.285803
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:45.701752
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:30:48.117897
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:30:50.535454
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:30:52.949085
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:55.363681
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:30:57.777959
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:31:00.192617
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:31:02.608782
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:31:05.024678
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:31:07.441950
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:31:14.110758
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 04:31:23.085299
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 04:31:40.956430
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

# Generated at 2026-10-25 04:31:50.309478
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'Viafree'
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 04:31:52.726706
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:31:55.142903
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:31:57.670388
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:32:00.275589
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:32:02.691550
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:32:05.105731
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:32:08.695207
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:32:11.109539
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:32:17.906722
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 04:32:41.560881
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 04:32:44.089591
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:32:46.664377
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:32:49.190464
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:32:51.712060
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:32:54.128063
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:32:56.544789
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:32:59.080928
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:01.598607
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:04.013630
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:06.428528
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:33:08.843254
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:33:11.260156
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:33:13.674416
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:33:16.089149
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:33:18.503702
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:33:20.918601
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:23.332703
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:25.748152
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:28.166110
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:33:30.581339
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:33:32.995924
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:33:35.411525
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:33:37.836918
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:33:40.251374
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 04:33:45.062606
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:47.479459
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:49.895561
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:52.311366
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:54.726505
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:57.142428
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:33:59.558752
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:34:01.974836
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:34:04.388642
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 04:34:06.803025
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:34:09.221555
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:34:15.156211
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 04:34:38.503677
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 04:34:48.128617
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 04:34:49.561580
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

# Generated at 2026-10-25 04:35:05.330744
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, TVPlayIE)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._VALID_URL

# Generated at 2026-10-25 04:35:07.748837
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:35:10.162015
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:35:12.575754
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:35:14.991846
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:35:20.896404
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE(None)

# Generated at 2026-10-25 04:35:28.986079
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

# Generated at 2026-10-25 04:35:30.419520
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

# Generated at 2026-10-25 04:35:31.853028
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

# Generated at 2026-10-25 04:35:43.325064
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-25 04:35:44.732649
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

# Generated at 2026-10-25 04:36:09.332808
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 04:36:11.749876
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:36:14.278711
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 04:36:16.699264
# Unit test for constructor of class TVPlayIE