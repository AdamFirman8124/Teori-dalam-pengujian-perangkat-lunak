

# Generated at 2022-06-14 13:32:27.777978
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    with tqdm(total=3, token='{token}', chat_id='{chat_id}') as pbar:
        pbar.update()
        pbar.update()
        pbar.update()

# Generated at 2022-06-14 13:32:34.569165
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm_telegram(range(10), token='901271047:AAG5oikvDm5dRjKzXoJyW0cBJgYlSGrwI6U', chat_id='808876638')
    for i in t:
        t.close()
        t.close()
        t.close()
    t.close()

# Generated at 2022-06-14 13:32:39.170155
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    io = TelegramIO('42', '42')
    io._message_id = 42
    assert io.message_id == 42
    assert io.write("test") is not None
    assert io.write("") is None
    assert io.write("") is None  # avoid Bot duplicate message error



# Generated at 2022-06-14 13:32:44.493580
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from io import StringIO
    from sys import platform
    with StringIO() as f:
        for _ in tqdm_telegram(list(range(10)), file=f, mininterval=0.0001, disable=True):
            pass
        if platform == "win32":
            assert f.getvalue() == "0/10 [#--------]                                                    \r\n"
        else:
            assert f.getvalue() == "0/10 [#--------]                                                    \n"

# Generated at 2022-06-14 13:32:47.913813
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    with tqdm_telegram(disable=True) as t:
        pass
    with tqdm_telegram(leave=True) as t:
        pass
    with tqdm_telegram(leave=False) as t:
        pass

# Generated at 2022-06-14 13:32:57.206002
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    t = tqdm_telegram(total=10, token='123123123:ABCDEF', chat_id='1234567890')
    t.display()
    assert t._instant_delta == 0
    assert t.format_dict['n'] == 0

    t.display(n=10)
    assert t._instant_delta == 10
    assert t.format_dict['n'] == 10
    t.clear()


# We can't unit test for creating & updating a Telegram message, it's async
#def test_tqdm_telegram():
#    for i in tqdm_telegram(range(5), token='123123123:ABCDEF', chat_id='1234567890'):
#        pass
#    for i in tqdm_telegram(range(5), disable=True):
#       

# Generated at 2022-06-14 13:33:00.325241
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    """Tests tqdm_telegram.clear()."""
    t = tqdm_telegram(total=10, leave=True)
    t.refresh()
    t.clear()
    t.close()

# Generated at 2022-06-14 13:33:03.239629
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    # Check that clear() method doesn't raise an exception
    t = tqdm_telegram(total=10, disable=True)
    t.clear()
    assert t.get_lock().locked()  # should not release lock

# Generated at 2022-06-14 13:33:04.359434
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    assert TelegramIO('', '').write('') == None

# Generated at 2022-06-14 13:33:12.475456
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """Unit test for method close of class tqdm_telegram."""
    for i in range(10):
        tqdm_telegram(10, desc='test_tqdm_telegram_close',
                      token='1020401305:AAFGtAUeRtRzD12PbAOSTGk-q3d8wQzmCZg',
                      chat_id='730052995').close()


test_tqdm_telegram_close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Sends updates to a Telegram bot.')

# Generated at 2022-06-14 13:35:36.861004
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    t = tqdm_telegram(0, disable=True)
    t.last_print_t = t.last_print_n = 0
    t.display(n=0, total=None, bar_format='{l_bar}{bar:10u}{r_bar}',
              elapsed=0, ncols=None, unit='it', unit_scale=True,
              dynamic_ncols=True)
    assert t.format_dict['bar_format'] == '{l_bar}{bar:10u}{r_bar}'

# Generated at 2022-06-14 13:35:47.215150
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """
    Unit test for method display of class tqdm_telegram.
    """
    from io import StringIO
    from time import sleep

    # Get the token and chat_id from the shell environment
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')

    # If the token nor the chat_id are informed, the test ends
    if not token or not chat_id:
        raise RuntimeError(
            'Token and chat_id from Telegram not informed. Test ends.')

    # Test the method display of the class tqdm_telegram

# Generated at 2022-06-14 13:35:56.003916
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    if not token:
        print('test_TelegramIO_delete: '
              'skip (environment variable TQDM_TELEGRAM_TOKEN is not set)')
        return
    if not chat_id:
        print('test_TelegramIO_delete: '
              'skip (environment variable TQDM_TELEGRAM_CHAT_ID is not set)')
        return

    io = TelegramIO(token, chat_id)
    io.write('test_TelegramIO_delete')
    io.delete()

    io = TelegramIO(token, chat_id)
    io.write('test_TelegramIO_delete')

test_Telegram

# Generated at 2022-06-14 13:35:57.002466
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    t = tqdm_telegram(1, 1, 'test', token='1234', chat_id='5678')
    t.display()

# Generated at 2022-06-14 13:36:02.637178
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import pytest
    from tqdm.auto import tqdm
    from tqdm.contrib.telegram import TelegramIO

    # monkey patching to bypass requests.post(...)
    # usage of requests.post will be tested in test_tqdm_telegram_tgio
    def patch_write(self, s):
        return s

    # monkey patching to make tqdm.write(...) return something
    def patch_write_tqdm(s, *args, **kwargs):
        return s

    tqdm_auto.write = patch_write_tqdm

    # test without TelegramIO instance
    call = tqdm_telegram(bar_format="{bar}", disable=True)

    assert call.display() == ""
    assert call.display(nolock=False) == ""
    assert call

# Generated at 2022-06-14 13:36:12.530842
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    token = getenv('TQDM_TELEGRAM_TOKEN')

    # Test with normal string
    test_text = "test_text_for_TelegramIO_write"
    test_file = TelegramIO(chat_id, token)
    test_file.write(test_text)

    # Test with no text
    test_file.write('')
    # Test with text with length one
    # test_file.write('a')

    # Test with text with '\r'
    test_file.write('\rText_with_\r_')

    # Test with non-text object
    test_file.write(['test_non_text_object'])

    # Test with non-text object with length one


# Generated at 2022-06-14 13:36:21.013756
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .tests_tqdm import pretest_posttest, closing

    @pretest_posttest
    def test_tqdm_telegram_display_ascii():
        with closing(tqdm_telegram(10, token='0' * 32, chat_id='0')) as t:
            t.display(l_bar='{desc}:', r_bar='{bar}', rate='{rate:5.2g}')


# Generated at 2022-06-14 13:36:24.882453
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    try:
        for i in tqdm(range(10), token='token', chat_id='chat_id'):
            if i == 5:
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        pass

# Generated at 2022-06-14 13:36:28.376367
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    chat_id = '26817106'
    token = '1216496926:AAF0mfizRgChcWJOYAaIyn6Uf1z0vNDkUd8'
    io = TelegramIO(token, chat_id)
    io.write('test')
    io.delete()

# Generated at 2022-06-14 13:36:32.667563
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    total = 5
    tieout = 10
    import time
    with tqdm(total=total) as pbar:
        for _ in range(total/2):
            pbar.update()
        time.sleep(tieout)
        pbar.clear()
        for _ in range(total/2):
            pbar.update()