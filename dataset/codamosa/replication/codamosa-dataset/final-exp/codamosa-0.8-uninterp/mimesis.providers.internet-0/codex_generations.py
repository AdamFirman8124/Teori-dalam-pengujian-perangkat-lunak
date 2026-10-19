

# Generated at 2022-06-14 00:20:49.571598
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    stock_image = internet.stock_image()
    print(stock_image)

# Generated at 2022-06-14 00:20:53.034643
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    t = Internet()
    print(t.hashtags())
    print(t.hashtags(3))

if __name__ == '__main__':
    test_Internet_hashtags()

# Generated at 2022-06-14 00:20:55.604155
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    internet = Internet()
    actual = internet.hashtags(1)
    print(actual)
    assert actual in HASHTAGS


# Generated at 2022-06-14 00:20:58.955903
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    try:
        internet = Internet()
        internet.stock_image(writable=True, height=1000, width=600)
    except urllib.error.URLError:
        assert False

# Generated at 2022-06-14 00:21:05.974031
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from PIL import Image
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".jpg") as f:
        img = Internet().stock_image(writable = True)
        f.write(img)
        f.seek(0)
        Image.open(f.name)
    pass

# Generated at 2022-06-14 00:21:08.060791
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider_internet = Internet()
    result = provider_internet.stock_image(keywords=['dog'], writable=True)
    assert result != None

# Generated at 2022-06-14 00:21:11.282361
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    res = internet.stock_image(640, 480)
    assert res.startswith('https://source.unsplash.com/')
    assert '?is-this-real-life' in res

# Generated at 2022-06-14 00:21:21.471552
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.enums import Layer
    result = Internet().stock_image()
    assert isinstance(result, str)
    assert 'https://' in result
    assert result.endswith('.jpg') or result.endswith('.jpeg')
    result = Internet().stock_image(width=800, height=600)
    assert isinstance(result, str)
    assert 'https://' in result
    assert result.endswith('.jpg') or result.endswith('.jpeg')
    result = Internet().stock_image(keywords=['car', 'mercedes'])
    assert isinstance(result, str)
    assert 'https://' in result
    assert result.endswith('.jpg') or result.endswith('.jpeg')


# Generated at 2022-06-14 00:21:22.996935
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    print(Internet().hashtags())


test_Internet_hashtags()

# Generated at 2022-06-14 00:21:25.570608
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis import Internet
    i = Internet()
    print(i.stock_image())


# Generated at 2022-06-14 00:21:39.600966
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    image = provider.stock_image(width=500, height=500)
    assert image.startswith('https://source.unsplash.com/500x500?') == True


# Generated at 2022-06-14 00:21:53.712409
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.enums import PortRange
    from mimesis.providers.utils import get_data

    i = Internet(seed=123)
    for _ in range(10):
        print(i.stock_image(
            width=320,
            height=240,
            keywords=['water', 'beach'],
            writable=True,
        ))
    i = Internet(123)
    try:
        i.stock_image(
            width=320,
            height=240,
            keywords=['water', 'beach'],
            writable=True,
        )
    except urllib.error.URLError:
        assert "error" == "error"
    print('Internet: stock_image: OK')


# Generated at 2022-06-14 00:22:02.283223
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    # Stock image
    i = Internet()
    print(i.stock_image())

    # Writable stock image
    i = Internet()
    writable_image = i.stock_image(writable=True)
    assert isinstance(writable_image, bytes)

    # Stock image with keywords
    i = Internet()
    print(i.stock_image(keywords=['dog', 'cat']))

    # Stock image with keywords and writable
    i = Internet()
    writable_image = i.stock_image(keywords=['dog', 'cat'], writable=True)
    assert isinstance(writable_image, bytes)

# Generated at 2022-06-14 00:22:08.820190
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.data import STOCK_IMAGE_KEYWORDS, STOCK_IMAGE_SIZE
    provider = Internet('en')
    result = provider.stock_image(STOCK_IMAGE_SIZE[0],STOCK_IMAGE_SIZE[1],STOCK_IMAGE_KEYWORDS,writable=True)
    assert isinstance(result, bytes)

# Generated at 2022-06-14 00:22:10.308296
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Stock image test."""
    internet = Internet()
    assert isinstance(internet.stock_image(writable=True), bytes)

# Generated at 2022-06-14 00:22:12.380545
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test method of class Internet."""
    result = Internet().stock_image()
    from urllib.parse import urlparse
    path = urlparse(result).path
    assert path.startswith('/')


# Generated at 2022-06-14 00:22:24.571269
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import ImageSize, ImageSizeUnit
    from mimesis.providers.file import Image
    from mimesis.providers.media import Media
    internet = Internet()
    media = Media()
    image = Image()
    assert isinstance(internet.stock_image(), str)
    assert len(internet.stock_image()) > 40
    assert internet.stock_image(
        media.image_size(unit=ImageSizeUnit.PIXELS),
        media.image_size(unit=ImageSizeUnit.PIXELS),
    ) == internet.stock_image(
        width=media.image_size(unit=ImageSizeUnit.PIXELS),
        height=media.image_size(unit=ImageSizeUnit.PIXELS),
    )

# Generated at 2022-06-14 00:22:27.998232
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    test = Internet()
    assert isinstance(test.stock_image(), str)
    assert isinstance(test.stock_image(writable=True), bytes)

# Generated at 2022-06-14 00:22:29.891175
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    internet.stock_image()


# Generated at 2022-06-14 00:22:39.843917
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()

    # Test for method stock_image, where all parameters
    # have their default values
    link_1 = internet.stock_image()
    # Test for method stock_image, where all parameters
    # have random values
    link_2 = internet.stock_image(width=500, height=500,
                                  keywords=['random', 'sun'])
    assert isinstance(link_1, str) & isinstance(link_2, str)
    
if __name__ == '__main__':
    test_Internet_stock_image()