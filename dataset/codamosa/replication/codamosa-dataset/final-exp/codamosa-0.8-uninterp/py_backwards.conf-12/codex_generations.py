

# Generated at 2022-06-14 01:21:56.330943
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)

    assert settings.debug == False

    args.debug = True
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:21:59.573036
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True, excel_file="", use_last_data=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:03.433425
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    result = settings.debug
    assert result == True


# Generated at 2022-06-14 01:22:07.606466
# Unit test for function init_settings
def test_init_settings():
    args_debug = Namespace(debug=True)
    init_settings(args_debug)
    assert settings.debug == True
    args_no_debug = Namespace(debug=False)
    init_settings(args_no_debug)
    assert settings.debug == False

# Generated at 2022-06-14 01:22:09.905931
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug


# Generated at 2022-06-14 01:22:14.477841
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:15.725014
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:20.552307
# Unit test for function init_settings
def test_init_settings():
    # Test
    args = Namespace(debug=True)
    init_settings(args)
    # Validate
    assert settings.debug == True


# Usage

# Generated at 2022-06-14 01:22:21.818158
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:22:28.094532
# Unit test for function init_settings
def test_init_settings():
    import argparse
    args = argparse.Namespace()
    args.debug = False
    init_settings(args)
    assert not settings.debug
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:35.118011
# Unit test for function init_settings
def test_init_settings():
    """
    Test that init_settings sets settings.debug to True when arguments has debug
    :return:
    """
    arguments = Namespace()
    arguments.debug = True
    init_settings(arguments)
    assert settings.debug is True

# Generated at 2022-06-14 01:22:37.817390
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True


# Generated at 2022-06-14 01:22:40.605610
# Unit test for function init_settings
def test_init_settings():
    import argparse
    args = argparse.Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:43.207711
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:46.938465
# Unit test for function init_settings
def test_init_settings():
    args = create_debug_args()
    init_settings(args)
    assert settings.debug is True


# Generated at 2022-06-14 01:22:49.987147
# Unit test for function init_settings
def test_init_settings():
    # Given
    args = Namespace(debug = "debug")

    # When
    init_settings(args)

    # Then
    assert settings.debug == True

# Generated at 2022-06-14 01:22:51.482070
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)

# Generated at 2022-06-14 01:22:54.393338
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True, loglevel='info')
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:58.035009
# Unit test for function init_settings
def test_init_settings():
    with patch.object(sys, 'argv', ['script-name', '--debug']):
        args = parse_args()
        init_settings(args)
    assert settings.debug is True

# Check the settings object exists

# Generated at 2022-06-14 01:23:01.737131
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:12.682159
# Unit test for function init_settings
def test_init_settings():
    # Set settings to default
    settings = Settings()

    # Define settings
    args = Namespace()
    setattr(args, 'debug', None)

    # Set settings as in program arguments
    init_settings(args)

    # Assert settings are as expected
    assert settings.debug == args.debug



# Generated at 2022-06-14 01:23:14.396806
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:15.688674
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:18.784277
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = 'False')
    assert settings.debug is False
    init_settings(args)
    assert settings.debug is False



# Generated at 2022-06-14 01:23:20.953043
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:24.625519
# Unit test for function init_settings
def test_init_settings():
    from argparse import Namespace
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:23:32.177857
# Unit test for function init_settings
def test_init_settings():
    """ Test function to test function init_settings"""
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug',action='store_true')
    args = parser.parse_args(sys.argv[1:])

    settings.debug = False
    init_settings(args)
    assert settings.debug == True

    settings.debug = True
    init_settings(args)
    assert settings.debug == True

    settings.debug = False
    args.debug = False
    init_settings(args)
    assert settings.debug == False



# Generated at 2022-06-14 01:23:34.800836
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:36.462270
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:23:40.059209
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug


if __name__ == "__main__":
    args = Namespace(debug=True)
    init_settings(args)