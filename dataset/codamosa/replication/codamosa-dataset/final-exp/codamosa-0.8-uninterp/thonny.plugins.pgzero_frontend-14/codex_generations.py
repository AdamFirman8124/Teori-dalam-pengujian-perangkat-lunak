

# Generated at 2022-06-22 13:02:32.629898
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()

# Generated at 2022-06-22 13:02:37.030438
# Unit test for function load_plugin
def test_load_plugin():
    from test.test_base import get_test_configuration
    from thonny.workbench import Workbench
    from thonny.plugins.pgzero_mode import _OPTION_NAME

    wb = Workbench(get_test_configuration())
    assert get_workbench().get_option(_OPTION_NAME) is False
    wb.destroy()

# Generated at 2022-06-22 13:02:43.684180
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench().create_test_workbench(gui=False)
    var = wb.get_variable(_OPTION_NAME)
    var.set(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    var.set(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    wb.in_simple_mode.set(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:02:44.557332
# Unit test for function load_plugin
def test_load_plugin():
    assert load_plugin() == None

# Generated at 2022-06-22 13:02:47.828232
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert get_workbench().get_variable(_OPTION_NAME) != None
    assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2022-06-22 13:02:56.134807
# Unit test for function update_environment
def test_update_environment():
    workbench = get_workbench()
    assert workbench.in_simple_mode() == False
    assert os.environ.get("PGZERO_MODE") == "False"
    workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "True"
    workbench.set_option(_OPTION_NAME, False)
    workbench.set_option("view.simple_mode", True)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "auto"
    workbench.set_option("view.simple_mode", False)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:03:07.863773
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from thonny import get_shell, get_running_backend, THONNY_USER_DIR
    import os
    import shutil
    import tempfile
    import sys

    tmp_dir = tempfile.mkdtemp()
    get_workbench().set_variable("USER_DIR", tmp_dir)
    os.environ["THONNY_USER_DIR"] = tmp_dir
    w = Workbench()
    w.create()
    # w.event_generate("<<NewWindow>>")
    # w.event_generate("<<NewFile>>")
    # w.event_generate("<<Save>>")

    get_workbench().set_default(_OPTION_NAME, False)

# Generated at 2022-06-22 13:03:11.390069
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, True)
    wb = get_workbench()
    assert wb.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:03:23.994349
# Unit test for function update_environment
def test_update_environment():
    for simple_mode in (False, True):
        wb = get_workbench()

        wb._get_config_var = lambda: None
        wb.in_simple_mode = lambda: simple_mode
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"

        wb._get_config_var = lambda: True
        wb.in_simple_mode = lambda: simple_mode
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"

        wb._get_config_var = lambda: False
        wb.in_simple_mode = lambda: simple_mode
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"

        wb._get_config_var = lambda: 0
       

# Generated at 2022-06-22 13:03:28.368775
# Unit test for function update_environment
def test_update_environment():
    from thonny.globals import get_workbench
    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda var: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:35.769163
# Unit test for function toggle_variable
def test_toggle_variable():
    # test 1
    assert get_workbench().get_option(_OPTION_NAME) == False

    # toggle_variable input
    toggle_variable()

    # test 2
    assert get_workbench().get_option(_OPTION_NAME) == True



# Generated at 2022-06-22 13:03:46.865148
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    os.environ["PGZERO_MODE"] = str(wb.get_option(_OPTION_NAME))
    assert wb.in_simple_mode() is False
    assert os.environ["PGZERO_MODE"] == "False"
    wb.get_command("toggle_pgzero_mode").execute()
    assert wb.in_simple_mode() is True

# Generated at 2022-06-22 13:03:53.573828
# Unit test for function update_environment
def test_update_environment():
    """Test that environment variable is set correctly"""
    if get_workbench().in_simple_mode():
        assert os.environ["PGZERO_MODE"] == "auto"
    else:
        assert os.environ["PGZERO_MODE"] == "False"
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:57.396471
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.globals import get_runner
    import thonny.plugins.bgd_programming_mode

    thonny.plugins.bgd_programming_mode.load_plugin()
    toggle_variable()
    assert get_workbench().get_option("run.pgzero_mode") == True

    # Test that if in simple mode, it toggles it back to false
    get_workbench().set_simple_mode(True)
    toggle_variable()
    assert get_workbench().get_option("run.pgzero_mode") == False

# Generated at 2022-06-22 13:04:07.796923
# Unit test for function update_environment
def test_update_environment():
    test_case = unittest.TestCase()

    orig_simple_mode = get_workbench().in_simple_mode

    def set_simple_mode(val):
        setattr(get_workbench(), "_simple_mode", val)

    def restore_simple_mode():
        set_simple_mode(orig_simple_mode)

    set_simple_mode(True)
    update_environment()
    test_case.assertEqual(os.environ["PGZERO_MODE"], "auto")
    set_simple_mode(False)

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    test_case.assertEqual(os.environ["PGZERO_MODE"], "1")

    get_workbench().set_option(_OPTION_NAME, False)
   

# Generated at 2022-06-22 13:04:12.936362
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    from thonny.common import get_runner
    from importlib import reload

    reload(get_runner)
    get_runner.get_runner()
    b = get_workbench()
    # check button
    b.add_command("toggle_pgzero_mode", "run", tr("Pygame Zero mode"), toggle_variable, _OPTION_NAME)
    # check environment variable
    update_environment()

# Generated at 2022-06-22 13:04:17.267237
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().in_simple_mode() == get_workbench().get_option(_OPTION_NAME)
    assert get_workbench().get_variable(_OPTION_NAME).get() == get_workbench().get_option(
        _OPTION_NAME
    )

# Generated at 2022-06-22 13:04:21.101372
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:24.650323
# Unit test for function update_environment
def test_update_environment():
    from thonny.plugins.run.backend import run_script
    

# Generated at 2022-06-22 13:04:32.728999
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, True)
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:04:45.057385
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import running_on_mac_os, running_on_windows
    from thonny.workbench import Workbench

    if running_on_windows():
        import winreg

        reg_value = winreg.QueryValue(winreg.HKEY_CURRENT_USER, r"Environment\PGZERO_MODE")
        assert reg_value is None

    old_environ = os.environ.copy()

    wb = Workbench()
    wb.set_option(_OPTION_NAME, False)
    wb.set_option("view.simple_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    os.environ.clear()
    os.environ.update(old_environ)

    wb.set_

# Generated at 2022-06-22 13:04:56.223492
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock
    from thonny.testing import get_runner
    runner = get_runner()
    runner.disable_gui()
    get_workbench().set_option(_OPTION_NAME, False)

    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().in_simple_mode = MagicMock(return_value=True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().in_simple_mode = MagicMock(return_value=False)
    get_work

# Generated at 2022-06-22 13:05:04.672488
# Unit test for function toggle_variable
def test_toggle_variable():
    # Clearing the workbench of any default setup
    get_workbench().clear_variable_cache()

    # Testing whether the function toggles the variable when we press the button
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False

    # Setting the workbench back to default setup
    get_workbench().clear_variable_cache()


# Generated at 2022-06-22 13:05:13.935491
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda x: False
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "False"

    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "auto"

    del os.environ["PGZERO_MODE"]
    update_environment()
    assert "PGZERO_MODE" not in os.environ

# Generated at 2022-06-22 13:05:18.641218
# Unit test for function toggle_variable
def test_toggle_variable():
    # populate test environment
    os.environ["PGZERO_MODE"] = "1"
    get_workbench().set_default(_OPTION_NAME, False)
    # test
    toggle_variable()
    assert(os.environ["PGZERO_MODE"] == "0")
    toggle_variable()
    assert(os.environ["PGZERO_MODE"] == "1")

# Generated at 2022-06-22 13:05:29.871776
# Unit test for function load_plugin
def test_load_plugin():
    # In this unittest, the load_plugin() function is called and the mainloop() function
    # is called. The reason is that the toggle_variable() function which calls the
    # update_environment() function is only called from the mainloop() function.

    # Clear all variables
    import os

    if "PGZERO_MODE" in os.environ:
        del os.environ["PGZERO_MODE"]

    global _OPTION_NAME
    _OPTION_NAME = "testing.pgzero_mode"

    # In this test the "run.pgzero_mode" variable is tested by the testing.pgzero_mode variable.
    # This is done so that the test can be run multiple times and each time the test has
    # an influence on the "run.pgzero_mode" variable.
    from thonny import get_work

# Generated at 2022-06-22 13:05:30.806510
# Unit test for function toggle_variable
def test_toggle_variable():
    # The function is tested in thonny/test/test_python_shell.py
    assert True

# Generated at 2022-06-22 13:05:40.586440
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.misc_utils import running_on_mac_os

    old_env = dict(os.environ)

# Generated at 2022-06-22 13:05:44.029669
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"


if __name__ == "__main__":
    load_plugin()

# Generated at 2022-06-22 13:05:49.380224
# Unit test for function load_plugin
def test_load_plugin():
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ.get("PGZERO_MODE") != "True"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ.get("PGZERO_MODE") == "True"

# Generated at 2022-06-22 13:05:58.941615
# Unit test for function toggle_variable
def test_toggle_variable():
    if not os.environ["PGZERO_MODE"] == "auto":
        toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:06:09.432362
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_option(_OPTION_NAME, False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    # Switch to simple mode
    get_workbench().set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"

    # Switch back
    get_workbench().set_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "False"

    # Toggle twice
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:06:19.595314
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_simple_mode(False)
    
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench().set_simple_mode(True)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "auto"
    
    get_workbench().set_simple_mode(False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    
    get_workbench().set_simple_mode(True)
    toggle

# Generated at 2022-06-22 13:06:27.254175
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_in_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_in_simple_mode(False)
    wb.set_default(_OPTION_NAME, True)
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_default(_OPTION_NAME, False)
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:06:33.200022
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.memory import set_workbench
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.set_default = Mock()
    workbench.add_command = Mock()
    set_workbench(workbench)
    load_plugin()

    workbench.set_default.assert_called_once_with(_OPTION_NAME, False)
    workbench.add_command.assert_called_once_with(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )

# Generated at 2022-06-22 13:06:40.041792
# Unit test for function load_plugin
def test_load_plugin():
    import unittest.mock
    from thonny.workbench import Workbench
    from thonny.globals import get_workbench

    with unittest.mock.patch.object(Workbench.instance, "set_default") as set_default, unittest.mock.patch.object(
        Workbench.instance, "add_command"
    ) as add_command:
        load_plugin()
    set_default.assert_called_once_with(_OPTION_NAME, False)
    assert add_command.call_count == 1

# Generated at 2022-06-22 13:06:44.508523
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_option(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True


# Generated at 2022-06-22 13:06:45.622863
# Unit test for function update_environment
def test_update_environment():
    print(os.environ["PGZERO_MODE"])

# Generated at 2022-06-22 13:06:50.823272
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.config import Configuration
    wb = Mock()
    wb.get_option = Configuration.get_workbench_option
    wb.get_variable = Configuration.get_workbench_variable

    wb.in_simple_mode = Mock(return_value=False)
    wb.get_option.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.in_simple_mode.return_value=True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:01.795175
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    assert os.environ["PGZERO_MODE"] == "auto"

    assert get_workbench().in_simple_mode() == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option("view.simple_mode", False)
    assert get_workbench().in_simple_mode() == False
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()

# Generated at 2022-06-22 13:07:24.243857
# Unit test for function update_environment
def test_update_environment():
    class FakeWorkbench:
        def __init__(self, mode):
            self._mode = mode

        def in_simple_mode(self):
            return self._mode
        
        def get_option(self, _):
            # Callers of this function are interested only in mode
            return self._mode

    workbench = FakeWorkbench(True)
    workbench.in_simple_mode = workbench.in_simple_mode.__get__(workbench,FakeWorkbench)
    workbench.get_option = workbench.get_option.__get__(workbench,FakeWorkbench)
    old_env = os.environ.copy()
    del os.environ["PGZERO_MODE"]

    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    workbench._mode

# Generated at 2022-06-22 13:07:34.381098
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_simple_mode(True)
    load_plugin()
    assert not wb.get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    load_plugin()
    assert not wb.get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"
    assert wb._get_variable(_OPTION_NAME) is not None
    assert wb.get_commands()["toggle_pgzero_mode"].flag_name == _OPTION_NAME
    assert "toggle_pgzero_mode" in [key for key in wb.get_command_names("run")]
    wb.set_simple

# Generated at 2022-06-22 13:07:46.131766
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock

    get_workbench = Mock()
    get_workbench.return_value.in_simple_mode.return_value = False
    get_workbench.return_value.get_option.return_value = False
    get_workbench.return_value.add_command.return_value = False
    get_workbench.return_value.set_default.return_value = False

    mock_workbench = Mock()
    mock_workbench.get_variable.return_value.get.return_value = False

    get_workbench.return_value.get_variable.return_value = mock_workbench.get_variable()

    load_plugin()
    assert get_workbench.return_value.set_default == False

# Generated at 2022-06-22 13:07:54.148549
# Unit test for function update_environment
def test_update_environment():
    # In order to test the function update_environment, we need to make sure that
    # the variable is not already set.
    try:
        os.environ.pop("PGZERO_MODE")
    except KeyError:
        pass
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().enter_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:02.701088
# Unit test for function load_plugin
def test_load_plugin():
    # TODO: create a new test editor
    # maybe later add a testing menu to thonny and use that

    # initial values
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os.environ.get("PGZERO_MODE") == "False"
    assert get_workbench().in_simple_mode() is False

    # toggle
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True
    assert os.environ.get("PGZERO_MODE") == "True"
    assert get_workbench().in_simple_mode() is False

    # set workbench to simple mode
    get_workbench().set_simple_mode()
    update_environment()
    assert get_workbench().get_option(_OPTION_NAME) is True


# Generated at 2022-06-22 13:08:11.181364
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_option("run.pgzero_mode", True)
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_option("run.pgzero_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:08:19.243462
# Unit test for function toggle_variable
def test_toggle_variable():
    tb = get_workbench()
    # check if the variable exists
    var = tb.get_variable(_OPTION_NAME)
    assert var.get() == False

    # check if the flag exists
    flag = tb.get_flag(_OPTION_NAME)
    assert flag.get() == False

    # function toggle_variable
    toggle_variable()

    # check if the flag exists
    flag = tb.get_flag(_OPTION_NAME)
    assert flag.get() == True

# Generated at 2022-06-22 13:08:27.671497
# Unit test for function update_environment
def test_update_environment():
    w = get_workbench()
    w.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    w.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    w._simple_mode_manager.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    w._simple_mode_manager.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:31.929970
# Unit test for function update_environment
def test_update_environment():
    # Assuming environment variable is set to 'auto' initially
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:41.802951
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.workbench import Workbench
    get_workbench = Mock(return_value=Workbench(None))
    from thonny.languages import English
    from thonny.plugins.run import init_pgzero_mode
    from thonny.ui_utils import CommonMenu
    get_workbench().set_default = Mock()
    get_workbench().add_command = Mock()
    get_workbench().get_variable = Mock(return_value=Mock(get=Mock(return_value=True), set=Mock()))
    get_workbench().in_simple_mode = Mock(return_value=False)
    os.environ["PGZERO_MODE"] = ""
    load_plugin()



# Generated at 2022-06-22 13:09:13.267116
# Unit test for function update_environment
def test_update_environment():
    try:
        del os.environ["PGZERO_MODE"]
    except KeyError:
        pass

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:09:14.425592
# Unit test for function load_plugin
def test_load_plugin():
    # TODO: use a test backend
    # TODO: create a unit test for this function
    assert False

# Generated at 2022-06-22 13:09:24.852052
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import patch
    from thonny import get_workbench
    from thonny.plugins.pgz_mode.pgz_mode import _OPTION_NAME, update_environment
    get_workbench().set_default(_OPTION_NAME, False)
    with patch.dict(os.environ, {"PGZERO_MODE": "auto"}):
        update_environment()
    assert os.environ["PGZERO_MODE"] == "0"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_option("ui.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:09:29.831919
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.plugins.run import toggle_variable
    toggle_variable()
    assert os.environ['PGZERO_MODE'] == 'True'
    toggle_variable()
    assert os.environ['PGZERO_MODE'] == 'False'
    toggle_variable()
    assert os.environ['PGZERO_MODE'] == 'True'

# Generated at 2022-06-22 13:09:31.149613
# Unit test for function update_environment
def test_update_environment():
    assert False, "Test not implemented" # TODO: implement your test here


# Generated at 2022-06-22 13:09:38.528940
# Unit test for function load_plugin
def test_load_plugin():
    # Load module
    get_workbench().delete_command("toggle_pgzero_mode")
    update_environment()

    # Function calling
    load_plugin()

    # Check
    assert "PGZERO_MODE" in os.environ
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert get_workbench().in_simple_mode() == False


if __name__ == "__main__":
    test_load_plugin()
    print("Everything passed")

# Generated at 2022-06-22 13:09:48.748037
# Unit test for function update_environment
def test_update_environment():
    from test.test_utils import get_workbench_without_config
    wb = get_workbench_without_config()
    wb.set_option(_OPTION_NAME, False)
    wb.in_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    wb.in_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    wb.in_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:09:52.317028
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:09:58.292101
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    get_workbench = Workbench.create_instance()
    get_workbench.set_default(_OPTION_NAME, False)
    get_workbench.add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )



# Generated at 2022-06-22 13:10:06.578789
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().destroy_instance()
    get_workbench().install_plugin(sys.modules[__name__])
    assert get_workbench().get_variable(_OPTION_NAME).get() is False
    
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() is True
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench().in_simple_mode = lambda : True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:11:17.207487
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:11:24.508584
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
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:11:31.882657
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import running_on_mac_os
    workbench = get_workbench()
    workbench.set_simple_mode(False)
    workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    workbench.set_simple_mode(False)
    workbench.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    workbench.set_simple_mode(True)
    workbench.set_option(_OPTION_NAME, True)
    update_environment()
    if running_on_mac_os():
        assert os.environ["PGZERO_MODE"] == "auto"
   

# Generated at 2022-06-22 13:11:42.306865
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench

    # check that the pgzero_mode is set to 0/False
    assert get_workbench().get_option(_OPTION_NAME) == False

    # toggle the pgzero_mode
    toggle_variable()

    # check that the pgzero_mode is now set to 1/True
    assert get_workbench().get_option(_OPTION_NAME) == True

    # check that the environment variable is now set to 1/True
    assert os.environ["PGZERO_MODE"] == str(get_workbench().get_option(_OPTION_NAME))

    # finally, toggle the pgzero_mode back to 0/False
    toggle_variable()

    # check that the pgzero_mode is now set to 0/False again
    assert get_workbench().get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:11:49.229156
# Unit test for function toggle_variable
def test_toggle_variable():
    class MockToggle:
        x = None
        def set(self, x):
            self.x = x

    get_workbench().add_variable(_OPTION_NAME, MockToggle())
    
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).x == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).x == False
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).x == True


# Generated at 2022-06-22 13:11:55.243421
# Unit test for function toggle_variable
def test_toggle_variable():
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False


if __name__ == "__main__":
    toggle_variable()

# Generated at 2022-06-22 13:12:01.277002
# Unit test for function update_environment
def test_update_environment():
    from thonny.shell import ShellView

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:12:04.723045
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_option("run.pgzero_mode", False)
    wb.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:12:15.819206
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock

    wb = mock.MagicMock()
    with mock.patch("thonny.plugins.thonny_pgzero.get_workbench", return_value=wb):
        load_plugin()

    wb.set_default.assert_called_once_with(_OPTION_NAME, False)
    assert wb.add_command.call_count == 1
    call_args = wb.add_command.call_args[1]
    assert call_args["command_id"] == "toggle_pgzero_mode"
    assert call_args["command_label"] == "Pygame Zero mode"
    assert call_args["flag_name"] == _OPTION_NAME
    assert call_args["group"] == 40

# Generated at 2022-06-22 13:12:26.727007
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert "PGZERO_MODE=False" == os.environ["PGZERO_MODE"]
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE=True" == os.environ["PGZERO_MODE"]

    wb.set_default(_OPTION_NAME, False)
    wb.in_simple_mode = lambda: True
    update_environment()
    assert "PGZERO_MODE=auto" == os.environ["PGZERO_MODE"]

