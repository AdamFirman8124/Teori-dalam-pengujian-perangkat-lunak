

# Generated at 2022-06-22 12:38:33.561241
# Unit test for function main
def test_main():
    assert main() != 0


# Generated at 2022-06-22 12:38:34.194630
# Unit test for function main
def test_main():
    assert 0 == main()

# Generated at 2022-06-22 12:38:37.423297
# Unit test for function main
def test_main():
    assert main(['/a/b/c/input', '/a/b/c/output', '3.5']) != 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:38.170389
# Unit test for function main
def test_main():
    from py_backwards.tests.main_tests import TestMain
    TestMain().test_main()

# Generated at 2022-06-22 12:38:48.833891
# Unit test for function main

# Generated at 2022-06-22 12:38:51.319112
# Unit test for function main
def test_main():
    sys.argv = 'py-backwards -i C:\dev\py-backwards C:\dev\py-backwards\_test -o ".\dist" -t 3.6 -r C:\dev\py-backwards'.split()
    assert main() == 0

# Generated at 2022-06-22 12:39:02.073777
# Unit test for function main
def test_main():
    print("Testing main\n")

    try:
        from unittest import mock
    except ImportError:
        from unittest.mock import Mock as mock

    class MockParser(object):
        def __init__(self):
            self.input = []
            self.output = None
            self.target = None
            self.root = None

    # test for invalid input and invalid output
    parser = MockParser()
    parser.input = ['file']
    parser.output = 'file'
    main._original_parse_args = main.parse_args
    main.parse_args = mock.Mock(return_value=parser)
    assert main() == 1
    print("\nTest for invalid input and output passed\n")

    # test for input not found
    parser.input = ['input']

# Generated at 2022-06-22 12:39:06.537024
# Unit test for function main
def test_main():
    sys.argv = ['pybackwards',
                '-i', 'test',
                '-o', 'test.py',
                '-t', '2.7',
                '-r', 'sources',
                '-d']
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:07.478675
# Unit test for function main
def test_main():
    assert main() == 0


# Generated at 2022-06-22 12:39:12.832275
# Unit test for function main
def test_main():
    assert main() == 0
    assert main('-i', '__tests__/resources/test_py36.py',
                '-t', '2.7',
                '-o', '__tests__/resources/test_py27.py') == 0
    assert main('-i', '__tests__/resources/test_py36.py',
                '-t', '3.5',
                '-o', '__tests__/resources/test_py35.py') == 0
    assert main('-i', '__tests__/resources/test_py36.py',
                '-t', '3.6',
                '-o', '__tests__/resources/test_py36.py') == 0

# Generated at 2022-06-22 12:39:41.292165
# Unit test for function main
def test_main():
    from . import settings

    def assert_executed_with_args(args, stderr, stdout):
        assert_called_with(sys.argv, *args)
        assert_called_with(sys.stderr.write, *stderr)
        assert_called_with(sys.stdout.write, *stdout)

    assert main.__name__ == 'main'
    assert main.__annotations__ == {'int': int}
    assert sys.argv == ['']

    sys.stderr.write = MagicMock()
    sys.stderr.flush = MagicMock()
    sys.stdout.write = MagicMock()
    sys.stdout.flush = MagicMock()

    sys.argv = ['', '-t', '2.7']

# Generated at 2022-06-22 12:39:44.219395
# Unit test for function main
def test_main():
    sys.argv = ['-i', 'test/data/test.py', '-o', 'output.py', '-t', 'python35']
    assert main() == 0

# Generated at 2022-06-22 12:39:46.856699
# Unit test for function main
def test_main():
    sys.argv[1:] = '-i a.py -o b.py -t 3.5'.split()
    target = main()
    assert target == 0

# Generated at 2022-06-22 12:39:48.219249
# Unit test for function main
def test_main():
    print(main())

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:48.726867
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:39:56.098567
# Unit test for function main
def test_main():
    sys.argv.clear()
    sys.argv.append("-i")
    sys.argv.append("tests/fixtures/project/a.py")
    sys.argv.append("-o")
    sys.argv.append("tests/test_output")
    sys.argv.append("-t")
    sys.argv.append("py27")
    sys.argv.append("-r")
    sys.argv.append("tests/fixtures")
    sys.exit(main())

# Generated at 2022-06-22 12:39:58.440464
# Unit test for function main
def test_main():
    stderr_out = StringIO()
    sys.stderr = stderr_out
    assert main() == 0
    stderr_out.close()

# Generated at 2022-06-22 12:40:00.347115
# Unit test for function main
def test_main():
    # testing compilable code in py-backwards
    assert main()==0

# Generated at 2022-06-22 12:40:01.051350
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:40:01.720497
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:40:23.997515
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', '../__tests__', '-o', '../__tests__/compiled',
                    '-t', '2.5', '-d']
    sys.exit(main())


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-22 12:40:34.978122
# Unit test for function main
def test_main():
    input = ['examples/example.py']
    output = 'examples/output'
    target = '2.7'
    root = 'examples'
    sys.argv = [
        'py-backwards',
        '-i',
        'examples/example.py',
        '-o',
        'examples/output',
        '-t',
        '2.7',
        '-r',
        'examples',
    ]
    assert main() == 0
    assert input == sys.argv[2]
    assert output == sys.argv[4]
    assert target == sys.argv[6]
    assert root == sys.argv[8]

# Generated at 2022-06-22 12:40:39.792572
# Unit test for function main
def test_main():
    sys.argv = ['-i', 'P:/Python/HomeWork2/test_variables.py', '-o',
                '/', '-t', '3.5', '-d', '-r', 'P:/Python/HomeWork2']
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:46.179155
# Unit test for function main
def test_main():
    old_sys_argv = sys.argv
    sys.argv = [
        'py-backwards', '-i', 'sample', '-o', 'sample_converted', '-t', '2.7', '-r', 'sample_converted'
    ]
    try:
        assert main() == 0
    finally:
        sys.argv = old_sys_argv


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:57.005884
# Unit test for function main
def test_main():
    from unittest import TestCase, mock
    from io import StringIO

    sys.stdout = StringIO()

    # Test for successful compilation
    module_mock = mock.Mock()
    module_mock.exit.side_effect = SystemExit(0)
    with mock.patch('sys.modules', {'argparse': module_mock}):
        with mock.patch('pybackwards.compiler.compile_files',
                        return_value={'files': 1}):
            with TestCase.assertRaises(SystemExit):
                main()

# Generated at 2022-06-22 12:41:02.022060
# Unit test for function main
def test_main():
    init_settings(None)
    args = ArgumentParser('pybackwards')
    with pytest.raises(exceptions.InputDoesntExists):
        compile_files('non-existing-file')
    with pytest.raises(exceptions.InvalidInputOutput):
        compile_files('non-existing-file', '.')
    with pytest.raises(exceptions.CompilationError):
        compile_files(get_testdata('wrong-syntax.py'))
    with pytest.raises(exceptions.TransformationError):
        compile_files(get_testdata('wrong-transformation.py'))
    result = compile_files(get_testdata('correct-syntax.py'), target='py36')
    assert result == 0

# Generated at 2022-06-22 12:41:11.725983
# Unit test for function main
def test_main():
    """
    tests function main
    """
    import os
    import tempfile
    import shutil
    import io


# Generated at 2022-06-22 12:41:13.434858
# Unit test for function main
def test_main():
    assert main() == 0, 'failed'

# Generated at 2022-06-22 12:41:15.290351
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as e:
        print(e)
        assert False

# Generated at 2022-06-22 12:41:20.842700
# Unit test for function main
def test_main():
    input = "tests/data/test_func.py"
    output = "tests/output/"
    target = "python2"
    root = "tests/data/"
    debug = True
    
    import sys
    sys.argv = ["py-backwards", "-i", input, "-o", output, "-t", target, "-r", root, "-d", debug]
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:00.600261
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:42:01.195524
# Unit test for function main
def test_main():
    assert main() != 1

# Generated at 2022-06-22 12:42:12.084910
# Unit test for function main
def test_main():
    # Test i/o
    sys.argv = ['py-backwards', '-i', 'test/resources/test_input', '-o',
                'test/resources/test_output', '-t', 'py35']
    assert main() == 0
    sys.argv = ['py-backwards', '-i', 'test/resources/test_input', '-o',
                'test/resources/test_input', '-t', 'py35']
    assert main() == 1

    # Test target
    sys.argv = ['py-backwards', '-i', 'test/resources/test_input', '-o',
                'test/resources/test_output', '-t', 'py36']
    assert main() == 1

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:17.688819
# Unit test for function main
def test_main():
    with mock.patch('argparse.ArgumentParser.parse_args', return_value=type('a', (object,), {'input': 'b', 'output': 'c', 'target': 'd'})):
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:21.507899
# Unit test for function main
def test_main():
    test_args = ['-i', 'test_data/test.py', '-o', 'test_data/out.py', '-t', '3.6', '-d']
    with patch('sys.argv', test_args):
        assert main() == 0

# Generated at 2022-06-22 12:42:22.063586
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:42:25.781809
# Unit test for function main
def test_main():
    sys.argv = ['test', '-i', 'compiler/test_data/test_input.py',
                '-o', 'compiler/test_data/test_output.py',
                '-t', '2.7']
    main()

# Generated at 2022-06-22 12:42:27.722837
# Unit test for function main
def test_main():
    """Test main function"""
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:28.681616
# Unit test for function main
def test_main():
    assert main() == 0


# Generated at 2022-06-22 12:42:39.307281
# Unit test for function main
def test_main():
    import io
    import sys

    from contextlib import redirect_stdout
    from .conf import init_settings
    from . import const

    f = io.StringIO()
    with redirect_stdout(f):
        exit(main({"input": ["test/test_files/test_files1/main.py"],
                   "output": "output", "target": const.TARGETS[2.7],
                   "root": "test/test_files/test_files1",
                   "debug": False}))
    sys.stdout = sys.__stdout__
    out = f.getvalue()
    assert out == messages.compilation_result({'test/test_files/test_files1/main.py': {'output_file': 'output/main.py'}})

# Generated at 2022-06-22 12:44:18.817347
# Unit test for function main
def test_main():
    import pytest
    import os
    import shutil
    import subprocess

    def runmain():
        if 'pyb_root_dir' in os.environ:
            del os.environ['pyb_root_dir']
        if 'pyb_debug' in os.environ:
            del os.environ['pyb_debug']
        return subprocess.call(['python', '-m', 'py_backwards.main'])

    def setup(func):
        def wrapper(tmpdir):
            func(tmpdir)
        return wrapper

    @setup
    def test_simple(tmpdir):
        input_ = tmpdir.mkdir("input").join("module.py")
        input_.write("")
        output = tmpdir.mkdir("output")
        assert runmain() == 2
        assert runmain

# Generated at 2022-06-22 12:44:29.926933
# Unit test for function main
def test_main():
    parser = ArgumentParser(
        'py-backwards',
        description='Python to python compiler that allows you to use some '
                    'Python 3.6 features in older versions.')
    parser.add_argument('-i', '--input', type=str, nargs='+', required=True,
                        help='input file or folder')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='output file or folder')
    parser.add_argument('-t', '--target', type=str,
                        required=True, choices=const.TARGETS.keys(),
                        help='target python version')
    parser.add_argument('-r', '--root', type=str, required=False,
                        help='sources root')

# Generated at 2022-06-22 12:44:33.241134
# Unit test for function main
def test_main():
    print('UNIT TEST FOR FUNCTION main')
    try:
        if main() != 0:
            raise Exception
        print('SUCCESS')
    except:
        print('FAILED')
    print('============================================================\n')


if __name__ == "__main__":
    sys.exit(main())

# Generated at 2022-06-22 12:44:37.476603
# Unit test for function main
def test_main():
    """ unit test for function main """
    sys.argv = [sys.argv[0], '-i', 'tests/resources/example.py', '-o', 'build', '-r', 'tests/resources', '-t', '2']
    assert main() == 0

# Generated at 2022-06-22 12:44:38.203702
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:44.194894
# Unit test for function main
def test_main():
    def exit(x):
        pass
    sys.exit = exit
    sys.argv = ['py-backwards.py', '-i','path_to_file','path_to_folder', '-o','output','file','folder','-t','python2','-r','root','-d']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:44:48.148544
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:44:48.690287
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:58.053202
# Unit test for function main
def test_main():
    # test wrong input
    sys.argv = ['-i', '-o', '--target', '3.6']
    assert main() == 2
    # test compilation error
    sys.argv = ['-i', 'tests/test_compiler/data/syntax_err.py', '-o', '.', '--target', '3.6']
    assert main() == 1
    # test transformation error
    sys.argv = ['-i', 'tests/test_compiler/data/transformation_err.py', '-o', '.', '--target', '2.7']
    assert main() == 1
    # test input doesnt exists

# Generated at 2022-06-22 12:45:02.908064
# Unit test for function main
def test_main():
    # Only test coverage, because main is effectively tested
    # by pytest in test_compiler.py
    with mock.patch('sys.argv', ['py-backwards', '-input', 'a_file.py', '-o',
                                 'an_output.py', '-t', '2.7']):
        main()