

# Generated at 2022-06-14 13:31:44.248931
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """
    Do not run doctest, as it will hang on travis-ci.
    Will create a tqdm bar on your Telegram if proper token and chat_id are set
    in your environment variables.
    """
    tqdm(total=100, desc="test run").display()

# Generated at 2022-06-14 13:31:54.888522
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    if not (token and chat_id):
        from nose.plugins.skip import SkipTest
        raise SkipTest("Skipping tqdm.contrib.telegram.test_tqdm_telegram_display: "
                       "$TQDM_TELEGRAM_TOKEN & $TQDM_TELEGRAM_CHAT_ID are required")

    t = tqdm_telegram(desc='test', total=3, token=token, chat_id=chat_id)

# Generated at 2022-06-14 13:31:58.738064
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """
    Create a tqdm instance and test the close method with 
    different values of leave argument.
    """
    t = tqdm_telegram(total=1, token='{token}', chat_id='{chat_id}')
    t.close()
    t.close(leave=True)
    t.close(leave=False)

# Generated at 2022-06-14 13:32:09.044183
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from shutil import rmtree
    from tempfile import mkdtemp
    from os.path import join
    from math import ceil
    from subprocess import check_output
    from time import sleep

    token = check_output(["cat", "secret.txt"])

    tmp_dir = mkdtemp()
    tqdm_auto.write(tmp_dir)
    with open(join(tmp_dir, "test.txt"), 'w') as f:
        f.write('test')
    sleep(1)

    # make sure that the other Bot will have time to read the message
    t1 = tqdm_telegram(total=ceil(sleep(1)), token=token,
                       chat_id="-375068367", unit='s', unit_scale=True)

# Generated at 2022-06-14 13:32:11.477497
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    a = TelegramIO("test_token", "test_chat_id")
    a.write("test_write")


if __name__ == '__main__':
    test_TelegramIO_write()

# Generated at 2022-06-14 13:32:13.097043
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    io = tqdm_telegram(total=100)
    io.close()
    assert io.stdout.closed

# Generated at 2022-06-14 13:32:19.440057
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from requests.exceptions import ConnectionError
    from .dummy_tqdm import DummyTelegram
    with DummyTelegram() as telegram:
        t = tqdm_telegram(bar_format='foo')
        try:
            t.tgio.session.post(t.tgio.API + '123456789.987654321:ABCD/sendMessage')
        except ConnectionError as e:
            pass
        else:
            raise AssertionError('test case should raise ConnectionError')
        t.display()
        assert telegram.l_bar, 'display() should call write()'

# Generated at 2022-06-14 13:32:23.126757
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    """
    >>> from tqdm.contrib.telegram import TelegramIO
    >>> tgio = TelegramIO('{token}', '{chat_id}')
    >>> tgio.delete().result()
    """
    pass


# Generated at 2022-06-14 13:32:28.112702
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from io import StringIO
    import sys

    io = StringIO()
    sys.stderr = io
    tqdm_telegram(total=10, bar_format="{bar}")
    assert io.getvalue().rstrip() == '{bar:10u}'

# Generated at 2022-06-14 13:32:35.633968
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    tgio = TelegramIO(token, chat_id)
    assert tgio.delete().result().status_code == 200
    tqdm_auto.write("All tests passed")

if __name__ == '__main__':
    test_TelegramIO_delete()

# Generated at 2022-06-14 13:35:10.950536
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    from ..utils import _range
    from .utils_test import check_token, take
    # check token
    token = check_token()
    if not token:
        return
    # get chat_id
    chat_id = take()
    if not chat_id:
        return
    f = TelegramIO(token, chat_id)
    for i in _range(10):
        f.write(str(i))
    f.delete()

# Generated at 2022-06-14 13:35:14.999349
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    assert tqdm(range(10), leave=False, disable=False).close() is None
    assert tqdm(range(10), leave=False, disable=False).clear() is None

test_tqdm_telegram_clear()

# Generated at 2022-06-14 13:35:24.065844
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from tqdm import tqdm
    from sys import stderr
    for i in tqdm_telegram(iterable=range(100), file=stderr, bar_format="{postfix}", postfix=["a"]):
        pass
        # Should print 'a', '100/100 100%|| 100/100 [00:00<00:00, ...]', etc


if __name__ == '__main__':
    from os import getenv
    for _ in tqdm_telegram(range(100),
                           token=getenv('TQDM_TELEGRAM_TOKEN'),
                           chat_id=getenv('TQDM_TELEGRAM_CHAT_ID')):
        pass

# Generated at 2022-06-14 13:35:27.703167
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from tqdm.contrib.telegram import tqdm, trange
    with tqdm(total=1000, desc='test', desc_set={}):
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:35:35.636050
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():

    class A(tqdm_telegram):
        def __init__(self, *args, **kwargs):
            super(tqdm_telegram, self).__init__(*args, **kwargs)
            self.leave = None
    a = A(1)
    a.pos = 0
    assert a.tgio.write.call_count == 1
    a.close()
    assert a.tgio.write.call_count == 2
    a.close()
    assert a.tgio.write.call_count == 3
    a.tgio.write.call_count = 0
    a = A(1)
    a.pos = 1
    a.close()
    assert a.tgio.write.call_count == 0
    a = A(1, leave=False)
    a.pos = 1


# Generated at 2022-06-14 13:35:38.544097
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .utils import _test_clear
    _test_clear(tqdm_telegram)

# Generated at 2022-06-14 13:35:41.293035
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import pytest
    tg = tqdm_telegram(total=2)
    assert tg.format_meter(bar_format='{bar}') == '{bar:10u}'


# Generated at 2022-06-14 13:35:45.878006
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from time import sleep
    for i in tqdm(range(10), desc='some desc', leave=True, ascii=True,
                  unit_scale=True, mininterval=0.01):
        sleep(i/2)

if __name__ == '__main__':
    test_tqdm_telegram_display()

# Generated at 2022-06-14 13:35:47.887460
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from pytest import raises
    with raises(AttributeError):
        for i in tqdm_telegram(iterable, token='{token}', chat_id='{chat_id}', leave=None):
            if i == 1:
                raise StopIteration()

# Generated at 2022-06-14 13:35:51.530750
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    from unittest import TestCase

    class TestTelegramIO(TestCase):
        pass

    TelegramIO._delete = TelegramIO.delete
    TelegramIO.delete = lambda self: None

    try:
        tio = TelegramIO(token='{token}', chat_id='{chat_id}')
        tio.delete()
    except Exception:
        TestTelegramIO.fail(self, "test_TelegramIO_delete()")
    finally:
        TelegramIO.delete = TelegramIO._delete
        del TelegramIO._delete