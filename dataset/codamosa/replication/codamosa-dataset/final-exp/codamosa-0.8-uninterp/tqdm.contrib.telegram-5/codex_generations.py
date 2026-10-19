

# Generated at 2022-06-14 13:32:57.389931
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    test_token = '123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJ'
    test_chat_id = '123456789'
    telegram_io = TelegramIO(test_token, test_chat_id)
    # check if write() returns the correct future object
    test_message = 'test message'
    future = telegram_io.write(test_message)
    assert future.result().headers['Date']
    # check if write() returns None when there is a creation rate limit
    telegram_io.token = '987654321:ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJ'
    telegram_io._message_id = 123
    future = telegram_io.write(test_message)
    assert future is None



# Generated at 2022-06-14 13:32:59.730165
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    t = tqdm_telegram(total=10)
    t.clear()
    t.close()


# Generated at 2022-06-14 13:33:03.802549
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    tqdm_telegram.tgio.write = lambda message: True
    tqdm_telegram.tgio.delete = lambda: True
    tqdm_telegram([]).close()
    tqdm_telegram([]).close(True)
    tqdm_telegram([]).close(False)
    tqdm_telegram([]).close(None)

# Generated at 2022-06-14 13:33:12.324331
# Unit test for method write of class TelegramIO
def test_TelegramIO_write():
    # These values are not the real ones
    chat_id = "-123456789"
    token = "123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_id = 1234567890

    class TempSession(Session):
        def post(url, data):
            assert data == {'text': '`Message`', 'chat_id': chat_id,
                            'parse_mode': 'MarkdownV2'}
            return {
                       'ok': True, 'result': {'message_id': message_id}
                   }, None
    TelegramIO.session = TempSession()
    tgio = TelegramIO(token=token, chat_id=chat_id)
    tgio.write("Message")
    assert has

# Generated at 2022-06-14 13:33:20.553470
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from sys import stderr
    from io import StringIO
    from time import sleep

    # Reset stderr to the original one
    stderr_real = stderr
    stderr = StringIO()
    t = tqdm_telegram(total=10, unit='B', unit_scale=True, mininterval=0.)
    t.display()
    t.update(1)
    # Unit test
    assert "Elapsed: 0:00:00.000" in stderr.getvalue()
    t.display()
    t.update()
    sleep(1)
    t.display()
    t.update()
    sleep(1)
    t.display()
    t.update()
    sleep(1)
    t.display()
    t.update(1)
    t.display()


# Generated at 2022-06-14 13:33:22.464448
# Unit test for method clear of class tqdm_telegram
def test_tqdm_telegram_clear():
    from .tests_tqdm import pretest_posttest as test
    test(tqdm_telegram)

# Generated at 2022-06-14 13:33:25.040590
# Unit test for method close of class tqdm_telegram
def test_tqdm_telegram_close():
    for leave in [False, True]:
        with tqdm(leave=leave) as t:
            t.close()


# Generated at 2022-06-14 13:33:34.154235
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    t = tqdm_telegram("H", disable=True)
    t.total = 15
    t.display(bar_format="{l_bar}{bar:10u}{r_bar}")
    assert t.tgio.text == "H"

    t = tqdm_telegram("H", disable=True)
    t.total = 15
    t.display(bar_format="{l_bar}<{bar:10u}>{r_bar}")
    assert t.tgio.text == "H"

    t = tqdm_telegram("H", disable=True)
    t.total = 15
    t.display(bar_format="{l_bar}{bar:10u}<{r_bar}")
    assert t.tgio.text == "H"


# Generated at 2022-06-14 13:33:39.865963
# Unit test for method delete of class TelegramIO
def test_TelegramIO_delete():
    token = getenv('TQDM_TELEGRAM_TOKEN')
    chat_id = getenv('TQDM_TELEGRAM_CHAT_ID')
    assert token is not None and len(token) > 0
    assert chat_id is not None and len(chat_id) > 0
    tgio = TelegramIO(token, chat_id)
    if tgio.message_id is None:
        tqdm_auto.write("Message creation failed")
        return
    tqdm_auto.write("Message %d created" % tgio.message_id)
    tgio.delete()
    tqdm_auto.write("Message %d deleted" % tgio.message_id)
    return tgio

# Generated at 2022-06-14 13:33:47.961812
# Unit test for method display of class tqdm_telegram
def test_tqdm_telegram_display():
    from io import StringIO
    import sys

    def run(capture):
        # Initialize fake tqdm
        t = tqdm(total=11, postfix="test_tqdm_telegram_display",
                 bar_format='{postfix}: {bar:10.2f}%')
        # Fake tqdm should not be able to write
        try:
            t.write('test')
        except Exception:
            pass
        # Fake progress and display tqdm progress
        with capture:
            t.update()
            t.display()

    captured = StringIO()
    with tqdm_telegram.wrapattr(sys, "stdout", captured):
        run(captured)

    captured_no_disable = StringIO()