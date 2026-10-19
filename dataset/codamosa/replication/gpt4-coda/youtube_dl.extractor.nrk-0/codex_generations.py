

# Generated at 2024-03-18 09:20:24.665419
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():    # Instantiate an object using the NRKTVDirekteIE class
    nrk_tv_direkte_ie = NRKTVDirekteIE()

    # Test the object's attributes to ensure it was constructed correctly
    assert nrk_tv_direkte_ie.IE_DESC == 'NRK TV Direkte and NRK Radio Direkte'
    assert nrk_tv_direkte_ie._VALID_URL == r'https?://(?:tv|radio)\.nrk\.no/direkte/(?P<id>[^/?#&]+)'
    assert nrk_tv_direkte_ie._TESTS == [{
        'url': 'https://tv.nrk.no/direkte/nrk1',
        'only_matching': True,
    }, {
        'url': 'https://radio.nrk.no/direkte/p1_oslo_akershus',
        'only_matching': True,
    }]

    # Print success message if all assertions pass

# Generated at 2024-03-18 09:20:25.698510
# Unit test for constructor of class NRKRadioPodkastIE

# Generated at 2024-03-18 09:20:30.030727
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():import unittest
from your_module import NRKTVIE  # Replace with the actual import for the NRKTVIE class


# Generated at 2024-03-18 09:20:31.839483
# Unit test for constructor of class NRKTVEpisodeIE

# Generated at 2024-03-18 09:20:33.663879
# Unit test for constructor of class NRKPlaylistIE

# Generated at 2024-03-18 09:20:35.063557
# Unit test for constructor of class NRKTVSerieBaseIE

# Generated at 2024-03-18 09:20:39.774088
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():import unittest
from your_module import NRKTVIE  # Replace with the actual import for your NRKTVIE class


# Generated at 2024-03-18 09:20:41.012641
# Unit test for constructor of class NRKTVEpisodesIE

# Generated at 2024-03-18 09:20:49.460576
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():    ie = NRKBaseIE()

# Generated at 2024-03-18 09:20:50.400760
# Unit test for constructor of class NRKTVSeasonIE

# Generated at 2024-03-18 09:21:39.885006
# Unit test for constructor of class NRKPlaylistIE

# Generated at 2024-03-18 09:21:41.046469
# Unit test for constructor of class NRKTVEpisodesIE

# Generated at 2024-03-18 09:21:42.902404
# Unit test for constructor of class NRKTVSeasonIE

# Generated at 2024-03-18 09:21:44.304730
# Unit test for constructor of class NRKPlaylistBaseIE

# Generated at 2024-03-18 09:21:45.790356
# Unit test for constructor of class NRKPlaylistIE

# Generated at 2024-03-18 09:21:52.628010
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():    ie = NRKBaseIE()

# Generated at 2024-03-18 09:21:56.145185
# Unit test for constructor of class NRKTVSeriesIE

# Generated at 2024-03-18 09:21:57.900565
# Unit test for constructor of class NRKSkoleIE

# Generated at 2024-03-18 09:21:59.165361
# Unit test for constructor of class NRKSkoleIE

# Generated at 2024-03-18 09:22:00.729195
# Unit test for constructor of class NRKRadioPodkastIE

# Generated at 2024-03-18 09:23:44.621536
# Unit test for constructor of class NRKIE
def test_NRKIE():    # Instantiate an object of NRKIE
    ie = NRKIE()

    # Assert _VALID_URL pattern matches expected URLs
    assert re.match(ie._VALID_URL, 'http://www.nrk.no/video/PS*150533')
    assert re.match(ie._VALID_URL, 'nrk:ecc1b952-96dc-4a98-81b9-5296dc7a98d9')
    assert re.match(ie._VALID_URL, 'https://v8-psapi.nrk.no/mediaelement/ecc1b952-96dc-4a98-81b9-5296dc7a98d9')
    assert re.match(ie._VALID_URL, 'nrk:150533')
    assert re.match(ie._VALID_URL, 'nrk:program/ENRK10100318')
    assert re.match(ie._VALID_URL, 'nrk:nrk1')

    #

# Generated at 2024-03-18 09:23:45.846784
# Unit test for constructor of class NRKTVSerieBaseIE

# Generated at 2024-03-18 09:23:47.294282
# Unit test for constructor of class NRKPlaylistIE

# Generated at 2024-03-18 09:23:48.792517
# Unit test for constructor of class NRKTVSerieBaseIE

# Generated at 2024-03-18 09:23:50.305242
# Unit test for constructor of class NRKTVSeriesIE

# Generated at 2024-03-18 09:23:51.898706
# Unit test for constructor of class NRKPlaylistIE

# Generated at 2024-03-18 09:23:53.344723
# Unit test for constructor of class NRKRadioPodkastIE

# Generated at 2024-03-18 09:23:54.953589
# Unit test for constructor of class NRKTVSerieBaseIE

# Generated at 2024-03-18 09:23:56.846993
# Unit test for constructor of class NRKTVSeasonIE

# Generated at 2024-03-18 09:23:58.176259
# Unit test for constructor of class NRKTVEpisodeIE

# Generated at 2024-03-18 09:27:00.159360
# Unit test for constructor of class NRKSkoleIE

# Generated at 2024-03-18 09:27:01.736414
# Unit test for constructor of class NRKRadioPodkastIE

# Generated at 2024-03-18 09:27:02.698055
# Unit test for constructor of class NRKTVEpisodeIE

# Generated at 2024-03-18 09:27:03.797647
# Unit test for constructor of class NRKPlaylistIE

# Generated at 2024-03-18 09:27:05.560405
# Unit test for constructor of class NRKTVSerieBaseIE

# Generated at 2024-03-18 09:27:06.892041
# Unit test for constructor of class NRKPlaylistBaseIE

# Generated at 2024-03-18 09:27:08.392353
# Unit test for constructor of class NRKTVSerieBaseIE

# Generated at 2024-03-18 09:27:09.441162
# Unit test for constructor of class NRKPlaylistBaseIE

# Generated at 2024-03-18 09:27:10.374071
# Unit test for constructor of class NRKPlaylistBaseIE

# Generated at 2024-03-18 09:27:12.652479
# Unit test for constructor of class NRKTVSeriesIE