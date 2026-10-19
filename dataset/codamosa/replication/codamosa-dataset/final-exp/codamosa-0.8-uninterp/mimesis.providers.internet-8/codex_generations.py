

# Generated at 2022-06-14 00:21:04.856543
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    image = provider.stock_image()
    assert image.startswith('https://')
    assert image.endswith('.jpg')



# Generated at 2022-06-14 00:21:08.197903
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    internet = Internet()
    assert internet.stock_image()

# Generated at 2022-06-14 00:21:10.957436
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    internet = Internet(seed=6)
    url = internet.stock_image()
    assert url == 'https://source.unsplash.com/1920x1080?wall,planet'

# Generated at 2022-06-14 00:21:20.257116
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    from mimesis.constants import BASE_PATH

    net = Internet()

    # Get image as a link
    link = net.stock_image(width=100, height=100)
    assert isinstance(link, str) and isinstance(link, str)

    # Get image as a bytes
    image = net.stock_image(width=100, height=100, writable=True)
    assert isinstance(image, bytes)

    # Save the image to file
    with open(BASE_PATH + '/mimesis/providers/internet/test_image.jpg', 'wb') as f:
        f.write(image)

# Generated at 2022-06-14 00:21:30.810194
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Test Internet stock_image method."""
    internet = Internet()
    width = 1920
    height = 1080
    keywords = ['river', 'house', 'cemetery']
    result = internet.stock_image(
        width=width,
        height=height,
        keywords=keywords,
    )
    assert isinstance(result, str)

    result = internet.stock_image(
        width=width,
        height=height,
        keywords=keywords,
        writable=True,
    )
    assert isinstance(result, bytes)

# Generated at 2022-06-14 00:21:37.855406
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    from mimesis.enums import Hashtag

    hashtags = ['#love']

    # Unit test for method hashtags of class Internet
    assert hashtags == Internet().hashtags(1)
    assert ['#love', '#sky', '#nice'] == Internet().hashtags()

    # Unit test for method hashtags of class Internet
    assert ['#books', '#book'] == Internet().hashtags(2, Hashtag.BOOKS)

# Generated at 2022-06-14 00:21:46.197306
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    print('Internet.stock_image')
    print(Internet().stock_image())
    print(Internet().stock_image(keywords=['funny']))
    print(Internet().stock_image(keywords=['mountain'], width=1920))
    print(Internet().stock_image(keywords=['trees', 'flowers'], height=1080))

# Generated at 2022-06-14 00:21:49.711361
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    intnet = Internet()

    res = intnet.hashtags(quantity=4)
    assert len(res) == 4

    res = intnet.hashtags()
    assert isinstance(res, str)


# Generated at 2022-06-14 00:21:56.166020
# Unit test for method hashtags of class Internet
def test_Internet_hashtags():
    """Test for Internet.hashtags()"""
    inter = Internet()
    hash_list = inter.hashtags(4)
    for i in hash_list:
        assert isinstance(i, str)
        assert i[0] == '#'

    hash_list = inter.hashtags(1)
    assert isinstance(hash_list, str)
    assert hash_list[0] == '#'

# Generated at 2022-06-14 00:22:02.384499
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    # Writable object test
    internet = Internet(seed=123)

    assert b'JFIF' in internet.stock_image(writable=True)
    # String test
    assert 'https://source.unsplash.com/1920x1080?python' in internet.stock_image()