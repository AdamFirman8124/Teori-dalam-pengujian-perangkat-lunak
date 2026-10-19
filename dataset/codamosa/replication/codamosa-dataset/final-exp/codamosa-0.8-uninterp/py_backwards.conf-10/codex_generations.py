

# Generated at 2022-06-14 01:22:04.085734
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args.debug=False
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:22:06.071356
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:22:08.464481
# Unit test for function init_settings
def test_init_settings():
    # mock args
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:13.501661
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True
    
    
if __name__ == '__main__':
    print('Running unit tests...')
    
    test_init_settings()
    
    print('All unit tests have passed')

# Generated at 2022-06-14 01:22:18.240538
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    args.debug = False
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:19.711113
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    asse

# Generated at 2022-06-14 01:22:24.472198
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=False)
    init_settings(test_args)

    test_args = Namespace(debug=True)
    init_settings(test_args)


if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:22:26.342140
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:28.699460
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug

# Test that __init__ sets debug to False

# Generated at 2022-06-14 01:22:29.599697
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:37.643803
# Unit test for function init_settings
def test_init_settings():
    args1 = Namespace(debug=False)
    init_settings(args1)
    assert settings.debug == False

    args2 = Namespace(debug=True)
    init_settings(args2)
    assert settings.debug == True
    print("Everything passed!")


# Run unit test for function init_settings
test_init_settings()

# Generated at 2022-06-14 01:22:39.948564
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:42.553396
# Unit test for function init_settings
def test_init_settings():
    dummy_args = Namespace(debug=True)
    init_settings(dummy_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:46.238332
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:48.065975
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:51.516262
# Unit test for function init_settings
def test_init_settings():
    settings.debug=True
    args = Namespace(debug="False")
    init_settings(args)
    settings.debug=False
    args = Namespace(debug="True")
    init_settings(args)

# Generated at 2022-06-14 01:22:55.015513
# Unit test for function init_settings
def test_init_settings():
    # Define arguments
    args = Namespace(debug = True)
    # Initialize settings
    init_settings(args)
    # Test result
    assert settings.debug == True

# Generated at 2022-06-14 01:22:59.941900
# Unit test for function init_settings
def test_init_settings():
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:02.781583
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:06.030241
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:14.822342
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)

    assert settings.debug == False

    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:23:18.431014
# Unit test for function init_settings
def test_init_settings():
    # create dummy command line arguments namespace
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:23:22.576748
# Unit test for function init_settings
def test_init_settings():
    # Test when debug is False
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

    # Test when debug is True
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:26.271513
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


# Define your services here.

# Generated at 2022-06-14 01:23:31.233306
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:36.132503
# Unit test for function init_settings
def test_init_settings():
    mock = MagicMock(spec=Namespace)
    del mock.debug
    mock.debug = "true"
    init_settings(mock)
    assert settings.debug == True


# Generated at 2022-06-14 01:23:38.839963
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace
    import sys
    
    args = Namespace(debug = True)
    init_settings(args)
    
    assert settings.debug == True

# Generated at 2022-06-14 01:23:41.629603
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    assert not settings.debug == False

# Generated at 2022-06-14 01:23:45.785781
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:47.740607
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:03.307622
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug
    args.debug = True
    init_settings(args)
    assert settings.debug


if __name__ == '__main__':
    test_init_settings()
    print('Unit test has passed.')

# Generated at 2022-06-14 01:24:07.598766
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

    args = Namespace(debug=True)
    init_se

# Generated at 2022-06-14 01:24:10.507681
# Unit test for function init_settings
def test_init_settings():
    init_settings(
        Namespace(
            debug=True
        )
    )
    assert settings.debug == True


if __name__ == "__main__":
    init_settings(
        Namespace(
            debug=True
        )
    )
    print(settings.debug)

# Generated at 2022-06-14 01:24:14.543868
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()

    args.debug = False
    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:18.830755
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:21.722910
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:24.978058
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:28.732501
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug
    init_settings(Namespace(debug=False))
    assert not settings.debug

# Generated at 2022-06-14 01:24:33.142114
# Unit test for function init_settings
def test_init_settings():
    try:
        assert(settings.debug == False)
    except Exception as e:
        print("Unit test init_settings failed")
        print(e)


test_init_settings()

# Function to load the appropriate URL based on user input

# Generated at 2022-06-14 01:24:37.969734
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:54.033457
# Unit test for function init_settings
def test_init_settings():
    debug = True
    args = Namespace()
    args.debug = debug
    init_settings(args)
    assert settings.debug == True


if __name__ == "__main__":
    debug = True
    args = Namespace()
    args.debug = debug
    init_settings(args)
    print(settings.debug)

# Generated at 2022-06-14 01:24:58.865269
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

test_init_settings()

# Generated at 2022-06-14 01:25:00.805161
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:25:07.088703
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=False)
    init_settings(test_args)
    assert settings.debug == False
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:08.790253
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:13.090642
# Unit test for function init_settings
def test_init_settings():
    args = mock.MagicMock()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:15.255559
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:20.210217
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()

    args.debug = True

    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:25:24.322300
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:28.131016
# Unit test for function init_settings
def test_init_settings():
    def test_args(debug):
        args = Namespace(debug=debug)
        init_settings(args)
        assert settings.debug == debug

    test_args(debug=True)
    test_args(debug=False)

# Generated at 2022-06-14 01:25:51.435695
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:25:55.807052
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = False)
    init_settings(args)
    assert settings.debug is False

    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:26:01.224310
# Unit test for function init_settings
def test_init_settings():
    from unittest import mock
    mock_args = mock.Mock()
    mock_args.debug = False
    init_settings(mock_args)
    assert not settings.debug
    mock_args.debug = True
    init_settings(mock_args)
    assert settings.debug
    
test_init_settings()

# Generated at 2022-06-14 01:26:03.426642
# Unit test for function init_settings
def test_init_settings():
    args = Args()
    args.debug = True
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:26:06.086145
# Unit test for function init_settings
def test_init_settings():
    global settings

    args = Namespace()
    args.debug = True

    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:26:08.371441
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:10.926823
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug is False
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:26:16.345980
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug = True)
    init_settings(test_args)
    assert settings.debug == True

    test_args = Namespace(debug = False)
    init_settings(test_args)
    assert settings.debug == False

# Generated at 2022-06-14 01:26:21.449165
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug is False, "Unexpected default value."
    init_settings(Namespace(debug=False))
    assert settings.debug is False, "Unexpected value."
    init_settings(Namespace(debug=True))
    assert settings.debug is True, "Unexpected value."

# Generated at 2022-06-14 01:26:24.559061
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", default=False, action="store_true")
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == True

if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:27:09.603227
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:27:11.909531
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug

# Generated at 2022-06-14 01:27:15.862914
# Unit test for function init_settings
def test_init_settings():
    # Fixture
    args = Namespace(debug=True)
    # Call function
    init_settings(args)
    # Assert function
    assert settings.debug == True

# Generated at 2022-06-14 01:27:19.396752
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:27:23.148120
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug and settings.debug == True

# Generated at 2022-06-14 01:27:26.271282
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)

    assert(settings.debug)

test_init_settings()

# Generated at 2022-06-14 01:27:30.013527
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:31.372090
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:27:37.766761
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug is False, "settings.debug should be False before initialising"

    init_settings(Namespace(debug=True))
    assert settings.debug, "init_settings should set debug to True if debug argument is True"

    init_settings(Namespace(debug=False))
    assert not settings.debug, "init_settings should set debug to False if debug argument is False"

# Generated at 2022-06-14 01:27:39.987611
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=False))
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:29:06.775797
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    init_settings(Namespace(debug=True))
    assert settings.debug == True 
    init_settings(Namespace(debug=False))
    assert settings.debug == False

# Generated at 2022-06-14 01:29:07.595513
# Unit test for function init_settings
def test_init_settings():
    pass

# Generated at 2022-06-14 01:29:11.198581
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True


# Based on https://stackoverflow.com/a/2020083

# Generated at 2022-06-14 01:29:14.258991
# Unit test for function init_settings
def test_init_settings():
    args = mock.Mock()
    args.debug = True

    init_settings(args)

    assert settings.debug is True



# Generated at 2022-06-14 01:29:18.162524
# Unit test for function init_settings
def test_init_settings():
    args = ['--debug']
    assert not settings.debug
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:29:21.253020
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    assert not settings.debug
    init_settings(args)
    assert not settings.debug
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:29:32.514541
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",
                        help="enable debug mode",
                        action="store_true")
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == False
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",
                        help="enable debug mode",
                        action="store_true")
    args = parser.parse_args(["--debug"])
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:29:36.057539
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:29:38.059743
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    assert settings.debug == False
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:29:44.974637
# Unit test for function init_settings
def test_init_settings():
    """Ensures that init_settings correctly sets debug to True if debug is requested.
    Tests with:
    1. set debug to True via command line args
    2. set debug to False via command line args
    """
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug = False)
    init_settings(args)
    assert settings.debug == False