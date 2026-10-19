

# Generated at 2022-06-14 01:21:54.332959
# Unit test for function init_settings
def test_init_settings():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true', default=False)
    args = parser.parse_args()

    init_settings(args)

    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:21:58.274753
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default=False, action='store_true', help="turn on debug")
    test_args = parser.parse_args()
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:02.656504
# Unit test for function init_settings
def test_init_settings():
    # Test default values
    init_settings(Namespace())
    assert settings.debug == False

    # Test with actual value
    init_settings(Namespace(**{'debug': True}))
    assert settings.debug == True

# Generated at 2022-06-14 01:22:07.845423
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--debug',
        action="store_true",
        help='Print debug information'
    )
    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:13.733070
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    ns = parser.parse_args([])
    init_settings(ns)
    assert not settings.debug
    ns = parser.parse_args(['--debug'])
    init_settings(ns)
    assert settings.debug


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:22:16.905398
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:18.820916
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:20.607290
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug==True

# Generated at 2022-06-14 01:22:22.022858
# Unit test for function init_settings
def test_init_settings():
    #Calling function
    init_settings(args)
    #Checking
    assert settings.debug == False

# Function get_args

# Generated at 2022-06-14 01:22:24.945936
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true",
                        help="debug mode")
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:29.266124
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))

    assert(settings.debug == True)

# Generated at 2022-06-14 01:22:34.791124
# Unit test for function init_settings
def test_init_settings():
    settings.debug = True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:22:45.361296
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    parser = ArgumentParser(description='Settings')
    parser.add_argument('-d', '--debug', default=False, action='store_true', help='Debug')
    args = parser.parse_args([])
    init_settings(args)
    assert settings.debug is False
    settings.debug = False
    parser = ArgumentParser(description='Settings')
    parser.add_argument('-d', '--debug', default=False, action='store_true', help='Debug')
    args = parser.parse_args(['-d'])
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:22:47.427195
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:22:49.644801
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:22:51.516198
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug='True')
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:56.929636
# Unit test for function init_settings
def test_init_settings():
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--debug', dest='debug', action='store_true', default=False)
        return parser.parse_args()

    args = get_args()
    init_settings(args)
    assert settings.debug is False

    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:00.704874
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    assert not settings.debug is False

# Generated at 2022-06-14 01:23:05.953107
# Unit test for function init_settings
def test_init_settings():
    class Args:
        def __init__(self) -> None:
            self.debug = False
    args = Args()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:07.352697
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)

    assert settings.debug == args.debug

# Generated at 2022-06-14 01:23:19.775517
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug is False

    args.debug = True
    init_settings(args)
    assert settings.debug is True


# Default settings (farmer)
# Only overwrite these settings once they're in the database
#
# The settings below have defaults that depend on other settings
#
# The settings that have defaults should be placed at the bottom
# of the file.

# Generated at 2022-06-14 01:23:21.144740
# Unit test for function init_settings
def test_init_settings():
    init_settings(args=Namespace(debug=True))
    assert settings.debug is True

# Generated at 2022-06-14 01:23:24.856238
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace())
    assert not settings.debug

    init_settings(Namespace(debug = True))
    assert settings.debug

# Generated at 2022-06-14 01:23:27.554341
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug
    init_settings(Namespace(debug=False))
    assert not settings.debug

# Generated at 2022-06-14 01:23:29.633764
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:31.593141
# Unit test for function init_settings
def test_init_settings():
    setattr(settings, 'debug', False)
    init_settings(Namespace(debug=False))
    assert settings.debug == False


# Generated at 2022-06-14 01:23:37.381198
# Unit test for function init_settings
def test_init_settings():
    arg_namespace = Namespace()
    arg_namespace.debug = False
    init_settings(arg_namespace)
    assert settings.debug == False

    arg_namespace = Namespace()
    arg_namespace.debug = True
    init_settings(arg_namespace)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:39.754642
# Unit test for function init_settings
def test_init_settings():
    args: Namespace = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:41.622163
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
  

# Generated at 2022-06-14 01:23:44.526280
# Unit test for function init_settings
def test_init_settings():
    result = Namespace(debug=True)
    init_settings(result)
    assert settings.debug

# Generated at 2022-06-14 01:23:55.788545
# Unit test for function init_settings
def test_init_settings():
    input_args = Namespace(debug=False)
    ini

# Generated at 2022-06-14 01:23:58.428995
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug

# Generated at 2022-06-14 01:24:02.177281
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    args.music_dir = '/home/mukund/Documents/'
    init_settings(args)
    assert(settings.debug == True)

# Generated at 2022-06-14 01:24:05.458201
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=False))
    assert not settings.debug

    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:24:08.573012
# Unit test for function init_settings
def test_init_settings():
    parser = ArgumentParser(prog='test_init_test')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    init_settings(args)

# Generated at 2022-06-14 01:24:10.221455
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug


test_init_settings()

# Generated at 2022-06-14 01:24:11.868597
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:14.839907
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

    # test_init_settings()

# Generated at 2022-06-14 01:24:18.365899
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:24:21.317710
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:43.539380
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    assert not settings.debug
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:47.656280
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    init_settings(Namespace(debug=True))
    assert settings.debug == True
    settings.debug = False
    init_settings(Namespace(debug=False))
    assert settings.debug == False

# Generated at 2022-06-14 01:24:48.939690
# Unit test for function init_settings
def test_init_settings():
    arg = argparse.Namespace(debug=True)
    init_settings(arg)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:51.482084
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug=True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:59.462850
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    init_settings(Namespace(debug=True))
    assert settings.debug == True


if __name__ == "__main__":
    parser = ArgumentParser(description="Debug setting")
    parser.add_argument(
        "--debug",
        dest="debug",
        action="store_true"
    )
    args = parser.parse_args()
    init_settings(args)
    if settings.debug:
        print("In debug mode")
    else:
        print("Not in debug mode")

# Generated at 2022-06-14 01:25:01.617345
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug is True

# Generated at 2022-06-14 01:25:05.466623
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:25:07.586592
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False, foo="bar")
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:25:14.477893
# Unit test for function init_settings
def test_init_settings():
    # Set the global variable settings.debug to False
    settings.debug = False
    # Test with args.debug set to True
    args_debug = Namespace(debug=True)
    init_settings(args_debug)
    assert(settings.debug)
    # Test with args.debug set to False
    args_debug = Namespace(debug=False)
    init_settings(args_debug)
    assert(not settings.debug)

# Generated at 2022-06-14 01:25:15.662692
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:25:59.490846
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True
    assert settings.debug == True

# Generated at 2022-06-14 01:26:01.478591
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True



# Generated at 2022-06-14 01:26:04.039374
# Unit test for function init_settings
def test_init_settings():
    # TODO: fix unit test for init_settings
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug, 'Debug mode enabled'

# Generated at 2022-06-14 01:26:09.120676
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False,
                     hmmfile=None,
                     libpath=None,
                     mode=None,
                     output=None,
                     species=None,
                     taxonomy=None,
                     threads=None)
    init_settings(args)
    assert settings.debug == False



# Generated at 2022-06-14 01:26:14.971673
# Unit test for function init_settings
def test_init_settings():
    # Test 1: default setting
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True
    # Test 2: debug = False
    args = Namespace(debug = False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:26:18.394618
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug

# Generated at 2022-06-14 01:26:23.148125
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert(settings.debug)

# Generated at 2022-06-14 01:26:28.013138
# Unit test for function init_settings
def test_init_settings():
    class ArgNamespace:
        def __init__(self) -> None:
            self.debug = True

    args = ArgNamespace()
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:32.759348
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:35.025875
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert set

# Generated at 2022-06-14 01:28:02.820227
# Unit test for function init_settings
def test_init_settings():
    # Preprocessing
    args = Namespace()
    args.debug = True

    # Execution
    init_settings(args)

    # Assertions
    assert settings.debug == True

# Generated at 2022-06-14 01:28:05.370950
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:07.080110
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is not False

# Generated at 2022-06-14 01:28:11.275765
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:15.757051
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:28:19.517148
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False, verbose=False)
    init_settings(args)
    assert settings.debug == False



# Generated at 2022-06-14 01:28:24.943853
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    # test debug on
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    # test debug off
    args.debug = False
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:28:28.632962
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug is True
    settings.debug = False

# Generated at 2022-06-14 01:28:34.434100
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug is False
    args.debug = True
    init_settings(args)
    assert settings.debug is True

if __name__ == '__main__':
    print('1')
    test_init_settings()
    print('2')

# Generated at 2022-06-14 01:28:35.860898
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:31:32.443189
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    assert settings.debug == False
    init_settings(args)
    assert settings.debug == False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:31:34.223166
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:31:36.543115
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug
    init_settings(Namespace(debug=False))
    assert not settings.debug

# Generated at 2022-06-14 01:31:38.040940
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:31:43.931897
# Unit test for function init_settings
def test_init_settings():
    set_args = Namespace(debug=True)
    init_settings(set_args)
    assert(settings.debug == True)

    set_args = Namespace(debug=False)
    init_settings(set_args)
    assert(settings.debug == False)

# Generated at 2022-06-14 01:31:45.418538
# Unit test for function init_settings
def test_init_settings():
    args = NamedTuple(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:31:51.037655
# Unit test for function init_settings
def test_init_settings():
    args = MagicMock()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug