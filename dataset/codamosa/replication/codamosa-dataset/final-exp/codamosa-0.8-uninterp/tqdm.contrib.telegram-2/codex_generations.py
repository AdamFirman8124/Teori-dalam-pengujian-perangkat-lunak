

# Generated at 2022-06-14 13:31:56.013455
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .test_tqdm import pretest_tqdm_clear
    return pretest_tqdm_clear(tqdm_telegram)


# Generated at 2022-06-14 13:32:02.943004
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .utils import _io
    from .utils_import import _import_tty
    tty = _import_tty()
    io = _io.StringIO()


# Generated at 2022-06-14 13:32:10.328522
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """
    This function checks if the close function of tqdm_telegram
    is working properly, deleting the message after use.
    """
    from time import sleep
    import requests
    import sys

    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')

    test_name = "Unit test for method close of class tqdm_telegram"
    test_description = "This function checks if the close function of \
tqdm_telegram is working properly, deleting the message after use."
    test_update = "tqdm-telegram: " + test_name
    session = Session()


# Generated at 2022-06-14 13:32:17.187344
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    # Initialize object `tqdm` with values `total=1` and `enable_telegram=False`
    tqdm_test = tqdm_telegram(total=1, enable_telegram=False)

    # Check attributes `_miniters` and `_n`
    assert tqdm_test._miniters == 1
    assert tqdm_test._n == 0

    # Update attribute `_n`
    tqdm_test._n = 1

    # Call method `clear`
    tqdm_test.clear()

    # Check attribute `_n`
    assert tqdm_test._n == 0

# Generated at 2022-06-14 13:32:22.935541
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = '748994212:AAHr_X2qFq3DnMvBhxJbR-GWpfaJPhEOR1E'
    chat_id = '-234258409'
    tg = TelegramIO(token, chat_id)
    tg.write("hello")
    assert tg.text == "hello"
    tg.delete()
    assert tg.text == "hello"
    tg = TelegramIO(token, chat_id)
    tg.write("hello")
    assert tg.text == "hello"



# Generated at 2022-06-14 13:32:28.029168
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    io = TelegramIO('', '')
    io.write('')
    io.write('xxx')
    io.write('xxx')
    io.write('xxx')
    io.write('xxx')
    io.write('xxx')
    io.write('xxx')

# Generated at 2022-06-14 13:32:35.264766
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    try:
        import pytest
    except ImportError:
        return
    from unittest import mock

    with mock.patch.object(TelegramIO, 'write') as wr:
        with tqdm(range(5), token='{token}', chat_id='{chat_id}') as t:
            for _ in t:
                t.clear()

        assert wr.call_count == 1

# Generated at 2022-06-14 13:32:40.439858
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """Unit test for method `tqdm.contrib.telegram.tqdm_telegram.display`"""
    t = tqdm_telegram(total=10)
    t.display()
    t.n = 3
    t.display()
    t.n = 5
    t.display()
    t.clear()
    t.close()

# Generated at 2022-06-14 13:32:46.183145
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    """Unit test for method `write` of class `TelegramIO`."""
    tgio = TelegramIO('blabla', 'blabla')
    assert tgio.text == 'TelegramIO'
    assert tgio.write('  ') == None
    assert tgio.text == '...'
    assert tgio.write('foo') == None
    assert tgio.text == 'foo'
    assert tgio.write('bar') == None
    assert tgio.text == 'bar'
    assert tgio.write('  ') == None
    assert tgio.text == '...'

# Generated at 2022-06-14 13:32:49.233483
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from time import sleep
    tqdm_telegram(total=10, position=3).write("")
    for i in tqdm_telegram(range(4), total=4, desc="test"):
        sleep(1)

# Generated at 2022-06-14 13:37:35.609239
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    try:
        tg = TelegramIO(
            getenv('TQDM_TELEGRAM_TOKEN'),
            getenv('TQDM_TELEGRAM_CHAT_ID'))
        tg.write('hello')
    except Exception as e:
        tqdm_auto.write(str(e))


if __name__ == '__main__':
    test_TelegramIO_write()