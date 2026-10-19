

# Generated at 2024-06-03 08:09:13.448985
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:14.723689
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:17.044480
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:18.486494
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:20.265319
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:21.874386
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:23.617120
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:24.933302
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:26.513870
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:27.879996
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:40.669303
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:42.023271
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:43.542397
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:44.999069
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:46.469111
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:48.071746
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:49.426586
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:50.946014
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:52.295840
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:09:53.714109
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:10:30.770693
# Unit test for method mute of class Register
def test_Register_mute():    register = Register()

# Generated at 2024-06-03 08:10:32.185908
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:10:34.362490
# Unit test for method as_dict of class Register
def test_Register_as_dict():    register = Register()

# Generated at 2024-06-03 08:10:39.735655
# Unit test for method __call__ of class Register
def test_Register___call__():    register = Register()

    # Mock render functions

# Generated at 2024-06-03 08:10:41.311436
# Unit test for method __new__ of class Style
def test_Style___new__():    rules = [RenderType(), RenderType()]

# Generated at 2024-06-03 08:10:45.353919
# Unit test for method __call__ of class Register
def test_Register___call__():    register = Register()

    # Mock render functions

# Generated at 2024-06-03 08:10:47.533105
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():    register = Register()

# Generated at 2024-06-03 08:10:53.671825
# Unit test for method copy of class Register
def test_Register_copy():    original = Register()

# Generated at 2024-06-03 08:10:56.302153
# Unit test for constructor of class Style
def test_Style():    style = Style("rule1", "rule2", value="test_value")

# Generated at 2024-06-03 08:10:57.645132
# Unit test for method unmute of class Register
def test_Register_unmute():    register = Register()

# Generated at 2024-06-03 08:11:31.435099
# Unit test for constructor of class Style
def test_Style():    style = Style("rule1", "rule2", value="test_value")

# Generated at 2024-06-03 08:11:33.009987
# Unit test for method unmute of class Register
def test_Register_unmute():    register = Register()

# Generated at 2024-06-03 08:11:35.158917
# Unit test for method unmute of class Register
def test_Register_unmute():    register = Register()

# Generated at 2024-06-03 08:11:37.119022
# Unit test for method __new__ of class Style
def test_Style___new__():    rules = [RenderType(), RenderType()]

# Generated at 2024-06-03 08:11:38.880533
# Unit test for method unmute of class Register
def test_Register_unmute():    register = Register()

# Generated at 2024-06-03 08:11:41.462883
# Unit test for method __new__ of class Style
def test_Style___new__():    rules = [RenderType(), RenderType()]

# Generated at 2024-06-03 08:11:42.695686
# Unit test for method unmute of class Register
def test_Register_unmute():    register = Register()

# Generated at 2024-06-03 08:11:45.033032
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():    register = Register()

# Generated at 2024-06-03 08:11:48.125061
# Unit test for method set_rgb_call of class Register

# Generated at 2024-06-03 08:11:53.949693
# Unit test for method __call__ of class Register
def test_Register___call__():    register = Register()

    # Mock render functions

# Generated at 2024-06-03 08:14:05.148443
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():    register = Register()

# Generated at 2024-06-03 08:14:07.598426
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():    register = Register()

# Generated at 2024-06-03 08:14:09.091142
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:14:12.658383
# Unit test for method copy of class Register
def test_Register_copy():
    original_register = Register()
    original_register.set_renderfunc(RenderType, lambda x: f"rendered_{x}")
    original_register.red = Style(RenderType(1), value="red")
    
    copied_register = original_register.copy()
    
    assert copied_register is not original_register
    assert copied_register.renderfuncs == original_register.renderfuncs
    assert copied_register.red == original_register.red
    assert copied_register.red.rules == original_register.red.rules
    assert copied_register.is_muted == original_register.is_muted
    
    # Modify the original and check that the copy does not change
    original_register.red = Style(RenderType(2), value="blue")
    assert copied_register.red != original_register.red
    assert copied_register.red.rules != original_register.red.rules

# Generated at 2024-06-03 08:14:15.689550
# Unit test for method set_rgb_call of class Register

# Generated at 2024-06-03 08:14:17.747937
# Unit test for method __new__ of class Style
def test_Style___new__():    rules = [RenderType(), RenderType()]

# Generated at 2024-06-03 08:14:22.722608
# Unit test for method copy of class Register
def test_Register_copy():    reg1 = Register()

# Generated at 2024-06-03 08:14:26.231018
# Unit test for method as_dict of class Register
def test_Register_as_dict():    register = Register()

# Generated at 2024-06-03 08:14:29.144166
# Unit test for method set_rgb_call of class Register

# Generated at 2024-06-03 08:14:31.485862
# Unit test for method set_eightbit_call of class Register

# Generated at 2024-06-03 08:16:47.926658
# Unit test for method as_namedtuple of class Register
def test_Register_as_namedtuple():    register = Register()

# Generated at 2024-06-03 08:16:52.736288
# Unit test for method copy of class Register
def test_Register_copy():    original = Register()

# Generated at 2024-06-03 08:16:54.285534
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:16:57.551831
# Unit test for method mute of class Register
def test_Register_mute():    register = Register()

# Generated at 2024-06-03 08:16:59.978791
# Unit test for method set_eightbit_call of class Register

# Generated at 2024-06-03 08:17:03.450573
# Unit test for method __setattr__ of class Register
def test_Register___setattr__():    register = Register()

# Generated at 2024-06-03 08:17:05.339895
# Unit test for method as_dict of class Register
def test_Register_as_dict():    register = Register()

# Generated at 2024-06-03 08:17:07.414897
# Unit test for method set_rgb_call of class Register

# Generated at 2024-06-03 08:17:08.679258
# Unit test for constructor of class Register
def test_Register():    register = Register()

# Generated at 2024-06-03 08:17:11.054839
# Unit test for method set_renderfunc of class Register