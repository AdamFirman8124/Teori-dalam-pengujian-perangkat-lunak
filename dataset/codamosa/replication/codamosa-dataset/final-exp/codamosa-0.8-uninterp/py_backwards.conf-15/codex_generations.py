

# Generated at 2022-06-14 01:21:59.711061
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:04.375328
# Unit test for function init_settings
def test_init_settings():
    # test_args = Namespace()
    # print(test_args)
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:22:12.444637
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    parser = argparse.ArgumentParser(description='Process number of tweets')
    parser.add_argument('--debug', choices=['y', 'n'], default='y')
    args = parser.parse_args(['--debug', 'n'])
    init_settings(args)
    assert settings.debug == False

    settings.debug = False
    parser = argparse.ArgumentParser(description='Process number of tweets')
    parser.add_argument('--debug', choices=['y', 'n'], default='y')
    args = parser.parse_args(['--debug', 'y'])
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:16.571898
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True
# End unit test for function init_settings


# Generated at 2022-06-14 01:22:20.978242
# Unit test for function init_settings
def test_init_settings():
    global settings
    settings = Settings()
    assert settings.debug == False
    init_settings(Namespace(debug = True))
    assert settings.debug == True
    init_settings(Namespace(debug = False))
    assert settings.debug == False

# Generated at 2022-06-14 01:22:25.021573
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    assert settings.debug == False
    init_settings(args)
    assert settings.debug == True

if __name__ == '__main__':
    # Test settings
    test_init_settings()

# Generated at 2022-06-14 01:22:27.264982
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(
        debug=True,
    )
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:30.094651
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=False)
    init_settings(test_args)
    assert settings.debug == False



# Generated at 2022-06-14 01:22:34.597923
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace

    # create an instance of arg-parser of argparse
    args = Namespace(debug=True)

    #    call the function init_settings
    init_settings(args)

    assert settings.debug is True

# Generated at 2022-06-14 01:22:37.219158
# Unit test for function init_settings
def test_init_settings():
    args = ['-d']
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:41.593834
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:45.299206
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:47.138400
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:50.285253
# Unit test for function init_settings
def test_init_settings():
    args = Namespace
    args.debug = True
    init_settings(args)
    assert settings.debug
    args.debug = False
    init_setti

# Generated at 2022-06-14 01:22:55.762696
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:22:59.095599
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)

    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:23:02.325572
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:05.566765
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:07.318799
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug
    assert not settings.debug


# Generated at 2022-06-14 01:23:08.973559
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)

    assert settings.debug == True
    logging.basicConfig(level=logging.DEBUG if settings.debug else logging.INFO)

# Generated at 2022-06-14 01:23:16.582722
# Unit test for function init_settings
def test_init_settings():
    # test for debug
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:23:21.903930
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug is False

# Generated at 2022-06-14 01:23:26.932527
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False

    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:30.996800
# Unit test for function init_settings
def test_init_settings():
    args1 = argparse.Namespace(debug=False)
    init_settings(args1)
    assert settings.debug == False

    args2 = argparse.Namespace(debug=True)
    init_settings(args2)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:34.569846
# Unit test for function init_settings
def test_init_settings():
    settings.debug = False
    init_settings(Namespace(debug=True))
    assert settings.debug == True



# Generated at 2022-06-14 01:23:38.589918
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:41.375124
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug


if __name__ == '__main__':
    fire.Fire(init_settings)

# Generated at 2022-06-14 01:23:44.526096
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:46.666838
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug


# Generated at 2022-06-14 01:23:48.135344
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:24:01.801350
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:05.586450
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug is True
    init_settings(Namespace(debug=False))
    assert settings.debug is False


# End of file pinco

# Generated at 2022-06-14 01:24:08.677725
# Unit test for function init_settings
def test_init_settings():
    mocker = Mocker()
    mockargs = mocker.Mock()
    mockargs.debug = "debug"
    init_settings(mockargs)
    assert settings.debug == "debug"


# Generated at 2022-06-14 01:24:10.194121
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:24:14.799806
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False


test_init_settings()

# Generated at 2022-06-14 01:24:18.330745
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True


# Generated at 2022-06-14 01:24:24.228578
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    # Should not raise errors
    init_settings(args)
    args.debug = True
    init_settings(args)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 01:24:27.334000
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:24:32.072196
# Unit test for function init_settings
def test_init_settings():
    parser = get_parser()
    args = parser.parse_args(['-d'])
    init_settings(args)
    assert settings.debug == True
    # print('test_init_settings passed')

# Generated at 2022-06-14 01:24:34.265587
# Unit test for function init_settings
def test_init_settings():
    settings.debug = True
    assert settings.debug



# Generated at 2022-06-14 01:24:58.065122
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    setattr(args, 'debug', True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:01.030033
# Unit test for function init_settings
def test_init_settings():
    parser = ArgumentParser(description="")
    parser.add_argument("-d", "--debug", help="", action="store_true")
    args = parser.parse_args(['-d'])
    init_settings(args)

    assert settings.debug

# Generated at 2022-06-14 01:25:04.917443
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:08.789108
# Unit test for function init_settings
def test_init_settings():
    global settings
    settings = Settings()
    args = Namespace()

    init_settings(args)
    assert settings.debug is False

    args.debug = True
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:25:12.841971
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:25:14.717644
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug=True)
    init_settings(test_args)
    assert settings.debug

# Generated at 2022-06-14 01:25:16.149188
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:18.164762
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:21.164173
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:25:24.087882
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True