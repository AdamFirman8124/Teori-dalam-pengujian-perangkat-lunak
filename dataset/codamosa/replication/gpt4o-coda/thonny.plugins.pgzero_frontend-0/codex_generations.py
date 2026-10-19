

# Generated at 2024-06-03 11:21:19.572643
# Unit test for function update_environment

# Generated at 2024-06-03 11:21:23.449307
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:21:28.871289
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:21:35.502356
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is

# Generated at 2024-06-03 11:21:40.013106
# Unit test for function update_environment
def test_update_environment():    # Mocking the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple

# Generated at 2024-06-03 11:21:43.724133
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:21:49.614898
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is

# Generated at 2024-06-03 11:21:56.563901
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3: When not

# Generated at 2024-06-03 11:22:00.728505
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.options = {}

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def get_option(self, name):
            return self.options.get(name, None)

        def in_simple_mode(self):
            return False


# Generated at 2024-06-03 11:22:04.273951
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.simple_mode = False
            self.options = {_OPTION_NAME: False}
        
        def in_simple_mode(self):
            return self.simple_mode
        
        def get_option(self, name):
            return self.options.get(name, None)
        
        def set_option(self, name, value):
            self.options[name] = value

    # Replace the real get_workbench with the mock
    original_get_workbench = get_workbench
    mock_workbench = MockWorkbench()
    get_workbench = lambda: mock_workbench

    # Test when in simple mode
    mock_workbench.simple_mode = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and option is False
    mock_workbench.simple_mode = False

# Generated at 2024-06-03 11:22:12.311334
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {_OPTION_NAME: False}
            self.simple_mode = False

        def get_variable(self, name):
            return self.variables[name]

        def get_option(self, name):
            return self.variables[name]

        def in_simple_mode(self):
            return self.simple_mode

        def set_default(self, name, value):
            self.variables[name] = value

    # Setting up the mock workbench
    mock_workbench = MockWorkbench()
    original_get_workbench = get_workbench
    get_workbench = lambda: mock_workbench

    # Test when not in simple mode and option is False
    mock_workbench.variables[_OPTION_NAME] = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test when not in simple mode and option is True
    mock_workbench.variables

# Generated at 2024-06-03 11:22:16.170317
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:22:26.605446
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called and the environment variable was set correctly

# Generated at 2024-06-03 11:22:30.749750
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    initial_value = get_workbench().get_variable(_OPTION_NAME).get()
    
    # Call the function to toggle the variable
    toggle_variable()
    
    # Check if the variable has been toggled
    toggled_value = get_workbench().get_variable(_OPTION_NAME).get()
    assert toggled_value == (not initial_value), f"Expected {not initial_value}, but got {toggled_value}"
    
    # Check if the environment variable has been updated correctly
    expected_env_value = "auto" if get_workbench().in_simple_mode() else str(toggled_value)
    assert os.environ["PGZERO_MODE"] == expected_env_value, f"Expected {expected_env_value}, but got {os.environ['PGZERO_MODE']}"


# Generated at 2024-06-03 11:22:35.208336
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3: When not

# Generated at 2024-06-03 11:22:38.850618
# Unit test for function update_environment
def test_update_environment():    # Mocking the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value
            self.variables = {_OPTION_NAME: MockVariable(option_value)}

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

        def get_variable(self, option_name):
            return self.variables[option_name]

    class MockVariable:
        def __init__(self, value):
            self.value = value

        def get(self):
            return self.value

        def set(self, value):
            self.value = value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()

# Generated at 2024-06-03 11:22:41.982554
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:22:44.806458
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:22:48.268999
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.options = {}
            self.simple_mode = False

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def get_option(self, name):
            return self.options.get(name, None)

        def in_simple_mode(self):
            return self.simple_mode


# Generated at 2024-06-03 11:22:51.579089
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:23:02.409908
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value
            self.variables = {_OPTION_NAME: MockVariable(option_value)}

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

        def get_variable(self, option_name):
            return self.variables[option_name]

    class MockVariable:
        def __init__(self, value):
            self.value = value

        def get(self):
            return self.value

        def set(self, value):
            self.value = value

    # Test when in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"



# Generated at 2024-06-03 11:23:06.679098
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called and the environment variable was set correctly

# Generated at 2024-06-03 11:23:10.408463
# Unit test for function update_environment
def test_update_environment():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode

# Generated at 2024-06-03 11:23:15.094411
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3: When not

# Generated at 2024-06-03 11:23:19.236499
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:23:21.812300
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:23:22.370581
# Unit test for function update_environment

# Generated at 2024-06-03 11:23:26.292109
# Unit test for function update_environment
def test_update_environment():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode

# Generated at 2024-06-03 11:23:29.759393
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:23:34.680859
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    initial_value = get_workbench().get_variable(_OPTION_NAME).get()
    
    # Call the function to toggle the variable
    toggle_variable()
    
    # Check if the variable has been toggled
    toggled_value = get_workbench().get_variable(_OPTION_NAME).get()
    assert toggled_value == (not initial_value), f"Expected {not initial_value}, but got {toggled_value}"
    
    # Check if the environment variable has been updated correctly
    expected_env_value = "auto" if get_workbench().in_simple_mode() else str(toggled_value)
    assert os.environ["PGZERO_MODE"] == expected_env_value, f"Expected {expected_env_value}, but got {os.environ['PGZERO_MODE']}"


# Generated at 2024-06-03 11:23:53.535149
# Unit test for function load_plugin
def test_load_plugin():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.default_options = {}

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.default_options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def in_simple_mode(self):
            return False

        def get_option(self, name):
            return self.default_options.get(name, False)


# Generated at 2024-06-03 11:23:57.545025
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.options = {}

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def get_option(self, name):
            return self.options.get(name, None)

        def in_simple_mode(self):
            return False


# Generated at 2024-06-03 11:23:58.047808
# Unit test for function update_environment

# Generated at 2024-06-03 11:24:03.115063
# Unit test for function load_plugin
def test_load_plugin():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.variables[name] = MockVariable(value)

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def in_simple_mode(self):
            return False

        def get_option(self, name):
            return self.variables[name].get()


# Generated at 2024-06-03 11:24:07.371186
# Unit test for function load_plugin
def test_load_plugin():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.simple_mode = False

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.variables[name] = MockVariable(value)

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, name):
            return self.variables[name].get()


# Generated at 2024-06-03 11:24:11.111972
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is

# Generated at 2024-06-03 11:24:16.066660
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    initial_value = get_workbench().get_variable(_OPTION_NAME).get()
    
    # Call the function to toggle the variable
    toggle_variable()
    
    # Check if the variable has been toggled
    toggled_value = get_workbench().get_variable(_OPTION_NAME).get()
    assert toggled_value == (not initial_value), f"Expected {not initial_value}, but got {toggled_value}"
    
    # Check if the environment variable has been updated correctly
    expected_env_value = "auto" if get_workbench().in_simple_mode() else str(toggled_value)
    assert os.environ["PGZERO_MODE"] == expected_env_value, f"Expected {expected_env_value}, but got {os.environ['PGZERO_MODE']}"


# Generated at 2024-06-03 11:24:20.177971
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.options = {}

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def get_option(self, name):
            return self.options.get(name, None)

        def in_simple_mode(self):
            return False


# Generated at 2024-06-03 11:24:24.404417
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is

# Generated at 2024-06-03 11:24:29.412108
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:25:00.107586
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value
            self.variables = {_OPTION_NAME: MockVariable(option_value)}

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

        def get_variable(self, option_name):
            return self.variables[option_name]

    class MockVariable:
        def __init__(self, value):
            self.value = value

        def get(self):
            return self.value

        def set(self, value):
            self.value = value

    # Test when in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"



# Generated at 2024-06-03 11:25:03.835183
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is

# Generated at 2024-06-03 11:25:08.311813
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:25:12.767202
# Unit test for function update_environment
def test_update_environment():    # Mocking the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3:

# Generated at 2024-06-03 11:25:16.824974
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:25:22.068882
# Unit test for function load_plugin
def test_load_plugin():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.options = {}

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def in_simple_mode(self):
            return False

        def get_option(self, name):
            return self.options.get(name, None)


# Generated at 2024-06-03 11:25:26.404062
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.simple_mode = False

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.variables[name] = MockVariable(value)

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, name):
            return self.variables[name].get()


# Generated at 2024-06-03 11:25:29.591753
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:25:33.380434
# Unit test for function load_plugin
def test_load_plugin():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.simple_mode = False

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.variables[name] = MockVariable(value)

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, name):
            return self.variables[name].get()


# Generated at 2024-06-03 11:25:38.118628
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3: When not

# Generated at 2024-06-03 11:26:37.911323
# Unit test for function update_environment
def test_update_environment():    # Mocking the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3:

# Generated at 2024-06-03 11:26:45.201741
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is

# Generated at 2024-06-03 11:26:49.280798
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.options = {}
            self.simple_mode = False

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def get_option(self, name):
            return self.options.get(name, None)

        def in_simple_mode(self):
            return self.simple_mode


# Generated at 2024-06-03 11:26:52.875011
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3: When not

# Generated at 2024-06-03 11:26:53.348782
# Unit test for function update_environment

# Generated at 2024-06-03 11:26:56.999674
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if the environment variable was set correctly
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:26:59.609366
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:27:03.062542
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:27:07.060083
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.options = {}

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def get_option(self, name):
            return self.options.get(name, None)

        def in_simple_mode(self):
            return False


# Generated at 2024-06-03 11:27:14.302914
# Unit test for function load_plugin
def test_load_plugin():    # Mock the get_workbench function and its methods
    mock_workbench = MagicMock()
    mock_workbench.get_variable.return_value.get.return_value = False
    mock_workbench.in_simple_mode.return_value = False
    mock_workbench.get_option.return_value = False

    with patch('thonny.get_workbench', return_value=mock_workbench):
        load_plugin()

        # Check if set_default was called with the correct arguments
        mock_workbench.set_default.assert_called_once_with(_OPTION_NAME, False)

        # Check if add_command was called with the correct arguments
        mock_workbench.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

        # Check if update_environment was called
        assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:29:10.126822
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is

# Generated at 2024-06-03 11:29:14.522841
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3: When not

# Generated at 2024-06-03 11:29:18.149055
# Unit test for function update_environment
def test_update_environment():    # Mocking the get_workbench function and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: When in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: When not in simple mode and option is False
    mock_workbench = MockWorkbench(simple_mode=False, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test case 3:

# Generated at 2024-06-03 11:29:21.935492
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.simple_mode = False
            self.options = {_OPTION_NAME: False}

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, name):
            return self.options.get(name, None)

    mock_workbench = MockWorkbench()

    # Patching get_workbench to return the mock object
    original_get_workbench = get_workbench
    get_workbench = lambda: mock_workbench

    # Test when in simple mode
    mock_workbench.simple_mode = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test when not in simple mode and option is False
    mock_workbench.simple_mode = False
    mock_workbench.options[_OPTION_NAME] = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2024-06-03 11:29:24.665600
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:29:29.184737
# Unit test for function load_plugin
def test_load_plugin():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self):
            self.variables = {}
            self.commands = []
            self.default_options = {}

        def get_variable(self, name):
            if name not in self.variables:
                self.variables[name] = MockVariable()
            return self.variables[name]

        def set_default(self, name, value):
            self.default_options[name] = value

        def add_command(self, command_id, menu_name, description, handler, flag_name, group):
            self.commands.append({
                "command_id": command_id,
                "menu_name": menu_name,
                "description": description,
                "handler": handler,
                "flag_name": flag_name,
                "group": group
            })

        def in_simple_mode(self):
            return False

        def get_option(self, name):
            return self.default_options.get(name, False)


# Generated at 2024-06-03 11:29:32.272392
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function to toggle the variable back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:29:36.714951
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value
            self.variables = {_OPTION_NAME: MockVariable(option_value)}

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

        def get_variable(self, option_name):
            return self.variables[option_name]

    class MockVariable:
        def __init__(self, value):
            self.value = value

        def get(self):
            return self.value

        def set(self, value):
            self.value = value

    # Test when in simple mode
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"



# Generated at 2024-06-03 11:29:39.800722
# Unit test for function toggle_variable
def test_toggle_variable():    # Set up the initial state
    get_workbench().set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "False"

    # Call the function to toggle the variable
    toggle_variable()

    # Check if the variable has been toggled
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    # Call the function again to toggle back
    toggle_variable()

    # Check if the variable has been toggled back
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2024-06-03 11:29:45.549648
# Unit test for function update_environment
def test_update_environment():    # Mocking get_workbench and its methods
    class MockWorkbench:
        def __init__(self, simple_mode, option_value):
            self.simple_mode = simple_mode
            self.option_value = option_value

        def in_simple_mode(self):
            return self.simple_mode

        def get_option(self, option_name):
            return self.option_value

    # Test case 1: Simple mode is True
    mock_workbench = MockWorkbench(simple_mode=True, option_value=False)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test case 2: Simple mode is False and option is True
    mock_workbench = MockWorkbench(simple_mode=False, option_value=True)
    get_workbench = lambda: mock_workbench
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Test case 3: Simple mode is