

# Generated at 2022-06-14 00:21:16.531872
# Unit test for method stock_image of class Internet
def test_Internet_stock_image(): 
    internet = Internet(random_state=1)
    image = internet.stock_image(width=200, height=200, keywords=['People'])
    assert image == 'https://source.unsplash.com/200x200?People'


# Generated at 2022-06-14 00:21:19.287335
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    provider = Internet()
    res = provider.hashtags()
    assert isinstance(res, str) or isinstance(res, list)
    if (isinstance(res, list)):
        assert len(res) == 4

# Generated at 2022-06-14 00:21:20.756395
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    Internet()

# Generated at 2022-06-14 00:21:23.154953
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    image = internet.stock_image()
    assert image.startswith('https://')

# Generated at 2022-06-14 00:21:33.362580
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.enums import Language
    from pathlib import Path
    import PIL.Image

    path = Path(__file__).parent / 'image_test.jpg'
    inte = Internet(language=Language.EN)
    with path.open('wb') as f:
        f.write(inte.stock_image(width=1920, height=1024, writable=True))
    data = PIL.Image.open(path)

    # Check width.
    assert data.width == 1920

    # Check height.
    assert data.height == 1024

# Generated at 2022-06-14 00:21:44.382525
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    import os
    # set the path for saving stock image
    path = "..\\results\\internet\\stock_image\\"
    # create instance of Internet
    internet = Internet()
    # create image as sequence of bytes and save this image to the path
    # in JPG/JPEG format
    img = internet.stock_image(writable=True, keywords=['sun'])
    os.makedirs(path, exist_ok=True)
    with open(path + "sun.jpg", mode="wb") as f:
        f.write(img)
    # create image as sequence of bytes and save this image to the path
    # in JPG/JPEG format
    img = internet.stock_image(writable=True, keywords=["airplane"])

# Generated at 2022-06-14 00:21:51.159367
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    print("Unit test for method hashtags of class Internet")
    internet = Internet()
    internet.seed(1)
    ret = internet.hashtags()
    assert (ret == ['#love', '#sky', '#nice'])
    assert (type(ret) == list)


# Generated at 2022-06-14 00:21:54.329483
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    img = internet.stock_image()
    assert isinstance(img, str)
    assert img.startswith('https://')
    img = internet.stock_image(writable=True)
    assert isinstance(img, bytes)
    assert len(img) > 0

# Generated at 2022-06-14 00:21:58.845288
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from PIL import Image
    from io import BytesIO

    internet = Internet('en')
    imageBytes = internet.stock_image(writable=True)

    image = Image.open(BytesIO(imageBytes))
    assert image.size[0] == 1920
    assert image.size[1] == 1080

# Generated at 2022-06-14 00:22:01.522715
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    internet = Internet()
    test_result = '#love, #sky, #nice, #school'
    assert (internet.hashtags(quantity=4) == test_result)

# Generated at 2022-06-14 00:22:28.297874
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet() 
    print(internet.stock_image())

# Generated at 2022-06-14 00:22:34.104719
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    internet = Internet(random=False)

    tags = internet.hashtags(quantity=6)
    print(tags)


# Generated at 2022-06-14 00:22:36.375896
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    internet = Internet()
    hashtag = internet.hashtags()
    assert hashtag in HASHTAGS


# Generated at 2022-06-14 00:22:40.116997
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    print(Internet().hashtags())

# Generated at 2022-06-14 00:22:53.306382
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    from mimesis.enums import Hashtag

    h = Internet(seed=1559)

    hashtags = h.hashtags(quantity=4, category=Hashtag.NAMES)
    assert hashtags == ['#vinod', '#rajendra', '#vikash', '#ashok']

    hashtags = h.hashtags(quantity=4, category=Hashtag.FLOWER)
    assert hashtags == ['#lotus', '#jasmine', '#sampaguita', '#rose']

    hashtags = h.hashtags(quantity=4, category=Hashtag.SPORTS)
    assert hashtags == ['#cricket', '#football', '#volleyball', '#chess']

    hashtags = h.hashtags(quantity=4, category=Hashtag.WEATHER)

# Generated at 2022-06-14 00:23:04.116158
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet."""

    def test_arg_width():
        """Test method with argument 'width'."""
        internet = Internet()
        width = internet.random.randint(1, 3840 + 1)
        img_url = internet.stock_image(width=width)
        assert img_url.startswith('https://source.unsplash.com/{}x'.format(width))

    def test_arg_height():
        """Test method with argument 'height'."""
        internet = Internet()
        height = internet.random.randint(1, 2160 + 1)
        img_url = internet.stock_image(height=height)
        assert img_url.startswith('https://source.unsplash.com/x{}'.format(height))


# Generated at 2022-06-14 00:23:09.845977
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    test=Internet()
    image=test.stock_image()
    print(image)
    print('\n')
    print('Test passed successfully.')

if __name__ == '__main__':
    test_Internet_stock_image()

# Generated at 2022-06-14 00:23:16.460573
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    # These calls must not raise exceptions
    assert internet.stock_image()
    assert internet.stock_image(writable=True)
    assert internet.stock_image((500, 500))
    assert internet.stock_image(keywords=('hello', 'world'))
    assert internet.stock_image((500, 500), keywords=('hello', 'world'))
    assert internet.stock_image(writable=True, keywords=('hello', 'world'))
    assert internet.stock_image((500, 500), writable=True)
    assert internet.stock_image((500, 500), writable=True,
                                keywords=('hello', 'world'))

# Generated at 2022-06-14 00:23:19.884262
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    internet = Internet("en")
    schema = {"hashtags": ["#love", "#sky", "#nice"]}
    assert internet.hashtags() == schema["hashtags"]

# Generated at 2022-06-14 00:23:25.041709
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    inst = Internet()
    res = inst.stock_image(1024, 768,
                           ['nature'], True)
    assert res is not None
    assert len(res) > 0