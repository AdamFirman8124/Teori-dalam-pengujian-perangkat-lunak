

# Generated at 2022-06-14 01:22:20.105365
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:23.262629
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True
    init_settings(test_args)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:26.341831
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:29.684233
# Unit test for function init_settings
def test_init_settings():
    args = Namespace
    args.debug = True
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:34.817442
# Unit test for function init_settings
def test_init_settings():
    args = init_parser(['-d'])
    init_settings(args)
    assert settings.debug


# Generated at 2022-06-14 01:22:39.529514
# Unit test for function init_settings
def test_init_settings():
    arguments = Namespace(debug=True)
    init_settings(arguments)
    assert settings.debug == True

    arguments = Namespace(debug=False)
    init_settings(arguments)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:45.592130
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    args.debug = False
    args.a = 10
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:49.307788
# Unit test for function init_settings
def test_init_settings():
    class Args:
        debug = None

    args = Args
    args.debug = False
    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:55.414694
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", type=str, help="Enable debugging",
                        action="store_true")
    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:58.119403
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:23:02.403097
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:05.733716
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True


# Generated at 2022-06-14 01:23:09.146800
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug

# should be able to run tests by calling py.test

# Generated at 2022-06-14 01:23:12.575230
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:23:16.281120
# Unit test for function init_settings
def test_init_settings():
    sys.argv[1:] = ['--debug']
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:23:21.778686
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug is True
    init_settings(Namespace(debug=False))
    assert settings.debug is False

# Generated at 2022-06-14 01:23:26.857264
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:28.517920
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:31.106709
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:34.569019
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:41.819633
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    settings.debug = False
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False


# Generated at 2022-06-14 01:23:44.831811
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:47.925223
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False

    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:51.255391
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:56.955459
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:02.271238
# Unit test for function init_settings
def test_init_settings():
    settings1 = Settings()
    args = Namespace(debug=True)
    ini_settings(args)
    assert settings.debug == True

    settings2 = Settings()
    args = Namespace(debug=False)
    ini_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:05.651198
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Finished testing for function init_settings

# Generated at 2022-06-14 01:24:09.382866
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

# Generated at 2022-06-14 01:24:11.642664
# Unit test for function init_settings
def test_init_settings():
    args = argparse.Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:24:16.818762
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    args.debug = False
    init_settings(args)
    assert settings.debug == False


if __name__ == "main":
    test_init_settings()

# Generated at 2022-06-14 01:24:26.602032
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:29.462447
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:32.096720
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:24:35.138336
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    eq_(settings.debug, True)

# Generated at 2022-06-14 01:24:38.817949
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

# Generated at 2022-06-14 01:24:41.842716
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:45.602870
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.dubug == False

# Generated at 2022-06-14 01:24:49.488514
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:24:53.329967
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug
    assert not settings.debug == 0



# Generated at 2022-06-14 01:24:57.808839
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:13.541599
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


if __name__ == '__main__':
    init_settings(Namespace())

# Generated at 2022-06-14 01:25:15.768022
# Unit test for function init_settings
def test_init_settings():
    parser = init_parser()
    args = parser.parse_args(["-d"])

    init_settings(args)

    assert settings.debug == True


# Generated at 2022-06-14 01:25:17.054262
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:19.316517
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:21.970892
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:25:25.905462
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug = True))
    assert settings.debug == True
    init_settings(Namespace(debug = False))
    assert settings.debug == False

test_init_settings()

# Generated at 2022-06-14 01:25:28.385732
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False

    args = Namespace()
    args.debug = True
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:25:34.237488
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:36.147057
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug=True
    init_setti

# Generated at 2022-06-14 01:25:39.318328
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

test_init_settings()

# Generated at 2022-06-14 01:25:55.013269
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug

    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:25:57.251169
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:26:00.036318
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:26:02.256539
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    # print(settings.debug)

# Generated at 2022-06-14 01:26:04.875998
# Unit test for function init_settings
def test_init_settings():
    parser = create_parser()
    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:08.487106
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    # Test with no arguments
    init_settings(Namespace())
    assert not settings.debug
    # Test with debug set
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:26:11.017643
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:26:17.083218
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    if settings.debug == False:
        print("Function init_settings() didn't work")
    else:
        print("Function init_settings() did work")

# Generated at 2022-06-14 01:26:19.908937
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True
    init_settings(Namespace(debug=False))
    assert settings.debug == False

# Generated at 2022-06-14 01:26:21.800990
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    init_settings(args)

    assert settings.debug
    assert not hasattr(settings, "foo")

# Generated at 2022-06-14 01:26:45.766532
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:49.957792
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    init_settings(args)
    assert not settings.debug

    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:26:56.134139
# Unit test for function init_settings
def test_init_settings():

    # setup
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Turn on debug output",
    )
    args = parser.parse_args()
    args.debug = True

    # run
    init_settings(args)

    # check
    assert settings.debug



# Generated at 2022-06-14 01:27:00.701133
# Unit test for function init_settings
def test_init_settings():
    init_settings(
        args=Namespace(
            debug=True
        )
    )

    assert settings.debug

test_init_settings()

# Generated at 2022-06-14 01:27:02.694413
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:05.306111
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:27:09.564306
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True





# Generated at 2022-06-14 01:27:16.796460
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug')
    args = parser.parse_args([])
    init_settings(args)
    assert not settings.debug

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug')
    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug


# Simple function to dump an object

# Generated at 2022-06-14 01:27:19.358365
# Unit test for function init_settings
def test_init_settings():
    global settings
    args = Namespace()
    args.debug = True
    init_settings(args)
    
    assert settings.debug == True



# Generated at 2022-06-14 01:27:23.097237
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    settings.debug = False
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:28:12.919828
# Unit test for function init_settings
def test_init_settings():
    # Arrange
    args = Namespace()
    args.debug = True

    # Act
    init_settings(args)

    # Assert
    assert settings.debug == True

# Generated at 2022-06-14 01:28:16.631561
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:28:24.877578
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    if settings.debug != True:
        raise AssertionError("Error, settings.debug should be true.")
    args2 = Namespace()
    args2.debug = False
    init_settings(args2)
    if settings.debug != False:
        raise AssertionError("Error, settings.debug should be false.")
    return 0

# Generated at 2022-06-14 01:28:29.512162
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:28:34.164021
# Unit test for function init_settings
def test_init_settings():
    a = Namespace(debug=True)
    init_settings(a)
    assert settings.debug is True
    a = Namespace(debug=False)
    init_settings(a)
    assert settings.debug is False
    a = Namespace()
    init_settings(a)
    assert settings.debug is False

# Generated at 2022-06-14 01:28:35.659560
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:38.420478
# Unit test for function init_settings
def test_init_settings():
    """
        Test Case for init_settings
    """
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:28:43.712053
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True
test_init_settings()

# Generated at 2022-06-14 01:28:47.035427
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Add your tests here

# Generated at 2022-06-14 01:28:50.479708
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

# Generated at 2022-06-14 01:29:38.576971
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug

# Generated at 2022-06-14 01:29:44.040977
# Unit test for function init_settings
def test_init_settings():
    # Case 1: debug = True
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    # Case 2: debug = False
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:29:46.948342
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    argv = ["--debug"]
    args = parser.parse_args(argv)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:29:50.708670
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:29:52.282548
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    asse

# Generated at 2022-06-14 01:29:55.115144
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    assert settings.debug == False
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:29:59.086995
# Unit test for function init_settings
def test_init_settings():
    # test for debug
    result = init_settings(Namespace(debug=True))
    assert result == None
    assert settings.debug == True
    # test for not debug
    result = init_settings(Namespace(debug=False))
    assert result == None
    assert settings.debug == False

# Generated at 2022-06-14 01:30:04.160019
# Unit test for function init_settings
def test_init_settings():
    from unittest.mock import Mock
    args = Mock()
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True


# Unit tests for the settings

# Generated at 2022-06-14 01:30:14.545364
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    init_settings(args)
    assert settings.debug == True


# Define parser
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('files', nargs='+')
parser.add_argument('--dest', type=str)

# Parse arguments
args = parser.parse_args()

# Initialize settings
init_settings(args)

# Print settings
print(settings.debug)
print(args.files)
print(args.dest)

# Generated at 2022-06-14 01:30:16.236362
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:31:50.496648
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:31:54.290977
# Unit test for function init_settings
def test_init_settings():
    assert settings.debug == False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:31:56.064481
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:31:59.247704
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:32:01.829138
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:32:06.344774
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:32:11.994525
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    mocker.patch('job_service.settings.settings', settings)
    args=Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:32:15.761399
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Example function that uses settings.debug