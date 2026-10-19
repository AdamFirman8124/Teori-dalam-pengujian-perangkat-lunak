

# Generated at 2022-06-13 14:13:45.048768
# Unit test for method parse_kv_args of class LookupModule
def test_LookupModule_parse_kv_args():
    # Instantiate a LookupModule object
    l = LookupModule()

    # Invoke method parse_kv_args with a valid arguments string
    l.parse_kv_args({'start': '1', 'end': '11', 'stride': '2', 'format': '0x%02x'})

    # Check the values were properly set
    assert l.start == 1
    assert l.end == 11
    assert l.stride == 2
    assert l.format == '0x%02x'

    # Invoke method parse_kv_args with an invalid arguments string
    l.parse_kv_args({'start': '1', 'end': 'abc', 'stride': '2', 'format': '0x%02x'})



# Generated at 2022-06-13 14:13:55.469657
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    lookup_module = LookupModule()

    # First test:
    # start = None, end = None, stride = None, format = None
    match_result = SHORTCUT.match("")
    assert match_result == None
    lookup_module.reset()
    assert lookup_module.start == 1
    assert lookup_module.count == None
    assert lookup_module.end == None
    assert lookup_module.stride == 1
    assert lookup_module.format == "%d"

    # Second test:
    # start = None, end = None, stride = None, format = None
    lookup_module.reset()
    match_result = SHORTCUT.match("I am not a valid shortcut")
    assert match_result == None
    assert lookup_module.start == 1
    assert lookup_module.count == None

# Generated at 2022-06-13 14:14:05.715967
# Unit test for method parse_simple_args of class LookupModule

# Generated at 2022-06-13 14:14:17.789593
# Unit test for method parse_kv_args of class LookupModule
def test_LookupModule_parse_kv_args():

    instance = LookupModule()

    args = dict(start='1', end='2', format='%d')
    try:
        instance.parse_kv_args(args)
        assert (instance.start == 1) and (instance.end == 2) and (instance.format == '%d')
    except Exception as e:
        assert False

    args = dict(start='0x10', end='0x12', format='%d')
    try:
        instance.parse_kv_args(args)
        assert (instance.start == 0x10) and (instance.end == 0x12) and (instance.format == '%d')
    except Exception as e:
        assert False

    args = dict(start='0x10', end='2', format='%d')

# Generated at 2022-06-13 14:14:25.143422
# Unit test for method parse_kv_args of class LookupModule
def test_LookupModule_parse_kv_args():
    lookup = LookupModule()
    terms = []
    terms.append(dict(start='1', end='10', format='host%02d'))
    terms.append(dict(start='0x10', end='0x20', format='host%02d'))
    terms.append(dict(start='010', end='020', format='host%02d'))
    terms.append(dict(count='10', format='host%02d'))
    terms.append(dict(count='0x10', format='host%02d'))
    terms.append(dict(count='010', format='host%02d'))
    terms.append(dict(start='0x10', end='0x20', stride='2', format='host%02d'))

# Generated at 2022-06-13 14:14:36.834711
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup_module = LookupModule()
    lookup_module.start = 1
    lookup_module.end = 5
    lookup_module.format = '%d'
    lookup_module.stride = 1

    output = ['1', '2', '3', '4', '5']
    assert list(lookup_module.generate_sequence()) == output

    lookup_module.start = 1
    lookup_module.end = 10
    lookup_module.format = '%d'
    lookup_module.stride = 2

    output = ['1', '3', '5', '7', '9']
    assert list(lookup_module.generate_sequence()) == output

    lookup_module.start = 1
    lookup_module.end = 2
    lookup_module.format = '%02x'
    lookup_module.str

# Generated at 2022-06-13 14:14:47.483016
# Unit test for method parse_simple_args of class LookupModule

# Generated at 2022-06-13 14:15:00.306152
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    assert list(LookupModule(None, None, None).generate_sequence()) == []
    assert list(LookupModule(None, None, None, end = 0).generate_sequence()) == []
    assert list(LookupModule(None, None, None, start = 1, end = 0).generate_sequence()) == []
    assert list(LookupModule(None, None, None, start = 1, end = 10).generate_sequence()) == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    assert list(LookupModule(None, None, None, start = 1, end = 10, stride = 1).generate_sequence()) == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Generated at 2022-06-13 14:15:10.834970
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    class _LookupModule(LookupModule):
        def reset(self):
            self.start = None
            self.end = None
            self.stride = None
            self.format = None
            self.count = None
    lookup = _LookupModule()

    lookup.parse_simple_args("7")
    assert lookup.start == 7
    assert lookup.end == 7
    assert lookup.stride == 1
    assert lookup.format == "%d"

    lookup.reset()
    lookup.parse_simple_args("5-8")
    assert lookup.start == 5
    assert lookup.end == 8
    assert lookup.stride == 1
    assert lookup.format == "%d"

    lookup.reset()
    lookup.parse_simple_args("2-10/2")
    assert lookup.start == 2
    assert lookup

# Generated at 2022-06-13 14:15:16.954300
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    look_up_module = LookupModule()
    look_up_module.start = 0
    look_up_module.stride = 1
    look_up_module.end = 10
    look_up_module.format = "%d"
    assert [i for i in look_up_module.generate_sequence()] == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Generated at 2022-06-13 14:15:31.762356
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    assert lookup_module.sanity_check() == None
    lookup_module.count = None
    lookup_module.end = None
    try:
        lookup_module.sanity_check()
    except AnsibleError as e:
        assert str(e) == 'must specify count or end in with_sequence'
    lookup_module.count = 5
    lookup_module.end = 5
    try:
        lookup_module.sanity_check()
    except AnsibleError as e:
        assert str(e) == "can't specify both count and end in with_sequence"
    lookup_module.start = 5
    lookup_module.stride = 2
    lookup_module.end = None
    lookup_module.sanity_check()
    assert lookup_module.end == 9
    lookup

# Generated at 2022-06-13 14:15:37.926113
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    example = []
    example.append(
        {
            "terms": ["start=4 end=16 stride=2 format=testuser%02x"],
            "result": ["testuser04", "testuser06", "testuser08", "testuser0a", "testuser0c", "testuser0e", "testuser10"]
        }
    )

# Generated at 2022-06-13 14:15:50.690146
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    lookup = LookupModule()

    # We should get False if passed parameter is not string
    assert lookup.parse_simple_args(None) is False

    # We should get False if we passed an invalid shortcut format
    assert lookup.parse_simple_args('as') is False

    # Check that invalid exadecimal numbers are detected
    assert lookup.parse_simple_args('0x-0x') is False

    # Check that invalid octal numbers are detected
    assert lookup.parse_simple_args('0o-0o') is False

    # Check that valid octal numbers are detected
    assert lookup.parse_simple_args('0o-0o018') is True

    # Check that invalid octal numbers are detected
    assert lookup.parse_simple_args('0o-0o018/0o') is False

    # Check that valid octal

# Generated at 2022-06-13 14:15:58.852367
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup_module = LookupModule()

    lookup_module.start = 1
    lookup_module.end = 6
    assert(list(lookup_module.generate_sequence()) == ["1", "2", "3", "4", "5", "6"])

    lookup_module.start = 5
    lookup_module.end = 12
    assert(list(lookup_module.generate_sequence()) == ["5", "6", "7", "8", "9", "10", "11", "12"])

    lookup_module.start = 1
    lookup_module.end = 8
    lookup_module.stride = 2
    assert(list(lookup_module.generate_sequence()) == ["1", "3", "5", "7"])

    lookup_module.start = 7
    lookup_module.end = 0

# Generated at 2022-06-13 14:16:04.412449
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    assert l.run(["10"], {}) == ["10"]
    assert l.run(["10", "20"], {}) == ["10", "20"]
    assert l.run(["10-20"], {}) == ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    assert l.run(["10-20/2"], {}) == ["10", "12", "14", "16", "18", "20"]
    assert l.run(["0x10-0x20/2"], {}) == ["0x10", "0x12", "0x14", "0x16", "0x18", "0x20"]

# Generated at 2022-06-13 14:16:14.508895
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup = LookupModule()

    lookup.start = 1
    lookup.count = None
    lookup.end = None
    lookup.stride = 1
    lookup.format = "%d"
    lookup.sanity_check()

    lookup.start = 1
    lookup.count = 10
    lookup.end = None
    lookup.stride = 1
    lookup.format = "%d"
    lookup.sanity_check()

    lookup.start = 1
    lookup.count = None
    lookup.end = 10
    lookup.stride = 1
    lookup.format = "%d"
    lookup.sanity_check()

    lookup.start = 10
    lookup.count = 5
    lookup.end = None
    lookup.stride = 1
    lookup.format = "%d"
    lookup.sanity_check()


# Generated at 2022-06-13 14:16:23.847042
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Input list of arguments
    args = [
            "end=11",
            "count=5",
            "end=10",
            "stride=2",
            "start=5",
            "start=4",
            "start=0x0f00",
            "count=4",
            "format=0x%02x",
            "start=0",
            "start=1",
            "format=%04x",
            "end=16",
            "stride=2",
            "end=32",
            "stride=1",
            "start=4",
            "start=0",
            "start=0",
            "end=0",
            "end=0",
            "end=0"
            ]
    # Expected results

# Generated at 2022-06-13 14:16:36.098575
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup = LookupModule()
    lookup.start = 1
    lookup.end = 5
    lookup.stride = 1

    assert lookup.sanity_check() is None, "End was greater than start and stride was positive"

    # Negative stride
    lookup.start = 10
    assert lookup.sanity_check() is None, "End was less than start and stride was negative"

    with pytest.raises(AnsibleError):
        lookup.end = 5
        lookup.stride = 1
        lookup.sanity_check()
    with pytest.raises(AnsibleError):
        lookup.start = 10
        lookup.end = 5
        lookup.stride = 1
        lookup.sanity_check()
    with pytest.raises(AnsibleError):
        lookup.start = 10

# Generated at 2022-06-13 14:16:46.264532
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    module = LookupModule()
    test_cases = (
        ("5", False, None, None, None, None, None),
        ("5-8", True, 5, 8, None, None, None),
        ("2-10/2", True, 2, 10, 2, None, None),
        ("4:host%02d", True, 4, None, None, None, "host%02d")
    )
    for term, expected_outcome, expected_start, expected_end, expected_stride, expected_count, expected_format in test_cases:
        module.reset()
        result = module.parse_simple_args(term)
        assert result == expected_outcome
        if expected_start is None:
            assert module.start == 1
        else:
            assert module.start == expected_start

# Generated at 2022-06-13 14:16:50.269209
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    cur_obj = LookupModule()
    cur_obj.start = 0
    cur_obj.end = None
    cur_obj.count = 5
    cur_obj.stride = 1
    cur_obj.format = "%d"
    return cur_obj.generate_sequence()

# Generated at 2022-06-13 14:17:08.835207
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    # Start and end values with positive value of stride
    assert LookupModule().sanity_check(1, 3) == None

    # Start and end values with negative value of stride
    assert LookupModule().sanity_check(3, 1, -1) == None

    # Start and count values with positive value of stride
    assert LookupModule().sanity_check(1, 3, 1) == None

    # Start and count values with negative value of stride
    assert LookupModule().sanity_check(3, 1, -1) == None

    # Assert error with positive values of stride with end value smaller than start value
    try:
        LookupModule().sanity_check(3, 1)
        assert False, 'Invalid parameters'
    except AnsibleError as e:
        assert 'to count backwards make stride negative' in e.message

   

# Generated at 2022-06-13 14:17:18.054116
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    error_msg = "must specify count or end in with_sequence"
    # Case 1
    test_obj = LookupModule()
    try:
        test_obj.sanity_check()
    except AnsibleError as e:
        assert e.message == error_msg
    # Case 2
    test_obj.count = 5
    try:
        test_obj.sanity_check()
    except AnsibleError as e:
        assert e.message == error_msg
    # Case 3
    test_obj.count = None
    test_obj.end = 0
    try:
        test_obj.sanity_check()
    except AnsibleError as e:
        assert e.message == error_msg


# Generated at 2022-06-13 14:17:30.499275
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    x = LookupModule()
    x.start = 1
    x.count = None
    x.end = None
    x.stride = 1
    x.format = "%d"
    x.sanity_check()
    x.count = None
    x.end = 1
    x.sanity_check()
    x.count = 1
    x.end = None
    x.sanity_check()
    x.count = 1
    x.end = 1
    try:
        x.sanity_check()
    except Exception as e:
        assert isinstance(e, AnsibleError)

    x.count = None
    x.end = 0
    try:
        x.sanity_check()
    except Exception as e:
        assert isinstance(e, AnsibleError)

    x.end = 1

# Generated at 2022-06-13 14:17:43.824991
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    import pytest
    lm = LookupModule()
    lm.start = 1
    lm.end = 100
    lm.stride = 2
    lm.sanity_check()

    lm.count = 10
    with pytest.raises(AnsibleError):
        lm.sanity_check()
    del lm.count
    
    lm.end = None
    lm.count = 10
    lm.sanity_check()
    assert lm.end == 19

    lm.count = 0
    lm.sanity_check()
    assert lm.end == 0
    assert lm.stride == 0
    assert lm.start == 0

    lm.stride = 0
    with pytest.raises(AnsibleError):
        lm.san

# Generated at 2022-06-13 14:17:55.142532
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup = LookupModule()
    lookup.reset()
    lookup.count = 4
    lookup.sanity_check()
    assert(lookup.start == 1)
    assert(lookup.end == 5)
    assert(lookup.stride == 1)

    lookup.reset()
    lookup.count = 0
    lookup.sanity_check()
    assert(lookup.start == 0)
    assert(lookup.end == 0)
    assert(lookup.stride == 0)

    lookup.reset()
    lookup.stride = -1
    lookup.count = 4
    lookup.sanity_check()
    assert(lookup.start == 1)
    assert(lookup.end == -5)
    assert(lookup.stride == -1)

    lookup.reset()

# Generated at 2022-06-13 14:18:04.832198
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.six.moves import cStringIO as StringIO
    import textwrap

# Generated at 2022-06-13 14:18:07.347007
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
  lookup = LookupModule()
  lookup.start = 1
  lookup.end = 1
  lookup.stride = 1
  lookup.s

# Generated at 2022-06-13 14:18:16.046306
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    module = LookupModule()
    module.start = 1
    module.end = 5
    sequence = list(module.generate_sequence())
    assert(sequence == ['1', '2', '3', '4', '5'])
    module.start = 4
    module.end = 2
    module.stride = -1
    sequence = list(module.generate_sequence())
    assert(sequence == ['4', '3', '2'])
    module.stride = 2
    module.start = 4
    module.end = 16
    sequence = list(module.generate_sequence())
    assert(sequence == ['4', '6', '8', '10', '12', '14', '16'])
    module.format = 'testuser%02x'
    module.start = 0
    module.end = 32


# Generated at 2022-06-13 14:18:24.192793
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    # Test non-matching regular expression
    term = ''
    result = LookupModule().parse_simple_args(term)
    expected = False
    assert result == expected

    # Test base case
    term = 'start=4 end=16 stride=2 format=testuser%02x'
    result = LookupModule().parse_simple_args(term)
    expected = False
    assert result == expected

    # Test all numbers
    term = '1-16'
    result = LookupModule().parse_simple_args(term)
    expected = True
    assert result == expected

    # Test missing end
    term = '1'
    result = LookupModule().parse_simple_args(term)
    expected = True
    assert result == expected

    # Test missing end and stride
    term = '1:testuser%02x'

# Generated at 2022-06-13 14:18:37.127759
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create and initialize the object
    test_object = LookupModule()

    # Try with a term using the simple format
    start = 0
    end   = 5
    stride = 1
    test_term = "%d-%d/%d" % (start, end, stride)
    results = test_object.run([test_term], None)
    assert results == ['0', '1', '2', '3', '4', '5']

    # Try with a term using the key-value format
    start = 0
    end   = 5
    stride = 1
    test_term = "start=%d end=%d stride=%d" % (start, end, stride)
    results = test_object.run([test_term], None)

# Generated at 2022-06-13 14:18:52.161494
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup = LookupModule()

    # Test 1: stride positive and end < start
    lookup.end = 10
    lookup.start = 20
    lookup.stride = 2

    try:
        lookup.sanity_check()
        fail('Test 1: stride positive and end < start')
    except AnsibleError:
        pass

    # Test 2: stride negative and end > start
    lookup.stride = -2

    try:
        lookup.sanity_check()
        ok('Test 2: stride negative and end > start')
    except AnsibleError:
        fail('Test 2: stride negative and end > start')

    # Test 3: count number of '%' in format string
    lookup.format = '%d %d'


# Generated at 2022-06-13 14:19:03.643670
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    # A. Simple case : for term='5-8'
    lm.reset()
    lm.parse_simple_args('5-8')
    result = lm.run(['5-8'])
    assert result == [ '5', '6', '7', '8' ]

    # B. A case with stride='2' : for term='5-8/2'
    lm.reset()
    lm.parse_simple_args('5-8/2')
    result = lm.run(['5-8/2'])
    assert result == [ '5', '7' ]

    # C. A case with format='%02d' : for term='5-8:%02d'
    lm.reset()

# Generated at 2022-06-13 14:19:15.046261
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    from ansible.errors import AnsibleError

    print("Testing LookupModule.parse_simple_args ...")

    lm = LookupModule()

    # Test: wrong type
    try:
        lm.parse_simple_args(123)
    except AnsibleError as e:
        print('Catched: %s' % e)
    else:
        raise Exception('LookupModule.parse_simple_args did not catch wrong type')

    # Test: empty string
    if lm.parse_simple_args('') is not False:
        raise Exception('LookupModule.parse_simple_args returned not False for empty string')

    if not lm.parse_simple_args('h'):
        raise Exception('LookupModule.parse_simple_args returned False for "h"')


# Generated at 2022-06-13 14:19:26.805646
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup = LookupModule()
    lookup.start = 0
    lookup.end = 10
    lookup.stride = 1
    lookup.sanity_check()
    assert True

    with pytest.raises(AnsibleError) as error:
        lookup.count = 10
        lookup.sanity_check()
    assert "can't specify both count and end in with_sequence" in str(error)

    with pytest.raises(AnsibleError) as error:
        lookup.count = None
        lookup.sanity_check()
    assert "must specify count or end in with_sequence" in str(error)

    with pytest.raises(AnsibleError) as error:
        lookup.end = 10
        lookup.stride = -1
        lookup.sanity_check()

# Generated at 2022-06-13 14:19:34.659306
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    lm = LookupModule()
    # Simple form start/end
    term = '1-3'
    assert lm.parse_simple_args(term) is True
    assert lm.start == 1
    assert lm.end == 3
    assert lm.stride == 1
    assert lm.format == '%d'
    # Simple form start/end/stride
    term = '1-4/2'
    assert lm.parse_simple_args(term) is True
    assert lm.start == 1
    assert lm.end == 4
    assert lm.stride == 2
    assert lm.format == '%d'
    # Simple form start/end/stride
    term = '1-5/-2'
    assert lm.parse_simple_args(term) is True
   

# Generated at 2022-06-13 14:19:47.514356
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:19:55.304856
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():

    # Test case with arguments 'start=10 end=0 stride=-1'
    l = LookupModule()
    l.reset()
    l.parse_kv_args(parse_kv('start=10 end=0 stride=-1'))

    try:
        l.sanity_check()
    except AnsibleError as e:
        # Error expected because end < start with stride < 0
        assert e.__str__() == 'to count forward don\'t make stride negative'
    else:
        assert False



# Generated at 2022-06-13 14:20:00.236437
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lm = LookupModule()
    lm.end = 5
    lm.stride = 1
    lm.format = '%d'
    assert(list(lm.generate_sequence()) == ['1', '2', '3', '4', '5'])


# Generated at 2022-06-13 14:20:11.771862
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    lookup_module = LookupModule()
    # Tests with arguments given in key=value format
    # Example 1: creating a test_user
    terms = ['start=1 end=100']
    lookup_module.run(terms, None)
    # Example 2: creating a test_user
    terms = ['start=100 end=1']
    lookup_module.run(terms, None)
    # Example 3: creating a test_user
    terms = ['start=1 end=100 format=testuser%02x']
    lookup_module.run(terms, None)
    # Example 4: creating a test_user
    terms = ['start=1 end=100 format=testuser%02x/']

# Generated at 2022-06-13 14:20:20.452156
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    """
    Checks the sanity check using a new set of parameters
    """
    current_class = LookupModule()

    # Setting the parameters and calling the function
    parameters = [(1, 10, 1), (1, 10, -1), (10, 1, 1), (10, 1, -1)]
    for (start, end, stride) in parameters:
        current_class.start = start
        current_class.end = end
        current_class.stride = stride
        current_class.sanity_check()



# Generated at 2022-06-13 14:20:33.863267
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    Lookup = LookupModule(None, None)

    Lookup.format = "%d"
    Lookup.start = 0
    Lookup.end = 2
    Lookup.stride = 1
    assert list(Lookup.generate_sequence()) == ["0", "1", "2"]

    Lookup.start = 2
    Lookup.end = 0
    Lookup.stride = -1
    assert list(Lookup.generate_sequence()) == ["2", "1", "0"]

    Lookup.start = 2
    Lookup.end = 2
    Lookup.stride = -1
    assert list(Lookup.generate_sequence()) == ["2", "1", "0"]

    Lookup.start = 0
    Lookup.end = -2
    Lookup.stride = -1
    assert list

# Generated at 2022-06-13 14:20:43.975447
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    lookup_module.start = 1
    lookup_module.end = 3
    lookup_module.stride = 0
    lookup_module.format = "%d"
    try:
        lookup_module.sanity_check()
    except:
        assert False, 'Incorrectly raised exception for "stride" = 0'
    lookup_module.stride = 1
    try:
        lookup_module.sanity_check()
    except:
        assert False, 'Incorrectly raised exception for "stride" > 0'
    lookup_module.stride = -1
    try:
        lookup_module.sanity_check()
    except:
        assert False, 'Incorrectly raised exception for "stride" < 0'

# Generated at 2022-06-13 14:20:54.339611
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    # Test for positive sequence
    lm = LookupModule()
    lm.start = 3
    lm.end = 13
    lm.stride = 2
    lm.format = "%d"
    assert list(lm.generate_sequence()) == [str(n) for n in range(3,14,2)]

    # Test for negative sequence
    lm.start = 13
    lm.end = 3
    lm.stride = -2
    assert list(lm.generate_sequence()) == [str(n) for n in range(13,2,-2)]

# Generated at 2022-06-13 14:21:02.432983
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    def ex_val_err(start, end, stride, count):
        lookup_module.start = start
        lookup_module.end = end
        lookup_module.stride = stride
        lookup_module.count = count
        try:
            lookup_module.sanity_check()
        except AnsibleError as e:
            return e
        raise Exception("AnsibleError not raised")
    def ex_ans_err(start, end, stride, count, msg):
        error = ex_val_err(start, end, stride, count)
        if msg in error.message:
            return
        raise Exception("Wrong message: " + error.message)
    # count or end

# Generated at 2022-06-13 14:21:11.578807
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = dict(start=0,end=17,stride=5,format='%03x')
    terms = ['start=0 end=17 stride=5 format=%03x']
    variables = dict(foo='bar')

    lookup_obj =  LookupModule()
    res = lookup_obj.run(terms, variables)
    assert( res == ['000', '005', '00a', '00f'])

    res = lookup_obj.run(terms, variables, **args)
    assert( res == ['000', '005', '00a', '00f'])

# Generated at 2022-06-13 14:21:18.790309
# Unit test for method parse_simple_args of class LookupModule

# Generated at 2022-06-13 14:21:23.450282
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    from ansible.plugins.lookup.sequence import LookupModule
    lookup = LookupModule()
    lookup.start = 0
    lookup.end = 10
    lookup.stride = 2
    lookup.sanity_check()
    assert list(lookup.generate_sequence()) == [0, 2, 4, 6, 8, 10]


# Generated at 2022-06-13 14:21:34.574693
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup = LookupModule()
    lookup.start = 0
    lookup.count = None
    lookup.end = 4
    lookup.stride = 1
    lookup.format = "%d"
    actual = [0, 1, 2, 3, 4]
    assert actual == list(lookup.generate_sequence())
    lookup = LookupModule()
    lookup.start = 4
    lookup.count = None
    lookup.end = -1
    lookup.stride = -1
    lookup.format = "%d"
    actual = [4, 3, 2, 1, 0]
    assert actual == list(lookup.generate_sequence())
    lookup = LookupModule()
    lookup.start = 0
    lookup.count = None
    lookup.end = 4
    lookup.stride = 2
    lookup.format = "%d"

# Generated at 2022-06-13 14:21:42.492673
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():

    lookup_obj = LookupModule()
    lookup_obj.start = 4
    lookup_obj.stride = 2
    lookup_obj.end = 16
    lookup_obj.format = 'obj_%02d'

    rc = [x for x in lookup_obj.generate_sequence()]

    assert rc == ['obj_04', 'obj_06', 'obj_08', 'obj_10', 'obj_12', 'obj_14', 'obj_16']

    print('TEST: class LookupModule method generate_sequence: PASS')


# Generated at 2022-06-13 14:21:45.516996
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    lookup_module.start = 0
    lookup_module.end = 0
    lookup_module.stride = 0
    lookup_module.count = 0
    lookup_module.sanity_check()

# Generated at 2022-06-13 14:22:02.366948
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    l = LookupModule()
    l.start = 1
    l.count = None
    l.end = None
    l.stride = 1
    l.format = "%d"
    with pytest.raises(AnsibleError) as excinfo:
        l.sanity_check()
    assert "must" in str(excinfo.value)
    l.end = 1
    with pytest.raises(AnsibleError) as excinfo:
        l.sanity_check()
    assert "can't" in str(excinfo.value)
    l.end = None
    l.count = 1
    with pytest.raises(AnsibleError) as excinfo:
        l.sanity_check()
    assert "can't" in str(excinfo.value)
    l.start = 2


# Generated at 2022-06-13 14:22:10.365085
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    generated_sequence = []

    lookup_module = LookupModule()
    lookup_module.start = 0
    lookup_module.end = 4
    lookup_module.stride = 1

    for i in lookup_module.generate_sequence():
        generated_sequence.append(int(i))

    assert len(generated_sequence) == 5
    assert generated_sequence[0] == 0
    assert generated_sequence[1] == 1
    assert generated_sequence[2] == 2
    assert generated_sequence[3] == 3
    assert generated_sequence[4] == 4

    generated_sequence = []
    lookup_module.start = 5
    lookup_module.end = 6
    lookup_module.stride = 1

    for i in lookup_module.generate_sequence():
        generated_sequence.append(int(i))

   

# Generated at 2022-06-13 14:22:17.187950
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    lookup_module.reset()
    lookup_module.count = None
    lookup_module.end = None
    assert_raises(AnsibleError, "must specify count or end in with_sequence", lookup_module.sanity_check)

    lookup_module.count = 10
    lookup_module.end = 10
    assert_raises(AnsibleError, "can't specify both count and end in with_sequence", lookup_module.sanity_check)

    lookup_module.count = 10
    lookup_module.end = None
    lookup_module.start = 1
    lookup_module.stride = 1
    assert_equal(lookup_module.end, 11)
    # test also with count = 0
    lookup_module.count = 0

# Generated at 2022-06-13 14:22:26.980009
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookupMod = LookupModule()
    lookupMod.start = 1
    lookupMod.end = 10
    lookupMod.stride = 1
    lookupMod.format = "%d"

    lookupMod.sanity_check()

    try:
        lookupMod.end = None
        lookupMod.count = 5
        lookupMod.sanity_check()
    except AnsibleError:
        assert False

    try:
        lookupMod.end = None
        lookupMod.count = 0
        lookupMod.sanity_check()
    except AnsibleError:
        assert False

    try:
        lookupMod.stride = -1
        lookupMod.start = 10
        lookupMod.end = 1
        lookupMod.sanity_check()
    except AnsibleError:
        assert False

    lookupMod.stride = 1
    lookupMod

# Generated at 2022-06-13 14:22:38.174972
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    """Test the generate_sequence method of LookupModule"""
    p = LookupModule()
    p.reset()
    p.start = 3
    p.end = 8
    p.stride = 1
    p.format = "%d"
    l = list(p.generate_sequence())
    assert l == [3, 4, 5, 6, 7, 8]
    p.reset()
    p.start = 0
    p.end = 0
    p.stride = 0
    l = list(p.generate_sequence())
    assert l == [0]
    p.reset()
    p.start = 3
    p.end = 8
    p.stride = 2
    l = list(p.generate_sequence())
    assert l == [3, 5, 7]
    p.reset()
   

# Generated at 2022-06-13 14:22:51.267061
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()


# Generated at 2022-06-13 14:23:03.987439
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    # Set variables
    look = LookupModule()
    look_up = {'start': 1, 'end': 10, 'stride': 1}
    look_up_1 = {'start': 1, 'end': 10, 'stride': -1}
    look_up_2 = {'start': 10, 'end': 1, 'stride': 1}
    look_up_3 = {'start': 10, 'end': 1, 'stride': -1}
    # Positive test
    look.start = look_up['start']
    look.end = look_up['end']
    look.stride = look_up['stride']
    try:
        look.sanity_check()
        assert True
    except AnsibleError:
        assert False
    # Negative test with positive stride
    look.start = look_

# Generated at 2022-06-13 14:23:12.426596
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    _list = []
    l = LookupModule()


# Generated at 2022-06-13 14:23:24.296013
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    start = 10
    count = 5
    item = LookupModule()
    item.start = start
    item.count = count

    # count and end specified
    end = 0
    stride = -1
    item.end = end
    item.stride = stride
    try:
        item.sanity_check()
    except Exception as exc:
        assert exc.message == "can't specify both count and end in with_sequence"

    # stride not set
    item = LookupModule()
    item.start = 0
    item.end = 1
    try:
        item.sanity_check()
    except Exception as exc:
        assert exc.message == "must specify count or end in with_sequence"

    # stride value negative and start > end
    item = LookupModule()
    item.start = 2