

# Generated at 2022-06-14 13:31:26.129145
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    class TqdmDisplayMock(tqdm_telegram):
        def display(self, **kwargs):
            super(TqdmDisplayMock, self).display(**kwargs)
            return self.format_dict['bar_format']

    t = TqdmDisplayMock(10, disable=True)
    assert t.display() == '{bar:10u}'
    t = TqdmDisplayMock(10, disable=True, bar_format='|{bar}|')
    assert t.display() == '|{bar:10u}|'
    t = TqdmDisplayMock(10, disable=True, bar_format='<{bar}>')
    assert t.display() == '<{bar:10u}>'

# Generated at 2022-06-14 13:31:35.411825
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    import os
    from .utils_test import _delete_dir
    from .utils_test import _test_write
    from .utils_test import _test_reset_deprecate
    from .utils_test import _test_close_deprecate
    from .utils_test import _test_update_deprecate
    from .utils_test import _test_enable
    from .utils_test import _test_disable
    from .utils_test import _test_mininterval
    from .utils_test import _test_miniters
    from .utils_test import _test_maxinterval
    from .utils_test import _test_color_strs
    from .utils_test import _test_ascii_strs
    from .utils_test import _test_unicode_strs
    from .utils_test import _test

# Generated at 2022-06-14 13:31:45.823236
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    message_id = None
    for i in range(10):
        if i % 2 == 0:
            iter = TelegramIO(
                token=getenv('TQDM_TELEGRAM_TOKEN'),
                chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'))
            message_id = iter.message_id
        else:
            iter = TelegramIO(
                token=getenv('TQDM_TELEGRAM_TOKEN'),
                chat_id=getenv('TQDM_TELEGRAM_CHAT_ID'))
            message_id = iter.message_id
            iter.write("test")
    return message_id


# Generated at 2022-06-14 13:31:56.312326
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """Unit test for tqdm_telegram.close()"""
    # TODO: update assertion message to a fixed expected message
    try:
        import pytest
        from tqdm.std import tqdm as tqdm_std
        from tqdm.auto import tqdm as tqdm_auto
    except ImportError:
        return
    tgrange = ttgrange
    

# Generated at 2022-06-14 13:32:03.275487
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    import time

    tk = '123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    ch = '1111111111'
    for i in tqdm_telegram(range(5), token=tk, chat_id=ch):
        time.sleep(0.01)
    for i in tqdm_telegram(range(5), disable=True, token=tk, chat_id=ch):
        time.sleep(0.01)

# Generated at 2022-06-14 13:32:06.438185
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm_telegram(token='211957063:AAEdZfOQ2WK9Xnt_eJd6Gz3qU5W6U5ec6aA', chat_id='75943746', miniters=1)
    t.close()

# Generated at 2022-06-14 13:32:14.272883
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    class TelegramIO_mock(TelegramIO):
        def __init__(self, token, chat_id):
            self.write_params = []
            super(TelegramIO_mock, self).__init__(token, chat_id)

        def write(self, s):
            self.write_params.append(s)

    io_obj = TelegramIO_mock("token", "chat_id")

    io_obj.write("123")
    assert io_obj.write_params == ["123"]

    io_obj.write("abc")
    assert io_obj.write_params == ["123", "abc"]

    io_obj.write("1234567890"*100)

# Generated at 2022-06-14 13:32:20.053421
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import io
    import sys
    import time
    sys.stdout = io.StringIO()
    for i in tqdm(range(5)):
        time.sleep(0.1)
    assert sys.stdout.getvalue().count('\x1b') == 17
    sys.stdout.truncate(0)
    for i in tqdm(range(5)):
        time.sleep(0.1)
        tqdm.clear()
    assert sys.stdout.getvalue().count('\x1b') == 1

# Generated at 2022-06-14 13:32:26.595947
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = getenv('TQDM_TELEGRAM_TOKEN', '123456789:aBcDeFgHiJkLmNoPqRsT')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID', '@tqdml')
    msg = TelegramIO(token, chat_id)
    msg.delete()

# Generated at 2022-06-14 13:32:33.868312
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    """
    Test function for method close of class tqdm_telegram.

    Test cases:
    * Test error case when TelegramIO is not initialized;
    * Test simple case when TelegramIO is initialized;
    * Test case when TelegramIO is initialized and leave=True;
    """
    # Test error case when TelegramIO is not initialized
    test_tqdm_telegram_obj = tqdm_telegram(
        range(1),
        desc='Test error case when TelegramIO is not initialized',
        disable=True)
    test_tqdm_telegram_obj.close()

    # Test simple case when TelegramIO is initialized
    test_tqdm_telegram_obj = tqdm_telegram(
        range(1),
        desc='Test simple case when TelegramIO is initialized')
    test_tqdm_telegram

# Generated at 2022-06-14 13:35:55.777735
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    import os
    os.environ['TQDM_TELEGRAM_TOKEN'] = '123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    os.environ['TQDM_TELEGRAM_CHAT_ID'] = '123456789'
    tqdm_telegram(
        [1, 2, 3], bar_format="{percentage:.0f}% - {bar} - {n}/{total}", unit_scale=True)

# Generated at 2022-06-14 13:35:58.261684
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    # Create the instance
    # Note: the telegram chat_id is the telegram bot under test chat_id
    instance = TelegramIO('telegram_token', 'telegram_chat_id')
    # Call the class method
    instance.delete()

# Generated at 2022-06-14 13:35:59.909799
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    with ttgrange(10) as x:
        pass
    assert isinstance(x, tqdm_telegram)

# Generated at 2022-06-14 13:36:01.869868
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    t = tqdm_telegram(_range(10), disable=True)
    t.close()



# Generated at 2022-06-14 13:36:03.516796
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    io = TelegramIO("", "")
    io.delete()

# Generated at 2022-06-14 13:36:13.231636
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """
    Tests that the `display` method of `tqdm_telegram` does not raise
    any exception.
    """
    from tqdm.auto import tqdm
    from tqdm.contrib.telegram import tqdm_telegram
    from tqdm.tests.utils import _suppress_stdout

    for i in tqdm(_range(10), desc="test_tqdm_telegram_display",
                  disable=None):
        pass
    for i in tqdm(_range(10), desc="test_tqdm_telegram_display",
                  file=tqdm_telegram("dummy")):
        pass

# Generated at 2022-06-14 13:36:19.679273
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .utils_test import _set_docstring, _suppress_stdout, _range_of_tests

    try:
        for _ in tqdm(_range_of_tests):
            pass
    except NameError:  # <- name not defined
        # Maybe no token is set
        return

    with _suppress_stdout():
        t = tqdm(total=1)
        _set_docstring(t, tqdm.__doc__)
        t.close()
        _set_docstring(t, tqdm_telegram.__doc__)



# Generated at 2022-06-14 13:36:29.173858
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """
    test for method display of class tqdm_telegram
    """
    from os import getenv
    from tqdm.contrib.test_utils import unittest
    from tqdm import tqdm

    @unittest.skipIf(getenv('TQDM_TELEGRAM_TOKEN') is None, 'No Telegram token')
    @unittest.skipIf(getenv('TQDM_TELEGRAM_CHAT_ID') is None, 'No Telegram chat ID')
    def test_tqdm_telegram_display_token_env_var(self):
        '''
        tests that tqdm_telegram's update fct is called
        '''

# Generated at 2022-06-14 13:36:30.458382
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    __test_close(tqdm_telegram)

# Generated at 2022-06-14 13:36:37.495960
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    # Arrange
    import os, sys
    tgio = TelegramIO(os.getenv('TQDM_TELEGRAM_TOKEN'), os.getenv('TQDM_TELEGRAM_CHAT_ID'))
    tqdm_telegram.clear(tgio, None, None, None)
    # Act
    tqdm_telegram.write(tgio, 'A')
    tqdm_telegram.clear(tgio, None, None, None)
    tqdm_telegram.write(tgio, 'A')
    try:
        tqdm_telegram.delete(tgio)
    except Exception as e:
        pass
    # Assert
    tqdm_telegram.join(tgio)