

# Generated at 2022-06-14 13:30:27.347006
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    for _ in tqdm_telegram(["a", "b", "c"], token=getenv('TQDM_TELEGRAM_TOKEN'),
                           chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'), miniters=1,
                           mininterval=0):
        pass


# Generated at 2022-06-14 13:30:30.350277
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """
    Test for method close of class tqdm_telegram
    """
    i = tqdm(token='token', chat_id='chat_id')
    i.close()

# Generated at 2022-06-14 13:30:33.154150
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    tqdm_telegram(['a', 'b']).close()
    assert True, 'unit test for class TelegramIO passed'



# Generated at 2022-06-14 13:30:37.386392
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    with tqdm_telegram(total=100,
                       token='1031524567:AAHR_3YNAOzQlAiO5vhJc-kD0tyKkR1B8xw',
                       chat_id='-1001217359469') as t:
        for i in range(10):
            t.update()
            time.sleep(1)

# Generated at 2022-06-14 13:30:38.918797
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
        telegram_write = TelegramIO('a', 'b').write
        assert telegram_write('c') is None

# Generated at 2022-06-14 13:30:45.985022
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from io import StringIO
    from sys import stdout
    from os import environ, getenv
    from time import time

    class io(StringIO):
        """Mock file to capture stdout"""
        def write(self, *args):
            super(io, self).write(*args)

    # Store current stdout
    #   Note: this does not work with Jupyter notebook
    current_stdout = stdout
    # Create a temporary token
    token = environ.setdefault(
        'TQDM_TELEGRAM_TOKEN', '123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # Create a temporary chat_id
    chat_id = environ.setdefault('TQDM_TELEGRAM_CHAT_ID', '123456789')
    #

# Generated at 2022-06-14 13:30:52.743411
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    # ignore
    class tqdm_fake(tqdm_telegram):
        def __init__(self, *args, **kwargs):
            super(tqdm_telegram, self).__init__(*args, **kwargs)
    t = tqdm_fake(_range(3), token='token', chat_id='chat_id')
    assert t.tgio.token == 'token'
    assert t.tgio.chat_id == 'chat_id'

# Generated at 2022-06-14 13:30:55.697393
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from io import StringIO
    io = StringIO()
    bar = tqdm_telegram(desc=__name__, total=10, file=io, disable=True)
    for _ in range(10):
        bar.n = _
        bar.display()
        assert io.getvalue().strip() == \
            u'{0:>2}/10 {0:2.0f}%|{1}|[elapsed: 0:00:00]'.format(_, 10 * '#')
        io.seek(0)
        io.truncate()



# Generated at 2022-06-14 13:31:05.807435
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    """Unit test for constructor of class tqdm_telegram"""
    t = tqdm_telegram(total=4)
    for i in range(5):
        t.update(1)
    t.close()


if __name__ == '__main__':
    from time import sleep
    import warnings
    warnings.filterwarnings("ignore", message="Handler 'h'", category=TqdmWarning)
    # examples
    with tqdm(total=30) as t:
        for i in range(10):
            sleep(.25)
            t.update()
    with trange(10) as t:
        for i in t:
            sleep(.25)
        t.set_description('Processing..')
        for i in t:
            sleep(.25)

# Generated at 2022-06-14 13:31:17.444953
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import pytest
    from ..std import tqdm_gui
    from ..pandas import tqdm_pandas
    from ..std import tqdm_notebook
    from .tqdm_telegram import tqdm_telegram
    from .tqdm_telegram import TelegramIO

    try:
        tqdm_telegram((i for i in range(3)), disable=True)
    except Exception as e:
        pytest.fail(f"test_tqdm_telegram_clear() raised Exception: {e}")
    try:
        tqdm_telegram((i for i in range(3)), bar_format="a", disable=True)
    except Exception as e:
        pytest.fail(f"test_tqdm_telegram_clear() raised Exception: {e}")


#

# Generated at 2022-06-14 13:32:42.837226
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    """Unit test for method write of class TelegramIO"""
    print('Testing TelegramIO.write()...', end='')
    from requests import HTTPError
    from time import sleep
    from random import seed, randint
    from tqdm.utils import _term_move_up
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    seed(1)
    for _ in range(20):
        s = TelegramIO(token, chat_id)
        tqdm_auto.write(' ' * (len(s.text) + 2))
        _term_move_up()
        tqdm_auto.write(s.text)
        sleep(randint(1, 10))

# Generated at 2022-06-14 13:32:47.914437
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    """
    Unit test for tqdm_telegram constructor
    """
    from .tests_telegram import main as test_tqdm_telegram_main
    from .utils_override import ArgumentParserError
    try:
        test_tqdm_telegram_main()
    except ArgumentParserError:
        pass

# Generated at 2022-06-14 13:32:49.227681
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm(total=1, leave=False)
    t.close()

# Generated at 2022-06-14 13:32:53.924460
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    with tqdm_telegram(total=100, token='749333786:AAE7Vu_kI9A7VHXGXfvFxIIMtbN6DwRO-Hg', chat_id='-284833842') as t:
        for i in range(10):
            t.update()

# Generated at 2022-06-14 13:32:58.784065
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    with tqdm(['a', 'b'], disable=True, token='', chat_id='') as t:
        t.n = 1
        t.display()

# Generated at 2022-06-14 13:33:00.453425
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    assert TelegramIO(token='test1', chat_id='test2').write('test') is None


# Generated at 2022-06-14 13:33:10.279337
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import mock
    import shutil


# Generated at 2022-06-14 13:33:12.719217
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    tio = TelegramIO("token", "chat-id")
    tio._message_id = 0
    assert(tio.message_id == 0)
    tio.delete()

# Generated at 2022-06-14 13:33:18.846319
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .utils import _test_write_read_bar_tqdm
    _test_write_read_bar_tqdm(tqdm)  # do not pass kwargs below
    _test_write_read_bar_tqdm(tqdm, miniters=10)
    _test_write_read_bar_tqdm(tqdm, mininterval=0.01)
    _test_write_read_bar_tqdm(tqdm, miniters=10, mininterval=0.01)

# Generated at 2022-06-14 13:33:25.946788
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import random
    import time
    random.seed(0)
    tg = tqdm_telegram(total=100)
    for k in range(100):
        time.sleep(2 * random.random())
        tg.display(**{
            'bar_format': f'{k:03} |{k+1}|',
            'postfix': {'A': k+1, 'B': k+2}
        })
    tg.close()
    assert tg.tgio.message_id is not None



# Generated at 2022-06-14 13:36:17.692833
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    for _ in tqdm(range(4), disable=False):
        pass

# Generated at 2022-06-14 13:36:27.236515
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    # test 1
    pbar = tqdm_telegram(total=10, file=TelegramIO('', ''),
                         mininterval=0.000000000001)
    for i in range(3):
        pbar.update()
    pbar.close()
    # test 2
    pbar = tqdm_telegram(total=10, file=TelegramIO('', ''),
                         bar_format="{bar:} {postfix[0]} {postfix[1]}")
    pbar.update()
    pbar.set_postfix_str("a", "b")
    pbar.close()
    # test 3
    pbar = tqdm_telegram(total=10, file=TelegramIO('', ''),
                         bar_format="{bar:} {postfix}")
    pbar.update()

# Generated at 2022-06-14 13:36:30.438439
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    t = tqdm_telegram(1, token=getenv('TQDM_TELEGRAM_TOKEN'),
                      chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'))
    t.display()
    t.n = t.total
    t.display()

# Generated at 2022-06-14 13:36:37.916937
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    t = tqdm_telegram(range(10), clear=True, leave=False)
    # test the first call of display()
    t.display()
    assert t.tgio.text != '', \
        'TelegramIO.write() called by class tqdm_telegram.display() failed'
    # test the next calls of display()
    old_text = t.tgio.text
    for i in t:
        t.display(i)
        assert t.tgio.text == old_text, \
            'TelegramIO.write() called by class tqdm_telegram.display() failed'
    t.close()
    assert t.tgio.text == '', \
        'TelegramIO.write() called by class tqdm_telegram.close() failed'



# Generated at 2022-06-14 13:36:41.626861
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    telegram_io = TelegramIO(token, chat_id)
    telegram_io.write('')
    telegram_io.write('test')
    telegram_io.write('test2')

# Generated at 2022-06-14 13:36:44.756784
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    t = tqdm_telegram(total=10, bar_format='{desc}{l_bar}{bar}{r_bar}',
                      desc='Test')
    assert len(t.format_dict['desc']) == 0
    t.display()
    assert len(t.format_dict['desc']) > 0

# Generated at 2022-06-14 13:36:55.342076
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import io
    capture = io.StringIO()

    t = tqdm(["a", "b", "c"], file=capture)
    t.update()
    t.update()
    t.update()
    t.clear()
    t.close()

    current_capture = capture.getvalue()


if __name__ == '__main__':
    from os import getenv
    _token = getenv('TQDM_TELEGRAM_TOKEN')
    _chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    print("Token:", _token)
    print("Chat:", _chat_id)
    from time import sleep


# Generated at 2022-06-14 13:37:00.828516
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """Test tqdm_telegram.close()"""
    try:
        for _ in tqdm_telegram(
                range(2), total=2, disable=True,
                token="test", chat_id="test"):
            pass
    except:
        raise AssertionError('tqdm_telegram.close() should not raise any '
                             'exception when disable is set')

# Generated at 2022-06-14 13:37:08.919211
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    from os import environ
    from requests import post
    from .tests import PythonIO
    for out in (PythonIO(), TelegramIO(environ['TQDM_TELEGRAM_TOKEN'],
                                       environ['TQDM_TELEGRAM_CHAT_ID'])):
        if out.message_id is None:
            break
        for i in tqdm(range(10), file=out):
            out.write("i = %d" % i)
        out.write("Done.")
        out.delete()


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-14 13:37:15.775031
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """
    Test if method `display` of class tqdm_telegram is working normally.
    """
    test_data = {
        'bar_format': '{bar}',
    }

    result_data = {
        'bar_format': '{l_bar}{bar:10u}{r_bar}',
    }

    try:
        tqdm_telegram().format_dict = test_data
        tqdm_telegram().display()
        assert tqdm_telegram().format_dict == result_data
    except AssertionError:
        print("Test method display of class tqdm_telegram failed.")
    else:
        print("Test method display of class tqdm_telegram passed.")

if __name__ == '__main__':
    test_tqdm_telegram_display()