

# Generated at 2022-06-14 16:24:12.209213
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = url='http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    heiseIE = HeiseIE(url)
    assert heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:24:13.401641
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()


# Generated at 2022-06-14 16:24:25.415383
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(HeiseIE.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html') == True)
    assert(HeiseIE.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130') == True)
    assert(HeiseIE.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html?wt_mc=rss.ho.beitrag.atom') == True)

# Generated at 2022-06-14 16:24:26.414759
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:24:30.922300
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    mpegURL = HeiseIE(None)
    assert mpegURL._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Unit test to test if title is being parsed correctly

# Generated at 2022-06-14 16:24:34.221378
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
  # Test if HeiseIE instance can be created with HeiseIE as argument
  heiseIE = HeiseIE(HeiseIE.ie_key())
  assert heiseIE

# Generated at 2022-06-14 16:24:40.165947
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:24:49.208508
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()
    assert heiseie.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert not heiseie.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html?utm_source=rss')
    assert heiseie.IE_NAME == 'heise'

# Generated at 2022-06-14 16:24:50.726324
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(InfoExtractor())

# Generated at 2022-06-14 16:24:52.107628
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise is not None

# Generated at 2022-06-14 16:25:15.174769
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/ct/artikel/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html?wt_mc=rss.ho.beitrag.atom")
    assert ie.name == "heise"
    assert ie.url_re == "https?://(?:www\\.)?heise\\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\\.html"
    assert ie.expire_time == 1800

# Generated at 2022-06-14 16:25:16.612514
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    import doctest
    doctest.testmod(HeiseIE)

# Generated at 2022-06-14 16:25:23.915211
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie

    # instance of HeiseIE
    assert ie.__class__.__name__ == 'HeiseIE'

# Generated at 2022-06-14 16:25:34.176880
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:25:35.200464
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._TESTS

# Generated at 2022-06-14 16:25:45.338322
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    url = "https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html"
    video = ie.extract(url)
    assert video['id'] == "1_59mk80sf"
    assert video['title'] == "c't uplink 20.8: Staubsaugerroboter Xiaomi Vacuum 2, AR-Brille Meta 2 und Android rooten"

# Generated at 2022-06-14 16:25:51.701041
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.title == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert ie.description == 'md5:c934cbfb326c669c2bcabcbe3d3fcd20'

# Generated at 2022-06-14 16:26:01.940451
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:06.137361
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    extractor = HeiseIE()
    assert extractor.suitable('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')

# Generated at 2022-06-14 16:26:07.229901
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:25.684408
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.SUCCESS == 'SUCCESS'


# Generated at 2022-06-14 16:26:26.126356
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    print(ie)

# Generated at 2022-06-14 16:26:33.838041
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()
    assert heiseie.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') == True
    assert heiseie.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html') == True
    assert heiseie.suitable('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html') == True

# Generated at 2022-06-14 16:26:35.345604
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_class = HeiseIE(HeiseIE.ie_key())
    assert test_class

# Generated at 2022-06-14 16:26:38.945428
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
  ie = HeiseIE()
  assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:44.365080
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'
    return HeiseIE._real_extract(HeiseIE(), url)

# Generated at 2022-06-14 16:26:50.562307
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    url_to_test = url
    h = HeiseIE()
    assert(url_to_test == h.url)
    return h

# Generated at 2022-06-14 16:26:51.904807
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie is not None

# Generated at 2022-06-14 16:26:55.425128
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'


# Generated at 2022-06-14 16:26:57.012184
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:27:44.727676
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    ie_Heise = HeiseIE(url)
    print(ie_Heise.version)
    print(ie_Heise.version_id)
    print(ie_Heise.ie_key())
    assert ie_Heise.ie_key() == "Heise"

# Generated at 2022-06-14 16:27:49.531180
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    ie = HeiseIE(url)
    assert ie.url == url

# Generated at 2022-06-14 16:27:50.975100
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE(None)
    assert isinstance(heiseIE, HeiseIE)

# Generated at 2022-06-14 16:27:51.844350
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    video = HeiseIE()

# Generated at 2022-06-14 16:27:55.960826
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise='http://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    h = HeiseIE(heise)
    assert h.url == heise
    h = HeiseIE('')
    assert h.url == ''

# Generated at 2022-06-14 16:27:56.764444
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    pass

# Generated at 2022-06-14 16:27:57.594149
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie

# Generated at 2022-06-14 16:28:09.832105
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info=HeiseIE('https://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html').extract()
    info.get('id') == '3214137'
    info.get('title') == "c't uplink 20.8: Staubsaugerroboter Xiaomi Vacuum 2, AR-Brille Meta 2 und Android rooten"

# Generated at 2022-06-14 16:28:10.462160
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    pass

# Generated at 2022-06-14 16:28:15.321119
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert(heiseIE._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html')
    assert(heiseIE.ie_key() == 'heise')

# Generated at 2022-06-14 16:29:57.378134
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Testing with working code
    # Sources: https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html
    #          https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html
    heise_ie = HeiseIE()

# Generated at 2022-06-14 16:29:58.295877
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(HeiseIE)

# Generated at 2022-06-14 16:29:59.623910
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie.IE_NAME == 'heise'

# Generated at 2022-06-14 16:30:00.529294
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(None)

# Generated at 2022-06-14 16:30:02.845058
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    my_test = HeiseIE()
    print('Unit test for constructor of class HeiseIE:')
    print('type: ' + str(my_test))


# Generated at 2022-06-14 16:30:03.963213
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    d=HeiseIE()
    print(d.ie_key())

# Generated at 2022-06-14 16:30:04.706131
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()


# Generated at 2022-06-14 16:30:05.400319
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()

# Generated at 2022-06-14 16:30:06.186932
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:30:14.465058
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    id = '1_kkrq94sm'
    title = "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"

    ie = HeiseIE(None)
    assert ie.suitable(url) == True
    assert ie.extract(url)['id'] == id
    assert ie.extract(url)['title'] == title

# Generated at 2022-06-14 16:33:39.590784
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()

# Generated at 2022-06-14 16:33:41.656278
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE({})
    assert obj is not None

# Generated at 2022-06-14 16:33:50.964600
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:33:51.510825
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()
    assert obj != None

# Generated at 2022-06-14 16:33:54.438353
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # pylint: disable=too-many-function-args
    heise = HeiseIE(InfoExtractor())
    assert heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
