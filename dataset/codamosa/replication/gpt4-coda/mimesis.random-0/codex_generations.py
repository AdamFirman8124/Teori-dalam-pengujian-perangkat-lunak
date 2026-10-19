

# Generated at 2024-03-18 06:17:31.763262
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "Default code length should be 4"
    assert code_default[0].isalpha() and code_default[0].isupper(), "First character should be an uppercase letter"
    assert code_default[1:].isdigit(), "Following characters should be digits"

    # Test the custom_code method with a custom mask
    custom_mask = 'A##-##B'
    code_custom_mask = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(code_custom_mask) == len(custom_mask), "Custom mask code length should match the mask length"
    assert code_custom_mask[0].isalpha() and code_custom_mask[0].isupper(), "First character should be an uppercase letter"
    assert code_custom

# Generated at 2024-03-18 06:17:38.875672
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "Default code length should be 4"
    assert code_default[0].isalpha() and code_default[1:].isdigit(), "Default code should match pattern @###"

    # Test with a custom mask
    custom_mask = 'A##-##B'
    code_custom_mask = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(code_custom_mask) == len(custom_mask), "Custom mask code length should match mask length"

# Generated at 2024-03-18 06:17:48.370459
# Unit test for method custom_code of class Random
def test_Random_custom_code():    rnd = Random()

    # Test with default mask

# Generated at 2024-03-18 06:17:57.126297
# Unit test for method custom_code of class Random
def test_Random_custom_code():    import pytest


# Generated at 2024-03-18 06:18:03.636416
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "Default code length should be 4"
    assert code_default[0].isalpha() and code_default[0].isupper(), "First character should be an uppercase letter"
    assert code_default[1:].isdigit(), "Last three characters should be digits"

    # Test the custom_code method with a custom mask
    custom_mask = 'A##-##B'
    code_custom_mask = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(code_custom_mask) == len(custom_mask), "Custom code length should match custom mask length"
    assert code_custom_mask[0].isalpha() and code_custom_mask[0].isupper(), "First character should be an uppercase letter"
    assert code_custom

# Generated at 2024-03-18 06:18:10.515830
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "Default code length should be 4"
    assert code_default[0].isalpha() and code_default[0].isupper(), "First character should be an uppercase letter"
    assert code_default[1:].isdigit(), "Following characters should be digits"

    # Test with a different mask
    mask = 'A##-##B'
    code_mask = rnd.custom_code(mask=mask)
    assert len(code_mask) == len(mask), f"Code length should match mask length {len(mask)}"
    assert code_mask[0] == 'A' and code_mask[-1] == 'B', "Code should start with 'A' and end with 'B'"
    assert code_mask[1:3].isdigit() and code_mask

# Generated at 2024-03-18 06:18:17.932510
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Test the custom_code method with default mask
    default_code = random.custom_code()
    assert len(default_code) == 4
    assert default_code[0].isalpha() and default_code[0].isupper()
    assert default_code[1:].isdigit()

    # Test the custom_code method with custom mask
    custom_mask = 'A##-@@@'
    custom_code = random.custom_code(mask=custom_mask, char='@', digit='#')
    assert len(custom_code) == 7
    assert custom_code[0] == 'A'
    assert custom_code[1:3].isdigit()
    assert custom_code[3] == '-'
    assert custom_code[4:].isalpha() and custom_code[4:].isupper()

    # Test the custom_code method with same placeholders for digits and chars

# Generated at 2024-03-18 06:18:27.156731
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default mask
    default_code = rnd.custom_code()
    assert len(default_code) == 4, "Default code length should be 4"
    assert default_code[0].isalpha() and default_code[0].isupper(), "First character should be an uppercase letter"
    assert default_code[1:].isdigit(), "Last three characters should be digits"

    # Test the custom_code method with a custom mask
    custom_mask = 'A##-##B'
    custom_code = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(custom_code) == 7, "Custom code length should be 7"
    assert custom_code[0] == 'A', "First character should be 'A'"

# Generated at 2024-03-18 06:18:36.001266
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Test the custom_code method with default mask
    default_code = random.custom_code()
    assert len(default_code) == 4
    assert default_code[0].isalpha() and default_code[0].isupper()
    assert default_code[1:].isdigit()

    # Test the custom_code method with a custom mask
    custom_mask = 'A##-@@@'
    custom_code = random.custom_code(mask=custom_mask, char='@', digit='#')
    assert len(custom_code) == 7
    assert custom_code[0] == 'A'
    assert custom_code[1:3].isdigit()
    assert custom_code[3] == '-'
    assert all(c.isalpha() and c.isupper() for c in custom_code[4:])

    # Test the custom_code method with same placeholders for digits and chars

# Generated at 2024-03-18 06:18:42.533959
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "Default code length should be 4"
    assert code_default[0].isalpha() and code_default[1:].isdigit(), "Default code should match pattern @###"

    # Test with a custom mask
    custom_mask = 'A##-##B'
    code_custom_mask = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(code_custom_mask) == len(custom_mask), "Custom mask code length should match the mask length"

# Generated at 2024-03-18 06:18:54.212577
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "Default code length should be 4"
    assert code_default[0].isalpha() and code_default[1:].isdigit(), "Default code should match pattern @###"

    # Test with a different mask
    mask = 'A##-##B'
    code_mask = rnd.custom_code(mask=mask, char='A', digit='#')
    assert len(code_mask) == len(mask), "Code length should match mask length"
    assert code_mask[0].isalpha() and code_mask[1:3].isdigit() and code_mask[4:6].isdigit() and code_mask[-1].isalpha(), "Code should match the custom mask pattern"

    # Test with same placeholders for digits and chars

# Generated at 2024-03-18 06:19:00.790066
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "Default code length should be 4"
    assert code_default[0].isalpha() and code_default[1:].isdigit(), "Default code should match pattern @###"

    # Test with a custom mask
    custom_mask = 'A##-##B'
    code_custom_mask = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(code_custom_mask) == len(custom_mask), "Custom mask code length should match the mask length"
    assert code_custom_mask[0].isalpha() and code_custom_mask[1:3].isdigit() and code_custom_mask[4:6].isdigit() and code_custom_mask[-1].isalpha(), "Custom mask code should match the custom pattern"

    #

# Generated at 2024-03-18 06:19:09.842504
# Unit test for method custom_code of class Random
def test_Random_custom_code():    rnd = Random()

    # Test with default mask

# Generated at 2024-03-18 06:19:17.188356
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "The default code length should be 4."
    assert code_default[0].isalpha() and code_default[0].isupper(), "The first character should be an uppercase letter."
    assert code_default[1:].isdigit(), "The last three characters should be digits."

    # Test the custom_code method with a custom mask
    custom_mask = 'A##-##B'
    code_custom_mask = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(code_custom_mask) == len(custom_mask), "The code length should match the custom mask length."

# Generated at 2024-03-18 06:19:26.244766
# Unit test for method custom_code of class Random
def test_Random_custom_code():    import unittest


# Generated at 2024-03-18 06:19:34.791450
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Arrange
    custom_random = Random()

    # Act
    code_with_default_mask = custom_random.custom_code()
    code_with_custom_mask = custom_random.custom_code(mask='@@##@@')
    code_with_same_placeholders = None
    exception_raised = False

    try:
        code_with_same_placeholders = custom_random.custom_code(char='#', digit='#')
    except ValueError:
        exception_raised = True

    # Assert
    assert len(code_with_default_mask) == 4
    assert code_with_default_mask[0].isalpha() and code_with_default_mask[0].isupper()
    assert code_with_default_mask[1:].isdigit()
    assert len(code_with_custom_mask) == 6
    assert code_with_custom_mask[0:2].isalpha() and code_with_custom_mask[0:2].isupper()
    assert code_with_custom_mask[2:4].isdigit()

# Generated at 2024-03-18 06:19:40.809196
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Create an instance of the Random class
    rnd = Random()

    # Test the custom_code method with default parameters
    code_default = rnd.custom_code()
    assert len(code_default) == 4, "The default code length should be 4"
    assert code_default[0].isalpha() and code_default[0].isupper(), "The first character should be an uppercase letter"
    assert code_default[1:].isdigit(), "The last three characters should be digits"

    # Test the custom_code method with a custom mask
    custom_mask = 'A##-##B'
    code_custom_mask = rnd.custom_code(mask=custom_mask, char='A', digit='#')
    assert len(code_custom_mask) == len(custom_mask), "The code length should match the custom mask length"
    assert code_custom_mask[0] == 'A', "The first character should match the custom mask"
    assert code_custom_mask[-1]

# Generated at 2024-03-18 06:19:48.852087
# Unit test for method custom_code of class Random
def test_Random_custom_code():    rnd = Random()

    # Test with default mask

# Generated at 2024-03-18 06:19:54.646873
# Unit test for method custom_code of class Random
def test_Random_custom_code():    import unittest


# Generated at 2024-03-18 06:20:04.760938
# Unit test for method custom_code of class Random
def test_Random_custom_code():    # Arrange
    custom_random = Random()

    # Act
    code_with_default_mask = custom_random.custom_code()
    code_with_custom_mask = custom_random.custom_code(mask='@@@###')
    code_with_same_placeholders = None
    try:
        code_with_same_placeholders = custom_random.custom_code(char='#', digit='#')
    except ValueError as e:
        caught_exception = str(e)

    # Assert
    assert len(code_with_default_mask) == 4
    assert code_with_default_mask[0].isalpha() and code_with_default_mask[1:].isdigit()
    assert len(code_with_custom_mask) == 6
    assert all(c.isalpha() for c in code_with_custom_mask[:3])
    assert all(c.isdigit() for c in code_with_custom_mask[3:])
    assert code_with_same_placeholders is None
    assert caught_exception == 'You cannot use the same placeholder for digits and chars!'
