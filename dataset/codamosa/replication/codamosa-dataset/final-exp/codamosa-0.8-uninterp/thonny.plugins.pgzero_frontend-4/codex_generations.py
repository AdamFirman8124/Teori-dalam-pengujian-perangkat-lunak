

# Generated at 2022-06-22 13:02:36.328384
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin() # No exception
    wb = get_workbench()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:02:42.038743
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:02:51.539089
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from unittest.mock import Mock
    from thonny.workbench import _add_command

    wb = Workbench()
    command_dict = {}
    wb.get_variable = lambda k: {_OPTION_NAME: False}[k]
    wb.set_default = Mock()
    wb.in_simple_mode = lambda: False

    _add_command = Mock()
    _add_command.side_effect = lambda n, c, l, f, fg, g, **kw: command_dict.__setitem__(
        n, (c, l, f, fg, g)
    )

    load_plugin()

    assert wb.set_default.call_count == 1
    assert wb.set_default.call_args

# Generated at 2022-06-22 13:02:56.223173
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    
    workbench = get_workbench()
    # Check to see if option was created
    assert workbench.get_option(_OPTION_NAME)
    assert workbench.get_option(_OPTION_NAME) == False

    # Check to see if command is available
    command = workbench.get_command("toggle_pgzero_mode")
    assert command
    assert command.handler == toggle_variable
    assert command.flag_name == _OPTION_NAME
    assert command.group == 40


# Generated at 2022-06-22 13:03:07.961806
# Unit test for function update_environment
def test_update_environment():
    # Save old PGZERO_MODE environment variable
    old_pgz = os.environ.get("PGZERO_MODE")

    # Test default value in normal mode
    wb = get_workbench()
    wb.in_simple_mode = lambda: False
    wb.get_option = lambda x: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test in simple mode
    wb.in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test value True
    wb.in_simple_mode = lambda: False
    wb.get_option = lambda x: True
    update_environment()
    assert os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:03:20.675794
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    assert "PGZERO_MODE" not in os.environ
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:03:25.103808
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    if os.name != 'nt':
        assert os.environ["PGZERO_MODE"] == "0"

    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:03:29.086084
# Unit test for function load_plugin
def test_load_plugin():
    import unittest.mock
    from thonny import get_workbench

    with unittest.mock.patch("os.environ") as mock_environ:
        load_plugin()
        mock_environ.__setitem__.assert_called_once_with("PGZERO_MODE", "0")

# Generated at 2022-06-22 13:03:40.911119
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_simple_mode(True)
    wb.get_variable(_OPTION_NAME).set(True)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert get_workbench().get_option

# Generated at 2022-06-22 13:03:52.134863
# Unit test for function update_environment
def test_update_environment():
    mode_var = get_workbench().get_variable(_OPTION_NAME)
    assert not mode_var.get()
    assert os.environ.get("PGZERO_MODE", False) == "False"
    
    # Switch mode on
    get_workbench().get_option(_OPTION_NAME, True)
    assert os.environ.get("PGZERO_MODE", False) == "True"
    
    # Switch mode off
    get_workbench().get_option(_OPTION_NAME, False)
    assert os.environ.get("PGZERO_MODE", True) == "False"
    
    # Set PGZERO_MODE environment variable
    os.environ["PGZERO_MODE"] = "auto"
    assert os.environ.get("PGZERO_MODE", False) == "auto"

# Generated at 2022-06-22 13:04:08.228757
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench

    # Reset environment
    os.environ["PGZERO_MODE"] = ""
    load_plugin()

    # Standalone
    assert os.environ["PGZERO_MODE"] == "False"
    assert get_workbench().get_option(_OPTION_NAME) == False

    # In simple mode
    get_workbench().set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    assert get_workbench().get_option(_OPTION_NAME) == False

    # In simple mode, but normal mode forced
    get_workbench().set_simple_mode(True)
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:14.796085
# Unit test for function update_environment
def test_update_environment():
    get_workbench().in_simple_mode = lambda: False
    os.environ["PGZERO_MODE"] = "1"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"



# Generated at 2022-06-22 13:04:17.324205
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from types import MappingProxyType

    get_workbench().get_variable = Mock(return_value=Mock(get=lambda: False))
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:19.480253
# Unit test for function load_plugin
def test_load_plugin():
    _clear_all_variables()
    load_plugin()
    _check_variable_values()



# Generated at 2022-06-22 13:04:20.062996
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:04:22.418818
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False

# Generated at 2022-06-22 13:04:33.762417
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import Mock
    mock_variable = Mock()
    mock_variable.set = Mock()
    mock_variable.get = Mock()
    mock_variable.get.return_value = True
    mock_wb = Mock()
    mock_wb.in_simple_mode = Mock()
    mock_wb.in_simple_mode.return_value = False
    mock_wb.get_variable = Mock()
    mock_wb.get_variable.return_value = mock_variable
    mock_wb.get_option = Mock()
    mock_wb.get_option.return_value = True
    mock_wb.get_option.return_value = False
    toggle_variable()
    mock_wb.get_variable.assert_called_once_with(_OPTION_NAME)

# Generated at 2022-06-22 13:04:43.225869
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.ui_utils import toggle_checkbox

    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_variable(_OPTION_NAME).get() is False
    assert os.environ.get("PGZERO_MODE") != "True"

    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() is True
    assert os.environ.get("PGZERO_MODE") == "True"

    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() is False
    assert os.environ.get("PGZERO_MODE") == "False"

    get_workbench().set_simple_mode(True)

# Generated at 2022-06-22 13:04:54.280944
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.workbench import Workbench

    w = Workbench()
    w.create_main_window()
    w.add_command("toggle_pgzero_mode", "run", "Pygame Zero mode", toggle_variable)
    # default must be None
    assert w.get_option(_OPTION_NAME) == False
    # default must be None
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert w.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert w.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:05:01.396678
# Unit test for function update_environment
def test_update_environment():
    import os
    from thonny import get_workbench
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

# Generated at 2022-06-22 13:05:16.037648
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_variable("run.pgzero_mode").get() == False

# Generated at 2022-06-22 13:05:20.844122
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    assert wb.get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == False
    toggle_variable()

# Generated at 2022-06-22 13:05:31.775842
# Unit test for function load_plugin
def test_load_plugin():
    @contextlib.contextmanager
    def mock_get_workbench(options, settings=None, in_simple_mode=False):
        class MockWorkbench:
            def __init__(self, options, settings, in_simple_mode):
                self.options = options
                self.settings = settings
                self.in_simple_mode = in_simple_mode
                self.add_backend_created_listener = mock.Mock()
                self.add_command = mock.Mock()
            
            def get_option(self, name):
                return self.options[name]
            
            def set_default(self, name, value):
                self.options[name] = value
            
            def get_variable(self, name):
                return settings[name]
            

# Generated at 2022-06-22 13:05:41.440243
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from thonny import get_workbench
    from unittest.mock import patch, MagicMock

    _ = tr("Pygame Zero mode")
    workbench = Workbench()
    workbench.in_simple_mode = MagicMock(return_value=False)
    get_workbench = MagicMock(return_value=workbench)
    with patch("thonny.plugins.pgzero.update_environment.os", autospec=True) as os_mock:
        from thonny.plugins.pgzero import update_environment

        update_environment()
        assert os_mock.environ["PGZERO_MODE"] == str(get_workbench().get_option(_OPTION_NAME))

        workbench.in_simple_mode.return_value = True
       

# Generated at 2022-06-22 13:05:49.716672
# Unit test for function load_plugin
def test_load_plugin():
    global get_workbench, tr
    
    # Mock functions to test load_plugin()
    get_workbench = lambda: 0
    tr = lambda x: x
    workbench = get_workbench()
    workbench.add_command = []
    workbench.set_default = []
    workbench.get_variable = {}

    # Test function load_plugin()
    load_plugin()
    assert len(workbench.add_command) == 1
    assert len(workbench.set_default) == 1
    assert workbench.get_variable == {'_OPTION_NAME': []}

# Generated at 2022-06-22 13:06:01.106462
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import get_environ_cmd

    if os.name == "nt":
        expected_cmd = '@echo off\nset PGZERO_MODE="False"\n'
    else:
        expected_cmd = '#!/bin/sh\nexport PGZERO_MODE="False"\n'

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert get_environ_cmd().getvalue() == expected_cmd

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    if os.name == "nt":
        expected_cmd = '@echo off\nset PGZERO_MODE="True"\n'

# Generated at 2022-06-22 13:06:06.362183
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False

    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == True

# Generated at 2022-06-22 13:06:14.854417
# Unit test for function load_plugin
def test_load_plugin():
    # Foo is simple mode
    get_workbench().set_simple_mode(True)
    load_plugin()
    assert os.environ.get("PGZERO_MODE") == "auto"
    # Now Foo is not simple mode
    get_workbench().set_simple_mode(False)
    toggle_variable()
    assert os.environ.get("PGZERO_MODE") == "True"
    toggle_variable()
    assert os.environ.get("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:06:22.425508
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.codeview import get_code_view
    from thonny.shell import ShellTextWidget
    from thonny.workbench import Workbench
    from thonny.misc_utils import running_on_mac_os, running_on_windows

    workbench = Workbench()
    workbench.create()

    # this should not fail because of an exception:
    load_plugin()

    # Check operation of the command
    original_value = workbench.get_option(_OPTION_NAME)
    assert not workbench.get_variable(_OPTION_NAME).get()
    workbench.event_generate("<<UpdateEnvironment>>")
    assert os.environ.get("PGZERO_MODE") == "0"

    workbench.invoke_command("toggle_pgzero_mode")
    assert workbench.get_option

# Generated at 2022-06-22 13:06:30.805716
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock

    wb = Mock()
    wb.get_option.return_value = False
    wb.in_simple_mode.return_value = False
    wb.get_variable.return_value = False

    with patch("thonny.plugins.pgzero.get_workbench", return_value=wb):
        update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.get_option.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:50.152078
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench
    from thonny.plugins.pgzero_mode import toggle_variable
    from thonny.languages import tr
    from tkinter import IntVar
    from thonny.common import TkVersion
    from test.test_thonny import running_on_mac_os
    from thonny.ui_utils import CommonDialog
    from thonny.config import get_workbench
    
    toggle_variable()
    if running_on_mac_os():
        print("Skipped test on Mac")
    else:
        assert "PGZERO_MODE" in os.environ
        assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    if running_on_mac_os():
        print("Skipped test on Mac")

# Generated at 2022-06-22 13:06:59.061129
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench

    workbench.get_option = lambda *args, **kw: False
    workbench.set_default = lambda *args, **kw: None
    workbench.add_command = lambda *args, **kw: None
    workbench.in_simple_mode = lambda: False
    workbench.get_variable = lambda *args, **kw: False
    workbench.get_option = lambda *args, **kw: False
    workbench.set_default = lambda *args, **kw: None

    load_plugin()

# Generated at 2022-06-22 13:07:03.261998
# Unit test for function update_environment
def test_update_environment():
    if get_workbench().in_simple_mode():
        assert len(os.environ["PGZERO_MODE"]) > 0
    else:
        assert os.environ["PGZERO_MODE"] == str(get_workbench().get_option(_OPTION_NAME))

# Generated at 2022-06-22 13:07:14.275296
# Unit test for function load_plugin

# Generated at 2022-06-22 13:07:23.948970
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.init(["--simple-mode"])
    assert len(wb.get_commands()) == 4

    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "True"
    assert wb.get_commands()["toggle_pgzero_mode"].flag_name == _OPTION_NAME
    assert wb.get_commands()["toggle_pgzero_mode"].get_label() == tr("Disable Pygame Zero mode")

    toggle_variable()
    assert not wb.get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:07:32.707945
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
    assert os.environ["PGZERO_MODE"] == str(wb.get_option(_OPTION_NAME))
    wb.set_variable(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == str(wb.get_option(_OPTION_NAME))



# Generated at 2022-06-22 13:07:42.853167
# Unit test for function update_environment
def test_update_environment():
    with tempfile.TemporaryDirectory() as thonny_user_dir:
        get_workbench().set_user_directory(thonny_user_dir)
        get_workbench().get_option(_OPTION_NAME).set(True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"
        get_workbench().get_option(_OPTION_NAME).set(False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
        get_workbench().switch_to_simple_mode()
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:44.875390
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, True)
    toggle_variable()
    toggle_variable()

# Generated at 2022-06-22 13:07:56.194638
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    from thonny.config import get_runner

    if "PGZERO_MODE" in os.environ:
        del os.environ["PGZERO_MODE"]
    wb = get_workbench()
    wb._CommunicationThread = lambda *args, **kwargs: None
    wb._EventHandlerThread = lambda *args, **kwargs: None
    # Mock get_runner so it won't try to connect to the shell
    wb.get_runner = lambda: get_class_stub(klass=get_runner())
    wb.in_simple_mode = lambda: False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get

# Generated at 2022-06-22 13:08:03.911692
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.clear_test_mode()
    from thonny.plugins.run import run_file_command
    from thonny.plugins.run import run_module_command
    from thonny.plugins.run import debug_command
    assert not hasattr(wb, "toggle_pgzero_mode")
    assert not hasattr(wb, "fgcolor")
    assert "PGZERO_MODE" not in os.environ

    load_plugin()
    assert hasattr(wb, "toggle_pgzero_mode")
    assert hasattr(wb, "fgcolor")
    assert isinstance(wb.toggle_pgzero_mode, run_file_command.RunFileCommand)
    wb.get_option("run.pgzero_mode")

# Generated at 2022-06-22 13:08:37.619192
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.plugins.purepythontb import PurePythonTBPlugin
    from thonny import get_workbench, ui_utils, workbench
    from thonny.workbench import Action, Variable
    
    # test for variables
    new_get_workbench = workbench.Workbench()
    new_get_workbench.set_default(_OPTION_NAME, False)
    var = new_get_workbench.get_variable(_OPTION_NAME)
    
    assert str(var.get()) == str(False)
    
    # test for command
    new_workbench = workbench.Workbench()
    new_workbench.set_default(_OPTION_NAME, False)
    assert get_workbench().get_command("toggle_pgzero_mode") == None
    
    new_workbench.add

# Generated at 2022-06-22 13:08:48.789082
# Unit test for function load_plugin
def test_load_plugin():
    import unittest.mock
    from thonny import workbench
    from thonny.ui_utils import VariableSpinbox
    import tkinter as tk

    mb_1 = unittest.mock.MagicMock(
        spec=tk.Menubutton, **{"menu": unittest.mock.MagicMock(spec=tk.Menu)}
    )
    mb_2 = unittest.mock.MagicMock(
        spec=tk.Menubutton, **{"menu": unittest.mock.MagicMock(spec=tk.Menu)}
    )
    mb_3 = unittest.mock.MagicMock(
        spec=tk.Menubutton, **{"menu": unittest.mock.MagicMock(spec=tk.Menu)}
    )
   

# Generated at 2022-06-22 13:08:56.068409
# Unit test for function update_environment
def test_update_environment():
    import os
    import unittest
    
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    os_env = os.environ["PGZERO_MODE"]
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    os_env2 = os.environ["PGZERO_MODE"]
    #print(os_env)
    #print(os_env2)
    assert os_env == "False"
    assert os_env2 == "True"


#############################################################################
# Unit tests for function toggle_variable
#############################################################################

# Generated at 2022-06-22 13:09:05.827166
# Unit test for function update_environment
def test_update_environment():
    import os
    from thonny import get_workbench

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_option("run.simple_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_option("run.simple_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_option("run.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:09:11.483174
# Unit test for function load_plugin
def test_load_plugin():
    wb = MockWorkbench()
    load_plugin()
    assert wb.in_simple_mode() == False
    assert wb.get_option(_OPTION_NAME) == False
    
    assert wb.in_simple_mode() == True
    assert wb.get_option(_OPTION_NAME) == True
    

# Generated at 2022-06-22 13:09:15.943159
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    get_workbench().destroy()
    load_plugin()
    assert isinstance(get_workbench(), Workbench)
    assert get_workbench().get_variable(_OPTION_NAME).get() == False


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:09:21.209968
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) == False

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:09:32.436262
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.languages import tr
    from thonny.misc_utils import running_on_mac_os

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
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert get_workbench().get_default("run.play_button_command") == "run_file"
    assert get_workbench().get_default("run.play_button_text") == "Run program"
    assert get

# Generated at 2022-06-22 13:09:42.275965
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock

    wb = Mock()
    wb.in_simple_mode.return_value = False
    wb.get_option.return_value = True

    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()

    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_clear()
    get_workbench.cache_

# Generated at 2022-06-22 13:09:45.413329
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:10:54.283049
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_variable(_OPTION_NAME).get() == False

    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == True

    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == False

# Generated at 2022-06-22 13:11:05.053256
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_default(_OPTION_NAME, True)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().in_simple_mode = True
    update_environment()

# Generated at 2022-06-22 13:11:09.889519
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, True)
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    
    get_workbench().set_option(_OPTION_NAME, False)
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:11:20.429238
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock

    with mock.patch("thonny.workbench.Workbench.set_default"):
        with mock.patch(
            "thonny.workbench.Workbench.add_command",
            return_value="test_return"
        ) as mock_add_command:
            with mock.patch(
                "thonny.workbench.Workbench.get_variable",
                return_value="test_variable"
            ) as mock_get_variable:
                load_plugin()
                assert mock_get_variable.call_count == 1
                assert mock_get_variable.call_args[0] == (_OPTION_NAME,)
                assert mock_add_command.call_count == 1

# Generated at 2022-06-22 13:11:31.794692
# Unit test for function update_environment
def test_update_environment():
    old_env = os.environ.get("PGZERO_MODE")
    wb = get_workbench()

    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "False"

    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "True"

    wb.set_simple_mode(True)
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "auto"

    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, False)
    update_environment()

# Generated at 2022-06-22 13:11:37.383039
# Unit test for function update_environment
def test_update_environment():
    import os
    get_workbench().in_simple_mode = lambda: False
    print(get_workbench().in_simple_mode())
    update_environment()
    print(os.environ["PGZERO_MODE"])
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:11:45.739528
# Unit test for function update_environment
def test_update_environment():
    environ_bak = dict(os.environ)

    from thonny.globals import get_workbench

    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    workbench.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    workbench.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    workbench.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    os.environ

# Generated at 2022-06-22 13:11:51.856309
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True

    # If in simple mode then pgzero_mode is always True
    wb.in_simple_mode = lambda: True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:11:59.099959
# Unit test for function toggle_variable
def test_toggle_variable():
    _OPTION_NAME = "run.pgzero_mode"
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:12:04.991263
# Unit test for function update_environment
def test_update_environment():
    if "PGZERO_MODE" in os.environ:
        del os.environ["PGZERO_MODE"]
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"