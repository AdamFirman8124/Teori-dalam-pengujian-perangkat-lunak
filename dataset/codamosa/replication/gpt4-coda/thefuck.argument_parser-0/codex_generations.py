

# Generated at 2024-03-18 07:39:24.398386
# Unit test for method print_help of class Parser
def test_Parser_print_help():    parser = Parser()

# Generated at 2024-03-18 07:39:32.389303
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:39:39.919474
# Unit test for method print_help of class Parser
def test_Parser_print_help():    from io import StringIO

# Generated at 2024-03-18 07:39:40.893943
# Unit test for method print_help of class Parser
def test_Parser_print_help():from io import StringIO
from unittest.mock import patch


# Generated at 2024-03-18 07:39:42.961653
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:39:43.881709
# Unit test for method print_help of class Parser
def test_Parser_print_help():from io import StringIO
from unittest.mock import patch


# Generated at 2024-03-18 07:39:51.234180
# Unit test for method print_help of class Parser
def test_Parser_print_help():    from io import StringIO

# Generated at 2024-03-18 07:39:58.692871
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

# Generated at 2024-03-18 07:39:59.841032
# Unit test for method print_help of class Parser
def test_Parser_print_help():from unittest.mock import patch
from io import StringIO


# Generated at 2024-03-18 07:40:02.161595
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:40:15.631986
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:40:31.886022
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:40:34.729322
# Unit test for method print_help of class Parser
def test_Parser_print_help():from unittest.mock import patch
from io import StringIO


# Generated at 2024-03-18 07:40:35.481187
# Unit test for method parse of class Parser
def test_Parser_parse():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 07:40:40.359232
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:40:42.250709
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:40:52.884164
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:40:56.102353
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:41:05.420307
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:41:13.539971
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:41:39.165215
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:41:41.137225
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    parser = Parser()

# Generated at 2024-03-18 07:41:48.099844
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:41:55.254633
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:42:02.061285
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:42:03.197353
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():from io import StringIO
from unittest.mock import patch


# Generated at 2024-03-18 07:42:10.002057
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

# Generated at 2024-03-18 07:42:12.631261
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:42:20.464245
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

# Generated at 2024-03-18 07:42:35.651453
# Unit test for method parse of class Parser
def test_Parser_parse():    # Create an instance of the Parser class
    parser = Parser()

    # Test with no arguments
    args = parser.parse(['thefuck'])
    assert not args.version
    assert args.alias is None
    assert args.shell_logger is None
    assert not args.enable_experimental_instant_mode
    assert not args.help
    assert not args.debug
    assert args.command == []

    # Test with version argument
    args = parser.parse(['thefuck', '--version'])
    assert args.version
    assert args.alias is None
    assert args.shell_logger is None
    assert not args.enable_experimental_instant_mode
    assert not args.help
    assert not args.debug
    assert args.command == []

    # Test with alias argument
    args = parser.parse(['thefuck', '--alias'])
    assert not args.version
    assert args.alias == get_alias()
    assert args.shell_logger is None
    assert not args

# Generated at 2024-03-18 07:43:02.322486
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:43:05.060280
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:43:10.589144
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:43:11.376091
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():from io import StringIO
from unittest.mock import patch


# Generated at 2024-03-18 07:43:16.455929
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:43:21.992788
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:43:23.412835
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():from io import StringIO
from unittest.mock import patch


# Generated at 2024-03-18 07:43:26.650164
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:43:28.972895
# Unit test for method print_help of class Parser
def test_Parser_print_help():    parser = Parser()

# Generated at 2024-03-18 07:43:30.658708
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:44:24.787193
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

# Generated at 2024-03-18 07:44:32.971983
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:44:33.696800
# Unit test for method parse of class Parser
def test_Parser_parse():import unittest
from unittest.mock import patch


# Generated at 2024-03-18 07:44:41.061860
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:44:44.957868
# Unit test for method print_help of class Parser
def test_Parser_print_help():    parser = Parser()

# Generated at 2024-03-18 07:44:45.814385
# Unit test for method print_help of class Parser
def test_Parser_print_help():from unittest.mock import patch
from io import StringIO


# Generated at 2024-03-18 07:44:50.823992
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:44:56.499931
# Unit test for method print_help of class Parser
def test_Parser_print_help():    from io import StringIO

# Generated at 2024-03-18 07:45:01.348924
# Unit test for method print_help of class Parser
def test_Parser_print_help():    from io import StringIO

# Generated at 2024-03-18 07:45:04.235363
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:46:42.502120
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:46:43.619180
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():from io import StringIO
from unittest.mock import patch


# Generated at 2024-03-18 07:46:49.533117
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

    # Test with no arguments

# Generated at 2024-03-18 07:46:53.388204
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:47:01.405982
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

# Generated at 2024-03-18 07:47:10.106250
# Unit test for method parse of class Parser
def test_Parser_parse():    parser = Parser()

# Generated at 2024-03-18 07:47:13.095197
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()

# Generated at 2024-03-18 07:47:16.370845
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    from io import StringIO

# Generated at 2024-03-18 07:47:17.129735
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():from io import StringIO
from unittest.mock import patch


# Generated at 2024-03-18 07:47:20.789138
# Unit test for constructor of class Parser
def test_Parser():    parser = Parser()