

# Generated at 2022-06-22 12:38:34.467045
# Unit test for function main
def test_main():
    from mock import patch, MagicMock
    from .compiler import compile_files
    with patch('pybackwards.compiler.compile_files', return_value=0):
        main()
        main2()
    with patch('pybackwards.compiler.compile_files', return_value=1):
        main3()


# Generated at 2022-06-22 12:38:40.283337
# Unit test for function main
def test_main():
    args = ['tests/test_code/py3.6_standart_code.py', '-o', 'tests/out.py',
            '-t', '3.4', '-i', 'tests/test_code/py3.6_standart_code.py']
    exit_code = main(args)
    assert exit_code == 0, 'Bad exit code'


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:48.035708
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from .main import main
    with patch('sys.argv', ['py-backwards', '-i', 'a.py', '-o', 'b.py',
                            '-t', '2.7', '-r', 'root']):
        assert main() == 0
    with patch('sys.argv', ['py-backwards', '-i', 'a.py', '-o', 'b.py',
                            '-t', '3.6', '-r', 'root']):
        assert main() == 0

# Generated at 2022-06-22 12:38:49.940227
# Unit test for function main
def test_main():
    """ Unit test for function main """
    assert main() == 0

# Generated at 2022-06-22 12:38:53.444239
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'tests/sample.py', '-o', 'main', '-t', 'py36']
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:54.789792
# Unit test for function main
def test_main():
    init_settings(ArgumentParser().parse_args([]))
    assert main() == 1

# Generated at 2022-06-22 12:38:55.388703
# Unit test for function main
def test_main():
    assert main() != 0

# Generated at 2022-06-22 12:38:55.948104
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-22 12:38:56.516604
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:39:03.116344
# Unit test for function main
def test_main():
    exit_code = main(["-i", "C:\\Users\\Student24.DESKTOP-E9U6CJU\\Desktop\\py-backwards\\tests\\test.py", "-o", "C:\\Users\\Student24.DESKTOP-E9U6CJU\\Desktop\\py-backwards\\tests\\test_output.py", "-t", "3.5"])
    assert exit_code == 0

# Generated at 2022-06-22 12:39:12.434480
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:18.035012
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'test/test_src/test_input.py', '-o', 'test/test_src/test_input_out.py', '-t', '2.7', '-r', 'test/test_src']
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:18.622817
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:22.209559
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'test/test.py', '-o', 'test_output/', '-t', '2.7', '-r', 'test/test.py']
    main()
    assert True

# Generated at 2022-06-22 12:39:27.560982
# Unit test for function main
def test_main():
    assert main(['-i', '/home/Sebastian/Desktop/py-backwards/py_backwards_new/samples/simple_file.py',
                 '-r', '/home/Sebastian/Desktop/py-backwards/',
                 '-t', '2.7',
                 '-o', '/home/Sebastian/Desktop/py-backwards',
                 ]) == 0

# Generated at 2022-06-22 12:39:34.177727
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'meow.py', '-t', '3.5',
                '-o', 'output.py']
    with patch('sys.stdout') as mock_stdout:
        main()
        assert messages.input_doesnt_exists(['meow.py']) in mock_stdout.getvalue()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:38.878542
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch
    with patch('sys.stdin', StringIO('2 3')):
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            result = main()
            assert result == 0
            assert mocked_stdout.getvalue() == '5\n'

# Generated at 2022-06-22 12:39:42.742750
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', 'test_file.py', '-o', 'test_file.out.py',
                '-t', '3', '-r', '.']
    assert main() == 0

# Generated at 2022-06-22 12:39:53.889233
# Unit test for function main
def test_main():

    class MockArgumentParser:
        def __init__(self, input: str, output: str, target: str, root: str,
                     debug: bool):
            self.input = input
            self.output = output
            self.target = target
            self.root = root
            self.debug = debug

    class MockArgs:
        def __init__(self, input: str, output: str, target: str, root: str,
                     debug: bool):
            self.input = input
            self.output = output
            self.target = target
            self.root = root
            self.debug = debug

    class MockArgumentParserFactory:
        def __init__(self, input: str, output: str, target: str, root: str,
                     debug: bool):
            self.mock_arguments = MockArgumentParser

# Generated at 2022-06-22 12:40:01.778167
# Unit test for function main
def test_main():
    import os
    import pytest
    import pathlib
    
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from pyback.compiler import compile_files
    from pyback.conf import init_settings
    from pyback import messages, const

    from pyback.test.resources.test_source import source_good_code, source_bad_code, source_for_startswith

    from pyback.test.resources.test_source import source_for_syntax_error, source_for_transformation_error, source_for_invalid_output

    test_dir = 'test'
    input_dir = os.path.join(test_dir, 'input')

# Generated at 2022-06-22 12:40:19.574160
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:21.141993
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:29.440187
# Unit test for function main
def test_main():
    import sys
    from io import StringIO
    args = sys.argv
    sys.argv = ['py-backwards', '-i', 'what.banana.py', '-o', '.', '-t', '2.7']
    out = StringIO()
    try:
        main()
    except SystemExit:
        pass
    sys.stdout = out
    sys.argv = args
    assert out.getvalue().strip() == "Input what.banana.py doesn't exist"

test_main()

# Generated at 2022-06-22 12:40:37.545632
# Unit test for function main
def test_main():
    # Case when 1 input
    sys.argv = ['-i', 'tests/examples/test.py',
                '-o', 'tests/examples/test.py',
                '-t', '2']

    if main() != 0:
        raise Exception('Test failed')

    # Case when several inputs
    sys.argv = ['-i', 'tests/examples/test.py', 'tests/examples/tests',
                '-o', 'tests/examples/output',
                '-t', '3']

    if main() != 0:
        raise Exception('Test failed')

    # Case when several inputs and root parameter

# Generated at 2022-06-22 12:40:41.031150
# Unit test for function main
def test_main():
    from .test_main import main as main_test
    import doctest
    doctest.testmod(main_test, optionflags=doctest.ELLIPSIS)

if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:40:41.658907
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:45.360934
# Unit test for function main
def test_main():
    assert main() == 0
    #sys.argv = [sys.argv[0], '--input', '../tests', '--output', '../tests_out', '--root', '../tests', '--target', 'py36']
    #main()

# Generated at 2022-06-22 12:40:49.084782
# Unit test for function main
def test_main():
    sys.argv = ['main.py', '-i', 'tests', '-o', 'output', '-t', 'python36', '-d', '-r']
    assert main() == 0

# Generated at 2022-06-22 12:40:58.604483
# Unit test for function main
def test_main():
    from py_backwards.compiler import compile_files
    from .conf import init_settings
    from . import const, messages, exceptions


    settings = init_settings('')
    settings.input = ['tests/data/data_py2/test2.py']
    settings.output = 'test.py'
    settings.target = 'py_2'
    settings.debug = False
    settings.root = 'tests/data'

    try:
        for input_ in settings.input:
            result = compile_files(input_, settings.output,
                                   const.TARGETS[settings.target],
                                   settings.root)
    except exceptions.CompilationError as e:
        print(messages.syntax_error(e), file=sys.stderr)
        return 1

# Generated at 2022-06-22 12:41:04.218840
# Unit test for function main
def test_main():
    from .compiler import compile_ut
    from . import utils

    input = f'{utils.get_root()}/tests/data/input/class_init.py'
    output = f'{utils.get_root()}/tests/data/output/'
    target = '3.4'
    root = f'{utils.get_root()}/tests/data'

    args = type('', (), {})()
    args.input = [input]
    args.output = output
    args.target = target
    args.root = root

    init_settings(args)
    compile_ut()


# Generated at 2022-06-22 12:41:44.827937
# Unit test for function main
def test_main():
    import py_backwards
    # args = ['-i', 'py_backwards/test_data/py36/async_func.py', '-o', 'py_backwards/test_data/py36/async_func_output.py', '-t', '3.3', '-r', 'py_backwards/test_data']
    # main(args)
    py_backwards.main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:41:48.239699
# Unit test for function main
def test_main():
    sys.argv = ['script', '-i', 'tests/sources/func.py',
                '-o', 'tests/sources/main_compiled/func.py', '-r',
                'tests/sources', '-t', '2.7']
    main()
    assert os.path.exists(sys.argv[-3] + '.pyc')
    os.remove(sys.argv[-3] + '.pyc')
    assert os.path.exists('tests/sources/main_compiled/func.py')
    os.remove('tests/sources/main_compiled/func.py')

# Generated at 2022-06-22 12:41:58.757356
# Unit test for function main
def test_main():
    argv = ["py-backwards", "-i", "tests/input", "-o", "tests/output", "-t", "2.7" ]
    main()
	# check if file has been created and has expected content
    assert(os.path.isfile('tests/output/zero_division.py'))
    f = open('tests/output/zero_division.py', 'r')
    assert(f.read() == '''def zero_division_fixture(x, y) :
    return x / y
''')
    f.close()
    # check if file has been created and has expected content
    assert(os.path.isfile('tests/output/division.py'))
    f = open('tests/output/division.py', 'r')

# Generated at 2022-06-22 12:42:02.517937
# Unit test for function main
def test_main():
    #TODO
    # Add test cases
    print("Test main")
    assert 1==1

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:03.418610
# Unit test for function main
def test_main():
    # @Implement
    pass

# Generated at 2022-06-22 12:42:04.538913
# Unit test for function main
def test_main():
    assert True == True


# Generated at 2022-06-22 12:42:07.002464
# Unit test for function main
def test_main():
    print(main())

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:07.741993
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:08.721945
# Unit test for function main
def test_main():
    r = main()
    assert r == 1

# Generated at 2022-06-22 12:42:09.197433
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:34.415147
# Unit test for function main
def test_main():
    test_target = 'backwards'
    test_input = 'tests/input_dir'
    test_input_file = 'tests/input_dir/test.py'
    test_output = 'tests/output_dir/'
    test_output_file = test_output + 'test.py'
    test_root = 'tests/input_dir'
    sys.argv = ['-i', test_input,
                '-o', test_output,
                '-t', test_target,
                '-r', test_root]
    # Test with non existing input directory
    sys.argv[2] = 'tests/bad_input'
    assert main() == 1

    # Test with existing input and non existing output directory
    sys.argv[2] = test_input
    assert main() == 1

    # Test

# Generated at 2022-06-22 12:43:38.118812
# Unit test for function main
def test_main():
    sys.argv += '-i py_backwards/test/test.py -o test_folder/new.py -t 2.7'.split()
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:43:38.697878
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:39.591701
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:47.126003
# Unit test for function main
def test_main():
    config.init_settings(['test_main.py', '-i', 'test_data/test_case1.py', '-o', 'test_data/out.py', '-t', 'python36', '-d'])
    try:
        for input_ in config.input:
            result = compiler.compile_files(input_, config.output,
                                   const.TARGETS['python36'],
                                   config.root)
    except exceptions.CompilationError as e:
        print(e, file=sys.stderr)
        return 1
    except exceptions.TransformationError as e:
        print(e, file=sys.stderr)
        return 1
    except exceptions.InputDoesntExists:
        print(e, file=sys.stderr)
        return 1

# Generated at 2022-06-22 12:43:47.944606
# Unit test for function main
def test_main():
    assert main() in (0, 1)

# Generated at 2022-06-22 12:43:48.650032
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:58.420305
# Unit test for function main
def test_main():
    import os
    import shutil
    from tempfile import mkdtemp
    from subprocess import Popen, PIPE

    #no output to stdout
    sys.stdout = open(os.devnull, 'w')

    #temporary directory
    tmp_dir = mkdtemp()
    os.chdir(tmp_dir)

    #create test file
    f = open(os.path.join(tmp_dir, 'test.py'), 'w')
    f.write('def foo(a):\n\tprint(a)')
    f.close()

    #create test directory
    os.mkdir('test_dir')
    f = open(os.path.join(tmp_dir, 'test_dir', 'test.py'), 'w')

# Generated at 2022-06-22 12:44:00.807087
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards','-i', 'source/main.py', '-o', 'out', '-t', 'python3.5', '-d', '-r', 'root']
    assert(main()) == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:44:09.161408
# Unit test for function main
def test_main():
    import io
    from contextlib import redirect_stdout

    init_settings(ArgumentParser().parse_args())

    # Test for empty input
    f = io.StringIO()
    with redirect_stdout(f):
        assert main() == 1
    assert f.getvalue() == 'Error: the following arguments are required: -i/--input, -t/--target, -o/--output\n'

    # Test for invalid target
    f = io.StringIO()
    with redirect_stdout(f):
        args = ['-i', 'test.py', '-o', '-o.py', '-t', 'abc']
        assert main(args) == 1

# Generated at 2022-06-22 12:47:27.471382
# Unit test for function main
def test_main():
    assert_raises(SystemExit, main)
    assert_raises(SystemExit, main, ['dummy.py'])
    assert_raises(SystemExit, main, ['dummy.py'], ['dummy.py'])
    assert_raises(SystemExit, main, ['dummy.py'], ['dummy.py'], ['3.6'])
    assert_raises(SystemExit, main, ['dummy.py'], ['dummy.py'], ['3.6'], ['.'])
    assert_raises(SystemExit, main, ['dummy.py'], ['dummy.py'], ['3.6'], ['.'], True)

# Generated at 2022-06-22 12:47:38.414949
# Unit test for function main
def test_main():
    import unittest.mock as mock
    import mock
    import py_backwards
    import traceback
    import sys
    import os
    import shutil

    # set the path for the mocked sys.argv
    sys.argv = ['script', '-i', 'input', '-o', 'output', '-t', '2.7', '-r', 'src']

    # catch the sys.exit() call and ignore it
    def exit_mock(*args, **kwargs):
        pass

    # mock out the sys.exit()
    with mock.patch.object(sys, 'exit', exit_mock):
        # catch the traceback
        exc_info = None
        try:
            py_backwards.main()
        except Exception as e:
            exc_info = sys.exc_info()
       

# Generated at 2022-06-22 12:47:49.077715
# Unit test for function main
def test_main():
    sys.argv[1:] = [
        '-i', 'tests/files/a.py',
        '-o', 'tests/files/out',
        '-t', '2.7',
        '-r', 'tests/files'
    ]
    assert main() == 0
    sys.argv[1:] = [
        '-i', 'tests/files/a.py',
        '-o', 'tests/files/out/a.py',
        '-t', '2.7',
        '-r', 'tests/files'
    ]
    assert main() == 0

# Generated at 2022-06-22 12:47:49.898745
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:47:55.868303
# Unit test for function main
def test_main():
    run_args = sys.argv
    sys.argv = ['python', '-i', './test_data/test_source.py', '-t', '2', '-o', './test_data/test_source_copy.py']
    assert main() == 0

    file_before = open('./test_data/test_source.py', 'r', encoding='utf8').read()
    file_after = open('./test_data/test_source_copy.py', 'r', encoding='utf8').read()

    os.remove('./test_data/test_source_copy.py')
    sys.argv = run_args

# Generated at 2022-06-22 12:47:57.620996
# Unit test for function main
def test_main():
    assert main() == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:48:08.088492
# Unit test for function main
def test_main():
    import os
    import tempfile
    init_settings(lambda: None)
    output = tempfile.mkdtemp()


# Generated at 2022-06-22 12:48:12.289946
# Unit test for function main
def test_main():
      assert main([-i, 'test\test.py', -o, 'test\test-out.py', -t, '3.5', -r, 'test']) == 1

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:48:12.865717
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:48:17.338863
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', settings.root + 'tests/input.py',
                    '-o', settings.root + 'tests/output.py',
                    '-t', '3.6',
                    '-r', settings.root + 'tests']
    settings.log_level = settings.LogLevel.DEBUG
    settings.log_to_console = True
    main()


if __name__ == '__main__':
    main()