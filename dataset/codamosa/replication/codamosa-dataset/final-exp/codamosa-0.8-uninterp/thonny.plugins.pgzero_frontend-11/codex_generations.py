

# Generated at 2022-06-22 13:02:42.186751
# Unit test for function update_environment
def test_update_environment():
    from thonny.common import InlineCommand
    from unittest.mock import patch
    from thonny import get_workbench
    from thonny.tktextext import TextFrame
    from tkinter import Tk
    from thonny.shell import ShellView
    from thonny.shell import ShellText

    def command_for_shell(command):
        view = get_workbench().get_view("ShellView")
        view._run_command(InlineCommand(command, "Shell"))

    root = Tk()
    shell = ShellView(root)
    shell.text = TextFrame(root)
    text = ShellText(root)
    shell.text.text_frame.text = text
    shell.text.text_frame.insert("end", ">>> ")
    shell.text.text_frame.text

# Generated at 2022-06-22 13:02:45.858887
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    test_config = wb.get_option(_OPTION_NAME)
    assert test_config == False
    assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2022-06-22 13:02:54.450598
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_simple_mode(False)
    os.environ["PGZERO_MODE"] = "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_simple_mode(True)
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:03:04.618218
# Unit test for function update_environment
def test_update_environment():
    w = get_workbench()
    w.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    
    w.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    w.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    w.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:03:12.183236
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import (
        running_on_mac_os,
        running_on_linux,
        running_on_windows,
    )

    if running_on_mac_os() or running_on_linux():
        get_workbench().set_option(_OPTION_NAME, False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"
    elif running_on_windows():
        get_workbench().set_option(_OPTION_NAME, False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
        get_workbench().set_option(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:21.640522
# Unit test for function load_plugin
def test_load_plugin():
    from tests.test_base import get_test_tk_root
    from thonny import get_workbench
    from thonny.workbench import Workbench
    root = get_test_tk_root()
    WB = Workbench(root)
    WB.create_contents()
    WB.enable_simple_mode(False)
    load_plugin()
    assert "toggle_pgzero_mode" in WB.get_menu("run")._name_to_item
    assert get_workbench().get_option(_OPTION_NAME) == False



# Generated at 2022-06-22 13:03:25.309596
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default("run.pgzero_mode", False)
    load_plugin()
    assert get_workbench().in_simple_mode() is False
    toggle_variable()
    assert get_workbench().in_simple_mode() is True

# Generated at 2022-06-22 13:03:26.279688
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()


# Generated at 2022-06-22 13:03:35.367588
# Unit test for function update_environment
def test_update_environment():
    from test.test_base import FakeTk
    from thonny.memory import PythonProcessMemory
    tk = FakeTk()
    get_workbench().create(tk)
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    # Also test that it doesn't break if environment variable is already set by another library
    os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:03:46.645658
# Unit test for function update_environment
def test_update_environment():
    from thonny.globals import get_runner
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.insert_command("set_simple_mode")
    update_environment()
    assert get_runner().get_environ()["PGZERO_MODE"] == "auto"

    wb.insert_command("set_simple_mode")
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert get_runner().get_environ()["PGZERO_MODE"] == "auto"

    wb.insert_command("set_simple_mode")
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()

# Generated at 2022-06-22 13:04:01.288580
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().in_simple_mode = lambda: False
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:04.800572
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    #flag_name="run.pygame_zero_mode"
    #group=40

# Generated at 2022-06-22 13:04:14.966203
# Unit test for function update_environment
def test_update_environment():
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import test_runner
    import thonny
    thonny.add_workbench_options = lambda *args : None
    thonny._load_configuration = lambda *args : None
    load_plugin()
    toggle_variable()
    update_environment()
    test_runner.run_tests(get_workbench().get_plugin_loader())
    if os.environ["PGZERO_MODE"] == "True":
        os.environ["PGZERO_MODE"] = "True"
    else:
        os.environ["PGZERO_MODE"] = "False"

if __name__ == "__main__":
    test_update_environment()

# Generated at 2022-06-22 13:04:26.913577
# Unit test for function update_environment
def test_update_environment():
    def assert_env_is_set(result_val):
        assert os.environ["PGZERO_MODE"] == str(result_val)

    old_env = dict(os.environ)

# Generated at 2022-06-22 13:04:37.434998
# Unit test for function toggle_variable
def test_toggle_variable():
    print("")
    print("Running unittest for toggle_variable function:")
    # Initialize test variables
    var_pgzero_mode = False  # variable to store state of pgzero_mode
    # Check initial state of plugin
    print("Initial state of plugin:")
    print("PGZERO_MODE = ", os.environ["PGZERO_MODE"])
    print("Starting automated test")
    toggle_variable()
    print("Toggled PGZERO_MODE:")
    print("PGZERO_MODE = ", os.environ["PGZERO_MODE"])
    # Confirm that state has changed.
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    print("Toggled PGZERO_MODE again:")

# Generated at 2022-06-22 13:04:46.870881
# Unit test for function update_environment
def test_update_environment():
    b = get_workbench()
    os.environ["PGZERO_MODE"] = ""
    # in simple mode
    b.set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    # in normal mode
    b.set_normal_mode()
    os.environ["PGZERO_MODE"] = ""
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"
    os.environ["PGZERO_MODE"] = ""
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:04:56.675105
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)
    get_workbench().set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    get_workbench().set_option("run.pgzero_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:05:04.297782
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:05:14.778974
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.plugins.pgzero_mode import load_plugin
    from thonny.workbench import Workbench
    mock_workbench  = Mock(spec=Workbench)
    mock_workbench.get_variable = Mock(return_value=True)
    mock_workbench.get_option = Mock(return_value=True)
    mock_workbench.set_default = Mock(return_value=True)
    mock_workbench.in_simple_mode = Mock(return_value=True)
    mock_workbench.add_command = Mock(return_value=True)
    mock_workbench.bind("<Configure>")
    Workbench._instance = mock_workbench
    load_plugin()

# Generated at 2022-06-22 13:05:24.779764
# Unit test for function load_plugin
def test_load_plugin():
    global get_workbench
    get_workbench = lambda : None
    
    class Workbench:
        def __init__(self):
            self.variables = {
                _OPTION_NAME: None
            }
            self.variables["run.pgzero_mode"] = BooleanVar(None, False)
            
        def add_command(self, x, y, z, a, flag_name, group):
            pass
        
    get_workbench = lambda : Workbench()
    
    from thonny import get_workbench
    load_plugin()
    assert(get_workbench().variables[_OPTION_NAME].get() == False)
    get_workbench().variables[_OPTION_NAME].set(True)
    assert(get_workbench().variables[_OPTION_NAME].get() == True)

# Generated at 2022-06-22 13:05:36.365749
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:05:39.250339
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:05:39.844801
# Unit test for function update_environment
def test_update_environment():
    update_environment()

# Generated at 2022-06-22 13:05:51.244515
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench
    wb = workbench.get_workbench()
    wb.destroy_editors()
    wb.unload_plugin("thonny.plugins.pgzero_mode")
    wb.unload_plugin("thonny.plugins.pgzrun")

    assert not wb.in_simple_mode()
    assert "PGZERO_MODE" not in os.environ

    load_plugin()
    assert not wb.get_variable("run.pgzero_mode").get()
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    assert wb.get_variable("run.pgzero_mode").get()
    assert os.environ["PGZERO_MODE"] == "True"


# Generated at 2022-06-22 13:06:01.503428
# Unit test for function update_environment
def test_update_environment():
    # Test if PGZERO_MODE is set correctly based on the _OPTION_NAME parameter in
    # simple mode and normal mode.
    os.environ.pop("PGZERO_MODE", None)
    get_workbench().set_simple_mode(True)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "auto"

    os.environ.pop("PGZERO_MODE", None)
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:06:08.340813
# Unit test for function update_environment
def test_update_environment():
    # Case 1: PGZERO_MODE when workbench is in simple mode
    get_workbench().set_option(_OPTION_NAME, True)
    get_workbench().set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Case 2: PGZERO_MODE when workbench is in normal mode
    get_workbench().set_normal_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:10.889307
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False



# Generated at 2022-06-22 13:06:12.439541
# Unit test for function toggle_variable
def test_toggle_variable():
    _toggle_variable()
    assert _OPTION_NAME in get_workbench().get_default_options()
    assert get_workbench().get_option(_OPTION_NAME) == False
    
test_toggle_variable()

# Generated at 2022-06-22 13:06:13.027157
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:06:17.543417
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:06:34.952586
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_variable(_OPTION_NAME, True)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:40.328608
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    load_plugin()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:06:48.276603
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.misc_utils import running_on_linux
    from thonny.globals import get_runner
    from thonny.plugins.run import PGZERORunner

    get_workbench().in_simple_mode = lambda: False  # overwrite
    get_workbench().get_option = lambda name: True  # overwrite

    # Mock runner (not mocking its update_environment function)
    runner = Mock()
    runner.update_environment = PGZERORunner.update_environment
    get_runner().change_runner(runner)

    update_environment()
    assert 'PGZERO_MODE=True' in get_runner().update_environment()

    if not running_on_linux():
        assert 'PGZERO_MODE=True' in get_runner().get

# Generated at 2022-06-22 13:06:52.331789
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    var = get_workbench().get_variable(_OPTION_NAME)
    assert var.get() == False
    var.set(True)
    load_plugin()
    assert var.get() == True

# Generated at 2022-06-22 13:07:02.777296
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import patch
    from thonny import get_workbench, get_shell

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode(True)
    update_environment()
    assert "PGZERO_MODE=auto" in get_shell().popen.mock_calls[-2]

    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_simple_mode(False)
    update_environment()
    assert "PGZERO_MODE=True" in get_shell().popen.mock_calls[-2]

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode(False)
    update_environment

# Generated at 2022-06-22 13:07:05.546394
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench

    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()



# Generated at 2022-06-22 13:07:15.866898
# Unit test for function load_plugin
def test_load_plugin():
    with test_utils.test_mock_frontend() as test_mock:
        load_plugin()
        assert isinstance(test_mock.master._menu.find_child("run", "toggle_pgzero_mode"), tkinter.Checkbutton)
        assert test_mock.get_option(_OPTION_NAME) == False
        assert os.environ["PGZERO_MODE"] == "False"
        toggle_variable()
        assert test_mock.get_option(_OPTION_NAME) == True
        assert os.environ["PGZERO_MODE"] == "True"
        test_mock.set_simple_mode()
        assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:27.504887
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from unittest.mock import Mock, patch
    from thonny.config_ui import VariablesFrame
    from thonny.config_manager import ConfigurationManager
    from thonny.plugins.configure import ConfigurationDialog, get_configuration_manager
    configuration_manager = get_configuration_manager()
    run_group = configuration_manager.create_configuration_group("run")
    run_group.create_variable("pgzero_mode", False)
    workbench = Workbench()
    workbench.set_simple_mode(False)
    configuration_dialog = Mock(spec=ConfigurationDialog)
    variables_frame = Mock(spec=VariablesFrame)
    configuration_dialog.add_variable = Mock()

# Generated at 2022-06-22 13:07:33.473220
# Unit test for function load_plugin
def test_load_plugin():
    # In order to be able to run tests inside a python package one
    # must trick the package into thinking that there is a workbench
    # to use.
    # http://stackoverflow.com/a/26847690
    import thonny.workbench
    thonny.workbench.Workbench(None, None, "test")
    # load the plugin
    load_plugin()
    # check that plugin was installed
    assert get_workbench()["toggle_pgzero_mode"] != None


# Generated at 2022-06-22 13:07:40.575161
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
    updates = update_environment()
    assert updates
    assert updates["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:03.029019
# Unit test for function toggle_variable
def test_toggle_variable():
    assert(toggle_variable() == None)

# Generated at 2022-06-22 13:08:07.488301
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, True)
    assert "PGZERO_MODE" not in os.environ
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    workbench.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:13.586987
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:14.700519
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()


# Generated at 2022-06-22 13:08:20.475258
# Unit test for function toggle_variable
def test_toggle_variable():
    # First time disable the plugin, second time enable it again
    get_workbench().set_default("run.pgzero_mode", False)
    assert get_workbench().get_option("run.pgzero_mode") == False
    toggle_variable()
    assert get_workbench().get_option("run.pgzero_mode") == True

# Generated at 2022-06-22 13:08:25.087577
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:35.183764
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from thonny.globals import get_workbench
    from unittest.mock import patch
    from thonny.config import get_config_dir, get_config_file_path

    with patch("unittest_plugin.update_environment"), patch("unittest_plugin.toggle_variable"), patch("unittest_plugin.get_workbench"), patch("unittest_plugin.get_workbench"):
        Workbench().get_variable(_OPTION_NAME).set(False)
        load_plugin()
        assert toggle_variable._func_code is toggle_variable.__code__ # pylint: disable=protected-access
        toggle_variable()
        update_environment()


# Generated at 2022-06-22 13:08:40.395592
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    load_plugin()
    assert _OPTION_NAME in wb.get_defaults()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_option(_OPTION_NAME, True)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:43.962417
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import running_on_mac_os, running_on_linux, running_on_windows
    if running_on_windows():
        return
    if running_on_linux():
        return
    if running_on_mac_os():
        return

# Generated at 2022-06-22 13:08:54.691358
# Unit test for function update_environment
def test_update_environment():
    old_environ = os.environ.copy()
    try:
        # in simple mode it should be set to auto
        from thonny.main import simple_mode
        simple_mode(True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"

        # in normal mode it should be set to the value of preference
        from thonny.main import simple_mode
        simple_mode(False)
        get_workbench().set_option(_OPTION_NAME, False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"

        get_workbench().set_option(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"

    finally:
        os

# Generated at 2022-06-22 13:09:24.222283
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.globals import get_runner
    get_workbench().set_default("python_path", "python3")

    toggle_variable()
    assert get_runner().get_env()["PGZERO_MODE"] == "True"

    toggle_variable()
    assert get_runner().get_env()["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:09:35.520625
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    wb = Workbench()
    wb.set_default("run.pgzero_mode", False)
    wb.set_default("view.simple_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    wb.set_option("view.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    
    wb.set_option("view.simple_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    wb.set_option("run.pgzero_mode", True)
    update_environment()

# Generated at 2022-06-22 13:09:38.900530
# Unit test for function update_environment
def test_update_environment():
    from test.config_helper import get_workbench
    from importlib import reload
    reload(get_workbench)
    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, False)
    update_environment()

# Generated at 2022-06-22 13:09:49.364787
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import MagicMock

    wb = MagicMock()
    wb.in_simple_mode.return_value = True
    wb.get_variable.return_value.get.return_value = False
    wb.get_option.return_value = False

    with patch("thonny.plugins.pgzero.run.get_workbench", return_value = wb):
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "auto"
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "True"
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "auto"
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "False"
        toggle_

# Generated at 2022-06-22 13:09:52.738981
# Unit test for function toggle_variable
def test_toggle_variable():
    import unittest
    import thonny
    from thonny.workbench import Workbench

    class Test(unittest.TestCase):
        def test_default(self):
            root = Workbench().get_variable("run.pgzero_mode")
            self.assertEqual(root.get(), False)

    from thonny import workbench
    workbench.set_variable("run.pgzero_mode", True)
    unittest.main(argv=[__file__, "Test"])

# Generated at 2022-06-22 13:09:55.233837
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    assert load_plugin() is None

# Generated at 2022-06-22 13:09:57.928440
# Unit test for function load_plugin
def test_load_plugin():
    # This function is called at the start and end of the test suite
    # I would like to create a clean environment for each test
    # but it seems that this is not possible in Thonny
    pass

# Generated at 2022-06-22 13:10:01.249042
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False



# Generated at 2022-06-22 13:10:04.739327
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:08.340875
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_variable(_OPTION_NAME, True)
    toggle_variable()
    assert not get_workbench().get_variable(_OPTION_NAME)
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME)

# Generated at 2022-06-22 13:11:11.486024
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock
    from thonny.config import get_workbench
    from thonny.plugins.pgzero_mode import update_environment

    workbench = get_workbench()
    workbench.set_default = MagicMock()
    workbench.set_default.assert_not_called()
    workbench.get_variable = MagicMock(return_value=True)

    update_environment()
    os.environ["PGZERO_MODE"].should.be.equal("True")
    workbench.set_default.assert_called_once_with(
        "run.pgzero_mode", False, show_in_config=True
    )

# Generated at 2022-06-22 13:11:14.173077
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    workbench = get_workbench()
    workbench.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    workbench.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:11:15.747097
# Unit test for function update_environment
def test_update_environment():
  get_workbench().set_in_simple_mode(True)
  update_environment()
  assert os.environ["PGZERO_MODE"] == "auto"

  get_workbench().set_in_simple_mo

# Generated at 2022-06-22 13:11:21.720472
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "unknown"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:11:30.151580
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(False)
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:11:31.127153
# Unit test for function toggle_variable
def test_toggle_variable():
    print(toggle_variable())

# Generated at 2022-06-22 13:11:41.764852
# Unit test for function load_plugin
def test_load_plugin():
    # If I import the plugin, the command should be registered
    load_plugin()
    assert get_workbench().default_commands["toggle_pgzero_mode"]

    # If I enable it, then I should enter on PygameZero mode
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "True"

    # If I disable it, then I should enter on PygameZero mode
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "False"

    # When I am in simple mode, then I should be on auto

# Generated at 2022-06-22 13:11:48.785554
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import TestCase, mock
    from thonny import get_workbench

    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)

    with mock.patch("thonny.plugins.pgzero_mode.get_workbench") as g:
        g.return_value = wb
        load_plugin()
        assert g.called

    # check if the command is added
    assert wb.get_commands().get("toggle_pgzero_mode")


# Generated at 2022-06-22 13:11:52.266163
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:12:02.647582
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from thonny.globals import get_runner
    from thonny.config import get_workbench_configuration

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    assert get_workbench_configuration()["run.pgzero_mode"] == "False"
    assert os.environ["PGZERO_MODE"] == "False"
    
    # Toggle mode
    get_workbench().event_generate("TogglePgzeroMode")