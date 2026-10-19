

# Generated at 2022-06-22 12:38:33.499946
# Unit test for function main
def test_main():
    sys.argv = ['']
    assert main() == 1

# Generated at 2022-06-22 12:38:36.610260
# Unit test for function main
def test_main():
    """ Test main function of the program. """
    # Test 1: Check that there is no exception when calling main with no input
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:37.219349
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:38:45.288026
# Unit test for function main
def test_main():
    args = ArgumentParser(description='Test main function')
    args.add_argument('-i', '--input', type = str, nargs='+', required=True,
                        help='input file or folder')
    args.add_argument('-o', '--output', type = str, required=True,
                        help='output file or folder')
    args.add_argument('-t', '--target', type = str,
                        required=True, choices=const.TARGETS.keys(),
                        help='target python version')
    args.add_argument('-r', '--root', type = str, required=False,
                        help='sources root')
    args.add_argument('-d', '--debug', action='store_true', required=False,
                        help='enable debug output')

# Generated at 2022-06-22 12:38:45.983046
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:38:48.990629
# Unit test for function main
def test_main():
    with mock.patch('py-backwards.main.compile_files',
                    return_value=const.CompilationStats(1, 2, 3)):
        assert main() == 0

# Generated at 2022-06-22 12:38:51.540564
# Unit test for function main
def test_main():
    args = ["-i", "test.py", "-o", "test.c", "-t", "pythran"]
    assert main(args) == 0

# Generated at 2022-06-22 12:39:01.945650
# Unit test for function main
def test_main():
    # first test case
    sys.argv = ['', '-i', 'py_backwards/test_files/test.py', '-o', '../test.py',
                '-t', '3.7']
    assert 0 == main()

    # second test case
    sys.argv = ['', '-i', 'py_backwards/test_files/', '-o', '../test_folder/',
                '-t', '3.8']
    assert 0 == main()

    # third test case
    sys.argv = ['', '-i', 'py_backwards/test_files/test.py', '-o', '../test_folder/',
                '-t', '3.8', '-r', 'py_backwards/test_files/']
    assert 0 == main()

    #

# Generated at 2022-06-22 12:39:04.337054
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit

# Generated at 2022-06-22 12:39:07.423911
# Unit test for function main
def test_main():
    import pytest
    with pytest.raises(SystemExit) as e:
        main()
    assert e.type == SystemExit
    assert e.value.code == 2


if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:39:27.609010
# Unit test for function main
def test_main():
    assert main() == 0
    assert main() == 1
    assert main() == 1

# Generated at 2022-06-22 12:39:28.244137
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:38.825105
# Unit test for function main
def test_main():
    import os
    
    def test_with_good_input(filename, target_version):
        try:
            os.remove('output')
        except:
            pass
        main(['-i', filename, '-o', 'output', '-t', target_version])
        assert os.path.exists('output') is True
        os.remove('output')

    def test_with_bad_input(filename, target_version):
        try:
            os.remove('output')
        except:
            pass
        with pytest.raises(SystemExit):
            main(['-i', filename, '-o', 'output', '-t', target_version])
        assert os.path.exists('output') is False

    # Unit test for function main() with good input

# Generated at 2022-06-22 12:39:44.683979
# Unit test for function main
def test_main():
    from . import test_utils

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    patcher = patch.object(test_utils, 'compile_files', return_value={'x': 'y'})
    patcher.start()

    try:
        test_utils.main()
        assert False, 'No error thrown'
    except SystemExit as e:
        assert e.code == 0
    finally:
        patcher.stop()

# Generated at 2022-06-22 12:39:46.193094
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:50.828920
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'tests/input/correct.py', '-o', 'a.py',
                '-t', '3.5', '-r', 'tests/input/']
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 12:39:52.959017
# Unit test for function main
def test_main():
    assert main() == 1

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:59.514758
# Unit test for function main
def test_main():
    # Test python script with good input.
    # Test cases:
    # Test case:
    with pytest.raises(SystemExit) as cm:
        main()
    assert cm.value.code == 0

    # Test python script with bad input and errors.
    # Test cases:
    # Test case:
    # Test case:
    # Test case:
    # Test case:
    with pytest.raises(SystemExit) as cm:
        main()
    assert cm.value.code == 1

# Generated at 2022-06-22 12:40:07.271193
# Unit test for function main
def test_main():
    from . import __main__
    from . import exceptions

    import io
    import sys


# Generated at 2022-06-22 12:40:08.007482
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:26.082997
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:36.387976
# Unit test for function main
def test_main():
    test_args = ['fake', 'fake', 'fake', 'fake']
    with patch('sys.argv', new=test_args):
        with patch('pybackwards.compiler.compile_files') as mock:
            mock.side_effect = exceptions.CompilationError
            assert main() == 1
            mock.side_effect = exceptions.InputDoesntExists
            assert main() == 1
            mock.side_effect = exceptions.InvalidInputOutput
            assert main() == 1
            mock.side_effect = PermissionError
            assert main() == 1
            mock.return_value = {
                ('/tmp/foo.py', '/tmp/foo.py'): True,
                ('/tmp/bar.py', '/tmp/bar.py'): False,
            }
            assert main() == 0

# Generated at 2022-06-22 12:40:40.345713
# Unit test for function main
def test_main():
    sys.argv = ["pybackwards.py", "-i", "tests/main_tests", "-o", "tests/main_tests/out", "-t", "3.5", "-d", "-r", "main_tests"]
    assert(main() == 0)

# Generated at 2022-06-22 12:40:41.369325
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:42.720855
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:40:47.244291
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.4']
    assert main() == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:57.688177
# Unit test for function main
def test_main():
    samples = [
        (['sample.py'], ['sample_out.py'], '3.7', '.', True, 0),
        (['sample.py', 'sample2.py'], ['sample_out.py', 'sample2_out.py'], '3.7', '.', True, 0),
        (['sample.py', 'sample2.py'], ['/some/dir', '/some/dir'], '3.7', '.', True, 1),
        (['sample.py'], ['not/existing/dir'], '3.7', '.', True, 1),
        (['sample.py'], ['sample_out.py'], '3.7', 'non/existing/root', True, 1)
    ]

# Generated at 2022-06-22 12:41:02.999958
# Unit test for function main
def test_main():
    args = ['--input', 'tests/sources/print.py',
            '--output', 'output.py',
            '--target', '3.3',
            '--root', 'tests/sources']
    try:
        sys.argv = [sys.argv[0]] + args
        main()
    except SystemExit as e:
        if e.code != 0:
            raise

# Generated at 2022-06-22 12:41:11.957155
# Unit test for function main
def test_main():
    """
    Tests interaction with user
    """
    # Test correct work
    sys.argv = ['py-backwards', '-i', '/home/user/', '-o', '/home/user/pyb/', '-t', '2.7']
    main()

    # Test unrecognized arguments
    sys.argv = ['py-backwards', '-s', '/home/user/', '-g', '/home/user/pyb/', '-f', '2.7']
    main()

    # Test not enough arguments
    sys.argv = ['py-backwards', '-i', '/home/user/', '-t', '2.7']
    main()

    # Test not correct work

# Generated at 2022-06-22 12:41:19.661064
# Unit test for function main
def test_main():
    # Test1: debug output
    sys.argv = ['-i', 'input_0.py', '-o', 'output_0.py', '-t', '2.7', '-r',
                'root_0', '-d']

    # Test2: output file is not exists
    sys.argv = ['-i', 'input_1.py', '-o', 'output_1.py', '-t', '3.6', '-r',
                'root_1', '-d']

    # Test3: input file is not exists
    sys.argv = ['-i', 'input_2.py', '-o', 'output_2.py', '-t', '3.6', '-r',
                'root_2', '-d']

    # Test4: input and output are equals

# Generated at 2022-06-22 12:42:08.492693
# Unit test for function main
def test_main():
    import os
    import json


    def get_data(filename):
        with open(os.path.join('tests', 'test_data', filename)) as f:
            return json.load(f)


    def get_input_files():
        return [
            os.path.join('tests', 'test_files', f)
            for f in get_data('input')
        ]
    args = [
        '-i'] + get_input_files() + [
        '-o', get_data('output')[0],
        '-t', get_data('target')[0],
    ]
    main_args = main.__code__.co_varnames
    args_values = dict(zip(main_args, args))
    args_values['debug'] = True
    main(**args_values)