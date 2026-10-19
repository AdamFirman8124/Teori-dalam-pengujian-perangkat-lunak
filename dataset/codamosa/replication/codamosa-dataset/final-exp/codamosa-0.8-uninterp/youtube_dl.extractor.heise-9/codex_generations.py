

# Generated at 2022-06-14 16:24:13.510522
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    x = HeiseIE()
    ydl.add_info_extractor(x)
    url = "http://www.heise.de/newsletter/artikel-archiv/newsletter/heise-online-Top-Thema-66-4787998.html?wt_mc=nl.ho.topthema.rss"
    ydl.extract_info(url, download=False)

# Generated at 2022-06-14 16:24:16.968992
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('www.heise.de/newsticker/meldung/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html')

# Generated at 2022-06-14 16:24:18.456897
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE(None)
    assert isinstance(instance, HeiseIE)

# Generated at 2022-06-14 16:24:21.637700
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()._download_webpage('http://www.heise.de/', '')
    HeiseIE()._download_xml('http://www.heise.de/', '', {})

# Generated at 2022-06-14 16:24:27.018184
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    web_page = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    video = HeiseIE()
    video.download(web_page)

# Generated at 2022-06-14 16:24:34.372319
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    match = HeiseIE._VALID_URL.match('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert match is not None
    assert match.group('id') == '2404147'
    match = HeiseIE._VALID_URL.match('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert match is not None

# Generated at 2022-06-14 16:24:40.259084
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test for _VALID_URL regex
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    heise = HeiseIE(url)
    match = heise._VALID_URL.match(url)
    assert match is not None
    assert match.group('id') == '3814130'

    # Test for title
    m = {'fulltitle': '1', 'title': '2'}
    webpage = '<head><meta name="%s" content="%s"></head>'
    m_title = 'm title'
    div_title = 'div title'

# Generated at 2022-06-14 16:24:42.226295
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.extractor_key == 'heise'

# Generated at 2022-06-14 16:24:43.131721
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.extractor.class_name == 'HeiseIE'

# Generated at 2022-06-14 16:24:45.924452
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE(None)
    assert heiseIE.ie_key() == 'heise'

# Generated at 2022-06-14 16:25:03.896206
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie != None

# Generated at 2022-06-14 16:25:04.944534
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie_instance = HeiseIE()

# Generated at 2022-06-14 16:25:14.798375
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_name() == 'heise.de'
    assert 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html' in ie.working_webpage_regex()
    assert 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html' in ie.working_webpage_regex()

# Generated at 2022-06-14 16:25:16.367611
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    t = HeiseIE()
    assert t.ie_key() == 'Heise'

# Generated at 2022-06-14 16:25:21.657470
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'


# Generated at 2022-06-14 16:25:23.451589
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(None, None)

# Generated at 2022-06-14 16:25:33.790245
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    assert HeiseIE._match_id(url) == '3814130'
    assert HeiseIE._match_id('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html') == '3700244'
    assert HeiseIE._match_id('http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html') == '3214137'

# Generated at 2022-06-14 16:25:39.464857
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("")
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie.__name__ == 'Heise'
    assert ie.ie_key() == 'heise'
    assert ie.test()

# Generated at 2022-06-14 16:25:40.732950
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    impo

# Generated at 2022-06-14 16:25:42.091192
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()

# Generated at 2022-06-14 16:26:24.206729
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    import re
    url = ""
    url_pattern = r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    match = re.search(url_pattern, url)
    video_id = match.group('id')
    webpage = ""
    webpage_title = ""
    webpage_description = ""
    webpage_thumbnail = ""
    webpage_date = ""

    video = HeiseIE._real_extract(url, webpage, webpage_title, webpage_description, webpage_thumbnail, webpage_date)
    assert 'id' in video.keys()
    assert 'title' in video.keys()
    assert 'description' in video.keys()
    assert 'thumbnail' in video.keys()

# Generated at 2022-06-14 16:26:25.141948
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.ie_key() == 'Heise'

# Generated at 2022-06-14 16:26:29.630905
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.__class__.__name__ == 'HeiseIE', "Constructor should be HeiseIE"
#

# Generated at 2022-06-14 16:26:35.794485
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("https://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html")
    extracted = ie.extract("https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html")
    assert extracted.get("id") == "1_kkrq94sm"
    assert extracted.get("title") == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert extracted.get("description") == "md5:c934cbfb326c669c2bcabcbe3d3fcd20"

# Generated at 2022-06-14 16:26:40.045031
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:26:50.684534
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.suitable(
        'https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')
    assert ie.suitable('http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html')
    assert not ie.suitable('http://www.heise.de/newsticker/meldung/')
    assert not ie.suitable('http://www.heise.de')



# Generated at 2022-06-14 16:26:54.250959
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info = HeiseIE()._real_extract("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    print(info)

# Generated at 2022-06-14 16:26:55.552647
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Check if HeiseIE capable of creating an instance
    HeiseIE() == HeiseIE

# Generated at 2022-06-14 16:27:01.735353
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test = HeiseIE()
    assert test._type == "playlist"
    assert test._TITLE == "c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"

# Generated at 2022-06-14 16:27:04.187082
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    tester = HeiseIE()
    assert tester.ie_key() == "heise"

# Generated at 2022-06-14 16:28:35.487027
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:36.103445
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()

# Generated at 2022-06-14 16:28:36.595667
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    pass

# Generated at 2022-06-14 16:28:39.946415
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from . import _test_internet, _test_xml
    from .constructor import _test_constructor
    if _test_internet() and _test_xml():
        _test_constructor(HeiseIE, ['URL'])

# Generated at 2022-06-14 16:28:42.659171
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    hie = HeiseIE()
    assert hie
    assert hie.ie_key() == 'heise'
    assert hie.ie_name() == 'Heise.de'

# Generated at 2022-06-14 16:28:47.280669
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    ie.extract(url)

# Generated at 2022-06-14 16:28:48.635872
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE('foo', 'bar', 'baz')

# Generated at 2022-06-14 16:28:50.272117
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE(None, None)
    assert heiseIE is not None

# Generated at 2022-06-14 16:28:58.220113
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.url_re.match('https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')
    assert ie.url_re.match('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')

# Generated at 2022-06-14 16:29:03.244246
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Unit test for constructor of class HeiseIE
    :return:
    """
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    heise = HeiseIE()
    heise.extract(url)
    print("Unit test for constructor of class HeiseIE done.")

if __name__ == '__main__':
    test_HeiseIE()

# Generated at 2022-06-14 16:30:41.745642
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Create a HeiseIE instance
    ie = HeiseIE()

    # Make sure that it's the correct instance
    assert ie.ie_key() == 'heise'
    assert ie.info_dict() == {
        'id': 'heise',
        'title': 'heise video',
        'description': 'Video portal of the c\'t, iX and technology review magazines from the publisher of Heise',
        'extractor': 'heise'
    }

# Generated at 2022-06-14 16:30:49.711792
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    # test one of the URLs in test_data
    test_url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    HeiseIE._VALID_URL = \
        r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert heiseIE._match_id(test_url) == '2404147'



# Generated at 2022-06-14 16:30:50.506821
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert callable(HeiseIE)

# Generated at 2022-06-14 16:31:01.501165
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    def _run_test(url, *args, **kwargs):
        video_id = HeiseIE._match_id(url)
        webpage = HeiseIE._download_webpage(url, video_id)
        return HeiseIE._real_extract(url, webpage, video_id, *args, **kwargs)

    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    info_dict = _run_test(url)
    assert 'title' in info_dict, 'Failed to extract \'title\' of video'
    assert 'video_id' in info_dict, 'Failed to extract \'video_id\' of video'

# Generated at 2022-06-14 16:31:09.634573
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # url is the url to be tested
    url = 'https://www.heise.de/video/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'
    # regex is the regular expression to be tested.
    regex = HeiseIE._VALID_URL
    # match is the result of the match test.
    match = re.match(regex, url)
    # assert the expected result is returned.
    assert match is not None
    assert match.group('id') == '3959893'

# Generated at 2022-06-14 16:31:13.061625
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # pylint: disable=protected-access
    heise_ie = HeiseIE()
    assert heise_ie._TEST == 'test'  # pylint: disable=protected-access

# Generated at 2022-06-14 16:31:14.005874
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:31:15.305379
# Unit test for constructor of class HeiseIE
def test_HeiseIE():

    assert HeiseIE.ie_key() == 'Heise'

# Generated at 2022-06-14 16:31:17.183592
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Test the constructor of class HeiseIE"""
    HeiseIE()

# Generated at 2022-06-14 16:31:18.065588
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()