

# Generated at 2024-06-01 18:30:21.160659
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:25.283668
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:28.742883
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:32.145623
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:35.358363
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:30:38.299489
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:41.383889
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:44.055099
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:47.391357
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:30:50.901444
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:05.065969
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:31:08.126142
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:11.113512
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:31:13.884310
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:19.939286
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:23.300385
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:26.677267
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:29.867347
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:33.724186
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:36.803674
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:31:51.890730
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:55.266021
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:31:58.665900
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:32:01.509927
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:06.305364
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:09.150499
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:11.949435
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:15.201658
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:18.529708
# Unit test for function parse
def test_parse():    # Test case 1: Valid Google style docstring
    google_docstring = """
    Summary line.

    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.

    Returns:
        bool: Description of return value.
    """
    result = parse(google_docstring, Style.google)
    assert result.short_description == "Summary line."
    assert len(result.params) == 2
    assert result.params[0].arg_name == "param1"
    assert result.params[1].arg_name == "param2"
    assert result.returns.type_name == "bool"

    # Test case 2: Valid Numpy style docstring

# Generated at 2024-06-01 18:32:21.218033
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:32:32.233566
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:35.272828
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:32:38.621019
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:32:41.979244
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:44.824436
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:48.030000
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:53.039904
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:56.327355
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:32:59.673290
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:02.447741
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:12.881893
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:15.796906
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:18.933849
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:22.099842
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:25.895367
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:28.776739
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:32.059439
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:35.409179
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:33:38.925035
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:42.826816
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:55.305554
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:33:58.637666
# Unit test for function parse
def test_parse():    # Test case 1: Parsing with a specific style
    docstring_text = """
    This is a test function.

    :param x: The first parameter.
    :param y: The second parameter.
    :returns: The result of the function.
    """
    style = Style.google
    result = parse(docstring_text, style)
    assert isinstance(result, Docstring)
    assert result.params[0].arg_name == "x"
    assert result.params[1].arg_name == "y"
    assert result.returns.description == "The result of the function."

    # Test case 2: Parsing with auto style
    result = parse(docstring_text)
    assert isinstance(result, Docstring)
    assert result.params[0].arg_name == "x"
    assert result.params[1].arg_name == "y"
    assert result.returns.description == "The result of the function."

    # Test case 3: Parsing with

# Generated at 2024-06-01 18:34:01.574022
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:04.848722
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:07.574534
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:10.993722
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:14.142228
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:16.950840
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:20.105440
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:23.873843
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:34.763674
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:39.290168
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:43.448199
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:34:46.313382
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:34:50.165100
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:34:53.272589
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:34:56.642802
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:00.810812
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:03.583050
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:06.474625
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:18.226452
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:21.757840
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:35:25.125825
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:29.253863
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:32.225004
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:35.183862
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:35:37.862175
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:40.750413
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:35:45.467677
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:48.389823
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:35:58.477018
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:02.997662
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:06.527209
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:09.128916
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:12.721906
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:16.172741
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:19.919085
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:23.106418
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:25.859985
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:36:28.833061
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:39.177936
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:42.074102
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:36:45.624726
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:48.432074
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:51.801021
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:54.787496
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:36:58.014687
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:01.578408
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:05.514407
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:09.068242
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:19.368444
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:22.185284
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:25.101945
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:27.764614
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:31.106855
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:34.269746
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:37:37.505234
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:41.014673
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:44.554701
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:47.127166
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:37:56.720031
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:37:59.671651
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:02.721371
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:06.058864
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:38:08.794366
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:38:12.636053
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:19.873470
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:23.451036
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:26.469590
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:29.616282
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:39.670764
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:43.190617
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:45.872856
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:38:48.889511
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:51.976350
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:38:54.670543
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:38:58.346637
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:01.873998
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:39:05.094300
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:08.606840
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:18.517635
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:21.788556
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:24.596157
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:39:28.905052
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:32.028928
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:35.309990
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:39.235314
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:42.914297
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:39:46.081961
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:49.377571
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:39:58.970936
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:40:02.616333
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring

# Generated at 2024-06-01 18:40:05.550087
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring, ParseError

# Generated at 2024-06-01 18:40:08.848148
# Unit test for function parse
def test_parse():    from docstring_parser.common import Docstring