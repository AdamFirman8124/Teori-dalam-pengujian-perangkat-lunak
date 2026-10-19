

# Generated at 2022-06-22 12:38:41.844674
# Unit test for function main
def test_main():
    from . import conf, const

    class Args:
        input = [__file__]
        output = 'output.py'
        target = 'py33'
        debug = False

    sys.argv = [__file__, '-i', __file__, '-o', 'output.py', '-t', 'py33',
                '-r', 'sources']
    init_settings(Args)
    assert conf.settings.debug == Args.debug
    assert conf.settings.target == const.TARGETS[Args.target]
    assert sys.argv == [__file__]

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:51.671191
# Unit test for function main
def test_main():
    from .parser import parse_file
    from . import transform, ast_transform

    @transform.transformation
    def transformer(node):
        if isinstance(node, ast.FunctionDef):
            new_node = copy.deepcopy(node)
            new_node.name = 'A'
            return new_node

    ast_transform.add('test', transformer)

    if 'tests' not in sys.path:
        sys.path.insert(0, 'tests')
    sys.argv = [sys.executable, '--input', 'test_main.py', '--output',
                'tests/test_main_output.py', '--target', '2']
    main()

    # Test if 'A' is real name
    tree = parse_file('tests/test_main_output.py')
    assert tree.body

# Generated at 2022-06-22 12:38:58.128421
# Unit test for function main
def test_main():
    class Args():
        def __init__(self):
            self.input = ['py-backwards/tests/test_compiler.py']
            self.output = 'py-backwards/tests/out.py'
            self.root = None
            self.target = '3.5'
            self.debug = False
    args = Args()
    main()
    assert args.output == 'py-backwards/tests/out.py'

# Generated at 2022-06-22 12:39:02.029773
# Unit test for function main
def test_main():
    try:
        assert main() == 0
    except AssertionError as e:
        assert false, 'test_main() has failed'

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:03.494035
# Unit test for function main
def test_main():
    assert main() == 0 #TODO should it not throw exception?

# Generated at 2022-06-22 12:39:04.429338
# Unit test for function main
def test_main():
    # TODO
    assert 1 == 1

# Generated at 2022-06-22 12:39:05.729851
# Unit test for function main
def test_main():
    args = main.__annotations__
    assert args['return'] == int

# Generated at 2022-06-22 12:39:15.275105
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', 'test/resources/valid.py', '-o', '.', '-t', 'python2', '-r', 'test/resources']
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

    assert main() == 0

    sys.argv = [sys.argv[0], '-i', 'test/resources/invalid.py', '-o', '.', '-t', 'python2', '-r', 'test/resources']

    assert main() == 1

    sys.argv = [sys.argv[0], '-i', 'test/resources/invalid_folder', '-o', '.', '-t', 'python2', '-r', 'test/resources']


# Generated at 2022-06-22 12:39:16.810558
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:17.398300
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:29.851121
# Unit test for function main
def test_main():
    sys.argv = ["py_backwards.py",
                "-i", "test.py",
                "-o", "test_out.py",
                "-t", "3.5"]

# test_main()

# Generated at 2022-06-22 12:39:30.369067
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:39:31.873042
# Unit test for function main
def test_main():
    init_settings(test_args)
    assert main() == 0


# Generated at 2022-06-22 12:39:36.509737
# Unit test for function main
def test_main():
    sys.argv = ['main', '-i', 'test_issue1.py', '-o', 'test_issue1_out.py',
                '-t', '3.5', '-r', '.', '-d']

    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:47.369315
# Unit test for function main
def test_main():
    with patch('argparse.ArgumentParser') as arg_parser_mock:
        instance = arg_parser_mock.return_value
        instance.parse_args = MagicMock(return_value=MagicMock(
            input=[],
            output='foo.py',
            target='python-27',
            root=''))

        compile_files_mock = MagicMock()
        compile_files_mock.return_value = {'foo.py': 'foo.py'}
        with patch('pybackwards.compiler.compile_files', compile_files_mock):
            config_mock = MagicMock()
            with patch('pybackwards.conf.init_settings', config_mock):
                assert main() == 0


# Generated at 2022-06-22 12:39:49.504238
# Unit test for function main
def test_main():
    # TODO: add unit test for function main
    pass

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:53.889086
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'test/test_data/test_input.py',
                    '-o', 'test/test_data/test_output.py',
                    '-t', '2.7']
    main()

# Generated at 2022-06-22 12:39:58.551426
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'test.py', '-t', '2.7', '-r', 'src', '-d']
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:59.662931
# Unit test for function main
def test_main():
    assert(main() == 0)

# Generated at 2022-06-22 12:40:00.619210
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:19.519301
# Unit test for function main
def test_main():
  print('test not implemented')

# Generated at 2022-06-22 12:40:21.547190
# Unit test for function main
def test_main():
    assert main() == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:31.444523
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', '../test_sources', '-o', '../test_out',
                '-t', '3.6', '-r', '../test_sources']
    assert main() == 0
    sys.argv = ['py-backwards', '-i', '../test_sources', '-o', '../test_out',
                '-t', '3.6']
    assert main() == 0
    sys.argv = ['py-backwards', '-i', '../test_sources', '-o', '../test_out',
                '-t', '3.6', '-r', '../test_sources', '-d']
    assert main() == 0

# Generated at 2022-06-22 12:40:32.743540
# Unit test for function main
def test_main():
    m = main()
    assert m == 0

# Generated at 2022-06-22 12:40:39.293409
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards',
        '-i',
        'tests/compiler/test_data/source/test.py',
        '-o',
        'tests/compiler/test_data/',
        '-t',
        'python3.5',
        '-d'
    ]
    assert main() == 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

# Generated at 2022-06-22 12:40:49.050231
# Unit test for function main
def test_main():
    import io
    import sys
    import os
    import shutil

    def run(arguments, output):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        sys.argv = ['py-backwards'] + arguments
        res = main()
        sys.stdout.seek(0)
        assert sys.stdout.read() == output
        sys.stdout = stdout
        return res

    def compile_files_tst(*args, **kwargs):
        return {'files': [
            'a/b.py'
        ]}

    path = 'test_folder/'
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

# Generated at 2022-06-22 12:40:49.654344
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:51.372412
# Unit test for function main
def test_main():
    # This is a really bad test, but I can't find and better idea.
    assert main() == 0

# Generated at 2022-06-22 12:40:55.980104
# Unit test for function main
def test_main():
    argv_backup = sys.argv
    sys.argv = ['py-backwards', '-i', 'tests/sample_files', '-o',
                'generated.py', '-t', '27']
    assert main() == 0
    sys.argv = argv_backup

# Generated at 2022-06-22 12:40:57.557092
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:41:33.645701
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:41:34.252544
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:41:45.532073
# Unit test for function main
def test_main():
    from .mock import mock_settings, mock_compile_files, mock_print,\
        mock_exit, mock_argparse, mock_exceptions
    mock_settings(const.TARGETS['python2'], False)
    mock_print(0, 'Compilation succeeded')
    mock_exit(0, 0)
    mock_compile_files('input', 'output', const.TARGETS['python2'], 'root')
    mock_argparse(['-i', 'input', '-o', 'output', '-t', 'python2',
                   '-r', 'root'])
    main()

    mock_settings(const.TARGETS['python2'], False)
    mock_print(1, 'Compilation failed')
    mock_exit(1, 1)

# Generated at 2022-06-22 12:41:53.017838
# Unit test for function main
def test_main():
    assert run_main(['-h']) == 0
    assert run_main(['-i', 'file.py', '-t', '3.5', '-o', 'output']) == 1
    assert run_main(['-i', 'input_file.py', '-t', '3.5', '-o', 'output.py']) == 0
    assert run_main(['-i', 'input_folder', '-t', '3.5', '-o', 'output_folder']) == 0
    assert run_main(['-i', 'input_folder', '-t', '3.5', '-r', 'input_folder', '-o', 'output_folder']) == 0


# Generated at 2022-06-22 12:42:03.244842
# Unit test for function main
def test_main():
    import os
    import re
    import tempfile
    from .conf import settings
    from .compiler import compile_file
    from .tree import print_tree

    with tempfile.TemporaryDirectory() as temp_dir:
        input_file = os.path.join(temp_dir, 'in.py')
        output_file = os.path.join(temp_dir, 'out.py')
        with open(input_file, 'w') as f:
            f.write('print\'abc\'')
        os.mkdir(os.path.join(temp_dir, 'noexist'))

        # Normal case
        main()
        assert not settings.debug
        assert not settings.transforms
        assert not settings.tree


# Generated at 2022-06-22 12:42:03.834254
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:13.744310
# Unit test for function main
def test_main():
    run_main([])
    run_main(["--input", "file1"])
    run_main(["--input", "file1", "--target", "3.7"])
    run_main(["--input", "file1", "--output"])
    run_main(["--input", "file1", "--root", "file1"])
    run_main(["--input", "file1", "--output", "file1", "--target", "3.7"])
    run_main(["--input", "file1", "--input", "file2", "--output", "file2",
              "--target", "3.5"])

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:23.506971
# Unit test for function main
def test_main():

    def _test_case(args, expected_result):
        sys.argv[1:] = args.split()
        result = main()
        assert result == expected_result

    _test_case(
        "",
        2
    )

    _test_case(
        "py-backwards -i test-data -o out -t 2.7",
        0
    )

    _test_case(
        "py-backwards -i test-data-2 -o out -t 2.7",
        2
    )

    _test_case(
        "py-backwards -i test-data -o out -t 2.7 -r /home/user/source_dir",
        0
    )


# Generated at 2022-06-22 12:42:24.126763
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:24.703195
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:59.001738
# Unit test for function main
def test_main():
    import argparse
    argparse.ArgumentParser.parse_args = mock.Mock(
        return_value=argparse.Namespace(
            debug=False,
            input=['a.py'],
            output='c.py',
            root='root',
            target='2.7'
        )
    )
    exc = exceptions.CompilationError('foo')
    exc_ = exceptions.TransformationError('foo')
    compiler.compile_files = mock.Mock()
    compiler.compile_files.side_effect = [
        {'ok': 1, 'fail': 0},
        compiler.CompilationError('foo'),
        compiler.TransformationError('foo'),
        compiler.InputDoesntExists('foo'),
        compiler.InvalidInputOutput(['foo'], 'bar')
    ]
    assert main()

# Generated at 2022-06-22 12:43:59.599527
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:08.928428
# Unit test for function main
def test_main():
    # Test case with no errors
    sys.argv = ['./py-backwards', '-i', 'tests/data', '-o', '/tmp', '-t', 'py27', '-r', 'tests/data']
    main()
    assert True

    # Test case with error
    sys.argv = ['./py-backwards', '-i', 'tests/data', '-o', '/tmp/test_test_test', '-t', 'py27', '-r', 'tests/data']
    try:
        main()
    except SystemExit as e:
        assert e.code == 1


# Generated at 2022-06-22 12:44:16.758964
# Unit test for function main
def test_main():
    with open('/tmp/input.py', 'w') as f:
        f.write('a=1\n')
    with open('/tmp/output.py', 'w') as f:
        f.write('# Nothing!\n')

    assert main()==1

    with open('/tmp/input.py', 'w') as f:
        f.write('a: int = 1\n')
    with open('/tmp/output.py', 'w') as f:
        f.write('# Nothing!\n')

    assert main()==0

# Generated at 2022-06-22 12:44:19.522065
# Unit test for function main
def test_main():
    # Compile a file backwards to py3.6
    assert main(['-i tests/examples/py3.7/await', '-o output', '-t 3.6']) == 0

# Generated at 2022-06-22 12:44:30.159044
# Unit test for function main
def test_main():
    import pytest
    import os
    import io
    import sys

    #Check if the proper command line arguments are required
    with pytest.raises(SystemExit):
        with open(os.devnull, 'w') as f:
            with io.StringIO() as buf, contextlib.redirect_stderr(buf):
                sys.argv = ['py-backwards.py']
                main()
                output = buf.getvalue()
                assert 'usage: py-backwards [-h] -i INPUT [INPUT ...] -o OUTPUT' \
                       ' -t TARGET [-r ROOT] [-d]' in output

    #Check if the proper command line arguments are required

# Generated at 2022-06-22 12:44:38.334436
# Unit test for function main
def test_main():
    class MockArgumentParser:
        def __init__(self):
            self.args = []

        def parse_args(self):
            return self.args

    init_settings({})

    parser_1 = MockArgumentParser()
    parser_1.args = {'input': ['a/b/c.py'],
                     'output': '',
                     'target': 'py35',
                     'root': '',
                     'debug': False}

    try:
        main()
        print('No error thrown')
        sys.exit(1)
    except SystemExit as e:
        assert e.code == 2

    parser_2 = MockArgumentParser()

# Generated at 2022-06-22 12:44:38.850600
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:44.150347
# Unit test for function main
def test_main():
    args_door, sys.argv = sys.argv, ['py-backwards', '-i', 'main.py', '-o', 'main_out.py',' -t','3.5',' -r','src',' -d']
    out = main()
    assert out == 0
    sys.argv = args_door

# Generated at 2022-06-22 12:44:44.715893
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:48:17.377619
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', './input.py', '-o', './output.py', '-t', '3.5', '-r', './root']
    assert main() == 0
    sys.argv = [sys.argv[0], '-i', './input.py', '-o', './output.py', '-t', '3.5']
    assert main() == 0
    sys.argv = [sys.argv[0], '-i', './input.py', '-o', './output', '-t', '3.5']
    assert main() == 0

# Generated at 2022-06-22 12:48:21.965008
# Unit test for function main
def test_main():
    sys.argv = [
        'py-backwards-cli',
        '-i',
        './tests/source.py',
        '-o',
        './tests/out.py',
        '-t',
        '3.4',
        '-r',
        './tests/'
    ]

    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:48:32.292689
# Unit test for function main
def test_main():
    from . import conf
    from . import exceptions

    # Test invalid args
    with pytest.raises(exceptions.InvalidInputOutput):
        main(['-i']) # noqa
    with pytest.raises(exceptions.InvalidInputOutput):
        main(['-o']) # noqa
    with pytest.raises(exceptions.InvalidInputOutput):
        main(['-i', 'input', '-o']) # noqa
    with pytest.raises(exceptions.InvalidInputOutput):
        main(['-i', '-o', 'output']) # noqa
    with pytest.raises(exceptions.InvalidInputOutput):
        main(['-i', 'input', '-o', 'output']) # noqa