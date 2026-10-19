

# Generated at 2022-06-14 00:20:53.394204
# Unit test for method port of class Internet
def test_Internet_port():
    from mimesis.enums import PortRange

    internet = Internet()
    min_value, max_value = PortRange.ALL.value
    assert min_value <= internet.port() <= max_value

    min_value, max_value = PortRange.WELL_KNOWN.value
    assert min_value <= internet.port(port_range=PortRange.WELL_KNOWN) <= max_value

# Generated at 2022-06-14 00:20:56.858918
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    hash = Internet()
    assert isinstance(hash.hashtags(), list) == True
    assert len(hash.hashtags()) == 4
    assert isinstance(hash.hashtags(1), str) == True

# Generated at 2022-06-14 00:20:59.513317
# Unit test for method port of class Internet
def test_Internet_port():
    """Unit test for method port of class Internet."""
    internet = Internet()
    for i in range(100):
        port = internet.port()

        assert (0 < port < 65535)

# Generated at 2022-06-14 00:21:05.685072
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from PIL import Image
    from io import BytesIO

    internet = Internet()
    img_bytes = internet.stock_image(writable=True)
    img = Image.open(BytesIO(img_bytes))

    assert img.format == 'JPEG'

# Generated at 2022-06-14 00:21:09.025416
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    from mimesis.enums import Hashtag

    internet = Internet('cs')
    assert internet.hashtags(Hashtag.FOOD) == ['#kyselina', '#snídaně',
                                               '#dieta', '#zdravé']

# Generated at 2022-06-14 00:21:13.978595
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    path = internet.stock_image(writable=True)
    # проверяем, что результат - объект класса int
    assert isinstance(path, int)


# Generated at 2022-06-14 00:21:18.176985
# Unit test for method port of class Internet
def test_Internet_port():
  s = Internet()
  d = s.port()
  assert (d < 65536) and (d > 0)


# Generated at 2022-06-14 00:21:24.520485
# Unit test for method port of class Internet
def test_Internet_port():
    '''
    def port(self, port_range: PortRange = PortRange.ALL) -> int:
        """Generate random port.
        :param port_range: PortRange enum object.
        :return: Port number.
        :raises NonEnumerableError: if port_range is not in PortRange.
        :Example:
            8080
        """
        if isinstance(port_range, PortRange):
            return self.random.randint(*port_range.value)

        raise NonEnumerableError(PortRange)
    '''
    import unittest
    from mimesis.enums import PortRange
    from mimesis.providers.internet import Internet
    import mimesis.enums

    class Test_port(unittest.TestCase):
        def setUp(self):
            self.port_range

# Generated at 2022-06-14 00:21:36.466091
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import PortRange
    from mimesis.providers.internet import Internet
    from mimesis.providers.utils import default_seed
    from mimesis.typing import Seed

    # Seed for current class
    _seed = '3972190980402496'
    # _seed = '3972190980402496'
    # _seed = '3972190980402496'

    # Seed for all classes
    # seed = '3972190980402496'

    seed = default_seed

    # You can use a seed different from the default by changing the
    # value of the global variable _seed.
    #
    # In this case, the results obtained by this program will always be
    # the same, otherwise the results will be different.
    #
    # If the

# Generated at 2022-06-14 00:21:37.813647
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    assert Internet().stock_image()

# Generated at 2022-06-14 00:21:52.610781
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    test_str = internet.stock_image(writable = True)
    if isinstance(test_str,bytes):
        pass
    else:
        assert False

# Generated at 2022-06-14 00:22:02.284314
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    import os
    import sys
    import unittest

    try:
        # noinspection PyUnresolvedReferences
        import PIL
    except ImportError:
        # noinspection PyUnresolvedReferences
        import PIL.Image as PIL

    # noinspection PyUnresolvedReferences
    import requests

    class TestInternet(unittest.TestCase):

        def setUp(self):
            self.TEST_DIRECTORY = os.path.dirname(
                os.path.abspath(sys.modules['__main__'].__file__),
            )
            self.INTERNET = Internet('en')


# Generated at 2022-06-14 00:22:12.075745
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test for method stock_image of class Internet."""
    from unittest import TestCase
    from mimesis.enums import PortRange

    class TestInternet(TestCase):

        def setUp(self):
            self.inter = Internet('en')

        def test_stock_image(self):
            keywords = ['sky', 'sea']
            image = self.inter.stock_image(keywords=keywords)
            self.assertIsInstance(image, str)
            self.assertEqual(image, 'https://source.unsplash.com/1920x1080?sky,sea')

            image = self.inter.stock_image(keywords=keywords, writable=True)
            self.assertIsInstance(image, bytes)

        def test_image_placeholder(self):
            image = self.inter.image_place

# Generated at 2022-06-14 00:22:23.942063
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import PortRange
    from mimesis.providers.internet import Internet
    internet = Internet()
    print(internet.home_page())
    print(internet.image_placeholder())
    print(internet.ip_v4(with_port=True, port_range=PortRange.HIGH))
    print(internet.ip_v6())
    print(internet.user_agent())
    print(internet.port(PortRange.ALL))
    print(internet.port(PortRange.LOW))
    print(internet.port(PortRange.HIGH))
    print(internet.port(PortRange.SYSTEM))
    print(internet.port(PortRange.REGISTERED))
    print(internet.ip_v4(port_range=PortRange.PRIVATE))

# Generated at 2022-06-14 00:22:26.076686
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    tester = Internet()
    assert type(tester.stock_image()) == str

# Generated at 2022-06-14 00:22:29.137794
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    image = internet.stock_image()
    assert isinstance(image, str)

# Generated at 2022-06-14 00:22:34.396016
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    img = Internet().stock_image()
    assert type(img) is str
    assert img.startswith("https")
    assert img.endswith("?random")


if __name__ == '__main__':
    test_Internet_stock_image()

# Generated at 2022-06-14 00:22:39.169733
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    assert Internet().stock_image(keywords=['nature', 'beautiful']) == 'https://source.unsplash.com/1920x1080?nature,beautiful'
    Internet().stock_image(keywords=['nature', 'beautiful'], writable=True)

# Generated at 2022-06-14 00:22:41.111343
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    img_url = provider.stock_image()
    assert img_url.startswith('http')

# Generated at 2022-06-14 00:22:47.118941
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Width, Height

    net = Internet()
    keywords = net.random.choice(Height.short.value)
    net.stock_image(width=Width.high.value, height=keywords)

test_Internet_stock_image()

# Generated at 2022-06-14 00:23:09.477045
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Width, Height
    from mimesis.exceptions import FormatFunctionFailed
    from PIL import Image
    import base64
    import io
    import shutil
    import sys
    import tempfile

    test_out = False

# Generated at 2022-06-14 00:23:11.580061
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test automatically."""
    i = Internet()
    a = i.stock_image()
    assert a is not None
    assert isinstance(a, str)

# Generated at 2022-06-14 00:23:13.975720
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    obj = Internet()
    res = obj.stock_image()
    print(res)

# Generated at 2022-06-14 00:23:19.883566
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    i = Internet()
    assert isinstance(i.stock_image(), str)
    assert isinstance(i.stock_image(writable=True), bytes)
    assert i.stock_image().startswith('https://')
    assert i.stock_image(writable=True).startswith(b'\xff\xd8\xff')

# Generated at 2022-06-14 00:23:21.051599
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    assert type(Internet().stock_image()) == str

# Generated at 2022-06-14 00:23:26.595891
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internetGen = Internet()
    print(str(internetGen.stock_image()))
    print(str(internetGen.stock_image(keywords=["dog", "cat"])))
    print(str(internetGen.stock_image(keywords=["dog"])))


# Generated at 2022-06-14 00:23:35.091378
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from unittest import TestCase
    from io import BytesIO
    from PIL import Image

    class InternetTestCase(TestCase):

        def test_Internet_stock_image(self):
            internet = Internet()
            image = internet.stock_image(writable=True)
            image = BytesIO(image)
            self.assertIsInstance(Image.open(image), Image.Image)

    InternetTestCase().test_Internet_stock_image()

# Generated at 2022-06-14 00:23:37.921560
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    inte = Internet()
    assert inte.stock_image()


# Generated at 2022-06-14 00:23:43.613477
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    import matplotlib.pyplot as plt
    import os
    p = Internet()
    img = p.stock_image(writable=True)
    plt.imshow(img, origin='upper')
    plt.show()

# Generated at 2022-06-14 00:23:52.403613
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    url = 'https://images.unsplash.com/photo-1542044896520-33b0b8ebb8e9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=80'
    actual = internet.stock_image(1920, 1080)
    assert actual == url

# Generated at 2022-06-14 00:25:28.782626
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    # Active HTTP connection required
    image_url = internet.stock_image()
    assert image_url


# Generated at 2022-06-14 00:25:35.891219
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Gender

    # Create a new instance of class Internet
    inter = Internet('en', Gender.MALE)
    # Generate random stock image link
    link = inter.stock_image()
    print(link)

if __name__ == "__main__":
    test_Internet_stock_image()

# Generated at 2022-06-14 00:25:38.669614
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    img = internet.stock_image(
        width=200,
        height=200,
        keywords=[
            'people', 'nature',
        ],
        writable=True
    )
    assert isinstance(img, bytes)

# Generated at 2022-06-14 00:25:45.499470
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test Internet.stock_image method."""
    from mimesis.providers.file import MimeType
    image = Internet().stock_image(
        width=640,
        height=480,
        keywords=['city'],
        writable=True,
    )
    file = File(seed=0)
    mime = file.mime_type(MimeType.IMAGE)
    assert mime in str(image)

# Generated at 2022-06-14 00:25:52.363049
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet"""
    import os, io, sys
    from io import BytesIO
    from PIL import Image

    image_bytes = io.BytesIO(Internet().stock_image(writable=True))
    print(image_bytes)
    print(bytes(image_bytes))

    im = Image.open(image_bytes)
    im.verify()
    im.show()


# Generated at 2022-06-14 00:25:54.975867
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    assert internet.stock_image() == 'https://source.unsplash.com/1920x1080?', "Internet.stock_image()"
    assert internet.stock_image(width=1000, height=500, keywords=['nature']) == 'https://source.unsplash.com/1000x500?nature', "Internet.stock_image()"

# Generated at 2022-06-14 00:25:58.547569
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    a, b = Internet().stock_image()
    print(a, b)

if __name__ == '__main__':
    test_Internet_stock_image()

# Generated at 2022-06-14 00:26:08.439465
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from pprint import pprint
    
    seed = 0
    test_file = "test.jpg"
    test_period = 10
    test_width = 500
    test_height = 500
    
    for test_count in range(test_period):
        random_generator = Internet(seed=seed)
        
        test_data = random_generator.stock_image(width=test_width,
                                                 height=test_height,
                                                 writable=True)
        
        with open(test_file, "wb") as file:
            file.write(test_data)
        
        print(f"Test count: {test_count}")
        print(f"Test seed: {seed}")
        
        seed += 1
        

# Generated at 2022-06-14 00:26:12.278745
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    global Internet
    Internet = Internet()
    r = Internet.stock_image()
    assert r == "https://source.unsplash.com/1920x1080?/Users/home/anaconda3/lib/python3.7/urllib/request.py"

# Generated at 2022-06-14 00:26:15.886324
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    rand_seed = randint(0, 10000)
    provider = Internet(seed=rand_seed)
    try:
        provider.stock_image(writable=True)
    except:
        assert True
    else:
        assert False
