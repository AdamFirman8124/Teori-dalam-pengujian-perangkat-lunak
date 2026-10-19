

# Generated at 2022-06-14 01:22:16.683698
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:22:20.104314
# Unit test for function init_settings
def test_init_settings():
    test_settings = init_settings(Namespace(debug=True))
    assert settings.debug is True

# Generated at 2022-06-14 01:22:22.545094
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug

# Generated at 2022-06-14 01:22:26.343795
# Unit test for function init_settings
def test_init_settings():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--debug", help="Set debug mode on", action='store_true')

# Generated at 2022-06-14 01:22:27.808571
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:30.504833
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True


# Generated at 2022-06-14 01:22:33.348380
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:35.145826
# Unit test for function init_settings
def test_init_settings():
    # DEBUG is default False
    assert settings.debug == False


# Test command line argument "debug", set debug to True

# Generated at 2022-06-14 01:22:39.406829
# Unit test for function init_settings
def test_init_settings():
    class FakeArg:
        def __init__(self):
            self.debug = True
    fake_arg = FakeArg()
    init_settings(fake_arg)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:42.977092
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:49.245492
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:22:51.812254
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:22:56.028437
# Unit test for function init_settings
def test_init_settings():
    from unittest.mock import Mock
    args = Mock()
    args.debug = True
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:58.722982
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:04.333917
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)
    assert settings.debug

    args = Namespace()
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:23:08.995089
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--debug',
        action = 'store_true'
    )

    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug
    assert args.debug


# Generated at 2022-06-14 01:23:14.896116
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    assert not settings.debug
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug


if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:23:18.986756
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug is False
    args.debug = True
    init_settings(args)
    assert settings.debug is True

test_init_settings()

# Generated at 2022-06-14 01:23:27.727205
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False
    # See if settings.debug can be toggled with repeated function calls.
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:30.044528
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace
    args = Namespace(debug = True)
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:23:39.602790
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', help='Enable debug mode', action="store_true")
    init_settings(parser.parse_args(sys.argv[1:]))
    # main()



# Generated at 2022-06-14 01:23:41.866900
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:45.259790
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False


# Generated at 2022-06-14 01:23:47.551211
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True
    init_settings(Namespace(debug=False))
    assert settings.debug == False

# Generated at 2022-06-14 01:23:52.274573
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True, verbose=0)
    init_settings(args)
    assert settings.debug


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 01:24:01.953810
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="debug mode", action="store_true")
    args = parser.parse_args("--debug".split())
    init_settings(args)
    assert settings.debug == True
    args = parser.parse_args("".split())
    init_settings(args)
    assert settings.debug == False
    parser.add_argument("--debug", help="debug mode", action="store_false")


if __name__ == "__main__":
    test_init_settings()
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="debug mode", action="store_true")
    args = parser.parse_args()
    init_settings(args)
    print(settings.debug)

# Generated at 2022-06-14 01:24:04.728362
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:07.114945
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:10.647260
# Unit test for function init_settings
def test_init_settings():
    args_namespace = Namespace()
    args_namespace.debug = True

    init_settings(args_namespace)

    assert settings.debug, "debug setting is not set to True"

    args_namespace.debug = False

    init_settings(args_namespace)

    assert not settings.debug, "debug setting is not set to False"



# Generated at 2022-06-14 01:24:15.310524
# Unit test for function init_settings
def test_init_settings():
    """Test the init_settings function."""

    settings.debug = False

    class Args:
        debug = False

    init_settings(Args())
    assert settings.debug is False
    Args.debug = True

    init_settings(Args())
    assert settings.debug is True

# Generated at 2022-06-14 01:24:25.423711
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:27.146978
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:24:32.153621
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    assert settings.debug is False
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:34.763020
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:35.832184
# Unit test for function init_settings
def test_init_settings():
    # TODO
    pass

# Generated at 2022-06-14 01:24:39.029945
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug



# Generated at 2022-06-14 01:24:40.848672
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(
        debug=True
    )
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:42.675330
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = 'True')
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:45.852477
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args.debug = False
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:49.163996
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    assert settings.debug != False



# Generated at 2022-06-14 01:25:05.316404
# Unit test for function init_settings
def test_init_settings():
    cwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parser = argparse.ArgumentParser(description="Python Project",
                                     usage='''pytorch-pipeline <command> [<args>]

This program can be executed with following commands:
    run     Run a Python Project

''')
    parser.add_argument('command', help='Subcommand to run')
    args = parser.parse_args(['run'])
    print(cwd)
    init_settings(args)

    # assert settings.debug == True
    assert settings.debug == False

# Generated at 2022-06-14 01:25:08.597464
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:25:12.841806
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:25:14.717618
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:16.149176
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:17.620722
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:26.403882
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="Print debug messages to console", action="store_true")
    args = parser.parse_args()

    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:28.488071
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:33.757846
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

test_init_settings()

# Generated at 2022-06-14 01:25:39.054195
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=False)
    init_settings(test_args)
    assert settings.debug is False
    settings.debug = True
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug is True

# Generated at 2022-06-14 01:26:01.479284
# Unit test for function init_settings
def test_init_settings():
    settings = init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:26:03.329487
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:08.056249
# Unit test for function init_settings
def test_init_settings():
    # Test w/o debug
    args = Namespace(debug = False)
    init_settings(args)
    assert(settings.debug == False)

    # Test debug
    args = Namespace(debug = True)
    init_settings(args)
    assert(settings.debug == True)

# Generated at 2022-06-14 01:26:11.295626
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:26:17.276531
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

    args.debug = False
    init_settings(args)
    assert not settings.debug


if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:26:19.471701
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:21.121807
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:22.359259
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:26:27.619190
# Unit test for function init_settings
def test_init_settings():
    # Test with debug mode enabled
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    # Test with debug mode disabled
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:26:32.233446
# Unit test for function init_settings
def test_init_settings():
    from collections import namedtuple

    x = namedtuple("x", "debug")
    args = x(True)

    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:15.833380
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:27:20.192180
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:27:23.880694
# Unit test for function init_settings
def test_init_settings():
    args = Mock()
    args.debug = True
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:27:26.507713
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:27:31.468664
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False

    init_settings(args)
    assert settings.debug is False

    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:27:33.615543
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug

    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:27:40.168440
# Unit test for function init_settings
def test_init_settings():
    # Without args, settings.debug should be False
    init_settings(Namespace())
    assert settings.debug == False
    # With args.debug = True, settings.debug should be True
    init_settings(Namespace(debug = True))
    assert settings.debug == True

if __name__ == '__main__':
    # Run tests if script is called directly
    test_init_settings()

# Generated at 2022-06-14 01:27:43.558239
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:45.660920
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:49.015112
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:29:16.189506
# Unit test for function init_settings
def test_init_settings():
    args_true = Namespace(debug=True)
    args_false = Namespace(debug=False)
    init_settings(args_true)
    assert settings.debug
    init_settings(args_false)
    assert not settings.debug

# Generated at 2022-06-14 01:29:18.282870
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False

test_init_settings()

# Generated at 2022-06-14 01:29:21.476902
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    init_settings(parser.parse_args())
    assert settings.debug

# Generated at 2022-06-14 01:29:27.570258
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace as NS
    args = NS(
        debug=False,
        force=False,
        host=None,
        port=None,
        reload='',
        scan_all=False,
        server='auto',
        settings=None,
        socket=None,
        ssl_keyfile='',
        ssl_certfile='',
        timeout=120,
        verify_ssl='auto',
    )
    init_settings(args)
    assert settings.debug == False



# Generated at 2022-06-14 01:29:31.634415
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:29:36.291301
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:29:39.422395
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


# Unit test fot function hextorgb

# Generated at 2022-06-14 01:29:41.315737
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_set

# Generated at 2022-06-14 01:29:43.432141
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:29:46.785657
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug = False)
    init_settings(args)
    assert settings.debug == False