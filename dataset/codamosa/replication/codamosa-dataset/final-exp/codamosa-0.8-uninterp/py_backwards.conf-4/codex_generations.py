

# Generated at 2022-06-14 01:21:59.760565
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == T

# Generated at 2022-06-14 01:22:03.687726
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)

    assert settings.debug == False

# Generated at 2022-06-14 01:22:05.634284
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:22:08.039741
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)  # Defaults
    init_settings(args)
    assert settings.debug == False
    # assert settings.debug == True

# Generated at 2022-06-14 01:22:11.798013
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True

    global settings

    assert settings.debug == False

    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:22:14.487784
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args2 = Namespace(debug=False)
    init_settings(args2)
    assert settings.debug == False



# Generated at 2022-06-14 01:22:15.779120
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert set

# Generated at 2022-06-14 01:22:22.093824
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert not settings.debug

if __name__ == "__main__":
    test_init_settings()

# Generated at 2022-06-14 01:22:27.093055
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:22:33.022079
# Unit test for function init_settings
def test_init_settings():
    # Test scenario 1: Run function with setting
    init_settings(Namespace(debug=True))
    assert settings.debug == True

    # Test scenario 2: Run function without setting
    init_settings(Namespace(debug=False))
    assert settings.debug == False

test_init_settings()

# Generated at 2022-06-14 01:22:38.172528
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:41.419500
# Unit test for function init_settings
def test_init_settings():
    arg = Namespace(debug=True)
    init_settings(arg)
    assert isinstance(settings, Settings)
    assert settings.debug == True



# Generated at 2022-06-14 01:22:43.568706
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:22:48.570202
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()

    # Test for debug = false
    init_settings(args)
    assert settings.debug == False

    # Test for debug = true
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:22:50.410363
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

# Generated at 2022-06-14 01:22:55.514097
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:00.473259
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == args.debug


if __name__ == '__main__':
    test_init_settings()

# Generated at 2022-06-14 01:23:04.491050
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:23:07.537603
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True



# Generated at 2022-06-14 01:23:11.484169
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:21.286620
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:26.175766
# Unit test for function init_settings
def test_init_settings():
    settings = Settings()
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug


if __name__ == '__main__':
    init_settings(Namespace())

# Generated at 2022-06-14 01:23:31.478917
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True


# Start peopledb

# Generated at 2022-06-14 01:23:37.380736
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True


if __name__ == "__main__":
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:23:40.219939
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True

    init_settings(Namespace(debug=False))
    assert settings.debug == False

# Generated at 2022-06-14 01:23:47.535299
# Unit test for function init_settings
def test_init_settings():
    import argparse
    args = argparse.Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Chess")
    parser.add_argument("--debug",
                        help="Enable debug mode",
                        action="store_true")
    args = parser.parse_args()
    init_settings(args)

# Generated at 2022-06-14 01:23:48.732966
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug

# Generated at 2022-06-14 01:23:53.612447
# Unit test for function init_settings
def test_init_settings():
    arg = Namespace(debug=True)
    init_settings(arg)
    assert settings.debug == True
    arg = Namespace(debug=False)
    init_settings(arg)
    assert settings.debug == False

# Generated at 2022-06-14 01:23:56.024191
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:23:58.597079
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:11.249246
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:14.037157
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug  # noqa

# Generated at 2022-06-14 01:24:18.069660
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:20.989749
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:24:25.699958
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace()
    test_args.debug = True
    init_settings(test_args)
    assert settings.debug

# Generated at 2022-06-14 01:24:31.182640
# Unit test for function init_settings
def test_init_settings():
    test_args = Namespace(debug = True)
    init_settings(test_args)
    assert settings.debug is True
    test_args = Namespace(debug = False)
    init_settings(test_args)
    assert settings.debug is False

# Generated at 2022-06-14 01:24:33.715796
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True

# Generated at 2022-06-14 01:24:35.664767
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug == True

# Generated at 2022-06-14 01:24:47.190246
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug


import sys
import logging


if settings.debug:
    level = logging.DEBUG
else:
    level = logging.INFO
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=level, stream=sys.stdout)


import unittest
import boto3
import time
import json

import src.handler as handler
import src.logger as logger

from controller import Controller

import tests.utils_database as utils_database
import tests.utils_handler as utils_handler


TEST_BUCKET = "test_bucket"

# Generated at 2022-06-14 01:24:49.175085
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:12.769474
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:15.942165
# Unit test for function init_settings
def test_init_settings():
    args_1 = Namespace(debug=False)
    init_settings(args_1)
    assert not settings.debug
    args_2 = Namespace(debug=True)
    init_settings(args_2)
    assert settings.debug

# Generated at 2022-06-14 01:25:17.892023
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug is True
    return


# Initialise settings
init_settings(parse_arguments())


# Generated at 2022-06-14 01:25:22.077125
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=False)
    init_settings(args)
    assert not settings.debug
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:24.715773
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:27.218294
# Unit test for function init_settings
def test_init_settings():
    assert not settings.debug
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug

# Generated at 2022-06-14 01:25:29.862072
# Unit test for function init_settings
def test_init_settings():
    settings = Settings()
    assert settings.debug == False
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:25:39.534304
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug', help='Set debug flag',
        action='store_true')
    args = parser.parse_args([])
    init_settings(args)
    assert settings.debug == False

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug', help='Set debug flag',
        action='store_true')
    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug == True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug', help='Set debug flag',
        action='store_true')


# Generated at 2022-06-14 01:25:51.944871
# Unit test for function init_settings
def test_init_settings():
    # Test 1: Test the debug flag is set to True
    args = Namespace()
    args.debug = True

    init_settings(args)
    assert settings.debug == True

    # Test 2: Test the debug flag is set to False
    args = Namespace()
    args.debug = False

    init_settings(args)
    assert settings.debug == False

if __name__ == '__main__':
    test_init_settings()
 

# Generated at 2022-06-14 01:25:54.641487
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:26:41.795708
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert(settings.debug)

# Generated at 2022-06-14 01:26:43.704090
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)

    assert settings.debug is True

# Generated at 2022-06-14 01:26:46.948167
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug == True
    args.debug = False
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:26:50.900682
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == args.debug
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == args.debug

# Generated at 2022-06-14 01:26:52.332150
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug



# Generated at 2022-06-14 01:26:56.613261
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False
    args.debug = True
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:27:02.983546
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser(description="Test settings")
    parser.add_argument("--debug", action = "store_true")
    settings.debug = False
    args = parser.parse_args(["--debug"])
    init_settings(args)
    assert settings.debug == True



# Generated at 2022-06-14 01:27:08.112332
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    assert isinstance(args.debug, bool) == False
    init_settings(args)
    assert isinstance(args.debug, bool) == True

# Generated at 2022-06-14 01:27:09.470955
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True))
    assert settings.debug == True

# Generated at 2022-06-14 01:27:13.329348
# Unit test for function init_settings
def test_init_settings():
    init_settings(Namespace(debug=True, input=None, output=None, width=None, height=None, resize=None, filter=None))
    assert settings.debug == True

# Generated at 2022-06-14 01:28:46.563442
# Unit test for function init_settings
def test_init_settings():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug')
    args = parser.parse_args()
    init_settings(args)
    assert settings.debug == False
    args = parser.parse_args(['--debug'])
    init_settings(args)
    assert settings.debug == True


# Unit tests for all functions in config.py


# Generated at 2022-06-14 01:28:48.855480
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:28:50.745599
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True, debug2=False)
    init_settings(args)
    assert settings.debug


# Define an example of a class that uses settings.debug

# Generated at 2022-06-14 01:28:52.503760
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True

# Generated at 2022-06-14 01:28:53.950868
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)

    assert settings.debug

# Generated at 2022-06-14 01:28:59.456563
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = False

    init_settings(args)

    assert(settings.debug == False)

    args.debug = True
    init_settings(args)

    assert(settings.debug == True)

# Generated at 2022-06-14 01:29:04.873458
# Unit test for function init_settings
def test_init_settings():
    for debug in [True, False]:
        args = Namespace(debug=debug)
        init_settings(args)
        assert (settings.debug == debug)

test_init_settings()


# The following code is for debugging only
if settings.debug:
    def debug_print(*objects, sep=' ') -> None:
        print(*objects, sep=sep, file=sys.stdout)
else:
    def debug_print(*objects, sep=' ') -> None:
        pass

# Generated at 2022-06-14 01:29:08.123077
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug=True)
    init_settings(args)
    assert settings.debug == True
    args = Namespace(debug=False)
    init_settings(args)
    assert settings.debug == False
    args = Namespace()
    init_settings(args)
    assert settings.debug == False

# Generated at 2022-06-14 01:29:11.455053
# Unit test for function init_settings
def test_init_settings():
    args = Namespace(debug = True)
    init_settings(args)
    assert settings.debug, "The debug variable should be True."

# Generated at 2022-06-14 01:29:13.651685
# Unit test for function init_settings
def test_init_settings():
    args = Namespace()
    args.debug = True
    init_settings(args)
    assert settings.debug