

# Generated at 2022-06-22 12:38:34.833601
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == "__main__":
    main()

# Generated at 2022-06-22 12:38:40.291953
# Unit test for function main
def test_main():
    import tempfile
    import os.path
    import shutil
    import sys
    import filecmp
    current_dir = os.path.dirname(__file__)
    test_dir = os.path.join(current_dir, '..', 'test')
    assert os.path.isdir(test_dir)
    assert os.path.isdir(os.path.join(test_dir, 'files'))
    assert os.path.isdir(os.path.join(test_dir, 'files', 'from'))
    assert os.path.isdir(os.path.join(test_dir, 'files', 'to'))
    # assert os.path.isdir(os.path.join(test_dir, 'files', 'to', '3.5'))
    # assert os.path.isdir(

# Generated at 2022-06-22 12:38:43.629904
# Unit test for function main
def test_main():
    main(r"C:\Users\zheka\PycharmProjects\py-backwards\test_files\test.py", "output.py", "3.5")


# Generated at 2022-06-22 12:38:45.780353
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-22 12:38:56.692724
# Unit test for function main
def test_main():
    # Test for not existing file
    try:
        main(['-i', 'test/test_data/test_core/test_test_data.py',
              '-o', '/tmp', '-t', '2.7'])
    except SystemExit as e:
        assert(e.code == 1)
    # Test for existing file
    assert(main(['-i', 'test/test_data/test_core/test_test_data.py',
                '-o', '/tmp', '-t', '2.7', '-r', 'test']) == 0)
    # Test for not existing file

# Generated at 2022-06-22 12:38:57.813621
# Unit test for function main
def test_main():
    result = main()
    assert result == 0

# Generated at 2022-06-22 12:39:00.485634
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:01.197689
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:02.855282
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:04.208150
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:17.784614
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'foo.py', '-o', 'bar.py', '-t', '2.7']
    sys.path.insert(0, './')
    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:19.635221
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    status = main()
    sys.exit(status)

# Generated at 2022-06-22 12:39:28.219989
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'tests/sample/simple.py', '-o', 'test',
                '-t', '3.4', '-r', 'tests/sample']
    main()
    # Test if output file exists
    assert os.path.isfile('test/sample/simple.py')
    # Test if output file is the same as expected
    with open('test/sample/simple.py', 'r') as f:
        with open('tests/test/simple.py', 'r') as expected:
            assert f.read() == expected.read()


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:38.836498
# Unit test for function main
def test_main():
    # case 1: invalid input
    assert main(['-i', 'foo', '-o', 'bar', '-t', '3.5', '-r', 'tmp']) == 1

    # case 2: invalid output
    assert main(['-i', 'tests/examples', '-o', '/root/meow', '-t', '3.5', '-r', 'tmp']) == 1

    # case 3: success
    assert main(['-i', 'tests/examples', '-o', 'tmp/output', '-t', '3.5', '-r', 'tmp']) == 0

    # case 4: success
    assert main(['-i', 'tests/examples', '-o', 'tmp/output', '-t', '3.5', '-r', 'tmp', '-d'])

# Generated at 2022-06-22 12:39:41.408883
# Unit test for function main
def test_main():
    assert main(['-i', '', '-o', '', '-t', '', '-d', '']) == 0

# Generated at 2022-06-22 12:39:45.948666
# Unit test for function main
def test_main():
    args = ['py-backwards', '-i', 'tests/test_data/functions/', '-o', 'res', '-t',
            'python38', '-d']
    result = main()
    assert result == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:54.986077
# Unit test for function main
def test_main():
    # Args:
    # -i: input file,
    # -o: output file,
    # -t: target
    # -r: root folder
    sys.argv = [
        'script.py',
        '-i', 'tests/test_data/regression/tokens_handling.py',
        '-o', 'tests/test_data/regression/tokens_handling_res.py',
        '-t', '3.5',
        '-r', 'tests'
    ]

    assert main() == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:01.987318
# Unit test for function main
def test_main():
    # Initializing the parser
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
    parser.add_argument

# Generated at 2022-06-22 12:40:02.505784
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:03.192995
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:22.323816
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:25.113928
# Unit test for function main
def test_main():
    main(['-i', 'example/input', '-o', 'example/output', '-t', '2.7', '-r', 'example/root'])

# Generated at 2022-06-22 12:40:31.562711
# Unit test for function main
def test_main():
    sys.argv[1:] = ['--input', 'input', '--output', 'output', '--target',
                    'py27']
    expected = 'Compilation complete. Successfully compiled 0/1 python files.'
    assert main() == 1
    assert sys.stderr.getvalue() == 'Input file "input" does not exists.\n'
    assert sys.stdout.getvalue() == expected


# Generated at 2022-06-22 12:40:32.382946
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:36.796873
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'tests/common/a.py', '-t', '3.6', '-o', 'test/test/test.py', '-d']
    main()

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:38.735019
# Unit test for function main
def test_main():
    init_settings()
    assert main() == 1

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:39.397408
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:40:40.044274
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:40:40.637990
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:40:41.969578
# Unit test for function main
def test_main():
    assert(main() == 0)

# Generated at 2022-06-22 12:41:21.727186
# Unit test for function main
def test_main():
    input = "tests/test_programs/test.py"
    output = "tests/output/out.py"
    target = "3.6"
    main(input, output, target)
    with open(output) as f:
        out = f.read()
        assert out == """def test(x, y):
    z = 1
    if x == y:
        return x + y
    elif x > y:
        return x - y
    else:
        return x * y
"""

# Generated at 2022-06-22 12:41:24.169859
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:41:24.765116
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:41:25.801055
# Unit test for function main
def test_main():
    print("test_main")
    assert main() == 0

# Generated at 2022-06-22 12:41:29.881974
# Unit test for function main
def test_main():
    input = 'test/data/example.py'
    output = 'test/data/example1.py'
    main(['-t', '2.7', '-i', input, '-o', output])


if __name__ == '__main__':
    status = main()
    sys.exit(status)

# Generated at 2022-06-22 12:41:33.837820
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards',
                '-i', 'tests/files/input/mymodule.py',
                '-o', 'tests/files/output',
                '-t', '2.7']

    assert main() == 0

# Generated at 2022-06-22 12:41:44.178143
# Unit test for function main
def test_main():
    sys.argv = sys.argv[:1]
    sys.argv.append('-i')
    sys.argv.append('input_file.py')
    sys.argv.append('-o')
    sys.argv.append('output_file.py')
    sys.argv.append('-t')
    sys.argv.append('3.5')

    from .compiler import compile_files
    from .conf import init_settings
    from .const import TARGETS
    from . import messages

    init_settings(None)
    compile_files = Mock(return_value=Mock(success=True))
    messages.compilation_result = Mock(return_value='result')

    result = main()

    assert result == 0


# Generated at 2022-06-22 12:41:45.311616
# Unit test for function main
def test_main():
    assert [], main()

# Generated at 2022-06-22 12:41:53.731590
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'test/test_data/test.py',
                '-o', 'test/test_data/test1.py', '-t', '2']
    return_code = main()
    assert return_code == 0
    sys.argv = ['py-backwards', '-i', 'test/test_data/test.py', '-i',
                'test/test_data/test2.py', '-o', 'test/test_data/test1.py',
                '-o', 'test/test_data/test1.py', '-t', '2']
    return_code = main()
    assert return_code == 0

# Generated at 2022-06-22 12:41:55.173320
# Unit test for function main
def test_main():
    """
    Test function main
    :return:
    """
    assert main() == 0

# Generated at 2022-06-22 12:43:20.895919
# Unit test for function main
def test_main():
    from argparse import Namespace
    from .settings import settings
    from .conf import init_settings

    init_settings(None)
    try:
        main()
    except RuntimeError:
        pass
    try:
        settings.input = "test"
        main()
    except RuntimeError:
        pass
    try:
        settings.input = ["test", "test2"]
        settings.output = "test"
        main()
    except RuntimeError:
        pass
    try:
        settings.output = "test"
        main()
    except RuntimeError:
        pass
    try:
        settings.output = "test.py"
        settings.target = "test"
        main()
    except RuntimeError:
        pass

# Generated at 2022-06-22 12:43:21.853264
# Unit test for function main
def test_main():
    settings.DEBUG = True
    assert main() == 1

# Generated at 2022-06-22 12:43:24.194396
# Unit test for function main
def test_main():
    #assert 1 == main()
    assert 0 == main()

# Generated at 2022-06-22 12:43:32.786851
# Unit test for function main
def test_main():
    # test false input
    with patch('pybackwards.compiler.compile_files') as mock_compile:
        with patch('argparse.ArgumentParser.parse_args') as mock_parse:
            mock_args = mock_parse.return_value
            mock_args.input = False
            mock_args.output = False
            mock_args.root = 'test_root'
            mock_args.target = 'test_target'
            mock_args.debug = False
            main()

    # test for input is not exists
    with patch('pybackwards.compiler.compile_files') as mock_compile:
        with patch('argparse.ArgumentParser.parse_args') as mock_parse:
            mock_args = mock_parse.return_value
            mock_args.input = 'test_input'


# Generated at 2022-06-22 12:43:36.791931
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', '/home/user/folder/file.py', '-o',
                '/home/user/folder/file-backwards.py', '-t', '3.5']
    assert main() == 0


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:43:38.611854
# Unit test for function main
def test_main():
    assert main() == 0
    assert main('-o test_input test_output -t python2.7') == 0

# Generated at 2022-06-22 12:43:42.400650
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', 'test/test_files/test.py', '-o', 'test.py', '-t', '2.7', '-r', 'src']
    assert(main() == 0)


# Generated at 2022-06-22 12:43:45.092163
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    exit(main())

# Generated at 2022-06-22 12:43:55.861575
# Unit test for function main
def test_main():
    from .argcompat import patch_argparse_for_pytest
    patch_argparse_for_pytest()
    from . import argcompat
    sys.argv = ['py-backwards', '-i', 'tests\\input_folder', '-o', 'tests\\output_folder', '-t', '2.7', '-r', 'tests\\input_folder']
    argcompat.ARG_PARSER.parse_args()
    assert main() == 0
    sys.argv = ['py-backwards', '-i', 'tests\\input_folder', '-o', 'tests\\output_folder', '-t', '3.5', '-r', 'tests\\input_folder']
    argcompat.ARG_PARSER.parse_args()
    assert main() == 0

# Generated at 2022-06-22 12:44:07.306812
# Unit test for function main
def test_main():
    from .settings import args
    from . import utils
    from tempfile import TemporaryDirectory
    from .conf import init_settings

    files = ['test.py', 'test1.py']
    target = 'py2'

    with TemporaryDirectory() as tmp_dir:
        for f in files:
            utils.create_file(tmp_dir, f, 'import string')
        output = f'{tmp_dir}/compiled'
        files_to_compile = [f'{tmp_dir}/{f}' for f in files]
        args.input = files_to_compile
        args.targets = {target}
        args.output = output
        args.debug = False
        args.root = tmp_dir

        init_settings(args)
        assert main() == 0

# Generated at 2022-06-22 12:47:19.952950
# Unit test for function main
def test_main():
    # For example
    assert main() == 0

# Generated at 2022-06-22 12:47:21.060293
# Unit test for function main
def test_main():
    assert (main() == 0)

# Generated at 2022-06-22 12:47:22.535911
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:47:30.207169
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

# Generated at 2022-06-22 12:47:31.010919
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:47:32.991175
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':  # pragma: no cover
    sys.exit(main())

# Generated at 2022-06-22 12:47:36.238194
# Unit test for function main
def test_main():
    args = [
        '-i', 'test/input/anonymous_functions.py', '-o', 'out', '-t', '3.5'
        ]
    sys.argv[1:] = args
    assert main() == 0

# Generated at 2022-06-22 12:47:37.408301
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-22 12:47:40.847725
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'test.py', '-o', 'test_res', '-t', '3.5']
    assert main() == 0

# Generated at 2022-06-22 12:47:41.620125
# Unit test for function main
def test_main():
    assert main() == 0