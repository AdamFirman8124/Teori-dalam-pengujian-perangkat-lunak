

# Generated at 2022-06-22 13:02:43.407876
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

    assert(os.environ["PGZERO_MODE"] == "False")
    assert(get_workbench().get_option(_OPTION_NAME) == False)

    toggle_variable()

    assert(os.environ["PGZERO_MODE"] == "True")
    assert(get_workbench().get_option(_OPTION_NAME) == True)

# Generated at 2022-06-22 13:02:51.967733
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.misc_utils import running_on_mac_os
    from thonny.misc_utils import running_on_windows

    old_env = os.environ.copy()
    old_mode = get_workbench().get_option(_OPTION_NAME)

    get_workbench().set_option(_OPTION_NAME, False)
    toggle_variable()
    if running_on_mac_os() or running_on_windows():
        assert get_workbench().get_option(_OPTION_NAME) == True
        assert os.environ["PGZERO_MODE"] == "auto"
    else:
        assert get_workbench().get_option(_OPTION_NAME) == False
        assert os.environ["PGZERO_MODE"] == str(get_workbench().get_option(_OPTION_NAME))

# Generated at 2022-06-22 13:02:55.382978
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.misc_utils import running_on_mac_os

    if running_on_mac_os():
        print("Skipping test_load_plugin on Mac OS")
    else:
        from thonny.workbench import Workbench

        the_workbench = Workbench()
        load_plugin()
        the_workbench.destroy()

# Generated at 2022-06-22 13:02:59.484874
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "0"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    os.environ["PGZERO_MODE"] = "1"
    update_environm

# Generated at 2022-06-22 13:03:03.774437
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().in_simple_mode() == False
    assert get_workbench().get_variable(_OPTION_NAME) is not None
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:03:07.881627
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "1"
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "0"


load_plugin()

# Generated at 2022-06-22 13:03:21.413501
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import MagicMock
    from thonny.plugins.pgzero_mode import update_environment
    wb = MagicMock()
    wb.get_option.side_effect = lambda x: [False, True]
    wb.in_simple_mode.side_effect = [True, False, True, False]
    wb.get_option = MagicMock()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.get_option.assert_called_once_with("run.pgzero_mode")
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    update_environment()


# Generated at 2022-06-22 13:03:30.871237
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.globals import get_runner
    from thonny.misc_utils import running_on_mac_os
    from thonny.plugins.run.runner import Runner as RunnerClass

    my_workbench = get_workbench()
    my_runner = get_runner()

    # Start with executing normally
    my_runner.run_command("name_of_program")
    assert my_runner.get_option("pgzero_mode") == False
    assert my_runner.environ["PGZERO_MODE"] == "0"

    # Toggle the variable twice
    my_workbench.execute_command("toggle_pgzero_mode")
    assert my_runner.get_option("pgzero_mode") == True
    assert my_runner.environ["PGZERO_MODE"] == "1"
    my_work

# Generated at 2022-06-22 13:03:36.264940
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().in_simple_mode() is False
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().get_variable(_OPTION_NAME).set(True)
    update_environment()
    assert get_workbench().in_simple_mode() is False
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:45.592281
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny import get_workbench

    wb = get_workbench()

    wb.set_default = Mock()
    wb.add_command = Mock()

    load_plugin()

    wb.set_default.assert_called_with(_OPTION_NAME, False)
    wb.add_command.assert_called_with(
        "toggle_pgzero_mode",
        "run",
        "Pygame Zero mode",
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    # TODO: further testing

# Generated at 2022-06-22 13:04:00.823455
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert "PGZERO_MODE" not in os.environ
    # Test toggle_variable function
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True
    assert os.environ["PGZERO_MODE"] == "True"
    # Test update_environment function
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:09.442621
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    wb = get_workbench()
    wb.delete_user_configuration()
    wb.testing_mode = True
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:19.869157
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import patch, Mock
    from thonny.workbench import Workbench
    from thonny.options_page import OptionsPage

    with patch("thonny.workbench.Workbench") as mock_wb:
        mock_wb.get_default_option.return_value = False

        mock_opt_page = Mock(OptionsPage)
        mock_wb.return_value.get_options_page.return_value = mock_opt_page

        load_plugin()
        wb = Workbench.get_instance()
        wb.set_variable(_OPTION_NAME, True)
        update_environment()

        # Assertions
        assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:22.559115
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert get_workbench().in_simple_mode()
    toggle_variable()
    assert not get_workbench().in_simple_mode()
    toggle_variable()
    assert get_workbench().in_simple_mode()

# Generated at 2022-06-22 13:04:33.908635
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny import get_workbench
    from thonny.plugins.pgzero_mode import load_plugin
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.in_simple_mode = Mock(return_value=False)
    workbench.get_option = Mock(return_value=False)

    options = {
        "run.pgzero_mode": False
    }

    def set_default(option, value):
        options[option] = value

    def get_variable(option):
        class SimpleVar():
            def get(self):
                return options[option]

            def set(self, value):
                options[option] = value

        return SimpleVar()


# Generated at 2022-06-22 13:04:34.680943
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:04:43.830502
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(True)
    wb.set_default(_OPTION_NAME, False)
    del os.environ["PGZERO_MODE"]
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    # TODO: how to test os.environ["PGZERO_MODE"] == "False"?
    wb.set_simple_mode(False)
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:50.998023
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().patch_tkvar(bool, True)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True

# Generated at 2022-06-22 13:05:00.778501
# Unit test for function toggle_variable
def test_toggle_variable():
    # Need to create a workbench object to make thonny read user settings
    # that make the variable _OPTION_NAME available.
    # Otherwise, a KeyError is raised.
    wb = get_workbench()

    # get the variable
    var = wb.get_variable(_OPTION_NAME)

    # case 1: variable does not yet exist => create variable
    try:
        os.environ["PGZERO_MODE"]
    except KeyError:
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "True"

    # case 2: variable is True => set it to False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

   

# Generated at 2022-06-22 13:05:09.359342
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    from thonny.misc_utils import running_on_mac_os
    from thonny.config_ui import ConfigurationPage
    from tkinter import ttk

    def my_create_page():
        page = ConfigurationPage(get_workbench().get_frame(), "Test")
        var = ttk.Checkbutton(page, text="My variable")
        page.add_checkbox(var, "my_variable")

        page.create_entries()
        page.update_entries()
        return page

    ConfigurationPage.create_page = classmethod(my_create_page)

    get_workbench().set_default("my_variable", True)
    update_environment()
    if running_on_mac_os():
        assert os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:05:23.746515
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:05:31.898491
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_simple_mode(True)
    toggle_variable()
    assert get_workbench().in_simple_mode()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_simple_mode(False)
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:05:36.368802
# Unit test for function toggle_variable
def test_toggle_variable():
    load_plugin()
    toggle_variable()
    assert get_workbench().in_simple_mode() == False
    toggle_variable()
    assert get_workbench().in_simple_mode() == True
    try:
        assert os.environ["PGZERO_MODE"] == "True"
    except KeyError:
        assert False

# Generated at 2022-06-22 13:05:42.297036
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.set_simple_mode(False)
    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:05:52.412804
# Unit test for function load_plugin
def test_load_plugin():
    from test.config_helper import get_workbench, get_runner, modname
    from test.test_runner import mock_run_with_shell
    wb = get_workbench()
    load_plugin()
    assert wb.get_option(_OPTION_NAME) is False
    with mock_run_with_shell(wb) as run:
        wb.call_command('toggle_pgzero_mode')
        assert wb.get_option(_OPTION_NAME) is True
        update_environment()
        assert os.environ["PGZERO_MODE"] == "1"
        wb.call_command('toggle_pgzero_mode')
        assert wb.get_option(_OPTION_NAME) is False
        assert os.environ["PGZERO_MODE"] == "0"
        run.assert_

# Generated at 2022-06-22 13:06:03.005375
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().get_variable(_OPTION_NAME).set(False)
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().get_variable(_OPTION_NAME).set(True)
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:08.410008
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import sentinel
    from thonny.globals import get_workbench

    wb = get_workbench()
    wb.add_variable(_OPTION_NAME, sentinel.original)
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME) is not sentinel.original
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME) is sentinel.original

# Generated at 2022-06-22 13:06:13.612131
# Unit test for function toggle_variable
def test_toggle_variable():
    # setup
    wb = get_workbench()
    assert not wb.get_variable(_OPTION_NAME)

    # execute
    toggle_variable()

    # verify
    assert wb.get_variable(_OPTION_NAME)

    # restore
    toggle_variable()
    assert not wb.get_variable(_OPTION_NAME)

# Generated at 2022-06-22 13:06:21.939165
# Unit test for function load_plugin
def test_load_plugin():
    # need to import Tk first, as thonny sometimes imports this file before Tk is read
    # (see https://bitbucket.org/plas/thonny/issues/1036/improving-handling-of-plugins)
    import tkinter
    from thonny import get_workbench, get_shell, get_runner
    from thonny.plugins.pgzero_mode import _OPTION_NAME

    wb = get_workbench()
    wb.clear_message_log()
    wb.set_default(_OPTION_NAME, False)
    # load_plugin()
    update_environment()

    get_runner().run_file("pgzero_mode_demo_1.py")

    assert os.environ["PGZERO_MODE"] == "False"
    assert get_shell().get

# Generated at 2022-06-22 13:06:30.994029
# Unit test for function load_plugin
def test_load_plugin():
    os.environ["PGZERO_MODE"] = "old"
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is True
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) is False
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:04.788576
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.misc_utils import running_on_mac_os
    if running_on_mac_os():
        # can't test on macOS, because os.environ["PGZERO_MODE"] is set by XCode
        return


# Generated at 2022-06-22 13:07:16.241852
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    from thonny.ui_utils import CommonDialog
    from unittest.mock import MagicMock
    from unittest import mock

    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = MagicMock(return_value=True)
    get_workbench().show_message = MagicMock()

    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().get_option = MagicMock(return_value=False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().in_simple_mode = lambda: True
    update_environment()

# Generated at 2022-06-22 13:07:27.903239
# Unit test for function update_environment
def test_update_environment():
    import os
    from thonny.plugins.pgzero_mode import update_environment
    from thonny import get_workbench
    from thonny.test.test_runner import TestRunner

    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, False)
    initial_env = os.environ
    non_existant = "THIS_SHOULD_NOT_EXIST_IN_THE_ENVIRONMENT"
    the_env = initial_env.copy()
    the_env[non_existant] = "This should be overwritten!!"

    try:
        os.environ[non_existant] # this should raise an error
        raise Exception("The PGZERO_MODE code appears to have a bug!")
    except KeyError:
        pass


    update_environment()


# Generated at 2022-06-22 13:07:37.995551
# Unit test for function load_plugin
def test_load_plugin():
    try:
        import pgzero
    except ImportError:
        pytest.skip("Plugin requires pgzero")
    import thonnycontrib.pgzero_mode

    # Change to this directory for testing load_plugin 
    # (which updates os.environ)
    os.chdir(os.path.dirname(thonnycontrib.pgzero_mode.__file__))
    sys.path.append(os.getcwd())
    
    wb = get_workbench()
    wb.register_editor_image("pgzero_mode.png", "pgzero_mode.png")
    thonnycontrib.pgzero_mode.load_plugin()

    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    w

# Generated at 2022-06-22 13:07:44.188413
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.unregister_command("toggle_pgzero_mode")
    load_plugin()
    assert wb.get_command("toggle_pgzero_mode")
    assert wb.get_option(_OPTION_NAME) is False
    assert "PGZERO_MODE" not in os.environ
    wb.set_simple_mode(True)
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "auto"
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE" in os.environ and os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:51.018912
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default("run.pgzero_mode", True)

    load_plugin()
    assert get_workbench().get_variable("run.pgzero_mode").get()
    assert os.environ["PGZERO_MODE"] == "True"
    assert "pgzero_mode" in [c.flag_name for c in get_workbench().get_commands("run")]

# Generated at 2022-06-22 13:07:57.796019
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    get_workbench().set_default(_OPTION_NAME, True)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == True
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:08:04.393094
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.misc_utils import running_on_mac_os

    if running_on_mac_os():
        print("Skipping plugin test (pgzero mode toggle not available on MacOS)")
        return
    _unload_plugin()

    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()

    # test that command is created
    cmd = get_workbench().get_command("toggle_pgzero_mode")
    assert isinstance(cmd, get_workbench().default_commands["toggle_pgzero_mode"])
    assert cmd.get_var_name() == _OPTION_NAME

    # test that environment variable is set

# Generated at 2022-06-22 13:08:06.477678
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_command("toggle_pgzero_mode")
    assert get_workbench().get_variable(_OPTION_NAME)

    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:08:18.041597
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest import mock
    from thonny.workbench import Workbench
    from thonny.misc_utils import (
        running_on_mac_os,
        running_on_windows,
        running_on_linux,
    )

    get_workbench = mock.MagicMock()
    get_workbench.return_value = Workbench()
    if running_on_mac_os or running_on_linux:
        os.environ["PATH"] = "/bin:/usr/bin"
        os.environ["PGZERO_MODE"] = "off"
    else:
        os.environ["PATH"] = "/bin:/usr/bin"
        os.environ["PGZERO_MODE"] = "off"

# Generated at 2022-06-22 13:08:44.111895
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, True)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True



# Generated at 2022-06-22 13:08:50.224301
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    prev_value = wb.get_option(_OPTION_NAME)
    load_plugin()
    assert wb.get_option(_OPTION_NAME)
    assert not wb.get_option(_OPTION_NAME)
    wb.set_option(_OPTION_NAME, prev_value)

# Generated at 2022-06-22 13:08:57.433254
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().has_command("toggle_pgzero_mode")
    wb = get_workbench()
    assert wb.get_option(_OPTION_NAME) == False
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    assert wb.get_option(_OPTION_NAME) == True

    get_workbench().set_simple_mode()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:09:01.842121
# Unit test for function toggle_variable
def test_toggle_variable():
    if _OPTION_NAME not in get_workbench().get_variable_names():
        get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_variable(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) is True
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) is False

# Generated at 2022-06-22 13:09:09.973558
# Unit test for function update_environment
def test_update_environment():
    from unittest import mock

    with mock.patch.dict("os.environ", clear=True):
        from thonny.plugins.pgzero_mode import update_environment

        update_environment()
        assert os.environ["PGZERO_MODE"] == str(False)
        assert "PGZERO_MODE" in os.environ

        get_workbench().set_option(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == str(True)

# Generated at 2022-06-22 13:09:19.760638
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.plugins.run.run_configuration import RunConfiguration
    from thonny.workbench import Workbench

    get_workbench().reset()
    assert not get_workbench().get_command("toggle_pgzero_mode")

    load_plugin()
    wb = get_workbench()
    assert wb.get_command("toggle_pgzero_mode")
    assert wb.get_option(_OPTION_NAME) == False

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True

    config = RunConfiguration()

    # Setting PGZERO_MODE environment variable to anything but None
    # should override the regular behaviour of the RunConfiguration.use_pgzero_mode()
    # and return True
    os.environ["PGZERO_MODE"] = "test"

# Generated at 2022-06-22 13:09:23.155800
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:09:34.513640
# Unit test for function update_environment
def test_update_environment():
    # This test requires coverage support to provide a virtual stdout
    return 
    # import sys
    # from unittest import mock

    # from thonny.common import InlineCommand, ToplevelCommand, INTERACTIVE_MODE_AVAILABLE
    # from thonny.misc_utils import running_on_mac_os
    # from thonny import get_workbench

    # from test.test_runner import RunnerTest
    # from thonny.common import PROFILE_ID, USER_DIR

    # def check_output(command, **kwargs):
    #     if command == ['coverage', 'run', '-p', '--parallel-mode']:
    #         return "write_coverage_file('.coverage.runner')"
    #     else:
    #         return subprocess.check_output

# Generated at 2022-06-22 13:09:43.076978
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop("PGZERO_MODE", None)

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()

# Generated at 2022-06-22 13:09:51.355793
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.workbench import Workbench
    from thonny.config_ui import ConfigurationPage
    import sys
    MockTk = Mock()
    MockEvent = Mock()
    sys.modules["tkinter"] = MockTk
    workbench = Workbench()
    workbench.create_variable = Mock()
    workbench.create_variable.return_value = ConfigurationPage()
    workbench.set_default = Mock()
    workbench.set_default.return_value = True
    workbench.add_command = Mock()
    workbench.add_command.return_value = True
    workbench.create_variable = Mock()
    workbench.create_variable.return_value = True
    workbench.set_default = Mock()
    workbench.set_default.return_

# Generated at 2022-06-22 13:10:56.526358
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    toggle_variable()
    assert (
        wb.get_variable(_OPTION_NAME).get()
        == wb.get_variable(_OPTION_NAME).get()
    )

# Generated at 2022-06-22 13:10:59.633652
# Unit test for function update_environment
def test_update_environment():
    print(os.environ["PGZERO_MODE"])
    toggle_variable()
    print(os.environ["PGZERO_MODE"])
    toggle_variable()
    print(os.environ["PGZERO_MODE"])


# Generated at 2022-06-22 13:11:06.753301
# Unit test for function update_environment
def test_update_environment():
    try:
        del os.environ["PGZERO_MODE"]
    except:
        pass

    os.environ["THONNY_SIMPLE_MODE"] = "1"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    del os.environ["THONNY_SIMPLE_MODE"]

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:11:13.681741
# Unit test for function toggle_variable
def test_toggle_variable():
    import os
    from thonny.globals import get_workbench
    from thonny import ui_utils
    get_workbench().set_default(_OPTION_NAME, True)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:11:17.700652
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False


# Generated at 2022-06-22 13:11:18.768311
# Unit test for function load_plugin
def test_load_plugin():
    # TODO: testing
    pass

# Generated at 2022-06-22 13:11:29.009172
# Unit test for function update_environment
def test_update_environment():
    my_workbench = get_workbench()
    my_plugin = load_plugin()
    my_workbench.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    my_workbench.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    my_workbench.set_option(_OPTION_NAME, True)
    my_workbench.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:11:39.731056
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench, get_runner
    from thonny.ui_utils import askyesno

    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, False)
    workbench.insert_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )

    # Case 1:
    # Run the program with pgzero mode = False
    # Output should be "Program output"
    workbench.set_default(_OPTION_NAME, False)

# Generated at 2022-06-22 13:11:47.501854
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    from thonny.workbench import Workbench
    from unittest.mock import patch

    workbench = Workbench(None)
    workbench.set_default("run.pgzero_mode", False)
    with patch("thonny.workbench.get_workbench", return_value=workbench):
        update_environment()

    assert os.environ["PGZERO_MODE"] == "False"

    workbench.set_option("run.pgzero_mode", True)
    with patch("thonny.workbench.get_workbench", return_value=workbench):
        update_environment()

    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:11:50.483381
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    # Load twice to make sure that it can handle multiple calls
    load_plugin()
    get_workbench().event_generate("ThemeChanged")

if __name__ == "__main__":
    # run test
    test_load_plugin()