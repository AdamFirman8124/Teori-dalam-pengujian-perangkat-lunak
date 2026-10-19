

# Generated at 2022-06-14 01:22:04.327820
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:22:07.401215
# Unit test for function init_settings
def test_init_settings():
    my_settings = Settings()
    my_settings.debug = True
    args = Namespace()
    args.debug = True
    init_settings(args)

    assert settings.debug == my_settings.debug


# Generated at 2022-06-14 01:22:09.905931
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:22:15.139847
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", type=bool, default=True)
    args = parser.parse_args()

    init_settings(args)

    assert settings.debug == args.debug

# Generated at 2022-06-14 01:22:19.817848
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    assert not settings.debug



# Generated at 2022-06-14 01:22:22.241200
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings
    assert settings.debug

# Generated at 2022-06-14 01:22:24.775557
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:27.543455
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    args.debug = False
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:30.742670
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True, log_file=None)
    init_settings(args)
    assert settings.debug is True


test_init_settings()

# Generated at 2022-06-14 01:22:33.966344
# Unit test for function init_settings
def test_init_settings():
    global settings
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:41.130444
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True


if __name__ == '__main__':
    assert False, "Please import me as a module, don't run me as a script."

# Generated at 2022-06-14 01:22:47.613949
# Unit test for function init_settings
def test_init_settings():
    print("Test function: init_settings")

    # Debug set to False by default
    args = Namespace(debug=False, instance=['test'])
    init_settings(args)
    assert settings.debug is False

    # Debug set to True
    args = Namespace(debug=True, instance=['test'])
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:22:51.064578
# Unit test for function init_settings
def test_init_settings():
    args1 = Namespace(debug=True)
    args2 = Namespace(debug=False)
    init_settings(args1)
    assert settings.debug
    init_settings(args2)
    assert not settings.debug

# Generated at 2022-06-14 01:22:55.086276
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settin

# Generated at 2022-06-14 01:22:58.944681
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False

    sys.argv = ['file', '--debug']
    args = parse_args()
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:02.171959
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    asse

# Generated at 2022-06-14 01:23:09.146044
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert hasattr(settings, 'debug')
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert hasattr(settings, 'debug')
    assert settings.debug == False

# Generated at 2022-06-14 01:23:12.576989
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()

    args.debug = True
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:23:15.171912
# Unit test for function init_settings
def test_init_settings():
    class Args:
        def __init__(self) -> None:
            self.debug = False
    args = Args()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:18.431631
# Unit test for function init_settings
def test_init_settings():
    args = argparse.Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:26.764619
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = False)
    init_settings(args)

    # Check that settings object has the correct value for debug
    assert settings.debug == False

# Generated at 2022-06-14 01:23:28.441827
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:30.465561
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:32.119704
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    assert args.debug == True

# Generated at 2022-06-14 01:23:35.292202
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True

    init_settings(test_args)

    assert settings.debug


# Generated at 2022-06-14 01:23:38.623376
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:40.637877
# Unit test for function init_settings
def test_init_settings():
    args = argparse.Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:45.668487
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug is False

    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:47.925330
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:23:54.404441
# Unit test for function init_settings
def test_init_settings():
    print("\nUnit Testing function init_settings")

    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False

    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

    print("Test complete")

# Generated at 2022-06-14 01:24:08.398588
# Unit test for function init_settings
def test_init_settings():
    try:
        args = Namespace(debug=False)
        init_settings(args)
        assert not settings.debug
    except AssertionError:
        print('AssertionError')
    else:
        print('Passed')



# Generated at 2022-06-14 01:24:13.863190
# Unit test for function init_settings
def test_init_settings():
    import sys
    import os
    import unittest

    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(CUR_DIR, '..', '..', '..', '..'))
    from utils.arg_parser import ArgParser
    parser = ArgParser(sys.argv[1:])
    args = parse

# Generated at 2022-06-14 01:24:18.333508
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:24:22.495280
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:26.025108
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:29.646798
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:24:31.503242
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(
        debug=True
    )
    init_settings(args)

    assert settings.debug == True

test_init_settings()

# Generated at 2022-06-14 01:24:34.926748
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    init_settings(Namespace())
    assert not settings.debug

# Generated at 2022-06-14 01:24:38.162472
# Unit test for function init_settings
def test_init_settings():
    """
    Unit test for function init_settings
    """
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:42.046694
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:25:05.998384
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug == True

if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:25:09.168487
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:25:13.735748
# Unit test for function init_settings
def test_init_settings():
    with patch('sys.argv', ['main_script.py', '--debug']):
        ns = ArgumentParser(description='Dummy parser').parse_args()
        init_settings(ns)
        assert settings.debug == True



# Generated at 2022-06-14 01:25:16.757451
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:19.076539
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:25:22.184233
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

test_init_settings()

# Generated at 2022-06-14 01:25:25.694155
# Unit test for function init_settings
def test_init_settings():
    global settings
    settings = Settings()
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:25:28.182468
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    assert not settings.debug

# Generated at 2022-06-14 01:25:32.996358
# Unit test for function init_settings
def test_init_settings():
    args = Namespace
    args.debug = True
    init_settings(args)
    assert settings.debug==True



# Generated at 2022-06-14 01:25:35.268061
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:58.305364
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:01.051008
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug=True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:02.881995
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:09.598451
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:26:10.872789
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:26:13.063775
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:17.152672
# Unit test for function init_settings
def test_init_settings():
    # Tests with --debug and without --debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:19.391105
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:23.830552
# Unit test for function init_settings
def test_init_settings():
    # Test on/off debug mode
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:26:27.603591
# Unit test for function init_settings
def test_init_settings():
    args = argparse.Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:11.337535
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:27:15.944326
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    configs = Namespace()
    init_settings(configs)
    assert not settings.debug
    configs = Namespace()
    configs.debug = True
    init_settings(configs)
    assert settings.debug

# Generated at 2022-06-14 01:27:19.396128
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:23.147990
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    assert settings.debug is False
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:27:25.703205
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:27:28.433665
# Unit test for function init_settings
def test_init_settings():
    assert(not settings.debug)
    import argparse
    args = argparse.Namespace()
    args.debug = True
    init_settings(args)
    assert(settings.debug)

# Generated at 2022-06-14 01:27:29.324543
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:27:33.812311
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args2 = Namespace(debug=False)
    init_settings(args2)
    assert settings.debug == False

# Generated at 2022-06-14 01:27:36.616566
# Unit test for function init_settings
def test_init_settings():
    init_settings(namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:27:39.501022
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


if __name__ == "main":
    test_init_settings()

# Generated at 2022-06-14 01:28:23.513982
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:29.253513
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug is False
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

test_init_settings()



# Generated at 2022-06-14 01:28:30.678993
# Unit test for function init_settings
def test_init_settings():
    test = Namespace()
    test.debug = False
    init_settings(test)
    assert settings.debug == test.debug

# Generated at 2022-06-14 01:28:34.251195
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:35.728163
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:28:37.321197
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:28:39.256936
# Unit test for function init_settings
def test_init_settings():
    Settings.__init__ = Mock()
    Namespace.__init__ = Mock()

    args = {'debug':True}
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:28:44.429959
# Unit test for function init_settings
def test_init_settings():
    # test default settings
    assert settings.debug == False

    # test settings changed by args
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:47.070885
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug is True

# Generated at 2022-06-14 01:28:50.513062
# Unit test for function init_settings
def test_init_settings():
    # Test 1:
    args = Namespace()
    init_settings(args)
    assert settings.debug == False

    # Test 2:
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:30:17.078234
# Unit test for function init_settings
def test_init_settings():
    # Arrange

    # Act
    settings.debug = True
    init_settings(settings)

    # Assert
    assert settings.debug is True

# Generated at 2022-06-14 01:30:22.102260
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:30:24.662638
# Unit test for function init_settings
def test_init_settings():
    global settings
    settings = Settings()
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:30:30.518317
# Unit test for function init_settings
def test_init_settings():
    # Arrange
    args = Namespace(
        debug=True
    )

    # Act
    init_settings(args)

    # Assert
    assert settings.debug


# Generated at 2022-06-14 01:30:32.577674
# Unit test for function init_settings
def test_init_settings():
     init_settings("test","test")
     assert settings.debug == False

# Generated at 2022-06-14 01:30:37.891970
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:30:39.728044
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(**{'debug': True})
    init_settings(args)
    assert settings.debug


# Generated at 2022-06-14 01:30:42.942594
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:30:46.279008
# Unit test for function init_settings
def test_init_settings():
    args = argparse.Namespace
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:30:50.856232
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    settings.debug = False
    args.debug = True
    init_settings(args)
    assert(settings.debug)
    settings.debug = False
    args.debug = False
    init_settings(args)
    assert not(settings.debug)