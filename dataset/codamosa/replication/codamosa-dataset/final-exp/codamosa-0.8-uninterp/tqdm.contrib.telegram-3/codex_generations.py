

# Generated at 2022-06-14 13:31:17.487998
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    with tqdm_telegram(total=1, disable=True, ncols=120) as t:
        t.total = 0
        t.close()

# Generated at 2022-06-14 13:31:25.836539
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    from random import random
    from time import sleep
    from os import environ
    token = environ.get('TQDM_TELEGRAM_TOKEN', '1234567890:AABBCCDDEEFF')
    chat_id = environ.get('TQDM_TELEGRAM_CHAT_ID', '1234567890')
    tg = TelegramIO(token, chat_id)
    if not tg.message_id:
        return
    for _ in ttgrange(10, desc='test_TelegramIO_write'):
        sleep(random())
    tg.delete()

# Generated at 2022-06-14 13:31:35.227298
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    '''
    Test method display of class tqdm_telegram
    '''
    from tqdm.auto import tqdm
    from bs4 import BeautifulSoup
    import requests
    import re
    testtoken = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    testchatid = "-123456789"
    # See https://core.telegram.org/bots/api#message

# Generated at 2022-06-14 13:31:40.611335
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    # Arrange
    t = tqdm_telegram(_range(3), file=__file__, total=5)
    assert hasattr(t, 'tgio')
    t.tgio.message_id = "123"

    # Act
    t.clear()

    # Assert
    assert any(t.tgio.futures)

# Generated at 2022-06-14 13:31:44.248765
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    t = tqdm_telegram(total=100, token='{token}', chat_id='{chat_id}')
    t.update(10)
    t.clear()
    del t

# Generated at 2022-06-14 13:31:47.816149
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import gc
    from .utils_test import tqdm_test_config
    with tqdm_test_config(bar_format='{l_bar}{bar}{r_bar}'):
        with tqdm_telegram(bar_format="{bar}") as pbar:
            pbar.write(pbar.bar_format.format(bar='abcdefghijklm'))
            pbar.close()
            assert pbar._instances == []
            gc.collect()
            pbar.clear()
            assert pbar._last_print_n == 0
            assert pbar._instances == [pbar]

# Generated at 2022-06-14 13:31:57.951181
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from io import StringIO

    def patch_tqdm(tqdm):
        class Tqdm(tqdm):
            _instances = []

            def _format_meter(self, *args, **kwargs):
                res = super(Tqdm, self)._format_meter(*args, **kwargs)
                self._last_len = len(res)
                return res

        return Tqdm

    old_print = tqdm_auto.write
    out = StringIO()

# Generated at 2022-06-14 13:32:01.998223
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    with tqdm(total=1000, desc="my_desc") as my_tqdm:
        my_tqdm.n = 100
        my_tqdm.clear()

# Generated at 2022-06-14 13:32:07.383315
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    """
    Test function for `tqdm_telegram.clear` method.
    """
    import sys

    with tqdm_telegram(total=10, file=sys.stderr, desc="main loop") as pbar:
        for i in _range(10):
            pbar.write("clear")
            pbar.clear()
            pbar.update()
            pbar.refresh()
        pbar.close()

# Generated at 2022-06-14 13:32:10.894792
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    r = tqdm_telegram._range(10, 100, 1, disable=True)
    r.display(bar_format='{total_time}: {bar}', total=1)
    r.clear()
    if r.format_dict['bar'] != '          ' or r.last_print_n != 1:
        raise AssertionError()

# Generated at 2022-06-14 13:34:25.213340
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    from os import getenv

    t = tqdm_telegram(range(2))
    t.close()
    t.close()

# Generated at 2022-06-14 13:34:26.749771
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from .utils_test import _tqdm_telegram
    for i in _tqdm_telegram(range(10)):
        pass

# Generated at 2022-06-14 13:34:32.810459
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    tt = tqdm_telegram(_range(10), token='907253005:AAH5Qj1aAtEDR5gUGp_IVJjKhpZnqjp3XDU')
    tt.close()
    assert tt.tgio._message_id != None
    tt.tgio.write("")
    tt.clear()
    assert tt.tgio._message_id != None

# Generated at 2022-06-14 13:34:42.919345
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    import json
    import os
    import subprocess
    def run_TelegramIO_write(token, chat_id, text):
        tg = TelegramIO(token, chat_id)
        tg.write(text)
    if (not os.path.exists('.travis.yml')):
        return
    with open('../tests/token.json') as f:
        json_data = json.load(f)
    res = subprocess.run(['hostname'], stdout=subprocess.PIPE, check=True)
    host = res.stdout.decode()
    token = json_data[host]["token"]
    chat_id = json_data[host]["chat_id"]
    text = "test_TelegramIO_write"

# Generated at 2022-06-14 13:34:46.713445
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    for leave in [True, False]:
        for pos in [0, 10]:
            leave = leave
            pos = pos
            for disable in [True, False]:
                if pos == 0 and leave == True:
                    assert tqdm_telegram(
                        disable=disable, leave=leave, pos=pos).close() == False
                else:
                    assert tqdm_telegram(
                        disable=disable, leave=leave, pos=pos).close() == True

# Generated at 2022-06-14 13:34:57.495039
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():

    # Test leave=True
    tg = tqdm_telegram(iterable=[], leave=True)
    tg.close()

    # Test leave=False
    tg = tqdm_telegram(iterable=[], leave=False)
    tg.close()

    # Test leave=None pos=0
    tg = tqdm_telegram(iterable=[], leave=None)
    tg.close()

    # Test leave=True pos=1
    tg = tqdm_telegram(iterable=["a"], leave=True)
    tg.close()

    # Test leave=False pos=1
    tg = tqdm_telegram(iterable=["a"], leave=False)
    tg.close()

    # Test leave=None pos=1 (should delete message)
   

# Generated at 2022-06-14 13:35:00.012572
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    with tqdm_telegram(total=10) as pbar:
        pbar.clear()
        assert len(pbar.tgio.pool._work_queue) == 0

# Generated at 2022-06-14 13:35:09.032820
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    import time
    tqdmtoken = getenv('TQDM_TELEGRAM_TOKEN')
    tqdmchatid = getenv('TQDM_TELEGRAM_CHAT_ID')
    tg1 = TelegramIO(tqdmtoken, tqdmchatid)
    tg2 = TelegramIO(tqdmtoken, tqdmchatid)

# Generated at 2022-06-14 13:35:10.986809
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    for _ in tqdm(range(0), disable=False):
        tqdm.clear()
    tqdm.close()

# Generated at 2022-06-14 13:35:22.343177
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import pytest
    from os import getenv, unsetenv

    try:
        unsetenv('TQDM_TELEGRAM_TOKEN')
    except Exception:
        assert 'TQDM_TELEGRAM_TOKEN' not in getenv()
    try:
        unsetenv('TQDM_TELEGRAM_CHAT_ID')
    except Exception:
        assert 'TQDM_TELEGRAM_CHAT_ID' not in getenv()

    with pytest.raises(KeyError) as e:
        tqdm(1, unit='B')
    assert 'TQDM_TELEGRAM_TOKEN' in str(e)

    with pytest.raises(KeyError) as e:
        tqdm(1, unit='B', token='FooToken')

# Generated at 2022-06-14 13:37:35.431750
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    assert TelegramIO("a", "b").delete() is None