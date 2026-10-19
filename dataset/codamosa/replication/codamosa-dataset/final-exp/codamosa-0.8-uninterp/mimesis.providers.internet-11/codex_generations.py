

# Generated at 2022-06-14 00:20:43.524108
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    inet = Internet()
    url = inet.stock_image()

    print("stock_image: " + url)
    assert(url[0:32] == 'https://source.unsplash.com/') or (url == 'urlopen error')

# Generated at 2022-06-14 00:20:56.687969
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    from mimesis.enums import Hashtag
    from mimesis.exceptions import NonEnumerableError
    internet = Internet()
    # Default parameter
    tags_1 = internet.hashtags()
    assert tags_1 == '#' + internet.random.choice(HASHTAGS)

    # Non-default parameter
    tags_2 = internet.hashtags(quantity=3)
    assert tags_2 == ['#' + internet.random.choice(HASHTAGS)
                      for _ in range(3)]

    # Non-default wrong parameter
    try:
        internet.hashtags(quantity='1')
    except ValueError:
        pass

    assert internet.hashtags(quantity=1) == '#' + internet.random.choice(HASHTAGS)


# Generated at 2022-06-14 00:21:03.969552
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    print()
    internet = Internet(seed=42)
    result = internet.hashtags(quantity=2)
    assert result == ['#priorities', '#horizontal']
    assert result == internet.hashtags(quantity=2)

    result = internet.hashtags(quantity=1)
    assert result == '#priorities'
    assert result == internet.hashtags(quantity=1)

# Generated at 2022-06-14 00:21:14.804810
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    class TestInternet(Internet):
        def __init__(self):
            super().__init__('en', seed=42)

    test = TestInternet()

    url1 = test.stock_image()
    assert url1 == "https://source.unsplash.com/1920x1080"

    url2 = test.stock_image(keywords=["cat", "dog"])
    assert url2 == "https://source.unsplash.com/1920x1080?cat,dog"

    url3 = test.stock_image(width=1024, height=768)
    assert url3 == "https://source.unsplash.com/1024x768"

# Generated at 2022-06-14 00:21:16.560123
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    stock_image = Internet().stock_image(width=250, height=250)
    print(stock_image)


# Generated at 2022-06-14 00:21:18.266936
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    int = Internet(random=True)
    url = int.stock_image()
    assert (url.startswith("https://images.unsplash.com/photo-"))

# Generated at 2022-06-14 00:21:28.781534
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    from mimesis.enums import Hashtag
    provider = Internet()
    for i in range(10):
        hash_tags = provider.hashtags()
        assert isinstance(hash_tags, str)
        hash_tags = provider.hashtags(quantity=2)
        assert isinstance(hash_tags, list)
        assert isinstance(hash_tags[0], str)
        assert isinstance(hash_tags[1], str)
        hash_tags = provider.hashtags(quantity=3, category=Hashtag.ANIMALS)
        assert isinstance(hash_tags, list)
        assert isinstance(hash_tags[0], str)
        assert isinstance(hash_tags[1], str)
        assert isinstance(hash_tags[2], str)


# Generated at 2022-06-14 00:21:38.338298
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test case for method stock_image of class Internet."""
    from mimesis.builtins import Internet

    i = Internet()

    random_image = i.stock_image()
    assert isinstance(random_image, str) is True

    random_image = i.stock_image(writable=True)
    assert isinstance(random_image, bytes) is True

    random_image = i.stock_image(width=100, height=100)
    assert isinstance(random_image, str) is True

    random_image = i.stock_image(keywords=['test'] * 20)
    assert isinstance(random_image, str) is True

    random_image = i.stock_image(keywords=['test'] * 20, writable=True)
    assert isinstance(random_image, bytes) is True

# Generated at 2022-06-14 00:21:51.200706
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import PortRange, MimeType
    from mimesis.providers.internet import Internet
    internet = Internet()
    print(internet.stock_image()) # https://source.unsplash.com/1920x1080/?
    print(internet.stock_image(keywords=["girl"])) #https://source.unsplash.com/1920x1080/?girl
    print(internet.stock_image(writable=True)) # b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00\t\x06\x07\x1...

# Generated at 2022-06-14 00:21:57.918624
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test for method stock_image of class Internet."""
    from mimesis.enums import ImageWidth, ImageHeight

    internet = Internet()
    image = internet.stock_image(width=ImageWidth.WIDTH_1920,
                                 height=ImageHeight.HEIGHT_1080)
    assert isinstance(image, str) and image.startswith('https://source.unsplash.com/1920x1080')

# Generated at 2022-06-14 00:22:12.892562
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    print(internet.stock_image(1920, 1080, ['dog', 'cat']))
    # print(internet.stock_image(3000, 3000))  # <- return 400
    print(internet.stock_image(100, 100))
    print(internet.stock_image(50, 50))
    print(internet.stock_image(300, 300))
    print(internet.stock_image(500, 500))
    print(internet.stock_image(1024, 768))
    print(internet.stock_image(1600, 900))
    print(internet.stock_image(1920, 1080))
    print('*'*50)
    print(internet.stock_image(writable=True))
    print(internet.stock_image())

# Generated at 2022-06-14 00:22:16.460991
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    # Test stock_image() in the Internet with HTTP connection
    try:
        Internet().stock_image()
    except urllib.error.URLError as e:
        print(e)

# Generated at 2022-06-14 00:22:22.548652
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Generate a link to the random stock image."""
    # Code from https://source.unsplash.com/
    i = Internet(seed=0)
    link = i.stock_image(800, 600)
    assert link == 'https://source.unsplash.com/800x600'

# Generated at 2022-06-14 00:22:26.943900
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test for method stock_image.

    :return: None
    """
    assert len(Internet().stock_image()) > 0

# Generated at 2022-06-14 00:22:31.590183
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    stock_image = internet.stock_image()
    print(stock_image)

if __name__ == "__main__":
    test_Internet_stock_image()

# Generated at 2022-06-14 00:22:36.072845
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test method stock_image of class Internet."""
    stock_image = Internet.stock_image()
    assert isinstance(stock_image, str)
    assert 'https://source.unsplash' in stock_image
    assert 'jpg' in stock_image

# Generated at 2022-06-14 00:22:43.181548
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    internet = Internet('ru')
    # Not writable
    a = internet.stock_image(1920, 1080, ['big', 'mountains'])
    print(a)
    # Writable
    b = internet.stock_image(1920, 1080, ['big', 'mountains'], writable=True)
    print(b)



# Generated at 2022-06-14 00:22:50.418484
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet."""
    from mimesis import Internet
    import datetime
    url = Internet("ru").stock_image()
    from PIL import Image
    from io import BytesIO

    try:
        image_object = Image.open(BytesIO(url))
        width, height = image_object.size
        print(datetime.datetime.now(), url, width, height)
    except:
        pass

# Generated at 2022-06-14 00:22:55.049831
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    Internet_ = Internet()
    result = Internet_.stock_image()
    print(result)

# Generated at 2022-06-14 00:23:03.625241
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    import os
    import requests
    import shutil
    import tempfile

    imagepath = '/tmp/unsplash.jpg'
    r = requests.get(
        'https://source.unsplash.com/200x200/?nature',
        stream=True
    )

    with open(imagepath, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

    internet = Internet()
    path = internet.stock_image(writable=True)
    with open(imagepath, 'wb') as f:
        f.write(path)

    os.remove(imagepath)

# Generated at 2022-06-14 00:23:19.014542
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet."""
    from PIL import Image

    provider = Internet()
    data = provider.stock_image(writable=True)

    image = Image.open(io.BytesIO(data))
    assert isinstance(data, bytes)
    assert image.format == 'JPEG'

# Generated at 2022-06-14 00:23:24.807134
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet."""
    internet = Internet()
    url = internet.stock_image(20, 20)
    assert url

# Generated at 2022-06-14 00:23:28.774047
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    stock_image = Internet().stock_image()
    assert isinstance(stock_image, str) and stock_image.startswith(r'http://') and stock_image.endswith(r'.jpg?')

# Generated at 2022-06-14 00:23:32.217722
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    test_class = Internet()
    res = test_class.stock_image(200, 200, ['animals', 'pets'], True)
    assert isinstance(res, bytes)

# Generated at 2022-06-14 00:23:33.960148
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    image = internet.stock_image(1920, 1080)
    print(image)


# Generated at 2022-06-14 00:23:39.099705
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    stock_image = internet.stock_image()
    print(stock_image)
    assert stock_image.startswith('https://')

# Generated at 2022-06-14 00:23:42.778387
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    obj = Internet(seed=123)
    result = obj.stock_image(
        width=800,
        height=640,
        writable=True
    )

    assert(type(result) == bytes)

# Generated at 2022-06-14 00:23:45.830397
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet()
    internet.stock_image(writable=True)

# Generated at 2022-06-14 00:23:58.703807
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.enums import MimeType
    from mimesis.providers.file import File
    from mimesis.providers.generic import Generic

    assert len(Internet(seed=1).stock_image(
        writable=True,
        width=640,
        height=480,
    )) > 0

    png_image = Internet(
        seed=2,
    ).stock_image(
        keywords=['beach', 'sea', 'sunset'],
        writable=True,
        width=640,
        height=480,
    )
    assert File(
        seed=2,
    ).mime_type(
        type_=MimeType.IMAGE,
        writable=True,
        data=png_image,
    ) == MimeType.PNG


# Generated at 2022-06-14 00:24:00.973466
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test method Internet"""
    internet = Internet()
    print(internet.stock_image(keywords=["mimesis"]))

# Generated at 2022-06-14 00:24:34.414457
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """
    以下测试用例是 基于rspec(https://rspec.info/) 的Python实现
    全局安装： pip install rspec
    运行： rspec filename.py
    """
    import rspec

    result = Internet().stock_image()
    assert type(result) == str
    with rspec.Expectation("Should not raise an Exception"):
        assert Internet().stock_image(writable=True)


test_Internet_stock_image()

# Generated at 2022-06-14 00:24:38.273062
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    image = provider.stock_image()
    assert image.startswith('http')

# Generated at 2022-06-14 00:24:39.837313
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    stock_image(width,height,keywords,writable)

# Generated at 2022-06-14 00:24:46.285647
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    internet = Internet()
    res = internet.stock_image(width=100, height=100, writable=False)
    assert res.split('/')[2].split('.')[1] == 'unsplash'

    images = internet.stock_image(width=100, height=100, writable=True)
    assert images.split(b'/')[2].split(b'.')[1] == b'unsplash'

# Generated at 2022-06-14 00:24:48.160238
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    it = Internet()
    image = it.stock_image(width=3, height=3)
    assert isinstance(image, str)


# Generated at 2022-06-14 00:24:54.269122
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test of method stock_image."""
    internet = Internet()
    result1 = internet.stock_image()
    assert isinstance(result1, str)
    result2 = internet.stock_image(writable=True)
    assert isinstance(result2, bytes)

# Generated at 2022-06-14 00:24:59.400615
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test method Internet.stock_image() return URL."""
    provider = Internet()

    url = provider.stock_image(200, 200, ['cat', 'dog'])
    assert isinstance(url, str)
    assert url.startswith('https:')
    assert url.endswith('.jpg')

    # Writable mode is not tested
    # Should be tested with pytest

# Generated at 2022-06-14 00:25:04.543271
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.data import CODES
    from mimesis.enums import Language
    from mimesis.providers.internet import Internet

    def get_response(url):
        import io
        import urllib.request
        return io.BytesIO(urllib.request.urlopen(url).read())

    internet = Internet(Language.EN)
    url = internet.stock_image(keywords=["america", "brazil", "city"])
    assert len(get_response(url).read()) > 0

# Generated at 2022-06-14 00:25:10.277398
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    seed = '9a8d0e4f2a73893f76cc0f0c44817983'
    stock_image_url = 'https://source.unsplash.com/1920x1080?hello'
    internet = Internet(seed=seed)
    assert internet.stock_image() == stock_image_url

# Generated at 2022-06-14 00:25:14.302815
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.enums import ImageSize

    INTERNET = Internet()
    URL = INTERNET.stock_image(ImageSize.XLARGE)
    assert URL

