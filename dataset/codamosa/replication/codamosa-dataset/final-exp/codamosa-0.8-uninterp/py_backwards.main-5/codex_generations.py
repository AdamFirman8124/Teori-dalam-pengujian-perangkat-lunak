

# Generated at 2022-06-22 12:38:31.895020
# Unit test for function main
def test_main():
    assert(main()==0)



# Generated at 2022-06-22 12:38:33.793592
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:38.904497
# Unit test for function main
def test_main():
    sys.argv = sys.argv[:1] + ['-i', 'test/input', '-o', 'test/output',
                               '-t', 'py36', '-r', 'test/']

    # Don't run tests on py-backwards
    sys.argv.append('--ignore=py-backwards')
    assert main() == 0

# Generated at 2022-06-22 12:38:49.148940
# Unit test for function main
def test_main():
    # assert main() == 0
    assert main() == 0
    assert main(['-i', './py-backwards']) == 0
    assert main(['-i', './py-backwards', '-t', '3.6']) == 0
    assert main(['-i', './py-backwards', '-t', '3.6', '-r', './py-backwards']) == 0
    assert main(['-i', './py-backwards', '-t', '3.6', '-r', './py-backwards',
                 '-o', '/tmp/py-backwards']) == 0

# Generated at 2022-06-22 12:38:53.659363
# Unit test for function main
def test_main():
    target = sys.argv[0]
    sys.argv = sys.argv[:1] + ['-i', 'input.py', '-o', 'output.py', '-t',
                               '3.4', '-d', '-r', 'root']
    sys.modules.pop(__name__, None)
    from py_backwards import main
    main()
    sys.argv = sys.argv[:1] + ['-i', 'input', '-o', 'output', '-t', '3.5',
                               '-r', 'root']
    sys.modules.pop(__name__, None)
    from py_backwards import main
    main()

# Generated at 2022-06-22 12:39:00.962047
# Unit test for function main
def test_main():
    sys.argv.append('-i')
    sys.argv.append('1.py')
    sys.argv.append('2.py')
    sys.argv.append('-o')
    sys.argv.append('out_folder')
    sys.argv.append('-t')
    sys.argv.append('2.7')
    sys.argv.append('-r')
    sys.argv.append('in_folder')
    main()

# Generated at 2022-06-22 12:39:10.002820
# Unit test for function main
def test_main():
    get_char = msvcrt.getch
    args = ['-i', 'test\\test_cases\\test_hello_world', '-o', 'test\\output', '-t', '2.7', '-d']
    sys.argv = sys.argv[:1] + args
    main()
    assert 1 == 1, 'Exception was raised!'

    args = ['-i', 'test\\test_cases\\test_from_3_to_2',  '-o', 'test\\output', '-t', '2.7', '-d']
    sys.argv = sys.argv[:1] + args
    main()
    assert 1 == 1, 'Exception was raised!'


# Generated at 2022-06-22 12:39:11.567401
# Unit test for function main
def test_main():
    assert main() == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:20.697094
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'out', '-t', '3.6']
    assert main() == 1
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'out', '-t', '3.6']
    assert main() == 1
    sys.argv = ['py-backwards', '-i', 'test.py', '-o', 'out',
                '-t', '3.7', '-r','../src']
    assert main() == 1


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:28.057195
# Unit test for function main
def test_main():
    backend = StringIO()
    sys.stdout = backend
    main(['-i', '-o', '-t', '-r', '-d'])
    sys.stdout = sys.__stdout__

    assert backend.getvalue() == messages.compilation_result({})

    backend = StringIO()
    sys.stdout = backend
    main(['-i', '-o', '-t', '-r', '-d'])
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:47.053667
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass

# Generated at 2022-06-22 12:39:49.574182
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'test/dummy.py', '-o', 'test/output.py', '-t', '2.7']
    assert main() == 0

# Generated at 2022-06-22 12:39:50.782323
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-22 12:40:01.059497
# Unit test for function main
def test_main():
    """
    Test function that checks main function operation
    """
    sys.argv = ['py-backwards', '-i', 'C:\\Users\\isvol\\Desktop\\source.py',
    '-o', 'C:\\Users\\isvol\\Desktop\\output.py',
    '-t', 'python36', '-r', 'folder', '-d']
    assert main() == 0
    sys.argv = ['py-backwards', '-i', 'C:\\Users\\isvol\\Desktop\\source.py',
    '-o', 'C:\\Users\\isvol\\Desktop\\output.py',
    '-t', 'python34', '-r', 'folder', '-d']
    assert main() == 0

# Generated at 2022-06-22 12:40:02.076621
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-22 12:40:11.098918
# Unit test for function main
def test_main():
    try:
        import mock
    except ImportError:
        return
    else:
        mock_args = mock.Mock()
        mock_args.input = 'testinput.py'
        mock_args.output = 'testoutput.py'
        mock_args.target = '2.7'
        mock_args.root = '.'
        with mock.patch('sys.argv', ['py-backwards', '-i', 'testinput.py',
                                     '-o', 'testoutput.py', '-t', '2.7',
                                     '-r', '.']):
            assert main() == 0

# Generated at 2022-06-22 12:40:18.934890
# Unit test for function main
def test_main():
    argv = ['', '-i', 'tests/fixtures/main_test.py',
            '-o', 'tests/fixtures/output',
            '-t', 'python34']
    sys.argv = argv
    main()
    argv = ['', '-i', 'inexisting_file.py',
            '-o', 'tests/fixtures/output',
            '-t', 'python34']
    sys.argv = argv
    main()
    assert True

# Generated at 2022-06-22 12:40:20.928228
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:22.048707
# Unit test for function main
def test_main():
    init()
    assert main() == 0

# Generated at 2022-06-22 12:40:31.763671
# Unit test for function main
def test_main():
    input_ = 'tests'
    output_ = 'tests_out'
    target_ = '2.7'
    root_ = 'tests'

    from .compiler import compile_files
    from .conf import init_settings
    from . import const, messages

    const.DEBUG = False 

    init_settings({'input': input_, 'output': output_, 'target': target_, 'root': root_})

    result = compile_files(input_, output_, const.TARGETS[target_],  root_)
    print(messages.compilation_result(result))

    #return result
#test_main()

# Generated at 2022-06-22 12:40:59.048223
# Unit test for function main
def test_main():
    sysargv_1 = ['py-backwards', '-i', 'input_file', '-o', 'output_file', '-t',
                 '2.7', '-r', 'root_file']
    sysargv_2 = ['py-backwards', '-i', 'input_file', '-o', 'output_file', '-t',
                 '2.7', '-d']
    sysargv_3 = ['py-backwards', '-i', 'input_file', '-o', 'output_file', '-t',
                 '2.7']
    sysargv_4 = ['py-backwards', '-i', 'input_file', '-o', 'output_file', '-t',
                 '2.7', '-r']


# Generated at 2022-06-22 12:40:59.596771
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:41:10.618745
# Unit test for function main
def test_main():
    input_ = 'input'
    output = 'output'
    target = '2'
    root = 'root'
    assert main([input_, '--output', output, '--target', target,
                 '--root', root]) == 0
    assert main(['-i', input_, '-o', output, '-t', target,
                 '-r', root]) == 0
    assert main([input_, '-o', output, '-t', target,
                 '-r', root]) == 0
    assert main([input_, '--output', output, '-t', target,
                 '-r', root]) == 0
    assert main([input_, '--output', output, '--target', target,
                 '-r', root]) == 0

# Generated at 2022-06-22 12:41:11.273695
# Unit test for function main
def test_main():
    assert main() != 0

# Generated at 2022-06-22 12:41:21.261708
# Unit test for function main
def test_main():
    from .compiler import compile_files
    from .conf import init_settings
    from . import const, messages, exceptions
    try:
        for input_ in const.TARGETS.keys():
            result = compile_files(input_, const.TARGETS['3.8'],
                                   const.TARGETS['3.8'],
                                   const.TARGETS['root'],)
    except exceptions.CompilationError as e:
        print(messages.syntax_error(e), file=sys.stderr)
        return 1
    except exceptions.TransformationError as e:
        print(messages.transformation_error(e), file=sys.stderr)
        return 1

# Generated at 2022-06-22 12:41:32.078374
# Unit test for function main
def test_main():
    sys.argv = ["py_backwards", "-i", "test/test_files/test.py", "-o", "test/test_files/testout.py", "--target", "2.7"]
    assert main() == 0, "main() should return 0"
    with open("test/test_files/testout.py", 'r') as file:
        assert file.read() == "from __future__ import print_function\nprint(\"PY_BACKWARDS_ID\")\n", "main() should create file with rewritten code"
    os.remove("test/test_files/testout.py")

# Generated at 2022-06-22 12:41:39.637245
# Unit test for function main
def test_main():
    argv = ['py-backwards', '-i', 'test/test_files/test_files.py', '-o',
            'output.py', '-t', '3.5']
    main()
    assert open('output.py', 'r').readlines() == \
        open('test/test_files/output_3.5.py', 'r').readlines()
    os.remove('output.py')
    assert main(argv) == 0

# Generated at 2022-06-22 12:41:43.501820
# Unit test for function main
def test_main():
    tmp = const.ROOT
    const.ROOT = os.path.join(os.path.dirname(__file__), '..')
    try:
        assert main() == 1
    finally:
        const.ROOT = tmp

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:41:52.877170
# Unit test for function main
def test_main():
    """
        Unit test for function main
        :return:
        """
    class FakeArgs:
        input=['test_class.py', 'test_extend_dict']
        output ='test_output'
        target = '2.7'
        root = None
        debug = False
        def __init__(self):
            self.input=['test_class.py', 'test_extend_dict']
            self.output ='test_output'
            self.target = '2.7'
            self.root = None
            self.debug = False
      

    parser = ArgumentParser(
        'py-backwards',
        description='Python to python compiler that allows you to use some '
                    'Python 3.6 features in older versions.')

# Generated at 2022-06-22 12:41:54.320084
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:39.127424
# Unit test for function main
def test_main():
    # Test that error is returned if target is not specified
    with patch('sys.argv', ['py-backwards', '-i', 'spam', '-o', 'spam-backwards']):
        assert main() == 2

    # Test that error is returned if output is not specified
    with patch('sys.argv', ['py-backwards', '-i', 'spam', '-t', 'Python3']):
        assert main() == 2

    # Test that error is returned if input is not specified
    with patch('sys.argv', ['py-backwards', '-o', 'spam-backwards', '-t', 'Python3']):
        assert main() == 2

# Generated at 2022-06-22 12:42:39.731129
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:42:48.435081
# Unit test for function main
def test_main():
    # Check if function returns 0 after correct compilation
    sys.argv = [sys.argv[0], "-i", "test/test_files/correct_files/test1.py",
                "-o", "test/test_files/output/", "-t", "py27"]
    assert main() == 0
    
    # Check if function returns 1 after incorrect compilation
    sys.argv = [sys.argv[0], "-i", "test/test_files/incorrect_files/test1.py",
                "-o", "test/test_files/output/", "-t", "py27"]
    assert main() == 1

# Generated at 2022-06-22 12:42:51.180238
# Unit test for function main
def test_main():
    sys.argv[1:] = ['-i', 'tests/', '-o', 'tests-result/', '-t', '3.4', '-r', 'tests/']
    main()
    assert True

# Generated at 2022-06-22 12:43:01.771278
# Unit test for function main
def test_main():
    # tests input argument
    sys.argv.append('-i')
    sys.argv.append('file1')
    sys.argv.append('-i')
    sys.argv.append('file2')
    # tests output argument 
    sys.argv.append('-o')
    sys.argv.append('file1')
    # tests target argument
    sys.argv.append('-t')
    sys.argv.append('3.3')
    # tests root argument
    sys.argv.append('-r')
    sys.argv.append('file1')
    # tests debug argument
    sys.argv.append('-d')
    try:
        assert main() == 1
    except SystemExit:
        assert True



# Generated at 2022-06-22 12:43:08.575598
# Unit test for function main
def test_main():
    options = sys.argv
    options1 = ["-i", "input.py", "-o", "output.py",
                "-t", "2.7"]
    options2 = ["-i", "input.py", "-o", "input.py",
                "-t", "2.7"]
    options3 = ["-i", "input.py", "-o", "input.py",
                "-t", "2.7"]

    assert main(options) == 0
    assert main(options1) == 0
    assert main(options2) == 1
    assert main(options3) == 1

# Generated at 2022-06-22 12:43:20.159297
# Unit test for function main
def test_main():
    # Test invalid input and output
    for input_, output in [('', ''), ('.', '.'), ('..', '.'), ('file', '.'),
                           ('file', ''), ('', 'file'), ('.', 'file')]:
        sys.argv = [
            'py-backwards', '-i', input_, '-o', output, '-t', '2.7', '-r', '']
        assert main() == 1

    # Test invalid target
    sys.argv = ['py-backwards', '-i', 'test_data', '-o', 'tmp', '-t', '2.6',
                '-r', '']
    assert main() == 1

    # Test compilation error

# Generated at 2022-06-22 12:43:20.757159
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:43:21.348917
# Unit test for function main
def test_main():
    assert main() != 1

# Generated at 2022-06-22 12:43:32.591543
# Unit test for function main
def test_main():
    import io
    from unittest.mock import Mock, patch
    from unittest import TestCase

    class TestMain(TestCase):
        @patch('sys.argv', ['py_backwards'])
        def test_empty(self):
            self.assertIs(main(), 2)

        @patch('sys.argv', ['py_backwards', '-i', 'test_input', '-t', '3.5'])
        def test_wrong_target(self):
            self.assertIs(main(), 2)


# Generated at 2022-06-22 12:45:08.366723
# Unit test for function main
def test_main():
    sys.argv = [
        sys.argv[0],
        '-i', 'tests/test_files/test_simple.py',
        '-o', 'tests/output_files/test_simple.py',
        '-t', '2.7',
        '-d'
    ]
    assert main() == 0
    sys.argv = [
        sys.argv[0],
        '-i', 'tests/test_files/test_simple.py',
        '-o', 'tests/output_files',
        '-t', '2.7',
        '-d'
    ]
    assert main() == 0

# Generated at 2022-06-22 12:45:08.962251
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:45:09.832866
# Unit test for function main
def test_main():
    result = main()
    assert result == 0

# Generated at 2022-06-22 12:45:13.680530
# Unit test for function main
def test_main():
    test_args = ['-i', ('tests/data/from_3_7_syntax_test.py',
                        'tests/data/for_else_syntax_test.py'),
                 '-o', 'tests/data/output_folder',
                 '-t', '3.6']
    assert main(test_args) == 0

# Generated at 2022-06-22 12:45:20.701550
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-i', 'examples/input_file.py', '-o', 'examples/output_file.py', '-t', '3.0', '-r', 'examples']
    assert main() == 0
    sys.argv = [sys.argv[0], '-i', 'examples/input_folder', '-o', 'examples/output_folder', '-t', '3.0', '-r', 'examples']
    assert main() == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:45:30.142758
# Unit test for function main
def test_main():
    test_inputs = ['input.py', 'input']
    test_targets = ['2.7', '3.5', '3.6']
    test_roots = ['root', 'root/']
    test_outputs = ['output.py', 'output/']
    for input_ in test_inputs:
        for target in test_targets:
            for root in test_roots:
                for output in test_outputs:
                    args = []
                    args.append('-i')
                    args.append(input_)
                    args.append('-t')
                    args.append(target)
                    args.append('-o')
                    args.append(output)
                    args.append('-r')
                    args.append(root)
                    assert main(args) == 0

# Run function if invoked directly


# Generated at 2022-06-22 12:45:41.411823
# Unit test for function main
def test_main():
    with pytest.raises(exceptions.InputDoesntExists):
        main(['test.py', '-i' 'tests/data/b', '-o', 'tests/data/a', '-t', '3'])
    with pytest.raises(exceptions.InputDoesntExists):
        main(['tests/data/a', '-i', 'test.py', '-o', 'tests/data/a', '-t', '3'])
    with pytest.raises(exceptions.InputDoesntExists):
        main(['tests/data/b', '-i', 'tests/data/b', '-o', 'test.py', '-t', '3'])

# Generated at 2022-06-22 12:45:46.360172
# Unit test for function main
def test_main():
    try:
        sys.argv = [sys.argv[0], "test_input.py", "-o", "test_output.py", "-t",
                    "2.7"]
        main()
    except SystemExit:
        pass
    with open("test_output.py") as f:
        s = f.read()
    assert s == 'print("test")'
    os.remove("test_output.py")

# Generated at 2022-06-22 12:45:49.491977
# Unit test for function main
def test_main():
    assert main(['py-backwards', './tests/script.py','-o','./tests/script2.py', '-t', 'python2', '-d']) == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:45:50.037413
# Unit test for function main
def test_main():
    assert main() == 0