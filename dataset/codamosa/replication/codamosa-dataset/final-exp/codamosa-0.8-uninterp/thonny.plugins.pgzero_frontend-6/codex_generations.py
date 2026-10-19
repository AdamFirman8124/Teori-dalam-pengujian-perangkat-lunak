

# Generated at 2022-06-22 13:02:46.814671
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.workbench import Workbench
    from thonny.running import get_subprocess_environment

    workbench = Workbench()
    workbench.set_mode(Workbench.RUN_MODE)
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    proc = Mock()
    # When pgzero is disabled, environment should NOT be modified
    assert get_subprocess_environment(proc) == proc.env
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert get_subprocess_environment(proc) == {**os.environ, **proc.env}

# Generated at 2022-06-22 13:02:50.994221
# Unit test for function update_environment
def test_update_environment():
    get_workbench().unset_option(_OPTION_NAME)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:02:56.865473
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == True

# Generated at 2022-06-22 13:03:08.516477
# Unit test for function update_environment
def test_update_environment():
    import os
    import unittest.mock
    from thonny import get_workbench

    from thonny.testing import TestConfig, TestConfigLoader
    from thonny.globals import get_runner

    # Save the original values.
    original_env = os.environ.copy()
    original_conf = get_workbench().get_option(_OPTION_NAME)

    # Test the set_default function for the option,
    # which should be called every time the plugin is loaded.
    get_workbench().set_default(_OPTION_NAME, False)

    # Mock the environment variable and the get_option function.
    # The plugin is loaded during the start of thonny,
    # so we need to mock the environment variable before loading.
    os.environ = {}

# Generated at 2022-06-22 13:03:13.485077
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:15.617522
# Unit test for function toggle_variable
def test_toggle_variable():
    # Just checks that toggle_variable doesn't throw
    toggle_variable()

# Generated at 2022-06-22 13:03:20.123867
# Unit test for function update_environment
def test_update_environment():
    try:
        del os.environ["PGZERO_MODE"]
    except KeyError:
        pass
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:29.039226
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    assert "PGZERO_MODE" not in os.environ
    load_plugin()
    assert wb.in_simple_mode() == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_simple_mode(True)
    assert wb.in_simple_mode() == True
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    assert wb.in_simple_mode() == False
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:32.870142
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:41.177212
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench
    from thonny.languages import tr
    import pytest

    # add_command
    cmds = get_workbench().get_commands()
    assert "toggle_pgzero_mode" in cmds
    cmd = cmds["toggle_pgzero_mode"]
    assert cmd.label == tr("Pygame Zero mode")
    assert cmd.group == 40
    assert cmd.description == ""
    assert cmd._func == toggle_variable
    assert cmd._var is None

    # Initialize workbench
    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_option(_OPTION_NAME, True)
    # test_pgzero_mode
    test_pgzero_mode = get_workbench().get_variable(_OPTION_NAME).get

# Generated at 2022-06-22 13:03:59.655222
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    from thonny.codeview import CodeViewText

    class P:
        pass

    wb = P()
    wb.in_simple_mode = mock.Mock(return_value=True)
    wb.get_option = mock.Mock(return_value=False)
    get_workbench().in_simple_mode = wb.in_simple_mode
    get_workbench().get_option = wb.get_option
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.in_simple_mode.return_value = False
    wb.get_option.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"


# Generated at 2022-06-22 13:04:11.413570
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "old value"
    wb = get_workbench()
    del os.environ["PGZERO_MODE"]

    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_default(_OPTION_NAME, False)
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    del os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:04:20.401581
# Unit test for function toggle_variable
def test_toggle_variable():
    # Option has initial value False
    wb = get_workbench()
    var = wb.get_variable(_OPTION_NAME)
    assert not var.get()
    assert not wb.in_simple_mode()

    # Check that variable is toggled to True when function is executed
    toggle_variable()
    assert var.get()

    # Check that variable is toggled to False when function is executed again
    toggle_variable()
    assert not var.get()

    # Check that function sets PGZERO_MODE environment variable
    # in the case of complex mode
    toggle_variable()
    assert var.get()
    wb.set_simple_mode(False)
    assert not wb.in_simple_mode()
    update_environment()
    assert "PGZERO_MODE=True" == os.environ

# Generated at 2022-06-22 13:04:25.256703
# Unit test for function toggle_variable
def test_toggle_variable():

    import unittest.mock

    get_workbench().set_variable(_OPTION_NAME, False)
    get_workbench().get_option = unittest.mock.MagicMock(return_value=True)
    update_environment()


# Generated at 2022-06-22 13:04:30.014243
# Unit test for function update_environment
def test_update_environment():
    # Test that PGZERO_MODE is set to "auto" if not in simple mode
    get_workbench().in_simple_mode = lambda: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test that PG_ZERO_MODE is "True" if in simple mode
    get_workbench().in_simple_mode = lambda: True
    update_environme

# Generated at 2022-06-22 13:04:31.278285
# Unit test for function update_environment
def test_update_environment():
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:04:32.475919
# Unit test for function update_environment
def test_update_environment():
    # FIXME: implement this
    pass

# Generated at 2022-06-22 13:04:33.860570
# Unit test for function toggle_variable
def test_toggle_variable():
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:04:44.393263
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import MagicMock
    mock_get_workbench = MagicMock()
    mock_get_workbench.in_simple_mode.return_value = False
    mock_get_workbench.get_option.return_value = False
    mock_get_workbench.get_variable.return_value.set = MagicMock()
    mock_get_workbench.get_variable().set.side_effect = Exception("")
    mock_get_workbench.get_variable().get.side_effect = [True, False]
    toggle_variable()
    print(mock_get_workbench.mock_calls)
    mock_get_workbench.get_variable().set.assert_called_once_with(mock_get_workbench.get_option.return_value)
    mock_

# Generated at 2022-06-22 13:04:55.477988
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.globals import get_runner
    from thonny.misc_utils import running_on_windows

    get_workbench().set_simple_mode(False)

    load_plugin()

    assert get_workbench().get_option(_OPTION_NAME) == False

    toggle_variable()

    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()

    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    toggle_variable()

    assert get_workbench().get_option(_OPTION_NAME) == False

   

# Generated at 2022-06-22 13:05:09.596227
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    
    assert not wb.get_variable(_OPTION_NAME)
    assert "PGZERO_MODE" not in os.environ
    
    wb.set_simple_mode(True)
    update_environment()
    
    assert "PGZERO_MODE" not in os.environ
    
    
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    
    assert os.environ["PGZERO_MODE"] == "True"
    
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    

# Generated at 2022-06-22 13:05:21.452318
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from thonny.config import get_config_dir
    from thonny.config_ui import ConfigurationPage
    from thonny.globals import get_workbench
    from thonny.globals import get_runner
    import tkinter as tk


    get_workbench().set_default(_OPTION_NAME, None)
    assert os.getenv("PGZERO_MODE") is None
    root = tk.Tk()
    root.geometry("350x200")
    workbench = Workbench(root)
    ConfigurationPage(workbench.get_configuration_dialog())
    assert get_workbench().get_option("last_configuration_page_class") ==\
        "thonny.config_ui.ConfigurationPage"
    # Sim

# Generated at 2022-06-22 13:05:29.771566
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    class MockTk:
        def call(self, command, *args, **kwargs):
            pass
    class MockEvent:
        def add(self, command, *args, **kwargs):
            pass

    from types import SimpleNamespace
    wb.tk = MockTk()
    wb.event = MockEvent()
    wb.in_simple_mode = lambda: False

    wb.get_variable = lambda name: SimpleNamespace(get=lambda:False)
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:05:34.014493
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    var = wb.get_variable(_OPTION_NAME)
    assert var.get() == False
    toggle_variable()
    assert var.get() == True
    toggle_variable()
    assert var.get() == False

# Generated at 2022-06-22 13:05:43.388197
# Unit test for function update_environment
def test_update_environment():
    use_workbench = get_workbench()
    simplemode = use_workbench.in_simple_mode()
    use_workbench._simple_mode  = True
    update_environment()
    
    assert os.environ["PGZERO_MODE"] == "auto"
    
    use_workbench._simple_mode = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    use_workbench._simple_mode = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    
    use_workbench._simple_mode  = simplemode

# Generated at 2022-06-22 13:05:52.584121
# Unit test for function load_plugin
def test_load_plugin():
    # 1. Test that the plugin loads without error
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
    assert wb.get_variable(_OPTION_NAME) == False
    # 2. Test that the plugin toggles correctly
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME) == True
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME) == False
    # 3. Test that the environment variables are changed correctly
    update_environment()
   

# Generated at 2022-06-22 13:06:01.056538
# Unit test for function update_environment
def test_update_environment():
    import os
    import thonny
    get_workbench().set_simple_mode(True)
    update_environment()

# Generated at 2022-06-22 13:06:06.950854
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:06:16.606938
# Unit test for function toggle_variable
def test_toggle_variable():
    # Test initial state
    assert not get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test toggling
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert not get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:23.077392
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.register_command("toggle_pgzero_mode", "run", "", toggle_variable, flag_name=_OPTION_NAME)
    assert (wb.get_option(_OPTION_NAME) == False)
    assert (os.getenv("PGZERO_MODE") == "False")
    toggle_variable()
    assert (wb.get_option(_OPTION_NAME) == True)
    assert (os.getenv("PGZERO_MODE") == "True")
    wb.set_default(_OPTION_NAME, False)
    wb.set_simple_mode(True)
    assert (os.getenv("PGZERO_MODE") == "auto")

# Generated at 2022-06-22 13:06:43.495251
# Unit test for function update_environment
def test_update_environment():
    # test simple_mode
    os.environ["PGZERO_MODE"] = "0"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # test not simple_mode
    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:06:50.555485
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    # mock tkinter
    import unittest.mock as mock
    original = mock.MagicMock()
    get_workbench().tk = original
    mock_tk = mock.MagicMock()
    get_workbench().tk = mock_tk
    workbench_main = Workbench.main
    # mock entrypoint
    import unittest.mock as mock
    original = mock.MagicMock()
    (Workbench.main,) = (original,)
    mock_entrypoint = mock.MagicMock()
    (Workbench.main,) = (mock_entrypoint,)
    # mock set_default
    import unittest.mock as mock
    original = mock.MagicMock()
    (get_workbench().set_default,) = (original,)
    mock

# Generated at 2022-06-22 13:06:51.559534
# Unit test for function load_plugin
def test_load_plugin():
    # TODO: provide a unit test
    assert True

# Generated at 2022-06-22 13:07:02.086314
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(True)
    assert "PGZERO_MODE" not in os.environ
    wb.set_simple_mode(False)
    os.environ.pop("PGZERO_MODE", None)
    assert "PGZERO_MODE" not in os.environ
    wb.set_simple_mode(True)
    assert "PGZERO_MODE" not in os.environ
    os.environ["PGZERO_MODE"] = "True"
    wb.set_simple_mode(False)
    assert "PGZERO_MODE" in os.environ
    wb.set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:03.148407
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:07:05.884730
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_option(_OPTION_NAME, True)
    toggle_variable()
    get_workbench().set_option(_OPTION_NAME, False)
    toggle_variable()
    toggle_variable()

# Generated at 2022-06-22 13:07:10.774517
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os.environ["PGZERO_MODE"] == 'False'


# Generated at 2022-06-22 13:07:22.580173
# Unit test for function load_plugin
def test_load_plugin():
    print("test_load_plugin")

# Generated at 2022-06-22 13:07:25.568229
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    var = get_workbench().get_variable(_OPTION_NAME)
    assert var.get() == False



# Generated at 2022-06-22 13:07:33.287332
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    workbench = Workbench()
    load_plugin()

    assert workbench.get_default("run.pgzero_mode") == False
    assert workbench.commands["toggle_pgzero_mode"]["flag_name"] == "run.pgzero_mode"
    assert workbench.commands["toggle_pgzero_mode"]["group"] == 40
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:01.731456
# Unit test for function load_plugin
def test_load_plugin():
    from test.test_processor import temp_dir

    wb = get_workbench()
    wb.set_default(_OPTION_NAME,False)
    # load_plugin()

    assert wb.get_option(_OPTION_NAME) == False

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True

    # assert os.environ["PGZERO_MODE"] == 'True'
    update_environment()



if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:08:07.283199
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

# Generated at 2022-06-22 13:08:19.343108
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest import mock
    import thonny
    import thonny.workbench

    def _get_workbench():
        if not hasattr(thonny, "_workbench"):
            thonny._workbench = thonny.workbench.Workbench()
            thonny.workbench.load_plugin_manager()
        return thonny._workbench

    toggle_variable()
    assert _get_workbench().get_option(_OPTION_NAME) == True

    toggle_variable()
    assert _get_workbench().get_option(_OPTION_NAME) == False

    # Unit test for function update_environment
    def test_update_environment():
        from unittest import mock
        import os

        _get_workbench().set_option(_OPTION_NAME, True)

        # mock out in_

# Generated at 2022-06-22 13:08:21.277341
# Unit test for function load_plugin
def test_load_plugin():
    test_workbench = Workbench()
    load_plugin()
    test_workbench.destroy()

# Generated at 2022-06-22 13:08:28.542895
# Unit test for function update_environment
def test_update_environment():
    # TEST: test updating of os.environ["PGZERO_MODE"]
    assert os.getenv("PGZERO_MODE") == "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "False"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "True"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "auto"

# Generated at 2022-06-22 13:08:34.632654
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_default(_OPTION_NAME) == False
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:45.381198
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest import mock
    from thonny.workbench import Workbench
    from thonny.memory import GlobalVariable
    from thonny import get_workbench
    get_workbench().destroy() # This is needed because the workbench is created during import, but we need a mock one.
    parent = tkinter.Tk()
    mock_wb = Workbench(parent)
    mock_wb._global_variables = {_OPTION_NAME: GlobalVariable(_OPTION_NAME, False)}
    mock_wb._in_simple_mode = mock.Mock(return_value=False)
    with mock.patch('os.environ', {}):
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:08:50.377104
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, False)
    toggle_variable()
    assert workbench.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert workbench.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:08:58.234241
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from thonny import get_workbench
    get_workbench().in_simple_mode = lambda : True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    Workbench.in_simple_mode = lambda self : False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:09:08.010302
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "None"    
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
    
    os.environ["PGZERO_MODE"] = "None"    
    
if __name__ == "__main__":
    test_update_

# Generated at 2022-06-22 13:10:11.460612
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

    assert get_workbench().get_option(_OPTION_NAME) == False

    toggle_variable()

    assert get_workbench().get_option(_OPTION_NAME) == True

    toggle_variable()

    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:10:16.321536
# Unit test for function load_plugin
def test_load_plugin():
    import thonny
    from thonny.plugins.run.run_pgzero_mode import load_plugin
    from thonny import get_workbench

    thonny.workbench = thonny.ThonnyWorkbench()
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert get_workbench().in_simple_mode() == False
    assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2022-06-22 13:10:24.240337
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

if __name__ == "__main__":
    test_update_environment()

# Generated at 2022-06-22 13:10:29.238269
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_option(_OPTION_NAME) == False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:10:40.874067
# Unit test for function update_environment
def test_update_environment():
    original_envvars = os.environ


# Generated at 2022-06-22 13:10:46.265553
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:10:50.766582
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    var = wb.get_variable(_OPTION_NAME)
    assert var.get() == False
    toggle_variable()
    assert var.get() == True
    toggle_variable()
    assert var.get() == False

# Generated at 2022-06-22 13:10:52.856702
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    result = get_workbench().get_variable(_OPTION_NAME)
    assert result.get() == True

# Generated at 2022-06-22 13:11:00.803423
# Unit test for function update_environment
def test_update_environment():
    old_value = os.environ.get("PGZERO_MODE")
    try:
        get_workbench().set_simple_mode(True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"
    finally:
        # Restore original value
        get_workbench().set_simple_mode(False)
        if old_value is None:
            del os.environ["PGZERO_MODE"]
        else:
            os.environ["PGZERO_MODE"] = old_value

# Generated at 2022-06-22 13:11:05.887480
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    wb = Mock()
    wb.get_option = Mock(return_value=False)
    wb.in_simple_mode = Mock(return_value=False)
    get_workbench.return_value = wb
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'False'