

# Generated at 2022-06-14 17:06:04.614684
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE({'wv_info': {'video_id': '0'}})
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:06.231511
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Unit test for constructor of class TF1IE
    test_TF1IE_object = TF1IE()
    # Assertion
    assert test_TF1IE_object


# Generated at 2022-06-14 17:06:10.342513
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(TF1IE(), "http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")

# Generated at 2022-06-14 17:06:15.018088
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test class TF1IE

    Test data od entity class TF1IE
    """
    TF1IE().extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:06:16.011120
# Unit test for constructor of class TF1IE
def test_TF1IE():
    objTF1IE = TF1IE()

# Generated at 2022-06-14 17:06:27.356866
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:06:28.597707
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:33.648809
# Unit test for constructor of class TF1IE
def test_TF1IE():
	# Test with a sample URL from the unit test
	TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")

# Test for method _real_extract of class TF1IE

# Generated at 2022-06-14 17:06:34.272908
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:06:39.326853
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # function is not available in python3
    with open('tf1/test.html', 'r') as f:
        print(f.read())
        f.seek(0)
        print(TF1IE.suitable(f.read()))

# Generated at 2022-06-14 17:06:46.598081
# Unit test for constructor of class TF1IE
def test_TF1IE():
    global TF1IE
    # Check if the class was initialized correctly
    if TF1IE == None:
        raise Exception("Class TF1IE not initialized correctly!")
    else:
        return True

# Generated at 2022-06-14 17:06:54.371045
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test for the wat protocole
    TF1IETest = TF1IE('TF1IE', url='https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert TF1IETest._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:04.498975
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Needs to use the constructor to skip download
    """
    tf1 = TF1IE(None)
    result = tf1.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert result
    result = tf1.suitable('http://www.wat.tv/video/koh-lanta-du-22-mai-2015-1szdp.html')
    assert not result
    result = tf1.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert result

# Generated at 2022-06-14 17:07:16.401692
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert TF1IE._TESTS[0]['url'] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert TF1IE._TESTS[1]['url'] == 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2022-06-14 17:07:17.906266
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert isinstance(instance, TF1IE)

# Generated at 2022-06-14 17:07:24.252311
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    ie = TF1IE()
    ie.extract('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:07:25.118376
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()

# Generated at 2022-06-14 17:07:34.738753
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.__name__ == 'TF1IE'
    assert TF1IE.__doc__ == None
    t = TF1IE(None)
    assert t.suitable == False
    assert t.IE_NAME == 'tf1'
    assert t.ie_key() == 'TF1'
    assert t.extract_urls == ['^https?://(?:www\\.)?tf1\\.fr/.+\\.html$']
    assert t.valid_url('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html') == True
    assert t.valid_url('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html', False) == False
    assert t.valid

# Generated at 2022-06-14 17:07:35.349632
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:37.143185
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE()
    except TypeError as e:
        print(e)
        raise AssertionError

# Generated at 2022-06-14 17:07:53.670010
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html", {})
    TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html", {})
    print("yay")

if __name__ == "__main__": test_TF1IE()

# Generated at 2022-06-14 17:07:54.892440
# Unit test for constructor of class TF1IE
def test_TF1IE():
    return TF1IE()

# Generated at 2022-06-14 17:07:56.771149
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)

# Generated at 2022-06-14 17:08:04.071391
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # https://www.youtube.com/watch?v=pfW8zGV_w0M
    url1 = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-10-juin-2020.html"
    ex = TF1IE()
    assert ex.suitable(url1)
    assert re.match(TF1IE._VALID_URL, url1)



# Generated at 2022-06-14 17:08:05.421060
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    tf1ie.constructor_test()

# Generated at 2022-06-14 17:08:10.111014
# Unit test for constructor of class TF1IE
def test_TF1IE():
    yt_id = 'f392bc52245dc5ad43771650c96fb620' # md5 hash for the video
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'

    test_url = TF1IE(url)
    assert test_url.url == url
    assert test_url.id == yt_id

# Generated at 2022-06-14 17:08:12.765615
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()
    assert tf1IE is not None
    assert tf1IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:15.498443
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:16.898391
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('5676').url == '5676'

# Generated at 2022-06-14 17:08:21.378016
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE._VALID_URL is not None
    assert IE._TESTS is not None
    assert IE._login_form is not None
    assert IE._token_url is not None
    assert IE._token is not None
    assert IE._downloader is not None

# Generated at 2022-06-14 17:08:48.196692
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Constructor test.
    """
    url = "https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    TF1IE(url)

# Generated at 2022-06-14 17:08:51.319225
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    tf1ie_expected_output = '<TF1IE>'
    assert (str(tf1ie) == tf1ie_expected_output)


# Generated at 2022-06-14 17:08:54.873838
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test class constructor"""
    inst = TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    print(inst)

# Generated at 2022-06-14 17:08:58.110651
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert isinstance(TF1IE(None), TF1IE)

# Generated at 2022-06-14 17:08:59.307967
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()

# Generated at 2022-06-14 17:08:59.966664
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:09:02.821173
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:09:11.464235
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()
    assert tf1_ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:09:15.879948
# Unit test for constructor of class TF1IE
def test_TF1IE():
    return TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:09:17.115923
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tester = TF1IE()

# Generated at 2022-06-14 17:10:05.310369
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE("", "")
    assert tf1IE.SUFFIX == '&platform=android-phone&autostart=1'

# Generated at 2022-06-14 17:10:06.937700
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(tf1.py).extract_video_info(url)

# Generated at 2022-06-14 17:10:09.905664
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test the constructor of the class TF1IE
    """
    # Define some global variables
    tf1i = TF1IE(None)
    assert tf1i is not None


# Generated at 2022-06-14 17:10:10.692588
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE


# Generated at 2022-06-14 17:10:11.203423
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()

# Generated at 2022-06-14 17:10:16.140645
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Unit test for TF1IE class constructor
    Args:
        url: url string

    Returns:
        Nothing.
    """
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    test_TF1IE = TF1IE(url)
    assert test_TF1IE._VALID_URL == TF1IE._VALID_URL



# Generated at 2022-06-14 17:10:19.194620
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_object = {}
    assert TF1IE(test_object).suitable(test_object)

# Unit tests for results of method _real_extract

# Generated at 2022-06-14 17:10:23.409643
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE('tf1', 'abc')
    assert tf1IE is not None

if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:10:25.205059
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE().IE_DESC == 'TF1'       # calls constructor of TF1IE class

# Generated at 2022-06-14 17:10:30.936618
# Unit test for constructor of class TF1IE
def test_TF1IE():
    video = TF1IE()
    video.video_id = "123456"
    video.url = "http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    test_tuple = (TF1IE.__module__, TF1IE.IE_NAME, video.video_id, video.url)
    assert isinstance(video, InfoExtractor)


# Generated at 2022-06-14 17:12:33.976328
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:12:42.357973
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")
    TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")

# Generated at 2022-06-14 17:12:42.881598
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:12:45.048171
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE()
    except Exception as e:
        print("Error: Creating instance of TF1IE failed:", e)

# Generated at 2022-06-14 17:12:48.178223
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    return


# Generated at 2022-06-14 17:12:49.386803
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:12:54.007573
# Unit test for constructor of class TF1IE
def test_TF1IE():
    i = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert i.name == 'TF1IE'

# Generated at 2022-06-14 17:12:54.981230
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None, None)

# Generated at 2022-06-14 17:13:00.816018
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert TF1IE()._TESTS[0]['url'] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'


# Generated at 2022-06-14 17:13:02.486246
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('tf1', 'tf1')