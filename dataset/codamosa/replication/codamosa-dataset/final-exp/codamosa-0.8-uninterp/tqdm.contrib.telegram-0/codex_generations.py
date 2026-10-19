

# Generated at 2022-06-14 13:30:18.019106
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .utils import _range
    for _ in tqdm_telegram(_range(10), token='928168590:AAGbuS0zS12nY6IJNb6xdvh93W4jK96-LU0', chat_id='376098906'):
        pass

# Generated at 2022-06-14 13:30:30.109019
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from time import sleep

    with tqdm_telegram(total=2, desc='Foo!!!',
                       token=getenv('TQDM_TELEGRAM_TOKEN'),
                       chat_id=getenv('TQDM_TELEGRAM_CHAT_ID')) as pbar:
        sleep(0.3)
        pbar.set_description("Bar!!!")
        pbar.update()
        sleep(0.3)
        pbar.update()
    with tqdm_telegram(total=3, unit='i',
                       token=getenv('TQDM_TELEGRAM_TOKEN'),
                       chat_id=getenv('TQDM_TELEGRAM_CHAT_ID')) as pbar:
        sleep(0.3)
        pbar.update(1)

# Generated at 2022-06-14 13:30:32.151303
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm_telegram(disable=True)
    assert t.disable

# Generated at 2022-06-14 13:30:33.315380
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    tqdm_telegram(range(3)).close()

# Generated at 2022-06-14 13:30:41.696909
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    from .utils_test import _check_close

    class _TqdmTest(tqdm_telegram):
        """Slightly altered tqdm_telegram for testing purposes"""
        def __init__(self, *args, **kwargs):
            args2 = list(args)
            args2[0] = range(args2[0])
            
            super(_TqdmTest, self).__init__(*args2, **kwargs)
            self.delete_called = False
            self.write_called = False

        def write(self, *args, **kwargs):
            self.write_called = True

        def delete(self, *args, **kwargs):
            self.delete_called = True

    _check_close(_TqdmTest)


# Generated at 2022-06-14 13:30:46.713604
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    m = tqdm_telegram(range(3), leave=False, bar_format='{l_bar}{bar}{r_bar}')
    try:
        for i in m:
            pass
    except KeyboardInterrupt:
        assert True
    else:
        assert False
    try:
        m.close()
    except:
        assert False
    else:
        assert True

# Generated at 2022-06-14 13:30:50.695921
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .utils_test import _test_clear
    with _test_clear(tqdm_telegram) as progress_bar:
        progress_bar.update(2)
        progress_bar.update()

# Generated at 2022-06-14 13:30:54.880436
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    import time
    sleep = time.sleep
    my_tqdm = tqdm_telegram(total=10)
    my_tqdm.update(0)
    sleep(0.5)
    my_tqdm.close()
    sleep(0.5)

if __name__ == '__main__':
    test_tqdm_telegram_close()

# Generated at 2022-06-14 13:31:05.768129
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from os import devnull
    from sys import platform
    from tqdm.auto import tqdm
    from .utils_test import check_remove

    # Check 1/3
    try:
        check_remove()
        with open(devnull, 'w') as f:
            with tqdm(range(2), file=f) as pbar:
                pbar.update()
                pbar.clear()
                pbar.close()
    except Exception:
        raise
    finally:
        check_remove()

    # Check 2/3

# Generated at 2022-06-14 13:31:14.297200
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from argparse import Namespace
    from .utils import _term_move_up
    from .utils_test import _fake_write

    obj = tqdm_telegram(Namespace(bar_format='{bar}'),
                        token=getenv('TQDM_TELEGRAM_TOKEN'),
                        chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'))
    obj.pbar_str = 'bar'
    obj.dynamic_messages = {}
    assert obj.display() == _fake_write(_term_move_up() + 'bar')

# Generated at 2022-06-14 13:33:14.627821
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    global token, chat_id
    if token is None or chat_id is None:
        warn('Token or chat_id not found, please provide valid token and chat_id in the code'
            ' and run tests with the argument --pyargs tqdm.contrib.telegram')
        return
    telegramIO = TelegramIO(token, chat_id)
    telegramIO.submit(telegramIO.session.post, telegramIO.API + '%s/sendMessage' % token, data={
        'text': "Test message", 'chat_id': chat_id, 'parse_mode': 'MarkdownV2'})
    telegramIO.delete()
    assert True


# Generated at 2022-06-14 13:33:21.763230
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    # Work-in-progress
    from subprocess import Popen, PIPE
    import re
    import os
    import sys
    import signal
    import multiprocessing
    import time

    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    assert token is not None, "Set TQDM_TELEGRAM_TOKEN env var."
    assert chat_id is not None, "Set TQDM_TELEGRAM_CHAT_ID env var."


# Generated at 2022-06-14 13:33:26.109968
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from time import sleep
    from ..utils import _term_move_up
    with tqdm_telegram(total=10, miniters=None, mininterval=0) as t:
        for i in _range(5):
            t.update(5)
            sleep(0.5)
            t.clear()

# Generated at 2022-06-14 13:33:29.254792
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm_telegram(range(1))
    t.close()
    assert not t.tgio.workers
    assert not t.tgio.futures

# Unit tests for class TelegramIO

# Generated at 2022-06-14 13:33:37.113958
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import colorama
    from io import StringIO
    import sys

    # Test with color and without
    for color, clean in [(True, colorama.ansi.clear_line_ansi), (False, '')]:
        t = tqdm_telegram()
        t.leave = \
            t.clear = \
            t.bar_format = ' '
        tqdm_auto.write = lambda s: None  # Suppress non-test output

        # Test with and without file
        for f in [sys.stdout, StringIO(), None]:
            t.fd = f
            t.color = color
            t._send_update('q')
            assert t.tgio.text == 'q'
            t._send_update('w')
            assert t.tgio.text == 'w'
            t._send_

# Generated at 2022-06-14 13:33:39.415214
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .utils_test import _test_telegram, _test_clear

    _test_telegram(lambda: _test_clear(tqdm_telegram))



# Generated at 2022-06-14 13:33:47.691827
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import pytest
    from pkg_resources import parse_version
    from ast import literal_eval as make_tuple

    # test_tqdm_telegram_display() is disabled due to broken dependencies
    pytest.importorskip("requests")  # requires requests

    import requests
    if parse_version(requests.__version__) <= parse_version("2.5.2"):
        pytest.skip("telegram-tqdm unit-test requires requests >= 2.5.3")

    # get env variables
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')


# Generated at 2022-06-14 13:33:51.188709
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """
    Check that the method close of the class tqdm_telegram does not
    raise errors.
    """
    t = tqdm_telegram(range(10))
    t.close()
    t.disable = True
    t.close()

# Generated at 2022-06-14 13:33:58.530825
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    for i in tqdm_telegram(range(10), token='{token}', chat_id='{chat_id}'):
        pass


if __name__ == '__main__':
    __doc__ = __doc__.format(token="<YOUR_TELEGRAM_TOKEN_HERE>",
                             chat_id="<YOUR_TELEGRAM_CHAT_ID_HERE>")
    from doctest import testmod
    testmod(raise_on_error=True, verbose=True)
    test_tqdm_telegram_clear()

# Generated at 2022-06-14 13:34:00.476111
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from .tests import tests_telegram  # noqa


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:37:32.502901
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .utils_test import _imap_test, test_cls
    test_cls(tqdm_telegram, 'display', imap=_imap_test)



# Generated at 2022-06-14 13:37:34.927944
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from ._utils_test import _test_tqdm_display
    return _test_tqdm_display(tqdm_telegram)

# Generated at 2022-06-14 13:37:45.976980
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from unittest import TestCase

    class tqdm_telegram_display(TestCase):
        @classmethod
        def setUpClass(cls):
            cls.identity = str(cls) + "." + cls.__name__
            tqdm_auto.write(cls.identity + ": test @ "
                            + tqdm_auto.format_interval(tqdm_auto.monotonic()))

        def tearDown(self):
            try:
                del self.pbar
            except AttributeError:
                pass

        def test_tqdm_telegram(self):
            from os import getenv
            from tqdm.auto import trange
            from tqdm.contrib.telegram import tqdm_telegram
            self.pbar = tqdm_