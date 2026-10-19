

# Generated at 2022-06-14 13:30:40.343201
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    io = TelegramIO('b', 'c')
    io.write('e')

# Generated at 2022-06-14 13:30:43.400734
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .utils_test import tqdm_telegram_display
    tqdm_telegram_display(tqdm_telegram)

# Generated at 2022-06-14 13:30:53.671020
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    """
    Unit test for constructor of class tqdm_telegram
    """
    from tqdm._utils import _term_move_up as u

# Generated at 2022-06-14 13:31:00.252750
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import time
    import nose
    import nose.tools  # type: ignore

    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')

    if not (token and chat_id):
        warn("TQDM_TELEGRAM_TOKEN & TQDM_TELEGRAM_CHAT_ID env vars are required")
        return

    stats = []

    def on_result(fut, result):
        stats.append(result['error_code'])

    t = tqdm_telegram(total=100, token=token, chat_id=chat_id)

    t.tgio.on_result = on_result

    for _ in range(20):
        time.sleep(0.1)
       

# Generated at 2022-06-14 13:31:08.487551
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    import os
    import requests

    if os.environ.get('CI'):
        return  # skip for testing

    tg_token = os.environ.get('TQDM_TELEGRAM_TOKEN')
    tg_chat_id = os.environ.get('TQDM_TELEGRAM_CHAT_ID')
    if not (tg_token and tg_chat_id):
        from getpass import getpass
        tg_token = getpass("Telegram token: ")
        tg_chat_id = getpass("Telegram chat ID: ")

    s = "hello"
    tgio = TelegramIO(tg_token, tg_chat_id)
    # Test write
    tgio.write(s)
    # Test delete
    tgio.delete()
    # Test request

# Generated at 2022-06-14 13:31:17.751099
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    assert tqdm_telegram(total=42).close() is None
    assert tqdm_telegram(total=42, leave=True).close() is None
    assert tqdm_telegram(total=0, leave=None).close() is None
    assert tqdm_telegram(total=0, leave=False).close() is None
    assert tqdm_telegram(total=1, leave=None).close() is None
    assert tqdm_telegram(total=1, leave=-1).close() is None
    assert tqdm_telegram(total=0, leave=-1).close() is None

# Generated at 2022-06-14 13:31:28.514016
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    from tqdm.contrib.telegram import tqdm_telegram
    from nose.tools import assert_true
    from requests import post
    from os import environ
    from os.path import isfile
    import json

    # Upload to test bot with `TQDM_TELEGRAM_TOKEN`
    chat_id = environ['TQDM_TELEGRAM_CHAT_ID']
    token = environ['TQDM_TELEGRAM_TOKEN']

    # Send a message
    assert_true(post(
        'https://api.telegram.org/bot%s/sendMessage' % token,
        data={'text': '$tqdm-telegram-close-test', 'chat_id': chat_id}
    ).json()['ok'])
    # Check it exists
    res

# Generated at 2022-06-14 13:31:33.359063
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv("TQDM_TELEGRAM_CHAT_ID")
    if token is None or chat_id is None:
        return
    tgio = TelegramIO(token, chat_id)
    tgio.write("tqdm is an amazing tool")
    tgio.delete()

# Generated at 2022-06-14 13:31:35.012752
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm(total=100, disable=True)
    assert not t.disable
    t.close()
    assert t.disable

# Generated at 2022-06-14 13:31:45.294599
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """Test close method of class tqdm_telegram"""

    tgr = tqdm_telegram(disable=True)
    tgr.disable = False
    tgr.leave = False
    tgr.tgio = TelegramIO('a', 'b')
    tgr.close()
    assert tgr.pos == 0

    tgr = tqdm_telegram(disable=False)
    tgr.tgio = TelegramIO('a', 'b')
    tgr.close()
    assert tgr.pos == 0
    assert tgr.leave == False

    tgr.leave = True
    tgr.close()
    assert tgr.pos == 0
    assert tgr.disable == True

# Generated at 2022-06-14 13:33:32.848919
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    import pytest
    from .utils import suppress_stdout_stderr

    with suppress_stdout_stderr():
        io = TelegramIO(token='', chat_id='')
        io.submit(io.write, s='test')

        io.submit(io.delete)
        io.close()
        io.__exit__()

        with pytest.raises(Exception):
            io.submit(io.delete)

# Generated at 2022-06-14 13:33:34.972201
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    for i in tqdm_telegram(range(4)):
        if i == 2:
            break
        print(i)

# Generated at 2022-06-14 13:33:43.907150
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    test_token = 'test_token'
    test_chat_id = 'test_chat_id'
    test_s = 'test_s'
    test_message_id = 123456789

    tgio = TelegramIO(test_token, test_chat_id)
    assert tgio.message_id is None

    import requests_mock
    with requests_mock.Mocker() as m:
        m.post(TelegramIO.API + '{}/sendMessage'.format(test_token),
               json={'result': {'message_id': test_message_id},
                     'ok': True},
               status_code=200)
        tgio.message_id
        assert tgio.message_id == test_message_id

    with requests_mock.Mocker() as m:
        m.post

# Generated at 2022-06-14 13:33:50.518009
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import io
    import sys

    f = io.StringIO()
    t = tqdm_telegram(total=2, file=f, disable=True)
    t.update()
    t.clear(nolock=False)
    t.close()
    assert " 0%|" in f.getvalue()
    assert " 50%|" not in f.getvalue()
    assert "100%|" not in f.getvalue()

    if hasattr(sys.stdout, 'fileno'):
        t.close()
        return
    f = io.StringIO()
    t = tqdm_telegram(total=2, file=f, disable=True)
    t.update()
    t.clear(nolock=True)
    t.close()

# Generated at 2022-06-14 13:33:59.957642
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from tqdm.auto import tqdm

    t = tqdm(total=100, disable=True)
    t.display(0)
    assert t.format_dict == {
        'bar_format': '{l_bar}{bar}{r_bar}',
        'n': 1,
        'l_bar': '',
        'r_bar': '',
        'bar': '',
    }
    t.format_dict.update(bar_format='{l_bar}{bar}{r_bar}')
    t.display(50)
    assert t.format_dict == {
        'bar_format': '{l_bar}{bar}{r_bar}',
        'n': 50,
        'l_bar': '',
        'bar': '',
        'r_bar': '',
    }

# Generated at 2022-06-14 13:34:05.770833
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """Test tqdm_telegram.display"""
    t = tqdm_telegram(range(3), bar_format="{desc} {bar}")
    for i, j in enumerate(t):
        t.set_description("desc:%d" % i)
        t.update()
    assert True


# Generated at 2022-06-14 13:34:10.006376
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    """
    Tests that the method "write" of class TelegramIO
    """
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    to = TelegramIO(token, chat_id)
    assert to.write("testing") != None

# Generated at 2022-06-14 13:34:14.843254
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    import sys
    try:
        tio = TelegramIO('token', 'chat_id')
    except:
        sys.exit(0)

    try:
        tio.write('')
        tio.write('1')
    except:
        tio.delete()
        sys.exit(1)

    tio.delete()
    sys.exit(0)


if __name__ == '__main__':
    test_TelegramIO_write()

# Generated at 2022-06-14 13:34:19.837773
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    t = tqdm_telegram(chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'),
                      token=getenv('TQDM_TELEGRAM_TOKEN'))
    t.write(" ")
    t.write("hello")
    t.write("world")
    t.close()

# Generated at 2022-06-14 13:34:27.642319
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from io import StringIO
    from shutil import rmtree
    from os import mkdir
    from tempfile import gettempdir
    from tqdm import tqdm
    from tqdm._utils import _term_move_up
    from tqdm.contrib.telegram import tqdm_telegram

    str_io = StringIO()
    with tqdm_telegram(total=9, file=str_io) as pbar:
        assert pbar.n == 0
        assert pbar.last_print_n == 0
        pbar.update(5)
        assert pbar.n == 5
        assert pbar.last_print_n == 5
        pbar.clear()
        assert pbar.n == 5
        assert pbar.last_print_n == 5
        pbar.update(3)

# Generated at 2022-06-14 13:37:47.315238
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    """
    Unit test for method write of class TelegramIO.
    """
    # Token and chat_id for unit tests
    token = '1189089066:AAFgR0zZtsfeliz61JXGgK_bv-RAyE1cEEI'
    chat_id = '-1001150750555'
    message_id = [11]
    # Test class
    class TestTelegramIO(TelegramIO):
        """
        Class for unit tests.
        """
        def __init__(self, token, chat_id):
            """
            Class initialization.
            """
            super(TestTelegramIO, self).__init__(token, chat_id)

    # Test class init
    telegram_io = TestTelegramIO(token, chat_id)
    telegram_io.write