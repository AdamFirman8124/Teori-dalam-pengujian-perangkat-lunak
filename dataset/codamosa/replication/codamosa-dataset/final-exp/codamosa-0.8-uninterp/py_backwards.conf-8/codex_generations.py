

# Generated at 2022-06-14 01:22:13.341621
# Unit test for function init_settings
def test_init_settings():
    global settings
    settings = Settings()

    test1 = Namespace()
    test1.debug = True
    init_settings(test1)
    assert settings.debug == True

    test2 = Namespace()
    test2.debug = False
    init_settings(test2)
    assert settings.debug == False

# pytest -v -s test_settings.py



# Generated at 2022-06-14 01:22:17.667493
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug is True
    init_settings(Namespace(debug=False))
    assert settings.debug is False

# Generated at 2022-06-14 01:22:19.563783
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:23.058826
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False

    args = Namespace()
    args.debug = True
    ini

# Generated at 2022-06-14 01:22:27.877988
# Unit test for function init_settings
def test_init_settings():
    import argparse
    test_args = argparse.Namespace(debug=True)

    init_settings(test_args)
    assert settings.debug


if __name__ == "__main__":

    try:
        import pytest
        pytest.main(["-s", "tests/"])
    except ImportError:
        # print("Warning: pytest is not installed. Tests are skipped")
        pass

# Generated at 2022-06-14 01:22:30.092914
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:22:32.329380
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:22:34.790303
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:46.266865
# Unit test for function init_settings
def test_init_settings():
    fmt = "Could not set settings.{}"
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args([])
    init_settings(args)
    try:
        assert not settings.debug
    except AssertionError as e:
        print(fmt.format("debug"))
        raise e
    args = parser.parse_args(['-d'])
    init_settings(args)
    try:
        assert settings.debug
    except AssertionError as e:
        print(fmt.format("debug"))
        raise e
    print("test_init_settings: PASS")


# Generated at 2022-06-14 01:22:48.914872
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True, host="localhost", port=65432)
    init_settings(args)

    assert settings.debug == True
    assert settings.debug == False

# Generated at 2022-06-14 01:22:55.586047
# Unit test for function init_settings
def test_init_settings():
    fake_args = Namespace(debug=True)
    init_settings(fake_args)
    assert settings.debug

# Generated at 2022-06-14 01:22:58.944311
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True
    init_settings(test_args)

    assert settings.debug == True

# Generated at 2022-06-14 01:23:02.176949
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:11.703281
# Unit test for function init_settings
def test_init_settings():
    # Test all combinations of set and unset arguments
    np.testing.assert_equal(settings.debug, False)
    init_settings(Namespace(debug=False))
    np.testing.assert_equal(settings.debug, False)
    init_settings(Namespace(debug=True))
    np.testing.assert_equal(settings.debug, True)
    init_settings(Namespace(debug=False))
    np.testing.assert_equal(settings.debug, False)
    init_settings(Namespace(debug=True))
    np.testing.assert_equal(settings.debug, True)

# Generated at 2022-06-14 01:23:13.734637
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:18.076022
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert_true(settings.debug)

    args = Namespace(debug=False)
    init_settings(args)
    assert_false(settings.debug)

# Generated at 2022-06-14 01:23:20.308325
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:23.113139
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:27.060167
# Unit test for function init_settings
def test_init_settings():
    arguments = Namespace()
    arguments.debug = True
    init_settings(arguments)
    assert settings.debug == True
    arguments.debug = False
    init_settings(arguments)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:28.696297
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:23:38.589333
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:42.151328
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    print("Unit test for function init_settings passed")


if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:23:44.574375
# Unit test for function init_settings
def test_init_settings():
    class Args:
        debug = False
    init_settings(Args)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:45.954748
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:23:47.896929
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:51.191285
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:57.989894
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    settings.debug = False
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    settings.debug = False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:59.169314
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_s

# Generated at 2022-06-14 01:24:05.214779
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:07.405631
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:18.266998
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:24:21.237210
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:26.115895
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:28.858729
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True
    args.debug = False
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:24:32.638874
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug = False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:24:38.366039
# Unit test for function init_settings
def test_init_settings():
    # Initialize settings.
    settings = Settings()
    args = Namespace(debug=True)
    init_settings(args)
    # Confirm initialization.
    assert settings.debug

# Generated at 2022-06-14 01:24:43.962915
# Unit test for function init_settings
def test_init_settings():
    class Arg:
        debug = 1
    args = Arg()
    init_settings(args)
    assert settings.debug == True
    args.debug = 0
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:47.390325
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()

    init_settings(args)
    assert settings.debug is False

    args.debug = True

    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:59.501144
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    setattr(args, 'debug', True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace()
    setattr(args, 'debug', False)
    init_settings(args)
    assert settings.debug == False
    args = Namespace()
    init_settings(args)
    assert settings.debug == False


if __name__ == '__main__':
    args = Namespace()
    setattr(args, 'debug', True)
    init_settings(args)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG if settings.debug else logging.INFO)
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)
    logger.info('program started')
    logger

# Generated at 2022-06-14 01:25:03.160623
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False