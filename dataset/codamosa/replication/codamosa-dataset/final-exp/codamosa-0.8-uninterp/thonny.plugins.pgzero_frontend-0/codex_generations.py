

# Generated at 2022-06-22 13:02:32.035371
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)



# Generated at 2022-06-22 13:02:41.273737
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.misc_utils import running_on_mac_os

    wb = get_workbench()
    try:
        wb.set_default(_OPTION_NAME, True)
        wb.add_command(
            "toggle_pgzero_mode",
            "run",
            tr("Pygame Zero mode"),
            toggle_variable,
            flag_name=_OPTION_NAME,
            group=40,
        )
        if not running_on_mac_os():
            assert os.environ["PGZERO_MODE"] == "True"
    finally:
        wb.remove_command("toggle_pgzero_mode")
        wb.remove_option(_OPTION_NAME)
        if not running_on_mac_os():
            assert "PGZERO_MODE" not in os.environ

# Generated at 2022-06-22 13:02:50.651972
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny import get_workbench
    from thonny.workbench import Workbench
    from thonny.languages import tr
    from thonny.globals import get_workbench
    from thonny.globals import get_shell
    workbench = Workbench()
    workbench.set_default(_OPTION_NAME, False)
    workbench.add_command(
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

# Generated at 2022-06-22 13:03:00.417891
# Unit test for function update_environment
def test_update_environment():
    # Monkey patching
    import thonny.globals
    from thonny.globals import get_workbench

    thonny.globals.get_workbench = lambda: MockWorkbench(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    thonny.globals.get_workbench = lambda: MockWorkbench(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Unpatching
    thonny.globals.get_workbench = get_workbench


# Generated at 2022-06-22 13:03:12.146801
# Unit test for function update_environment
def test_update_environment():
    from thonny.config_ui import set_workbench_option
    from thonny.misc_utils import running_on_mac_os, running_on_windows
    from thonny.plugins.run.run_command import update_environment as run_update_environment
    import os
    import sys

    # Save original values
    old_env = os.environ.copy()
    old_mode = get_workbench().in_simple_mode()
    old_pgzero = get_workbench().get_option(_OPTION_NAME)

    def restore_original_values():
        get_workbench().set_simple_mode(old_mode)
        set_workbench_option(_OPTION_NAME, old_pgzero)
        os.environ = old_env


# Generated at 2022-06-22 13:03:18.816477
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:25.119850
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = ""
    workbench = get_workbench()
    workbench.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    workbench.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:03:28.659949
# Unit test for function load_plugin
def test_load_plugin():
    global my_workbench
    from thonny import Thonny
    my_workbench = Thonny(user_dir=None, work_dir=None, options_props={})
    load_plugin()

# Generated at 2022-06-22 13:03:34.206050
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench

    workbench = Workbench()
    try:
        workbench.set_global_option(_OPTION_NAME, True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "1"
    finally:
        del os.environ["PGZERO_MODE"]
        workbench.destroy()

# Generated at 2022-06-22 13:03:37.502460
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:03:53.236047
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, True)
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().get_configuration()["simple_mode"] = {"active": True}
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().get_configuration()["simple_mode"] = {"active": False}
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:03:59.076729
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    assert os.getenv("PGZERO_MODE") == "0"
    toggle_variable()
    assert os.getenv("PGZERO_MODE") == "1"
    toggle_variable()
    assert os.getenv("PGZERO_MODE") == "0"
    

# Generated at 2022-06-22 13:04:08.527291
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_simple_mode(False)
    get_workbench().set_default(_OPTION_NAME, False)
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"

    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_simple_mode(True)

    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:04:11.412804
# Unit test for function update_environment
def test_update_environment():
    get_workbench()
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:16.401612
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    u = update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_option(_OPTION_NAME, True)
    u = update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:21.741118
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:04:31.344408
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:39.282032
# Unit test for function update_environment
def test_update_environment():
    from thonny.globals import get_workbench
    from thonny.ui_utils import get_font
    from thonny.config import get_default_font, get_user_font

    # change workbench settings to trigger calling update_environment
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_default(_OPTION_NAME, True)

    # check if environment variable is set
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:48.726478
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert "PGZERO_MODE" in os.environ
    assert os.environ["PGZERO_MODE"] == "True"

    orig_mode = get_workbench().in_simple_mode()

# Generated at 2022-06-22 13:04:56.997271
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    
    wb.set_simple_mode(False)
    wb.set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:05:20.627887
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock

    get_workbench = Mock()
    get_workbench.get_option.return_value = True
    get_workbench.in_simple_mode.return_vale = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench.get_option.return_value = False
    get_workbench.in_simple_mode.return_vale = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench.get_option.return_value = False
    get_workbench.in_simple_mode.return_vale = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:05:31.382024
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == True

    wb.set_default(_OPTION_NAME, False)
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == False

    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == str(wb.get_option(_OPTION_NAME))

    wb.set_default(_OPTION_NAME, False)
    load_plugin()
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:05:35.914981
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_in_simple_mode(False)
    wb.set_option(_OPTION_NAME, True)
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:05:43.096788
# Unit test for function toggle_variable
def test_toggle_variable():
    # Assume that the default value is False
    pb = get_workbench()
    assert pb.get_variable(_OPTION_NAME).get() is False
    # Trigger the menu command
    toggle_variable()
    # Check that the variable is now True
    assert pb.get_variable(_OPTION_NAME).get() is True
    # Trigger the menu command again
    toggle_variable()
    # Check that the variable is now False again
    assert pb.get_variable(_OPTION_NAME).get() is False

# Generated at 2022-06-22 13:05:52.519439
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    wb = Workbench()
    wb.set_simple_mode(False)
    wb.set_option("run.pgzero_mode", False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_option("run.pgzero_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:00.610067
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().get_option(_OPTION_NAME).set(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"
    get_workbench().get_option(_OPTION_NAME).set(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

# Generated at 2022-06-22 13:06:10.251167
# Unit test for function load_plugin
def test_load_plugin():
    import unittest.mock as mock
    from thonny.plugins.pgzeromode import load_plugin
    from thonny import get_workbench

    wb = get_workbench()

    def mock_get_workbench():
        return wb

    with mock.patch("thonny.plugins.pgzeromode.get_workbench", mock_get_workbench):
        load_plugin()

    # Test if the command is added to the workbench
    assert wb.get_command("toggle_pgzero_mode") is not None

    # Test if the command has the correct group
    assert (
        wb.get_command("toggle_pgzero_mode")["group"] == 40
    )

    # Test if the command has the correct flag_name

# Generated at 2022-06-22 13:06:17.224592
# Unit test for function toggle_variable
def test_toggle_variable():
    # Fill variables as they are in wb after load
    wb = get_workbench()
    wb._variables[_OPTION_NAME] = True

    # Set expected results after call
    expected_dict = {"PGZERO_MODE": "False"}

    # Call function
    toggle_variable()

    # Check result
    assert wb._variables[_OPTION_NAME] == False
    assert os.environ["PGZERO_MODE"] == expected_dict["PGZERO_MODE"]



# Generated at 2022-06-22 13:06:23.373576
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
    var = get_workbench().get_variable(_OPTION_NAME)
    assert var.get() is False
    assert os.environ["PGZERO_MODE"] == "False"

    var.set(True)
    update_environment()
    assert var.get() is True
    assert os.environ["PGZERO_MODE"] == "True"

    wb.in_simple_mode = True
    update_environment()
    assert os

# Generated at 2022-06-22 13:06:27.406179
# Unit test for function load_plugin
def test_load_plugin():
    wb = WorkbenchMockup()
    load_plugin()
    assert "toggle_pgzero_mode" in wb.commands


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:06:58.919294
# Unit test for function load_plugin
def test_load_plugin():
    # Test whether plugin loads without error
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

# Generated at 2022-06-22 13:07:07.651608
# Unit test for function update_environment
def test_update_environment():
    # noinspection PyTypeChecker
    get_workbench().in_simple_mode = lambda: False
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # noinspection PyTypeChecker
    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:16.338350
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench

    get_workbench().set_default(_OPTION_NAME, False)
    Workbench.simple_mode = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    Workbench.simple_mode = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:07:21.796925
# Unit test for function toggle_variable
def test_toggle_variable():

    if get_workbench().get_variable(_OPTION_NAME).get():
        toggle_variable()

    assert (os.getenv("PGZERO_MODE") == "False")

    toggle_variable()

    assert (os.getenv("PGZERO_MODE") == "True")

# Generated at 2022-06-22 13:07:30.709898
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench

    workbench.unload_plugin("thonnycontrib.pgzero_mode")
    print(workbench.get_variable(_OPTION_NAME, None))
    assert workbench.get_variable(_OPTION_NAME, None) is None

    load_plugin()

    print(workbench.get_variable(_OPTION_NAME, None))
    assert workbench.get_variable(_OPTION_NAME, None) is False

    workbench.unload_plugin("thonnycontrib.pgzero_mode")
    print(workbench.get_variable(_OPTION_NAME, None))
    assert workbench.get_variable(_OPTION_NAME, None) is None

# Generated at 2022-06-22 13:07:37.461465
# Unit test for function update_environment
def test_update_environment():
    from thonny.workbench import Workbench
    from unittest.mock import MagicMock
    from thonny import get_workbench
    get_workbench = MagicMock(return_value = MagicMock(in_simple_mode=lambda:False, get_option=lambda x: True))
    load_plugin()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:42.212120
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME)
    assert get_workbench().get_option(_OPTION_NAME)


if __name__ == "__main__":
    load_plugin()

# Generated at 2022-06-22 13:07:49.629576
# Unit test for function update_environment
def test_update_environment():
    if "PGZERO_MODE" in os.environ:
        del os.environ["PGZERO_MODE"]
    
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    
    # TODO: test simple mode

# Generated at 2022-06-22 13:07:59.286656
# Unit test for function update_environment
def test_update_environment():
    import os, tempfile
    from thonny.config_ui import ConfigurationPage
    from thonny.workbench import Workbench
    from thonny.globals import get_workbench, is_running_on_raspberry_pi, set_workbench

    assert get_workbench() is not None
    original_value = get_workbench().get_option("run.pgzero_mode")

    with tempfile.TemporaryDirectory() as tempdir:
        tb = Workbench(tempdir, bypass_editor=True)
        set_workbench(tb)
        assert get_workbench() == tb

        get_workbench().set_option("run.pgzero_mode", True)
        update_environment()
        assert os.environ["PGZERO_MODE"] == "True"

        get_workbench().set

# Generated at 2022-06-22 13:08:07.889166
# Unit test for function update_environment
def test_update_environment():

    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:09:05.869145
# Unit test for function update_environment
def test_update_environment():
    dummy_workbench = SimpleNamespace(
        in_simple_mode=lambda: True, get_option=lambda option_name: False
    )

    def mock_setdefault(option_name, value):
        pass

    dummy_workbench.set_default = mock_setdefault

    def mock_get_variable(option_name):
        var = SimpleNamespace(get=lambda: value)

        def mock_set(value):
            pass

        var.set = mock_set
        return var

    dummy_workbench.get_variable = mock_get_variable
    dummy_workbench.get_variable(_OPTION_NAME).get = lambda: True
    get_workbench.cache_clear()

    with patch("thonny.plugins.pgzero.get_workbench", lambda: dummy_workbench):
        update_environment()

# Generated at 2022-06-22 13:09:16.886204
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock

    mock_wb = Mock()
    mock_wb.get_variable = lambda name: getattr(mock_wb, name)
    mock_wb.get_option = lambda name: getattr(mock_wb, name)
    mock_wb.in_simple_mode = lambda: False
    mock_wb.add_command = lambda name, command_name, label, command, flag_name, group: None
    mock_wb.set_default = lambda name, value: setattr(mock_wb, name, value)
    mock_wb.run_pgzero_mode = False
    mock_wb.run_pgzero_mode_changed_event = Mock()

    load_plugin()
    assert "PGZERO_MODE" not in os.environ

    mock_wb.in_simple_

# Generated at 2022-06-22 13:09:26.957278
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock

    get_workbench = Mock()
    set_default = Mock()
    add_command = Mock()
    get_workbench.return_value.set_default = set_default
    get_workbench.return_value.add_command = add_command
    global _OPTION_NAME

    _OPTION_NAME = "test_option"
    load_plugin()

    get_workbench.assert_called_once()
    set_default.assert_called_once()
    add_command.assert_called_once()
    set_default.assert_called_with(_OPTION_NAME, False)

# Generated at 2022-06-22 13:09:37.964493
# Unit test for function update_environment
def test_update_environment():
    from thonny.globals import get_workbench, set_workbench
    from unittest.mock import MagicMock
    from unittest import TestCase
    from thonny.globals import get_workbench, set_workbench

    class Tester(TestCase):
        def setUp(self):
            set_workbench(MagicMock())
            get_workbench().in_simple_mode = MagicMock()
            get_workbench().get_option = MagicMock()

        def test_enabled(self):
            get_workbench().in_simple_mode.return_value = False
            get_workbench().get_option.return_value = True
            update_environment()
            self.assertEqual(os.environ["PGZERO_MODE"], "True")


# Generated at 2022-06-22 13:09:49.309575
# Unit test for function update_environment
def test_update_environment():
    from unittest import TestCase
    from unittest.mock import Mock
    from thonny.workbench import Workbench
    from thonny.config import Configuration

    class TestCase(TestCase):
        def setUp(self):
            self.workbench = Workbench()
            self.workbench.in_simple_mode = Mock(return_value=False)
            self.workbench.get_option = Mock(return_value=False)

        def test_update_environment(self):
            self.assertEqual(False, os.environ.get("PGZERO_MODE"))
            update_environment()
            self.assertEqual("0", os.environ.get("PGZERO_MODE"))
            self.workbench.get_option.return_value = True
            update_environment()
            self.assertE

# Generated at 2022-06-22 13:09:52.700478
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:00.782770
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_default(_OPTION_NAME, True)
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:10:09.416009
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import Mock
    import os

    wb = Mock()
    wb.get_variable = lambda x: Mock(get=lambda: True)
    wb.in_simple_mode = lambda: False
    wb.get_option = lambda x: True

    os.environ["PGZERO_MODE"] = "some value"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    wb.in_simple_mode.return_value = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:10:13.179184
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:10:18.062383
# Unit test for function update_environment
def test_update_environment():
    get_workbench().in_simple_mode = lambda: False
    get_workbench().get_option = lambda name: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().get_option = lambda name: False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().in_simple_mode = lambda: True
    get_workbench().get_option = lambda name: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"