

# Generated at 2022-06-14 00:20:53.513959
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
	internet = Internet('en')
	print(internet.stock_image())


if __name__=='__main__':
	test_Internet_stock_image()

# Generated at 2022-06-14 00:20:57.410691
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    # print(internet.stock_image())
    # print(internet.stock_image(width=300, height=300))
    # print(internet.stock_image(keywords=['animals', 'cats']))

# Generated at 2022-06-14 00:21:08.413358
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    print('\nTest method stock_image of class Internet\n')
    internet = Internet()
    stock_image = internet.stock_image(width=1920, height=1080)
    print(stock_image)

    assert 'https://source.unsplash.com/1920x1080' in stock_image
    assert '.jpg' in stock_image

    try:
        stock_image = internet.stock_image(width=1920, height=1080, writable=True)
        assert isinstance(stock_image, bytes)
    except urllib.error.URLError:
        print('\nRequired an active HTTP connection\n')

# Generated at 2022-06-14 00:21:10.316058
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    test_class = Internet()
    print(test_class.hashtags(quantity=5))

# Generated at 2022-06-14 00:21:16.738187
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Take a screenshot."""
    from os import mkdir
    from os.path import dirname, isdir, join

    path = join(dirname(dirname(dirname(__file__))), 'image')
    if not isdir(path):
        mkdir(path)

    internet = Internet(seed=42)
    image = internet.stock_image()

    with open(join(path, 'unsplash.jpg'), 'wb') as file:
        file.write(image)

# Generated at 2022-06-14 00:21:23.708572
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.data import ANIMALS, SPORTS, GEOGRAPHY, MOVIES

    class Meta:
        name = 'internet'

    class Seed(object):
        def __init__(self, seed):
            self.seed = seed

    class Random(object):
        def __init__(self, seed):
            self.seed = seed

        def randint(self, start, end):
            return start

        def choice(self, iter):
            return iter[0]

    internet = Internet(seed=None)
    internet.__class__.Meta = Meta
    internet.seed = Seed(None)
    internet.random = Random(None)

    width = 1920
    height = 1080


# Generated at 2022-06-14 00:21:32.299488
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis import Internet
    import os
    import shutil
    import tempfile

    dirpath = tempfile.mkdtemp()

    with open(os.path.join(dirpath, 'image.jpg'), 'wb') as f:
        f.write(Internet().stock_image(writable=True))

    assert os.path.getsize(os.path.join(dirpath, 'image.jpg')) > 0
    shutil.rmtree(dirpath)

# Generated at 2022-06-14 00:21:43.732486
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    keywords = ['love', 'sky', 'nice', 'beautiful', 'amazing', 'fantastic']
    internet = Internet()

    res = internet.hashtags()
    assert isinstance(res, str)
    assert '#' in res

    res = internet.hashtags(quantity=1)
    assert isinstance(res, str)
    assert '#' in res

    res = internet.hashtags(quantity=4)
    assert isinstance(res, list)
    for _ in range(4):
        assert '#' in res[_]

    res = internet.hashtags(quantity=0)
    assert isinstance(res, list)
    assert len(res) == 0

    res = internet.hashtags(quantity=len(keywords))
    assert isinstance(res, list)

# Generated at 2022-06-14 00:21:47.039459
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    """Unit test for method hashtags of class Internet."""
    internet = Internet()
    tags = internet.hashtags()
    assert isinstance(tags, list)
    assert len(tags) == 4



# Generated at 2022-06-14 00:21:52.540833
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    image = internet.stock_image(writable=True)
    save_image = open('image.jpg', 'wb')
    save_image.write(image)
    save_image.close()

# Generated at 2022-06-14 00:22:20.336719
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    # Allowed method parameters 
    assert Internet.stock_image(width = '640', height = '480') == 'https://source.unsplash.com/640x480?', 'Allowed method parameters'
    assert Internet.stock_image(width = 640, height = 480, keywords = 'cat') == 'https://source.unsplash.com/640x480?cat', 'Allowed method parameters'
    assert Internet.stock_image(width = 640, height = 480, keywords = ['cat', 'kitty']) == 'https://source.unsplash.com/640x480?cat,kitty', 'Allowed method parameters'
    assert Internet.stock_image(width = '1920', height = '1080') == 'https://source.unsplash.com/1920x1080?', 'Allowed method parameters'
    assert Internet.stock_image

# Generated at 2022-06-14 00:22:27.635057
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.enums import MimeType
    from PIL import Image
    import io

    provider = Internet()

    # test for return link to image
    url = provider.stock_image()
    assert url == 'https://source.unsplash.com/1920x1080?'

    # test for keywords
    url = provider.stock_image(keywords=['nature'])
    assert url == 'https://source.unsplash.com/1920x1080?nature'
    url = provider.stock_image(keywords=['nature', 'house'])
    assert url == 'https://source.unsplash.com/1920x1080?nature,house'

    # test for writable

# Generated at 2022-06-14 00:22:29.409070
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    Internet.stock_image(1920, 1080, ['nature'], writable=True)

# Generated at 2022-06-14 00:22:33.644810
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    internet = Internet('en')
    image_url = internet.stock_image()
    assert image_url[0:12] == 'https://source'

# Generated at 2022-06-14 00:22:38.476123
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from PIL import Image
    from io import BytesIO
    internet = Internet()
    link = internet.stock_image(200, 200, writable=True)
    if link:
        img = Image.open(BytesIO(link))
        assert img.size == (200, 200)

# Generated at 2022-06-14 00:22:42.082279
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    print(internet.stock_image())
    print(internet.stock_image('800', '800'))
    print(internet.stock_image('800', '800', keywords=['nature', 'mountain']))



# Generated at 2022-06-14 00:22:46.639473
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    image_generator = Internet(seed = 12)
    assert image_generator.stock_image(width = 20, height = 40) == "https://source.unsplash.com/20x40?fitness"

# Generated at 2022-06-14 00:22:48.988202
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    assert internet.stock_image() == "https://source.unsplash.com/1920x1080"

# Generated at 2022-06-14 00:22:51.315444
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    assert internet.stock_image().startswith('https://source.unsplash.com/1920x1080?')

# Generated at 2022-06-14 00:23:02.207586
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import SizeUnit
    from mimesis.providers.internet import Internet
    internet = Internet()
    image = internet.stock_image(width=800, height=600,
                                 keywords=['nature', 'water'],
                                 writable=True)
    # Check that it's of type 'bytes'
    assert isinstance(image, bytes)
    # Check that it has the right size
    assert len(image) == 800 * 600 * 3 + 1024 # Account for the 1kb of metadata
    # Test that it can be read by Pillow
    import PIL
    PIL.Image.open(io.BytesIO(image))


# Generated at 2022-06-14 00:24:02.247505
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    generator = Internet()
    for i in range(10):
        assert type(generator.stock_image()) == str
        assert generator.stock_image().startswith('https://source.unsplash.com')


# Generated at 2022-06-14 00:24:04.954279
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    print(Internet().stock_image())

# Generated at 2022-06-14 00:24:11.713189
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    image = provider.stock_image(1920, 1080, keywords=['mimesis', 'cat'])
    assert isinstance(image, str)
    assert image.startswith('https://')
    assert image.endswith('1920x1080?mimesis,cat')

# Generated at 2022-06-14 00:24:13.340716
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    inte = Internet(seed=8)
    inte.stock_image()


# Generated at 2022-06-14 00:24:15.262867
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    result = provider.stock_image(writable=True)
    assert isinstance(result, bytes)

# Generated at 2022-06-14 00:24:19.471246
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    inter = Internet()
    link = inter.stock_image()
    assert isinstance(link, str)
    assert link.startswith('https://')

# Generated at 2022-06-14 00:24:24.935060
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    obj = Internet()
    res = obj.stock_image()
    assert res.startswith('https://source.unsplash.com/') is True
    res = obj.stock_image(writable=True)
    assert res.startswith(b'\xff\xd8') is True

# Generated at 2022-06-14 00:24:26.576909
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    assert internet.stock_image().find('http') == 0

# Generated at 2022-06-14 00:24:35.406644
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.builtins import Internet
    import os
    try:
        # url = 'https://source.unsplash.com/400x200?dog,cat'
        internet = Internet()
        url = internet.stock_image(1600,1200, ['nature'])
        print(url)
        response = urllib.request.urlopen(url)
        image = response.read()

        with open('image.jpeg', 'wb') as file:
            file.write(image)
        print(os.path.abspath('image.jpeg'))
    except urllib.error.URLError as e:
        print(e.reason)

if __name__ == '__main__':
    test_Internet_stock_image()

# Generated at 2022-06-14 00:24:45.437276
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet

    internet = Internet()
    # Should return 'https://source.unsplash.com/1920x1080'
    assert (internet.stock_image(keywords=None,
              width=1920,
              height=1080,
              writable=False))

    # Will return writable object
    stock_image = internet.stock_image(keywords=['random', 'image'],
                                       width=1920,
                                       height=1080,
                                       writable=True)
    assert (isinstance(stock_image, bytes))
