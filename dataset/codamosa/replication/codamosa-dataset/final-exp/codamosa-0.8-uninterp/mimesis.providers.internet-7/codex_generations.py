

# Generated at 2022-06-14 00:21:06.961584
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    """Testing Internet.hashtags()"""
    internet = Internet("en")
    test1 = internet.hashtags(quantity=1)
    test2 = internet.hashtags(quantity=3)
    test3 = internet.hashtags(quantity=5)
    assert isinstance(test1, str) and isinstance(test2, list) and isinstance(test3, list)

# Generated at 2022-06-14 00:21:08.454458
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    stock_image = internet.stock_image()
    assert isinstance(stock_image, str)

# Generated at 2022-06-14 00:21:12.497017
# Unit test for method port of class Internet
def test_Internet_port():
    provider = Internet()
    result = provider.port(port_range=PortRange.PRIVILEGED)
    assert result in range(1, 1024)

    result = provider.port(port_range=PortRange.ALL)
    assert result in range(1, 65535)

    result = provider.port(port_range=PortRange.UNPRIVILEGED)
    assert result in range(1024, 65535)

# Generated at 2022-06-14 00:21:21.623085
# Unit test for method port of class Internet
def test_Internet_port():
    from mimesis.enums import PortRange
    from mimesis.exceptions import NonEnumerableError
    from mimesis.typing import Seed

    seed = Seed.create_seed()
    internet = Internet(seed)

    test_range1 = PortRange.ALL

    res1 = internet.port(test_range1)
    assert res1 >= test_range1.value[0]
    assert res1 <= test_range1.value[1]

    test_range2 = PortRange.WELLKNOWN

    res2 = internet.port(test_range2)
    assert res2 >= test_range2.value[0]
    assert res2 <= test_range2.value[1]

    test_range3 = PortRange.UNPRIVILEGED

    res3 = internet.port(test_range3)

# Generated at 2022-06-14 00:21:27.520668
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet

    internet = Internet('ru')
    result = internet.stock_image(width=500, height=500, keywords=['nature'])
    assert result == 'https://source.unsplash.com/500x500?nature'



# Generated at 2022-06-14 00:21:34.922766
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import MimeType
    from mimesis import Internet
    generator = Internet()
    assert generator.stock_image(
        width=1920,
        height=1080,
        writable=True)
    assert generator.stock_image(
        width=1920,
        height=1080,
        keywords=[
            'cat',
            'dog',
        ])
    assert 'Content-Type: image/jpeg' in generator.content_type(
        MimeType.IMAGE)

# Generated at 2022-06-14 00:21:44.524036
# Unit test for method port of class Internet
def test_Internet_port():
    """Unit test for method port of class Internet."""
    from mimesis.enums import PortRange

    port_range_lst = [PortRange.ALL, PortRange.SYSTEM, PortRange.USER]
    provider = Internet()
    for _ in range(10):
        random_port = provider.port()
        assert isinstance(random_port, int)
        assert 0 <= random_port <= 65535

    for port_range in port_range_lst:
        for _ in range(10):
            random_port = provider.port(port_range=port_range)
            assert isinstance(random_port, int)
            assert 0 <= random_port <= 65535

# Generated at 2022-06-14 00:21:46.709643
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    print(provider.stock_image(800,600))

# Generated at 2022-06-14 00:21:54.977651
# Unit test for method port of class Internet
def test_Internet_port():
    internet = Internet()
    for i in range(10):
        assert internet.port(PortRange.ALL) >= 0
        assert internet.port(PortRange.ALL) <= 65535
        assert internet.port(PortRange.WELL_KNOWN) >= 0
        assert internet.port(PortRange.WELL_KNOWN) <= 1023
        assert internet.port(PortRange.REGISTERED) >= 1024
        assert internet.port(PortRange.REGISTERED) <= 49151
        assert internet.port(PortRange.DYNAMIC) >= 49152
        assert internet.port(PortRange.DYNAMIC) <= 65535
        assert internet.port(PortRange.PRIVATE) >= 49152
        assert internet.port(PortRange.PRIVATE) <= 65535

# Generated at 2022-06-14 00:21:59.789789
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    i = Internet('en')
    a = i.hashtags(quantity=0)
    assert a == []

    a = i.hashtags(quantity=1)
    assert isinstance(a, str)

    a = i.hashtags(quantity=4)
    assert isinstance(a, list)
    assert len(a) == 4

# Generated at 2022-06-14 00:22:57.170831
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    # Check for correct number of hashtags in case of a string
    assert len(Internet().hashtags(quantity=1)) == 1

    # Check for correct number of hashtags in case of a list
    assert len(Internet().hashtags(quantity=4)) == 4

# Generated at 2022-06-14 00:23:06.788305
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    i = Internet()
    img = i.stock_image(writable=True)
    img_url = i.stock_image()

    from PIL import Image

    Image.open(img).save('temp_img.jpg')
    # Check URL
    assert img_url == 'https://source.unsplash.com/1920x1080',\
        'URL to stock image is not valid'
    # Check temporary file
    assert Image.open('temp_img.jpg'),\
        'Image received via HTTP is empty'

# Generated at 2022-06-14 00:23:14.317840
# Unit test for method port of class Internet
def test_Internet_port():
    internet = Internet()
    ports = [internet.port(port_range=pr) for pr in PortRange]

    assert len(ports) == len(list(PortRange))
    for port in ports:
        if port < PortRange.SYSTEM:
            assert port in range(*PortRange.SYSTEM.value)
            continue
        if port < PortRange.USER:
            assert port in range(*PortRange.USER.value)
            continue
        if port < PortRange.ALL:
            assert port in range(*PortRange.ALL.value)
            continue

# Generated at 2022-06-14 00:23:16.918356
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    i = Internet()
    print(i.hashtags())
# >>> ['#moment', '#southeastasian', '#heart']


# Generated at 2022-06-14 00:23:26.021948
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Localization
    from mimesis.exceptions import NonEnumerableError
    from mimesis.providers.internet import Internet
    from mimesis.providers.network import Network

    internet = Internet(seed=42)
    network = Network(seed=42)

    for _ in range(10):
        ip = network.ipv4()
        port = internet.port()

        assert ip == '222.169.180.188'
        assert port == 7106

# Generated at 2022-06-14 00:23:30.686554
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    assert provider.stock_image(100,100, ['dog']) == 'https://source.unsplash.com/100x100?dog'

# Generated at 2022-06-14 00:23:36.133138
# Unit test for method port of class Internet
def test_Internet_port():
    Internet().port()
    Internet().port(PortRange.ALL)
    Internet().port(PortRange.SYSTEM)
    Internet().port(PortRange.REGISTERED)
    Internet().port(PortRange.DYNAMIC)
    Internet().port(PortRange.EPHEMERAL)
    Internet().port(PortRange.WELL_KNOWN)


# Generated at 2022-06-14 00:23:47.659430
# Unit test for method port of class Internet
def test_Internet_port():
    from random import seed
    from pytest import raises
    from mimesis.exceptions import NonEnumerableError
    from mimesis.enums import PortRange
    from mimesis.providers.internet import Internet


    class TestPort:

        def setup_class(self):
            self.internet = Internet('bg')
            self.port_range = PortRange.ALL


        def teardown_class(self):
            del self.internet
            del self.port_range


        def test_port(self):
            seed(0)
            result = self.internet.port(port_range=self.port_range)
            assert result == 69942


        def test_port_raises(self):
            with raises(NonEnumerableError):
                self.internet.port(port_range='')

# Generated at 2022-06-14 00:23:54.381693
# Unit test for method port of class Internet
def test_Internet_port():
    i = Internet()
    assert i.port(port_range=PortRange.STANDARD) in range(1024, 49151)
    assert i.port(port_range=PortRange.NON_STANDARD) in range(49152, 65535)
    assert i.port(port_range=PortRange.ALL) in range(1, 65535)
    assert i.port(port_range=PortRange.ALL) in range(1, 65535)

# Generated at 2022-06-14 00:23:55.505092
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    Internet().stock_image()

# Generated at 2022-06-14 00:24:41.821691
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    inte = Internet()
    print(inte.stock_image())

if __name__ == '__main__':
    test_Internet_stock_image()

# Generated at 2022-06-14 00:24:44.913004
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    print(Internet.stock_image(width=500, height=500,
                               keywords=['cat','dog','bird','squirrel'], writable=True))

test_Internet_stock_image()

# Generated at 2022-06-14 00:24:49.512065
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.data import KEYWORDS

    internetprovider = Internet()
    url = internetprovider.stock_image(900, 180, KEYWORDS)
    print(url)

    writable = internetprovider.stock_image(900, 180, KEYWORDS, True)
    with open('new_image.jpg', 'wb') as f:
        f.write(writable)

# Generated at 2022-06-14 00:25:00.996999
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Layer, PortRange, MimeType, TLDType

    i = Internet(seed=42)

    assert i.stock_image(width=100, height=100) == 'https://source.unsplash.com/100x100'
    assert i.stock_image(width=100, height=100, keywords=['coffee']) == 'https://source.unsplash.com/100x100?coffee'
    assert i.stock_image(width=100, height=100, keywords=['coffee', 'forest']) == 'https://source.unsplash.com/100x100?coffee,forest'

    assert i.top_level_domain() == '.com'
    assert i.top_level_domain(tld_type=TLDType.COUNTRY) == '.at'


# Generated at 2022-06-14 00:25:04.432086
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test random_stock_image method of class Internet."""
    INTERNET = Internet()
    image = INTERNET.stock_image(width=50, height=50, writable=True)

# Generated at 2022-06-14 00:25:19.616304
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import TLDType
    from mimesis.providers.internet import Internet
    from mimesis.seed import each
    with each() as seed:
        internet = Internet(seed=seed)
        # When keyword argument `writable` is True or omitted,
        # this method returns 2 URLs and 2 bytes objects,
        # each of them corresponding to a different seed.
        # This is the result obtained with seed value of `seed`
        # and is expected to be reproduced when seed is set to `seed`.
        assert internet.stock_image() == \
            'https://source.unsplash.com/1920x1080/?springs,dawn'
        assert internet.stock_image() == \
            'https://source.unsplash.com/1920x1080/?springs,dawn'
        assert internet.stock

# Generated at 2022-06-14 00:25:29.092322
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import PortRange
    from mimesis.enums import Layer
    from mimesis.enums import TLDType
    from mimesis.enums import MimeType
    from mimesis.enums import PortRange
    from mimesis.enums import Layer
    from mimesis.enums import Gender
    from mimesis.providers.internet import Internet
    internet = Internet()
    print(internet.top_level_domain(tld_type=TLDType.CC))
    print(internet.top_level_domain())
    print(internet.home_page(tld_type=TLDType.CC))
    print(internet.home_page())
    print(internet.hashtags(quantity=4))
    print(internet.hashtags(quantity=1))

# Generated at 2022-06-14 00:25:32.740807
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    # image = Internet().stock_image(writable=True)
    # with open('image.jpg', 'wb') as f:
    #     f.write(image)
    # print(image)
    assert True

# Generated at 2022-06-14 00:25:34.434655
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    image = Internet().stock_image()
    assert isinstance(image, str)

# Generated at 2022-06-14 00:25:39.145482
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()

    assert isinstance(internet.stock_image(), str)
    assert isinstance(internet.stock_image(writable=True), bytes)



# Generated at 2022-06-14 00:26:12.480240
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    assert internet.stock_image() is not None

# Generated at 2022-06-14 00:26:22.126757
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import PortRange
    from mimesis.providers.internet import Internet
    from mimesis.providers.file import File
    internet = Internet('es')
    file= File('es')
    #     assert internet.port(PortRange.PRIVATE) in range(49152, 65535)
    assert internet.port(PortRange.PRIVATE) in range(49152, 65535)
    assert internet.port(PortRange.PRIVATE) in range(49152, 65535)
    assert internet.port(PortRange.PRIVATE) in range(49152, 65535)
    assert internet.port(PortRange.PRIVATE) in range(49152, 65535)
    assert internet.port(PortRange.PRIVATE) in range(49152, 65535)
    assert internet.port

# Generated at 2022-06-14 00:26:28.262356
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class internet."""
    internet = Internet()
    image = internet.stock_image()
    assert isinstance(image, str)
    image_bytes = internet.stock_image(writable=True)
    assert isinstance(image_bytes, bytes)

# Generated at 2022-06-14 00:26:33.197818
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.builtins import Internet
    assert Internet().stock_image(width=150,
                                  height=150) == 'https://source.unsplash.com/150x150?'


# Generated at 2022-06-14 00:26:36.349081
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    # Step 1: Initialize an object P.
    P = Internet()
    # Step 2: Call the method under test.
    result = P.stock_image()
    print(result)
test_Internet_stock_image()

# Generated at 2022-06-14 00:26:43.991556
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Gender
    internet = Internet(gender=Gender.FEMALE, seed=123)
    assert internet.stock_image() == 'https://source.unsplash.com/50x50?react,react,react,react,react'
    assert internet.stock_image(width=20) == 'https://source.unsplash.com/20x1080?react,react,react,react,react'
    assert internet.stock_image(height=20) == 'https://source.unsplash.com/1920x20?react,react,react,react,react'
    assert internet.stock_image(width=20, height=20) == 'https://source.unsplash.com/20x20?react,react,react,react,react'


# Generated at 2022-06-14 00:26:51.611892
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    stock_image_1 = Internet().stock_image()
    assert stock_image_1 == "https://source.unsplash.com/1920x1080?showcase"

    stock_image_2 = Internet().stock_image(keywords=['showcase'])
    assert stock_image_2 == "https://source.unsplash.com/1920x1080?showcase"

    stock_image_3 = Internet().stock_image(keywords=['showcase', 'food'])
    assert stock_image_3 == "https://source.unsplash.com/1920x1080?showcase,food"


# Generated at 2022-06-14 00:27:02.591710
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    import os
    import base64

    from mimesis.providers.file import File

    i = Internet()

    # Download image from Unsplash
    image = i.stock_image(writable=True)

    # Save image to file
    filename = 'test_stock_image.jpg'
    with open(filename, 'wb') as f:
        f.write(image)

    # Check if image has been downloaded
    assert os.path.getsize(filename) > 0

    # Encode image as base64
    with open(filename, 'rb') as f:
        encoded = base64.b64encode(f.read())
        encoded_image = encoded.decode('utf-8')

    # Generate random image
    file = File()
    image_url = file.image(writable=True)

    #

# Generated at 2022-06-14 00:27:13.302997
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    print(internet.stock_image())
    print(internet.stock_image(width=1000, height=700, keywords=['cat']))
    print(internet.stock_image(width=1920, height=1080, keywords=['cat', 'dog', 'spider']))
    print(internet.stock_image(width='1000', height='700', keywords=['cat']))
    print(internet.stock_image(width='1000', height='700', keywords=['cat', 'dog', 'spider']))


# Generated at 2022-06-14 00:27:17.503884
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.enums import Layer
    from mimesis.exceptions import NonEnumerableError
    i = Internet()
    assert(i.stock_image() == i.stock_image(writable = False))
    try:
        i.stock_image(writable = True)
    except urllib.error.URLError:
        pass

# Generated at 2022-06-14 00:28:27.909926
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    obj = Internet()
    obj.stock_image()

# Generated at 2022-06-14 00:28:31.901549
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test method stock_image of class Internet."""
    internet = Internet()
    image = internet.stock_image()
    assert isinstance(image, str)
    assert image.startswith('https://source.unsplash.com')
    assert image.endswith('.jpg')

# Generated at 2022-06-14 00:28:34.122616
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    url = internet.stock_image()
    assert url

# Generated at 2022-06-14 00:28:36.874393
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    stock_image = provider.stock_image(writable=True)
    print(len(stock_image))
    # print(stock_image)

# Generated at 2022-06-14 00:28:40.346106
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    random_image = Internet().stock_image(width= '500', height= '500')
    error_random_image = 'http://source.unsplash.com/500x500?'
    assert (random_image == error_random_image)


# Generated at 2022-06-14 00:28:41.535580
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    assert internet.stock_image()

# Generated at 2022-06-14 00:28:49.946899
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Resolution

    i = Internet()
    width = Resolution.WIDE.value
    height = Resolution.WIDE.value
    keywords = ['ship', 'boat']
    assert isinstance(i.stock_image(width=width, height=height), str)
    assert isinstance(i.stock_image(keywords=keywords), str)
    assert isinstance(i.stock_image(width=width, height=height, writable=True), bytes)

# Generated at 2022-06-14 00:28:51.319826
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    u = Internet()
    image = u.stock_image()
    assert(isinstance(image, str) == True)

# Generated at 2022-06-14 00:28:56.740517
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    stock_image = Internet.stock_image()
    print(stock_image)
    assert stock_image == 'https://source.unsplash.com/1920x1080?'
    keywords = ['tiger', 'forest']
    stock_image = Internet.stock_image(keywords=keywords)
    print(stock_image)
    assert stock_image == 'https://source.unsplash.com/1920x1080?tiger,forest'

# Generated at 2022-06-14 00:29:09.372974
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test for method stock_image of class Internet."""
    print("-" * 65)
    print("Testing for method stock_image of class Internet")
    print("-" * 65)

    from mimesis import Internet
    from mimesis.enums import Layer

    rand_values = {}

    rand_values['protocol'] = Internet().network_protocol(
        layer=Layer.INTERNET)

    rand_values['ip'] = Internet().ip_v4(with_port=True)

    url = ('{protocol}://{ip}/'.format(**rand_values))

    print("Random link: {}".format(url))

    result = Internet().stock_image()
    print("Method without params: {}".format(result))

    result = Internet().stock_image(width=200, height=200)