

# Generated at 2022-06-22 13:02:47.750679
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "True"


# Generated at 2022-06-22 13:02:52.768383
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().reset_global_state()
    assert get_workbench().get_option(_OPTION_NAME) == False
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:03:02.563565
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:10.789460
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.unload_plugin("pgzero_mode")
    load_plugin()
    assert wb._default_values[_OPTION_NAME] == False
    assert wb.get_variable(_OPTION_NAME).get() == False
    assert "PGZERO_MODE" not in os.environ
    wb.get_variable(_OPTION_NAME).set(True)
    assert wb.get_variable(_OPTION_NAME).get() == True
    assert os.environ["PGZERO_MODE"] == "True"
    wb.unload_plugin("pgzero_mode")
    assert not hasattr(wb, _OPTION_NAME)
    assert "PGZERO_MODE" not in os.environ

# Generated at 2022-06-22 13:03:16.612808
# Unit test for function toggle_variable
def test_toggle_variable():
    """
    When PGzero_mode is set to false,
    toggle_variable sets PGzero_mode to True and vice versa
    """
    get_workbench().set_option(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:03:24.253248
# Unit test for function update_environment
def test_update_environment():
    from test.test_env import create_workbench

    wb = create_workbench()
    wb.set_default(_OPTION_NAME, True)
    wb.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:03:32.475802
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    assert _OPTION_NAME in wb.get_defaults()
    assert _OPTION_NAME not in wb.get_variables()
    load_plugin()
    var = wb.get_variable(_OPTION_NAME)
    assert var is not None
    assert var.get() == False
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "False"
    var.set(True)
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:03:39.107031
# Unit test for function load_plugin
def test_load_plugin():
    try:
        del os.environ["PGZERO_MODE"]
    except KeyError:
        pass
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().get_variable(_OPTION_NAME).set(True)
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:39.790345
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:03:44.336908
# Unit test for function load_plugin
def test_load_plugin():
    assert get_workbench().in_simple_mode()
    assert get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "auto"


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:03:54.957619
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    assert wb.get_option(_OPTION_NAME) == False
    assert wb.get_variable(_OPTION_NAME).get() == False
    assert os.environ.get("PGZERO_MODE") == "auto"

# Generated at 2022-06-22 13:04:04.068281
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "true"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "false"

# Generated at 2022-06-22 13:04:09.272518
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    load_plugin()
    assert wb.get_variable(_OPTION_NAME) is not None
    assert wb.get_command("toggle_pgzero_mode") is not None
    assert wb.get_option(_OPTION_NAME) is True

load_plugin()

# Generated at 2022-06-22 13:04:20.451071
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from thonny.config_ui import ConfigurationPage
    from thonny import get_runner
    import tkinter as tk

    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().destroy()
    get_workbench().create_toplevels()

    load_plugin()
    assert _OPTION_NAME in get_workbench().get_default_options()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert get_workbench().get_variable(_OPTION_NAME).get() == True
    get_workbench().get_variable(_OPTION_NAME).set(False)
    assert get_workbench().get_variable(_OPTION_NAME).get() == False

# Generated at 2022-06-22 13:04:25.736006
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:36.368145
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from thonny.testing import TemporaryTextMode
    from thonny.workbench import Workbench
    import tkinter as tk
    from thonny.globals import get_runner

    workbench = Workbench(tk.Tk())
    workbench.in_simple_mode = mock.Mock(return_value=True)

    with TemporaryTextMode(workbench):
        import thonny.plugins.pgzero_mode
        thonny.plugins.pgzero_mode.load_plugin()

        get_workbench().invoke("toggle_pgzero_mode")

# Generated at 2022-06-22 13:04:45.955326
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.config import set_default_workbench_config
    from thonny.languages import get_languages_menu_definition
    from thonny.workbench import Workbench
    from thonny.misc_utils import running_on_mac_os

    get_workbench().bind("Run.BeginRun", lambda: None)
    set_default_workbench_config()
    workbench = Workbench()
    workbench.create()
    load_plugin()

    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().get_variable(_OPTION_NAME).set(True)

# Generated at 2022-06-22 13:04:47.870514
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)

# Generated at 2022-06-22 13:04:58.217832
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()

    assert "toggle_pgzero_mode" in wb.get_command_names()
    assert _OPTION_NAME in wb.get_variable_names()
    assert "PGZERO_MODE" not in os.environ

    wb.set_option(_OPTION_NAME, True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_option(_OPTION_NAME, False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple_mode(True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:05:06.643029
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "off"
    from thonny import get_workbench

    workbench = get_workbench()
    workbench.set_simple_mode(True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "auto"

    workbench.set_simple_mode(False)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "off"

    workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == "auto"

# Generated at 2022-06-22 13:05:28.563476
# Unit test for function update_environment
def test_update_environment():
    env = dict(os.environ)
    try:
        wb = get_workbench()
        wb.set_default(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"
        wb.set_default(_OPTION_NAME, False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
        os.environ["THONNY_SIMPLE_MODE"] = "1"
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"
    finally:
        os.environ.clear()
        os.environ.update(env)

# Generated at 2022-06-22 13:05:33.143881
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = ""
    update_environment()
    os.environ["PGZERO_MODE"] = ""
    toggle_variable()
    update_environment()
    os.environ["PGZERO_MODE"] = ""
    toggle_variable()
    update_environment()

# Generated at 2022-06-22 13:05:38.597654
# Unit test for function update_environment
def test_update_environment():
    from thonny.globals import get_workbench
    from unittest.mock import patch
    from thonny import get_runner

    with patch.object(get_workbench(), "_primary_view") as mock_view:
        mock_view._configuration_name = "Simple"
        get_workbench().in_simple_mode = True
        mock_view.run_dir = "run_dir"
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"

    with patch.object(get_workbench(), "_primary_view") as mock_view:
        del mock_view
        get_workbench().in_simple_mode = False
        get_workbench().get_option = lambda x: True
        update_environment()

# Generated at 2022-06-22 13:05:42.854548
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    assert wb.get_option(_OPTION_NAME) == False
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == False
    assert wb.get_variable(_OPTION_NAME) != None

# Generated at 2022-06-22 13:05:52.470676
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench, configure_workbench, workbench_configuration_location

    os.environ["PGZERO_MODE"] = "auto"
    
    # remove all configuration files
    for file in os.listdir(workbench_configuration_location()):
        if file.endswith(".pickle"):
            os.remove(os.path.join(workbench_configuration_location(), file))

    # call load plugin
    load_plugin()

    # test loading variable
    assert not get_workbench().get_variable("run.pgzero_mode")

    # test loading environment variable
    assert os.environ["PGZERO_MODE"] == "False"
    
    # test loading simple mode
    configure_workbench(simple_mode=True)

# Generated at 2022-06-22 13:05:56.424654
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"



# Generated at 2022-06-22 13:06:01.951810
# Unit test for function update_environment
def test_update_environment():
    new_workbench = setup_test_env()
    new_workbench.set_default(_OPTION_NAME, False)
    new_workbench.set_simple_mode(True)
    del os.environ["PGZERO_MODE"]
    update_environment()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:10.856976
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from unittest.mock import MagicMock
    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.add_command = MagicMock(return_value=None)
    load_plugin()
    assert wb.get_variable(_OPTION_NAME)
    wb.add_command.assert_called_with(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    assert os.environ["PGZERO_MODE"] == "False"
    wb.in_simple_mode =  MagicMock(return_value=True)

# Generated at 2022-06-22 13:06:19.734762
# Unit test for function load_plugin
def test_load_plugin():
    # setup
    initial_pgzero_mode = os.environ.get("PGZERO_MODE")
    if initial_pgzero_mode:
        del os.environ["PGZERO_MODE"]
    get_workbench().set_simple_mode(True)
    get_workbench().set_option(_OPTION_NAME, True)
    assert os.environ.get("PGZERO_MODE") is None

    # test
    load_plugin()
    assert os.environ.get("PGZERO_MODE") == "auto"
    get_workbench().set_simple_mode(False)
    toggle_variable()
    assert get_workbench().option(_OPTION_NAME)
    assert os.enviro

# Generated at 2022-06-22 13:06:29.864646
# Unit test for function update_environment
def test_update_environment():
    from thonny.plugins.run.simple_executor import SimpleExecutor
    from thonny.runner import SimpleRunner
    from thonny import get_workbench

    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_option("view.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:58.531370
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    get_workbench().event_generate("WorkbenchConfigChange")
    assert get_workbench().get_option(_OPTION_NAME) == False #noqa

# Generated at 2022-06-22 13:07:01.217607
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_option(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) is False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True

# Generated at 2022-06-22 13:07:10.088302
# Unit test for function update_environment
def test_update_environment():
    import os
    import unittest.mock
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    with unittest.mock.patch("thonny.workbench.Workbench.in_simple_mode", return_value=False):
        with unittest.mock.patch("thonny.workbench.Workbench.get_option", return_value=False):
            update_environment()
            assert os.environ["PGZERO_MODE"] == "False"
        with unittest.mock.patch("thonny.workbench.Workbench.get_option", return_value=True):
            update_environment()
            assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:18.366751
# Unit test for function update_environment
def test_update_environment():
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_default("run.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:29.584584
# Unit test for function load_plugin
def test_load_plugin():
    import unittest.mock
    wb = unittest.mock.Mock()
    wb.in_simple_mode = lambda: False
    wb.get_option = lambda x: False
    with unittest.mock.patch("thonny.plugins.pgzero_mode.get_workbench") as g:
        g.return_value = wb
        load_plugin()
        wb.set_default.assert_called_once_with(_OPTION_NAME, False)
        wb.add_command.assert_called_once_with(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )

# Generated at 2022-06-22 13:07:36.901072
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) == False

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:07:40.834898
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock

    with mock.patch("thonny.plugins.pgzero_mode.toggle_variable") as toggle_variable_mock:
        load_plugin()
        assert toggle_variable_mock.call_count == 0

# Generated at 2022-06-22 13:07:52.176254
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.outline import (
        get_outline_viewer,
        _get_lenient_outline_parser,
        get_outline_plugins,
    )
    from thonny.plugins.outline_based_code_navigation import OutlineCodeNavigationPlugin
    from thonny.plugins.pgzero_mode import PgZeroModePlugin
    from thonny.plugins.simple_mode import SimpleModePlugin
    workbench = get_workbench()
    workbench.bind("Initialize", load_plugin)
    workbench.set_option("run.pgzero_mode", True)
    workbench.bind("ToplevelWindowCreated", lambda event: event.widget.destroy(), True)
    window = workbench.create_window(font_size=20, tk_vars={})
    workbench

# Generated at 2022-06-22 13:08:01.127570
# Unit test for function update_environment
def test_update_environment():
    del os.environ["PGZERO_MODE"]

    get_workbench().set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_advanced_mode()
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_advanced_mode()
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:07.888486
# Unit test for function toggle_variable
def test_toggle_variable():
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:09:02.281411
# Unit test for function update_environment
def test_update_environment():
    class TestFrame():
        def __init__(self, in_simple_mode=False, options={}):
            self.options = options
            self.in_simple_mode = in_simple_mode
            self.key2defs = {}

        def in_simple_mode(self):
            return self.in_simple_mode

        def set_default(self, name, value):
            self.key2defs[name] = value

        def get_option(self, option_name):
            return self.options.get(option_name)

        def get_option_default(self, option_name):
            return self.key2defs.get(option_name)

    wb = TestFrame(in_simple_mode=True)
    load_plugin()
    update_environment()

# Generated at 2022-06-22 13:09:13.378063
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_in_simple_mode(False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_in_simple_mode(True)
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:09:15.192316
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == False

# Generated at 2022-06-22 13:09:25.917446
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    from thonny.globals import get_workbench
    get_workbench().in_simple_mode = Mock(return_value=False)
    get_workbench().get_option = Mock(return_value=True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == 'True'
    get_workbench().in_simple_mode = Mock(return_value=True)
    update_environment()
    assert os.getenv("PGZERO_MODE") == 'auto'
    get_workbench().get_option = Mock(return_value=False)
    get_workbench().in_simple_mode = Mock(return_value=False)
    update_environment()
    assert os.getenv("PGZERO_MODE") == 'False'

# Generated at 2022-06-22 13:09:36.886529
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import Mock

    workbench = Mock()
    workbench.get_variable = lambda key: key
    workbench.set_variable = lambda key, value: (key, value)
    workbench.get_option = lambda key: key
    workbench.set_option = lambda key, value: (key, value)
    workbench.in_simple_mode = lambda: False
    workbench.add_command = lambda name, menu_name, label, callback, flag_name, group: label
    get_workbench.__self__ = workbench
    load_plugin()
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) is True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) is False
    toggle_variable()
   

# Generated at 2022-06-22 13:09:41.492376
# Unit test for function update_environment
def test_update_environment():
    workbench = get_workbench()
    workbench.set_simple_mode(False)
    workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    workbench.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:09:50.680275
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from unittest.mock import patch

    from thonny import get_workbench

    from thonny.plugins import pgzero

    with patch("thonny.plugins.pgzero.get_workbench") as mock_get_workbench:
        mock_workbench = Mock()
        mock_get_workbench.return_value = mock_workbench
        pgzero.load_plugin()

    assert mock_workbench.set_default.mock_calls == [
        Mock(
            args=("run.pgzero_mode", False), kwargs={},
        )
    ]

# Generated at 2022-06-22 13:09:56.025728
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:02.893486
# Unit test for function update_environment
def test_update_environment():
    from thonny.globals import get_workbench
    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:10:06.618278
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().unset_default(_OPTION_NAME)
    get_workbench().set_default(_OPTION_NAME, True)
    get_workbench().set_default(_OPTION_NAME, False)

# Generated at 2022-06-22 13:12:19.915870
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench

    wb = Workbench()
    load_plugin()
    assert wb.get_option(_OPTION_NAME) is False

# Generated at 2022-06-22 13:12:29.186996
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop("PGZERO_MODE", None)
    
    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda name: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda name: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:12:36.349665
# Unit test for function toggle_variable
def test_toggle_variable():
    update_environment()
    get_workbench().set_in_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    assert os.environ.get("PGZERO_MODE") == "False"
    toggle_variable()
    assert os.environ.get("PGZERO_MODE") == "True"
    toggle_variable()
    assert os.environ.get("PGZERO_MODE") == "False"