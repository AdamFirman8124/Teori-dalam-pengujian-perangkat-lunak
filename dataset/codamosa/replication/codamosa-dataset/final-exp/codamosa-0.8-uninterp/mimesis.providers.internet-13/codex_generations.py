

# Generated at 2022-06-14 00:21:18.929078
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from PIL import Image
    from io import BytesIO

    internet = Internet('en')
    pic = internet.stock_image(width=300, height=300, keywords='photo')
    assert isinstance(pic, str)

    pic = internet.stock_image(width=300, height=300, keywords=['photo'])
    assert isinstance(pic, str)

    pic = internet.stock_image(width=300, height=300, keywords='photo', writable=True)
    assert isinstance(pic, bytes)

    img = Image.open(BytesIO(pic))
    assert img.width == 300
    assert img.height == 300

# Generated at 2022-06-14 00:21:29.153509
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    import hashlib
    from random import randrange

    from mimesis.data import KEYWORDS
    from mimesis.enums import PortRange
    from mimesis.providers.internet import Internet
    
    internet = Internet()

    width = randrange(50, 2000)
    height = randrange(50, 2000)
    keywords = internet.random.choices(KEYWORDS, k=randrange(1, 10))
    url = internet.stock_image(width, height, keywords)
    image = internet.stock_image(width, height, keywords, True)

    assert url == 'https://source.unsplash.com/{}x{}?'.format(width, height) + ','.join(keywords)

# Generated at 2022-06-14 00:21:31.782797
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    url = internet.stock_image()
    assert url == "https://source.unsplash.com/1920x1080"

# Generated at 2022-06-14 00:21:35.148131
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    assert internet.stock_image() == \
        'https://source.unsplash.com/1920x1080'

# Generated at 2022-06-14 00:21:37.316810
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    stock_image = internet.stock_image(writable=True)
    assert isinstance(stock_image, bytes)

# Generated at 2022-06-14 00:21:40.396196
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet."""
    internet = Internet()
    image = internet.stock_image(100,100,writable=True)
    assert(type(image) == bytes)
    with open('image.jpeg', 'wb') as f:
        f.write(image)
        f.close()

# Generated at 2022-06-14 00:21:43.743072
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    print(internet.stock_image(width=250, height=250))

# Generated at 2022-06-14 00:21:48.005417
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    assert Internet().hashtags() == '#score' or Internet().hashtags() == ['#score', '#brillant',
                                                                          '#smell', '#home']

# Generated at 2022-06-14 00:21:55.267166
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import Category

    internet = Internet()

    # get image by keyword
    img_link = internet.stock_image(keywords=['nature', ])
    assert 'nature' in img_link

    # get image by category
    cat = Category.FASHION
    img_link_2 = internet.stock_image(keywords=[cat.value, ])
    assert img_link != img_link_2

# Generated at 2022-06-14 00:22:02.577262
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    ht = ['#love', '#sky', '#nice']
    ht2 = '#nice'
    internet = Internet()
    assert internet.hashtags(3) == ht
    assert internet.hashtags(1) == ht2
    internet = Internet(seed=123)
    assert internet.hashtags(3) == ht
    assert internet.hashtags(1) == ht2
    internet = Internet(seed=123)
    assert internet.hashtags(3) == ht
    assert internet.hashtags(1) == ht2

# Generated at 2022-06-14 00:22:58.803438
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    i = Internet()
    s = i.stock_image()
    print(s)

# Generated at 2022-06-14 00:23:02.728089
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method Internet_stock_image."""
    assert Internet.stock_image(writable=True) is None

# Generated at 2022-06-14 00:23:03.780480
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    Internet.stock_image()

# Generated at 2022-06-14 00:23:14.936489
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test for method stock_image of class Internet."""
    from mimesis.enums import FileType
    from mimesis.providers.file import File
    from mimesis.providers.internet import Internet

    file = File(seed=0)

# Generated at 2022-06-14 00:23:22.771063
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    Internet().stock_image()
    Internet().stock_image(keywords=['flower', 'nature'])
    Internet().stock_image(width=800, height=600)
    Internet().stock_image(width=800, height=600,
                           keywords=['flower', 'nature'])
    Internet().stock_image(width=800, height=600,
                           keywords=['flower', 'nature'],
                           writable=True)

# Generated at 2022-06-14 00:23:31.343224
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    image_url = internet.stock_image()
    assert image_url[:25] == 'https://source.unsplash.com/'
    assert image_url[-4:] == '.jpg'
    image_url = internet.stock_image(writable=True)
    assert isinstance(image_url, bytes)
    assert isinstance(internet.stock_image(keywords=['test']), str)
    assert isinstance(internet.stock_image(keywords=['test'], writable=True),
                      bytes)

# Generated at 2022-06-14 00:23:33.842664
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    print(Internet.stock_image())


if __name__ == '__main__':
    test_Internet_stock_image()

# Generated at 2022-06-14 00:23:37.890327
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    assert Internet().stock_image()
    assert Internet().stock_image(writable=True)

# Generated at 2022-06-14 00:23:46.297203
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import MimeType, Keyword
    import os
    import tempfile

    internet = Internet('en')
    width = internet.create_number(min=100, max=1000)
    height = internet.create_number(min=100, max=1000)
    keywords = [internet.random.choice(list(Keyword))]
    keywords_str = internet.random.choice(list(Keyword))

    internet.stock_image(width=width, height=height,
        keywords=keywords)
    internet.stock_image(width=width, height=height,
        keywords=keywords_str)

    image = internet.stock_image(width=width, height=height,
        keywords=keywords, writable=True)

    # Create temp file
    temp_file = tempfile.NamedTemporary

# Generated at 2022-06-14 00:23:48.499396
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    x = Internet().stock_image(writable=True)
    f = open("test_image.jpg", "wb")
    f.write(x)
    f.close()

