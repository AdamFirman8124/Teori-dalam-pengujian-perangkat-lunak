

# Generated at 2022-06-22 12:38:28.888735
# Unit test for function main
def test_main():
    assert(True == True)


# Generated at 2022-06-22 12:38:35.781845
# Unit test for function main
def test_main():
    from . import conf
    import os.path
    import shutil

    root = os.path.abspath('tests')
    input = os.path.join(root, 'test_project')
    output = os.path.join(root, 'out')
    root = os.path.join(root, 'test_project')
    target = '2.7'

    shutil.rmtree(output, ignore_errors=True)
    assert main(['-i', input, '-o', output, '-r', root, '-t', target]) == 0
    assert os.path.exists(output)
    assert conf.settings.failed_files == conf.settings.total_files
    print('Main test passed')


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:38.065347
# Unit test for function main
def test_main():
    assert main() == 0
    assert main() == 0

if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:38:39.431410
# Unit test for function main
def test_main():
    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:38:40.090231
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:38:41.839098
# Unit test for function main
def test_main():
    saved_argv = sys.argv
    assert main() == 0
    sys.argv = saved_argv

# Generated at 2022-06-22 12:38:46.134646
# Unit test for function main
def test_main():
    assert main() is 0

if __name__ == '__main__':
    sys.exit(main())


__all__ = (
    'compile_files',
    'exceptions',
    'messages',
    'main',
)

# Generated at 2022-06-22 12:38:57.121972
# Unit test for function main
def test_main():
    sys.argv = [
        sys.argv[0],
        '-i', 'test_data/input/enum.py',
        '-o', 'test_data/output_test',
        '-t', '3.4',
        '-r', 'test_data/input',
        '-d'
    ]

    assert 0 == main()

    sys.argv = [
        sys.argv[0],
        '-i', 'test_data/input/doesnt_exists.py',
        '-o', 'test_data/output_test',
        '-t', '3.4',
        '-r', 'test_data/input',
        '-d'
    ]

    assert 1 == main()


# Generated at 2022-06-22 12:38:57.770007
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:00.855548
# Unit test for function main
def test_main():
    result = main()
    assert result in [0, 1]


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:19.172317
# Unit test for function main
def test_main():
    from tempfile import TemporaryFile, TemporaryDirectory
    from textwrap import dedent
    from unittest import TestCase
    from unittest.mock import patch, MagicMock
    import shutil
    import os
    import contextlib
    
    
        
    class TestMain(TestCase):
        def setUp(self):
            self.tmp_dir = TemporaryDirectory()
            self.test_file = TemporaryFile(dir=self.tmp_dir.name)
            self.output_file = TemporaryFile(dir=self.tmp_dir.name)
        
        def tearDown(self):
            self.test_file.close()
            self.output_file.close()
            self.tmp_dir.cleanup()
        
        
        def test_main__correct_case(self):
            test_file = self.test

# Generated at 2022-06-22 12:39:19.825453
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-22 12:39:25.312016
# Unit test for function main
def test_main():
    from .conf import TARGET_PYTHON_VERSION
    from .conf import ROOT_PATH
    from .conf import OUTPUT_FOLDER

    comp = main(['-i', 'examples/test.py', '-o', OUTPUT_FOLDER,
          '-t', TARGET_PYTHON_VERSION, '-r', ROOT_PATH])
    assert(comp == 0)

# Generated at 2022-06-22 12:39:36.739236
# Unit test for function main
def test_main():
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main

# Generated at 2022-06-22 12:39:37.734573
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:38.334296
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:42.895174
# Unit test for function main
def test_main():
    reset_args(sys.argv)
    sys.argv = ['py-backwards', '-i', 'test/input', '-o', 'test/output', '-t', 'python37', '-r', 'test/input/']

    result = main()
    assert result == 0


# Generated at 2022-06-22 12:39:45.236100
# Unit test for function main
def test_main():
    print("\nTesting main...")
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:45.847913
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:39:56.888769
# Unit test for function main
def test_main():
    with patch('argparse.ArgumentParser.parse_args',
               return_value=MagicMock(input=['input.py'], output='output.py',
                                      target='3.5', root='', debug=True)):
        with patch('__main__.init_settings'), \
                patch('__main__.compile_files',
                      side_effect=[(1, 0, 0)]):
            assert main() == 0


# Generated at 2022-06-22 12:40:20.555430
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards',
        '-i', './tests/test_data/source',
        '-o', '.temp',
        '-t', '3.4',
        '-d'
    ]
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:27.045785
# Unit test for function main
def test_main():
    from .compiler import compile_files
    from .conf import init_settings

    parser = main()
    input_ = parser.input
    output_ = parser.output
    target_ = parser.target
    root_ = parser.root
    debug_ = parser.debug

    init_settings(parser)

    result = compile_files(input_, output_, const.TARGETS[target_], root_)
    print(messages.compilation_result(result))

# Generated at 2022-06-22 12:40:29.572227
# Unit test for function main
def test_main():
    init_settings(['-o', 'file.out', '-t', '3.5', '-i', 'file.in'])
    assert main() == 0

# Generated at 2022-06-22 12:40:30.557294
# Unit test for function main
def test_main():
    assert main() == 1

test_main()

# Generated at 2022-06-22 12:40:31.505088
# Unit test for function main
def test_main():
    assert main() == 0


# Generated at 2022-06-22 12:40:33.625210
# Unit test for function main
def test_main():
    print('test_main')
    return


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:44.134249
# Unit test for function main
def test_main():
    if __name__ == "main":
        import sys
        import io
        import os

        sys.argv = ['py-backwards', '-i', 'tests/fixtures/input.py',
                    '-o', 'tests/fixtures/output.py', '-t', '3.6', '-r',
                    'tests/fixtures/', '-d']

        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        assert os.path.isfile('tests/fixtures/output.py')
        assert captured_output.getvalue() \
            == 'tests/fixtures/input.py -> tests/fixtures/output.py\n'
        os.remove('tests/fixtures/output.py')


# Generated at 2022-06-22 12:40:44.990111
# Unit test for function main
def test_main():
    assert main() == 0


# Generated at 2022-06-22 12:40:46.251586
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:47.880860
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 12:41:33.450408
# Unit test for function main
def test_main():
    # No arguments
    try:
        sys.argv = []
        main()
        assert 0
    except SystemExit as e:
        assert not e.code
    # Failed compilation
    try:
        sys.argv = ['py-backwards', '-i', 'test/data/raise_syntax_error.py',
                    '-o', 'test/data/failed.py', '-t', '2.7', '-r', '.']
        main()
        assert 0
    except SystemExit as e:
        assert e.code
    # Successful compilation

# Generated at 2022-06-22 12:41:43.905201
# Unit test for function main
def test_main():
    import tempfile
    import os
    import shutil
    from io import StringIO
    from contextlib import redirect_stdout
    import pytest

    tempdir = tempfile.mkdtemp()
    input_dir = os.path.join(tempdir,'input')
    output_dir = os.path.join(tempdir,'output')
    input_temp = os.path.join(input_dir,'test.py')
    output_temp = os.path.join(output_dir,'test.py')

    def teardown():
        shutil.rmtree(tempdir)

    def get_result():
        f = StringIO()

# Generated at 2022-06-22 12:41:47.856892
# Unit test for function main
def test_main():
    assert main() == 0
    assert main() == 1
    assert main() == 1
    assert main() == 1
    assert main() == 1

if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:41:58.295387
# Unit test for function main
def test_main():
    sys.argv = [
        sys.argv[0],
        '-i', 'test/test_files/f-string_test.py',
        '-o', 'test/output/',
        '-t', '3.5',
        '-r', 'test/test_files',
        '-d'
    ]
    assert main() == 0

    sys.argv = [
        sys.argv[0],
        '-i', 'test/test_files/not-exists.py',
        '-o', 'test/output/',
        '-t', '3.5',
        '-r', 'test/test_files',
        '-d'
    ]
    assert main() == 1


# Generated at 2022-06-22 12:42:07.647946
# Unit test for function main
def test_main():
    from .conf import Settings
    from .test.test_py_backwards import tmpdir
    import os
    import pytest
    pytest.importorskip("colorama")
    with tmpdir.as_cwd():
        with pytest.raises(SystemExit):
            main()
        if Settings.verbose:
            print("tmpdir:", os.getcwd())
        with pytest.raises(SystemExit):
            main()
        open("test_main.py", "w").write("""if 5:
    def myfunc():
        print("test")
myfunc()
""")
        main()
        # TODO: more tests

# Generated at 2022-06-22 12:42:17.088303
# Unit test for function main
def test_main():
    import os
    import json
    import difflib
    import shutil

    input_path = './test/test_module/test_input.py'
    output_path = './test_output.py'
    root_path = './test/test_module'
    test_input_path = './test/test_module/test_input.py'

# Generated at 2022-06-22 12:42:17.747863
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:42:28.348264
# Unit test for function main
def test_main():
    with mock.patch('sys.argv', ['py-backwards', '-i',
                                 'tests/test_sources/test1.py',
                                 '-o', 'test_sources_result/test1.py',
                                 '-t', '3.2']):
        assert 0 == main()
        with mock.patch('sys.argv', ['py-backwards', '-i',
                                     'tests/test_sources/test1.py',
                                     '-o', 'test_sources_result/test1.py',
                                     '-t', '5.6']):
            assert 1 == main()

# Generated at 2022-06-22 12:42:32.317416
# Unit test for function main
def test_main():
    sys.argv[-2:] = ['--input=tests/input.py', '--output=tests/output.py',
                     '--target=py36', '--root=tests']
    assert main() == 0

# Generated at 2022-06-22 12:42:35.764980
# Unit test for function main
def test_main():
    args = ['--input', 'test/data/version_test.py', '--output', 'test/output',
            '--target', '2.7', '--debug']
    if main(args) != 0:
        raise RuntimeError

# Generated at 2022-06-22 12:44:17.892807
# Unit test for function main
def test_main():
    sys.argv = "py_backwards -i ./sample_files/1.py -o ./sample_files -t 3.5 -r ./sample_files/output.py".split()
    sys.exit = lambda code: code
    assert main() == 1

    sys.argv = "py_backwards -i ./sample_files/2.py -o ./sample_files -t 3.5 -r ./sample_files/output.py".split()
    sys.exit = lambda code: code
    assert main() == 1

    sys.argv = "py_backwards -i ./sample_files/sample.py -o ./sample_files -t 3 -r ./sample_files/output.py".split()
    sys.exit = lambda code: code
    assert main() == 1


# Generated at 2022-06-22 12:44:20.863066
# Unit test for function main
def test_main():
    assert main(["files/example.py", "files/example2.py"], "files/output.py",
                "2.7", "files") == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:44:26.292393
# Unit test for function main
def test_main():
    from . import mock_main_argparse
    from .compiler import compile_files
    from .conf import init_settings, settings

    init_settings(mock_main_argparse())
    result = compile_files('some_file', 'some_output', 'some_target',
                           'some_root')
    assert result == 0

# Generated at 2022-06-22 12:44:34.743523
# Unit test for function main

# Generated at 2022-06-22 12:44:38.506628
# Unit test for function main
def test_main():
    argv = [sys.argv[0], '-i', 'test/test.py', '-o', 'out.py', '-t',
            '2.7', '-r', 'test']
    assert main() == 0
    assert main(argv) == 0

# Generated at 2022-06-22 12:44:49.244701
# Unit test for function main
def test_main():
    saved_argv = sys.argv
    saved_stdout = sys.stdout

# Generated at 2022-06-22 12:44:58.760844
# Unit test for function main
def test_main():
    import contextlib
    from io import StringIO
    from tempfile import TemporaryDirectory
    from .compiler import compile_file

    with TemporaryDirectory() as tmpdir:
        file_ext = 'py'
        filename = 'test.py'
        input_file_path = '/'.join((tmpdir, filename))
        with open(input_file_path, 'w') as f:
            f.write('test')


# Generated at 2022-06-22 12:45:05.117232
# Unit test for function main
def test_main():
    src = 'test_files'
    target = 'test_files_out'
    version = '3.6'
    args = {
        'input': src,
        'target': version,
        'output': target
    }
    sys.argv.extend(['-i', src, '-o', target, '-t', version])
    res = main()
    assert res == 0
    assert os.path.exists(target)
    assert os.path.isdir(target)

# Generated at 2022-06-22 12:45:05.665183
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-22 12:45:06.636037
# Unit test for function main
def test_main():
    assert type(main()) == int