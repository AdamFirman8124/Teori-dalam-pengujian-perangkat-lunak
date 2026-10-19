

# Generated at 2022-06-22 12:38:32.726889
# Unit test for function main
def test_main():
    sys.argv = [
        '-i', 'example/Python36Features.py',
        '-o', 'test',
        '-t', '2.7'
    ]
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:33.580062
# Unit test for function main
def test_main():
    #assert main() == 0
    print('How are you?')

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:39.338467
# Unit test for function main
def test_main():
    import os
    files = []
    for i in range(5):
        file = 'test' + str(i) + '.py'
        with open(file, 'w') as f:
            f.write('# test file\n')
            f.write('def test():\n    print(1)')
        files.append(file)
    sys.argv = [
        os.path.realpath(__file__),
        '-i', *files,
        '-o', 'output',
        '-t', '2',
        '-r', '.'
    ]
    cwd = os.getcwd()
    try:
        sys.exit(main())
    finally:
        sys.stdout.seek(0)
        output = sys.stdout.read().strip()
        assert sys.std

# Generated at 2022-06-22 12:38:46.151365
# Unit test for function main
def test_main():
    """
    Test main function
    :return:
    """
    from pytest import raises
    from io import StringIO
    from sys import stdout, stderr

    sys.stdout = None
    sys.stderr = None
    test_output = StringIO()

    sys.stdout = test_output
    sys.stderr = test_output

    with raises(SystemExit) as e:
        main(['-t', 'Python3.4', '-i', '/wrong/path/to/file', '-o', 'test_output'])
    assert str(e.value) == '1'
    assert 'Input file or folder \'/wrong/path/to/file\' doesn\'t exist' in test_output.getvalue()

    test_output = StringIO()

    sys.stdout = test_output


# Generated at 2022-06-22 12:38:52.262382
# Unit test for function main
def test_main():
    init_settings = {'input': 'input.py',
                     'output': 'output.py',
                     'target': 'python35',
                     'root': 'C:/Test/Input'}
    E = ['C:/Test/Input/input.py']
    O = ['C:/Test/Output/output.py']
    assert main(E,O) == 0

# Generated at 2022-06-22 12:38:52.880227
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:38:56.070756
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'sample/input.py', '-o', 'sample/output.py', '-t', '2.7', '-r', 'samples']
    assert main() == 0

# Generated at 2022-06-22 12:38:57.538768
# Unit test for function main
def test_main():
    """
        test for function main
    """
    assert main() == 0

# Generated at 2022-06-22 12:38:58.088585
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:39:04.155344
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'test_data/test_main.py',
                '-o', 'test_data/test_main.out.py', '-t', '2.7']
    main()
    f = open('test_data/test_main.out.py')
    assert 'def main():' in f.read()
    f.close()
    return

# Generated at 2022-06-22 12:39:23.819119
# Unit test for function main
def test_main():
    import unittest
    import os
    import shutil

    class TestCase(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            # Create files
            file_names = ['test.py', '__init__.py', 'test.pyc']
            base_dir = os.path.dirname(__file__)

# Generated at 2022-06-22 12:39:28.196155
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', './tests/test.py', '-o', './tests/test2.py', '-t', '3.5']
    assert main() == 0

# Generated at 2022-06-22 12:39:28.982156
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:35.907295
# Unit test for function main
def test_main():
    args = sys.argv
    sys.argv = sys.argv[:1]
    sys.argv.extend(['-i', 'src/test/resources/test_resources.py',
                     '-o', '/tmp/py-backwards-test/test_resources.py',
                     '-t', 'python27',
                     '-r', 'src/test/resources/'])
    result = main()
    sys.argv = args
    return result

# Generated at 2022-06-22 12:39:41.520831
# Unit test for function main
def test_main():
    unparsed = ['bla','-i','input','-o','output','-t','3.4']
    init_settings(main()[1])
    assert SETTINGS['input'] == 'input'
    assert SETTINGS['output'] == 'output'
    assert SETTINGS['target'] == '3.4'
    
    
if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:46.415954
# Unit test for function main
def test_main():
    # We need to mock sys.argv
    saved_args = sys.argv
    sys.argv = ["py-backwards", "-i", "input.py", "-o", "output.py", "-t", "2.7"]
    assert main() == 0
    sys.argv = saved_args


# Generated at 2022-06-22 12:39:53.255545
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from .conf import settings
    from . import const, messages, exceptions

    with patch.object(sys, 'argv', ['compiler.py',
                                    '--input', '.',
                                    '--output', '.',
                                    '--target', '3.5']):
        main()
        assert settings['compile']['input'] == ['.']
        assert settings['compile']['output'] == '.'
        assert settings['compile']['target'] == '3.5'



# Generated at 2022-06-22 12:39:55.524866
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-22 12:39:56.936067
# Unit test for function main
def test_main():
    # calling main function
    status = main()
    assert status == 0

# Generated at 2022-06-22 12:40:02.598233
# Unit test for function main
def test_main():
    with mock.patch.object(sys, 'argv', ['py-backwards', '-i', 'test/test_folder/test.py', '-o', 'compiled.py', '-t', '2.7', '-r', 'test/test_folder/']):
        assert main() == 0
    with mock.patch.object(sys, 'argv', ['py-backwards', '-i', 'test/test_folder/test2.py', '-o', 'compiled.py', '-t', '2.7', '-r', 'test/test_folder/']):
        assert main() == 1

# Generated at 2022-06-22 12:40:21.819145
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:22.919473
# Unit test for function main
def test_main():
    assert main() == 0


# Generated at 2022-06-22 12:40:29.244874
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '--input', 'test', '--output', 'out', '--target', '3.4', '--debug']
    assert main() == 0

    sys.argv = ['py-backwards', '--input', 'test', '--output', 'out', '--target', '18.4', '--debug']
    assert main() == 1

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-22 12:40:30.984705
# Unit test for function main
def test_main():
    assert True


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:36.849171
# Unit test for function main
def test_main():
    init_settings(ArgumentParser().parse_args(['-i', 'tests', '-o', 'test_output', '-t', 'Python2',]))
    assert main() == 0
    init_settings(ArgumentParser().parse_args(['-i', 'tests', '-o', 'test_output', '-t', 'Python2', '-r', 'tests']))
    assert main() == 0

# Generated at 2022-06-22 12:40:45.113004
# Unit test for function main
def test_main():
    from .compiler.compiler import compile_files_to_ast
    from .version import __version__

    input_ = '1 + 1'
    output = compile_files_to_ast(input_, '2.7')
    assert output == '1 + 1'

    input_ = 'a := 1'
    output = compile_files_to_ast(input_, '3.5')
    assert output == 'a = 1'

    input_ = 'a := 1'
    output = compile_files_to_ast(input_, '3.6')
    assert output == 'a := 1'


# Generated at 2022-06-22 12:40:55.121057
# Unit test for function main
def test_main():
    # No arguments raise error
    with pytest.raises(SystemExit):
        main()

    # All arguments provided but incorrect python version
    with pytest.raises(SystemExit):
        args = ['--input', '-i', '--output', '-o', '--target', '-t',
                '--debug', '-d', '--root', '-r']
        main(args)

    # All correct arguments
    args = ['--input', 'input', '--output', 'output', '--target', '3.6',
            '--debug', '-d', '--root', 'root']
    main(args)


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:41:01.409625
# Unit test for function main
def test_main():
    try:
        main()
        assert False, 'Expected exception'
    except SystemExit as e:
        assert e.code == 2
    except:
        pass
    try:
        main([])
        assert False, 'Expected exception'
    except SystemExit as e:
        assert e.code == 2
    except:
        pass
    try:
        main(['-h'])
        assert False, 'Expected exception'
    except SystemExit as e:
        assert e.code == 0
    except:
        pass
    try:
        main(['-i', './good.py'])
        assert False, 'Expected exception'
    except SystemExit as e:
        assert e.code == 2
    except:
        pass

# Generated at 2022-06-22 12:41:11.682138
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'testFiles/hello_world.py', '-o', 'test_main.out',
                    '-t', '2.7', '-d']
    assert main() == 0
    sys.argv[1:] = ['-i', 'testFiles/hello_world.py', '-o', 'test_main.out',
                    '-t', '2.7', '-r', 'testFiles']
    assert main() == 0
    sys.argv[1:] = ['-i', 'testFiles/hello_world.py', '-o', 'test_main.out',
                    '-t', '2.7', '-d', '-r', 'testFiles']
    assert main() == 0

# Generated at 2022-06-22 12:41:16.770887
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit) as main_exit:
        main()
    assert main_exit.type == SystemExit
    assert main_exit.value.code == 2

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:04.621069
# Unit test for function main
def test_main():
    class Args:
        'Fake args object for test_main'
        def __init__(self, input_, output, target, root='/'):
            self.input = [input_]
            self.output = output
            self.target = target
            self.root = root
            self.debug = True

    try:
        main()
    except:
        assert True
    try:
        main(Args('nofile', '', '3.3'))
    except:
        assert True

    try:
        main(Args('nofile', '', '3.3'))
    except exceptions.InputDoesntExists:
        assert True

    try:
        main(Args('tests', 'tests/results', '3.3'))
    except exceptions.InvalidInputOutput:
        assert True


# Generated at 2022-06-22 12:42:13.822656
# Unit test for function main
def test_main():
    import os
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        shutil.copytree('tests/compiler', '%s/compiler' % (temp_dir,))
        sys.argv = [sys.argv[0]] + '-t 2.7 -i %s/compiler/module -o ' \
                                  '%s/output'.split() + [temp_dir]
        main() == 0
        assert os.path.exists('%s/output/compiler/module.py' % (temp_dir,))


if __name__ == "__main__":
    sys.exit(main())

# Generated at 2022-06-22 12:42:23.860075
# Unit test for function main
def test_main():
    init()
    """Should print syntax error"""
    # input_ = "for i in range(10):\n    print(i)\nprint(i)"
    # output = StringIO()
    # sys.stdout = output
    # main(input_, "main.py")
    # assert sys.stdout != output.getvalue()
    """Should print syntax error"""
    sys.argv = sys.argv + ["-i", "test/sample_code/simple.py",
                           "-o", "test/test_code/output.py",
                           "-t", "2.7",
                           "-r", "/home/user/"]
    for input_ in sys.argv[1:]:
        output = StringIO()
        sys.stdout = output
        main()

# Generated at 2022-06-22 12:42:35.717449
# Unit test for function main
def test_main():
    from . import utils
    from .compiler import compile_files
    from .exceptions import CompilationError, TransformationError, InputDoesntExists, InvalidInputOutput
    from . import const

    utils.get_args = lambda: MagicMock(input=['test_data/test1.py', 'test_data/test2.py'],
                                       output='tmp',
                                       debug=False,
                                       target='py36',
                                       root='test_data/')

    compile_files = MagicMock(side_effect=lambda input, output, target, root: [(input, output, False)])
    print = MagicMock()
    main()

# Generated at 2022-06-22 12:42:45.486118
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from io import StringIO
    import contextlib

    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    sys.path.insert(0, '/')

# Generated at 2022-06-22 12:42:46.996206
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-22 12:42:49.506693
# Unit test for function main
def test_main():
    # description
    args = ["-i","input","-o","output",
            "-t","target",
            "-d",
            "-r","root"]
    
    assert main() == 0

# Generated at 2022-06-22 12:42:59.985557
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

# Generated at 2022-06-22 12:43:04.023623
# Unit test for function main
def test_main():
    import subprocess
    import os

    try:
        os.remove('my.py')
    except:
        pass

    subprocess.check_output(['python', '-m', 'pb', '-o', 'my.py', '-t', 'python36', 'my.py'])
    os.remove('my.py')

# Generated at 2022-06-22 12:43:10.763041
# Unit test for function main
def test_main():
    # test main with valid args
    sys.argv = ['py-backwards', '-t', '3.5', 
                '-i', './tests/examples/', 
                '-o', './tests/output', 
                '-r', './tests/examples/'
                '-d']
    assert main() == 0

    # test main with wrong target
    sys.argv = ['py-backwards', '-t', '3.6', 
                '-i', './tests/examples/', 
                '-o', './tests/output', 
                '-r', './tests/examples/'
                '-d']
    assert main() == 1

    # test main with wrong input

# Generated at 2022-06-22 12:44:50.385657
# Unit test for function main
def test_main():
    import subprocess
    from .tests.functions.compile_errors import *
    from .tests.functions.transform_errors import *
    from .tests.functions.input_doesnt_exist import *
    from .tests.functions.permission_error import *
    from .tests.functions.input_output_error import *
    from .tests.functions.compilation_ok import *
    import os

    os.environ['PYCHARM_HOSTED'] = '1'
    
    files = [
        compile_errors,
        transform_errors,
        input_doesnt_exist,
        permission_error,
        input_output_error,
        compilation_ok,
    ]

    for file in files:
        file.main()


# Generated at 2022-06-22 12:44:59.581862
# Unit test for function main
def test_main():
    from py_backwards.arguments import mock_args
    from .helpers import pytest_ensure_clean_output
    from .conf import settings
    settings.DEBUG = True
    test_args = mock_args('py_backwards\tests\test_resources\test.py',
                          'py_backwards\tests\test_resources\test2.py',
                          'py_backwards\tests\test_resources\out')
    test_args.target = const.TARGETS.py34.name
    main()
    pytest_ensure_clean_output('py_backwards\tests\test_resources\test2.py')
    test_args.target = const.TARGETS.py35.name
    main()

# Generated at 2022-06-22 12:45:00.178234
# Unit test for function main
def test_main():
    assert main == main

# Generated at 2022-06-22 12:45:00.880712
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-22 12:45:01.463309
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:45:11.063069
# Unit test for function main
def test_main():
    # Test 1: Input is a file
    input_ = 'file.py'
    output = 'out.py'
    target = '2.7'
    sys.argv = ['command', '-i', input_, '-t', target, '-o', output]
    assert main() == 0
    assert os.path.exists(output)
    assert os.path.isfile(output)
    os.remove(output)
    # Test 2: Input is a folder
    input_ = 'folder'
    output = 'out'
    target = '2.7'
    sys.argv = ['command', '-i', input_, '-t', target, '-o', output]
    assert main() == 0
    assert os.path.exists(output)
    assert os.path.isdir(output)

# Generated at 2022-06-22 12:45:21.407914
# Unit test for function main
def test_main():
    # Testing for Python3.6
    sys.argv = [
        'py-backwards',
        '../',
        '../build/',
        '-t',
        'py36'
    ]
    main()
    py36 = os.path.exists('build')
    shutil.rmtree('build')
    assert py36 == True

    # Testing for Python3.5
    sys.argv = [
        'py-backwards',
        '../',
        '../build/',
        '-t',
        'py35'
    ]
    main()
    py35 = os.path.exists('build')
    shutil.rmtree('build')
    assert py35 == True

    # Testing for Python3.4

# Generated at 2022-06-22 12:45:22.067890
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:45:27.215120
# Unit test for function main
def test_main():
    """
    Test passed arguments.
    """
    args = 'py-backwards -i test_py2.py -o test_py2_result.py -t 2'
    path = 'py_backwards/'
    sys.argv = args.split(' ')
    if path not in sys.path:
        sys.path.append(path)
    assert main() == 0

# Generated at 2022-06-22 12:45:27.735313
# Unit test for function main
def test_main():
    assert main() == 0