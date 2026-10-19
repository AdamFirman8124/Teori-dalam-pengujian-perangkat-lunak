

# Generated at 2022-06-22 13:02:40.588793
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default("run.pgzero_mode", False)
    wb.step_mode = wb.SIMPLE_MODE

    update_environment()
    assert os.environ.get("PGZERO_MODE") == "auto"

    wb.step_mode = None
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "False"

    wb.set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "True"

# Generated at 2022-06-22 13:02:48.016758
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:02:51.612211
# Unit test for function toggle_variable
def test_toggle_variable():
    old_value=get_workbench().get_variable(_OPTION_NAME)
    toggle_variable()
    assert(get_workbench().get_variable(_OPTION_NAME)!=old_value)

# Generated at 2022-06-22 13:02:57.732661
# Unit test for function update_environment
def test_update_environment():
    if _OPTION_NAME in os.environ:
        del os.environ[_OPTION_NAME]
    
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ[_OPTION_NAME] == "True"
    
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ[_OPTION_NAME] == "False"
    
    get_workbench().set_simple_mode(True)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:03:02.281439
# Unit test for function update_environment
def test_update_environment():
    assert "PGZERO_MODE" not in os.environ

    get_workbench().set_variable("run.pgzero_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_variable("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:07.564126
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:15.966029
# Unit test for function update_environment
def test_update_environment():
    import thonny

    get_workbench().set_simple_mode(True)
    thonny.workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    thonny.workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(False)
    thonny.workbench.set_option(_OPTION_NAME, False)
    update

# Generated at 2022-06-22 13:03:22.223012
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    update_environment()
    assert get_workbench().get_option(
    "test_load_plugin"
    ) == False


# Generated at 2022-06-22 13:03:28.515695
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().unset_default(_OPTION_NAME)
    load_plugin()

    assert os.environ.get("PGZERO_MODE") in ["0", "1"]
    assert get_workbench().get_option(_OPTION_NAME)
    get_workbench().set_option(_OPTION_NAME, False)
    assert os.environ.get("PGZERO_MODE") in ["0", "1"]
    assert not get_workbench().get_option(_OPTION_NAME)



# Generated at 2022-06-22 13:03:37.230276
# Unit test for function load_plugin
def test_load_plugin():
    try:
        from thonny.workbench import Workbench
        from thonny.plugins.run import RunCommand
        from thonny import get_workbench
        import unittest.mock as mock
        import threading
    except ImportError:
        return

    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, False)
    workbench.register_command(
        _OPTION_NAME,
        RunCommand(workbench, "toggle_pgzero_mode", "run", "Pygame Zero mode", toggle_variable, 40),
    )

    with mock.patch.object(threading.Event, "is_set", return_value=False):
        workbench.set_default(_OPTION_NAME, True)

# Generated at 2022-06-22 13:03:53.873890
# Unit test for function toggle_variable
def test_toggle_variable():
    class MockView:
        def add_checkbutton(self, *args, **kwargs):
            pass

    class MockWorkbench:
        def __init__(self):
            self.log = ""
            self.variable = "0"

        def add_command(self, *args, **kwargs):
            self.log += "Thonny plugin added"

        def get_variable(self, name):
            return self.variable

        def set_variable(self, name, value):
            self.log += "Thonny plugin setting variable value"
            self.variable = value

    # This will raise an error if the view does not have the correct methods
    MockWorkbench().get_view("RunView")
    mockView = MockView()
    mockWorkbench = MockWorkbench()

# Generated at 2022-06-22 13:03:58.430957
# Unit test for function update_environment
def test_update_environment():
    # Create a mockup of the environment and clean it
    def mock_clean():
        os.environ.clear()

    # Create a mockup where the in_simple_mode function returns True
    def mock_simple_mode():
        return True

    # Create a mockup where the in_simple_mode function returns False
    def mock_normal_mode():
        return False

    # Create a mockup of the get_option function that returns True
    def mock_option_true():
        return True

    # Create a mockup of the get_option function that returns False
    def mock_option_false():
        return False

    # Import the module that we are testing
    import thonnycontrib.pgzero_mode as pgze

    # Create a mockup of the workbench where the in_simple_mode function returns True
    workbench = Magic

# Generated at 2022-06-22 13:04:04.444401
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.set_default(_OPTION_NAME, True)
    os.environ["PGZERO_MODE"] = "auto"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    os.environ["PGZERO_MODE"] = "auto"
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

if __name__ == "__main__":
    test_update_environment()

# Generated at 2022-06-22 13:04:10.202355
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    commands = wb.get_commands()
    assert "toggle_pgzero_mode" in commands
    assert commands["toggle_pgzero_mode"].label == tr("Pygame Zero mode")
    assert commands["toggle_pgzero_mode"].flag_name == _OPTION_NAME
    assert commands["toggle_pgzero_mode"].group == 40

# Generated at 2022-06-22 13:04:20.692286
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock

    wb = Mock()
    wb.set_default = Mock()
    wb.add_command = Mock()
    wb.in_simple_mode = Mock(return_value = True)

    load_plugin()

    wb.set_default.assert_called_with(_OPTION_NAME, False)
    wb.add_command.assert_called_with(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )

    toggle_variable()
    update_environment()

    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:25.636084
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert _OPTION_NAME in get_workbench().get_variable_names()



# Generated at 2022-06-22 13:04:28.441882
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:33.069191
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:37.354301
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert "PGZERO_MODE" not in os.environ
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:39.692251
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()

    assert os.environ["PGZERO_MODE"] == "False"
    

# Generated at 2022-06-22 13:04:53.119556
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.workbench import Workbench

    wb = Workbench(Mock(), config_dir=".")
    wb.in_simple_mode = lambda: False
    wb.set_default = lambda x, y: None
    wb.get_variable = lambda x: Mock(get=lambda: True)
    wb.add_command = lambda *args, **kwargs: None
    wb.get_option = lambda x: True
    load_plugin()


# Generated at 2022-06-22 13:05:01.990304
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    wb = Workbench()
    assert os.environ.get("PGZERO_MODE") is None
    load_plugin()
    assert os.environ.get("PGZERO_MODE") == "False"
    get_workbench().in_simple_mode = lambda: False
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "False"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "True"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "auto"



# Generated at 2022-06-22 13:05:12.956298
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench
    workbench.get_options()["run.pgzero_mode"] = False
    assert workbench.in_simple_mode()
    assert not workbench.get_option(_OPTION_NAME)
    assert "PGZERO_MODE" not in os.environ

    load_plugin()
    assert not workbench.in_simple_mode()
    assert workbench.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    assert len(workbench.get_command("toggle_pgzero_mode")["variable_names"]) == 1
    assert _OPTION_NAME in workbench.get_command("toggle_pgzero_mode")["variable_names"]

    toggle_variable()

# Generated at 2022-06-22 13:05:16.201586
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:05:25.129925
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(False)

    wb.set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_option("run.pgzero_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:05:32.410857
# Unit test for function update_environment
def test_update_environment():
    # In normal mode
    os.environ["PGZERO_MODE"] = "bogus"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    # In simple mode
    get_workbench().set_simple_mode(True)
    os.environ["PGZERO_MODE"] = "bogus"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)

# Generated at 2022-06-22 13:05:33.575236
# Unit test for function toggle_variable
def test_toggle_variable():
        toggle_variable()

# Generated at 2022-06-22 13:05:36.416513
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    update_environment()



# Generated at 2022-06-22 13:05:47.049148
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    from thonny.globals import get_runner
    from thonny.globals import get_workbench
    from thonny.plugins.run.pgzero_mode import update_environment
    from unittest.mock import MagicMock

    # Mock the necessary functions to simulate the environment of Thonny
    mock_get_workbench = MagicMock(return_value=MagicMock())
    mock_get_workbench.get_option.return_value = False
    mock_get_workbench.in_simple_mode.return_value = False
    mock_get_workbench.get_variable.return_value = False
    mock_get_runner = MagicMock(return_value=MagicMock())
    mock_get_runner.get_backend_cmd_line

# Generated at 2022-06-22 13:05:54.145187
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_simple_mode(True)
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:10.999726
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:06:13.978258
# Unit test for function toggle_variable
def test_toggle_variable():

    toggle_variable()
    assert os.getenv("PGZERO_MODE") == "True"

    toggle_variable()
    assert os.getenv("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:06:18.801215
# Unit test for function load_plugin
def test_load_plugin():
    wb = create_workbench_mock()
    load_plugin(wb)
    assert wb.get_default(_OPTION_NAME) is False
    assert wb.get_command("toggle_pgzero_mode").flag_name == _OPTION_NAME
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:06:19.305877
# Unit test for function load_plugin
def test_load_plugin():
    pass

# Generated at 2022-06-22 13:06:28.036429
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_default(_OPTION_NAME, True)
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:38.422121
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_simple_mode(False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    assert get_workbench().get_option(_OPTION_NAME) == False

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    assert get_workbench().get_option(_OPTION_NAME) == True

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:40.646682
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop("PGZERO_MODE", None)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:06:41.506206
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:06:46.981432
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert get_workbench().in_simple_mode() == False
    assert os.getenv("PGZERO_MODE") == "False"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.getenv("PGZERO_MODE") == "True"
    get_workbench().set_simple_mode(True)
    assert os.getenv("PGZERO_MODE") == "auto"

# Generated at 2022-06-22 13:06:49.885341
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_option(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:07:05.332921
# Unit test for function toggle_variable
def test_toggle_variable():
    "Toggle the variable between True and False using test_toggle_variable."
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == True

# Generated at 2022-06-22 13:07:13.940046
# Unit test for function toggle_variable
def test_toggle_variable():
    try:
        get_workbench().set_default(_OPTION_NAME, False)
        toggle_variable()
        assert get_workbench().get_option(_OPTION_NAME) == True
        assert os.environ["PGZERO_MODE"] == "True"
        toggle_variable()
        assert get_workbench().get_option(_OPTION_NAME) == False
        assert os.environ["PGZERO_MODE"] == "False"
    finally:
        get_workbench().set_default(_OPTION_NAME, False)
        update_environment()

# Generated at 2022-06-22 13:07:22.924871
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    from thonny import Workbench

    from thonny.misc_utils import running_on_linux

    with mock.patch("os.environ", {}):
        w = Workbench()
        w.set_in_simple_mode(False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
        w.set_default(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"

        # When in simple mode (default), it will never enable Pygame Zero mode.
        w.set_in_simple_mode(True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"

        # On Linux, Pygame Zero mode is enabled

# Generated at 2022-06-22 13:07:24.197095
# Unit test for function load_plugin
def test_load_plugin():
    pass

# Generated at 2022-06-22 13:07:29.915255
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from unittest.mock import patch

    wb = Mock()
    wb.get_option = Mock(return_value = True)

    with patch("thonny.plugins.pgzero_mode.get_workbench") as get_wb:
        get_wb.return_value = wb
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:39.985423
# Unit test for function update_environment
def test_update_environment():

    def dummy_get_variable(name):
        class Dummy:
            def get():
                return False
        return Dummy()

    def dummy_in_simple_mode():
        return True

    def dummy_get_option(name):
        return False

    get_workbench().get_variable = dummy_get_variable
    get_workbench().in_simple_mode = dummy_in_simple_mode
    get_workbench().get_option = dummy_get_option

    # Run the function once
    update_environment()

    # Check that the environment variable is set
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().in_simple_mode = lambda: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:07:50.849245
# Unit test for function update_environment
def test_update_environment():
    # Command called by Thonny's Turtle Graphics plugin
    # If pgzero is installed and enabled, pgzrun should be used instead of Python
    # Note: when running tests in Thonny, plugin has already been loaded
    if os.environ.get("PGZERO_MODE", "") == "":
        get_workbench().set_default(_OPTION_NAME, True)
        update_environment()
        assert os.environ.get("PGZERO_MODE", "") == "auto"

        get_workbench().set_default(_OPTION_NAME, False)
        update_environment()
        assert os.environ.get("PGZERO_MODE", "") == "0"
    else:
        old = os.environ.get("PGZERO_MODE", "")


# Generated at 2022-06-22 13:07:57.290804
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "True"
    assert get_workbench().get_variable(_OPTION_NAME).get()
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"
    assert not get_workbench().get_variable(_OPTION_NAME).get()

# Generated at 2022-06-22 13:08:02.743890
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    val = bool(get_workbench().get_option(_OPTION_NAME))
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) != val
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == val

# Generated at 2022-06-22 13:08:08.451855
# Unit test for function update_environment
def test_update_environment():
    if "PGZERO_MODE" in os.environ:
        del os.environ["PGZERO_MODE"]

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:38.040651
# Unit test for function toggle_variable
def test_toggle_variable():
    import thonny.globals

    # Create a test workbench
    test_workbench = thonny.globals.get_workbench()
    test_workbench.set_default(_OPTION_NAME, False)

    # Set the test variable to False -> toggle button is False
    var = test_workbench.get_variable(_OPTION_NAME)
    assert var.get() == False
    assert toggle_variable == 0

    # Set the test variable to True -> toggle button is True
    test_workbench.set_default(_OPTION_NAME, True)
    var = test_workbench.get_variable(_OPTION_NAME)
    assert var.get() == True
    assert toggle_variable == 1

# Generated at 2022-06-22 13:08:43.196098
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.enter_simple_mode()
    get_workbench().set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.leave_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:46.223820
# Unit test for function toggle_variable
def test_toggle_variable():
    try:
        toggle_variable()
    except Exception as e:
        print(e)
        
test_toggle_variable()
load_plugin()

# Generated at 2022-06-22 13:08:52.762448
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ.get("PGZERO_MODE", "") == "True"
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    assert os.environ.get("PGZERO_MODE", "") == "False"

# Generated at 2022-06-22 13:08:59.733678
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) is False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True
    # Shouldn't enable it in simple mode
    get_workbench().set_simple_mode()
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is False

# Generated at 2022-06-22 13:09:03.789466
# Unit test for function toggle_variable
def test_toggle_variable():
    d = get_workbench().get_variable(_OPTION_NAME)
    d.set(True)
    assert d.get() == True
    toggle_variable()
    assert d.get() == False
    toggle_variable()
    assert d.get() == True

# Generated at 2022-06-22 13:09:11.372991
# Unit test for function toggle_variable
def test_toggle_variable():
    # Reset the status of PygameZero
    get_workbench().set_variable(_OPTION_NAME, False)
    update_environment()
    # Set the status of PygameZero to True
    assert get_workbench().get_variable(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    # Set the status of PygameZero to False
    

# Generated at 2022-06-22 13:09:16.187050
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, False)

    assert not workbench.in_pgzero_mode()
    toggle_variable()
    assert workbench.in_pgzero_mode()
    toggle_variable()
    assert not workbench.in_pgzero_mode()

# Generated at 2022-06-22 13:09:22.056373
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:09:32.002455
# Unit test for function update_environment
def test_update_environment():

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

load_plugin()

# Generated at 2022-06-22 13:10:38.341465
# Unit test for function update_environment
def test_update_environment():
    from thonny.testing import empty_workbench
    from thonny.plugins.run.run_commands import RunCommand
    from thonny.globals import get_runner
    wb = empty_workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"



# Generated at 2022-06-22 13:10:43.791463
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert "PGZERO_MODE" in os.environ
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert "PGZERO_MODE" in os.environ
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:53.763342
# Unit test for function update_environment
def test_update_environment():
    get_workbench().disable_simple_mode()
    os.environ.pop("PGZERO_MODE", None)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().enable_simple_mode()
    os.environ.pop("PGZERO_MODE", None)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"


if __name__ == "__main__":
    import unittest.mock
    from thonny.workbench import Workbench

    unittest.mock.patch("thonny.workbench.Workbench", Workbench).start()
    get_workbench().disable_simple_mode()

#     get_workbench().disable_simple_mode()
#     assert toggle

# Generated at 2022-06-22 13:10:56.262397
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_variable(_OPTION_NAME)
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:11:06.753327
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock
    wb = mock.MagicMock()
    wb.get_variable.return_value.get.return_value = True
    wb.get_variable.return_value.set.return_value = True
    with mock.patch("thonny.plugins.pgzero_mode.get_workbench", return_value=wb):
        with mock.patch(
            "thonny.plugins.pgzero_mode.tr", lambda x: x
        ), mock.patch("thonny.plugins.pgzero_mode.os.environ") as mock_env:
            load_plugin()
            assert mock_env["PGZERO_MODE"] == "True"
            wb.set_default.assert_called_with("run.pgzero_mode", False)

# Generated at 2022-06-22 13:11:14.475760
# Unit test for function load_plugin
def test_load_plugin():
    wb = Workbench()
    wb.load_plugin_sources(TEST_CASES_DIR)


if __name__ == "__main__":
    load_plugin()
    get_workbench().run_command("toggle_pgzero_mode")
    print(get_workbench().get_option(_OPTION_NAME))
    get_workbench().run_command("toggle_pgzero_mode")
    print(get_workbench().get_option(_OPTION_NAME))

# Generated at 2022-06-22 13:11:15.758989
# Unit test for function toggle_variable
def test_toggle_variable():
    # no code currently
    pass

# Generated at 2022-06-22 13:11:22.091148
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert not wb.in_simple_mode()
    assert wb.get_option(_OPTION_NAME) == False

    update_environment()
    assert wb.in_simple_mode()
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:11:26.816549
# Unit test for function update_environment
def test_update_environment():
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:11:35.975717
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().test_mode()
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert get_workbench().get_variable(_OPTION_NAME) == False
    assert get_workbench().get_variable(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    # TODO: need to test with simple mode here