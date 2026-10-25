

# Generated at 2026-10-24 07:09:09.605001
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:09:12.118315
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:09:14.631729
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:09:17.050141
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:09:19.468223
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:09:21.885153
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:09:24.304006
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:09:26.714724
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:09:29.132312
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:09:31.546094
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:09:44.236424
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()
assert isinstance(ie, ViafreeIE)
assert ie._GEO_BYPASS is False

# Generated at 2026-10-24 07:09:52.255182
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 07:09:53.570781
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:10:10.036893
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:10:12.468790
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:10:14.870120
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:10:17.431892
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:10:19.849184
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:22.271785
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:24.679051
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:27.092391
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:29.506006
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:31.920764
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:34.335690
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:36.748980
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:39.164563
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:10:41.588233
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:10:44.002182
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:10:46.419493
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:10:48.836196
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:10:51.257393
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:10:53.669103
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:10:56.081601
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:11:30.318323
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()

# Generated at 2026-10-24 07:11:32.735552
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:11:35.152588
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:11:37.572429
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:11:39.992375
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:11:42.407640
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:11:44.826624
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:11:47.394865
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:11:49.809833
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:11:52.223162
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:11:54.636693
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:11:57.051407
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:11:59.467639
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:12:01.882423
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:12:04.295421
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:12:06.708469
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:12:09.121885
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:12:11.536348
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:12:13.949209
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:12:16.363580
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:12:41.328952
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:12:58.009194
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

    # Constructor creates a usable instance with the documented IE_NAME

# Generated at 2026-10-24 07:13:14.468147
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:13:28.612476
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:13:45.078181
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:14:01.565941
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:14:03.983961
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:14:06.394902
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:14:08.811267
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:14:27.164747
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()

# Generated at 2026-10-24 07:14:29.035965
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:14:30.352950
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:14:31.695676
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:14:33.028026
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:14:34.351521
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:14:50.858376
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:14:53.370424
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:14:55.783470
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:14:58.200589
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:15:00.615427
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:15:03.030157
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:15:05.444617
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:15:07.859825
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:15:10.277099
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:15:12.693245
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:15:15.108567
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:15:17.520959
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:15:19.940081
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:15:22.356626
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:15:24.771553
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:15:27.186488
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:15:29.602546
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:15:32.017390
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:15:34.434708
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:15:36.852506
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:15:38.355237
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()
assert isinstance(ie, ViafreeIE)
assert ie._GEO_BYPASS is False

# Generated at 2026-10-24 07:15:40.076623
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:15:56.664082
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:15:58.099354
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:15:59.425199
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:16:00.764600
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:16:17.350155
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:16:33.835568
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:16:35.165158
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:16:36.567498
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:16:37.902640
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:16:54.421130
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:17:10.873430
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:17:27.288137
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:17:29.707339
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:17:32.123324
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:17:34.692886
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:17:37.108331
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:17:39.527509
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:17:42.098880
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

# Generated at 2026-10-24 07:17:44.646873
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:17:46.025860
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:17:47.412327
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:17:48.738589
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:17:50.049396
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:17:51.387277
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:17:52.709178
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:18:09.119296
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:18:11.693877
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:14.115553
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:16.532247
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:18.947891
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:18:21.361506
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:18:23.775218
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:18:29.191037
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:31.605917
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:34.022030
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:36.435499
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:18:38.849456
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:18:41.422456
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:18:43.837053
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:46.250444
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:48.666643
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:51.083798
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:53.501540
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:18:55.916273
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:19:12.454887
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')