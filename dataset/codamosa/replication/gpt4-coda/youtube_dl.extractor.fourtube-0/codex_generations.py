

# Generated at 2024-03-18 09:09:43.097864
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():    # Test case for the constructor of FourTubeIE
    def test_constructor(self):
        ie = FourTubeIE()
        self.assertEqual(ie.IE_NAME, '4tube')
        self.assertIsNotNone(ie._VALID_URL)
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')
        self.assertEqual(ie._TKN_HOST, 'token.4tube.com')


# Generated at 2024-03-18 09:09:49.309604
# Unit test for constructor of class FuxIE

# Generated at 2024-03-18 09:09:55.648918
# Unit test for constructor of class PornTubeIE

# Generated at 2024-03-18 09:10:00.615765
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    # Test case for the constructor of PornerBrosIE
    def test_constructor(self):
        ie = PornerBrosIE()
        self.assertEqual(ie.IE_NAME, 'pornerbros')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.pornerbros.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'token.pornerbros.com')


# Generated at 2024-03-18 09:10:07.582324
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the object has the attribute _VALID_URL
        self.assertTrue(hasattr(extractor, '_VALID_URL'))

        # Assert that the object has the attribute _URL_TEMPLATE
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))

        # Assert that the object has the attribute _TKN_HOST
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))

        # Assert that the object has the attribute _TESTS
        self.assertTrue(hasattr(extractor, '_TESTS'))


# Generated at 2024-03-18 09:10:14.866602
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the _TKN_HOST attribute is set correctly
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))
        self.assertIsNone(extractor._TKN_HOST)

        # Assert that the _URL_TEMPLATE attribute is set correctly
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))
        self.assertIsNone(extractor._URL_TEMPLATE)

        # Assert that the _VALID_URL attribute is set correctly
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertIsNone(extractor._VALID_URL)

        # Assert that the IE_NAME attribute is set correctly

# Generated at 2024-03-18 09:10:22.802260
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():    # Test case for the constructor of PornTubeIE
    def test_constructor(self):
        ie = PornTubeIE()
        self.assertEqual(ie.IE_NAME, 'porntube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.porntube.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'tkn.porntube.com')


# Generated at 2024-03-18 09:10:29.547183
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():    # Test case for the constructor of FourTubeIE
    def test_constructor(self):
        ie = FourTubeIE()
        self.assertEqual(ie.IE_NAME, '4tube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')
        self.assertEqual(ie._TKN_HOST, 'token.4tube.com')


# Generated at 2024-03-18 09:10:34.395947
# Unit test for constructor of class FuxIE

# Generated at 2024-03-18 09:10:42.615374
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the _TKN_HOST attribute is set correctly
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))
        self.assertEqual(extractor._TKN_HOST, 'token.4tube.com')

        # Assert that the _URL_TEMPLATE attribute is set correctly
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))
        self.assertEqual(extractor._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')

        # Assert that the _VALID_URL attribute is set correctly
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertIsNotNone(extractor._VALID_URL)


# Generated at 2024-03-18 09:11:18.776109
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    ie = PornerBrosIE()

# Generated at 2024-03-18 09:11:23.118911
# Unit test for constructor of class FourTubeIE

# Generated at 2024-03-18 09:11:28.853316
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the _TKN_HOST attribute is set correctly
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))
        self.assertIsNone(extractor._TKN_HOST)  # Assuming _TKN_HOST should be None by default

        # Assert that the _URL_TEMPLATE attribute is set correctly
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))
        self.assertIsNone(extractor._URL_TEMPLATE)  # Assuming _URL_TEMPLATE should be None by default


# Generated at 2024-03-18 09:11:34.893296
# Unit test for constructor of class FuxIE

# Generated at 2024-03-18 09:11:41.125454
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the _TKN_HOST attribute is set correctly
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))
        self.assertIsNone(extractor._TKN_HOST)

        # Assert that the _URL_TEMPLATE attribute is set correctly
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))
        self.assertIsNone(extractor._URL_TEMPLATE)

        # Assert that the _VALID_URL attribute is set correctly
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertIsNone(extractor._VALID_URL)


# Generated at 2024-03-18 09:11:48.176877
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    # Test case for the constructor of PornerBrosIE
    def test_constructor(self):
        ie = PornerBrosIE()
        self.assertEqual(ie.IE_NAME, 'pornerbros')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.pornerbros.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'token.pornerbros.com')


# Generated at 2024-03-18 09:11:54.937956
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():    # Test case for the constructor of PornTubeIE
    def test_constructor(self):
        ie = PornTubeIE()
        self.assertEqual(ie.IE_NAME, 'porntube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.porntube.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'tkn.porntube.com')


# Generated at 2024-03-18 09:12:01.636143
# Unit test for constructor of class FuxIE

# Generated at 2024-03-18 09:12:07.387134
# Unit test for constructor of class FuxIE

# Generated at 2024-03-18 09:12:12.154027
# Unit test for constructor of class PornTubeIE

# Generated at 2024-03-18 09:13:14.917657
# Unit test for constructor of class FourTubeIE

# Generated at 2024-03-18 09:13:24.069679
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    ie = PornerBrosIE()

# Generated at 2024-03-18 09:13:28.221245
# Unit test for constructor of class FuxIE

# Generated at 2024-03-18 09:13:33.721871
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():    # Test case for the constructor of PornTubeIE
    def test_constructor(self):
        ie = PornTubeIE()
        self.assertEqual(ie.IE_NAME, 'porntube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.porntube.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'tkn.porntube.com')


# Generated at 2024-03-18 09:13:38.098394
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the object has the attribute _TKN_HOST
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))

        # Assert that the _TKN_HOST attribute is not empty
        self.assertTrue(getattr(extractor, '_TKN_HOST'))


# Generated at 2024-03-18 09:13:42.176100
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():    # Test case for the constructor of FourTubeIE
    def test_constructor(self):
        ie = FourTubeIE()
        self.assertEqual(ie.IE_NAME, '4tube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')
        self.assertEqual(ie._TKN_HOST, 'token.4tube.com')


# Generated at 2024-03-18 09:13:46.544985
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    # Test case for the constructor of PornerBrosIE
    def test_constructor(self):
        ie = PornerBrosIE()
        self.assertEqual(ie.IE_NAME, 'pornerbros')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.pornerbros.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'token.pornerbros.com')


# Generated at 2024-03-18 09:13:57.442892
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    # Unit test for constructor of class PornerBrosIE
    def test_PornerBrosIE_constructor():
        ie = PornerBrosIE()
        assert ie.IE_NAME == 'pornerbros'
        assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
        assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
        assert ie._TKN_HOST == 'token.pornerbros.com'
        assert 'url' in ie._TESTS[0]
        assert 'md5' in ie._TESTS[0]
        assert 'info_dict' in ie._TESTS[0]
        assert 'params' in ie._TESTS[0]
        assert ie

# Generated at 2024-03-18 09:14:02.796096
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():    # Test case for the constructor of FourTubeIE
    def test_constructor(self):
        ie = FourTubeIE()
        self.assertEqual(ie.IE_NAME, '4tube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')
        self.assertEqual(ie._TKN_HOST, 'token.4tube.com')


# Generated at 2024-03-18 09:14:09.110896
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():    # Test case for the constructor of FourTubeIE
    def test_constructor(self):
        ie = FourTubeIE()
        self.assertEqual(ie.IE_NAME, '4tube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')
        self.assertEqual(ie._TKN_HOST, 'token.4tube.com')


# Generated at 2024-03-18 09:16:12.768862
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():    # Test case for the constructor of FourTubeIE
    def test_constructor(self):
        ie = FourTubeIE()
        self.assertEqual(ie.IE_NAME, '4tube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')
        self.assertEqual(ie._TKN_HOST, 'token.4tube.com')


# Generated at 2024-03-18 09:16:20.820453
# Unit test for constructor of class FuxIE

# Generated at 2024-03-18 09:16:27.338482
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():    ie = PornTubeIE()


# Generated at 2024-03-18 09:16:33.614793
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():    # Test case for the constructor of FourTubeIE
    def test_constructor(self):
        ie = FourTubeIE()
        self.assertEqual(ie.IE_NAME, '4tube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.4tube.com/videos/%s/video')
        self.assertEqual(ie._TKN_HOST, 'token.4tube.com')


# Generated at 2024-03-18 09:16:40.824905
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the required attributes are present
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))


# Generated at 2024-03-18 09:16:47.193998
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():    # Test case for the constructor of PornTubeIE
    def test_constructor(self):
        ie = PornTubeIE()
        self.assertEqual(ie.IE_NAME, 'porntube')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.porntube.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'tkn.porntube.com')


# Generated at 2024-03-18 09:16:55.744602
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    # Test case for the constructor of PornerBrosIE
    def test_constructor(self):
        ie = PornerBrosIE()
        self.assertEqual(ie.IE_NAME, 'pornerbros')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.pornerbros.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'token.pornerbros.com')


# Generated at 2024-03-18 09:17:02.282029
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the _TKN_HOST attribute is set correctly
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))
        self.assertIsNone(extractor._TKN_HOST)

        # Assert that the _URL_TEMPLATE attribute is set correctly
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))
        self.assertIsNone(extractor._URL_TEMPLATE)

        # Assert that the _VALID_URL attribute is set correctly
        self.assertTrue(hasattr(extractor, '_VALID_URL'))
        self.assertIsNone(extractor._VALID_URL)


# Generated at 2024-03-18 09:17:08.466142
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():    # Test case for PornerBrosIE constructor
    def test_constructor(self):
        ie = PornerBrosIE()
        self.assertEqual(ie.IE_NAME, 'pornerbros')
        self.assertEqual(ie._VALID_URL, r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
        self.assertEqual(ie._URL_TEMPLATE, 'https://www.pornerbros.com/videos/video_%s')
        self.assertEqual(ie._TKN_HOST, 'token.pornerbros.com')


# Generated at 2024-03-18 09:17:13.866680
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():    # Test case for the constructor of FourTubeBaseIE
    def test_constructor(self):
        # Create an instance of the FourTubeBaseIE class
        extractor = FourTubeBaseIE()

        # Assert that the object is an instance of FourTubeBaseIE
        self.assertIsInstance(extractor, FourTubeBaseIE)

        # Assert that the object has the attribute _VALID_URL
        self.assertTrue(hasattr(extractor, '_VALID_URL'))

        # Assert that the object has the attribute _URL_TEMPLATE
        self.assertTrue(hasattr(extractor, '_URL_TEMPLATE'))

        # Assert that the object has the attribute _TKN_HOST
        self.assertTrue(hasattr(extractor, '_TKN_HOST'))

        # Assert that the object has the attribute _TESTS
        self.assertTrue(hasattr(extractor, '_TESTS'))
