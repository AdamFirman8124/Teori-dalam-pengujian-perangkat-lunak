

# Generated at 2022-06-22 12:38:28.616464
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:38:29.916086
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-22 12:38:34.554997
# Unit test for function main
def test_main():
    sys.argv = ['compile.py', '--input', 'immagini', '--output', 'out', '--target', '2.7', '--root', '.', '--debug']
    main()
    
    
if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:37.666704
# Unit test for function main
def test_main():
    assert main('-i ./test/input/test.py -o ./test/output/test.py -t 2.7'.split()) == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:47.901284
# Unit test for function main
def test_main():
    from io import StringIO
    import sys
    from . import const
    from .conf import init_settings

    saved_out, saved_err = sys.stdout, sys.stderr

# Generated at 2022-06-22 12:38:54.648803
# Unit test for function main
def test_main():
    sys.argv = ["py-backwards.py", "-i", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tests", "fixtures", "sample.py")), "-o", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tests", "fixtures", "sample2.py")), "-t", "3.5", "-d"]
    main()

# Generated at 2022-06-22 12:38:59.447578
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards.py', '-i', 'tests/sources/test_main.py', '-o',
        '/tmp/test_main.py', '-t', '3.5', '-r', '/home/python-backwards/']

    assert main() == 0


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 12:39:01.984440
# Unit test for function main
def test_main():

    import pytest

    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-22 12:39:06.900089
# Unit test for function main
def test_main():
    from . import test_util
    args = ['--input', 'test_code/test.py', '--output', 'test_code/out.py',
            '--target', 'Python3']
    sys.argv = sys.argv[:1] + args
    main()
    test_util.compare_files('test_code/out.py', 'test_code/test_main.py')

# Generated at 2022-06-22 12:39:16.723066
# Unit test for function main
def test_main():
    # test success compilation
    with patch('sys.argv',
               ['py-backwards', '-i', 'test/example.py', '-o', 'out.py', '-t',
                '2.7', '-r', '~/']):
        assert main() == 0
    with patch('sys.argv',
               ['py-backwards', '-i', 'test/example.py', '-o', 'out.py', '-t',
                '3.6', '-r', '~/']):
        assert main() == 0

# Generated at 2022-06-22 12:39:38.505618
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i ', 'tests/test.py', '-o ', 'test_out.py',
                '-t ', 'python2', '-r ', 'tests']
    result = main()
    assert result == 0

# Generated at 2022-06-22 12:39:42.425120
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'tests/test_input', '-o', 'tests/test_output',
                '-t', '3.6', '-r', 'tests/test_input']
    assert main() == 0

# Generated at 2022-06-22 12:39:45.184745
# Unit test for function main
def test_main():
    from .test.test_main import create_parser, parse_args
    parser = create_parser()
    args = parse_args(parser)
    main(args)

# Generated at 2022-06-22 12:39:46.554756
# Unit test for function main
def test_main():
    assert main() == 0, "Failed to execute main function"


# Generated at 2022-06-22 12:39:52.930261
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'test/test_data.py', '-o', 'test/out.py',
                '-t', 'py35']
    assert main() == 0
    sys.argv = ['', '-i', 'test/test_data.py', '-o', 'test/out.py',
                '-t', 'py27']
    assert main() == 1

# Generated at 2022-06-22 12:39:53.606642
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:03.143359
# Unit test for function main
def test_main():
    import sys
    import os
    import unittest


    class Test(unittest.TestCase):
        def setUp(self):
            self.target = 'python-2.7'
            self.output = '../temp/'

        def tearDown(self):
            files = os.listdir(self.output)
            for file in files:
                os.remove(self.output + file)

        def test_permissions(self):
            sys.argv = [sys.argv[0], '-i', 'helloworld.py', '-o', '/', '-t', self.target]
            assert main() == 1


# Generated at 2022-06-22 12:40:10.960952
# Unit test for function main
def test_main():
    from .test_compiler import test_compile_files
    from .conf import settings
    from .messages import info, compilation_result
    from . import const

    target = const.TARGETS[settings.target]
    for input_ in settings.input:
        result = test_compile_files(input_, settings.output, target,
                                    settings.root)
        info(compilation_result(result))

if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:40:12.067561
# Unit test for function main

# Generated at 2022-06-22 12:40:18.037678
# Unit test for function main
def test_main():
    args = [
        '-i', 'tests/test_tree/demo/__init__.py',
        '-o', 'tests/test_tree/demo_3to3.5/__init__.py',
        '-t', 'python3.5'
    ]
    assert main(args) == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:56.298223
# Unit test for function main
def test_main():
  assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:41:06.202112
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

# Generated at 2022-06-22 12:41:09.773151
# Unit test for function main
def test_main():
    from .globals import _args

    args = _args
    args.input = './test/test_input'
    args.output = './test/test_output'
    args.target = 'python27'

    assert(main() == 0)

# Generated at 2022-06-22 12:41:20.287639
# Unit test for function main
def test_main():
    import pytest
    # No args
    with pytest.raises(SystemExit):
        main()
    # No input
    with pytest.raises(SystemExit):
        main('-o', 'a.py', '-t', '3.5')
    # Target is not specified
    with pytest.raises(SystemExit):
        main('-i', 'a.py', '-o', 'a.py')
    # Target is not supported
    with pytest.raises(SystemExit):
        main('-i', 'a.py', '-o', 'a.py', '-t', '3.9')
    # Not implemented
    with pytest.raises(Exception):
        main('-i', 'a.py', '-o', 'a.py', '-t', '3.6')


# Generated at 2022-06-22 12:41:27.586770
# Unit test for function main
def test_main():
    sys.argv = sys.argv[:1]
    sys.argv.extend(['--input', 'tests/py_sample.py',
                     '--output', 'out.py', '--target', '3',
                     '--root', 'tests/'])
    assert(main() == 0)
    sys.argv = sys.argv[:1]
    sys.argv.extend(['--input', 'tests/py_sample.py',
                     '--output', 'out.py', '--target', '3'])
    assert(main() == 0)
    sys.argv = sys.argv[:1]
    sys.argv.extend(['--input', 'tests/py_sample.py',
                     '--output', 'out.py', '--target', '3'])


# Generated at 2022-06-22 12:41:38.982496
# Unit test for function main
def test_main():
    input_list = ["tests/test_files/3.6/target.py"]
    output_path = "tests/output_files/3.6"
    target = "2.7"
    root = "tests"
    # Функция main должна возвращать значение 0
    assert main() == 0
    # Проверяем наличие компилированного файла после компиляции

# Generated at 2022-06-22 12:41:44.250821
# Unit test for function main
def test_main():
    raise NotImplementedError


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(messages.user_interrupt, file=sys.stderr)
        sys.exit(1)

# Generated at 2022-06-22 12:41:48.065082
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', '1.py', '2.py', '-o', 'out', '-t', 'py35']
    assert main() == 0



# Generated at 2022-06-22 12:41:48.599536
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:41:53.240919
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'source/index.py', '-o', 'output/index.py', '-t', '3.5', '-r', 'source', '-d' ]
    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:29.637378
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:32.111995
# Unit test for function main
def test_main():
  assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:33.572595
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:43.254906
# Unit test for function main
def test_main():
    # Case: Successful compilation
    sys.argv = ['py-backwards', '-i', 'main.py', '-o', 'output.py', '-t', '3.5']
    assert main() == 0

    # Case: Wrong input
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.5']
    assert main() == 1

    # Case: Wrong output
    sys.argv = ['py-backwards', '-i', 'main.py', '-o', 'output.py', '-t', '3.6']
    assert main() == 1

    # Case: Wrong target

# Generated at 2022-06-22 12:42:44.632557
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-22 12:42:47.359777
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:47.989827
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:51.135705
# Unit test for function main
def test_main():
    result = main(['-i', 'src/py_backwards.py', '-o', 'test_folder/test_file',
                   '-t', '3.5', '-r', 'src', '-d'])
    assert result == 0

# Generated at 2022-06-22 12:42:52.450545
# Unit test for function main
def test_main():
    _main = main()
    assert _main == 0

# Generated at 2022-06-22 12:42:53.341368
# Unit test for function main
def test_main():
    pass  # TODO: put tests here

# Generated at 2022-06-22 12:44:26.670706
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:44:27.908066
# Unit test for function main
def test_main():
    print(main())


# Generated at 2022-06-22 12:44:31.018895
# Unit test for function main
def test_main():
    with patch('compiler.compile_files', return_value=3) as mock_compile:
        assert main() == 0
        mock_compile.assert_called_once()


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:44:32.326036
# Unit test for function main
def test_main():
    """ Tests main function. """
    #TODO implement
    ...

# Generated at 2022-06-22 12:44:40.840828
# Unit test for function main
def test_main():
    target = 'target'
    output = 'output'
    files = ['file1','file2','file3']
    root = '/'
    args = ['-i', ' '.join(files), '-o', output, '-t', target, '-r', root]
    with patch('pybackwards.main.init_settings') as init_settings_mock,\
         patch('pybackwards.main.compile_files') as compile_files_mock, \
         patch('sys.argv', args), \
         patch('sys.stderr.write') as stderr_mock, \
         patch('sys.stdout.write') as stdout_mock:
        init_settings_mock.return_value = None
        compile_files_mock.return_value = 3
        assert main() == 0

# Generated at 2022-06-22 12:44:41.397445
# Unit test for function main
def test_main():
    assert main() != 0

# Generated at 2022-06-22 12:44:44.315313
# Unit test for function main
def test_main():
    """
    Testing function main()
    """
    assert main() == 0

# Generated at 2022-06-22 12:44:47.628753
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '--input', 'tests/sample.py', '--output', '123.py', '--target', 'py34', '-d', '-v']
    assert main() == 0

# Generated at 2022-06-22 12:44:55.598975
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards', '-i', 'fixtures/sample_1.py', '-o',
        '_run/sample_1.py', '-t', '2.7', '-r', 'fixtures/']
    assert main() == 0
    sys.argv = [
        'py-backwards', '-i', 'fixtures/sample_1.py', '-o',
        '_run/sample_1.py', '-t', '2.7']
    assert main() == 0
    sys.argv = [
        'py-backwards', '-i', 'fixtures/sample_1.py', '-o',
        '_run/sample_1.py', '-t', '2.7']
    assert main() == 0
    sys.arg

# Generated at 2022-06-22 12:44:56.203400
# Unit test for function main
def test_main():
    assert main() == 0