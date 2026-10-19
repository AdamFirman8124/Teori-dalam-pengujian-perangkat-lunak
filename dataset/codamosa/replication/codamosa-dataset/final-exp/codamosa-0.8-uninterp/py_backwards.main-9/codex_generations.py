

# Generated at 2022-06-22 12:38:31.229338
# Unit test for function main
def test_main():
    main()

test_main()

# Generated at 2022-06-22 12:38:32.372545
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:38:37.340233
# Unit test for function main
def test_main():
    #inputs = ['input.txt', 'err1.txt', 'err2.txt', 'err3.txt']
    #ouputs = ['output.txt', 'err1.txt', 'err2.txt', 'err3.txt']
    inputs = ['err2.txt', 'err3.txt']
    ouputs = ['err1.txt', 'err2.txt']
    error = []
    for i in range(len(inputs)):
        result = main(inputs[i], ouputs[i], '2.7', '', False)
        error.append(result)
    assert error == [0, 0, 1, 1]

# Generated at 2022-06-22 12:38:41.881933
# Unit test for function main
def test_main():
    result = main(["P:/backwards-0.1.0/backwards/tests/sources/block_comments.py",
                   "P:/backwards-0.1.0/backwards/tests/sources/__init__.py",
                   "P:/backwards-0.1.0/backwards/tests/sources/numbers.py",
                   "P:/backwards-0.1.0/backwards/tests/sources/fstrings.py"
                   ], "P:/backwards-0.1.0/backwards/tests/sources/__init__.py"
                   , "python2.7", "P:/backwards-0.1.0/backwards/tests/sources/__init__.py")
    assert result==0

# Generated at 2022-06-22 12:38:42.573027
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-22 12:38:45.301123
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:38:55.573116
# Unit test for function main
def test_main():
    sys.stdout = open('tests/out.txt', 'w')
    sys.stderr = open('tests/err.txt', 'w')
    sys.argv = ['py-backwards.py', 'tests/input.py', '-o', 'tests/output.py', '-r', 'tests', '-t', '2.7']
    main()
    with open('tests/output.py', 'r') as file:
        result = ''.join(file.readlines())
    with open('tests/expected.py', 'r') as expected:
        expected_result = ''.join(expected.readlines())
        assert result == expected_result
    sys.stdout.close()
    sys.stderr.close()

# Generated at 2022-06-22 12:39:00.591970
# Unit test for function main
def test_main():
    sys.argv[1:] = ["-i", "./test/test_data_files/test_input.py", "-o", "./", "-t", "3.5"]
    sys.exit(main())

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:39:04.155467
# Unit test for function main
def test_main():
    sys.argv = 'py-backwards -i py_vars.py -o py_vars_out.py -t 2.7'.split()
    result = main()
    assert result == 0
if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:39:13.183377
# Unit test for function main
def test_main():
    code = "some code"
    with open('some_file.py', 'w', encoding='utf-8') as f:
        f.write(code)
    with open('some_file_2.py', 'w', encoding='utf-8') as f:
        f.write(code)
    with open('some_dir/some_file.py', 'w', encoding='utf-8') as f:
        f.write(code)
    with open('some_dir/some_file_2.py', 'w', encoding='utf-8') as f:
        f.write(code)
    main(['some_file.py', 'some_file_2.py', 'some_dir'], 'some_output_dir')

# Generated at 2022-06-22 12:39:23.315905
# Unit test for function main
def test_main():
    assert main() == main()

# Generated at 2022-06-22 12:39:36.111732
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

# Generated at 2022-06-22 12:39:40.199505
# Unit test for function main
def test_main():
    # set sys.argv to some value
    sys.argv = [1, 2, 3]
    # use built-in function to strip __main__ and replace with main
    sys.modules['__main__'].__main__ = main
    # execute the program
    main()

# Generated at 2022-06-22 12:39:48.962504
# Unit test for function main
def test_main():
    file_name = 'test_file'
    args = ArgumentParser('py-backwards',
                          description='Python to python compiler that allows'
                                      ' you to use some Python 3.6'
                                      ' features in older versions.')
    args.add_argument('-i', '--input', type=str, nargs='+',
                      required=True, help='input file or folder')
    args.add_argument('-o', '--output', type=str, required=True,
                      help='output file or folder')
    args.add_argument('-t', '--target', type=str, required=True,
                      help='target python version')
    args.add_argument('-r', '--root', type=str, required=False,
                      help='sources root')

# Generated at 2022-06-22 12:39:49.513128
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:39:59.559040
# Unit test for function main
def test_main():
    from io import StringIO
    import sys
    import unittest

    from . import const, messages, exceptions

    class TestMain(unittest.TestCase):
        def test_main(self):
            try:
                out = StringIO()
                sys.stdout = out
                main()
            except SystemExit as e:
                self.assertEqual(e.code, messages.INPUT_REQUIRED)

            try:
                out = StringIO()
                sys.stdout = out
                main(['-i', 'inp.py'])
            except SystemExit as e:
                self.assertEqual(e.code, messages.OUTPUT_REQUIRED)


# Generated at 2022-06-22 12:40:02.504260
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'input/', '-o', 'output', '-t', 'python35']
    main()

# Generated at 2022-06-22 12:40:03.192973
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:05.935086
# Unit test for function main
def test_main():
    r = main()
    assert(r == 1)

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:40:06.994553
# Unit test for function main
def test_main():
    assert(main() == 0)

# Generated at 2022-06-22 12:40:35.970850
# Unit test for function main
def test_main():
    from . import testing_tools

    main()

    main_inputs = [
        ['-i', 't.py', '--output', 'output.txt', '-t', '3.5'],
        ['-i', 't.py', '--output', 'output.txt', '-t', '3.6'],
        ['-i', 't.py', '--output', 'output.txt', '-t', '3.7'],
        ['-i', 't.py', '--output', 'output.txt', '-t', '3.8'],
        ['-i', 't.py', '--output', 'output.txt', '-t', '3.9']
    ]
    for test_input in main_inputs:
        sys.argv = test_input
        main()




# Generated at 2022-06-22 12:40:36.592170
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:40:37.260851
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:40:37.948320
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-22 12:40:47.994462
# Unit test for function main
def test_main():
    import os

    root_path = os.path.abspath(os.path.dirname(__file__))
    project_path = os.path.join(root_path, '..')
    python_root = os.path.join(root_path, 'test', 'python_examples')

    test_path = os.path.join(root_path, 'test_tmp')
    test_output_path = os.path.join(test_path, 'output')
    test_output_path2 = os.path.join(test_path, 'output_2')
    test_output_path3 = os.path.join(test_path, 'output_3')
    os.makedirs(test_output_path)
    os.makedirs(test_output_path2)

# Generated at 2022-06-22 12:40:49.778625
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:40:59.048203
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

# Generated at 2022-06-22 12:41:10.134717
# Unit test for function main
def test_main():
    import pytest
    from py_backwards.conf import settings

    def reset_args():
        settings.input = None
        settings.output = None
        settings.target = None
        settings.file = None

    with pytest.raises(SystemExit) as e:
        reset_args()
        main()
    assert e.value.code == 2
    with pytest.raises(SystemExit) as e:
        reset_args()
        main(['-i', 'test/test_file.py'])
    assert e.value.code == 2
    with pytest.raises(SystemExit) as e:
        reset_args()
        main(['-i', 'test/test_file.py', '-o', 'test/test_file.py'])
    assert e.value.code == 2

# Generated at 2022-06-22 12:41:19.040180
# Unit test for function main
def test_main():
    print("test_main_target_3_6")
    params = """-i test/data/input_3_6/h1.py test/data/input_3_6/h2.py test/data/input_3_6/h3.py -o test/data/output/out -t 3.6"""
    argv = params.split(" ")
    sys.argv = argv
    main()
    file = open("test/data/output/out/h1.py", "r")
    print(file.read())
    file = open("test/data/output/out/h2.py", "r")
    print(file.read())
    file = open("test/data/output/out/h3.py", "r")
    print(file.read())
    print("--------------------")

   

# Generated at 2022-06-22 12:41:19.741830
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:42:03.155441
# Unit test for function main
def test_main():
    sys.argv = ['main.py', '-i', '../tests/test.py', '-o', '../tests/test2.py',
                '-t', 'py27', '-r', '../tests', '-d']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-22 12:42:03.639264
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:04.118609
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:09.379835
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'examples/erdos.py', '-o', 'erdos.py', '-t', '2']

# Uncomment to test
#test_main()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.argv += ['-h']
    sys.exit(main())

# Generated at 2022-06-22 12:42:11.771541
# Unit test for function main
def test_main():
    ret= main([ '-t', '2.7' ,'-i', 'input.py' ,'-o', 'output.py'])
    assert ret == 0

# Generated at 2022-06-22 12:42:19.045434
# Unit test for function main
def test_main():
    # Args that are not present in argparse
    args = argparse.Namespace()
    args.input = ['examples/test.py']
    args.output = 'examples/test'
    args.target = 'python34'
    args.root = 'examples'
    args.debug = False
    init_settings(args)

    result = main()
    assert result == 0



# Generated at 2022-06-22 12:42:19.615580
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:42:20.883044
# Unit test for function main
def test_main():
    exit_code = main()
    assert exit_code == 0

# Generated at 2022-06-22 12:42:21.467497
# Unit test for function main
def test_main():
    return 0

# Generated at 2022-06-22 12:42:22.022347
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:43:56.336128
# Unit test for function main
def test_main():
    parser = ArgumentParser('test')
    parser.add_argument('-r', '--root', type=str, required=False,
                    help='sources root')
    args = parser.parse_args()
    init_settings(args)
    sys.argv = ['py-backwards', '-i', './test/test_files/test_files', '-o', './test/output/', '-t', '3.5', '-d']
    assert main() == 0

# Generated at 2022-06-22 12:43:57.902893
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-22 12:43:59.958286
# Unit test for function main
def test_main():
    # check that the program does not return error if all inputs are correct
    assert main() == 0

# Generated at 2022-06-22 12:44:03.693593
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'tests/data/examples/basic_example.py', '-o', 'output.py',
                '-d', '-t', '2.7']
    assert main() == 0

# Generated at 2022-06-22 12:44:13.477480
# Unit test for function main
def test_main():
    # Positive test
    input = 'input.py'
    output = 'output.py'
    args = ['py-backwards', '-i', input, '-o', output, '-t', '3.5', '-r', 'root']
    sys.argv = args
    main()
    assert open(output).read() == '1 + 2\n'

    # Negative test
    input = 'input.py'
    output = 'input.py'
    args = ['py-backwards', '-i', input, '-o', output, '-t', '3.5', '-r', 'root']
    sys.argv = args
    assert main() == 1

# Generated at 2022-06-22 12:44:23.866059
# Unit test for function main
def test_main():
    from . import test_util
    import types
    import os
    import shutil
    from . import const
    from . import exceptions

    with test_util.WithTempDirectory() as temp_dir:
        # TODO process single directories too
        # Test version
        test_file = 'test.py'
        with open(os.path.join(temp_dir, test_file), 'w+') as file:
            file.write('print(1)')

        result = test_util.run_module('-i', test_file,
                                      '-o', temp_dir,
                                      '-t', '3',
                                      '-r', temp_dir)

        assert result.exit_code == 0, \
            "main() return non zero exit code {0}".format(result.exit_code)
        assert os

# Generated at 2022-06-22 12:44:32.621439
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards', '-i', 'tests/example.py', '-o',
                'tests/example.py', '-t', '3.5', '-r', 'tests']

    assert main() == 0

    sys.argv = ['py-backwards', '-i', 'tests/example2.py', '-o',
                'tests/example2.py', '-t', '3.5', '-r', 'tests']

    assert main() == 1

    sys.argv = ['py-backwards', '-i', 'tests/example.py', '-o',
                'tests/example.py', '-t', '3.5']

    assert main() == 0

# Generated at 2022-06-22 12:44:34.982884
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 12:44:35.577468
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-22 12:44:46.960756
# Unit test for function main
def test_main():
    sys.argv = ['', '-i', 'examples/a.py', '-o', '.out', '-t', '2.7']
    assert main() == 1

    sys.argv = ['', '-i', '.in', '-o', '.out', '-t', '2.7']
    assert main() == 1

    sys.argv = ['', '-i', 'examples/a.py', '-o', 'examples/a.py', '-t', '2.7']
    assert main() == 1

    sys.argv = ['', '-i', 'test_dir', '-o', '.out', '-t', '2.7']
    assert main() == 1


# Generated at 2022-06-22 12:48:16.478820
# Unit test for function main
def test_main():
    return
    # init_settings(args)

# Generated at 2022-06-22 12:48:18.358103
# Unit test for function main
def test_main():
    assert main() == 0

if __name__ == "__main__":
    sys.exit(main())

# Generated at 2022-06-22 12:48:29.983900
# Unit test for function main
def test_main():
    sys.argv = ['py-backwards',
                '-i', '../tests/data/unit-tests',
                '-o', '../tests/data/unit-tests',
                '-t', '3.5']
    assert main() == 0

    sys.argv = ['py-backwards',
                '-i', '../tests/data/unit-tests',
                '-o', './compiled-data/unit-tests',
                '-t', '3.5']
    assert main() == 0

    sys.argv = ['py-backwards',
                '-i', '../tests/data/unit-tests',
                '-o', './compiled-data/unit-tests',
                '-t', '3.5']
    assert main() == 0
