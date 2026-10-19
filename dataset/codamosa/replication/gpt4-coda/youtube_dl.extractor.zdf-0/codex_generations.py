

# Generated at 2024-03-18 09:32:34.956854
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:32:41.950752
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()


# Generated at 2024-03-18 09:32:46.446926
# Unit test for constructor of class ZDFIE
def test_ZDFIE():    # Test case for the constructor of ZDFIE
    def test_constructor(self):
        extractor = ZDFIE()
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertTrue(hasattr(extractor, '_TESTS'))
        self.assertIsInstance(extractor._TESTS, list)
        self.assertGreater(len(extractor._TESTS), 0)
        self.assertTrue(all(isinstance(test, dict) for test in extractor._TESTS))


# Generated at 2024-03-18 09:32:50.334042
# Unit test for constructor of class ZDFIE
def test_ZDFIE():    # Test case for the constructor of ZDFIE
    def test_constructor(self):
        extractor = ZDFIE()
        self.assertEqual(extractor._GEO_COUNTRIES, ['DE'])
        self.assertEqual(extractor._QUALITIES, ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'))
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertTrue(hasattr(extractor, '_TESTS'))


# Generated at 2024-03-18 09:32:52.210688
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:32:54.949694
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:32:59.359841
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    # Test instantiation and check class attributes
    extractor = ZDFBaseIE()
    assert extractor._GEO_COUNTRIES == ['DE']
    assert extractor._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert hasattr(extractor, '_call_api')
    assert hasattr(extractor, '_extract_subtitles')
    assert hasattr(extractor, '_extract_format')
    assert hasattr(extractor, '_extract_ptmd')
    assert hasattr(extractor, '_extract_player')


# Generated at 2024-03-18 09:33:04.440574
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()

# Generated at 2024-03-18 09:33:05.449718
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:33:09.219933
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()

# Generated at 2024-03-18 09:34:02.726194
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()

# Generated at 2024-03-18 09:34:08.225259
# Unit test for constructor of class ZDFIE
def test_ZDFIE():    # Test case for the constructor of ZDFIE
    def test_constructor(self):
        ie = ZDFIE()
        self.assertEqual(ie._VALID_URL, r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html')
        self.assertTrue(isinstance(ie._TESTS, list))
        self.assertTrue(all(isinstance(test, dict) for test in ie._TESTS))
        self.assertTrue(all('url' in test for test in ie._TESTS))


# Generated at 2024-03-18 09:34:09.124459
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:34:16.705099
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:34:18.419133
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:34:30.443250
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:34:39.065463
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:34:42.855201
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:34:48.664724
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()

# Generated at 2024-03-18 09:34:53.707430
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:36:32.311134
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:36:35.984323
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:36:44.300922
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:36:45.262159
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:36:48.470702
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:36:49.938005
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:36:56.851073
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:36:58.112027
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:37:04.089306
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    # Test instantiation and check class attributes
    extractor = ZDFBaseIE()
    assert extractor._GEO_COUNTRIES == ['DE']
    assert extractor._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

    # Test _call_api method with mock data
    mock_video_id = 'test_video'
    mock_url = 'http://example.com/api'
    mock_item = 'item'
    mock_api_token = 'test_token'
    mock_referrer = 'http://referrer.example.com'
    mock_response = {'key': 'value'}

    with mock.patch('ZDFBaseIE._download_json', return_value=mock_response) as mock_download_json:
        response = extractor._call_api(mock_url, mock_video_id, mock_item, mock_api_token, mock_referrer)

# Generated at 2024-03-18 09:37:05.336672
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:40:15.311007
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()

# Generated at 2024-03-18 09:40:21.522175
# Unit test for constructor of class ZDFIE
def test_ZDFIE():    # Test case for the constructor of ZDFIE
    def test_constructor(self):
        ie = ZDFIE()
        self.assertTrue(hasattr(ie, '_VALID_URL'))
        self.assertTrue(hasattr(ie, '_TESTS'))
        self.assertIsInstance(ie._TESTS, list)
        self.assertGreater(len(ie._TESTS), 0)
        self.assertTrue(all(isinstance(test, dict) for test in ie._TESTS))
        self.assertTrue(all('url' in test for test in ie._TESTS))


# Generated at 2024-03-18 09:40:25.460933
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()

# Generated at 2024-03-18 09:40:28.071823
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:40:35.856764
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:40:44.643180
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()


# Generated at 2024-03-18 09:40:48.787536
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():    ie = ZDFBaseIE()

# Generated at 2024-03-18 09:40:51.908722
# Unit test for constructor of class ZDFIE

# Generated at 2024-03-18 09:40:55.000651
# Unit test for constructor of class ZDFChannelIE

# Generated at 2024-03-18 09:41:27.672146
# Unit test for constructor of class ZDFIE
def test_ZDFIE():    # Test case for the constructor of ZDFIE
    def test_constructor(self):
        extractor = ZDFIE()
        self.assertEqual(extractor._GEO_COUNTRIES, ['DE'])
        self.assertEqual(extractor._QUALITIES, ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'))
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertTrue(hasattr(extractor, '_TESTS'))
