

# Generated at 2024-06-02 15:43:00.209607
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:43:03.398800
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the data
        config.load()
        
        # Assert the data is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid json}")
        
        # Assert that loading invalid JSON raises ConfigFileError
        try:
            config.load()
        except ConfigFileError:
            pass
        else:
            assert False, "Expected ConfigFileError"
        
        # Remove the file to simulate file not found
        temp

# Generated at 2024-06-02 15:43:05.510504
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:43:07.147992
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:43:10.348923
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4: X

# Generated at 2024-06-02 15:43:13.261052
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:43:15.101499
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:43:16.483367
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:43:18.665380
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:43:21.742183
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:43:29.807516
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:43:32.900745
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # Test 

# Generated at 2024-06-02 15:43:34.808420
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:43:37.872849
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:43:39.911090
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:43:43.194727
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{ invalid json }")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove

# Generated at 2024-06-02 15:43:44.590363
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:43:47.494606
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:43:49.823738
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:43:52.863431
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value",
            "__meta__": {
                "httpie": "2.4.0"
            }
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert the content is loaded correctly
        assert config['key'] == 'value'
        assert config['__meta__']['httpie'] == '2.4.0'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{ invalid json }")
        
        # Attempt to load the invalid

# Generated at 2024-06-02 15:44:00.682869
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:44:02.389570
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:44:05.472351
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the data
        config.load()
        
        # Assert the data is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid json}")
        
        # Assert that loading invalid JSON raises ConfigFileError
        try:
            config.load()
        except ConfigFileError:
            pass
        else:
            assert False, "Expected ConfigFileError"
        
        # Remove the file and assert that loading non-existent file does

# Generated at 2024-06-02 15:44:08.344508
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # Test 

# Generated at 2024-06-02 15:44:11.481293
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:44:13.327238
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:44:16.626322
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:44:19.755363
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    temp_file_path = Path(temp_dir.name) / 'test_config.json'

    # Write a valid JSON to the temp file
    valid_json_content = {"key": "value"}
    temp_file_path.write_text(json.dumps(valid_json_content))

    # Initialize BaseConfigDict with the temp file path
    config = BaseConfigDict(path=temp_file_path)

    # Load the config
    config.load()

    # Assert that the config was loaded correctly
    assert config['key'] == 'value'

    # Write an invalid JSON to the temp file
    temp_file_path.write_text("{invalid_json}")

    # Assert that loading invalid JSON raises ConfigFileError
    try:
        config.load()
    except ConfigFileError:
        pass
    else:
        assert False, "Expected ConfigFileError"

    # Clean up
    temp_dir

# Generated at 2024-06-02 15:44:23.167407
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the data
        config.load()
        
        # Assert the data is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove the file to simulate file not found
        temp

# Generated at 2024-06-02 15:44:26.471528
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{ invalid json }")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove

# Generated at 2024-06-02 15:44:36.263287
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:44:38.861318
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:44:41.910271
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:44:44.662267
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{ invalid json }")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
       

# Generated at 2024-06-02 15:44:46.547834
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:44:49.442236
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:44:52.692953
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the data
        config.load()
        
        # Assert the data is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove the file to test IOError
        temp_path.unlink

# Generated at 2024-06-02 15:44:56.162175
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:44:57.864105
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:44:59.747391
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:45:07.260970
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:45:10.191411
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:45:13.160552
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:45:16.192733
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:45:19.711505
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir() 

# Generated at 2024-06-02 15:45:23.997057
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:45:26.922055
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:45:30.981716
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:45:33.085008
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:45:36.656607
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the data
        config.load()
        
        # Assert the data is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove the file to simulate file not found
        temp

# Generated at 2024-06-02 15:45:44.466063
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:45:47.493954
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:45:49.475482
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:45:52.749952
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:45:54.563873
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:45:57.848829
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:46:01.117984
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

# Generated at 2024-06-02 15:46:03.861722
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:46:06.932277
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:46:07.424213
# Unit test for method load of class BaseConfigDict

# Generated at 2024-06-02 15:46:15.164110
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:46:18.775462
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4: X

# Generated at 2024-06-02 15:46:21.093143
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:46:25.162504
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup original environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4:

# Generated at 2024-06-02 15:46:27.198035
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:46:30.826686
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:46:35.859807
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:46:38.302337
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:46:41.257907
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    from unittest import mock

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {'key': 'value'}
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Create an instance of BaseConfigDict with the temp file path
        config = BaseConfigDict(path=temp_path)
        
        # Load the config
        config.load()
        
        # Assert that the content was loaded correctly
        assert config['key'] == 'value'
        
        # Test with invalid JSON content
        temp_path.write_text('invalid json')
        
        # Create a new instance of BaseConfigDict with the temp file path
        config = BaseConfigDict(path=temp_path)
        
        # Assert that loading invalid JSON raises ConfigFileError

# Generated at 2024-06-02 15:46:46.558426
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4: X

# Generated at 2024-06-02 15:46:54.260322
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:46:57.955590
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Assert that loading invalid JSON raises ConfigFileError

# Generated at 2024-06-02 15:46:59.586890
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:47:01.859092
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:47:03.789484
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:47:07.901015
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:47:10.772976
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:47:13.857830
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    from unittest import mock

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {'key': 'value'}
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Test loading the valid JSON content
        config = BaseConfigDict(temp_path)
        config.load()
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text('invalid json')
        
        # Test loading the invalid JSON content
        config = BaseConfigDict(temp_path)
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        # Test loading from a non-existent file
        non_existent

# Generated at 2024-06-02 15:47:15.938966
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:47:18.892406
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Test case 1: Valid JSON file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        config = BaseConfigDict(temp_path)
        config.load()
        assert config == valid_data

        # Test case 2: Invalid JSON file
        temp_path.write_text("{invalid json}")
        config = BaseConfigDict(temp_path)
        try:
            config.load()
        except ConfigFileError as e:
            assert "invalid baseconfigdict file" in str(e)

        # Test case 3: Non-existent file
        non_existent_path = Path(temp_dir) / 'non_existent.json'
        config = BaseConfigDict(non_existent_path)
        config.load()  # Should not raise an exception


# Generated at 2024-06-02 15:47:26.987743
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup original environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4:

# Generated at 2024-06-02 15:47:30.286364
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:47:33.301956
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()  # Clean up

    # Test

# Generated at 2024-06-02 15:47:36.272030
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        temp_path = Path(tempdir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:47:39.835200
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:47:42.160198
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:47:43.981888
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:47:47.411968
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

# Generated at 2024-06-02 15:47:49.847184
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:47:52.953453
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:47:59.311033
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:48:01.045529
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:48:03.592881
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:48:05.844540
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:48:09.566329
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # Test 

# Generated at 2024-06-02 15:48:12.645306
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

# Generated at 2024-06-02 15:48:15.994587
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:48:18.009957
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:48:21.080935
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:48:23.007200
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:48:29.203265
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:48:30.872875
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:48:33.875128
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:48:37.225256
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:48:40.347941
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove the

# Generated at 2024-06-02 15:48:44.866205
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    from unittest import mock

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Test loading valid JSON
        config = BaseConfigDict(temp_path)
        config.load()
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid json}")
        
        # Test loading invalid JSON
        config = BaseConfigDict(temp_path)
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Test file not found
        non_existent_path = Path(temp_dir) / 'non_existent.json'


# Generated at 2024-06-02 15:48:47.129646
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:48:50.562360
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # Test 

# Generated at 2024-06-02 15:48:54.552702
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:48:56.237610
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:49:02.048863
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:49:03.756112
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:49:05.261812
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:49:08.100300
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:49:11.090097
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:49:14.187689
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:49:16.882112
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:49:18.585208
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:49:22.207246
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:49:23.374052
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:49:29.054261
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:49:30.662948
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:49:32.328828
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:49:36.555036
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_path = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_path.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_path
    legacy_path.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:49:39.186697
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:49:41.067395
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:49:44.269617
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:49:47.289924
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:49:49.238387
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:49:50.924374
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:49:57.315883
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/config/dir'
    assert get_default_config_dir() == Path('/custom/config/dir')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:49:59.978719
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:50:01.878856
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:50:05.152304
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:50:07.889362
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert the data is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        # Remove the file and attempt to load, should

# Generated at 2024-06-02 15:50:12.087723
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:50:14.105643
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:50:17.673658
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # Test 

# Generated at 2024-06-02 15:50:21.275953
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:50:24.351227
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

# Generated at 2024-06-02 15:50:32.763276
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e).lower()
        
        #

# Generated at 2024-06-02 15:50:35.348184
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:50:38.877453
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

# Generated at 2024-06-02 15:50:40.981520
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:50:43.083248
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:50:46.992210
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

# Generated at 2024-06-02 15:50:48.866468
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:50:50.960608
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:50:55.416258
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup original environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4:

# Generated at 2024-06-02 15:50:59.703551
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]

    # Test

# Generated at 2024-06-02 15:51:04.928818
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:51:08.047158
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

# Generated at 2024-06-02 15:51:11.153825
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:51:14.758082
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:51:16.955008
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:51:19.842210
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:51:22.731252
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('/tmp/test_config.json')

# Generated at 2024-06-02 15:51:29.840502
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test 2: Windows environment
    if is_windows:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test 3: Legacy config directory exists
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()  # Clean up

    # Test

# Generated at 2024-06-02 15:51:31.587670
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:51:34.311538
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:51:40.528214
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:51:43.564694
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4: X

# Generated at 2024-06-02 15:51:45.636140
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:51:47.912790
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:51:49.965282
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:51:52.183237
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:51:54.531913
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:51:57.226047
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:51:59.743507
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:52:02.202962
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:52:07.681324
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:52:10.975186
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup original environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4:

# Generated at 2024-06-02 15:52:13.282441
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:52:21.179361
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy config directory
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG config directory
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2024-06-02 15:52:27.090601
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON content to the file
        valid_json_content = {
            "key": "value"
        }
        temp_path.write_text(json.dumps(valid_json_content))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the configuration
        config.load()
        
        # Assert that the content is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON content to the file
        temp_path.write_text("{invalid_json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove the

# Generated at 2024-06-02 15:52:30.180538
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_dir
    legacy_dir.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:52:32.351093
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():    temp_dir = Path('temp_test_dir')

# Generated at 2024-06-02 15:52:33.728031
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    config_path = Path('test_config.json')

# Generated at 2024-06-02 15:52:36.691583
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():    # Create a temporary directory and file for testing
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / 'config.json'
        
        # Write a valid JSON to the file
        valid_data = {"key": "value"}
        temp_path.write_text(json.dumps(valid_data))
        
        # Initialize BaseConfigDict with the path
        config = BaseConfigDict(temp_path)
        
        # Load the data
        config.load()
        
        # Assert the data is loaded correctly
        assert config['key'] == 'value'
        
        # Write an invalid JSON to the file
        temp_path.write_text("{invalid json}")
        
        # Attempt to load the invalid JSON and catch the exception
        try:
            config.load()
        except ConfigFileError as e:
            assert 'invalid baseconfigdict file' in str(e)
        
        # Remove the file to simulate file not found
        temp

# Generated at 2024-06-02 15:52:39.948859
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Test when ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test legacy ~/.httpie
    legacy_path = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_path.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_path
    legacy_path.rmdir()

    # Test XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg/config'
    assert get_default_config_dir() == Path('/custom/xdg/config') / DEFAULT_CONFIG_DIRNAME

# Generated at 2024-06-02 15:52:46.228439
# Unit test for function get_default_config_dir
def test_get_default_config_dir():    # Backup environment variables
    original_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    original_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # Test case 1: ENV_HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/httpie/config'
    assert get_default_config_dir() == Path('/custom/httpie/config')

    # Test case 2: Running on Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Test case 3: Legacy config directory exists
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()  # Clean up

    # Test case 4: X

# Generated at 2024-06-02 15:52:48.735200
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():    config_path = Path('test_config.json')