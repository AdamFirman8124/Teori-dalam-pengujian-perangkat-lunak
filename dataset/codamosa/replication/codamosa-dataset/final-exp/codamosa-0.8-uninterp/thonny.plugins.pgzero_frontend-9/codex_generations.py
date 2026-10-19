

# Generated at 2022-06-22 13:02:38.355734
# Unit test for function load_plugin
def test_load_plugin():
    return

# Generated at 2022-06-22 13:02:46.853614
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default("run.pgzero_mode", "False")
    load_plugin()
    assert wb.get_command("toggle_pgzero_mode")
    assert "PGZERO_MODE" not in os.environ
    get_workbench().event_generate("ThemeChanged", theme_name="simple")
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.unload_plugin("pgzero_mode")
    assert "PGZERO_MODE" not in os.environ

# Generated at 2022-06-22 13:02:54.306740
# Unit test for function update_environment
def test_update_environment():
    sys.modules["thonny.workbench"]._set_active_shell_type("IPython")
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    sys.modules["thonny.workbench"]._set_active_shell_type("PythonShell")
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    sys.modules["thonny.workbench"]._set_active_shell_type("PythonShell")
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:06.111149
# Unit test for function load_plugin
def test_load_plugin():
    # test side effect: add command to run menu
    assert get_workbench().in_simple_mode()
    get_workbench().set_simple_mode(False)
    
    wb = get_workbench()
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ['PGZERO_MODE'] == 'False'
    
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ['PGZERO_MODE'] == 'True'
    
    get_workbench().set_simple_mode(True)
    load_plugin()
    assert os.environ['PGZERO_MODE'] == 'auto'

# Generated at 2022-06-22 13:03:12.053406
# Unit test for function update_environment
def test_update_environment():
    # Called before get_workbench().get_option()
    get_workbench().in_simple_mode = lambda: True
    get_workbench().get_option = lambda *args: None
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Called before get_workbench().get_option()
    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda *args: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:16.819914
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:03:19.549432
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:29.352891
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_shell
    from thonny.shell import ShellTextWidget
    from thonny import get_workbench
    from thonny.languages import tr
    from thonny.workflow import Command
    import os
    import thonny
    import sys
    workbench = get_workbench()
    assert "PGZERO_MODE" not in os.environ
    load_plugin()
    workbench.set_default(_OPTION_NAME, "test")
    update_environment()
    assert os.environ["PGZERO_MODE"] == "test"
    workbench.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    test_shell = get_shell()
    test_shell.text_widget = Shell

# Generated at 2022-06-22 13:03:35.925538
# Unit test for function update_environment
def test_update_environment():
    # reset environment before testing
    old_env = os.environ.get("PGZERO_MODE", "auto")
    os.environ["PGZERO_MODE"] = "auto"
    from thonny.workbench import Workbench
    from unittest import mock

    # setup
    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.set_option(_OPTION_NAME, False)
    os.environ["PGZERO_MODE"] = "auto"

    # assert in simple mode
    assert wb.in_simple_mode()
    assert os.environ.get("PGZERO_MODE", False) == "auto"

    # change simple mode
    wb.get_option("view.simple_mode").set(False)
    wb.simple_

# Generated at 2022-06-22 13:03:40.644448
# Unit test for function update_environment
def test_update_environment():
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

# Generated at 2022-06-22 13:03:54.022208
# Unit test for function load_plugin
def test_load_plugin():
    try:
        del os.environ["PGZERO_MODE"]
    except KeyError:
        pass

    from thonny import get_workbench
    from thonny.languages import tr

    from thonny.plugins.pgzero.pgzero_plugin import load_plugin
    from thonny.plugins.pgzero.pgzero_plugin import toggle_variable
    from thonny.plugins.pgzero.pgzero_plugin import update_environment

    _OPTION_NAME = "run.pgzero_mode"

    load_plugin()

    pgzero_mode = get_workbench().get_option(_OPTION_NAME)

    assert pgzero_mode == False

    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()

    pgzero_mode = get_workbench().get_option

# Generated at 2022-06-22 13:03:57.049708
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

if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:04:03.775954
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:08.077216
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default("run.pgzero_mode", True)
    toggle_variable()
    assert not wb.get_option("run.pgzero_mode")
    toggle_variable()
    assert wb.get_option("run.pgzero_mode")

# Generated at 2022-06-22 13:04:17.068714
# Unit test for function toggle_variable
def test_toggle_variable():
    try:
        # create a simple_mode runconfig:
        with tempfile.TemporaryDirectory() as temp_dir:
            demo_file = os.path.join(temp_dir, "demo.py")
            with open(demo_file, "w") as fp:
                fp.write(
                    '# run with --mode=simple\nprint("Hello world!")\npass'
                )

            run_config = RunConfiguration(demo_file, "simple")
            get_workbench().set_run_configuration(run_config)

    except:
        # run mode was not set to simple, but that's okay for the unit test
        pass

    # start unit testing:

    # get the current value of the pgzero flag from the workbench
    # if it doesn't exist, it will be created
    pg

# Generated at 2022-06-22 13:04:23.200181
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_variable(_OPTION_NAME).get() == False
    load_plugin()
    var = get_workbench().get_variable(_OPTION_NAME)
    assert var.get() == False
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:04:26.262056
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:04:36.791134
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_option(_OPTION_NAME) == False

    load_plugin()
    assert list(get_workbench().get_commands().keys()) == ["toggle_pgzero_mode"]
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple

# Generated at 2022-06-22 13:04:42.056896
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = ""
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:04:53.169545
# Unit test for function update_environment
def test_update_environment():
    import thonny.plugins.pgzero_mode

    wb = get_workbench()
    wb.set_simple_mode(True)
    thonny.plugins.pgzero_mode.update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.set_simple_mode(False)
    wb.set_option(thonny.plugins.pgzero_mode._OPTION_NAME, True)
    thonny.plugins.pgzero_mode.update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    wb.set_simple_mode(False)
    wb.set_option(thonny.plugins.pgzero_mode._OPTION_NAME, False)
    thonny.plugins.pgzero_mode.update

# Generated at 2022-06-22 13:05:09.198654
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench

    # Test if _OPTION_NAME is in the dictionary variables.
    assert _OPTION_NAME in get_workbench().variables
    # Test if value for key _OPTION_NAME is True. (Can be False if testing GUI.)
    assert get_workbench().variables[_OPTION_NAME] == True
    # Test if key "PGZERO_MODE" is in the dictionary variables.
    assert "PGZERO_MODE" in os.environ
    # Test if value for key "PGZERO_MODE" is True. (Can be False if testing GUI.)
    assert os.environ["PGZERO_MODE"] == "True"
    # Test if key "PGZERO_MODE" is in the dictionary variables.
    assert "PGZERO_MODE" in os.environ
    toggle

# Generated at 2022-06-22 13:05:16.368258
# Unit test for function load_plugin
def test_load_plugin():
    import thonny

    thonny._get_workbench().clear_commands()
    load_plugin()

    assert thonny._get_workbench().get_default(_OPTION_NAME) == False
    assert thonny._get_workbench().get_option(_OPTION_NAME) == False
    assert thonny._get_workbench().get_variable(_OPTION_NAME).get() == False

    assert len(thonny._get_workbench().commands) == 1

# Generated at 2022-06-22 13:05:17.802237
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)

# Generated at 2022-06-22 13:05:19.969202
# Unit test for function update_environment
def test_update_environment():
    assert os.environ["PGZERO_MODE"] == "0", os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:05:30.879329
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock
    from thonny import get_workbench
    from thonny.plugins.run import _OPTION_NAME

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_variable(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_variable(_OPTION_NAME, True)
    update_environment()

# Generated at 2022-06-22 13:05:36.064407
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:05:39.380103
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:05:49.277489
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import get_editor
    
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == 'True'

    toggle_variable()    
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == 'False'

    get_workbench().set_default(_OPTION_NAME, True)
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == 'True'

# Generated at 2022-06-22 13:06:00.706417
# Unit test for function update_environment
def test_update_environment():
    import os
    import unittest
    from unittest.mock import MagicMock
    from thonny import get_workbench
    from test.test_base import run_with_append_argv

    saved_env = os.environ["PGZERO_MODE"]

    def run_in_simple_mode():
        os.environ["PGZERO_MODE"] = "auto"
        wb = MagicMock()
        wb.in_simple_mode.return_value = True
        get_workbench().set_option(_OPTION_NAME, "A")
        get_workbench()._wb = wb
        update_environment()
        unittest.TestCase().assertEqual(os.environ["PGZERO_MODE"], "auto")
        get_workbench()._wb = None


# Generated at 2022-06-22 13:06:10.250852
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import running_on_mac_os

    if running_on_mac_os():
        # pygamezero is not installed on macOS
        return

    from thonny.globals import get_runner, get_workbench, get_shell

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_option("run.use_shell", True)
    get_shell().clear_output()
    get_runner().execute_source("from pgzero import *\nfrom pgzero.loaders import sounds\nprint(env.PGZERO_MODE)", "fake")
    time.sleep(0.1)
    assert get_shell().get_feedback("stdout")[0] == "False"

# Generated at 2022-06-22 13:06:26.227498
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)


# Generated at 2022-06-22 13:06:33.278950
# Unit test for function update_environment
def test_update_environment():
    try:
        del os.environ["PGZERO_MODE"]
    except KeyError:
        pass

    # checking simple mode
    get_workbench().set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_edit_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().get_option(_OPTION_NAME).set(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().get_option(_OPTION_NAME).set(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Unit test

# Generated at 2022-06-22 13:06:37.099120
# Unit test for function update_environment
def test_update_environment():
    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    workbench.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    workbench.set_simple_mode(True)
    del os.environ["PGZERO_MODE"]
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:46.322634
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock

    # TODO: set_simple_mode should not be mocked, but this is the easiest way to restore previous value
    set_simple_mode = mock.patch("thonny.workbench.Workbench.set_simple_mode").start()


# Generated at 2022-06-22 13:06:49.137789
# Unit test for function update_environment
def test_update_environment():
    assert os.environ["PGZERO_MODE"] == "False"
    # toggle_variable()
    # assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:57.563205
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert get_workbench().get_variable(_OPTION_NAME) == False

    get_workbench().set_simple_mode()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_advanced_mode()
    get_workbench().get_variable(_OPTION_NAME).set(True)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:01.181725
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.create()

    assert _OPTION_NAME not in wb.configuration
    load_plugin()
    assert wb.configuration[_OPTION_NAME] is False
    assert wb.get_variable("run.pgzero_mode") is not None



# Generated at 2022-06-22 13:07:05.233559
# Unit test for function load_plugin
def test_load_plugin():
    print('load_plugin')
    test_wb = get_workbench()
    load_plugin()
    assert(test_wb.get_variable(_OPTION_NAME) == False)


# Generated at 2022-06-22 13:07:11.022346
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:07:17.800094
# Unit test for function update_environment
def test_update_environment():
    # pylint: disable=global-statement
    global _OPTION_NAME
    _OPTION_NAME = "thonny.plugins.pgzero_mode.run.pgzero_mode"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:50.701210
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.languages import tr
    from thonny.common import get_runner
    from thonny.workflow import SimpleWorkflow
    get_runner().run_source("run_pip_command('install pgzero')")
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.set_default("view.hide_toolbar", False)
    wb.set_default("view.hide_status_bar", False)
    wb.set_default("view.hide_side_panel", False)
    wb.reset_view_options()
    wb.set_default("run.backend", "Python")
    wb.set_default("run.environment", "venv")
    wb

# Generated at 2022-06-22 13:08:00.138815
# Unit test for function update_environment
def test_update_environment():
    test_workbench = get_workbench()
    test_workbench.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    test_workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    test_workbench.set_option(_OPTION_NAME, False)
    test_workbench.set_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    test_workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:04.469411
# Unit test for function update_environment
def test_update_environment():
    p = get_workbench().get_variable(_OPTION_NAME)
    p.set(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    p.set(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().in_simple_mode_ = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:06.717104
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.destroy()
    wb.create()
    load_plugin()
    assert wb.get_option(_OPTION_NAME) is False
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:10.550328
# Unit test for function update_environment
def test_update_environment():
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == str(not get_workbench().get_option(_OPTION_NAME))

# Generated at 2022-06-22 13:08:16.370630
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()

    from thonny.plugins.run import load_plugin

    # Check default option
    assert get_workbench().get_option(
        _OPTION_NAME
    ) == False  # noqa: E712,E714 pylint: disable=singleton-comparison



# Generated at 2022-06-22 13:08:22.254134
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default("run.pgzero_mode", False)
    load_plugin()
    assert get_workbench().get_variable("run.pgzero_mode")
    assert get_workbench().get_option("run.pgzero_mode") == False
    assert os.environ["PGZERO_MODE"] == "False"



# Generated at 2022-06-22 13:08:27.466534
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    from unittest.mock import Mock

    b = Workbench()
    m = Mock()
    b.add_command = m
    b.set_default = m

    load_plugin()
    m.assert_called_with("toggle_pgzero_mode", "run", tr("Pygame Zero mode"), toggle_variable, flag_name=_OPTION_NAME, group=40)

# Generated at 2022-06-22 13:08:38.502576
# Unit test for function load_plugin
def test_load_plugin():
    wb = mock.Mock()
    wb.get_variable = mock.Mock(return_value=MockVariable(False))
    wb.add_command = mock.Mock()
    wb.set_default = mock.Mock()
    wb.in_simple_mode = mock.Mock(return_value=False)

    global get_workbench
    get_workbench = mock.Mock(return_value=wb)

    global update_environment
    update_environment = mock.Mock()

    global os
    os = mock.Mock()
    load_plugin()

    os.environ.__setitem__.assert_called_once_with("PGZERO_MODE", "False")
    wb.set_default.assert_called_once_with(_OPTION_NAME, False)
   

# Generated at 2022-06-22 13:08:41.244197
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:09:36.291549
# Unit test for function update_environment
def test_update_environment():
    os.environ.clear()
    update_environment()
    assert "PGZERO_MODE" in os.environ

if __name__ == "__main__":
    test_update_environment()

# Generated at 2022-06-22 13:09:38.854529
# Unit test for function toggle_variable
def test_toggle_variable():

    for _ in range(2):
        toggle_variable()
        env = os.environ["PGZERO_MODE"]
        assert 'True' == env or 'False' == env

# Generated at 2022-06-22 13:09:47.812066
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:09:59.479423
# Unit test for function update_environment
def test_update_environment():
    from test.config_helper import (
        get_config,
        get_config_value,
        get_default_value,
        set_config_value,
    )
    from test.config_helper import set_default_value

    os.environ.pop("PGZERO_MODE", None)

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    set_config_value(
        get_config(), _OPTION_NAME, True
    )  # option takes precedence
    update_environment()

# Generated at 2022-06-22 13:10:03.763884
# Unit test for function load_plugin
def test_load_plugin():
    wb = Workbench()
    load_plugin()
    assert wb.get_variable(_OPTION_NAME).get() == False
    assert wb.get_command("toggle_pgzero_mode")

if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:10:13.591765
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import running_on_mac_os, running_on_windows, running_on_linux
    from thonny.globals import get_workbench
    from unittest.mock import MagicMock, patch

    # running_on_mac_os = True
    # running_on_windows = True
    # running_on_linux = True
    simple_mode_false_mock = MagicMock(side_effect=[False])
    simple_mode_true_mock = MagicMock(side_effect=[True])

    def wb_get():
        return False

    def wb_get_simple():
        return True

    # Check without envirnoment
    update_environment()

# Generated at 2022-06-22 13:10:19.147506
# Unit test for function toggle_variable
def test_toggle_variable():
    if get_workbench().get_option("run.pgzero_mode"):
        os.environ["PGZERO_MODE"] = str(True)
    else:
        os.environ["PGZERO_MODE"] = str(False)
    toggle_variable()
    if os.environ["PGZERO_MODE"] == str("False"):
        print("Pass")
    else:
        print("Failed")



# Generated at 2022-06-22 13:10:23.904558
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    assert wb.get_option(_OPTION_NAME) == False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:10:26.491711
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True



# Generated at 2022-06-22 13:10:38.339545
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny import get_workbench, get_runner
    from thonny.plugins.pgzero_mode_plugin import _OPTION_NAME
    from thonny.languages import tr
    from thonny.globals import get_workbench
    import os

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()