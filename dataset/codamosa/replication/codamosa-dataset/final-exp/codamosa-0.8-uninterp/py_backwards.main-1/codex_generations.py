

# Generated at 2022-06-22 12:38:29.204173
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', '.', '-o', 'output', '-t', '26']
    assert main() == 0


# Generated at 2022-06-22 12:38:39.102668
# Unit test for function main
def test_main():
    import subprocess
    cm = subprocess.run([sys.executable, '-m', 'py_backwards.cli'], stderr=subprocess.PIPE)
    assert cm.returncode == 2
    cm = subprocess.run([sys.executable, '-m', 'py_backwards.cli', '-i', 'input', '-o', 'output', '-t', '2'], stderr=subprocess.PIPE)
    assert cm.returncode == 1
    cm = subprocess.run(['python3', '-m', 'py_backwards.cli', '-i', 'input', '-o', 'output', '-t', '2'])
    assert cm.returncode == 0

# Generated at 2022-06-22 12:38:42.532123
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass
    # For now, function main() only prints the messages and returns int
    # values, so checking that there were no uncaught exceptions is enough

# Generated at 2022-06-22 12:38:52.017239
# Unit test for function main
def test_main():
    from pytest import raises
    from . import messages
    from .conf import AppSettings, get_settings

    # check nothing go wrong when valid params passed
    with raises(SystemExit) as pytest_wrapped_e:
        sys.argv += ['-i', 'input_file.py', '-o', 'output_file.py', '-t', '3.6']
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

    # check we've got exception when invalid params passed
    with raises(SystemExit) as pytest_wrapped_e:
        sys.argv = ['py-backwards', ]
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value

# Generated at 2022-06-22 12:38:53.162477
# Unit test for function main
def test_main():
    """Test function main
    """
    assert main() == 0

# Generated at 2022-06-22 12:39:03.854831
# Unit test for function main
def test_main():
    argv_backup = sys.argv
    sys.argv = ['py-backwards', '-i', './test/input', '-o', './test/output',
                '-t', '3.4', '-r', './test']
    assert main() == 0
    sys.argv = sys.argv[:1] + ['py-backwards', '-i', './test/input', '-o',
                               './test/output', '-t', '3.4', '-r', './test',
                               '-d']
    assert main() == 0

# Generated at 2022-06-22 12:39:05.608282
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:06.934743
# Unit test for function main
def test_main():
    from . import unittest
    unittest.main(main, sys.argv[1:])

# Generated at 2022-06-22 12:39:07.454147
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:07.949097
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:26.924222
# Unit test for function main
def test_main():
    import subprocess

    def run_subprocess(args):
        sub_args = ['py-backwards']
        for arg in args:
            sub_args.append(arg)
        process = subprocess.run(sub_args, capture_output=True, text=True)
        return process.returncode, process.stdout

    def run_code(code, path):
        file = open(path, 'w')
        file.write(code)
        file.close()

        return_code, std_out = run_subprocess(['-i', path, '-o', '../output/' +
                                               path[path.rfind('/') + 1:],
                                               '-t', '3.5'])
        return return_code, std_out


# Generated at 2022-06-22 12:39:27.960121
# Unit test for function main
def test_main():
    print(main())


# Generated at 2022-06-22 12:39:29.079556
# Unit test for function main
def test_main():
    assert main() == 1
    assert main() == 1

# Generated at 2022-06-22 12:39:34.315885
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'main.py', '-o', 'main_3.6.py',
                '-t', '3.6', '-d']
    assert main() == 0
    print(main.__doc__)


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:35.417402
# Unit test for function main
def test_main():
    # assert main() == 0
    pass

# Generated at 2022-06-22 12:39:41.040131
# Unit test for function main
def test_main():
    sys.argv = [' python3 -m py_backwards.main -i test/test_module.py -o test/test_module.py3.4 -t python3.4']
    sys.argv = [' python3 -m py_backwards.main -i test/test_module.py -o test/test_module.py2.7 -t python2.7']
    assert main() == 0

# Generated at 2022-06-22 12:39:41.767377
# Unit test for function main
def test_main():
    assert main() != 0

# Generated at 2022-06-22 12:39:48.172136
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', 'test.py', '-o', 'test.py', '-t', '3.5']
    assert main() == 0

    sys.argv = [sys.argv[0], '-i', 'test.py', '-o', 'test.py', '-t', '3.6']
    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:54.884857
# Unit test for function main
def test_main():
    init_settings(ArgumentParser.parse_args(
        ['test_input.py',
         '-i', 'tests',
         '-o', 'temp',
         '-t', '3.4',
         '-d',
         '-r', 'tests']
    ))
    from . import compiler
    compiler.compile('tests/test_input.py')

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:55.484714
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:40:15.998574
# Unit test for function main
def test_main():
    assert main()

# Check if this was run from the command line
if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:26.945923
# Unit test for function main
def test_main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', type=str, nargs='+', required=True)
    parser.add_argument('-o', '--output', type=str, required=True)
    parser.add_argument('-t', '--target', type=str, required=True)
    parser.add_argument('-r', '--root', type=str, required=False)
    parser.add_argument('-d', '--debug', default=False, required=False)

    test_args = parser.parse_args(['-i', 'data_test', '-o', 'data_out',
                                   '-t', 'py36', '-r', 'data_test'])
    init_settings(test_args)
    assert main() == 0

# Generated at 2022-06-22 12:40:28.099888
# Unit test for function main
def test_main():
    # TODO:
    pass



# Generated at 2022-06-22 12:40:31.721858
# Unit test for function main
def test_main():
    assert main(['-i', 'tests/examples/ex1.py', '-o', 'compiled' ,'-t','2.7']) == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:34.202902
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:34.839074
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:45.358010
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards',
                '-i', '../tests/data/input/my_module.py',
                '-o', '../tests/data/output/my_module.py',
                '-t', 'py35',
                '-r', '../tests/data/input']
    assert main() == 0

    sys.argv = ['py-backwards',
                '-i', '../tests/data/input/not_exists.py',
                '-o', '../tests/data/output/not_exists.py',
                '-t', 'py35']
    assert main() == 1


# Generated at 2022-06-22 12:40:56.412098
# Unit test for function main
def test_main():
    # Get current folder for input file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(current_dir, '..', 'test', 'test_generator')

    # Create test folder for output file
    output_dir = os.path.join(current_dir, '..', 'test', 'pybackwards_test')
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Test 1: Generate warning when target is not python 3.6

# Generated at 2022-06-22 12:41:01.130667
# Unit test for function main
def test_main():
    class Args:
        pass
    args = Args()
    args.input = ['file1.py']
    args.output = 'file2.py'
    args.target = 'python36'
    args.root = './'
    args.debug = True
    init_settings(args)
    assert main() == 0

# Generated at 2022-06-22 12:41:11.067253
# Unit test for function main
def test_main():
    import os
    import tempfile

    tests_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'tests')
    input_path = os.path.join(tests_path, 'data', 'test_input.py')
    input_folder_path = os.path.join(tests_path, 'data')
    input_folder_path_empty = os.path.join(tests_path, 'data', 'empty')
    input_root = os.path.join(tests_path, 'data2')

    output_path = os.path.join(tests_path, 'data', 'test_output.py')
    output_path_empty = os.path.join(tests_path, 'data', 'empty.py')
    output_folder_path = os

# Generated at 2022-06-22 12:41:59.439419
# Unit test for function main
def test_main():
    from .py_backwards import main
    from .conf import settings
    from .exceptions import CompilationError, InputDoesntExists, \
                            TransformationError, InvalidInputOutput
    from .messages import syntax_error, transformation_error, \
                         input_doesnt_exists, invalid_output, \
                         compilation_result
    import os
    import sys
    import pytest
    import tempfile

    source_dir = tempfile.TemporaryDirectory()
    output_dir = tempfile.TemporaryDirectory()
    source_file = os.path.join(source_dir.name, 'test.py')
    output_file = os.path.join(output_dir.name, 'test.py')


# Generated at 2022-06-22 12:42:04.050130
# Unit test for function main
def test_main():
    n_args = len(sys.argv)
    sys.argv.extend([
        '-i', 'main.py',
        '-o', 'test_out',
        '-t', '3.4'
    ])
    assert main() == 0
    sys.argv = sys.argv[:n_args]

# Generated at 2022-06-22 12:42:05.119694
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:06.066111
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:07.296501
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:42:16.738425
# Unit test for function main
def test_main():
    # test for invalid argument
    assert main(['-target', 'python36', '-input', 'test_files/test.py']) == (2)
    # test for syntax error
    assert main(['-target', 'python36', '-input', 'test_files/test1.py']) == (1)
    # test for transformation error
    assert main(['-target', 'python36', '-input', 'test_files/test2.py']) == (1)
    # test for input doesnt exists
    assert main(['-target', 'python36', '-input', 'input']) == (1)
    # test for invalid input/output
    assert main(['-target', 'python36', '-input', 'test_files/test.py',
                 '-output', 'test_files']) == (1)

# Generated at 2022-06-22 12:42:27.293599
# Unit test for function main
def test_main():
    try:
        raise exceptions.CompilationError("error string", 1, 1, 0)

    except exceptions.CompilationError as e:
        assert messages.syntax_error(e) == "error string"

    try:
        raise exceptions.InputDoesntExists("file.py")

    except exceptions.InputDoesntExists as e:
        assert messages.input_doesnt_exists(e) == "File file.py doesn't exists."

    try:
        raise exceptions.InvalidInputOutput("input file", "output file")

    except exceptions.InvalidInputOutput as e:
        assert messages.invalid_output(e[0], e[1]) == "You can't use input file as output."


# Generated at 2022-06-22 12:42:29.064172
# Unit test for function main
def test_main():
    assert main() == 0


if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:42:30.280944
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:35.256262
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards',
        '-i',
        'testdata/input/main.py',
        '-o',
        'testdata/output/main',
        '-t',
        'python36',
        '-r',
        'testdata/input/'
    ]
    assert main() == 0

# Generated at 2022-06-22 12:44:14.965962
# Unit test for function main
def test_main():
    with mock.patch('argparse.ArgumentParser.parse_args') as mock_args:
        mock_args.return_value = argparse.Namespace(
            input=['tests/test_data/source/hello.py', 'tests/test_data/source/'],
            output='tests/test_data/output/',
            target='python36',
            root='tests/test_data/source/',
            debug=False
        )
        with mock.patch('py_backwards.compiler.init_settings') as mock_init_settings:
            mock_init_settings.return_value = None

# Generated at 2022-06-22 12:44:26.175107
# Unit test for function main
def test_main():
    # Testing main function with no arguments
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

    # Testing main function with debug flag but no input
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(['--debug'])
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

    # Testing main function with bad target argument
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(['--target', '2.7', '--input', 'tests'])
    assert pytest_wrapped_e

# Generated at 2022-06-22 12:44:34.550277
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest import TestCase
    from . import run
    from . import const

    class TestMain(TestCase):

        def test_empty_args(self):
            with self.assertRaises(SystemExit):
                run.main()

        def test_invalid_input(self):
            args = ['pyback.py', '-i', '--input']
            with self.assertRaises(SystemExit):
                run.main(args)

        def test_invalid_target(self):
            args = ['pyback.py', '-i', 'input', '-o', 'output', '-t', 'invalid']
            with self.assertRaises(SystemExit):
                run.main(args)


# Generated at 2022-06-22 12:44:35.154510
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:35.795223
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:41.725072
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'a', '-o', 'b', '-r', 'c', '-t', 'py27']
    init_settings()
    settings.input = ['a']
    settings.root = 'c'
    settings.target = 'py27'
    settings.output = 'b'
    assert main() == 1


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:44:47.325246
# Unit test for function main
def test_main():
    with open('temp.txt', 'w') as file:
        file.write('a = 3')
    sys.argv = ['py-backwards', '-i', 'temp.txt', '-o', 'temp_new.txt', '-t', '3020']
    assert main() == 0

# Generated at 2022-06-22 12:44:55.212456
# Unit test for function main
def test_main():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', '../', '-t', '2.7']
    main()
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', '../', '-t', '3.3']
    main()
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', '../', '-t', '3.4']
    main()
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', '../', '-t', '3.5']
    main()

# Generated at 2022-06-22 12:45:03.088299
# Unit test for function main
def test_main():
    assert len(sys.argv) < 1
    sys.argv.append("-i")
    sys.argv.append("tests/resources/features.py")
    sys.argv.append("-o")
    sys.argv.append("tests/resources/features_out.py")
    sys.argv.append("-t")
    sys.argv.append("2")
    sys.argv.append("-r")
    sys.argv.append("py-backwards")
    assert len(sys.argv) == 9


# Generated at 2022-06-22 12:45:12.379772
# Unit test for function main
def test_main():
    # Test when input exists
    with pytest.raises(SystemExit):
        sys.argv += ['-i', 'pybackwards/test_data/test_file_0.py',
                     '-t', 'py34', '-o', 'pybackwards/test_output/test_file_1.py']
        main()

    # Test when input doesn't exist
    with pytest.raises(SystemExit):
        sys.argv += ['-i', 'pybackwards/test_data/test_file.py',
                     '-t', 'py34', '-o', 'pybackwards/test_output/test_file_2.py']
        main()

    # Test when invalid output