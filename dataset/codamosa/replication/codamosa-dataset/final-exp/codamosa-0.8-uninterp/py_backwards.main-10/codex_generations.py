

# Generated at 2022-06-22 12:38:35.004341
# Unit test for function main
def test_main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    try:
        result = main()
    except SystemExit:
        result = 0
    assert result == 0

# Generated at 2022-06-22 12:38:40.449860
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

# Generated at 2022-06-22 12:38:46.552482
# Unit test for function main

# Generated at 2022-06-22 12:38:57.768222
# Unit test for function main
def test_main():
    # Testing compilation without errors
    sys.argv = ["py-backwards", "-i", "test/test_files/test.py",
                "-o", "test/test_files/test_output.py",
                "-t", "2", "-r", "test/test_files"]
    assert main() == 0
    # Testing compilation with errors
    sys.argv = ["py-backwards", "-i", "test/test_files/test_error.py",
                "-o", "test/test_files/test_error_output.py",
                "-t", "2", "-r", "test/test_files"]
    assert main() == 1
    # Testing compilation with errors

# Generated at 2022-06-22 12:39:03.838896
# Unit test for function main
def test_main():
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = StringIO()

    assert main() == 1

    stdout.write(sys.stdout.getvalue())
    sys.stdout = stdout
    sys.stderr = stderr


if __name__ == '__main__':
    main()
    from . import logger
    logger.disable()

# Generated at 2022-06-22 12:39:07.292916
# Unit test for function main
def test_main():
    #args = ['-i', 'py-backwards', '-o', '/tmp/py-backwards-res.py', '-t', '3.5']
    #sys.argv[1:] = args
    #main()

    assert main() == 0

# Generated at 2022-06-22 12:39:09.579374
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'input.py', '-o', 'output.py', '-t', '3.5']
    assert main() == 0

# Generated at 2022-06-22 12:39:13.363617
# Unit test for function main
def test_main():
    import os
    import shutil
    from .tests.utils import create_source_code
    from .conf import settings

    folder = './tests/temp/'
    output = './tests/temp/out/'
    os.makedirs(folder, exist_ok=True)

    create_source_code(folder)

    main([ '-i', folder, '-o', output, '-t', '3.5'])
    assert settings.output_folder == output
    assert settings.input_folder == folder
    shutil.rmtree(folder)
    shutil.rmtree(output)

# Generated at 2022-06-22 12:39:14.255895
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-22 12:39:24.814251
# Unit test for function main
def test_main():
    import unittest as ut
    import colorama
    import os
    import shutil
    import subprocess
    import tempfile
    import sys

    class TestFunctions(ut.TestCase):

        def setUp(self):
            def output():
                return colorama.Style.BRIGHT + colorama.Fore.GREEN + \
                    colorama.Back.BLACK
            sys.stdout.write("\n")
            sys.stdout.flush()
            self.tmp_dir1 = tempfile.mkdtemp()
            self.tmp_dir2 = tempfile.mkdtemp()
            self.tmp_file_name1 = 'tmp_file.txt'
            self.tmp_file_name2 = 'tmp_file2.txt'

# Generated at 2022-06-22 12:39:43.503552
# Unit test for function main
def test_main():
    import pytest
    from argparse import Namespace
    from .conf import SETTINGS
    from . import const

    def create_args(input_: str, output: str, target: str, root: str,
                    debug: bool = False):
        return Namespace(input=[input_], output=output, target=target,
                         root=root, debug=debug)

    assert main() == 1  # Not all parameters passed
    assert main(create_args('/fdsafds/fdsafds', '/fdsafds/fdsafdsa', '3', '')) == 1  # First file doesn't exists
    assert main(create_args('/fdsafds/fdsafds', '/fdsafds/fdsafdsa', '3', '', False)) == 1  # Second file doesn't exists
    assert main

# Generated at 2022-06-22 12:39:45.439093
# Unit test for function main
def test_main():
    assert main() == 1

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:49.514248
# Unit test for function main
def test_main():
    # This use case is only possible when you run py-backwards directly
    # by command line, because py-backwards is an executable file,
    # so it's not required to install py-backwards
    try:
        main()
    except SystemExit:
        pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:50.197681
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:00.932667
# Unit test for function main
def test_main():
    from . import test_utils
    from .test_utils import MockArgumentParser, MockSettings
    import sys
    import runpy
    from io import StringIO
    from .conf import Settings

    def _mock_init_settings(args):
        Settings.debug = args.debug

    Settings.load_settings = MockSettings
    settings = Settings()
    settings.debug = False
    ArgumentParser.__init__ = MockArgumentParser

    settings.target = 'python27'
    settings.input = ['test.py']
    settings.output = 'out.py'
    settings.root = 'root'
    init_settings = runpy.run_path('pybackwards/compiler.py')['init_settings']
    init_settings(_mock_init_settings, args=settings)

# Generated at 2022-06-22 12:40:07.731657
# Unit test for function main
def test_main():
    from .conf import settings
    test_args = ArgumentParser('test', description='')
    test_args.add_argument('-i', '--input', type=str, nargs='+', required=True,
                           help='input file or folder')
    test_args.add_argument('-o', '--output', type=str, required=True,
                           help='output file or folder')
    test_args.add_argument('-t', '--target', type=str,
                           required=True, choices=const.TARGETS.keys(),
                           help='target python version')
    test_args.add_argument('-r', '--root', type=str, required=False,
                           help='sources root')

# Generated at 2022-06-22 12:40:19.217611
# Unit test for function main
def test_main():
    old_sys_argv = sys.argv
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'out.py', '-t', '3.5']
    assert main() == 1
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'out.py', '-t', '3.6']
    assert main() == 1
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'out.py', '-t', '3.7']
    assert main() == 1
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'out.py', '-t', '3.8']

# Generated at 2022-06-22 12:40:22.975300
# Unit test for function main
def test_main():
    assert main() == 0
    assert main(["test.py", "test2.py"], "output.py", "3.5") == 0
    assert main(["test.py", "test2.py"], "output.py", "2.7") == 0

# Generated at 2022-06-22 12:40:23.618333
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:24.314823
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:43.901758
# Unit test for function main
def test_main():
    assert main() == 0


if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:40:45.484751
# Unit test for function main
def test_main():
    assert main([]) == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:46.045110
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-22 12:40:50.507539
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards.py', '-i', './tests/data/examples/example.py', '-o', './example.py', '-t', '2.7', '-r', './tests/data/examples']
    assert 0 == main()

# Generated at 2022-06-22 12:40:58.327724
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'tests/input.py', '-o',
                'tests/output.py', '-t', '2.7', '-d']
    test_result = main()
    assert(test_result == 0)
    sys.argv = ['py-backwards', '-i', 'tests/input.py', '-o',
                'tests/output.py', '-t', '2.6', '-d']
    test_result = main()
    assert(test_result == 1)


if __name__ == "__main__":
    main()

# Generated at 2022-06-22 12:41:00.006813
# Unit test for function main
def test_main():
    """
    >>> main(['-i','../test/test_source', '-o', '../test/test_output', '-t', '2.7', '-r', '../test'])
    """

# Generated at 2022-06-22 12:41:05.430786
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'test/gold/nested', '-o', 'test/out',
                '-t', '3.5', '-r', 'test']
    assert main() == 0
    sys.argv = ['py-backwards', '-i', 'test/gold/nested', '-o', 'test/gold',
                '-t', '3.5', '-r', 'test']
    assert main() == 1
    sys.argv = ['py-backwards', '-i', 'test/gold/nested', '-o', 'test/',
                '-t', '3.5', '-r', 'test']
    assert main() == 1

# Generated at 2022-06-22 12:41:11.589838
# Unit test for function main
def test_main():
    input_folder = 'input'
    output_folder = 'output'
    output_file = 'output/a.txt'
    target = '2.7'
    args = ['-i', input_folder, '-o', output_folder, '-t', target]

    assert main() == 0

    with open(output_file, 'r') as f:
        assert f.read() == 'foo'

    import shutil

    shutil.rmtree(output_folder)

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:41:13.040282
# Unit test for function main
def test_main():
    # Set up

    # Assertion

    # Return
    return None

# Generated at 2022-06-22 12:41:16.080009
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit) as exit_e:
        main()
    assert exit_e.value.code == 2


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:02.623948
# Unit test for function main
def test_main():
    import pytest
    import subprocess
    #test if invalid argument result in usage
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2
    #test if it runs compilation
    result = subprocess.check_output(['python3', '-m', 'py_backwards', '-i', 'tests/source/', '-o', 'tests/output/', '-t', '3.5', '-r', 'tests/source/'], universal_newlines=True)
    assert result == 'compilation finished with 0 errors\n'

# Generated at 2022-06-22 12:42:08.973391
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'test_files\\test_main.py',
                    '-o', 'test_files\\out.py',
                    '-t', '3.5']
    assert main() == 0


if __name__ == '__main__':
    try:
        value = main()
    except KeyboardInterrupt:
        print('\n' + messages.interrupt(), file=sys.stderr)
        value = 1
    sys.exit(value)

# Generated at 2022-06-22 12:42:12.586058
# Unit test for function main
def test_main():
    sys.argv = sys.argv[:1]
    sys.argv.append('-i')
    sys.argv.append('py-backwards/tests/test_data/non_empty_folder')
    sys.argv.append('-o')
    sys.argv.append('py-backwards/tests/test_output')
    sys.argv.append('-t')
    sys.argv.append('python2')

    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:13.454348
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:23.390325
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards', '-i', 'mypy/mypy/test_data/package/test_module.py',
        '-i', 'mypy/mypy/test_data/package/test_module.txt', '-o',
        'mypy/mypy/test_data/package/test_module-2.py', '-t', '2']
    assert main() == 0


# Generated at 2022-06-22 12:42:35.208622
# Unit test for function main
def test_main():
    # Basic test
    sys.argv = ['py-backwards',
                '-r', 'root',
                '-o', 'out',
                '-t', '3.3',
                '-i', 'source1', 'source2']
    assert main() == 0

    # Test that exception is raised when no target is given
    sys.argv = ['py-backwards',
                '-o', 'out',
                '-i', 'source1', 'source2']
    assert main() != 0

    # Test that exception is raised when no output is given
    sys.argv = ['py-backwards',
                '-t', '3.3',
                '-i', 'source1', 'source2']
    assert main() != 0

    # Test that exception is raised when no input is given
    sys.arg

# Generated at 2022-06-22 12:42:39.795580
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'tests/test_src',
                '-o', 'tests/test_out',
                '-t', '2.7']
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:42.206163
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:42:42.817482
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:53.317726
# Unit test for function main
def test_main():
    # Test command line parser
    sys.argv = ["py-backwards", "-i", "main.py", "-o", "output.py",
                "-t", "python36"]
    main()
    assert settings.input == ["main.py"]
    assert settings.output == "output.py"
    assert settings.target == "python36"
    assert settings.debug == False

    # Test settings init
    settings.input = settings.output = settings.target = settings.debug = None
    args = Namespace(input=["main.py"], output="output.py", target="python36",
                     debug=False, root=None)
    init_settings(args)
    assert settings.input == ["main.py"]
    assert settings.output == "output.py"
    assert settings.target == "python36"

# Generated at 2022-06-22 12:44:25.780414
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:27.818157
# Unit test for function main
def test_main():
    assert main() == 1

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:44:32.687580
# Unit test for function main
def test_main():
    sys.argv = sys.argv[:1] + ['-i', 'tests/test_files/test.py',
                               '-o', 'tests/test_files/test.bak.py',
                               '-t', 'py35',
                               '-r', 'tests/test_files/',
                               '-d']
    assert main() == 0
    #assert False

# Generated at 2022-06-22 12:44:40.955994
# Unit test for function main
def test_main():
    import os
    import shutil
    import tempfile
    import uuid
    import random
    import subprocess
    import filecmp
    import os.path

    def create_random_file(path, lines = None):
        with open(path, 'w') as f:
            if lines is None:
                k = random.randint(2, 10)
            else:
                k = lines
            for i in range(k):
                f.write(str(uuid.uuid4()))
                f.write('\n')

    def folder_name(x):
        l = []
        for i in range(random.randint(2, 10)):
            l.append(str(uuid.uuid4()))
        path = os.path.join(*l)
        if x == 'p':
            os

# Generated at 2022-06-22 12:44:49.313698
# Unit test for function main
def test_main():
    args = ArgumentParser('', description='')
    args.add_argument = lambda *args, **kwargs: True
    args.parse_args = lambda: argparse.Namespace(target=const.TARGETS['3.5'],
                                                 debug=True,
                                                 root='',
                                                 input=['input'],
                                                 output='output')
    settings.DEBUG = True

    try:
        assert main() == 0
    except AssertionError:
        return False
    return True


if __name__ == "__main__":
    print(main())

# Generated at 2022-06-22 12:44:50.655532
# Unit test for function main
def test_main():
    # What to test?
    assert True

# Generated at 2022-06-22 12:44:53.723639
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'tests/sources/classes.py', '-o', 'tests/sources/classes.out.py', '-t', '2.7']
    sys.exit(main())

# Generated at 2022-06-22 12:44:56.457461
# Unit test for function main
def test_main():
    args = ['--input', '/path/to/python/file', '--output', '/path/to/output', '--target', '3.5']
    assert main() == 0

# Generated at 2022-06-22 12:45:04.267561
# Unit test for function main
def test_main():
    sys.argv = ['/home/miroslav/PycharmProjects/py-backwards/py-backwards/pybackwards.py', '-i', '/home/miroslav/PycharmProjects/py-backwards/tests/test_compile_cases/3.6.py', '-o', '/home/miroslav/PycharmProjects/py-backwards/tests/test_compile_cases/3.6_out.py', '-t', '2.6']

    if __name__ == '__main__':
        main()

# Generated at 2022-06-22 12:45:14.657283
# Unit test for function main
def test_main():
    import os
    import pytest
    import py_backwards.conf
    from py_backwards.tests.utils import create_file, remove_file
    import subprocess
    import shutil

    # Disable debug output
    py_backwards.conf.enable_debug_output(False)

    # Try to compile some file that can't be found by compiler
    with pytest.raises(exceptions.InputDoesntExists):
        main()

    # Try to compile some valid file but output is invalid
    with pytest.raises(exceptions.InvalidInputOutput):
        main('-i', '__init__.py', '-o', 'test_output')

    # Compile valid file and try to use invalid output path