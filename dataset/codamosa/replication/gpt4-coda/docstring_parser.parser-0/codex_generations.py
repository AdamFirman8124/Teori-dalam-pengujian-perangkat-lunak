

# Generated at 2024-03-18 05:22:45.103498
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "The text to parse."
    assert parsed.long_description == "The style of docstring to parse. Defaults to Style.auto."
    assert len(parsed.params) == 2

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len(parsed_auto.params)

# Generated at 2024-03-18 05:22:53.839311
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:23:00.083151
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:23:07.676260
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:23:08.232384
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:23:09.012269
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:23:16.933477
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:23:17.518650
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:23:24.468257
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """

# Generated at 2024-03-18 05:23:31.420680
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:23:46.625293
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstrings for different styles

# Generated at 2024-03-18 05:23:52.765506
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:24:01.856976
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:24:02.419590
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:24:07.943792
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: The text to parse.
    :param style: The style of docstring to parse. Defaults to Style.auto.
    :returns: The parsed docstring object.
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:24:08.515838
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:24:20.498944
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style to use for parsing.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)

# Generated at 2024-03-18 05:24:21.082789
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:24:27.645968
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:24:36.396487
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert parsed.short_description == "Example function with types documented in the docstring."
    assert len(parsed.params) == 2
    assert parsed.returns.type_name == "bool"

    # Test with auto style detection
    auto_detected_docstring = """Example function with types documented in the docstring.

    :param param1: The first parameter.
    :type param1: int
    :param param2: The second parameter.
    :type param2: str
    :returns: bool -- The return value. True for success, False otherwise.
    """
   

# Generated at 2024-03-18 05:24:53.812708
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "The text to parse."
    assert parsed.long_description == "The style of docstring."
    assert len(parsed.params) == 2

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert parsed_auto.short_description == "docstring text to parse"

# Generated at 2024-03-18 05:25:08.146213
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:25:08.676650
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:09.197931
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:15.165107
# Unit test for function parse
def test_parse():    import pytest

    # Test with explicit style

# Generated at 2024-03-18 05:25:15.705072
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:22.897610
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_style_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_style_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len

# Generated at 2024-03-18 05:25:29.616069
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style to use for parsing.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    numpy_style_docstring = """
    Parameters
    ----------
    text : str
        The text to parse.
    style : Style, optional
        The style to use for parsing.

    Returns
    -------
    Docstring
        The parsed docstring object.
    """


# Generated at 2024-03-18 05:25:30.141399
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:30.756956
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:40.151513
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:45.831688
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mocking the parse functions for different styles

# Generated at 2024-03-18 05:25:46.364797
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:46.960669
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:25:53.264566
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """This is a sample Google-style docstring.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert parsed.short_description == "This is a sample Google-style docstring."
    assert len(parsed.params) == 2
    assert parsed.returns.description == "Description of return value"

    # Test with auto style detection
    auto_detected_docstring = """This is a sample docstring with auto style detection.

    :param arg1: Description of arg1
    :type arg1: int
    :param arg2: Description of arg2
    :type arg2: str
    :returns: Description of return value
    """
    parsed_auto = parse(auto_detected_docstring)


# Generated at 2024-03-18 05:25:59.396991
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:26:05.595400
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style to use for parsing.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len(parsed_auto.params)

# Generated at 2024-03-18 05:26:12.211313
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:26:12.753903
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:26:18.634619
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:26:27.079372
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:26:36.780662
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style to use for parsing.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)

# Generated at 2024-03-18 05:26:42.620253
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:26:48.190622
# Unit test for function parse
def test_parse():    import pytest

    # Test with explicit style

# Generated at 2024-03-18 05:26:54.627994
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:27:01.261159
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:27:07.216834
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:27:07.889618
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:27:13.686031
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:27:19.653953
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:27:34.443484
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mocking the parse functions for different styles

# Generated at 2024-03-18 05:27:41.254512
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "The text to parse."
    
    # Test with auto style detection
    auto_detected_docstring = """
    :param text: The text to parse.
    :param style: The style of docstring to parse. Defaults to Style.auto.
    :returns: The parsed docstring object.
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert parsed_auto.short_description == "The text to parse."
    
    # Test with a style that should raise a ParseError


# Generated at 2024-03-18 05:27:51.865983
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:27:52.617666
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:27:53.284013
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:27:53.842243
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:28:02.524358
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """This is a sample Google style docstring.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert parsed.short_description == "This is a sample Google style docstring."
    assert len(parsed.params) == 2
    assert parsed.returns.description == "Description of return value"

    # Test with auto style detection
    auto_detected_docstring = """This is a sample docstring with auto style detection.

    :param arg1: Description of arg1
    :type arg1: int
    :param arg2: Description of arg2
    :type arg2: str
    :return: Description of return value
    :rtype: bool
    """

# Generated at 2024-03-18 05:28:08.025500
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: The text to parse.
    :param style: The style of docstring to parse. Defaults to Style.auto.
    :returns: The parsed docstring object.
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len(parsed_auto.params) == 2

    # Test with an unsupported style

# Generated at 2024-03-18 05:28:16.577413
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstrings for different styles

# Generated at 2024-03-18 05:28:22.749821
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "The text to parse."
    assert parsed.long_description == "The style of docstring to parse. Defaults to Style.auto."
    assert len(parsed.params) == 2

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len(parsed_auto.params)

# Generated at 2024-03-18 05:28:36.456141
# Unit test for function parse
def test_parse():    import pytest

    # Test with explicit style

# Generated at 2024-03-18 05:28:43.170046
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:28:48.862710
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstring text

# Generated at 2024-03-18 05:28:57.521090
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "The text to parse."
    assert parsed.long_description == "The style of docstring to parse. Defaults to Style.auto."
    assert len(parsed.params) == 2

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len

# Generated at 2024-03-18 05:29:03.992379
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstrings for different styles

# Generated at 2024-03-18 05:29:10.172794
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style to use for parsing.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    numpy_style_docstring = """
    Parameters
    ----------
    text : str
        The text to parse.
    style : Style, optional
        The style to use for parsing.

    Returns
    -------
    Docstring
        The parsed docstring object.
    """


# Generated at 2024-03-18 05:29:10.760501
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:29:18.072804
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'

    # Test with auto style detection
    auto_detected_docstring = google_style_docstring
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len(parsed_auto.params) == 2

    # Test with a style that should raise a ParseError

# Generated at 2024-03-18 05:29:26.326657
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:29:33.070462
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "The text to parse."
    assert parsed.long_description == "The style of docstring to parse. Defaults to Style.auto."
    assert len(parsed.params) == 2

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:29:47.478619
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style to use for parsing.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)

# Generated at 2024-03-18 05:29:55.809844
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """This is a sample Google style docstring.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert parsed.short_description == "This is a sample Google style docstring."
    assert len(parsed.params) == 2
    assert parsed.returns.description == "Description of return value"

    # Test with auto style detection
    auto_detected_docstring = """This is a sample docstring with auto style detection.

    :param arg1: Description of arg1
    :type arg1: int
    :param arg2: Description of arg2
    :type arg2: str
    :return: Description of return value
    :rtype: bool
    """

# Generated at 2024-03-18 05:30:03.005492
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len(parsed_auto.params)

# Generated at 2024-03-18 05:30:10.536469
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.short_description == "The text to parse."
    assert parsed.long_description == "The style of docstring to parse. Defaults to Style.auto."
    assert len(parsed.params) == 2

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:30:17.723088
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:30:29.594430
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:30:35.706325
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """

# Generated at 2024-03-18 05:30:54.238542
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """This is a sample Google-style docstring.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert parsed.short_description == "This is a sample Google-style docstring."
    assert len(parsed.params) == 2
    assert parsed.returns.description == "Description of return value"

    # Test with auto style detection
    numpy_style_docstring = """This is a sample NumPy-style docstring.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value
    """
    parsed = parse(numpy_style_docstring)

# Generated at 2024-03-18 05:31:04.179963
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)
    assert len(parsed_auto.params)

# Generated at 2024-03-18 05:31:05.058520
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:31:18.190661
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:31:26.692299
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstrings for different styles

# Generated at 2024-03-18 05:31:37.242367
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:31:37.926334
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:31:44.910089
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstrings for different styles

# Generated at 2024-03-18 05:31:45.521207
# Unit test for function parse
def test_parse():import pytest


# Generated at 2024-03-18 05:31:53.895229
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstrings for different styles

# Generated at 2024-03-18 05:31:59.893711
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:32:08.696286
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)
    assert isinstance(parsed_auto, Docstring)

# Generated at 2024-03-18 05:32:15.622472
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse.
    
    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style detection
    auto_detected_docstring = """
    :param text: docstring text to parse
    :param style: docstring style, defaults to auto
    :returns: parsed docstring representation
    """
    parsed_auto = parse(auto_detected_docstring)

# Generated at 2024-03-18 05:32:29.093989
# Unit test for function parse
def test_parse():    # Test with explicit style
    google_style_docstring = """
    Args:
        text (str): The text to parse.
        style (Style, optional): The style of docstring to parse. Defaults to Style.auto.

    Returns:
        Docstring: The parsed docstring object.
    """
    parsed = parse(google_style_docstring, style=Style.google)
    assert isinstance(parsed, Docstring)
    assert len(parsed.params) == 2
    assert parsed.params[0].arg_name == 'text'
    assert parsed.params[1].arg_name == 'style'
    assert parsed.returns is not None
    assert parsed.returns.type_name == 'Docstring'

    # Test with auto style
    auto_parsed = parse(google_style_docstring)
    assert isinstance(auto_parsed, Docstring)
    assert len(auto_parsed.params) == 2

    # Test with non-existing style

# Generated at 2024-03-18 05:32:36.369021
# Unit test for function parse
def test_parse():    from unittest.mock import patch

    # Mock docstrings for different styles