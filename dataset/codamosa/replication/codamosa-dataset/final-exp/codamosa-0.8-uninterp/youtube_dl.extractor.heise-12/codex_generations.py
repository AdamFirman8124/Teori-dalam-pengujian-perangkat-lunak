

# Generated at 2022-06-14 16:24:05.209787
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert heiseIE is not None
    assert heiseIE.ie_key() == 'heise'
    assert heiseIE.ie_key() == 'Heise'

# Generated at 2022-06-14 16:24:08.503261
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_ = globals()['HeiseIE']
    instance = class_()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:24:20.289818
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

    heiseie = HeiseIE()


# Generated at 2022-06-14 16:24:22.366175
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:24:24.061346
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    assert h is not None

# Generated at 2022-06-14 16:24:25.231027
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Constructor should fail without a video_id
    with pytest.raises(TypeError):
        HeiseIE()

# Generated at 2022-06-14 16:24:34.310553
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
  input = 'http://www.heise.de/video/artikel/-1-488975.html'
  assert HeiseIE()._VALID_URL(input)
  assert HeiseIE().suitable(input)
  assert HeiseIE().extract(input).get('id') == '1_s1s3lx61'
  assert HeiseIE().extract(input).get('title') == 'Vorhut der neuen Revolution - ZdF'
  input = 'http://www.heise.de/newsticker/meldung/Spaetgestarteter-Bericht-Internet-Daten-von-NSA-Zielen-ausgewertet-2102729.html?wt_mc=rss.ho.beitrag.atom'
  assert HeiseIE()._VALID_URL(input)


# Generated at 2022-06-14 16:24:34.879395
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    pass

# Generated at 2022-06-14 16:24:45.110578
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:24:54.905851
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie.ie_key() == 'heise'
    assert ie.suitable('http://www.heise.de/example')
    assert ie.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert not ie.suitable('https://www.youtube.com/watch?v=AQmBkPdG9fg')
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:06.936864
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("url", "title", "description", "thumbnail")
    assert str(ie) == "<HeiseIE url:url title:title description:description thumbnail:thumbnail>"

# Generated at 2022-06-14 16:25:12.426534
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    obj = InfoExtractor.legacy_request(url)
    assert obj.__class__.__name__ == 'HeiseIE', 'unexpected constructor of class HeiseIE'

# Generated at 2022-06-14 16:25:24.760913
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_name() == 'Heise'
    assert ie.suitable(None) == False
    assert ie.suitable('') == False
    assert ie.suitable('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html') == True
    assert ie.suitable('http://www.heise.de/newsticker/meldung/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html?wt_mc=rss.ho.beitrag.atom') == True

# Generated at 2022-06-14 16:25:31.381079
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    _url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    obj = HeiseIE()
    assert obj._match_id(_url) == '2404147'
    assert obj._real_extract(_url).keys() == ['id', 'title', 'description', 'thumbnail', 'timestamp', 'formats']

# Generated at 2022-06-14 16:25:43.811823
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    HeiseIE("http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html")
    HeiseIE("https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html")

# Generated at 2022-06-14 16:25:44.439562
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:25:47.099377
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE(None, None)
    assert heise_ie.__name__ == 'HeiseIE'
    assert heise_ie.test() is False

# Generated at 2022-06-14 16:25:48.170933
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()

# Generated at 2022-06-14 16:25:52.251274
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    print("The instance was created:", instance)
    # test the method _real_extract of the created instance
    print("extracting information from URL: ", instance._real_extract("url"))

# Generated at 2022-06-14 16:25:58.297063
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from . import YTDLCustomIE
    HeiseIE = YTDLCustomIE('HeiseIE', ['heise.de'], dict(
        name='Heise',
        ie='HeiseIE'
    ))
    assert HeiseIE.name == 'Heise'
    assert HeiseIE.ie == 'HeiseIE'
    assert HeiseIE.hosts == ['heise.de']

# Generated at 2022-06-14 16:26:25.093684
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert (heise_ie._VALID_URL
            == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html')
    assert heise_ie._TESTS[2]['url'] == 'https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'

# Generated at 2022-06-14 16:26:29.491685
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert HeiseIE.suitable('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert not HeiseIE.suitable('http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html')

# Generated at 2022-06-14 16:26:32.317884
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:41.847627
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.suitable('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html') == True
    assert HeiseIE.suitable('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html') == True

# Generated at 2022-06-14 16:26:44.514060
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Constructor test of HeiseIE"""
    instance = HeiseIE({})
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:26:45.846055
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE({})
    assert instance.ie

# Generated at 2022-06-14 16:26:56.380187
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()

    # Test when using youtube links
    webpage = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    assert heise_ie._extract_urls(webpage) == ['https://www.youtube.com/watch?v=6kmWbXleKW4']

    # Test when using kaltura links
    webpage = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'

# Generated at 2022-06-14 16:26:57.879979
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:26:58.982862
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()

# Generated at 2022-06-14 16:27:06.972805
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie.__name__ == 'heise'
    assert ie.ie_key() == 'heise'
    assert ie.server_url == 'www.heise.de'
    assert ie.short_name() == 'heise'

# Generated at 2022-06-14 16:27:56.714367
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL == HeiseIE.VALID_URL
    assert HeiseIE._TESTS == HeiseIE.TESTS

# Generated at 2022-06-14 16:28:05.340365
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    heiseIE = HeiseIE()
    assert heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert heiseIE.ie_key() == 'Heise'


# Generated at 2022-06-14 16:28:07.099135
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Test whether constructor of HeiseIE works."""
    ie=HeiseIE()

# Generated at 2022-06-14 16:28:07.594702
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    hie = HeiseIE()


# Generated at 2022-06-14 16:28:12.863840
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.set_test_source_url(
        'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.get_video_id('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') == '2404147'
#    ie.download_video()

# Generated at 2022-06-14 16:28:23.596988
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    x = HeiseIE(None)
    assert x._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:24.895467
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()



# Generated at 2022-06-14 16:28:35.159699
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    url = r'https://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html'
    id = r'3214137'
    exp_title = r'c\u2019t uplink, Folge 20.8: Staubsaugerroboter Xiaomi Vacuum 2, AR-Brille Meta 2 und Android rooten'
    exp_description = r'md5:f50fe044d3371ec73a8f79fcebd74afc'
    exp_timestamp = 1517567237

# Generated at 2022-06-14 16:28:40.791818
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE.HeiseIE(None)
    heise_ie.add_format('test_format', 'test_url', 'test_label')
    heise_ie.add_format('test_format2', 'test_url2', 'test_label2')
    heise_ie.add_format('test_format', 'test_url3', 'test_label3')
    expected = [('test_format3', 'test_url3', 'test_label3'),
                ('test_format2', 'test_url2', 'test_label2')]
    assert heise_ie.formats == expected, 'Expected %s got %s' %(
        expected, heise_ie.formats)

# Generated at 2022-06-14 16:28:43.822954
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Test constructor of class HeiseIE"""
    heise = HeiseIE()
    assert heise.ie_key() == 'heise'
    assert heise.ie_name() == 'heise'

# Generated at 2022-06-14 16:30:33.679998
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    class_name = 'HeiseIE'
    item = HeiseIE._build_url_result(url, None, class_name, {})
    assert item['url'] == url
    assert item['ie_key'] == class_name

# Generated at 2022-06-14 16:30:35.576488
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    # check if HeiseIE constructor is working
    assert ie._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:30:38.847992
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE('www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') is not None

# Generated at 2022-06-14 16:30:42.978869
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.key() == 'HeiseIE'

# Generated at 2022-06-14 16:30:51.685966
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert ie.id == "1_kkrq94sm"
    assert ie.title == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert ie.description == "md5:c934cbfb326c669c2bcabcbe3d3fcd20"
    assert ie.formats[0].format_note == "mp4_720p"
    assert ie.formats[0].height == 720
    assert ie.formats[2].format_note == "mp4_360p"

# Generated at 2022-06-14 16:31:01.910105
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from .test_download import get_testcases
    return get_testcases(HeiseIE, [
        ('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html', {
            'skip': 'Geoblocked',
        }),
        ('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html', {
            'skip': 'Geoblocked',
        }),
    ])

# Generated at 2022-06-14 16:31:08.400993
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("heise", "www.heise.de", True)
    test_url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    info_dict = ie.extract(test_url)
    assert info_dict["id"] == '1_ntrmio2s'

# Generated at 2022-06-14 16:31:11.803598
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # construct HeiseIE instance
    heise_ie = HeiseIE()
    # Check expected type is given
    assert(isinstance(heise_ie, InfoExtractor))

# Generated at 2022-06-14 16:31:22.072674
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.__name__ == 'HeiseIE'
    assert HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert HeiseIE._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert HeiseIE._TESTS[0]['info_dict']['id'] == '1_kkrq94sm'

# Generated at 2022-06-14 16:31:24.159686
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.extract('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')