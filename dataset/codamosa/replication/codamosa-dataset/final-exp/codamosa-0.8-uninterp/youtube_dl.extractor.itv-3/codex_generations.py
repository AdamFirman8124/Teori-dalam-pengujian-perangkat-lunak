

# Generated at 2022-06-14 16:34:46.615614
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert itv.GEO_COUNTRIES == ['GB']
    assert itv.IE_NAME == 'itv'


# Generated at 2022-06-14 16:34:50.557489
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:34:56.968024
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from . import ITVBTCCIE
    from . import BrightcoveNewIE
    
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    itv_btcc_ie = ITVBTCCIE()
    itv_btcc_ie._real_extract(url)

    brightcove_new_ie = BrightcoveNewIE()
    brightcove_new_ie._real_extract(url)

# Generated at 2022-06-14 16:34:59.550429
# Unit test for constructor of class ITVIE
def test_ITVIE():

    '''ITVIE()
    '''

    test_obj = ITVIE()
    assert test_obj is not None


# Generated at 2022-06-14 16:35:06.281196
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    instance = ITVBTCCIE(ITVBTCCIE._downloader)
    instance.url = url
    instance._match_id(url)
    instance._real_extract(url)
    instance._real_initialize()


# Generated at 2022-06-14 16:35:09.488715
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Test if ITVBTCCIE is able to construct a regular expression that can
    # extract the wanted id from a url.
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    video_id = 'btcc-2018-all-the-action-from-brands-hatch'
    match = ITVBTCCIE._VALID_URL.match(url)
    assert match.group('id') == video_id

# Generated at 2022-06-14 16:35:10.553423
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    info_extractor = ITVBTCCIE()

# Generated at 2022-06-14 16:35:12.153936
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)

# Generated at 2022-06-14 16:35:15.472176
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE), 'The constructor returns a wrong instance of a derived class'

# Generated at 2022-06-14 16:35:26.981339
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info = ITVIE()._parse_json("""
        {
            "@context": "http://schema.org/",
            "@type": "TVEpisode",
            "name": "Episode 1",
            "description": "description text",
            "image": "https://www.image.com/image.jpg",
            "episodeNumber": 1,
            "partOfSeason": {
                "@type": "TVSeason",
                "name": "Series 1",
                "numberOfEpisodes": 10
            }
        }
    """)


# Generated at 2022-06-14 16:35:43.622446
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012', {}, ITVIE._GEO_COUNTRIES)

# Generated at 2022-06-14 16:35:47.095027
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:35:58.177751
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    btcc_ie_obj = ITVBTCCIE()
    assert btcc_ie_obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert btcc_ie_obj._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:36:01.320874
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = ITVIE()._VALID_URL
    mobj = re.match(ITVIE._VALID_URL, url)
    video_id = mobj.group('id')
    assert video_id

# Generated at 2022-06-14 16:36:05.269503
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    IT = ITVBTCCIE()
    assert IT.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'



# Generated at 2022-06-14 16:36:07.693905
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test = ITVIE()
    assert test._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:36:14.077155
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
	i = ITVBTCCIE("ITVBTCCIE", "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
	assert i.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:18.033931
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """ITVBTCCIE constructor can be used as a unit test to check if the
    ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE is still valid and does not contain typos.
    """
    ITVBTCCIE()

# Generated at 2022-06-14 16:36:19.753750
# Unit test for constructor of class ITVIE
def test_ITVIE():
    parser = ITVIE()
    assert parser is not None


# Generated at 2022-06-14 16:36:25.949887
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('ITVIE', [{'id': '2a4547a0012',
        'ext': 'mp4',
        'title': 'Liar - Series 2 - Episode 6',
        'description': 'md5:d0f91536569dec79ea184f0a44cca089',
        'series': 'Liar',
        'season_number': 2,
        'episode_number': 6,
    }])

# Generated at 2022-06-14 16:36:52.396093
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:36:55.976931
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = ITVBTCCIE._TEST['url']
    playlist_id = ITVBTCCIE._TEST['info_dict']['id']
    webpage = ITVBTCCIE._download_webpage(None, url)
    entries = ITVBTCCIE._real_extract(ITVBTCCIE(), url, webpage)
    assert entries['id'] == playlist_id


# Generated at 2022-06-14 16:37:01.095940
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # This is a real case which failed in test_py2.
    # unitest.main() did not report error, so I made this unit test.
    inst = ITVBTCCIE()
    inst.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    inst._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Old URL formats

# Generated at 2022-06-14 16:37:04.257610
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE(ITVBTCCIE.ie_key())
    ie.extract(url)


# Generated at 2022-06-14 16:37:15.600582
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = "https://www.itv.com/hub/liar/2a4547a0012"
    ins = ITVIE()
    res = ins.extract(url)
    # Check if the instance is valid
    assert hasattr(ins, '_match_id')
    assert hasattr(ins, '_real_extract')
    assert hasattr(ins, '_VALID_URL')
    assert hasattr(ins, 'BRIGHTCOVE_URL_TEMPLATE')
    assert hasattr(ins, '_download_webpage')
    assert hasattr(ins, '_search_regex')
    assert hasattr(ins, '_html_search_meta')
    assert hasattr(ins, '_json_ld')

# Generated at 2022-06-14 16:37:16.217756
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:37:17.166714
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    return ITVBTCCIE()

# Generated at 2022-06-14 16:37:24.386355
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
        assert ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch').url == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
        assert ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')._match_id == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:37:24.966188
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(None)

# Generated at 2022-06-14 16:37:28.260936
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE('http://www.itv.com/hub/liar/2a4547a0012')
    assert ie.params['data-video-playlist'] == 'https://mercury.itv.com/PlaylistService/Channels/ITV/Playlists/ITVODPages/2a4547a0012'

# Generated at 2022-06-14 16:38:27.251188
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    t = ITVBTCCIE()
    t._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:38:29.158805
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie.youtube_ie, BrightcoveNewIE)

# Generated at 2022-06-14 16:38:37.026560
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE_url = ITVIE._VALID_URL
    assert ITVIE_url != ''

    # Create an instance of ITVIE class
    obj_ITVIE = ITVIE('abc')
    assert obj_ITVIE._VALID_URL == ITVIE_url
    assert obj_ITVIE.url == ''

    obj_ITVIE = ITVIE('abc', url='https://www.itv.com/hub/liar/2a4547a0012')
    assert obj_ITVIE.url == 'https://www.itv.com/hub/liar/2a4547a0012'

    assert ITVIE._GEO_COUNTRIES == ['GB']

test_ITVIE()

# Generated at 2022-06-14 16:38:41.039876
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    btcc = ITVBTCCIE()
    assert btcc._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:38:44.146574
# Unit test for constructor of class ITVIE
def test_ITVIE():
    try:
        ITVIE()
    except:
        assert False, 'Constructor test for ITVIE failed!'


# Generated at 2022-06-14 16:38:53.704604
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._downloader is not None
    assert ie.suitable('http://www.itv.com/hub/liar/2a4547a0012')
    assert ie.suitable('https://www.itv.com/hub/through-the-keyhole/2a2271a0033')
    assert ie.suitable('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034')
    assert ie.suitable('https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024')


# Generated at 2022-06-14 16:38:56.402533
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    return ITVBTCCIE

# Generated at 2022-06-14 16:38:56.861954
# Unit test for constructor of class ITVIE
def test_ITVIE():
    unit = ITVIE()

# Generated at 2022-06-14 16:38:58.799030
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('http://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:39:00.466620
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_class = ITVIE("")
    assert test_class

# Generated at 2022-06-14 16:41:19.160675
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:41:20.587264
# Unit test for constructor of class ITVIE
def test_ITVIE():
    inst = ITVIE()
    assert inst is not None


# Generated at 2022-06-14 16:41:21.719999
# Unit test for constructor of class ITVIE
def test_ITVIE():
    y = ITVIE()
    assert y.GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:41:24.429292
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie._VALID_URL == ITVBTCCIE._VALID_URL
    assert ie.BRIGHTCOVE_URL_TEMPLATE == ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:41:34.764838
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from sys import version_info
    from .test_brightcove import TestBrightcoveNew
    from .test_brightcove_legacy import TestBrightcoveLegacy
    if version_info[:2] < (3, 4):
        return
    for test in TestBrightcoveNew().gen_tests():
        test['url'] = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
        yield test
    for test in TestBrightcoveLegacy().gen_tests():
        test['url'] = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
        yield test
    return ITVBTCCIE()

# Generated at 2022-06-14 16:41:37.279119
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    title = ITVBTCCIE()._og_search_title('<meta property="og:title" content="BTCC 2018: All the action from Brands Hatch"/>')
    assert title == 'BTCC 2018: All the action from Brands Hatch'

# Generated at 2022-06-14 16:41:41.713568
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert(ITVIE()._VALID_URL == ITVIE._VALID_URL)
    assert(ITVIE()._TESTS == ITVIE._TESTS)
    assert(ITVIE()._GEO_COUNTRIES == ITVIE._GEO_COUNTRIES)
    assert(ITVIE().BRIGHTCOVE_URL_TEMPLATE == ITVIE.BRIGHTCOVE_URL_TEMPLATE)

# Generated at 2022-06-14 16:41:44.820410
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from .generic_tests import check_generic_extractor_constructor
    return check_generic_extractor_constructor(ITVIE)

# Generated at 2022-06-14 16:41:49.956611
# Unit test for constructor of class ITVIE
def test_ITVIE():
    i = ITVIE()
    url = "http://www.itv.com/hub/liar/2a4547a0012"
    i = ITVIE()
    e = i._real_extract(url)
    assert e['title'] == 'Liar - Series 2 - Episode 6'

# Generated at 2022-06-14 16:41:57.535507
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvie = ITVIE()
    assert itvie._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert itvie._GEO_COUNTRIES == ['GB']
    assert itvie._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'