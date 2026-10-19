

# Generated at 2024-03-18 08:12:30.666937
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:12:37.830046
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)
    
    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()
        
        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
        
        # Asserting that add_command was called with the correct parameters

# Generated at 2024-03-18 08:12:46.133000
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)
    
    # Mocking the tr function
    mock_tr = unittest.mock.Mock(return_value="Pygame Zero mode")
    
    # Mocking the os.environ dictionary
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
            with unittest.mock.patch('thonny.languages.tr', mock_tr):
                # Call the function to test
                load_plugin()
                
                # Assert that set_default was called with the correct parameters
                mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
                
                # Assert that add_command was called with the correct parameters
                mock_workbench.add

# Generated at 2024-03-18 08:12:53.135052
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable and option value
    original_env_var = os.environ.get("PGZERO_MODE")
    original_option_value = get_workbench().get_option(_OPTION_NAME)

    # Test when in simple mode
    get_workbench().set_option("general.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and the option is True
    get_workbench().set_option("general.simple_mode", False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and the option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore the original environment variable and option value

# Generated at 2024-03-18 08:13:01.874529
# Unit test for function update_environment
def test_update_environment():    # Backup original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE")

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto", "PGZERO_MODE should be 'auto' in simple mode"

    # Test when not in simple mode and the option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True", "PGZERO_MODE should be 'True' when the option is True"

    # Test when not in simple mode and the option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False", "PGZERO_MODE should be 'False' when the option is False"

    # Restore

# Generated at 2024-03-18 08:13:06.034001
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:13:12.882642
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)
    mock_workbench.in_simple_mode = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the os.environ to prevent actual environment variable changes
        with patch.dict('os.environ', {}, clear=True):
            # Call the function to test
            load_plugin()

            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:13:18.426880
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:13:26.366471
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)
    mock_workbench.in_simple_mode = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the os.environ to check if it is being set correctly
        with patch.dict('os.environ', {}, clear=True):
            # Call the function to test
            load_plugin()

            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:13:35.233201
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()

        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Asserting that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Asserting that get_option was called to check the initial state

# Generated at 2024-03-18 08:13:45.436376
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable if it exists
    original_env = os.environ.get("PGZERO_MODE")

    # Set up the test for simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto", "Should set PGZERO_MODE to 'auto' in simple mode"

    # Set up the test for non-simple mode with pgzero_mode enabled
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True", "Should set PGZERO_MODE to 'True' when pgzero_mode is enabled"

    # Set up the test for non-simple mode with pgzero_mode disabled
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()

# Generated at 2024-03-18 08:13:56.085549
# Unit test for function update_environment
def test_update_environment():    # Backup original environment variable and option value
    original_env_var = os.environ.get("PGZERO_MODE")
    original_option_value = get_workbench().get_option(_OPTION_NAME)


# Generated at 2024-03-18 08:14:00.163550
# Unit test for function toggle_variable
def test_toggle_variable():    original_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:14:06.134946
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)
    mock_workbench.in_simple_mode = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the os.environ to prevent actual environment variable changes
        with patch.dict('os.environ', {}, clear=True):
            # Call the function to test
            load_plugin()

            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:14:18.842076
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)
    
    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the os.environ to check if it is being set correctly
        with unittest.mock.patch.dict('os.environ', {}, clear=True):
            # Call the function to test
            load_plugin()
            
            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
            
            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:14:26.249931
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE", None)

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Set the workbench to normal mode with pgzero_mode off and test
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Set the workbench to normal mode with pgzero_mode on and test
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Restore the original environment variable
    if original_pgzero_mode is not None:
        os.environ["PGZERO_MODE"] = original_pgzero_mode
   

# Generated at 2024-03-18 08:14:32.629464
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Call the function to test
        load_plugin()

        # Assert that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Assert that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Assert

# Generated at 2024-03-18 08:14:41.026884
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_env_var = os.environ.get("PGZERO_MODE", None)

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Set the workbench to normal mode with pgzero_mode off and test
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Set the workbench to normal mode with pgzero_mode on and test
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Restore the original environment variable
    if original_env_var is not None:
        os.environ["PGZERO_MODE"] = original_env_var

# Generated at 2024-03-18 08:14:47.048309
# Unit test for function update_environment
def test_update_environment():    # Save original environment variable and workbench state
    original_env_var = os.environ.get("PGZERO_MODE")
    original_simple_mode = get_workbench().in_simple_mode()
    original_option = get_workbench().get_option(_OPTION_NAME)

    # Test when in simple mode
    get_workbench()._set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and the option is True
    get_workbench()._set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and the option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore original environment variable and workbench state

# Generated at 2024-03-18 08:15:04.774012
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)
    
    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the update_environment function to prevent side effects
        with unittest.mock.patch('update_environment') as mock_update_environment:
            # Call the function to test
            load_plugin()
            
            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
            
            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:15:18.367718
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()

        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Asserting that add_command was called with the correct parameters

# Generated at 2024-03-18 08:15:27.745622
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()

        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Asserting that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Asserting that the environment variable PGZERO_MODE is set correctly

# Generated at 2024-03-18 08:15:32.831664
# Unit test for function toggle_variable
def test_toggle_variable():    original_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:15:39.194054
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE")

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto", "Should set PGZERO_MODE to 'auto' in simple mode"

    # Set the workbench to not simple mode and test with option False
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False", "Should set PGZERO_MODE to 'False' when option is False"

    # Set the workbench to not simple mode and test with option True
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()

# Generated at 2024-03-18 08:15:45.339677
# Unit test for function update_environment
def test_update_environment():    # Save original environment variable and option value
    original_env_var = os.environ.get("PGZERO_MODE")
    original_option_value = get_workbench().get_option(_OPTION_NAME)

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore original environment variable and option value
    if original_env_var is not None:
        os.environ["PGZERO_MODE"] = original_env_var

# Generated at 2024-03-18 08:15:51.919032
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Mocking the tr function
    mock_tr = unittest.mock.Mock(return_value="Pygame Zero mode")

    # Mocking the os.environ dictionary
    original_environ = dict(os.environ)
    os.environ.clear()

    # Patching the get_workbench and tr functions
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench), \
         unittest.mock.patch('thonny.languages.tr', mock_tr):
        # Call the function under test
        load_plugin()

        # Assert that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Assert that add_command was called with the

# Generated at 2024-03-18 08:16:03.571248
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Mocking the tr function
    mock_tr = unittest.mock.Mock(return_value="Pygame Zero mode")

    # Mocking the os.environ dictionary
    with unittest.mock.patch.dict('os.environ', {}, clear=True):
        with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
            with unittest.mock.patch('thonny.languages.tr', mock_tr):
                # Call the function to test
                load_plugin()

                # Assert that set_default was called with the correct parameters
                mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

                # Assert that add_command was called with the correct parameters
                mock_workbench.add_command.assert_called_once

# Generated at 2024-03-18 08:16:11.241155
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()

        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Asserting that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Asserting that get_option was called to check the initial state

# Generated at 2024-03-18 08:16:20.164342
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Call the function to test
        load_plugin()

        # Assert that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Assert that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Assert

# Generated at 2024-03-18 08:16:29.796390
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)
    
    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()
        
        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
        
        # Asserting that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )
        
        # Asserting that get_option was called to

# Generated at 2024-03-18 08:16:49.086842
# Unit test for function update_environment
def test_update_environment():    # Save original environment variable and option value
    original_env = os.environ.get("PGZERO_MODE")
    original_option = get_workbench().get_option(_OPTION_NAME)

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore original environment variable and option value
    if original_env is not None:
        os.environ["PGZERO_MODE"] = original_env

# Generated at 2024-03-18 08:16:52.102190
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:16:58.557566
# Unit test for function update_environment
def test_update_environment():    # Backup original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE")

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto", "PGZERO_MODE should be 'auto' in simple mode"

    # Test when not in simple mode and the option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True", "PGZERO_MODE should be 'True' when the option is True"

    # Test when not in simple mode and the option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False", "PGZERO_MODE should be 'False' when the option is False"

    # Restore

# Generated at 2024-03-18 08:17:07.654444
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)
    
    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the os.environ to prevent actual environment variable changes
        with unittest.mock.patch.dict('os.environ', {}, clear=True):
            # Call the function to test
            load_plugin()
            
            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
            
            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:17:17.170936
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE")

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and the option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and the option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore the original environment variable
    if original_pgzero_mode is not None:
        os.environ["PGZERO_MODE"] = original_pgzero_mode
    else:
        del os.environ["PGZERO_MODE"]

# Generated at 2024-03-18 08:17:21.223988
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:17:30.568758
# Unit test for function update_environment
def test_update_environment():    # Save original environment and option state
    original_env = os.environ.get("PGZERO_MODE")
    original_option = get_workbench().get_option(_OPTION_NAME)

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore original environment and option state
    if original_env is not None:
        os.environ["PGZERO_MODE"] = original_env

# Generated at 2024-03-18 08:17:37.016639
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE", None)

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Set the workbench to normal mode with pgzero_mode off and test
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Set the workbench to normal mode with pgzero_mode on and test
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Restore the original environment variable
    if original_pgzero_mode is not None:
        os.environ["PGZERO_MODE"] = original_pgzero_mode
   

# Generated at 2024-03-18 08:17:43.794891
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Call the function to test
        load_plugin()

        # Assert that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Assert that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Assert that get_option was called to check the initial state
        mock

# Generated at 2024-03-18 08:17:47.467023
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:18:24.464568
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:18:29.421417
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:18:39.782597
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE", None)

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Set the workbench to normal mode with pgzero_mode off and test
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Set the workbench to normal mode with pgzero_mode on and test
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Restore the original environment variable
    if original_pgzero_mode is not None:
        os.environ["PGZERO_MODE"] = original_pgzero_mode
   

# Generated at 2024-03-18 08:18:43.974432
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:18:50.536602
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable if it exists
    original_env = os.environ.get("PGZERO_MODE")

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode but the option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and the option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore the original environment variable
    if original_env is not None:
        os.environ["PGZERO_MODE"] = original_env
    else:
        del os.environ["PGZERO_MODE"]

# Generated at 2024-03-18 08:18:55.451459
# Unit test for function load_plugin
def test_load_plugin():    # Save original environment and workbench state
    original_env = os.environ.copy()
    original_option = get_workbench().get_option(_OPTION_NAME)

    # Call the function to test
    load_plugin()

    # Check if the default is set correctly
    assert get_workbench().get_option(_OPTION_NAME) == False

    # Check if the command is added to the workbench
    assert "toggle_pgzero_mode" in get_workbench()._commands

    # Check if the environment variable is set correctly
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore original environment and workbench state
    os.environ = original_env
    get_workbench().set_option(_OPTION_NAME, original_option)


# Generated at 2024-03-18 08:19:04.599769
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE", None)

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto", "PGZERO_MODE should be 'auto' in simple mode"

    # Set the workbench to not simple mode and test with the option set to True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True", "PGZERO_MODE should be 'True' when the option is True"

    # Set the workbench to not simple mode and test with the option set to False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()

# Generated at 2024-03-18 08:19:12.288210
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)
    mock_workbench.in_simple_mode = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the os.environ to check if it is being set correctly
        with patch.dict('os.environ', {}, clear=True):
            # Call the function to test
            load_plugin()

            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:19:21.045368
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable if it exists
    original_env = os.environ.get("PGZERO_MODE")

    # Test when in simple mode
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and the option is True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test when not in simple mode and the option is False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Restore the original environment variable
    if original_env is not None:
        os.environ["PGZERO_MODE"] = original_env
    else:
        del os.environ["PGZERO_MODE"]

# Generated at 2024-03-18 08:19:29.796988
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.MagicMock()
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Mocking the tr function
        with unittest.mock.patch('thonny.languages.tr', side_effect=lambda x: x):
            # Call the function to test
            load_plugin()

            # Assert set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

            # Assert add_command was called with the correct parameters
            mock_workbench.add_command.assert_called_once_with(
                "toggle_pgzero_mode",
                "run",
                "Pygame Zero mode",
                toggle_variable,
                flag_name=_OPTION_NAME,
                group=40,
            )

            # Assert update_environment was called
            assert mock_workbench.method_calls[-1] == unittest.mock.call.update_environment()

# Generated at 2024-03-18 08:20:29.217263
# Unit test for function load_plugin
def test_load_plugin():    # Mock the necessary parts of the workbench
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)

    # Replace the get_workbench function with a mock that returns the mock workbench
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Call the function to test
        load_plugin()

        # Assert that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Assert that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Assert that the environment variable PGZERO_MODE is set

# Generated at 2024-03-18 08:20:40.579002
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_env_var = os.environ.get("PGZERO_MODE", None)

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Set the workbench to normal mode with pgzero_mode off and test
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Set the workbench to normal mode with pgzero_mode on and test
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Restore the original environment variable
    if original_env_var is not None:
        os.environ["PGZERO_MODE"] = original_env_var

# Generated at 2024-03-18 08:20:47.670023
# Unit test for function update_environment
def test_update_environment():    # Backup the original environment variable
    original_pgzero_mode = os.environ.get("PGZERO_MODE", None)

    # Set the workbench to simple mode and test
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto", "PGZERO_MODE should be 'auto' in simple mode"

    # Set the workbench to not simple mode and test with the option set to True
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True", "PGZERO_MODE should be 'True' when the option is True"

    # Set the workbench to not simple mode and test with the option set to False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()

# Generated at 2024-03-18 08:20:53.112303
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:20:57.942377
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:21:06.226200
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.set_default = MagicMock()
    mock_workbench.add_command = MagicMock()
    mock_workbench.get_option = MagicMock(return_value=False)
    mock_workbench.in_simple_mode = MagicMock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with patch('thonny.get_workbench', return_value=mock_workbench):
        # Patching the os.environ to prevent actual environment variable changes
        with patch.dict('os.environ', {}, clear=True):
            # Call the function to test
            load_plugin()

            # Assert that set_default was called with the correct parameters
            mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

            # Assert that add_command was called with the correct parameters

# Generated at 2024-03-18 08:21:13.013974
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()

        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Asserting that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Asserting

# Generated at 2024-03-18 08:21:23.150393
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()

        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Asserting that add_command was called with the correct parameters
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Asserting

# Generated at 2024-03-18 08:21:27.628235
# Unit test for function toggle_variable
def test_toggle_variable():    initial_value = get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2024-03-18 08:21:33.852140
# Unit test for function load_plugin
def test_load_plugin():    # Mocking the get_workbench function and its methods
    mock_workbench = unittest.mock.Mock()
    mock_workbench.set_default = unittest.mock.Mock()
    mock_workbench.add_command = unittest.mock.Mock()
    mock_workbench.get_option = unittest.mock.Mock(return_value=False)

    # Patching the get_workbench function to return the mock object
    with unittest.mock.patch('thonny.get_workbench', return_value=mock_workbench):
        # Calling the function to test
        load_plugin()

        # Asserting that set_default was called with the correct parameters
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Asserting that add_command was called with the correct parameters