

# Generated at 2022-06-22 13:02:39.878454
# Unit test for function update_environment
def test_update_environment():
    class MockWorkbench:
        def in_simple_mode(self):
            return False
        
        def get_option(self, name):
            return True
    
    wb = MockWorkbench()
    assert os.environ.get("PGZERO_MODE", "") == ""

    wb.in_simple_mode = True
    update_environment()
    assert os.environ.get("PGZERO_MODE", "") == "auto"
    
    wb.in_simple_mode = False
    update_environment()
    assert os.environ.get("PGZERO_MODE", "") == "True"

# Generated at 2022-06-22 13:02:50.115874
# Unit test for function load_plugin
def test_load_plugin():
    """Load plugin and run load_plugin function"""
    import thonny

    # Load testing plugin
    load_plugin()

    # Initialise plugin and create a test window
    thonny._load_plugin_tests()
    test_window = thonny.create_test_window(globals())

    # Select menu command to add-remove a button to the tool bar
    test_window.run_command("toggle_pgzero_mode")
    test_window.update()

    # Get button from tool bar and check it has the correct icon and text
    button = test_window.get_button_from_command("toggle_pgzero_mode")

# Generated at 2022-06-22 13:03:01.660192
# Unit test for function update_environment
def test_update_environment():
    from io import StringIO
    from thonny import get_workbench
    from thonny.test.test_runner_configuration import get_runner_configuration
    from thonny.plugins.pygamezero import _OPTION_NAME

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert "PGZERO_MODE=False" in os.environ

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE=True" in os.environ

    get_workbench().set_simple_mode(True)
    update_environment()
    assert "PGZERO_MODE=auto" in os.environ

# Generated at 2022-06-22 13:03:11.879041
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import Mock
    from tkinter import BooleanVar
    wb = Mock()
    wb.in_simple_mode.return_value = False
    wb.get_variable.return_value = BooleanVar(value=False)
    wb.set_option.return_value = None
    wb.get_option.return_value = True
    with patch('thonny.plugins.pgzero_support.get_workbench',
               return_value=wb,
               create=True):
        toggle_variable()


# Generated at 2022-06-22 13:03:22.309765
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = ""
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    os.environ["PGZERO_MODE"] = ""
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:03:28.119570
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench

    get_workbench().destroy()
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os.environ.get("PGZERO_MODE", "True") == "False"



# Generated at 2022-06-22 13:03:35.154370
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.test_utils import macos_only
    from thonny import get_workbench
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.set_testing_mode(True)

# Generated at 2022-06-22 13:03:46.611969
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    original_wb = get_workbench()

# Generated at 2022-06-22 13:03:51.141439
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "True"
    assert get_workbench().in_simple_mode() == False

    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "False"
    assert get_workbench().in_simple_mode() == False


# Generated at 2022-06-22 13:03:56.934868
# Unit test for function load_plugin
def test_load_plugin():
    import sys
    from thonny.plugins.run import run_backend

    sys.modules["pgzrun"] = run_backend
    sys.modules["pgzero"] = run_backend
    load_plugin()


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:04:05.065673
# Unit test for function update_environment
def test_update_environment():
    assert os.environ["PGZERO_MODE"] == "0"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:04:06.246485
# Unit test for function load_plugin
def test_load_plugin():
    # TODO
    pass


# Generated at 2022-06-22 13:04:12.285218
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().in_simple_mode = lambda: True
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:18.317864
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_simple_mode(False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_simple_mode(True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "auto"

if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:04:21.368960
# Unit test for function update_environment
def test_update_environment():
    os.environ.clear()
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:29.718033
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_in_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:39.608570
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.languages import tr
    from thonny.workbench import Workbench
    from thonny.config import DEFAULT_CONFIG_DIR
    from os.path import join

    old_config_dir = get_workbench().get_option("common.config_dir")
    old_simple_mode = get_workbench().in_simple_mode()
    os.environ["PGZERO_MODE"] = ""
    load_plugin()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    assert os.environ["PGZERO_MODE"] == "False"
    assert get_workbench().in_simple_mode() == False

# Generated at 2022-06-22 13:04:51.377665
# Unit test for function load_plugin
def test_load_plugin():
    wb = Workbench()
    get_runner = wb.get_runner
    wb.set_runner(lambda: None)

# Generated at 2022-06-22 13:04:53.994557
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:05:05.443543
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.common import InlineCommand
    from thonny.plugins.run.pgzero_mode import load_plugin
    import os

    os.environ["PGZERO_MODE"] = "auto"
    workbench = get_workbench()
    options = workbench.get_variable("Options")
    load_plugin()
    assert options.get("run.pgzero_mode") == False
    assert workbench.in_simple_mode() == False
    assert os.environ["PGZERO_MODE"] == "False"
    workbench.execute("toggle_pgzero_mode")
    assert os.environ["PGZERO_MODE"] == "True"
    command = InlineCommand("run", "toggle_pgzero_mode")
    assert command.get_flag_name

# Generated at 2022-06-22 13:05:19.438023
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    var = wb.get_variable(_OPTION_NAME)
    assert not var
    assert not "PGZERO_MODE" in os.environ

    load_plugin()

    assert var
    assert var.get_name() == _OPTION_NAME
    assert var.get_value() == False
    assert wb.get_option(_OPTION_NAME) == False
    assert "PGZERO_MODE" in os.environ

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    w

# Generated at 2022-06-22 13:05:29.851977
# Unit test for function toggle_variable
def test_toggle_variable():
    import unittest.mock
    
    workbench = unittest.mock.Mock()
    workbench.get_variable = unittest.mock.MagicMock()
    get_workbench.cache_clear()
    get_workbench.cache = lambda: workbench
    
    # Test case 1: internal variable is False
    workbench.get_variable.return_value.get.return_value = False
    toggle_variable()
    workbench.set_variable.assert_called_once_with(_OPTION_NAME, True)
    
    # Test case 2: internal variable is True
    workbench.reset_mock()
    workbench.get_variable.return_value.get.return_value = True
    toggle_variable()

# Generated at 2022-06-22 13:05:38.272760
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench
    from thonny.languages import EnglishLanguagePack
    from thonny.globals import set_language_pack
    from thonny.plugins.pgzeromode.pgzeromode import toggle_variable

    workbench = get_workbench()
    workbench.set_variable("run.pgzero_mode", True)
    set_language_pack(EnglishLanguagePack())
    
    assert workbench.get_variable("run.pgzero_mode") == True
    
    toggle_variable()
    
    assert workbench.get_variable("run.pgzero_mode") == False

# Generated at 2022-06-22 13:05:49.578998
# Unit test for function load_plugin
def test_load_plugin():
    #Clear the workbench
    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_in_simple_mode(False)
    get_workbench().destroy_window()

    #Load the plugin
    load_plugin()

    #Check that the command has been added and that the option value is False
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    assert get_workbench().get_command("toggle_pgzero_mode") != None

    #Check that the environment variable has been set
    assert os.environ["PGZERO_MODE"] == "False"

    #Check that in simple mode the environment variable defaults to True
    get_workbench().set_in_simple_mode

# Generated at 2022-06-22 13:05:57.046661
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock

    os.environ = {}  # use a clean dict for testing
    wb = mock.Mock()

    wb.in_simple_mode.return_value = False
    wb.get_option = mock.Mock(_OPTION_NAME, return_value=True)
    get_workbench().set_workbench(wb)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.in_simple_mode.return_value = True
    wb.get_option = mock.Mock(_OPTION_NAME, return_value=True)
    get_workbench().set_workbench(wb)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:07.902013
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from unittest.mock import MagicMock

    wb = Workbench()
    wb.get_option = MagicMock(return_value=True)
    wb.in_simple_mode = MagicMock(return_value=False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == str(wb.get_option(_OPTION_NAME))

    # Enter simple mode
    wb.in_simple_mode = MagicMock(return_value=True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:12.385139
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_variable(_OPTION_NAME, True)
    load_plugin()
    assert wb.in_simple_mode() is False
    assert wb.get_option(_OPTION_NAME) is True

# Generated at 2022-06-22 13:06:19.380932
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest import mock
    
    get_workbench = mock.MagicMock()
    set_variable = get_workbench().get_variable().set

    toggle_variable()
    set_variable.assert_called_once_with(True)

    set_variable.reset_mock()
    toggle_variable()
    set_variable.assert_called_once_with(False)

    set_variable.reset_mock()
    toggle_variable()
    set_variable.assert_called_once_with(True)


# Generated at 2022-06-22 13:06:27.746275
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_in_simple_mode(True)
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:33.937585
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock
    from thonny.common import THONNY_USER_DIR

    with mock.patch("thonny.globals.Variable") as MockVariable:
        MockVariable.reset_mock()
        load_plugin()
    assert os.path.exists(os.path.join(THONNY_USER_DIR, "config-v2.json"))
    assert MockVariable.called

# Generated at 2022-06-22 13:06:39.938195
# Unit test for function toggle_variable
def test_toggle_variable():
    assert toggle_variable() == None

# Generated at 2022-06-22 13:06:44.698932
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    wb.execute_command("toggle_pgzero_mode")
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "False"
    wb.execute_command("toggle_pgzero_mode")
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:49.139603
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) == False
    get_workbench().set_variable(_OPTION_NAME, True)
    #toggle_variable()
    #assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:07:00.703548
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.globals import get_workbench, get_runner
    get_workbench().set_simple_mode(True)
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    get_workbench().set_simple_mode(False)
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    toggle_variable()

# Generated at 2022-06-22 13:07:05.372112
# Unit test for function load_plugin
def test_load_plugin():
    assert "toggle_pgzero_mode" in get_workbench().commands
    assert (
        get_workbench().commands["toggle_pgzero_mode"]["label"] == tr("Pygame Zero mode")
    )
# Unittest for function toggle_variable

# Generated at 2022-06-22 13:07:13.184884
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:19.289283
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop("PGZERO_MODE", None)
    assert os.getenv("PGZERO_MODE") is None
    update_environment()
    assert os.getenv("PGZERO_MODE") == "False"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "True"

# Generated at 2022-06-22 13:07:24.196025
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    load_plugin()
    assert wb.get_default(_OPTION_NAME) == True
    assert "PGZERO_MODE" in os.environ

# Generated at 2022-06-22 13:07:31.739669
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False


if __name__ == "__main__":
    print(os.environ.get("PGZERO_MODE"))
    load_plugin()
    print(os.environ.get("PGZERO_MODE"))

# Generated at 2022-06-22 13:07:40.986252
# Unit test for function load_plugin
def test_load_plugin():
    # set the test mode for Thonny
    os.environ["THONNY_TEST_RUN"] = "1"
    # load the module
    from thonny.plugins.pgzero import load_plugin

    # call the function under test
    load_plugin()

    workbench = get_workbench()
    var = workbench.get_variable(_OPTION_NAME)
    assert not var.get()
    assert os.environ["PGZERO_MODE"] == "False"
    # assert that the command is registered
    cmd = workbench.get_command("toggle_pgzero_mode")
    assert cmd is not None

    # call the command
    cmd()

    # test the command
    assert var.get()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:00.177723
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from thonny import ui_utils
    from thonny.shell import ShellTextWidget
    from thonny.misc_utils import running_on_mac_os
    import tkinter as tk
    workbench = Workbench()
    workbench.set_default("run.pgzero_mode", True)
    workbench.create()
    workbench.register_default_shell("test_shell", ShellTextWidget)
    workbench.add_command("toggle_pgzero_mode","run",tr("Pygame Zero mode"),toggle_variable,flag_name=_OPTION_NAME,group=40,)
    text_widget = workbench.get_default_shell()
    assert(not text_widget._is_pgzero_mode)
    toggle_variable()

# Generated at 2022-06-22 13:08:05.644353
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:17.231976
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench
    from unittest.mock import MagicMock
    from thonny.workbench import Workbench
    from thonny.workbench import get_runner, get_runner_command
    from thonny.workbench import get_variable, set_variable
    from thonny.workbench import get_option, set_default_option
    from thonny.workbench import add_command
    from thonny.globals import get_workbench
    from thonny.languages import tr
    import os

    # TODO: I don't know how to mock the GUI

# Generated at 2022-06-22 13:08:23.042414
# Unit test for function load_plugin
def test_load_plugin():
    # test load_plugin function
    from thonny.plugins.pgz_mode import load_plugin
    from thonny.workbench import Workbench

    workbench = Workbench()
    load_plugin()
    assert workbench.get_option(_OPTION_NAME) == False
    assert workbench.get_command("toggle_pgzero_mode") is not None


# Generated at 2022-06-22 13:08:28.964364
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_simple_mode(False)

    var = get_workbench().get_variable(_OPTION_NAME)
    assert var.get() is False

    get_workbench().set_simple_mode(True)

    var = get_workbench().get_variable(_OPTION_NAME)
    assert var.get() is True

# Generated at 2022-06-22 13:08:29.714714
# Unit test for function toggle_variable

# Generated at 2022-06-22 13:08:39.073382
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from thonny.misc_utils import running_on_mac_os, running_on_windows
    wb = Workbench()

    get_workbench().set_option(_OPTION_NAME, False)
    load_plugin()

    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_option(_OPTION_NAME, True)
    load_plugin()

    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "1"

    wb.in_simple_mode = lambda: True
    load_plugin()

    assert "PGZERO_MODE" in os.environ
    assert os.environ

# Generated at 2022-06-22 13:08:50.437682
# Unit test for function update_environment
def test_update_environment():
    from test.test_base import run_fake_ui
    run_fake_ui(lambda: update_environment())
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().in_simple_mode = lambda: False
    run_fake_ui(lambda: update_environment())
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().in_simple_mode = lambda: False
    run_fake_ui(lambda: update_environment())
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_default(_OPTION_NAME, True)
    get_

# Generated at 2022-06-22 13:08:54.511231
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_in_simple_mode(True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_in_simple_mode(False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:09:05.981806
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench
    from thonny.config_ui import TkVariable
    from unittest.mock import Mock
    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.in_simple_mode = Mock(return_value=False)
    wb.get_option = Mock(return_value=False)
    wb.get_variable = Mock(return_value=TkVariable(wb.get_option(_OPTION_NAME)))
    wb.add_command = Mock()
    os.environ["PGZERO_MODE"] = "False"
    load_plugin()
    toggle_variable()
    assert os.environ.get("PGZERO_MODE", "True") == "True"
    toggle_variable()
    assert os

# Generated at 2022-06-22 13:09:35.936103
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    old_get_option = Workbench.get_option

    def get_option(self, name):
        if name == _OPTION_NAME:
            return False
        else:
            return old_get_option(self, name)

    old_set_default = Workbench.set_default

    def set_default(self, name, value):
        if name == _OPTION_NAME:
            pass
        else:
            old_set_default(self, name, value)

    Workbench.get_option = get_option
    Workbench.set_default = set_default
    import os

    old_environ = os.environ
    os.environ = {"PGZERO_MODE": "auto"}

    load_plugin()


# Generated at 2022-06-22 13:09:39.886643
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from unittest.mock import Mock
    wb=Workbench()
    wb.add_command = Mock()
    wb.set_default = Mock()
    load_plugin()
    assert wb.add_command.call_count==1

# Generated at 2022-06-22 13:09:49.668832
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.workbench import Workbench
    from thonny.memory import get_shared_memory_dict
    
    shared_memory_dict = get_shared_memory_dict()
    workbench = Mock(spec=Workbench)
    workbench.get_variable = get_shared_memory_dict().__getitem__
    workbench.get_option = get_shared_memory_dict().__getitem__
    workbench.in_simple_mode.return_value = False
    workbench.set_default.side_effect = shared_memory_dict.__setitem__
    workbench.add_command.return_value = None
    load_plugin(workbench)
    assert "PGZERO_MODE" in os.environ

# Generated at 2022-06-22 13:09:58.576135
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "1"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "0"
    wb.set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:10:01.536549
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:06.660524
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:10:10.652130
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    workbench = Workbench()
    load_plugin()

    # check commands
    assert workbench.get_variable(_OPTION_NAME)
    assert workbench.commands["toggle_pgzero_mode"]



# Generated at 2022-06-22 13:10:17.740503
# Unit test for function update_environment
def test_update_environment():
    from test.config_helper import get_test_config_dir

    config_dir = get_test_config_dir()
    os.environ["XDG_CONFIG_HOME"] = config_dir
    os.environ["THONNY_USER_DIR"] = config_dir
    os.environ["THONNY_WORK_DIR"] = config_dir
    

# Generated at 2022-06-22 13:10:29.096619
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    import thonny
    from thonny.languages import english as en

    thonny.WORKBENCH = mock.Mock()
    thonny.WORKBENCH.in_simple_mode.return_value = False
    thonny.WORKBENCH.get_option = mock.Mock(return_value=False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"  # False

    thonny.WORKBENCH.get_option.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"  # True

    thonny.WORKBENCH.in_simple_mode.return_value = True
    update_environment()
    assert os.environ

# Generated at 2022-06-22 13:10:37.797637
# Unit test for function update_environment
def test_update_environment():
    import os
    from thonny import get_workbench
    from thonny.workbench import Workbench
    workbench = Workbench()
    workbench.reset_commands()
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert "PGZERO_MODE" not in os.environ
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"


# Generated at 2022-06-22 13:11:43.200600
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop('PGZERO_MODE', None)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ['PGZERO_MODE'] == '0'
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ['PGZERO_MODE'] == '1'

# Generated at 2022-06-22 13:11:54.194353
# Unit test for function load_plugin
def test_load_plugin():
    # Set to a clean state
    get_workbench().set_default("run.pgzero_mode", False)
    get_workbench().set_default("run.debugger", "auto")

    # Fake an environment, so that simple mode is not used
    thonny_env = os.environ["THONNY"]
    os.environ["THONNY"] = "1"
    get_workbench().set_default("run.pgzero_mode", True)
    get_workbench().set_default("run.debugger", "auto")
    load_plugin()
    os.environ["THONNY"] = thonny_env

    # Check that default value is set correctly
    # In this case, the highlighter cannot run
    # and pgzero mode is disabled

# Generated at 2022-06-22 13:12:02.310194
# Unit test for function toggle_variable
def test_toggle_variable():
    try:
        os.environ["PGZERO_MODE"]
    except KeyError:
        pgzero_mode = None
        pgzero_mode_env = None
    else:
        pgzero_mode = os.environ.get("PGZERO_MODE")
        pgzero_mode_env = os.environ.get("PGZERO_MODE")

    workbench = get_workbench()
    var = workbench.get_variable(_OPTION_NAME)
    var.set(True)
    # Without any environment variables set and simple mode disabled, pgzero_mode is True and PGZERO_MODE is set to True
    if not os.environ.get("PGZERO_MODE"):
        update_environment()
        assert os.environ.get("PGZERO_MODE") == "True"
    # pgzero_

# Generated at 2022-06-22 13:12:07.270036
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.ui_utils import OptionSubMenu
    from tkinter import Tk
    from thonny.plugins.run import RunView
    from thonny import get_workbench
    Tk().withdraw()
    get_workbench().set_default("run.pgzero_mode", False)
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_default("run.pgzero_mode", True)
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_default("run.pgzero_mode", False)
    assert os.environ["PGZERO_MODE"] == "False"
    # check environment variable when in simple mode
    get_workbench().set_simple

# Generated at 2022-06-22 13:12:18.732189
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest import mock
    from thonny.config import get_workbench

    # Create the mock object
    workbench = mock.MagicMock()

    # Use the get_workbench function from tkgui.py to give the mock object
    # as a return value to the get_workbench function we are using.
    # This means that when we call get_workbench() on the line below,
    # it will use the mocked object instead.
    get_workbench.return_value = workbench

    # For testing, we set the assertions flag to False.
    # Otherwise, it will raise an error when it is called
    # before it is asserted.
    workbench.set_default.assert_called_once_with = False
    workbench.get_option.assert_called_once_with = False

    # Call the function


# Generated at 2022-06-22 13:12:23.731880
# Unit test for function toggle_variable
def test_toggle_variable():
    # Toggle once
    os.environ["PGZERO_MODE"] = "auto"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

    # Toggle twice
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:12:26.768918
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert "toggle_pgzero_mode" in get_workbench().get_variable(_OPTION_NAME)._observers
    assert "run.toggle_pgzero_mode" in get_workbench().commands

# Generated at 2022-06-22 13:12:28.919356
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench
    
    workbench.clear_test_data()
    load_plugin()
    assert workbench.get_option(_OPTION_NAME) == False