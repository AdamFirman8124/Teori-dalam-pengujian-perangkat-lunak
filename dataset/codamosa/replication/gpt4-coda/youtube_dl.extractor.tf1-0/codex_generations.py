

# Generated at 2024-03-18 09:22:22.442996
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:22:26.501132
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:22:30.075172
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:22:35.699417
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:22:43.724904
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

    # Test _VALID_URL pattern

# Generated at 2024-03-18 09:22:46.353965
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:22:51.029943
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:22:55.949707
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:23:03.074072
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for a URL that only matches the pattern
    ie = TF1IE()

# Generated at 2024-03-18 09:23:13.058237
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert info_dict.get('title') is not None
    assert info_dict.get('description') is not None
    assert info_dict.get('upload_date') == '20190611'
    assert info_dict.get('timestamp') == 1560273989
    assert info_dict.get('duration') == 1738
    assert info_dict.get('series') == 'Quotidien avec Yann Barthès'

# Generated at 2024-03-18 09:23:31.628292
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:23:36.029720
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:23:40.541376
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:23:43.822461
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:23:46.758851
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:23:50.943145
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:23:53.605891
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:24:00.220680
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical TF1 video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738
    assert info_dict.get('timestamp') == 1560273989
    assert info_dict.get('upload_date') == '20190611'

    # Test case for matching URLs

# Generated at 2024-03-18 09:24:06.606191
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for a URL that only matches the pattern
    ie = TF1IE()

# Generated at 2024-03-18 09:24:11.122631
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:24:53.053625
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Create an instance of the TF1IE class
    tf1ie = TF1IE()

    # Check if the instance is created and is an instance of InfoExtractor
    assert isinstance(tf1ie, InfoExtractor), "TF1IE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URLs
    assert re.match(tf1ie._VALID_URL, 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'), "The URL should match the _VALID_URL pattern"
    assert re.match(tf1ie._VALID_URL, 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'), "The URL should match the _VALID_URL pattern"

# Generated at 2024-03-18 09:25:04.648802
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for 'only_matching' scenario
    only_matching_test_url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2024-03-18 09:25:08.966966
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:25:12.785686
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:25:20.029696
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for 'only_matching' scenario
    only_matching_ie = TF1IE()

# Generated at 2024-03-18 09:25:29.167873
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for 'only_matching' scenario
    only_matching_test_url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2024-03-18 09:25:35.681255
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

    # Check if the _VALID_URL pattern matches the expected URLs

# Generated at 2024-03-18 09:25:41.757722
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:25:45.006931
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:25:51.094868
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:26:50.674132
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:26:53.426820
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:27:00.210472
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

    # Test _VALID_URL pattern

# Generated at 2024-03-18 09:27:03.147912
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:27:07.721581
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:27:11.020624
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:27:21.099419
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for 'only_matching' scenario
    only_matching_ie = TF1IE()

# Generated at 2024-03-18 09:27:30.066324
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for 'only_matching' scenario
    only_matching_test_url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2024-03-18 09:27:40.860039
# Unit test for constructor of class TF1IE
def test_TF1IE():    # Test case for a typical video extraction
    ie = TF1IE()
    test_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '13641379'
    assert info_dict.get('ext') == 'mp4'
    assert 'Quotidien avec Yann Barthès' in info_dict.get('series')
    assert 'intégrale' in info_dict.get('tags')
    assert info_dict.get('duration') == 1738

    # Test case for 'only_matching' scenario
    only_matching_ie = TF1IE()

# Generated at 2024-03-18 09:27:44.244717
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:29:43.325792
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:29:45.949361
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:29:50.935042
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:29:56.130325
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:29:59.030965
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:30:03.276415
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:30:06.732285
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:30:09.374883
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:30:12.203580
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()

# Generated at 2024-03-18 09:30:16.728976
# Unit test for constructor of class TF1IE
def test_TF1IE():    ie = TF1IE()