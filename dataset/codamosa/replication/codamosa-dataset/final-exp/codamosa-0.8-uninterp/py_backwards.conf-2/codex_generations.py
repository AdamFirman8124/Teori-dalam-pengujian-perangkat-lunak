

# Generated at 2022-06-14 01:22:15.798178
# Unit test for function init_settings
def test_init_settings():
    argparse_args = Namespace(debug=True)
    init_settings(argparse_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:20.070770
# Unit test for function init_settings
def test_init_settings():
  args = Namespace(debug = True)
  init_settings(args)
  assert settings.debug == True




# Generated at 2022-06-14 01:22:22.539291
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:22:24.674124
# Unit test for function init_settings
def test_init_settings():
    args = Namespace
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:26.979600
# Unit test for function init_settings
def test_init_settings():
    args=Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True


# Generated at 2022-06-14 01:22:29.325919
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:34.568804
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:37.748079
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:22:40.068761
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:44.957867
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    old_debug = settings.debug
    init_settings(args)
    assert settings.debug != old_debug
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == old_debug




# Generated at 2022-06-14 01:22:50.513664
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True
    init_settings(Namespace(debug=False))
    assert settings.debug == False

# Generated at 2022-06-14 01:22:56.676821
# Unit test for function init_settings
def test_init_settings():
    """
    Ensure debug settings is set to true or false using command line arguments
    """
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False


test_init_settings()

# Generated at 2022-06-14 01:22:59.783758
# Unit test for function init_settings
def test_init_settings():
    fake_args = Namespace(debug=True)
    init_settings(fake_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:03.240480
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:23:07.466439
# Unit test for function init_settings
def test_init_settings():
    arg_test = Namespace(debug = True)
    init_settings(arg_test)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:14.078604
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

# Generated at 2022-06-14 01:23:16.530637
# Unit test for function init_settings
def test_init_settings():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true')

    init_settings(parser.parse_args(['--debug']))
    assert settings.debug

# Generated at 2022-06-14 01:23:22.055093
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = False)
    init_settings(args)
    assert settings.debug == False
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:23:25.729000
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:31.449587
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug


if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:23:40.589495
# Unit test for function init_settings
def test_init_settings():
    # args set to --debug
    args = Namespace(debug=True)

    # use init_settings on the args, should set debug to true
    init_settings(args)

    assert settings.debug == True
    print("test_init_settings passed")

test_init_settings()

# Generated at 2022-06-14 01:23:42.720252
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:46.351916
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug = False)
    init_settings(args)
    assert settings.debug == False

# test_init_settings()

# Generated at 2022-06-14 01:23:49.721694
# Unit test for function init_settings
def test_init_settings():
    import os

    def get_args(args):
        parser = make_parser()
        return parser.parse_args(args)

    settings.debug = False
    init_settings(get_args([]))
    assert not settings.debug
    settings.debug = False
    init_settings(get_args(['--debug']))
    assert settings.debug

# Generated at 2022-06-14 01:23:53.035194
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:57.067502
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    args.debug = False
    init_settings(args)

# Generated at 2022-06-14 01:24:00.044134
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:05.705407
# Unit test for function init_settings
def test_init_settings():
    expected = True
    settings.debug = False
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action="store_true", help="Debug mode")
    args = parser.parse_args(['--debug'])
    init_settings(args)
    actual = settings.debug
    assert expected == actual

# Generated at 2022-06-14 01:24:08.745283
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:10.597978
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:25.700195
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:24:29.222368
# Unit test for function init_settings
def test_init_settings():
    mock_args = MagicMock()
    mock_args.debug = True
    init_settings(mock_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:33.319819
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert not settings.debug
    args.debug = True
    init_settings(args)
    assert settings.debug

if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:24:35.351745
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:37.386527
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)

    assert settings.debug

# Generated at 2022-06-14 01:24:41.300994
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:24:44.437152
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:48.016267
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:50.728050
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    arg_namespace = Namespace(debug=True)
    init_settings(arg_namespace)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:55.377347
# Unit test for function init_settings
def test_init_settings():
    args = ArgParser().parse_args([])
    init_settings(args)
    assert not settings.debug
    args = ArgParser().parse_args(['--debug'])
    init_settings(args)
    assert settings.debug


# Generated at 2022-06-14 01:25:16.923464
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:18.576428
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:25:25.954750
# Unit test for function init_settings
def test_init_settings():
    class FakeArgparse:
        def __init__(self, debug: bool) -> None:
            self.debug = debug
    class TestSettings:
        def __init__(self) -> None:
            self.debug = False
    test_settings = TestSettings()
    args = FakeArgparse(debug=True)
    init_settings(args)
    assert test_settings.debug == settings.debug

# Generated at 2022-06-14 01:25:28.025639
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:34.217103
# Unit test for function init_settings
def test_init_settings():
    # Set up parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true')
    cmd_args = parser.parse_args()

    init_settings(cmd_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:36.615316
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:39.251975
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug is False
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:25:43.235955
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:25:47.760942
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:25:53.504158
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--debug", action="store_true",
                    help="Turn on debug mode")
    args = ap.parse_args()
    init_settings(args)
    print(settings.debug)

# Generated at 2022-06-14 01:26:17.186270
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()

    args.debug = False
    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

test_init_settings()

# Generated at 2022-06-14 01:26:19.392531
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:23.708935
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:26:27.862580
# Unit test for function init_settings
def test_init_settings():
    unit_test_args = Namespace(debug=True)
    init_settings(unit_test_args)
    assert settings.debug is True

# Generated at 2022-06-14 01:26:30.677290
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:35.545976
# Unit test for function init_settings
def test_init_settings():
    import argparse
    mock_args = argparse.Namespace(debug=['True'])
    init_settings(mock_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:38.437507
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:44.107819
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    # A test to check if init_settings sets the debug to True
    args.debug = True
    init_settings(args)
    assert settings.debug
    # A test to check if init_settings sets the debug to False
    args.debug = False
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:26:45.674161
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
 

# Generated at 2022-06-14 01:26:51.096427
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:27:39.194656
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug == True
    # Second test
    settings.debug = False
    test_args = Namespace(debug=False)
    init_settings(test_args)
    assert settings.debug == False

# Generated at 2022-06-14 01:27:40.674429
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:27:46.354878
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True
    init_settings(test_args)
    assert settings.debug is True

# Generated at 2022-06-14 01:27:51.553398
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:27:55.020721
# Unit test for function init_settings
def test_init_settings():
    a = ArgumentParser()
    a.add_argument("--debug", action="store_true")
    args = a.parse_args(["--debug"])
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:28:00.050759
# Unit test for function init_settings
def test_init_settings():
    class Args:
        debug = False
    args = Args()
    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:02.111292
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:28:05.807958
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert(settings.debug == False)
    args.debug = True
    init_settings(args)
    assert(settings.debug == True)

# Generated at 2022-06-14 01:28:07.860612
# Unit test for function init_settings
def test_init_settings():
    def cc():
        pass

    args = Namespace(debug=True)

    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:28:11.528645
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    # assert settings.debug == False

# Generated at 2022-06-14 01:28:57.812985
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:28:59.259238
# Unit test for function init_settings
def test_init_settings():
    settings = init_settings()
    assert settings.debug == False

# Generated at 2022-06-14 01:29:02.756760
# Unit test for function init_settings
def test_init_settings():
    parser = create_parser()
    args = parser.parse_args("test -d true".split())
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:29:16.974411
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Notes - using Python argparse for command line arguments
# for when I want to run a script from the command line
# but I am also using Pycharm, where I am using argparse for help messages
# and not for the command line arguments
# I just copied this from the argparse tutorial.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# Generated at 2022-06-14 01:29:18.134864
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:29:21.591868
# Unit test for function init_settings
def test_init_settings():
    class Args:
        def __init__(self, debug: bool) -> None:
            self.debug = debug
    def set_debug(debug: bool) -> None:
        settings.debug = debug
    print_debug = settings.debug
    init_settings(Args(False))
    print_debug = settings.debug
    init_settings(Args(True))
    print_debug = settings.debug



# Generated at 2022-06-14 01:29:25.023101
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:29:28.545243
# Unit test for function init_settings
def test_init_settings():
    Mod = Namespace()
    Mod.debug = 'Debug'
    init_settings(Mod)
    assert settings.debug

# Generated at 2022-06-14 01:29:31.647731
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = "True"
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:29:33.975588
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(log_file="testfile.txt", debug=True)
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:30:23.874448
# Unit test for function init_settings
def test_init_settings():
    # Arrange
    args = Namespace()
    args.debug = True
    local_settings = Settings()

    # Act
    init_settings(args)

    # Assert
    assert local_settings.debug == True


if __name__ == "__main__":
    # Test code
    test_init_settings()
    pass

# Generated at 2022-06-14 01:30:26.962279
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:30:30.150629
# Unit test for function init_settings
def test_init_settings():
    args = argparse.Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:30:32.717839
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:30:35.485544
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:30:38.000879
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True



# Generated at 2022-06-14 01:30:44.127125
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False



# Generated at 2022-06-14 01:30:48.174552
# Unit test for function init_settings
def test_init_settings():
    testargs1 = Namespace(debug=True)

    init_settings(testargs1)

    assert settings.debug == True

    testargs2 = Namespace(debug=False)

    init_settings(testargs2)

    assert settings.debug == False

# Generated at 2022-06-14 01:30:52.580865
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug


# TODO: have the parser return a Settings object, which allows keeping the init_settings
# function without the need for a global variable...

# Generated at 2022-06-14 01:30:56.790403
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True