

# Generated at 2026-10-24 21:50:14.271011
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:50:15.594449
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 21:50:21.983641
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-24 21:50:23.420699
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 21:50:33.349983
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

    downloader = object()
    extractor_with_downloader = TVPlayHomeIE(downloader)

    assert extractor_with_downloader._downloader is downloader

# Generated at 2026-10-24 21:50:35.771279
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:50:38.187785
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:50:40.605024
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:50:43.024434
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:50:45.445882
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:50:47.861842
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:50:50.279371
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:50:52.695961
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:50:55.115522
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:50:57.672866
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:00.092324
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:05.299963
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:51:11.340197
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:51:17.382931
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:51:25.790308
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    assert isinstance(ie, TVPlayHomeIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.suitable(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')

# Generated at 2026-10-24 21:51:33.562739
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-24 21:51:36.095873
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:38.630803
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:41.049053
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:43.466273
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:45.883289
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:48.299772
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:50.717225
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:53.134791
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:55.696019
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:51:58.114013
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:52:00.535647
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:52:07.047409
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:52:15.185938
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 21:52:23.123816
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:52:34.367880
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:52:36.790926
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:52:39.445862
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:52:41.890259
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:52:44.306387
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:52:46.725344
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:52:49.331935
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:52:51.753941
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:52:54.169633
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:52:56.585556
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:52:59.004876
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:01.419815
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:03.838262
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:06.257273
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:53:08.671584
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:53:11.088985
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:53:13.505439
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:15.921676
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:18.333076
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:20.752134
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:53:23.168273
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:53:25.588821
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:53:28.006809
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:30.423886
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:32.840762
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:35.297840
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:53:37.713821
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:53:40.130230
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:53:42.546364
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:44.960632
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:47.375909
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:49.790730
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:52.205285
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:54.622988
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:53:57.037751
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:53:59.456317
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:54:01.874621
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:54:04.292397
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:54:06.707483
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:54:09.123813
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:54:11.540587
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:54:13.962415
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:54:16.379185
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:54:18.794591
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:21.217205
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:23.635613
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:26.047763
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:28.470126
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:30.885334
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:33.305019
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:54:35.723174
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:54:38.141819
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:54:40.558593
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:42.974928
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:45.392381
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:47.807359
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:50.226231
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:52.652999
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:54:55.063125
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:55:01.703252
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()

# Generated at 2026-10-24 21:55:09.595989
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    downloader = object()
    extractor = TVPlayHomeIE(downloader)

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'TVPlayHome'

# Generated at 2026-10-24 21:55:10.994643
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 21:55:20.643751
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:55:21.992008
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 21:55:31.541395
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()


# Generated at 2026-10-24 21:55:35.529824
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:37.951692
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:40.372919
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:42.791203
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:45.207309
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:47.622522
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:50.038981
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:52.458625
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:54.876783
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:55:57.296529
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:55:59.715470
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:56:02.132306
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:56:09.053351
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():extractor = ViafreeIE()

# Generated at 2026-10-24 21:56:19.362292
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    downloader = object()
    extractor = TVPlayHomeIE(downloader)

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

# Generated at 2026-10-24 21:56:20.694524
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 21:56:27.977981
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:56:37.058741
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()


# Generated at 2026-10-24 21:56:39.613872
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:56:42.030752
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:56:44.450108
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 21:56:50.176718
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:56:52.593417
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:56:55.156982
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:56:57.575131
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:56:59.996131
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:57:02.412121
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:57:04.829506
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:57:07.248470
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:57:09.668839
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:57:16.953058
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:57:26.351213
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert extractor is not None
    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)

# Generated at 2026-10-24 21:57:33.807222
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 21:57:43.534527
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()


# Generated at 2026-10-24 21:57:51.931548
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:57:54.571364
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:57:56.989952
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:57:59.407454
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:58:01.979275
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:58:04.396317
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:58:06.814193
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:58:16.868440
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:58:19.285179
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:58:21.702934
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:58:24.121345
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:58:29.165929
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:58:36.785127
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-24 21:58:45.177547
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:58:55.545022
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    downloader = object()
    extractor = TVPlayHomeIE(downloader)

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 21:59:05.106115
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 21:59:07.631754
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:59:10.155378
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:59:12.572652
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:59:15.089137
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:59:17.504517
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:59:19.921450
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:59:22.340498
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:59:24.756345
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:59:27.175732
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 21:59:29.596424
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 21:59:38.028126
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():extractor = TVPlayHomeIE()

# Generated at 2026-10-24 22:00:03.517142
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 22:00:04.883710
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 22:00:06.256267
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')