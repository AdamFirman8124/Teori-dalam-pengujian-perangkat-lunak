

# Generated at 2022-06-22 13:02:41.818084
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    os.environ["PGZERO_MODE"] = "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:02:44.767236
# Unit test for function update_environment
def test_update_environment():
    var = get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:02:51.253130
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ.get("PGZERO_MODE") == "False"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ.get("PGZERO_MODE") == "True"
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ.get("PGZERO_MODE") == "False"

# Generated at 2022-06-22 13:02:57.091016
# Unit test for function update_environment
def test_update_environment():
    import thonny
    import os

    env = os.environ
    if "PGZERO_MODE" in env:
        del env["PGZERO_MODE"]

    thonny._get_workbench_instance = lambda: None
    thonny._get_workbench_instance().get_option = lambda x: True
    thonny._get_workbench_instance().in_simple_mode = lambda: None
    update_environment()
    assert env["PGZERO_MODE"] == "True"

    thonny._get_workbench_instance().in_simple_mode = lambda: True
    update_environment()
    assert env["PGZERO_MODE"] == "auto"

load_plugin()

# Generated at 2022-06-22 13:03:05.988505
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_variable(_OPTION_NAME).get()==False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get()==True
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get()==False
    assert os.environ["PGZERO_MODE"] == "False"
    load_plugin()

# Generated at 2022-06-22 13:03:13.638819
# Unit test for function update_environment
def test_update_environment():
    """ test update_environment """
    os.environ["PGZERO_MODE"] = ""
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().in_simple_mode = lambda: False


# Generated at 2022-06-22 13:03:20.731820
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = ""
    assert os.environ["PGZERO_MODE"] == ""
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    os.environ["PGZERO_MODE"] = ""
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:28.132640
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    assert wb.get_default(_OPTION_NAME) == True
    assert wb.get_option(_OPTION_NAME) == True

    # running toggle_variable should give us False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:37.878029
# Unit test for function update_environment
def test_update_environment():
    env = {}
    os.environ = env
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert env["PGZERO_MODE"] == "True"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert env["PGZERO_MODE"] == "False"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert env["PGZERO_MODE"] == "auto"
    get_workbench().in_simple_mode = lambda: False
    update_environment()
    assert env["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:46.608234
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_option(_OPTION_NAME, "auto")
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.set_option(_OPTION_NAME, "auto")
    wb.enter_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.leave_simple_mode()
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:54.755502
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:04:06.354191
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.globals import get_workbench
    from thonny import ui_utils
    from unittest.mock import Mock
    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, True)
    workbench.add_statusbar_cascade("testcommand", _("testcommand"), "testcommand", "test_command")
    ui_utils.create_menu_item = Mock()

    toggle_variable()
    assert workbench.get_option(_OPTION_NAME) is False
    toggle_variable()
    assert workbench.get_option(_OPTION_NAME) is True

    assert ui_utils.create_menu_item.call_count == 2

# Generated at 2022-06-22 13:04:09.647990
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    load_plugin()
    assert wb.get_option(_OPTION_NAME) is False
    assert wb.get_variable(_OPTION_NAME).get() is False



# Generated at 2022-06-22 13:04:20.887200
# Unit test for function toggle_variable
def test_toggle_variable():
    update_environment()
    get_workbench().add_variable(_OPTION_NAME, True)
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_in_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    # now test under Tk
    from tkinter import Tk
    from thonny.ui_utils import get_simplified_icon_path
    from thonny.globals import get_workbench

    root = Tk()
    get_workbench().set_top(root)

# Generated at 2022-06-22 13:04:23.303762
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench

    assert get_workbench().get_option(_OPTION_NAME) is False

# Generated at 2022-06-22 13:04:28.547122
# Unit test for function update_environment
def test_update_environment():
    w = get_workbench()
    w.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    w.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:38.741083
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny.globals import get_workbench

    wb_mock = Mock(name="Workbench")
    wb_mock.in_simple_mode = Mock(name="in_simple_mode")
    wb_mock.in_simple_mode = Mock(return_value=False)

    # Set up workbench
    setattr(get_workbench(), "_instance", wb_mock)

    # Set up test
    import os

    os.environ["PGZERO_MODE"] = None

    load_plugin()
    wb_mock.set_default.assert_called_with(_OPTION_NAME, False)

# Generated at 2022-06-22 13:04:41.557528
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    wb.set_default(_OPTION_NAME, False)
    update_environment()

# Generated at 2022-06-22 13:04:52.600969
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    assert wb.in_simple_mode()
    assert wb.get_option("run.pgzero_mode") is False
    assert "PGZERO_MODE" not in os.environ

    # Enable mode and check settings
    toggle_variable()
    assert not wb.in_simple_mode()
    assert wb.get_option("run.pgzero_mode") is True
    assert os.environ["PGZERO_MODE"] == "True"

    # Disable mode and check settings
    toggle_variable()
    assert not wb.in_simple_mode()
    assert wb.get_option("run.pgzero_mode") is False
    assert os.environ["PGZERO_MODE"] == "False"

    # Switch to simple mode and check settings

# Generated at 2022-06-22 13:04:57.642973
# Unit test for function update_environment
def test_update_environment():
    get_workbench().update_variable(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().update_variable(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:05:08.792352
# Unit test for function load_plugin
def test_load_plugin():
    # Removes exit button
    get_workbench().set_default("view.show_exit_button", False)
    # Loads plugin
    load_plugin()
    # Checks if the plugin is loaded
    assert "toggle_pgzero_mode" in get_workbench().get_editor_notebook().get_page_menu()._menu.keys()
    # Unloads plugin
    reset_plugin()



# Generated at 2022-06-22 13:05:14.447076
# Unit test for function load_plugin
def test_load_plugin():
    # The function can only be tested when the workbench
    # is running, so the test will be done with the
    # main script.
    from thonny import workbench

    workbench.set_default(_OPTION_NAME, True)
    load_plugin()
    assert workbench.get_option(_OPTION_NAME) is True

# Generated at 2022-06-22 13:05:24.453305
# Unit test for function update_environment
def test_update_environment():
    from thonny.misc_utils import get_virtualenv_python_exe

    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda *args, **kwargs: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda *args, **kwargs: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().in_simple_mode = lambda: True
    get_work

# Generated at 2022-06-22 13:05:34.408199
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock

    get_workbench = Mock(return_value=Mock(in_simple_mode=Mock(return_value=False), get_option=Mock(return_value=False)))
    import sys

    sys.modules["thonny"] = Mock(get_workbench=get_workbench)
    import thonnycontrib.pgzero

    thonnycontrib.pgzero.update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Unit test for function toggle_variable
    def test_toggle_variable():
        from unittest.mock import Mock

        get_workbench = Mock(return_value=Mock(get_variable=Mock(return_value=Mock(get=Mock(return_value=False)))))
       

# Generated at 2022-06-22 13:05:40.573616
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


# Generated at 2022-06-22 13:05:47.398287
# Unit test for function load_plugin
def test_load_plugin():
    test_workbench = Workbench()
    test_load_plugin.wb = test_workbench
    test_load_plugin.wb.set_default(_OPTION_NAME, False)
    test_load_plugin.wb.add_command(
        "toggle_pgzero_mode",
        "run",
        tr("Pygame Zero mode"),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=40,
    )
    update_environment()



# Generated at 2022-06-22 13:05:48.925732
# Unit test for function load_plugin
def test_load_plugin():
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:06:00.325266
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
    assert os.environ.get("PGZERO_MODE", None) is None
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) is True
    assert os.environ.get("PGZERO_MODE", None) == "True"
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) is False

# Generated at 2022-06-22 13:06:06.489118
# Unit test for function toggle_variable
def test_toggle_variable():
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:12.207374
# Unit test for function update_environment
def test_update_environment():
    os.environ.pop("PGZERO_MODE", None)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:20.723242
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_option(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:06:22.414759
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:06:32.321573
# Unit test for function load_plugin
def test_load_plugin():
    import unittest
    import unittest.mock

    mb_patcher = unittest.mock.patch("thonny.workbench.Workbench")
    mb_patcher.start()
    wb = get_workbench()

    m_patcher = unittest.mock.patch("thonny.run.pgzero_mode._OPTION_NAME", new="pgz.mode")
    m_patcher.start()
    load_plugin()

    assert wb.get_variable("pgz.mode") == False
    assert wb.get_option("pgz.mode") == False
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple_mode(True)
    update_environment()

# Generated at 2022-06-22 13:06:40.122328
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

# Generated at 2022-06-22 13:06:40.647893
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()

# Generated at 2022-06-22 13:06:44.125558
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()

    # case1:
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == True

    # case 2:
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == False

# Generated at 2022-06-22 13:06:46.981084
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:06:49.641738
# Unit test for function toggle_variable
def test_toggle_variable():
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:06:53.796244
# Unit test for function load_plugin
def test_load_plugin():
    """Without mocking, I was getting two "Toggle Pygame Zero mode" buttons
    when running pytest on thonnycontrib.pgzero_mode.
    It is caused by "auto" value of PGZERO_MODE env variable, which is
    used to detect whether the plugin has been loaded."""
    from unittest.mock import patch
    from thonny.workbench import Workbench

    with patch("os.environ.get") as mock_method:
        mock_method.return_value = None
        wb = Workbench()

        load_plugin()
        assert wb.get_variable(_OPTION_NAME) == False
        assert wb.get_default(_OPTION_NAME) == False
        assert mock_method.call_count == 2

        toggle_variable()

# Generated at 2022-06-22 13:06:55.511322
# Unit test for function toggle_variable
def test_toggle_variable():
    os.environ["PGZERO_MODE"] = "auto"
    load_plugin()
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:07:12.124333
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_option(_OPTION_NAME, False)
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_simple_mode(False)
    assert os.environ["PGZERO_MODE"] == "auto"


# Unit tests for function toggle_variable

# Generated at 2022-06-22 13:07:23.945175
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench

    w = Workbench()
    w.set_default(_OPTION_NAME, True)
    assert get_workbench().get_variable(_OPTION_NAME).get()

    toggle_variable()

    assert not get_workbench().get_variable(_OPTION_NAME).get()

    toggle_variable()

    assert get_workbench().get_variable(_OPTION_NAME).get()


if __name__ == "__main__":
    import sys
    from thonny.workbench import Workbench

    w = Workbench()
    w.set_default(_OPTION_NAME, True)
    assert get_workbench().get_variable(_OPTION_NAME).get()

    toggle_variable()

    assert not get_workbench().get_variable(_OPTION_NAME).get()



# Generated at 2022-06-22 13:07:27.757966
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False
    wb = get_workbench()
    assert wb.in_simple_mode() == True
    os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:37.915235
# Unit test for function update_environment
def test_update_environment():
    import os
    from thonny.plugins.pgzero_mode import update_environment, toggle_variable
    from thonny import get_workbench
    
    # Check if the environment variable is set
    if os.environ.get("PGZERO_MODE") == None:
        assert False

    # Ensure that the variable is set properly
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test that the toggle_variable function works
    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:07:42.478506
# Unit test for function update_environment
def test_update_environment():
    import os

    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda x: "foo bar"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "foo bar"
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    assert list(get_workbench().commands[40]) == ["toggle_pgzero_mode"]

# Generated at 2022-06-22 13:07:54.400322
# Unit test for function update_environment
def test_update_environment():
    from thonny.codeview import CodeViewText
    from unittest.mock import MagicMock, patch

    text = CodeViewText(None)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "off"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "on"

    with patch("thonny.plugins.pgzero_mode.get_workbench") as mock_get_workbench:
        mock_get_workbench.return_value = MagicMock()
        mock_get_workbench.return_value.in_simple_mode.return_value = True
        update_environment()
       

# Generated at 2022-06-22 13:08:02.068199
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_simple_mode(True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "auto"
    assert wb.in_simple_mode()
    assert not wb.get_option(_OPTION_NAME)
    wb.set_simple_mode(False)
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    assert wb.get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:08:13.306849
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.misc_utils import running_on_mac_os, running_on_windows
    from thonny.globals import get_workbench
    from thonny.ui_utils import get_default_font
    from tkinter import TOP, BOTH, X, GROOVE
    from thonny.languages import tr
    from thonny.plugins.pgzero_mode import load_plugin

    # Setup
    test_wb = get_workbench()
    test_wb.set_default(_OPTION_NAME, False)
    load_plugin()

    # Test
    commands = test_wb.get_commands()

# Generated at 2022-06-22 13:08:19.537701
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    
    os.environ.pop('PGZERO_MODE', None)
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'False'
    
    os.environ.pop('PGZERO_MODE', None)
    wb.set_option('run.pgzero_mode', True)
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'True'
    
    os.environ['PGZERO_MODE'] = 'auto'
    wb.set_option('run.pgzero_mode', False)
    update_environment()
    assert os.environ['PGZERO_MODE'] == 'False'
    

# Generated at 2022-06-22 13:08:29.609162
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import MagicMock
    from thonny import get_workbench, Workbench
    from thonny.languages import tr
    from thonny.plugins.pgzero_mode import load_plugin, toggle_variable

    get_workbench.reset_mock()
    get_workbench.return_value = MagicMock(spec=Workbench)

    # Function load_plugin
    load_plugin()

    get_workbench.return_value.set_default.assert_called_with(
        "run.pgzero_mode", False
    )

# Generated at 2022-06-22 13:08:54.780000
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

# Generated at 2022-06-22 13:08:58.372899
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    assert wb
    # var is False
    assert wb.get_variable(_OPTION_NAME).get()==False
    # toggle var
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get()==True
    # toggle var again
    toggle_variable()
    assert wb.get_varia

# Generated at 2022-06-22 13:09:02.162193
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench, get_runner
    get_workbench().unload_plugin("thonny.plugins.pgzero")
    import thonny.plugins.pgzero
    get_workbench().load_plugin("thonny.plugins.pgzero")
    import thonny.plugins.pgzero
    assert get_workbench().get_variable(_OPTION_NAME).get() == False
    toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME).get() == True


# Generated at 2022-06-22 13:09:11.561942
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    try:
        get_workbench().set_simple_mode(True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "auto"

        get_workbench().set_simple_mode(False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "False"
        get_workbench().set_option(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"
    finally:
        os.environ["PGZERO_MODE"] = "auto"

# Generated at 2022-06-22 13:09:15.993627
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:09:26.342398
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    original_var = os.environ.get("PGZERO_MODE")
    original_default_value = wb.get_default(_OPTION_NAME)

# Generated at 2022-06-22 13:09:34.904078
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

# Generated at 2022-06-22 13:09:37.118210
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    assert wb.get_command("toggle_pgzero_mode")


# Generated at 2022-06-22 13:09:45.661224
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import create_autospec
    from thonny import get_workbench
    from thonny.tkgui import TkGUI
    from thonny.running import parse_environment
    from thonny.languages import tr

    # Mock the Tkinter GUI
    mock_tk = create_autospec(Tk)
    workbench = TkGUI(mock_tk)
    workbench.set_default(_OPTION_NAME, False)

    # Call load_plugin
    load_plugin()

    # Test that the command was added to the workbench
    assert workbench.execute_command("toggle_pgzero_mode") == None

    # Test that the correct option was added
    assert workbench.get_option(_OPTION_NAME) == False

    # Test that the values are parsed by the command

# Generated at 2022-06-22 13:09:55.944160
# Unit test for function toggle_variable
def test_toggle_variable():
    os.environ["PGZERO_MODE"] = ""
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().in_simple_mode = lambda: True
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"
	
if __name__ == "__main__":
    from thonny.plugins.pgzero_mode import pgzero_mode as m
    m.load_plugin()

# Generated at 2022-06-22 13:10:59.326429
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench

    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, True)
    print(workbench.get_option(_OPTION_NAME))
    toggle_variable()
    assert not workbench.get_option(_OPTION_NAME)

    toggle_variable()
    assert workbench.get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:11:02.004330
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, True)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:11:08.753552
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_option(_OPTION_NAME) == False

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False

    wb.set_default(_OPTION_NAME, True)
    assert wb.get_option(_OPTION_NAME) == True

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:11:19.562282
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.workbench import Workbench
    import tempfile as tm
    import os

    os.environ["PGZERO_MODE"] = "auto"

    wb = Workbench()
    wb.set_default(_OPTION_NAME, False)
    wb.add_command("toggle_pgzero_mode", "run", tr("Pygame Zero mode"), toggle_variable)
    wb.initialize("Testing", [])

    assert "PGZERO_MODE" in os.environ

    f = tm.NamedTemporaryFile("w", delete=False)

# Generated at 2022-06-22 13:11:29.279116
# Unit test for function update_environment
def test_update_environment():
    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, False)
    workbench.set_simple_mode(False)
    update_environment()
    assert os.environ.get("PGZERO_MODE", None) == "False"
    workbench.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ.get("PGZERO_MODE", None) == "True"
    workbench.set_simple_mode(True)
    update_environment()
    assert os.environ.get("PGZERO_MODE", None) == "auto"

# Generated at 2022-06-22 13:11:34.497648
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    load_plugin()
    assert wb.in_simple_mode() == False
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:11:46.437772
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest.mock import Mock
    from thonny import ui_utils
    from thonny.common import ToplevelCommand
    from thonny.languages import get_language
    import thonny.plugins.run
    import thonny.plugins.trace

    wb = Mock()
    wb.in_simple_mode = Mock(return_value=False)

    # Mock the Checkbutton so it doesn't create any UI
    wb.create_variable = Mock(return_value=Mock(get=Mock(return_value=True), set=Mock()))
    ui_utils.Checkbutton = Mock(side_effect=None)

    # Mock the ToplevelCommand so it doesn't create any UI
    ui_utils.create_toplevel = Mock(return_value=Mock())



# Generated at 2022-06-22 13:11:49.545559
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_option(_OPTION_NAME) == False
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:11:59.621171
# Unit test for function update_environment
def test_update_environment():
    old_PGZERO_MODE = os.environ.get("PGZERO_MODE", None)
    try:
        get_workbench().set_option(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "1"
        get_workbench().set_option(_OPTION_NAME, False)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "0"
    finally:
        if old_PGZERO_MODE is None:
            del os.environ["PGZERO_MODE"]
        else:
            os.environ["PGZERO_MODE"] = old_PGZERO_MODE

# Generated at 2022-06-22 13:12:00.402522
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    toggle_variable()