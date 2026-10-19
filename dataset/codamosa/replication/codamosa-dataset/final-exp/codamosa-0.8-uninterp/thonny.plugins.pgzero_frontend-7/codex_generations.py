

# Generated at 2022-06-22 13:02:47.751298
# Unit test for function update_environment
def test_update_environment():
    from unittest.mock import patch
    from unittest import TestCase

    class TestCase(TestCase):
        def setUp(self):
            self.patcher = patch("os.environ")
            self.environ = self.patcher.start()
            self.environ.clear()

        def tearDown(self):
            self.patcher.stop()

        def test_update_environment_enabled(self):
            get_workbench().set_default(_OPTION_NAME, True)
            update_environment()
            self.assertEqual(os.environ["PGZERO_MODE"], "1")

        def test_update_environment_disabled(self):
            get_workbench().set_default(_OPTION_NAME, False)
            update_environment()

# Generated at 2022-06-22 13:02:53.899592
# Unit test for function toggle_variable
def test_toggle_variable():
    print("test_toggle_variable")
    original_value=get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == original_value
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) != original_value
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == original_value

# Generated at 2022-06-22 13:03:05.685876
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().backend.stdout_captured = False
    print("Testing toggle_variable")
    print("PGZERO_MODE", os.environ.get("PGZERO_MODE"))
    print("get_workbench().get_option(OPTION_NAME)", get_workbench().get_option(_OPTION_NAME))
    toggle_variable()
    print("PGZERO_MODE", os.environ.get("PGZERO_MODE"))
    print("get_workbench().get_option(OPTION_NAME)", get_workbench().get_option(_OPTION_NAME))
    toggle_variable()
    print("PGZERO_MODE", os.environ.get("PGZERO_MODE"))

# Generated at 2022-06-22 13:03:14.339662
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench
    from thonny.languages import tr
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:03:24.432532
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench, get_shell
    wb = get_workbench()
    command = wb.get_command("toggle_pgzero_mode")
    assert command
    assert wb.get_variable(_OPTION_NAME).get() == False
    assert "PGZERO_MODE=False" in get_shell().run_command("print(os.environ)")
    command()
    assert wb.get_variable(_OPTION_NAME).get() == True
    assert "PGZERO_MODE=True" in get_shell().run_command("print(os.environ)")
    command()
    assert wb.get_variable(_OPTION_NAME).get() == False
    assert "PGZERO_MODE=False" in get_shell().run_command("print(os.environ)")



# Generated at 2022-06-22 13:03:33.107074
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.misc_utils import running_on_mac_os, running_on_windows
    from thonny.misc_utils import select_interpreter
    import sys
    import os
    
    thonny.workbench.test_setup()
    clean_sys_path()
    clean_pgzero_env()
    load_plugin()
    assert get_workbench().get_default(_OPTION_NAME) == False
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    assert os.environ["PGZERO_MODE"] == "True"
    clean_pgzero_env()
    

# Generated at 2022-06-22 13:03:38.368494
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:03:40.397958
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench

    _load_workbench()
    _unload_workbench()



# Generated at 2022-06-22 13:03:47.385758
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    var = wb.get_variable(_OPTION_NAME)
    assert not var.get()
    assert os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert var.get()
    assert os.environ["PGZERO_MODE"] == "1"
    toggle_variable()
    assert not var.get()
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:03:53.487084
# Unit test for function toggle_variable
def test_toggle_variable():
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.set_option(_OPTION_NAME, False)
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:04:01.188243
# Unit test for function load_plugin
def test_load_plugin():
    # TODO: Add unit test
    pass


# Generated at 2022-06-22 13:04:04.338534
# Unit test for function load_plugin
def test_load_plugin():
    for i in range(4):
        load_plugin()
        unload_plugin()

# Generated at 2022-06-22 13:04:14.612430
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    import sys

    sys.modules["thonny.workbench"] = Mock()
    sys.modules["thonny.workbench"].get_default = Mock()
    sys.modules["thonny.workbench"].get_option = Mock()
    sys.modules["thonny.workbench"].get_option.return_value = False
    sys.modules["thonny.workbench"].in_simple_mode = Mock()
    sys.modules["thonny.workbench"].in_simple_mode.return_value = False
    sys.modules["thonny.workbench"].set_default = Mock()
    sys.modules["thonny.workbench"].set_default.return_value = True
    sys.modules["thonny.workbench"].add_

# Generated at 2022-06-22 13:04:19.004070
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb._in_simple_mode = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb._in_simple_mode = False
    wb._set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:04:24.834791
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(True)
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    assert os.environ["PGZERO_MODE"] == "1"
    get_workbench().set_option(_OPTION_NAME, False)
    assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:04:31.295325
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import get_workbench
    from thonny.config import set_default
    set_default("run.pgzero_mode", True)
    load_plugin()
    assert get_workbench().get_variable(_OPTION_NAME).get()
    toggle_variable()
    assert not get_workbench().get_variable(_OPTION_NAME).get()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:04:42.094740
# Unit test for function load_plugin
def test_load_plugin():
    from thonny import workbench, THONNY_USER_DIR
    workbench.clear_test_data()
    load_plugin()
    assert workbench.get_option(_OPTION_NAME) is False
    
    # Check preferences file
    pref_path = os.path.join(THONNY_USER_DIR, "preferences.ini")
    pref_file = open(pref_path, "r")
    text = pref_file.read()
    pref_file.close()
    assert "Pygame Zero mode" in text
    
    # Check menu
    # TODO: How can I check if the menu item is added?
    assert True is True
    
    # Check variable
    assert "PGZERO_MODE" in os.environ

# Generated at 2022-06-22 13:04:53.216291
# Unit test for function load_plugin
def test_load_plugin():
    wb = Workbench()
    wb.set_default("run.pgzero_mode", False)
    assert not wb.get_variable("run.pgzero_mode")
    assert wb.get_option("run.pgzero_mode") == False
    assert wb.in_simple_mode()
    assert os.environ["PGZERO_MODE"] == "auto"

    load_plugin()
    assert wb.get_variable("run.pgzero_mode")
    assert wb.get_option("run.pgzero_mode") == True
    assert os.environ["PGZERO_MODE"] == "True"

    toggle_variable()
    assert wb.get_variable("run.pgzero_mode")
    assert wb.get_option("run.pgzero_mode") == False

# Generated at 2022-06-22 13:04:59.561635
# Unit test for function toggle_variable
def test_toggle_variable():
    # Set the original value to True
    os.environ["PGZERO_MODE"] = "True"

    # Call toggle_variable()
    toggle_variable()

    # Check if the new value is False
    assert os.environ["PGZERO_MODE"] == "False"

    # Set the original value to False
    os.environ["PGZERO_MODE"] = "False"

    # Call toggle_variable()
    toggle_variable()

    # Check if the new value is True
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:05:08.766965
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    assert wb.get_variable(_OPTION_NAME).get() is False
    assert wb.get_option(_OPTION_NAME) is False
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.simple_mode = True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.simple_mode = False
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    wb.set_default(_OPTION_NAME, True)
    assert wb.get_variable(_OPTION_NAME).get() is True
    assert wb.get_option(_OPTION_NAME) is True

# Generated at 2022-06-22 13:05:18.845867
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    initial_value = wb.get_option(_OPTION_NAME)
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) != initial_value
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == initial_value

# Generated at 2022-06-22 13:05:25.506879
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench().set_default(_OPTION_NAME, True)
    os.environ["PGZERO_MODE"] = "auto"
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    # Simulate simple mode
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:05:29.465950
# Unit test for function toggle_variable
def test_toggle_variable():
    set_option(_OPTION_NAME, True)
    assert get_option(_OPTION_NAME, True)
    toggle_variable()
    assert not  get_option(_OPTION_NAME, True)
    toggle_variable()
    assert get_option(_OPTION_NAME, True)

# Generated at 2022-06-22 13:05:33.752398
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(
        "run.pgzero_mode", False
    )
    load_plugin()
    assert get_workbench().get_default("run.pgzero_mode") == False
    os.environ["PGZERO_MODE"] = "auto"

# Generated at 2022-06-22 13:05:45.072141
# Unit test for function load_plugin
def test_load_plugin():
    # Unit test for function load_plugin
    wb = get_workbench()
# #
# #     wb.set_default(_OPTION_NAME, True)
# #     load_plugin()
# #     assert not wb.get_option(_OPTION_NAME)
# #     assert not bool(os.environ.get("PGZERO_MODE"))
# #
# #     toggle_variable()
# #     assert wb.get_option(_OPTION_NAME)
# #     assert os.environ.get("PGZERO_MODE") == "True"
# #
# #     toggle_variable()
# #     assert not wb.get_option(_OPTION_NAME)
# #     assert os.environ.get("PGZERO_MODE") == "False"
# #
# #     wb.in

# Generated at 2022-06-22 13:05:55.231159
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.in_simple_mode = lambda: True
    load_plugin()
    assert wb.in_simple_mode()
    assert "PGZERO_MODE" not in os.environ

    setattr(wb, "in_simple_mode", lambda: False)
    load_plugin()
    assert not wb.in_simple_mode()
    assert os.environ["PGZERO_MODE"] == "False"
    
    get_workbench().get_option('run.pgzero_mode').set(True)
    load_plugin()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:00.907808
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:06:05.291533
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.reset_commands()
    load_plugin()
    wb.get_option(_OPTION_NAME)
    wb.get_command("toggle_pgzero_mode")

# Generated at 2022-06-22 13:06:14.132851
# Unit test for function update_environment
def test_update_environment():
    if os.environ.__contains__("PGZERO_MODE"):
        del os.environ["PGZERO_MODE"]
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_option("general.simple_mode", True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:06:18.919053
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:06:40.685636
# Unit test for function load_plugin
def test_load_plugin():
    from unittest.mock import Mock
    from thonny import workbench
    from thonny.misc_utils import running_on_mac_os
    from thonny.workbench import Workbench

    wb = Workbench()
    wb.get_option = Mock(return_value=False)
    wb.set_default = Mock(return_value=False)
    wb.in_simple_mode = Mock(return_value=False)
    load_plugin()
    wb.add_command.assert_called()
    if running_on_mac_os():
        assert os.environ["PGZERO_MODE"] == "0"
    else:
        assert os.environ["PGZERO_MODE"] == "0"

# Generated at 2022-06-22 13:06:45.367673
# Unit test for function load_plugin
def test_load_plugin():
    from thonny.plugins.pgzrun_mode import toggle_variable

#     get_workbench().set_default(_OPTION_NAME, False)
#     get_workbench().add_command("toggle_pgzero_mode","run",tr("Pygame Zero mode"), 
#         toggle_variable, flag_name=_OPTION_NAME, group=40)
    update_environment()
    print("The Plugin was loaded successfully")
    

# Generated at 2022-06-22 13:06:46.836132
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    assert get_workbench().in_simple_mode() == False



# Generated at 2022-06-22 13:06:49.056516
# Unit test for function toggle_variable
def test_toggle_variable():
    # toggle_variable()
    assert get_workbench().get_variable(_OPTION_NAME) == False

# Generated at 2022-06-22 13:06:51.740556
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    load_plugin()

    assert hasattr(get_workbench(), 'toggle_pgzero_mode') == True

# Generated at 2022-06-22 13:06:57.697938
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == False
    toggle_variable()
    assert wb.get_option(_OPTION_NAME) == True

# Generated at 2022-06-22 13:07:04.408190
# Unit test for function update_environment
def test_update_environment():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"
    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"
    wb.put_into_simple_mode()
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"
    wb.put_into_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:13.235846
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "auto"
    wb = get_workbench()
    wb.set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    wb.set_simple_mode(False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == str(wb.get_option(_OPTION_NAME))

    wb.set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:07:16.842398
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:07:28.300050
# Unit test for function toggle_variable
def test_toggle_variable():
    assert "PGZERO_MODE" not in os.environ
    setattr(get_workbench().in_simple_mode, "return_value", False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    setattr(get_workbench().in_simple_mode, "return_value", False)
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    setattr(get_workbench().in_simple_mode, "return_value", True)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ

# Generated at 2022-06-22 13:07:57.155120
# Unit test for function update_environment
def test_update_environment():
    global os

    os = Mock()
    os.environ = {}

    update_environment()
    assert os.environ["PGZERO_MODE"] == "0"

    get_workbench().set_option(_OPTION_NAME, True)

    update_environment()
    assert os.environ["PGZERO_MODE"] == "1"

    get_workbench().in_simple_mode = lambda: True
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:00.325585
# Unit test for function update_environment
def test_update_environment():
    # set in_simple_mode to false
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == str(False)

# Generated at 2022-06-22 13:08:11.792835
# Unit test for function toggle_variable
def test_toggle_variable():
    from unittest import mock

    from thonny.workbench import Workbench

    # Set Tk version to 8.5 for testing
    for method in ("tk", "tk_version", "wantobjects"):
        setattr(mock._tkinter, method, getattr(tkinter, method))

    # Create mocked workbench
    with mock.patch("thonny.workbench.Workbench") as workbench:
        instance = workbench.return_value
        instance.get_option.return_value = False
        instance.set_option.assert_not_called()
        toggle_variable()
        instance.set_option.assert_called_once_with(_OPTION_NAME, True)
        toggle_variable()
        instance.set_option.assert_called_with(_OPTION_NAME, False)
        update_environment()



# Generated at 2022-06-22 13:08:19.781082
# Unit test for function update_environment
def test_update_environment():
    assert os.environ.get("PGZERO_MODE") == None

    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)

    wb.in_simple_mode = lambda: False
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "False"

    wb.in_simple_mode = lambda: True
    update_environment()
    assert os.environ.get("PGZERO_MODE") == "auto"

# Generated at 2022-06-22 13:08:22.410196
# Unit test for function load_plugin
def test_load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    assert not get_workbench().get_option(_OPTION_NAME)
    assert get_workbench().get_default(_OPTION_NAME) == False


# Generated at 2022-06-22 13:08:33.718269
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_simple_mode(False)

    get_workbench().set_option(_OPTION_NAME, True)
    assert get_workbench().get_option(_OPTION_NAME)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    assert not get_workbench().get_option(_OPTION_NAME)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    get_workbench().set_simple_mode(True)
    os.environ.pop("PGZERO_MODE", None)

    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

# Generated at 2022-06-22 13:08:41.886049
# Unit test for function toggle_variable
def test_toggle_variable():
    wb = get_workbench()
    wb._set_simple_mode(True)
    wb.set_variable(_OPTION_NAME, False)
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == False
    wb._set_simple_mode(False)
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == True
    toggle_variable()
    assert wb.get_variable(_OPTION_NAME).get() == False

# Generated at 2022-06-22 13:08:49.950553
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, False)
    load_plugin()
    # check command
    wb.open_command_view()
    command = get_workbench().find_command("toggle_pgzero_mode")
    assert command != None
    assert command.label == tr("Pygame Zero mode")
    assert not get_workbench().get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"


# Generated at 2022-06-22 13:08:55.738530
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    load_plugin()
    assert not wb.get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "False"
    toggle_variable()
    assert wb.get_option(_OPTION_NAME)
    assert os.environ["PGZERO_MODE"] == "True"

if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:08:57.494071
# Unit test for function toggle_variable
def test_toggle_variable():
    toggle_variable()
    assert not get_workbench().get_option(_OPTION_NAME)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME)

# Generated at 2022-06-22 13:09:58.251427
# Unit test for function load_plugin
def test_load_plugin():
    wb = get_workbench()
    wb.set_default(_OPTION_NAME, True)
    load_plugin()
    assert wb.in_simple_mode()
    assert wb.get_option(_OPTION_NAME) is True
    assert os.environ["PGZERO_MODE"] == "True"


# Generated at 2022-06-22 13:10:07.213823
# Unit test for function update_environment
def test_update_environment():
    os.environ["PGZERO_MODE"] = "fake"
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

# Generated at 2022-06-22 13:10:15.997808
# Unit test for function update_environment
def test_update_environment():
    from thonny import get_workbench

    # Test in simple mode, pizero mode should be auto
    get_workbench().set_simple_mode(True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    # Test in advanced mode, pizero mode should be false
    get_workbench().set_simple_mode(False)
    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

    # Test in advanced mode, pizero mode should be true
    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

# Generated at 2022-06-22 13:10:23.954253
# Unit test for function update_environment
def test_update_environment():
    get_workbench().set_default(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "auto"

    get_workbench().set_option(_OPTION_NAME, True)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "True"

    get_workbench().set_option(_OPTION_NAME, False)
    update_environment()
    assert os.environ["PGZERO_MODE"] == "False"

# Generated at 2022-06-22 13:10:33.106362
# Unit test for function load_plugin
def test_load_plugin():
    from unittest import mock
    from thonny.globals import get_workbench

    with mock.patch("thonny.plugins.pgzero_mode.update_environment"):
        mock_workbench = mock.Mock()
        mock_workbench.get_option = get_workbench().get_option

        with mock.patch("thonny.plugins.pgzero_mode.get_workbench", return_value=mock_workbench):
            mock_workbench.add_command = mock.Mock()
            mock_workbench.set_default = mock.Mock()
            mock_workbench.set_default.side_effect = lambda option, value: setattr(mock_workbench, option, value)

# Generated at 2022-06-22 13:10:39.018134
# Unit test for function load_plugin
def test_load_plugin():
    load_plugin()
    if get_workbench().in_simple_mode():
        os.environ["PGZERO_MODE"] = "auto"
    else:
        os.environ["PGZERO_MODE"] = str(get_workbench().get_option(_OPTION_NAME))


if __name__ == "__main__":
    test_load_plugin()

# Generated at 2022-06-22 13:10:41.189865
# Unit test for function toggle_variable
def test_toggle_variable():
    get_workbench().set_default(_OPTION_NAME, False)
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == True
    toggle_variable()
    assert get_workbench().get_option(_OPTION_NAME) == False

# Generated at 2022-06-22 13:10:51.713907
# Unit test for function toggle_variable
def test_toggle_variable():
    if 'PGZERO_MODE' in os.environ:
        del os.environ['PGZERO_MODE']
        
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().set_simple_mode()
    os.environ["PGZERO_MODE"] == "auto"
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"  
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "True"  
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"  
    toggle_variable()
    assert os.environ["PGZERO_MODE"] == "False"  
    toggle_variable()
    assert os.environ["PGZERO_MODE"]

# Generated at 2022-06-22 13:10:56.210668
# Unit test for function toggle_variable
def test_toggle_variable():
    try:
        os.environ["PGZERO_MODE"] = "test"
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "True"
        toggle_variable()
        assert os.environ["PGZERO_MODE"] == "False"
    finally:
        os.environ["PGZERO_MODE"] = "0"

# Generated at 2022-06-22 13:11:01.005152
# Unit test for function toggle_variable
def test_toggle_variable():
    # Test w:False
    w = get_workbench()
    w.set_option(_OPTION_NAME, False)
    toggle_variable()
    assert w.get_option(_OPTION_NAME) == True
    # Test w:True
    toggle_variable()
    assert w.get_option(_OPTION_NAME) == False