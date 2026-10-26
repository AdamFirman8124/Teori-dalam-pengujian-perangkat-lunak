

# Generated at 2026-10-25 11:08:15.255567
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 11:08:28.791588
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:08:35.867772
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

# Generated at 2026-10-25 11:08:43.987248
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 11:08:46.681438
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:08:49.099552
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:08:51.515062
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:08:53.931859
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 11:08:56.353309
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 11:08:58.765725
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 11:09:01.220583
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:09:03.905911
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

# Generated at 2026-10-25 11:09:05.683224
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:09:07.158264
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:09:16.289799
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
    assert extractor.ie_key() == 'TVPlay'

# Generated at 2026-10-25 11:09:28.689028
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:09:38.696659
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 11:09:40.297470
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:09:49.047459
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 11:09:56.142932
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None

# Generated at 2026-10-25 11:10:07.573123
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor.ie_key() == 'TVPlay'

# Generated at 2026-10-25 11:10:08.981115
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:10:16.891555
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
    assert extractor.ie_key() == 'TVPlay'

# Generated at 2026-10-25 11:10:23.259207
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:10:24.746224
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:10:26.311188
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:10:35.634957
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor.ie_key() == 'TVPlay'

# Generated at 2026-10-25 11:10:37.220443
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:10:47.137985
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert TVPlayIE.ie_key() == 'TVPlay'

# Generated at 2026-10-25 11:10:55.100138
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:10:56.638687
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:10:59.045502
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:11:01.741441
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:11:10.241349
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 11:11:17.302287
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._VALID_URL

# Generated at 2026-10-25 11:11:28.567772
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

# Generated at 2026-10-25 11:11:36.236475
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    downloader = object()
    extractor = TVPlayHomeIE(downloader)

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 11:11:37.684523
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:11:39.118640
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:11:40.527672
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:11:46.389116
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None

# Generated at 2026-10-25 11:11:53.590534
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor.suitable('mtg:418113')

# Generated at 2026-10-25 11:11:56.654085
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:12:03.596278
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

# Generated at 2026-10-25 11:12:06.133262
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:12:08.548902
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:12:10.962505
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:12:12.500252
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:12:13.934773
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:12:15.643143
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:12:22.230481
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._VALID_URL

# Generated at 2026-10-25 11:12:23.867886
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:12:25.679790
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:12:36.003332
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 11:12:45.808780
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()

    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 11:12:54.079184
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 11:12:56.500850
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 11:12:59.118563
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 11:13:01.543909
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 11:13:03.959506
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:13:06.379242
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:13:08.965795
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:13:11.617588
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:13:17.730773
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():extractor = TVPlayHomeIE(None)

# Generated at 2026-10-25 11:13:19.676977
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:13:29.499477
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor.ie_key() == 'TVPlay'

# Generated at 2026-10-25 11:13:36.489520
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 11:13:47.242598
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:13:58.896464
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

# Generated at 2026-10-25 11:14:06.173208
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

# Generated at 2026-10-25 11:14:08.796880
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:14:11.213559
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:14:13.629535
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 11:14:16.045516
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 11:14:23.995946
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 11:14:31.873649
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:14:33.303919
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:14:34.735415
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:14:43.032025
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 11:14:44.771605
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:15:04.630281
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 11:15:06.176669
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:15:14.576170
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:15:15.952535
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:15:17.300284
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:15:18.770711
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:15:20.152758
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:15:21.637577
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:15:23.172473
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:15:32.901777
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 11:15:48.873376
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:15:50.419763
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:15:51.947614
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:16:01.059881
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None

# Generated at 2026-10-25 11:16:02.487398
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:16:06.694388
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:16:08.232017
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:16:18.161702
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

# Generated at 2026-10-25 11:16:20.673347
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:16:28.912792
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._VALID_URL

# Generated at 2026-10-25 11:17:00.655131
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:17:07.824899
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:17:12.582262
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:17:14.071161
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 11:17:23.216519
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 11:17:31.489849
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

# Generated at 2026-10-25 11:17:33.015532
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 11:17:42.336196
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor.ie_key() == 'TVPlay'

# Generated at 2026-10-25 11:17:48.890936
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 11:17:56.572358
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

    # Verify that constructor initialization leaves the extractor usable.
    assert extractor.suitable('mtg:418113')
    assert extractor._match_id('mtg:418113') == '418113'