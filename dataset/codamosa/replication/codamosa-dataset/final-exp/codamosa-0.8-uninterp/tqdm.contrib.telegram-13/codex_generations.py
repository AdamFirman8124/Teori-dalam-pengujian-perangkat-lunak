

# Generated at 2022-06-14 13:31:07.062126
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    # Test if clear method doesn't cause a bug if it gets called during iteration
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    for i in tqdm(range(10), token=token, chat_id=chat_id):
        if i > 5:
            tqdm.clear()


if __name__ == '__main__':
    test_tqdm_telegram_clear()

# Generated at 2022-06-14 13:31:11.262983
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = 'token'
    chat_id = 'chat_id'
    tgio = TelegramIO(token, chat_id)
    tgio.message_id = 0  # Set a message_id in order to test
    tgio.delete()

# Generated at 2022-06-14 13:31:21.426760
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    import unittest

    class TestTelegramIO(unittest.TestCase):
        def setUp(self):
            self.tgio = TelegramIO('token', 'chat_id')

        def tearDown(self):
            self.tgio.close()

        def test_write(self):
            self.tgio.write('hello')
            self.assertEqual(self.tgio.text, 'hello')
            self.tgio.write('')
            self.assertEqual(self.tgio.text, '...')
            self.tgio.write('\n')
            self.assertEqual(self.tgio.text, '...')
            self.tgio.write('bye\r')
            self.assertEqual(self.tgio.text, 'bye')

# Generated at 2022-06-14 13:31:32.230644
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    # __init__
    # display
    # close
    import os
    import re
    import shutil
    import sys
    import time

    from tqdm import __version__

    try:
        import pytest
    except ImportError:
        pass
    else:
        sys.exit(pytest.main(['--verbose', __file__]))


# Generated at 2022-06-14 13:31:33.109518
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    import warnings

# Generated at 2022-06-14 13:31:43.807661
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    test_tqdm_telegram = tqdm_telegram(range(10), mininterval=0.1)
    test_tqdm_telegram.close()
    assert test_tqdm_telegram.tgio.message_id is not None
    assert test_tqdm_telegram.tgio.text == '10/10'

    # test_tqdm_telegram_disable = tqdm_telegram(range(10), mininterval=0.1,
    #                                            disable=True)
    # test_tqdm_telegram_disable.close()
    # assert test_tqdm_telegram_disable.tgio.message_id is None
    # assert test_tqdm_telegram_disable.tgio.text == '10/10'



# Generated at 2022-06-14 13:31:50.103927
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    from .tests_tqdm import pretest_posttest  # import as self
    with pretest_posttest(False):
        assert tqdm_telegram(disable=True).disable
        assert tqdm_telegram(disable=False, bar_format="").disable
        with tqdm_telegram(disable=False) as pbar:
            assert isinstance(pbar, tqdm_auto)
            assert isinstance(pbar.tgio, TelegramIO)

# Generated at 2022-06-14 13:31:53.210422
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    it = tqdm_telegram(range(10), token='{token}', chat_id='{chat_id}')
    for _ in it:
        pass

# Generated at 2022-06-14 13:31:56.962316
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    
    # Setup
    tg = TelegramIO(token='token', chat_id='chat_id')
    tg._message_id = '1'
    res = tg.delete()
    
    # Assertion
    assert res.json() == {'ok': True, 'result': True}



# Generated at 2022-06-14 13:32:00.070266
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    msg = TelegramIO(getenv('TQDM_TELEGRAM_TOKEN'),
                     getenv('TQDM_TELEGRAM_CHAT_ID'))
    str_msg = 'Hello, World!'
    msg.text = str_msg
    msg.write(str_msg)



# Generated at 2022-06-14 13:34:23.200927
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    import sys

    fobj = open(sys.argv[1], 'w')
    # Test all arguments

# Generated at 2022-06-14 13:34:25.250875
# Unit test for constructor of class tqdm_telegram
def test_tqdm_telegram():
    with tqdm_telegram(total=1) as pbar:
        pbar.update(1)
    assert pbar.tgio.text == "100%"

# Generated at 2022-06-14 13:34:27.467951
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    bar = tqdm(
        [1, 2, 3], token='{token}', chat_id='{chat_id}', leave=False)
    for _ in bar:
        bar.set_description("test_tqdm_telegram_clear")
        bar.clear()
    bar.close()

# Generated at 2022-06-14 13:34:29.801398
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .utils_test import _test_display
    _test_display(tqdm_telegram)

# Generated at 2022-06-14 13:34:33.319701
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    tqdm_telegram(range(10)).close()
    tqdm_telegram(range(10), leave=True).close()
    tqdm_telegram(range(10), leave=False).close()
    tqdm_telegram(range(10), leave=None).close()

# Generated at 2022-06-14 13:34:43.349714
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from .tests.telegram_token import token, chat_id
    from .tests.utils import FakeTqdmFile
    with FakeTqdmFile(hide=True) as fake:
        t = tqdm(total=4, file=fake, token=token, chat_id=chat_id)
        t.update(2)
        t.update()
        t.update(3)
        t.update()
        t.close()
    output = fake.read()
    assert ("\r  0%|          | 0/4 [00:00<?, ?it/s]\n" in output)
    assert ("\r 50%|█████     | 2/4 [00:00<?, ?it/s]\n" in output)

# Generated at 2022-06-14 13:34:48.892321
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    # Initialize tqdm and set its flag self.leave as True
    tt = tqdm(total=0)
    tt.leave = True
    # Initialize TelegramIO
    tt.tgio = TelegramIO("00", "00")
    # Set TelegramIO's message_id as None
    tt.tgio._message_id = None
    # Run close function
    tt.close()
    # Check if the message_id is not deleted (since the flag .leave is True)
    assert tt.tgio.message_id is None

# Generated at 2022-06-14 13:34:56.313358
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    """Test method display of class tqdm_telegram."""
    import os
    os.environ['TQDM_TELEGRAM_TOKEN'] = '{token}'
    os.environ['TQDM_TELEGRAM_CHAT_ID'] = '{chat_id}'
    with tqdm_telegram(total=10000, ncols=0) as t:
        for i in range(100):
            t.update(100)
###############################################################################
# END OF FILE
###############################################################################

# Generated at 2022-06-14 13:35:06.061849
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    import gc
    from tqdm.auto import tqdm
    
    # Initialize a tqdm object
    obj_tqdm = tqdm(list(range(10)))
    obj_tqdm.close()
    assert obj_tqdm.n != 0, \
        "Closing a tqdm object should not leave n to 0."
    
    # Initialize a tqdm_telegram object
    obj_tqdm_tg = tqdm_telegram(list(range(10)))
    del obj_tqdm_tg
    assert not obj_tqdm_tg.tgio.session._connection_pools, \
        "Leaving a tqdm_telegram object should close its session."
    gc.collect() # Force object collection

# Generated at 2022-06-14 13:35:10.051122
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    ttgrange(1, disable=True).close()
    with ttgrange(1) as t:
        t.close()
    with ttgrange(1, leave=True) as t:
        t.close()
    with ttgrange(1, leave=False) as t:
        t.close()