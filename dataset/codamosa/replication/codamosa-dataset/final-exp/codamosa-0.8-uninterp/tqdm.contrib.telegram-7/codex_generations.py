

# Generated at 2022-06-14 13:30:05.541993
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    """ Test tqdm_telegram.clear(). """
    from io import StringIO
    from time import sleep
    from tqdm import tqdm_telegram

    tqdm_auto.write = lambda *args, **kwargs: None

    fobj = StringIO()
    tqdm_auto.monitor_interval = 0  # prevent any updates
    with tqdm_telegram(total=100, file=fobj, miniters=0, mininterval=0,
                       disable=False, token='token', chat_id='chat_id') as t:
        t.update(1)
        sleep(0.01)
        self.assertEqual(fobj.getvalue().count('\r'), 1)
        t.clear(nolock=True)
        sleep(0.01)

# Generated at 2022-06-14 13:30:08.367392
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = '11111'
    chat_id = '1'

    message_ = TelegramIO(token, chat_id)
    assert message_.message_id

    message_.delete()
    assert message_.message_id is None

# Generated at 2022-06-14 13:30:12.133931
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    # Test case: leave=True
    t = tqdm_telegram(total=100, leave=True)
    t.close()
    assert (t.leave == True)

    # Test case: leave=False
    t = tqdm_telegram(total=100, leave=False)
    t.close()
    assert (t.leave == False)

    # Test case: leave=None
    t = tqdm_telegram(total=100, leave=None)
    position_before_close = t.pos
    t.close()
    assert (t.leave == None)
    assert (t.pos == position_before_close)

# Generated at 2022-06-14 13:30:18.932208
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    class Dummy:
        pass

    dummy = Dummy()
    dummy.tgio = TelegramIO("token", "chat_id")

    assert dummy.tgio.tgio.write("") is None
    assert dummy.tgio.tgio.text == 'TelegramIO'
    assert dummy.tgio.tgio.write("a") is None
    assert dummy.tgio.tgio.text == 'a'
    assert dummy.tgio.tgio.write("a") is None
    assert dummy.tgio.tgio.text == 'a'
    assert dummy.tgio.tgio.delete() is not None
    assert dummy.tgio.tgio.write("") is not None

# Generated at 2022-06-14 13:30:23.072933
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    tg = TelegramIO(token = '00000:00000', chat_id = '00000')
    # Since a message id is not assigned to tg,
    # this call to delete must not raise an exception.
    tg.delete()

# Generated at 2022-06-14 13:30:27.951304
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    import logging
    tqdm_auto.write('TelegramIO.delete() test:')
    ln = logging.getLogger("requests.packages.urllib3.connectionpool")
    ln.setLevel(logging.WARNING)
    tg = TelegramIO('token', 'chat_id')
    tg.delete()
    tg.close()

# Generated at 2022-06-14 13:30:35.518796
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    from os import environ as env
    from os import name as os_name
    from os import remove as os_remove
    from os import system as os_system
    from os import devnull as os_devnull
    from os.path import isfile as os_isfile
    from requests import Session

    # skip if OS is windows
    if os_name == 'nt':
        return

    # test TelegramIO method write
    def test_telegram_io():
        session = Session()
        tok = result = None
        with open('test_telegram_io.token', 'r') as f:
            tok = f.read()
            f.close()
        with open('test_telegram_io.result', 'r') as f:
            result = f.read()
            f.close()
        resp = session.post

# Generated at 2022-06-14 13:30:43.519231
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    from multiprocessing.pool import ThreadPool
    from requests.adapters import HTTPAdapter, DEFAULT_POOLSIZE
    from requests.packages.urllib3.util.retry import Retry

    class Dummy(object):
        def __init__(self, *args, **kwargs):
            self.__dict__.update(kwargs)

        def post(self, *args, **kwargs):
            return self

        def json(self):
            return self

        def close(self):
            raise Exception("Should not be called")

    token, chat_id = '123456789:ABCDEFG_hijklmnopqrstuvwxyz', '123456789'

    tgio = TelegramIO(token, chat_id)


# Generated at 2022-06-14 13:30:48.709226
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    token = "822104095:AAHdnBnKjWmMN8-vklMPu5X6gcG7Vu3W6U0"
    chat_id = "722236742"
    io = TelegramIO(token, chat_id)
    io.write("Testing TelegramIO")


# Generated at 2022-06-14 13:30:53.618794
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    import sys
    if sys.version_info[:2] < (3, 5):
        return
    from unittest import TestCase, main

    class TelegramIOTest(TestCase):
        def test_delete(self):
            tgio = TelegramIO('{token}', '{chat_id}')
            tgio.submit(tgio.delete)
            tgio.close()

    main()

# Generated at 2022-06-14 13:32:52.782049
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    class TelegramIO_test(TelegramIO):
        def submit(self, func, *args, **kwargs):
            return func(*args, **kwargs)

    test_token = '1234567890:abcdefghijklmnopqrstuvwxyz'
    test_chat_id = '9876543210'
    test_io = TelegramIO_test(test_token, test_chat_id)
    assert test_io.write('Test').json()['result']['message_id'] == \
        test_io.message_id
    test_io.write('Test 2')

# Generated at 2022-06-14 13:32:55.865928
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    t = tqdm_telegram(None, bar_format='|{bar}|', leave=False,
                      token='{token}', chat_id='{chat_id}')
    t.update()
    t.clear()
    t.close()


# Generated at 2022-06-14 13:33:04.997007
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import sys
    from .utils_test import with_recursion_limit
    from .utils_test import unmodified_tqdm

    # Check if the bar does not disappear when is called twice
    # the method clear.
    def _test_clear():
        with with_recursion_limit(5000):
            # Get tqdm object from tqdm.auto
            with unmodified_tqdm(
                    bar_format='{l_bar}{bar}|', leave=True, disable=False,
                    file=sys.stdout, token=getenv('TQDM_TELEGRAM_TOKEN'),
                    chat_id=getenv('TQDM_TELEGRAM_CHAT_ID')) as t:
                t.update(10)
                t.update(10)
                t.clear()
                t.clear()

# Generated at 2022-06-14 13:33:11.443510
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    tgio = TelegramIO(token="", chat_id="")
    tgio.write("hello world!")
    tgio.submit(tgio.session.post, tgio.API + '%s/editMessageText' % tgio.token,
                data={'text': '`' + "hello world!" + '`', 'chat_id': tgio.chat_id,
                      'message_id': tgio.message_id, 'parse_mode': 'MarkdownV2'}).result()
    tgio.delete()

# Generated at 2022-06-14 13:33:15.149816
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = '{token}'
    chat_id = '{chat_id}'
    tgio = TelegramIO(token, chat_id)
    tgio.write('Hello World')
    tgio.delete()
    tgio.close()

# Generated at 2022-06-14 13:33:24.416338
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import os
    import requests

    # invalid token, chat_id pair
    try:
        tte = tqdm_telegram(token="invalid_token", chat_id="invalid_chat_id")
        tte.display()
        tte.close()
        assert False
    except requests.exceptions.ConnectionError:
        pass

    # valid token, chat_id pair
    token = os.environ.get('TQDM_TELEGRAM_TOKEN', 'invalid_token')
    chat_id = os.environ.get('TQDM_TELEGRAM_CHAT_ID', 'invalid_chat_id')
    if (token == 'invalid_token') | (chat_id == 'invalid_chat_id'):
        print("tqdm Telegram tests skipped.")
        return

   

# Generated at 2022-06-14 13:33:33.594166
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    import time
    import unittest
    class TestTelegramIO_write(unittest.TestCase):
        def setUp(self):
            self.token = '123456789:this_is_a_fake_token'
            self.chat_id = '123456789'
            self.tgio = TelegramIO(self.token, self.chat_id)
            self.assertTrue(self.tgio.message_id)
            self.assertIs(self.tgio.write('TEST'), None)
            time.sleep(1)  # because the bot is slow...
        def test_TelegramIO_write(self):
            self.assertIs(self.tgio.write('TEST'), None)
        def tearDown(self):
            self.tgio.delete()
    unittest.main()

# Generated at 2022-06-14 13:33:36.541872
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    from os import getenv
    t = TelegramIO(getenv('TQDM_TELEGRAM_TOKEN'),
                   getenv('TQDM_TELEGRAM_CHAT_ID'))
    t.message_id
    t.delete()

# Generated at 2022-06-14 13:33:41.515784
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    tgio = TelegramIO('token', 'chat_id')
    import requests
    check = {'json': lambda *_, **__:
             {'result': {'message_id': tgio.message_id}},
             'raise_for_status': lambda *_, **__: None
             }
    requests.post = lambda *_, **__: check
    tgio.delete()

# Generated at 2022-06-14 13:33:45.780776
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    try:
        tgio = TelegramIO('123', '456')
    except Exception as e:
        assert isinstance(e, AttributeError)
    else:
        tgio.write('test')
        assert tgio.message_id == None
    tgio = TelegramIO('123123', '456456')
    tgio.write('test')
    assert tgio.message_id > 0

# Generated at 2022-06-14 13:37:28.974301
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """Unit test for method display of class tqdm_telegram."""
    #
    # NOTE: this entire test is not meant to run.
    #
    import os

    # suppress missing environment variable warning
    try:
        del os.environ['TQDM_TELEGRAM_TOKEN']
        del os.environ['TQDM_TELEGRAM_CHAT_ID']
    except KeyError:
        pass

    import tqdm
    import requests

    assert tqdm.__version__ == '4.42.0'

    # create a chat and a bot
    # get token and chat_id
    # send bot a message such as `/start`

    token=os.environ['TQDM_TELEGRAM_TOKEN']

# Generated at 2022-06-14 13:37:30.221598
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    io = TelegramIO("TOKEN", "CHAT_ID")
    io.write("test")

# Generated at 2022-06-14 13:37:36.672611
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    if not getenv('TQDM_TELEGRAM_CHAT_ID') or not getenv('TQDM_TELEGRAM_TOKEN'):
        warn('$TQDM_TELEGRAM_CHAT_ID or $TQDM_TELEGRAM_TOKEN not set. '
             'Cannot run `test_tqdm_telegram_close`.', TqdmWarning)
        return
    tqdm_telegram(range(3)).close()

# Generated at 2022-06-14 13:37:47.463058
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    """Test if message sent to Telegram is correct"""
    from time import time
    from threading import Thread
    import tqdm.contrib.telegram as telegram
    token = 'token'
    chat_id = 'chat_id'

    def tqdm_factory(iterable, **kwargs):
        kwargs = kwargs.copy()
        token = kwargs.pop('token', None)
        chat_id = kwargs.pop('chat_id', None)
        # Use tqdm_telegram instead of tqdm to replace the file-like object
        # with a TelegramIO object
        return telegram.tqdm_telegram(iterable, token=token, chat_id=chat_id,
                                      **kwargs)

    N = 10000  # Number of rounds of tests
    result_