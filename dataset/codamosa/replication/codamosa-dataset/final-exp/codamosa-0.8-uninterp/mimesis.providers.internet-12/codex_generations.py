

# Generated at 2022-06-14 00:21:01.221131
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    assert Internet().stock_image() == 'https://source.unsplash.com/1920x1080?'

# Generated at 2022-06-14 00:21:10.933892
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.providers.internet import Internet
    internet = Internet()
    image = internet.stock_image(
        width=1920,
        height=1080,
        keywords=['python', 'mimesis'],
        writable=False
    )
    assert image.startswith('https://source.unsplash.com/1920x1080?')
    image = internet.stock_image(
        width=1920,
        height=1080,
        keywords=['python', 'mimesis'],
        writable=True
    )
    assert isinstance(image, bytes)

# Generated at 2022-06-14 00:21:13.365160
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    provider = Internet()
    image = provider.stock_image(writable=True)
    assert(isinstance(image, bytes))

# Generated at 2022-06-14 00:21:18.679376
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet."""
    from mimesis.exceptions import NonEnumerableError

    internet = Internet()
    internet.stock_image(writable=True)

# Generated at 2022-06-14 00:21:20.663266
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    assert isinstance(Internet.stock_image(), str)

# Generated at 2022-06-14 00:21:30.539025
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    from mimesis.builtins import Internet
    import time

    internet = Internet('en')
    # stock_image will return link to the image

    print(internet.stock_image(height=1080,width=1920,keywords=['парк']))
    time.sleep(3)
    # But if you pass True for keyword writable,
    # stock_image will return the image as bytes
    # This can be useful if you want to write the image to a file

    print(type(internet.stock_image(900,1200,writable=True)))

# Generated at 2022-06-14 00:21:36.932236
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """
    Юнит-тест на функцию stock_image класса Internet.
    """
    image = Internet.stock_image()
    assert image == 'https://source.unsplash.com/1920x1080?', "Ошибка работы функции"
    return True


if __name__ == '__main__':
    test_Internet_stock_image()

# Generated at 2022-06-14 00:21:49.811301
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """Unit test for method stock_image of class Internet"""
    # result = Internet().stock_image()
    # print(result)
    # assert isinstance(result, str)
    # assert result == 'http://unsplash.it/1920/1080/?random'
    # result = Internet().stock_image(keywords=['city', 'landscape'])
    # print(result)
    # assert isinstance(result, str)
    # assert result == 'http://unsplash.it/1920/1080/?city,landscape'
    # result = Internet().stock_image(keywords=['city', 'landscape'],
    # writable=True)
    # print(result)
    # assert isinstance(result, bytes)
    print(Internet().stock_image(keywords=['city', 'landscape']))

# Generated at 2022-06-14 00:22:01.169576
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    """# Unit test for method stock_image of class Internet"""
    # Generate URL, writable=False
    stock_image_URL = Internet.stock_image()
    print(stock_image_URL)

    # Generate URL, writable=True
    stock_image_bytes = Internet.stock_image(writable=True)
    print(type(stock_image_bytes))

    # Generate URL, set keyword list
    stock_image_keywords = Internet.stock_image(
        keywords=['switzerland', 'nature', 'lake']
    )
    print(stock_image_keywords)

    # Generate URL, set key word list and writable=True

# Generated at 2022-06-14 00:22:06.853701
# Unit test for method stock_image of class Internet
def test_Internet_stock_image():
    import requests
    import os

    _path = "../../testimg.jpg"
    jpg = Internet().stock_image(writable=True)
    if os.path.exists(_path):
        os.remove(_path)

    with open(_path, 'wb') as f:
        f.write(jpg)

    assert os.path.getsize(_path) == requests.head(_path).headers['content-length']
    os.remove(_path)