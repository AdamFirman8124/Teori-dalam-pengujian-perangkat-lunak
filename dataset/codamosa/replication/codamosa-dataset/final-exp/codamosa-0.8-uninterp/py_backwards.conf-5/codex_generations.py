

# Generated at 2022-06-14 01:22:09.906770
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:12.113539
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:17.557235
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:22:24.774375
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser(description='Pyton Client')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args([])
    init_settings(args)
    assert settings.debug is False

    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug is True

if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:22:26.699331
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:22:32.858010
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="display debug info", action="store_true")
    args = parser.parse_args(["-d"])
    init_settings(args)
    assert settings.debug is True

test_init_settings()

# Generated at 2022-06-14 01:22:35.803758
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False
    
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:40.427266
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args2 = Namespace(debug=False)
    init_settings(args2)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:46.874450
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug",
        action="count",
        default=0,
        help="Debug information")
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == False
    args.debug = 1
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:50.359263
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    init_settings(Namespace())
    assert not settings.debug

    settings.debug = False
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:22:56.950756
# Unit test for function init_settings
def test_init_settings():
    class Dummy:
        def __init__(self):
            self.debug = False

    dummy = Dummy()
    args = Namespace(debug=False)
    init_settings(args)
    assert dummy.debug == False

# Generated at 2022-06-14 01:23:01.484031
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True
    # Delete setting before next test
    del settings.debug


# Generated at 2022-06-14 01:23:04.100224
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:23:07.502563
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:10.538797
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert(settings.debug == True)



# Generated at 2022-06-14 01:23:13.165445
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:23:15.915128
# Unit test for function init_settings
def test_init_settings():
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:23:21.253364
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False

    init_settings(args)

    assert settings.debug == False

# Generated at 2022-06-14 01:23:24.614028
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug is True



# Generated at 2022-06-14 01:23:26.677579
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:23:35.721915
# Unit test for function init_settings
def test_init_settings():
    class Args:
        def __init__(self):
            self.debug = True
    assert settings.debug == False

    init_settings(Args())
    assert settings.debug == True

# Generated at 2022-06-14 01:23:38.889231
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:40.882868
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:46.313016
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:23:48.665781
# Unit test for function init_settings
def test_init_settings():
    args = parse_args([])
    init_settings(args)
    assert settings.debug == False

    args = parse_args(["--debug"])
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:53.612093
# Unit test for function init_settings
def test_init_settings():
    """
    This function tests the init_settings function
    """
    # create a fake argv for testing
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:57.841400
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

# Generated at 2022-06-14 01:24:00.387944
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:02.408148
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:07.015997
# Unit test for function init_settings
def test_init_settings():
    class MockArgs:
        def __init__(self) -> None:
            self.debug = True
    args = MockArgs()
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:21.559564
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False


if __name__ == '__main__':
    pytest.main()

# Generated at 2022-06-14 01:24:27.311020
# Unit test for function init_settings
def test_init_settings():
    def test_header(msg: str) -> None:
        if settings.debug:
            print(msg)

    test_header("Testing init_settings")
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False, "Debug not set in settings"
    print("Passed test_init_settings")


test_init_settings()

# Generated at 2022-06-14 01:24:31.953548
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:24:34.539562
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:36.981603
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert False == settings.debug

# Generated at 2022-06-14 01:24:39.284783
# Unit test for function init_settings
def test_init_settings():
    args = []
    args.append("--debug")
    args = Namespace(args)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:42.224402
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:24:43.691054
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:24:45.711234
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:49.488564
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False

    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:11.611947
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=False))
    assert not settings.debug



# Generated at 2022-06-14 01:25:13.839060
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:25:15.942822
# Unit test for function init_settings
def test_init_settings():
    global settings
    init_settings(Namespace(debug=True))
    assert settings.debug
    init_settings(Namespace(debug=False))
    assert not settings.debug

# Generated at 2022-06-14 01:25:17.419909
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert(settings.debug == True)

# Generated at 2022-06-14 01:25:24.028240
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False

    parser = init_parser()
    args = parser.parse_args([])
    assert args.debug == False

    parser = init_parser()
    args = parser.parse_args(["--debug"])
    assert args.debug == True

    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:25:26.402657
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:25:28.488238
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:33.557028
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:25:38.167700
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

    args = Namespace(debug=False)
    init_settings(args)
    

# Generated at 2022-06-14 01:25:40.690861
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:25.956457
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    settings.debug = False

    assert settings.debug is False



# Generated at 2022-06-14 01:26:27.338203
# Unit test for function init_settings

# Generated at 2022-06-14 01:26:29.383726
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:26:36.400994
# Unit test for function init_settings
def test_init_settings():
    # Init with false arguments
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

    # Init with true arguments
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:41.195674
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

if __name__ == "__main__":

    test_init_settings()

# Generated at 2022-06-14 01:26:43.139040
# Unit test for function init_settings
def test_init_settings():
    args = Mock()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:45.020675
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True



# Generated at 2022-06-14 01:26:47.226745
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:50.951162
# Unit test for function init_settings
def test_init_settings():
    # Create dummy arguments object
    dummy_args = Namespace()
    dummy_args.debug = True
    # Call unit
    init_settings(dummy_args)

    # Assert that setting is set correctly
    assert settings.debug is True

# Generated at 2022-06-14 01:26:52.364454
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True


# Generated at 2022-06-14 01:28:22.709902
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(logging='warning', debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:25.781618
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug
    assert not settings.debug


# Generated at 2022-06-14 01:28:29.627477
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug = True))
    assert settings.debug == True

# Generated at 2022-06-14 01:28:31.193835
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:28:35.142349
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:28:38.390313
# Unit test for function init_settings
def test_init_settings():
    args_ = Namespace(debug=True)
    init_settings(args_)
    assert settings.debug == True

if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:28:44.256575
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug

    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:28:46.960721
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:28:49.255631
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:28:51.336089
# Unit test for function init_settings
def test_init_settings():
    # Arrange
    args = Namespace()
    args.debug = True
    expected = True
    
    # Act
    init_settings(arg)
    
    # Assert
    assert settings.debug == expected

# Generated at 2022-06-14 01:31:54.892653
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace
    from pytest import approx
    from . import init_settings, settings

    before = settings.debug

    args = Namespace()
    init_settings(args=args)

    after = settings.debug

    assert after == before

    args = Namespace(debug=True)
    init_settings(args=args)

    after = settings.debug

    assert after != before

    args = Namespace(debug=False)
    init_settings(args=args)

    after = settings.debug

    assert after == before

# Generated at 2022-06-14 01:31:57.439047
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:32:01.530375
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true')
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:32:04.042193
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:32:07.210372
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug