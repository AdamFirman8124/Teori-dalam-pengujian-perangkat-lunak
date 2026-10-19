

# Generated at 2022-06-14 13:31:32.315589
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    tgio = TelegramIO(token, chat_id)
    tgio.delete()


# Generated at 2022-06-14 13:31:39.658253
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    # Test tqdm_telegram with leave = True
    tg = tqdm_telegram(iterable = range(10), disable = False, leave = True)
    tg.disable = True
    tg.close()
    assert True

    # Test tqdm_telegram with leave = False
    tg = tqdm_telegram(iterable = range(10), disable = False, leave = False)
    tg.disable = True
    tg.close()
    assert True

    # Test tqdm_telegram with leave = None and pos = 0
    tg = tqdm_telegram(iterable = range(10), disable = False, leave = None)
    tg.disable = True
    tg.close()
    assert True

    # Test tqdm_telegram with leave = None and pos

# Generated at 2022-06-14 13:31:47.046053
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """
    Function to test the method display of class tqdm_telegram.
    """

    tg = tqdm_telegram(
        iterable=[1, 2, 3, 4, 5],
        desc="test",
        disable=False,
        leave=True,
        token=getenv('TQDM_TELEGRAM_TOKEN'),
        chat_id=getenv('TQDM_TELEGRAM_CHAT_ID')
    )

    assert(tg.n != None)


# Generated at 2022-06-14 13:31:57.340600
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .utils import _supports_unicode, get_bar, get_bar_unicode, get_monitor
    from .utils import randrange, time
    from .utils import TMonitor, tqdm_pandas

    var = randrange()
    for unit_scale in [True, False]:
        pbar = tqdm_telegram(range(10), unit_scale=unit_scale)
        for i in pbar:
            time.sleep(randrange())
            if unit_scale:
                n = round(var * i, 4)
                n = format(n, '.4g')
            else:
                n = var * i
            pbar.set_postfix_str(
                "postfix 1",
                "postfix 2",
                "postfix 3 = {0}".format(n))
            pbar

# Generated at 2022-06-14 13:32:08.559145
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import os
    import time
    import io
    sio = io.StringIO()

    tg = tqdm_telegram(0, file=sio)
    tg.total = 100
    tg.n = 10
    tg.avg_time = 1
    tg.last_print_t = time.time()
    tg.bar_format = '{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}'

# Generated at 2022-06-14 13:32:12.336509
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from time import sleep
    from .utils_test import pretest, posttest

    t = tqdm(**pretest())
    i = 0
    while i < 200:
        t.update()
        i += 1
        if i >= 100:
            sleep(0.01)
            t.clear()
        sleep(0.01)
    t.close()
    posttest(t)



# Generated at 2022-06-14 13:32:18.158388
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    class TestTelegramIO(TelegramIO):
        API = 'https://api.telegram.org/bot'

        def submit(self, func, *args, **kwargs):
            return func(*args, **kwargs)

    tg = TestTelegramIO("192487072:AAHZCx2QNxKaxSvO8Ww6y-U6-q3Jtc4c8bU", "586529126")
    assert(tg.message_id == 340)
    tg.write("Hello World!")

# Generated at 2022-06-14 13:32:19.951473
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    i_test = "Test"
    t_test = TelegramIO(i_test, i_test)
    assert not t_test.delete()

# Generated at 2022-06-14 13:32:30.853297
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    from socket import gaierror
    from unittest import TestCase, main

    class _TestTelegramIO(TelegramIO):
        """TelegramIO test class"""
        def __init__(self, *args, **kwargs):
            super(_TestTelegramIO, self).__init__(*args, **kwargs)
            self.data = None

        def post(self, *args, **kwargs):
            """Post Mock"""
            self.data = str(args[0]) + str(kwargs)
            self.resp_json = {'error_code': 429}

    class Tests(TestCase):
        """Test class"""
        def test_message_id_is_none(self):
            """Test message_id is None"""
            test_obj = _TestTelegramIO("token", "chat_id")

            self

# Generated at 2022-06-14 13:32:41.984116
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    _delete = TelegramIO.delete
    telegram_message_id = 42
    def delete(self):
        return telegram_message_id
    TelegramIO.delete = delete
    t = tqdm_telegram(total=0, leave=False)
    assert t.tgio.delete() == telegram_message_id
    assert t.tgio.delete() is None
    t = tqdm_telegram(total=0, leave=True)
    assert t.tgio.delete() is None
    t = tqdm_telegram(total=1, leave=None)
    assert t.tgio.delete() is None
    t = tqdm_telegram(total=1, leave=False)
    assert t.tgio.delete() == telegram_message_id
    TelegramIO.delete = _delete

# Generated at 2022-06-14 13:34:33.764596
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    from . import test_utils
    tqdm.write = test_utils.stdout_encode
    try:
        token = getenv('TQDM_TEST_TOKEN')
        chat_id = getenv('TQDM_TEST_CHAT_ID')
        if (token is None or chat_id is None):
            raise ImportError
        tg = TelegramIO(token, chat_id)
        tg.write('test')
        tg.delete()
        session = tg.session
        tqdm.write('\nOK')
    except Exception as e:
        tqdm.write('\n' + str(e))
    finally:
        session.close()

# Generated at 2022-06-14 13:34:38.560157
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    io = TelegramIO('token', 'chat_id')
    io.write('something').result()
    io.write('ddd').result()
    io.write(u"dd'fg").result()
    io.write(u"Μπ").result()
    return io

# Generated at 2022-06-14 13:34:40.966463
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    TelegramIO('token', 'chat_id').write('')


if __name__ == '__main__':
    # test
    _test_main_telegram()



# Generated at 2022-06-14 13:34:42.664618
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    from tqdm.auto import tqdm
    tqdm_telegram.close(tqdm(survey_id=0))

# Generated at 2022-06-14 13:34:45.874417
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    # test for leave=False
    bar = tqdm(total=1, leave=False)
    bar.close()
    assert bar._instances.get(bar._pos) is None

    # test for leave=True
    bar = tqdm(total=1, leave=True)
    bar.close()
    assert bar._instances.get(bar._pos) is not None

# Generated at 2022-06-14 13:34:53.673965
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    import pytest

    class FakeSession(Session):
        def post(self, *args, **kwargs):
            if len(args) == 1 and args[0] == 'delete_url':
                raise Exception('delete_exception')
            return super(FakeSession, self).post(*args, **kwargs)

    io = TelegramIO('', '')
    io.session = FakeSession()
    io.submit = lambda fn, *args, **kwargs: pytest.raises(
        Exception, msg='delete_exception',
        match=r'^Expected tqdm exception, not:\n.*delete_exception')
    io.delete()

# Generated at 2022-06-14 13:35:01.607083
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    logger = TelegramIO(getenv('TQDM_TELEGRAM_TOKEN'),
                        getenv('TQDM_TELEGRAM_CHAT_ID'))
    logger.write('TESTING tqdm_telegram_display')
    x = tqdm_telegram(range(1000), token=getenv('TQDM_TELEGRAM_TOKEN'),
                      chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'))
    for i in x:
        pass
    logger.write('TEST SUCCESSFUL')

# Generated at 2022-06-14 13:35:10.731746
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from random import random
    from time import sleep
    from io import DEFAULT_BUFFER_SIZE

    # Test default args
    t = tqdm_telegram()
    assert t._total == None
    assert t.n == 0
    assert t.dynamic_ncols == False

    # Test auto-refresh and manual refresh
    t = tqdm_telegram(0, ascii=True, dynamic_ncols=True)
    # Suppress 'xrange' objects don't have a len()
    assert len(t) == 0

    # Test manual ncols
    t = tqdm_telegram(0, ncols=80, ascii=True, dynamic_ncols=True)
    assert t.ncols == 80

    # Test moving average
    t = tqdm_telegram

# Generated at 2022-06-14 13:35:13.144089
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    io = TelegramIO('<token>', '<chat_id>')
    assert io.delete()
    io.message_id = None
    assert not io.delete()
    assert not TelegramIO('<token>', '<chat_id>').delete()

# Generated at 2022-06-14 13:35:15.641184
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    t = tqdm_telegram(total=100, desc="Test clear", leave=False)
    t.update(50)
    t.clear()
    t.close()