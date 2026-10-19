

# Generated at 2022-06-14 13:33:43.329388
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import re
    from .utils_test import _test_display
    from .utils_test import unicode

    class tqdm_telegram(_tqdm_telegram):
        def display(self, **kwargs):
            super(tqdm_telegram, self).display(**kwargs)
            try:
                stdout.write(self._last_write)
            except AttributeError:
                self._last_write = ""
            self._last_write += re.sub(r'\x1b[^m]*m', '',
                                       self.format_meter(**self.format_dict))

    with tqdm_telegram(total=10, ascii=True) as t:
        for i in range(10):
            t.update()
            time.sleep(0.1)


# Generated at 2022-06-14 13:33:47.892933
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from os import environ
    from random import random
    from time import sleep
    environ['TQDM_TELEGRAM_CHAT_ID'] = '0'
    environ['TQDM_TELEGRAM_TOKEN'] = '0'
    for i in tqdm(range(100), desc='Test', total=100):
        sleep(random() / 50)

if __name__ == "__main__":
    test_tqdm_telegram()

# Generated at 2022-06-14 13:33:58.397925
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    with tqdm_telegram(total=1, bar_format='{bar:50u}', token=None,
                       chat_id=None) as pbar:
        pbar.update(1)
    assert pbar.bar_format == '{bar:50u}'


if __name__ == "__main__":
    from os import remove
    from shutil import rmtree
    from tempfile import gettempdir

    try:
        import pytest
        pytest.main([__file__])
    finally:
        tmp = gettempdir()
        if tmp:
            tmp_files = [f for f in os.listdir(tmp)
                         if f.startswith("tqdm_telegram_")]

# Generated at 2022-06-14 13:34:01.516694
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm_telegram(total=100,leave=False,disable=False)
    t.close()
    t = tqdm_telegram(total=100,leave=True,disable=False)
    t.close()

# Generated at 2022-06-14 13:34:08.534121
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    for leave in [True, False]:
        for pos in [0, 5]:
            t = tqdm_telegram(total=10, leave=leave, pos=pos)
            t.clear()
            assert t.last_print_n == None and t.n == pos
            assert t.disable == False and t.leave == leave
            assert t.bar_format == '{l_bar}{bar:10u}{r_bar}' and t.pos == pos



# Generated at 2022-06-14 13:34:11.076830
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    with tqdm(total = 100) as t:
        for i in range(100):
            t.update(1)
    assert(t.tgio.write("") != None)

# Generated at 2022-06-14 13:34:13.583684
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    t = TelegramIO('1122334455:AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQ',
                   '123456789')
    t.write('testing TelegramIO.write')


# Generated at 2022-06-14 13:34:18.842458
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """Testing tqdm_telegram.display()"""
    from time import sleep
    from numpy.random import randint

    def check_display(t, n, **kwargs):
        sleep(randint(n=5) / 5.)
        t.update(randint(n=n))
        t.refresh(**kwargs)
        t.display(**kwargs)
        return t

    def check_clear(t):
        sleep(randint(n=5) / 5.)
        t.clear()
        return t

    def check_close(t):
        sleep(randint(n=5) / 5.)
        t.close()
        return t


# Generated at 2022-06-14 13:34:23.633099
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    # Test for method close of class tqdm_telegram
    for leave in [True, False, None]:
        for pos in [0, 1, 'foo']:
            for disable in [True, False, None]:
                instance = tqdm_telegram(leave=leave, disable=disable, pos=pos)
                instance.close()
test_tqdm_telegram_close()

# Generated at 2022-06-14 13:34:27.701113
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from tqdm.contrib.telegram import tqdm_telegram
    for test_iterable in (range(1000), iter(range(1000)), range(1000).__iter__()):
        with tqdm_telegram(test_iterable) as bar:
            for i in bar:
                pass


if __name__ == '__main__':
    from .utils_telegram_test import main
    main(__file__)

# Generated at 2022-06-14 13:36:54.257392
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    """Test TelegramIO.write function."""
    telegramio = TelegramIO(token=getenv('TQDM_TELEGRAM_TOKEN'), chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'))
    telegramio.text = ""
    telegramio.write(u"This is a test")
    telegramio.delete()

# Generated at 2022-06-14 13:37:00.115841
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .utils import _setup_tqdm, _teardown_tqdm, FakeTTY

    tqdm_args, _, tqdm_cls, _ = _setup_tqdm()

    with FakeTTY():
        with tqdm_cls(*tqdm_args, desc='test clear', unit='unit',
                      leave=False) as pbar:
            p = tqdm_telegram(total=100)
            p.write("*")
            pbar.update(1)
            p.write("*")
            pbar.clear()
            pbar.write("*")
            p.update(50)

    _teardown_tqdm()

# Generated at 2022-06-14 13:37:01.860973
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    myTqdm = tqdm_telegram(0)
    myTqdm.close()

# Generated at 2022-06-14 13:37:06.612842
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    t = tqdm_telegram(_range(10),
                      bar_format="{l_bar}{bar:10u}{r_bar}",
                      desc="Test",
                      disable=True)
    t.display()
    t.close()


if __name__ == '__main__':
    from ._main import main
    main()

# Generated at 2022-06-14 13:37:10.411058
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from .gui import _test_tqdm_telegram as test_tqdm_telegram
    with test_tqdm_telegram():
        import time
        for i in tqdm(iterable=range(10), token='{token}', chat_id='{chat_id}'):
            time.sleep(0.3)

# Generated at 2022-06-14 13:37:17.857035
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    import time
    t = tqdm(total=1, leave=False, disable=False)
    t.close()
    t.close()
    t = tqdm(total=1, leave=True, disable=False)
    t.close()
    t.close()
    t = tqdm(total=1, leave=None, disable=False)
    t.close()
    t.close()


if __name__ == '__main__':
    from ._main import main
    main()

# Generated at 2022-06-14 13:37:19.225236
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    tg = tqdm_telegram(0)
    tg.close()

# Generated at 2022-06-14 13:37:27.179184
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from os import environ
    from requests.exceptions import ConnectionError
    from tqdm.contrib.telegram import tqdm_telegram, ttgrange, tqdm, trange,\
        TelegramIO
    from .utils import _range, FormatCustomText, FormatCustomETB,\
        fmtdict, StringIO

# Generated at 2022-06-14 13:37:31.126101
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    tgio = TelegramIO(token="1234", chat_id="5678")
    message_id = tgio.message_id
    assert message_id == None
    tgio.delete()
    assert tgio.message_id == message_id

# Generated at 2022-06-14 13:37:41.788283
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    from time import sleep
    from os import environ
    old_mods = environ.get('TQDM_COL_DISABLE', '')
    environ['TQDM_COL_DISABLE'] = '1'
    # simple close test
    with tqdm(total=1, token='a', chat_id='b') as t:
        t.close()
    # test that the message is not deleted if `leave` = True
    with tqdm(total=1, token='a', chat_id='b') as t:
        t.close(leave=True)
    # test the auto leave if relevant
    with tqdm(total=1, token='a', chat_id='b') as t:
        t.close()