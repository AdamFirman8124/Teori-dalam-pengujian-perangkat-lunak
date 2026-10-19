

# Generated at 2022-06-22 12:38:40.509470
# Unit test for function main
def test_main():
    '''
    Tests if main function works properly
    '''
    sys.argv = ['', '-i', 'tests/inputs/class_deco.py', '-o', '/tmp/class_deco.py', '-t', '3.6', '-r', 'tests/inputs']
    with open('/tmp/class_deco.py', 'r') as file1:
        result = file1.read()
    with open('/tmp/class_deco', 'w') as file2:
        result2 = file2.write(result)
    assert result == result2

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:43.709958
# Unit test for function main
def test_main():
    assert main() == 0
    assert main('-i test/test_data/test.py -o test/test_data/test.py'
                ' -t 3.6 -r test/test_data -d') == 0

# Generated at 2022-06-22 12:38:48.730788
# Unit test for function main
def test_main():
    class args:
        debug = False
        input = ['/home/andrei/projects/py_backwards/py_backwards/tests/test.py']
        output = '/home/andrei/projects/py_backwards/py_backwards/tests/test2.py'
        target = '2.7'
        root = None

    init_settings(args)
    result = main()
    assert result == 0

# Generated at 2022-06-22 12:38:50.615373
# Unit test for function main
def test_main():
    assert main() != 0
    assert main() != 1

# Generated at 2022-06-22 12:39:01.623595
# Unit test for function main
def test_main():
    with patch('argparse.ArgumentParser.parse_args') as mock:
        mock.return_value = argparse.Namespace(
            input=None, output='-', target='3.8',
            debug=None, root=None)
        assert main() == 0

        mock.return_value = argparse.Namespace(
            input=None, output='-', target='2.7',
            debug=None, root=None)
        assert main() == 1

        mock.return_value = argparse.Namespace(
            input=None, output='-', target='3.8',
            debug=None, root=None)
        assert main() == 0

        mock.return_value = argparse.Namespace(
            input=None, output='-', target='3.8',
            debug=None, root=None)

# Generated at 2022-06-22 12:39:02.216446
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:39:11.046252
# Unit test for function main
def test_main():
    """
    A test for the command-line interface
    """
    import os
    import tempfile
    import shutil

    def call_main(*args):
        old_argv = sys.argv
        sys.argv = ['py-backwards'] + list(args)
        try:
            return main()
        finally:
            sys.argv = old_argv

    dirpath = tempfile.mkdtemp()

# Generated at 2022-06-22 12:39:14.002850
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'example.py', '-o', 'example.py']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:24.582336
# Unit test for function main

# Generated at 2022-06-22 12:39:32.852940
# Unit test for function main
def test_main():
    args = ['./main.py', '-i', './tests/assets/test.py', '-o',
    './tests/assets/test_output.py', '-t', '2.7', '-r', './tests/assets']
    main(args)
    assert filecmp.cmp('./tests/assets/test.py',
                                      './tests/assets/test_output.py')

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:52.803153
# Unit test for function main
def test_main():
    import sys
    import os
    from unittest.mock import patch
    from io import StringIO
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(script_dir, '..'))
    from tests.fixture import FileIOMock

    args_1 = ['py-backwards', '-i', 'tests/fixture/test_input',
              '-o', 'tests/fixture/test_output', '-t', '2',
              '--root', 'tests/fixture']
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.abspath(os.path.join(script_dir, '..'))



# Generated at 2022-06-22 12:39:57.451322
# Unit test for function main
def test_main():
    arguments = ["./tests/py_files/file.py", "-i", "./tests/files/", "-o", "./tests/py_files/", "-t", "2.7", "-r", "./tests/files", "-d"]
    if __name__ == '__main__':
        sys.argv = arguments
        main()

# Generated at 2022-06-22 12:40:06.339381
# Unit test for function main
def test_main():
    from tempfile import TemporaryDirectory
    from os import listdir
    import subprocess

    input_dir = TemporaryDirectory()
    output_dir = TemporaryDirectory()
    with open(f'{input_dir.name}/hello.py', 'w') as f:
        f.write('\n'.join([
            'def hello():',
            '    print("hello")',
            'hello()'
        ]))

    # An error will be raised when compiling this file and the compilation
    # should stop
    with open(f'{input_dir.name}/hello2.py', 'w') as f:
        f.write('\n'.join([
            'def hello():',
            '    print("hello")',
            'hello()',
            'hello1()'
        ]))

# Generated at 2022-06-22 12:40:06.997411
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:08.988359
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:20.559860
# Unit test for function main
def test_main():
    import unittest
    import unittest.mock

    class FakeArgparse(object):
        def __init__(self, input, output, target, root, debug):
            self.input = input
            self.output = output
            self.target = target
            self.root = root
            self.debug = debug

    class MainTest(unittest.TestCase):
        @unittest.mock.patch('py_backwards.main.ArgumentParser')
        def test_main__without_exception(self, argparse):
            argparse.parse_args.return_value = FakeArgparse(['asdf'], 'zxcv',
                                                            '2.7', '.', False)


# Generated at 2022-06-22 12:40:25.115174
# Unit test for function main
def test_main():
    input_ = 'test_data/test_folder'
    output = 'test_data/output_folder'
    target = '3.5'
    root = 'test_data'
    debug = False

    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:28.935463
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-t', '3.6', '-i', 'tests/test_files/']
    assert main() == 0

# Generated at 2022-06-22 12:40:35.911850
# Unit test for function main
def test_main():
    # Test no arguments
    print('Testing with no arguments ...')
    unit_testing_main([], 0)

    # Test invalid arguments
    print('Testing with invalid arguments ...')
    unit_testing_main(['-i', '1', '-o', '2', '-t', '3.6', '-r', '123'], 2)

    # Test valid arguments
    print('Testing with valid arguments ...')
    unit_testing_main(['-i', '1', '-o', '2', '-t', '3.6'], 0)



# Generated at 2022-06-22 12:40:36.538772
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:58.228405
# Unit test for function main
def test_main():
    sys.argv.extend(['-i', 'input_file', '-o', 'output_file', '-t', '3.6',
                     '-r', 'sources_root', '-d'])

    if main() != 0:
        raise RuntimeError('main() failed')


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:58.665844
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:59.277175
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:41:04.093989
# Unit test for function main
def test_main():
    sys.argv=['py-backwards', '-i', 'tests/sources/for.py', 'tests/sources/for.py', '-o', 'tests/sources/for.py', '-t', '2.7', '-r', 'tests/sources']
    assert main() == 0, 'Test failed'
        
test_main()

# Generated at 2022-06-22 12:41:08.400003
# Unit test for function main
def test_main():
    module = sys.modules['__main__']
    sys.argv = [sys.argv[0], '-i', 'input_file', '-o', 'output_file',
                '-t', '3.5', '-r', 'root', '-d']
    module.main()

# Generated at 2022-06-22 12:41:09.874018
# Unit test for function main
def test_main():
    args = main.__annotations__
    assert(args['return'] == int)

# Generated at 2022-06-22 12:41:20.373991
# Unit test for function main
def test_main():
    input_ = 'input'
    output = 'output'
    target = 'python2'
    root = 'root'
    input_ = test_main.__closure__[0].cell_contents
    output = test_main.__closure__[1].cell_contents
    target = test_main.__closure__[2].cell_contents
    root = test_main.__closure__[3].cell_contents
    input_ = test_main.__closure__[0].cell_contents
    output = test_main.__closure__[1].cell_contents
    target = test_main.__closure__[2].cell_contents
    root = test_main.__closure__[3].cell_contents

# Generated at 2022-06-22 12:41:27.627123
# Unit test for function main

# Generated at 2022-06-22 12:41:39.031084
# Unit test for function main
def test_main():
    class TestException(Exception):
        pass
    class TestArgs():
        """
        args mock for main() tests
        """
        def __init__(self, target, input, output, root, debug):
            self.target = target
            self.input = input
            self.output = output
            self.root = root
            self.debug = debug
    sys.argv[1:] = '-t py35 -i input/test.py -o output/ -r /root/'.split(' ')
    args = parser.parse_args()
    init_settings(args)

    # if input doesn't exists the error should be:
    # IOError: [Errno 2] No such file or directory: 'input/test.py'
    # and exit code should be 1

# Generated at 2022-06-22 12:41:45.573275
# Unit test for function main
def test_main():
    from . import test_compiler
    from . import test_conf
    from . import test_messages
    test_compiler.test_compile_files()
    test_conf.test_init_settings()
    test_messages.test_syntax_error()


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:11.940279
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards',
        '-i', 'tests/example.py',
        '-o', 'output/example.py',
        '-t', '2.7',
        '-r', 'tests/example'
    ]
    assert main() == 0
    sys.argv = [
        'py-backwards',
        '-i', 'tests/example.py',
        '-o', 'output/example',
        '-t', '2.7',
        '-r', 'tests/example'
    ]
    assert main() == 1
    sys.argv = [
        'py-backwards',
        '-i', 'tests/example.py',
        '-o', 'output/example.py'
    ]
    assert main() == 1

# Generated at 2022-06-22 12:42:12.956987
# Unit test for function main
def test_main():
    assert main() != 0

# Generated at 2022-06-22 12:42:19.749696
# Unit test for function main
def test_main():
    class FakeArguments:
        def __init__(self):
            self.input = 'tests/data/test_main.py'
            self.output = 'fake'
            self.target = 'python27'
            self.debug = False
            self.root = None

    with pytest.raises(exceptions.CompilationError):
        main(FakeArguments())


if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:42:26.486901
# Unit test for function main
def test_main():
    test_path = "../tests/test_main.py"
    test_compile_path = "../tests/backwards"
    sys.argv = ['py-backwards', '-i', test_path, '-o', test_compile_path, '-t', "2.7", '-r', '../']
    main()
    assert os.path.exists(test_compile_path)

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:37.608418
# Unit test for function main
def test_main():
    try:
        main()
        assert False
    except SystemExit as e:
        # the required arguments are missing
        assert e.code == 2

    try:
        main(['this-does-not-exist.py', 'this-does-not-exist-2.py'])
        assert False
    except SystemExit as e:
        # input does not exist
        assert e.code == 1

    try:
        main(['this-does-not-exist.py', 'this-does-not-exist-2.py'],
             './out',
             '3.6')
        assert False
    except SystemExit as e:
        # input does not exist
        assert e.code == 1


# Generated at 2022-06-22 12:42:48.777396
# Unit test for function main
def test_main():
    try:
        os.remove('files/__init__.py')
    except OSError:
        pass
    os.rename('files/_init.py', 'files/__init__.py')
    sys.argv[1:] = ['--input', 'files',
                    '--output', 'output',
                    '--target', '3.5',
                    '-r', 'files']
    assert (main() == 0)
    os.remove('files/__init__.py')
    os.rename('files/_init.py', 'files/__init__.py')

# Generated at 2022-06-22 12:42:51.180896
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'test', '-o', 'test', '-t', '3.6', '-d']
    assert main() == 0

# Generated at 2022-06-22 12:42:52.188641
# Unit test for function main
def test_main():
    assert callable(main)

# Generated at 2022-06-22 12:42:53.133672
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:57.884199
# Unit test for function main
def test_main():
    original = sys.argv
    sys.argv = ['', '-i', 'tests/test_sources/test_input',
                '-t', '3.6', '-o', 'tests/test_sources/test_output']
    result = main()
    sys.argv = original
    return result

# Generated at 2022-06-22 12:43:46.946841
# Unit test for function main
def test_main():
    test_input = "testinput.py"
    test_output = "testoutput.py"
    test_target = "2.7"
    test_root = "."
    assert main() == 1
    assert main(test_input, test_output, test_target) == 0

# Generated at 2022-06-22 12:43:47.481346
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:57.336361
# Unit test for function main
def test_main():
    init_settings(None)
    args = None
    try:
        result = compile_files('../test_files/test_folder', '../test_files/test_folder/output', const.TARGETS[args.target], args.root)
    except exceptions.CompilationError as e:
        print(e.err)
    except exceptions.TransformationError as e:
        print(e.err)
    except exceptions.InputDoesntExists:
        print(messages.input_doesnt_exists(args.input))
    except exceptions.InvalidInputOutput:
        print(messages.invalid_output(args.input, args.output))
    except PermissionError:
        print(messages.output_open_error(args.output))

# Generated at 2022-06-22 12:43:58.878035
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:59.460408
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:44:04.078677
# Unit test for function main
def test_main():
    argv = sys.argv
    sys.argv = ['pybackwards.py','-i', 'input', '-o', 'output', '-t', '3.5', '-r', 'root', '-d']
    assert(main() == 0)
    sys.argv = argv

# Generated at 2022-06-22 12:44:04.674662
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:44:07.458133
# Unit test for function main
def test_main():
    print("Testing function main ...", end="")
    args = main.__text_signature__
    assert args == "(self: py_backwards.__main__.Parser)", "main function has an invalid signature"
    print("Passed.")


# Generated at 2022-06-22 12:44:09.286707
# Unit test for function main
def test_main():
    assert main() in [0, 1]

# Generated at 2022-06-22 12:44:12.308271
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit as e:
        assert e.code == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:45:42.107276
# Unit test for function main
def test_main():
    try:
        result = main(["-t", "p32", "-i", "test.py", "-o", "test(1).py"])
    except SystemExit as e:
        assert e.code == 1

# Generated at 2022-06-22 12:45:45.176747
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:45:54.761459
# Unit test for function main
def test_main():
    filename = tempfile.mktemp()
    with open(filename, 'w') as f:
        f.write('from dataclasses import dataclass\n')
        f.write('from typing import List\n')
        f.write('from pprint import pprint\n')
        f.write('from enum import Enum\n')
        f.write('import pathlib\n')
        f.write('from .a import a\n')
        f.write('from . import b\n')
        f.write('from .b import c\n')
        f.write('from b import d\n')
        f.write('@dataclass\n')
        f.write('class A:\n')
        f.write('    x: int\n')
        f.write('    y: int\n')
       

# Generated at 2022-06-22 12:45:58.997934
# Unit test for function main
def test_main():
    with unittest.mock.patch('sys.argv', ['py-backwards', '-i', 'a', 'b', '-o', 'c', '-t', '3.5']):
        main()

# Generated at 2022-06-22 12:46:09.003365
# Unit test for function main
def test_main():
    SYSARGV = sys.argv
    sys.argv = ['py-backwards.py', '-i', 'test_file.py', '-o', '-', '-t', 'py36']

    assert main() == 1
    sys.argv = ['py-backwards.py', '-i', 'wrong_file.py', '-o', '-', '-t', 'py35']

    assert main() == 1

    sys.argv = ['py-backwards.py', '-i', 'tests/test_file.py', '-o', '-', '-t', 'py35']

    assert main() == 0

    sys.argv = ['py-backwards.py', '-i', 'tests/test_file.py', '-o', '-', '-t', 'py3']

# Generated at 2022-06-22 12:46:10.737263
# Unit test for function main
def test_main():
    args = ['py-backwards']
    with pytest.raises(SystemExit):
        main(args)


# Generated at 2022-06-22 12:46:21.127987
# Unit test for function main
def test_main():
    def _run(argv):
        with patch('sys.exit') as sx:
            with patch('sys.argv', argv):
                main()
            return sx.call_args[0][0]

    argv = ['prog', '-i', '/input', '-o', '/output', '-t', '2.7', '-r', '/root']
    result = _run(argv)
    assert result == 0

    argv = ['prog', '-i', '/input', '-o', '/output', '-t', '2.7']
    result = _run(argv)
    assert result == 0

    argv = ['prog', '-i', '/input', '-o', '/output', '-t', '2.7', '-d']

# Generated at 2022-06-22 12:46:26.420148
# Unit test for function main
def test_main():
    from .conf import settings
    from . import compiler

    assert main() == 0
    assert (settings.input == ['-i'])
    assert settings.output == ['-o']
    assert settings.target == '-t'
    assert settings.root == ['-r']
    assert settings.debug == True

# Generated at 2022-06-22 12:46:35.096644
# Unit test for function main
def test_main():
    import unittest
    import os
    import shutil

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            current_path = os.path.dirname(os.path.abspath(__file__))
            self.test_folder = os.path.join(current_path, 'test_folder')
            self.assertTrue(os.path.exists(self.test_folder))
            self.out_folder = os.path.join(self.test_folder, 'out')

        def tearDown(self):
            if os.path.exists(self.out_folder):
                shutil.rmtree(self.out_folder)


# Generated at 2022-06-22 12:46:36.267018
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    main()