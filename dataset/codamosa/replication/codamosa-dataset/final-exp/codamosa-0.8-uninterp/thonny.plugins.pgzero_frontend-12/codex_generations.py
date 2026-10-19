

# Generated at 2022-06-22 13:02:41.819660
# Unit test for function load_plugin
def test_load_plugin():
    assert get_workbench().set_default(_OPTION_NAME, None) is None
    assert get_workbench().in_simple_mode() is True
    assert get_workbench().set_default(_OPTION_NAME, True) is None
    assert get_workbench().get_option(_OPTION_NAME) is True
    assert get_workbench().get_option(_OPTION_NAME, False) is True
    assert get_workbench().add_command("toggle_pgzero_mode", "run", "", None, None) is None
    assert os.environ.get("PGZERO_MODE") is None
    assert get_workbench().set_default(_OPTION_NAME, False) is None
    assert get_workbench().in_simple_mode() is False

# Generated at 2022-06-22 13:02:48.989791
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop("PGZERO_MODE", None)
    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda x: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    os.environ.pop("PGZERO_MODE", None)
    get_workbench().in_simple_mode = lambda: True
    get_workbench().get_option = lambda x: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:02:54.429160
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:02:57.077066
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    load_plugin()
    assert wb.in_simple_mode() == wb.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:03:06.394589
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_command("toggle_pgzero_mode")
    variable = get_workbench().get_variable(_OPTION_NAME)
    variable.set(True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "True"
    variable.set(False)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "False"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "auto"

# Generated at 2022-06-22 13:03:13.165457
# Unit test for function update_environment
def test_update_environment():
    from thonny.plugins.backend_options.option_manager import OptionManager
    from unittest import mock

    with mock.patch("os.environ", {}), mock.patch("thonny.plugins.backend_options.run.get_workbench", lambda: OptionManager):        
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"
    with mock.patch("os.environ", {}), mock.patch("thonny.plugins.backend_options.run.get_workbench", lambda: OptionManager):
        OptionManager.set_option(_OPTION_NAME, False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:24.069575
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    import thonny
    from thonny.globals import get_workbench
    from thonny.languages import RUS, ENG
    workbench = Mock(spec=thonny.workbench.Workbench)
    workbench.in_simple_mode.return_value = False
    workbench.get_option.return_value = False
    thonny.workbench = workbench
    thonny.globals.get_workbench = Mock(return_value=workbench)

    update_environment()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "0"

    workbench.get_option.return_value = True
    update_environment()

# Generated at 2022-06-22 13:03:29.089854
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    command = get_workbench().find_command("toggle_pgzero_mode")
    assert command is not None
    assert isinstance(command, tk.Checkbutton)
    assert command["label"] == tr("Pygame Zero mode")
    # command.invoke()

# Generated at 2022-06-22 13:03:35.052703
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:46.569393
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench, get_shell
    from thonny.backend import BackendProxy
    from unittest.mock import MagicMock

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command = MagicMock()
    load_plugin()
    backend = BackendProxy.get_proxy()
    backend._send_command = MagicMock()
    mock_get_shell = MagicMock()
    mock_get_shell.in_simple_mode = MagicMock(return_value=True)
    get_workbench().get_shell = mock_get_shell
    update_environment()
    assert get_workbench().get_command("toggle_pgzero_mode") is not None

# Generated at 2022-06-22 13:04:04.535963
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.tktextext import TkTextPlus
    from tkinter import Tk
    from thonny import get_shell
    from unittest import mock
    from io import StringIO
    import sys

    get_workbench().set_default("has_builtins", True)

    root = Tk()
    text = TkTextPlus(root)
    text.pack()
    shell = get_shell()
    shell.set_editor(text)

    text.insert("1.0", "import pgzrun\npgzrun.go()")
    get_workbench().invoke("run-current-script")

    error_stream = StringIO()
    with mock.patch("sys.stderr", error_stream), mock.patch("tkinter.messagebox", return_value="ok"):
        load_plugin

# Generated at 2022-06-22 13:04:14.796097
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    
    get_workbench = Mock()
    get_workbench.in_simple_mode = Mock(return_value=True)
    get_workbench.get_default = Mock(return_value=True)
    get_workbench.get_option = Mock(return_value=True)

    update_environment()
    assert get_workbench.get_option.called
    assert not get_workbench.get_default.called
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench.in_simple_mode.return_value = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench.reset_mock()

# Generated at 2022-06-22 13:04:16.856704
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)

load_plugin()

# Generated at 2022-06-22 13:04:23.512370
# Unit test for function update_environment
def test_update_environment():
    assert "PGZERO_MODE" not in os.environ
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:04:30.687180
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    assert os.environ["PGZERO_MODE"] == "False"

    load_plugin()
    os.environ["PGZERO_MODE"] = "True"
    assert os.environ["PGZERO_MODE"] == "True"


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:04:40.851009
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    load_plugin()
    cmd = wb.get_command("toggle_pgzero_mode")
    assert cmd.label == tr("Pygame Zero mode")
    assert cmd.flag_name == _OPTION_NAME
    # test that command is always enabled
    assert cmd.enabled_in_simple_mode
    assert cmd.enabled_in_stopped_mode
    assert cmd.enabled_in_running_mode(None)
    assert cmd.enabled_in_debugging_mode(None)
    assert cmd.enabled_in_project_mode
    # test that toggle works
    cmd.execute()
    assert not wb.get_variable(_OPTION_NAME).get()
    cmd.execute()
    assert wb.get_

# Generated at 2022-06-22 13:04:46.721697
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:57.898261
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    # toggle_variable()
    workbench.set_variable(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    # toggle_variable()
    workbench.set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    # toggle_variable()
    workbench.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:05:07.830220
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert get_workbench().get_variable(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert get_workbench().get_variable(_OPTION_NAME) == True
    assert get_workbench().in_simple_mode() == False
    get_workbench().start_simple_mode()
    assert get_workbench().in_simple_mode() == True
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().stop_simple_mode()
    assert get_workbench().in_simple_mode() == False
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:05:14.252547
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, "False")
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:05:35.551447
# Unit test for function load_plugin
def test_load_plugin():
    # need to be implemented
    """
    import unittest
    import unittest.mock
    from thonny.plugins.python_turtle import main
    
    class Test_load_plugin(unittest.TestCase):
        def test_load_plugin(self):
            from thonny import get_workbench

            main.load_plugin()
            self.assertIsNotNone(get_workbench().get_variable("python_turtle"))
            self.assertTrue(get_workbench().get_option("python_turtle"))

    if __name__ == '__main__':
        unittest.main()
    """

# Generated at 2022-06-22 13:05:46.173195
# Unit test for function update_environment
def test_update_environment():
    # - in simple mode, no options -> auto
    # - in simple mode, true -> true
    # - in simple mode, false -> false
    #
    # - not in simple mode, no option -> false
    # - not in simple mode, true -> true
    # - not in simple mode, false -> false


    # set up
    from pgzero import config
    import os

    orig_simple_mode = get_workbench().in_simple_mode
    orig_option = get_workbench().get_option
    orig_environ = os.environ.get("PGZERO_MODE")

    def mock_simple_mode():
        return True

    def mock_option(name):
        if name == _OPTION_NAME:
            return True
        else:
            raise AssertionError()


# Generated at 2022-06-22 13:05:49.742236
# Unit test for function update_environment
def test_update_environment():
    try:
        del os.environ["PGZERO_MODE"]
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"
    finally:
        del os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:05:56.559029
# Unit test for function toggle_variable
def test_toggle_variable():
    import unittest.mock
    
    get_workbench = unittest.mock.MagicMock()
    get_workbench.get_variable = unittest.mock.MagicMock()
    get_var = get_workbench.get_variable.return_value
    get_var.get = unittest.mock.MagicMock()
    toggle_variable()
    
    get_workbench.get_variable.assert_called_once_with(_OPTION_NAME)
    get_var.set.assert_called_once_with(not get_var.get.return_value)
    assert get_var.get.call_count == 1
    


# Generated at 2022-06-22 13:06:05.692769
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.config import OptionsManager
    
    wb = Mock()
    wb.get_option = OptionsManager.get
    wb.in_simple_mode = Mock(return_value=False)
    
    get_workbench().in_simple_mode = Mock(return_value=False)
    get_workbench().get_option = OptionsManager.get
    
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    wb.in_simple_mode = Mock(return_value=True)
    get_workbench().in_simple_mode = Mock(return_value=True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:11.036148
# Unit test for function toggle_variable
def test_toggle_variable():
    os.environ["PGZERO_MODE"] = "0"
    
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "1"
    
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:06:12.952863
# Unit test for function update_environment
def test_update_environment():
    # clean up
    del os.environ["PGZERO_MODE"]
    # test
    update_environment()
    # check
    assert os.environ["PGZERO_MODE"] == "auto"
    # clean up
    del os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:06:14.287560
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:06:18.367164
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:23.873672
# Unit test for function load_plugin
def test_load_plugin():
    original_wb = get_workbench()
    get_workbench = MagicMock(return_value=original_wb)
    original_tr = tr
    tr = MagicMock(return_value="TranslatedText")
    original_update_environment = update_environment
    update_environment = MagicMock()
    original_toggle_variable = toggle_variable
    toggle_variable = MagicMock()
    import sys
    from unittest.mock import patch

    with patch.dict("sys.modules", get_workbench=get_workbench, tr=tr):
        import thonnycontrib.pgzero_mode

        new_wb = get_workbench()
        new_wb.add_command = MagicMock()
        thonnycontrib.pgzero_mode.load_plugin()

# Generated at 2022-06-22 13:06:46.211731
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import patch, MagicMock
    from thonny.misc_utils import running_on_mac_os

    workbench = get_workbench()
    workbench.set_option(_OPTION_NAME, False)
    workbench.set_simple_mode(False)
    with patch.dict(os.environ, {"PGZERO_MODE": "other_value"}):
        update_environment()
        if running_on_mac_os():
            assert os.environ["PGZERO_MODE"] == "auto"
        else:
            assert os.environ["PGZERO_MODE"] == "0"

    workbench.set_option(_OPTION_NAME, True)
    workbench.set_simple_mode(False)

# Generated at 2022-06-22 13:06:52.028127
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import patch
    from thonny import get_workbench

    get_workbench().in_simple_mode = lambda: False
    get_workbench().set_default(_OPTION_NAME, True)
    
    with patch.dict('os.environ', {'PGZERO_MODE': ''}):
        update_environment()
        assert os.environ['PGZERO_MODE'] == 'True'

    with patch.dict('os.environ', {'PGZERO_MODE': ''}):
        get_workbench().set_option(_OPTION_NAME, False)
        update_environment()
        assert os.environ['PGZERO_MODE'] == 'False'

    get_workbench().in_simple_mode = lambda: True

# Generated at 2022-06-22 13:07:02.152385
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_simple_mode()
    get_workbench().set_default(_OPTION_NAME, False)
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == str(
        get_workbench().get_option(_OPTION_NAME) # pylint: disable=line-too-long
    )
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:07.164400
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"



# Generated at 2022-06-22 13:07:18.977941
# Unit test for function load_plugin
def test_load_plugin():
    # Check with Debugger
    from thonny.globals import get_workbench
    from thonny.plugins.run.command import toggle_variable
    from thonny.plugins.run.run import update_environment
    import os

    assert get_workbench().get_variable("run.pgzero_mode") == False
    assert get_workbench().get_option("run.pgzero_mode") == False

    toggle_variable()
    assert get_workbench().get_variable("run.pgzero_mode") == True
    assert get_workbench().get_option("run.pgzero_mode") == True

    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(True)
    update_environment()

# Generated at 2022-06-22 13:07:29.776569
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import captured_stderr, captured_stdout, run_isolated
    from thonny.workbench import Workbench
    import sys
    import os

    saved_args = sys.argv
    try:
        get_workbench().set_default(_OPTION_NAME, False)
        sys.argv = ["thonny.exe", "--simple-mode"]
        wb = Workbench()
        assert os.environ["PGZERO_MODE"] == "auto"
        wb.destroy()
        sys.argv = saved_args
        wb = Workbench()
        assert os.environ["PGZERO_MODE"] == "False"
        wb.destroy()
    finally:
        sys.argv = saved_args

# Generated at 2022-06-22 13:07:39.953485
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench

    workbench.unload_plugin_by_name("pgzero_mode")

# Generated at 2022-06-22 13:07:48.052401
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from thonny import get_workbench
    from thonny.globals import get_runner
    from unittest.mock import Mock
    wb = Workbench()
    wb.set_variable(_OPTION_NAME, False)
    runner = Mock()
    get_runner.return_value = runner
    get_workbench.return_value = wb
    update_environment()
    get_runner().update_environment.assert_called_once_with(
        {"PGZERO_MODE": "False"}
    )

# Generated at 2022-06-22 13:07:58.194769
# Unit test for function toggle_variable

# Generated at 2022-06-22 13:08:06.338021
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench

    # Initial value of variable should be false
    var = get_workbench().get_variable(_OPTION_NAME)
    get_workbench().set_default(_OPTION_NAME, False)
    assert var.get() == False

    # Changing state of variable with toggle_variable should change it to true
    toggle_variable()
    assert var.get() == True

    # Changing state of variable with toggle_variable should change it back to false
    toggle_variable()
    assert var.get() == False

# Generated at 2022-06-22 13:08:27.671347
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench, register_plugin
    from unittest.mock import MagicMock, patch
    from test.test_runner import TkInterMock

    register_plugin(env_plugin)
    get_workbench().disable_simple_mode()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert "PGZERO_MODE" not in os.environ

    get_workbench().enable_simple_mode()
    get_workbench().add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os

# Generated at 2022-06-22 13:08:37.488749
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench

    get_workbench().set_simple_mode()
    assert os.environ["PGZERO_MODE"] == "auto"

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_advanced_mode()
    assert os.environ["PGZERO_MODE"] == "auto"

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"



# Generated at 2022-06-22 13:08:40.310005
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.create(None)
    load_plugin()


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:08:44.693224
# Unit test for function toggle_variable

# Generated at 2022-06-22 13:08:54.898039
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock

    get_workbench().get_option = MagicMock(return_value=True)
    get_workbench().in_simple_mode = MagicMock(return_value=False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().get_option = MagicMock(return_value=False)
    get_workbench().in_simple_mode = MagicMock(return_value=False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().get_option = MagicMock(return_value=False)
    get_workbench().in_simple_mode = MagicMock(return_value=True)
    update_environment()


# Generated at 2022-06-22 13:09:06.031165
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    # test case -1: simple mode
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ.get("PGZERO_MODE", "") == "auto"
    # test case 0: PGZERO_MODE==False (i.e. False is a string, not a bool)
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, "False")
    update_environment()
    assert os.environ.get("PGZERO_MODE", "") == "False"
    # test case 1: PGZERO_MODE==True (i.e. True is a string, not a bool)
    wb.set_simple_mode(False)

# Generated at 2022-06-22 13:09:12.522909
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    import os

    get_workbench().set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option("run.pgzero_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:09:18.266928
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    w = Workbench()
    load_plugin()
    assert w.get_option(_OPTION_NAME) == False

    # Check if set to true
    w.set_option(_OPTION_NAME, True)
    assert w.get_option(_OPTION_NAME) == True

    # Check if set to false
    w.set_option(_OPTION_NAME, False)
    assert w.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:09:25.844177
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.set_default = Mock()
    wb.add_command = Mock()
    load_plugin()
    wb.set_default.assert_any_call(_OPTION_NAME, False)
    wb.add_command.assert_called_once_with(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )

# Generated at 2022-06-22 13:09:34.413652
# Unit test for function load_plugin
def test_load_plugin():
    main_window = get_workbench()
    main_window.set_default(_OPTION_NAME, False)
    main_window.add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    update_environment()
    assert main_window.get_variable(_OPTION_NAME) == False
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:10:07.433371
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_variable(_OPTION_NAME, True)
    assert (get_workbench().get_variable(_OPTION_NAME) == True)
    get_workbench().set_variable(_OPTION_NAME, False)
    toggle_variable()
    assert (get_workbench().get_variable(_OPTION_NAME) == True)
    toggle_variable()
    assert (get_workbench().get_variable(_OPTION_NAME) == False)

# Generated at 2022-06-22 13:10:16.089165
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_simple_mode(False)
    load_plugin()
    assert wb.get_variable(_OPTION_NAME).get() is False
    assert os.environ["PGZERO_MODE"] == "False"
    assert len(wb.get_menus().get_menu("run").get_children()) == 8

    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() is True
    assert os.environ["PGZERO_MODE"] == "True"
    assert len(wb.get_menus().get_menu("run").get_children()) == 8

    wb.set_simple_mode(True)
    assert wb.get_variable(_OPTION_NAME).get() is True

# Generated at 2022-06-22 13:10:24.382384
# Unit test for function update_environment
def test_update_environment():
    b = get_workbench()
    b.set_simple_mode(True)
    b.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    b.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    b.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:26.893600
# Unit test for function update_environment
def test_update_environment():
    # I don't know how to do an assertion on a global variable, so let's
    # just check that it doesn't crash
    load_plugin()
    update_environment()

# Generated at 2022-06-22 13:10:38.677506
# Unit test for function update_environment
def test_update_environment():
    import os

    # This unit test can only be run if the program does not have access
    # to the environment variable PGZERO_MODE.
    # If the environment variable is present, then the unit test will
    # raise an exception stating that the environment variable is present.
    #
    # This is a test to see if the program will overwrite an existing
    # environment variable.
    #
    # This test should pass.
    try:
        os.environ["PGZERO_MODE"]
    except KeyError:
        wb = get_workbench()
        wb.set_default(_OPTION_NAME, False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
    else:
        raise Exception("environment variable PGZERO_MODE is present")

    # This unit test can only be

# Generated at 2022-06-22 13:10:42.243947
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().in_simple_mode = lambda: False
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:10:48.995143
# Unit test for function update_environment
def test_update_environment():
    assert "PGZERO_MODE" not in os.environ
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2022-06-22 13:10:55.862933
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ.get("PGZERO_MODE") == "False"
    
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ.get("PGZERO_MODE") == "True"
    
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ.get("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:11:04.154756
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.plugins.run.run_commands import get_run_commands
    from thonny.workbench import Workbench

    from thonny.misc_utils import running_on_mac_os

    wb = Workbench()
    wb.load_plugin(__name__)

    assert _OPTION_NAME in wb.get_option_names()

    # Test that the value of PGZERO_MODE is automatically set to an
    # expected value when the VARIANT is changed
    if running_on_mac_os():
        os.environ["VARIANT"] = "simple"
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
        # Assume that the process is restarted with different virtual env
        os

# Generated at 2022-06-22 13:11:11.794733
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import Mock
    from thonny.workbench import Workbench
    from thonny.common import get_runner
    import thonny.plugins.backend_options as backend_options
    import thonny.plugins.run as run
    import thonny.plugins.pgzero_mode as pgzero_mode

    mw = Mock()
    mw.get_variable = run.get_variable = pgzero_mode.get_variable = Mock()
    mw.get_variable.side_effect = ['first call', 'second call']
    mw.set_variable = Mock()
    mw.in_simple_mode = Mock(return_value=True)
    mw.get_option = Mock()
    mw.set_option = Mock()

    workbench = Workbench(mw)


# Generated at 2022-06-22 13:12:14.850476
# Unit test for function toggle_variable
def test_toggle_variable():
    startValue = get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    endValue = get_workbench().get_option(_OPTION_NAME)
    assert startValue != endValue
    assert endValue == True
    toggle_variable()
    endValue = get_workbench().get_option(_OPTION_NAME)
    assert endValue == False


# Generated at 2022-06-22 13:12:25.149412
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import Mock

    mock_get_workbench = Mock()
    mock_get_workbench.get_variable = Mock()
    mock_get_workbench.get_variable.return_value.get = Mock(return_value=False)
    mock_get_workbench.get_variable.return_value.set = Mock()
    mock_get_workbench.in_simple_mode = Mock(return_value=False)
    mock_get_workbench.get_option = Mock(return_value=True)

    toggle_variable()

    mock_get_workbench.get_variable.return_value.set.assert_called_once_with(True)


# Generated at 2022-06-22 13:12:27.723478
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_command("toggle_pgzero_mode")
    assert get_workbench().in_simple_mode() == get_workbench().get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:12:29.821888
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False