

# Generated at 2022-06-22 12:38:33.531268
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:38:43.343610
# Unit test for function main

# Generated at 2022-06-22 12:38:47.758950
# Unit test for function main
def test_main():
    input_ = 'test'
    output = 'test'
    target = '2.7'
    root = 'test'
    debug = True
    assert main(input_, output, target, root, debug) == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:48.491311
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:38:50.710328
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit as e:
        assert(e.code == 0)

# Generated at 2022-06-22 12:38:51.936770
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:02.256188
# Unit test for function main
def test_main():
    # preparing input args
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', type=str, nargs='+', required=True,
                        help='input file or folder')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='output file or folder')
    parser.add_argument('-t', '--target', type=str,
                        required=True, choices=const.TARGETS.keys(),
                        help='target python version')
    parser.add_argument('-r', '--root', type=str, required=False,
                        help='sources root')
    parser.add_argument('-d', '--debug', action='store_true', required=False,
                        help='enable debug output')
    # setting arguments of correct type
    args

# Generated at 2022-06-22 12:39:03.205147
# Unit test for function main
def test_main():
    assert main() == 0 # Successful execution

# Generated at 2022-06-22 12:39:12.117849
# Unit test for function main
def test_main():

    # Unit test for arguments without -o/--output
    parser = ArgumentParser(
        'py-backwards',
        description='Python to python compiler that allows you to use some '
                    'Python 3.6 features in older versions.')
    parser.add_argument('-i', '--input', type=str, nargs='+', required=True,
                        help='input file or folder')
    parser.add_argument('-t', '--target', type=str,
                        required=True, choices=const.TARGETS.keys(),
                        help='target python version')
    parser.add_argument('-r', '--root', type=str, required=False,
                        help='sources root')
    parser.add_argument('-d', '--debug', action='store_true', required=False,
                        help='enable debug output')

# Generated at 2022-06-22 12:39:14.304848
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:33.337123
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:39:33.953421
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:37.102124
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'test_input', '-o', 'test_output', '-r', 'test_input', '-t', '2.7']
    assert main() == 0

# Generated at 2022-06-22 12:39:47.028780
# Unit test for function main
def test_main():
    old_sys_argv = sys.argv

    sys.argv = 'py-backwards -i test/test_file/test -o test/compiled -t python2.7'.split()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

    sys.argv = 'py-backwards -t python2.7 -i test/test_file/test -o test/compiled'.split()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

    sys

# Generated at 2022-06-22 12:39:57.487303
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards',
                '-i', './tests/data/py36/dict_comprehension.py',
                '-o', './tests/data/py36/dict_comprehension_compiled.py',
                '-t', '2.7',
                '-d']
    assert main() == 0

    sys.argv = ['py-backwards',
                '-i', './tests/data/py36/dict_comprehension.py',
                '-o', './tests/data/py36/dict_comprehension_compiled.py',
                '-t', '3.3',
                '-d']
    assert main() == 0


# Generated at 2022-06-22 12:40:04.922975
# Unit test for function main
def test_main():
    sys.argv.append('-i')
    sys.argv.append('/home/marin/Documents/py-backwards/test.py')
    sys.argv.append('-o')
    sys.argv.append('/home/marin/Documents/py-backwards/test.py')
    sys.argv.append('-t')
    sys.argv.append('CPython37')
    sys.argv.append('-r')
    sys.argv.append('/home/marin/Documents/py-backwards')
    sys.argv.append('-d')
    main()

# Generated at 2022-06-22 12:40:16.523766
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

# Generated at 2022-06-22 12:40:17.130815
# Unit test for function main
def test_main():
    return

# Generated at 2022-06-22 12:40:17.738545
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:22.434500
# Unit test for function main
def test_main():
    main()
    main(['-i', '/py-backwards/tests/resources/Resources/code', '-o', '/py-backwards/tests/resources/results', '-t', '2.7'])

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:45.999383
# Unit test for function main
def test_main():
    try:
        argv = ['-i', 'input', '-o', 'output', '-t', '3', '-r', 'root']
        main(argv)
    except Exception:
        print('Unit test failed')
        sys.exit(1)
    print('Unit test successful')
    sys.exit(0)

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:46.653037
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:40:50.474398
# Unit test for function main
def test_main():
    args = {
        'input': ['../tests/parser/geo.py'],
        'output': '../tests/parser/output',
        'target': '3.4',
        'root': '../tests/parser'
    }
    assert main(args) == 0


# Generated at 2022-06-22 12:40:51.084724
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:40:55.039151
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'test_file_1.py', '-o', 'output.py',
                '-t', 'python36', '-r', 'test_file_1.py']
    assert main() == 0

# Generated at 2022-06-22 12:40:56.291847
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        assert main() == 0

# Generated at 2022-06-22 12:40:56.940771
# Unit test for function main
def test_main():
    assert main() != 0

# Generated at 2022-06-22 12:41:00.881265
# Unit test for function main
def test_main():
    # Test for valid input and output
    args = ['py-backwards', '-t', 3.2, '-i', 'test/test_files/test.py', '-o', 'test/output/test.py']
    output = main(args)
    assert output == 0

# Generated at 2022-06-22 12:41:06.638072
# Unit test for function main
def test_main():
    try:
        import pytest
        assert pytest.main([__file__, '-v', '-s']) == 0
    except ImportError as e:
        print('To run unit test please install pytest')

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:41:07.199531
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:41:53.524772
# Unit test for function main
def test_main():
    from click.testing import CliRunner
    from pathlib import Path
    from tempfile import NamedTemporaryFile
    from .cli import cli

    runner = CliRunner()

    # Test for not-existing input
    result = runner.invoke(cli, ['--input', 'not-existing',
                                 '--output', 'output',
                                 '--target', 'py27'])
    assert result.exit_code == 1

    # Test for multiple inputs
    result = runner.invoke(cli, ['--input', 'tests/data/basic.py',
                                 'tests/data/reformatted.py',
                                 '--output', 'output',
                                 '--target', 'py27'])
    assert result.exit_code == 1

    # Test for directory input

# Generated at 2022-06-22 12:42:02.977699
# Unit test for function main
def test_main():
    from tempfile import TemporaryDirectory
    import os, shutil
    output_dir = TemporaryDirectory()
    f = open(os.path.join(output_dir.name, 'input.py'), 'w')
    f.write('1 + 1')
    f.close()

    try:
        assert main(['-i', 'input.py', '-o', 'output.py', '-t', '2.7'],
                    output_dir.name) == 0
        assert os.path.exists(os.path.join(output_dir.name, 'output.py'))
    except AssertionError as e:
        print(e)
    finally:
        shutil.rmtree(output_dir.name)

# Generated at 2022-06-22 12:42:11.288824
# Unit test for function main
def test_main():
    # Test function with invalid arguments
    sys.argv = ['argv[0]', 'invalidArgument', '-o', 'test/test.py']
    assert main() == 2

    # Test function with invalid target
    sys.argv = ['argv[0]', '-i', 'test/test.py', '-o', 'test/test.py', '-t',
                'invalidTarget']
    assert main() == 2

    # Test function with invalid input
    sys.argv = ['argv[0]', '-i', 'invalidInput', '-o', 'test/test.py', '-t',
                'python2.7']
    assert main() == 1

    # Test function with invalid output

# Generated at 2022-06-22 12:42:22.462178
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', '../test/test_folder', '-o', '../test/output_folder', '-t', '2.7', '-root', '../test/']
    assert main() == 0
    sys.argv = ['py-backwards', '-i', '../test/test_folder', '-o', '../test/output_folder', '-t', '2.7', '-root', '../test/']
    main()
    assert len(os.listdir('../test/output_folder')) == len(os.listdir('../test/test_folder'))

# Generated at 2022-06-22 12:42:26.785459
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', '_test.py', '-o', '_test_out', '-t', '2.7']
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:32.818749
# Unit test for function main
def test_main():
    input_ = '../input'
    output_ = '../output'
    target_ = 'python3.6'
    args = '--input {} --output {} --target {}'.format(input_,output_,target_)
    sys.argv = sys.argv[0].split()
    sys.argv.extend(args.split())
    assert main() == 0

# Generated at 2022-06-22 12:42:38.832827
# Unit test for function main
def test_main():
    # Test with invalid number of arguments
    try:
        main()
    except SystemExit as e:
        assert e.code == 2

    # Test with invalid input
    try:
        main(['-i', '.', '-o', 'abc', '-t', 'py35'])
    except SystemExit as e:
        assert e.code == 1

# Test for function main
test_main()

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:42.173669
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.6', '-d']
    main()

# Generated at 2022-06-22 12:42:52.810531
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch
    from . import conf

    def get_main_result():
        output = StringIO()
        with patch('sys.stdout', new=output):
            main()
        return output.getvalue()

    def get_main_result_with_args(args):
        output = StringIO()
        with patch('sys.stdout', new=output), \
             patch.object(conf, 'settings', new=args):
            main()
        return output.getvalue()


# Generated at 2022-06-22 12:42:56.156004
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'tests/fib.py', '-o', 'output', '-t', '2.7.13',
                    '-r', 'tests']
    assert main() == 0

# Generated at 2022-06-22 12:44:38.158233
# Unit test for function main
def test_main():
    from .compiler import compile_code
    from .structures import CompilationResult
    from . import exceptions

    class Arguments:
        def __init__(self, input, output, target):
            self.input = input
            self.output = output
            self.target = target
            self.root = None
            self.debug = True

    class InputOutput:
        def __init__(self, text):
            self.text = text
            self.counter = 0
            self.input = None

        def write(self, text):
            self.input = text.decode('utf-8')

    # Test 1: simple code

# Generated at 2022-06-22 12:44:48.952617
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch

    with patch('sys.stderr', new=StringIO()) as fake_stderr:
        main()
        assert fake_stderr.getvalue().strip() == 'py-backwards: error: the following arguments are required: -i/--input, -o/--output, -t/--target\n'

    with patch('sys.stdout', new=StringIO()), patch('sys.stderr', new=StringIO()):
        args = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '35']
        main(args)
        assert sys.stderr.getvalue().strip() == 'No transformations performed.'

# Generated at 2022-06-22 12:44:55.468991
# Unit test for function main
def test_main():
    """
    >>> main()
    usage: py-backwards [-h] -i INPUT [INPUT ...] -o OUTPUT -t TARGET
                        [-r ROOT] [-d]
    py-backwards: error: the following arguments are required: -i/--input, -o/--output, -t/--target
    1

    """

try:
    from doctest import testmod
    testmod()
except ImportError:
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:45:05.845255
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

# Generated at 2022-06-22 12:45:06.415895
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:45:07.420621
# Unit test for function main
def test_main():
    result = main()
    assert result == 0

# Generated at 2022-06-22 12:45:08.050444
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:45:15.782675
# Unit test for function main
def test_main():
    test_inputs = [
        ("""-i input.py -o output.py -t 3.6""", 0),
        ("""-i input.py -o output.py -t 3.6""", 0),
        ("""-i input.py -o output.py -t 3.1""", 1),
        ("""-i input.py -o output.py -t 3.8""", 1),
    ]
    for input_data, answer in test_inputs:
        if main(input_data.split()) == answer:
            print("test passed")
        else:
            print("test failed")



# Generated at 2022-06-22 12:45:16.986942
# Unit test for function main
def test_main():
    init_settings(ArgumentParser())
    assert main() == 0

# Generated at 2022-06-22 12:45:24.854648
# Unit test for function main
def test_main():
    sys.argv = [
        '',
        '-i', 'C:\\Users\\jakub\\source\\py-backwards\\test_data\\src',
        '-o', 'C:\\Users\\jakub\\source\\py-backwards\\result',
        '-t', '3.5',
        '-r', 'C:\\Users\\jakub\\source\\py-backwards\\test_data\\src',
        '-d'
    ]

    main()


if __name__ == '__main__':
    main()