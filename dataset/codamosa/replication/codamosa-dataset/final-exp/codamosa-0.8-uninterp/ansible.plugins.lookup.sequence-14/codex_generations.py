

# Generated at 2022-06-13 14:13:39.480822
# Unit test for method parse_kv_args of class LookupModule
def test_LookupModule_parse_kv_args():
    lookup = LookupModule()
    lookup.reset()
    lookup.parse_kv_args(dict(start=5, end=11, stride=2))
    assert lookup.start == 5
    assert lookup.end == 11
    assert lookup.stride == 2
    assert lookup.count is None
    assert lookup.format == "%d"


# Generated at 2022-06-13 14:13:50.541106
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    """
    Test LookupModule.generate_sequence
    """
    # Basic tests of object return
    assert list(LookupModule().generate_sequence()) == []

    assert list(LookupModule(start=5).generate_sequence()) == ["1",
                                                              "2",
                                                              "3",
                                                              "4",
                                                              "5"]

    assert list(LookupModule(end=5, format="%d").generate_sequence()) == ["1",
                                                                          "2",
                                                                          "3",
                                                                          "4",
                                                                          "5"]


# Generated at 2022-06-13 14:13:59.186087
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    lookup_module.count = None
    lookup_module.end = None
    lookup_module.sanity_check()
    lookup_module.count = None
    lookup_module.end = 0
    lookup_module.sanity_check()
    lookup_module.count = 0
    lookup_module.end = None
    lookup_module.sanity_check()
    lookup_module.count = 0
    lookup_module.end = 0
    lookup_module.sanity_check()
    lookup_module.count = 1
    lookup_module.end = 0
    lookup_module.sanity_check()
    lookup_module.count = 2
    lookup_module.end = 1
    lookup_module.sanity_check()
    lookup_module.count = -1

# Generated at 2022-06-13 14:14:10.093704
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    l = LookupModule()

    # Simple
    l.start = 1
    l.end = 5
    l.stride = 1
    l.format = "%02d"
    assert list(l.generate_sequence()) == ["01", "02", "03", "04", "05"]

    # Count
    l.start = 0x0f00
    l.count = 4
    l.format = "%04x"
    assert list(l.generate_sequence()) == ["0f00", "0f01", "0f02", "0f03"]

    # Stride
    l.start = 1
    l.end = 11
    l.stride = 2
    assert list(l.generate_sequence()) == ["1", "3", "5", "7", "9"]
    l.start = 1


# Generated at 2022-06-13 14:14:16.553774
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        "0x0f00",
        "start=0x0f00 count=4 format=%04x",
        "start=0 count=5 stride=2",
        "start=1 count=5 stride=2",
        "10-0/-1",
        "10:host%02d",
        "10 end=20",
    ]

# Generated at 2022-06-13 14:14:22.326182
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=unused-import
    from ansible.playbook.play_context import PlayContext
    
    lookup_plugin = LookupModule()
    # invoke run() method with parameters
    actual_result = lookup_plugin.run(
        [
            'start=5'
        ],
        dict(),
    )
    # assert actual result with expected result
    assert actual_result == ['1', '2', '3', '4', '5']


# Generated at 2022-06-13 14:14:31.976394
# Unit test for method parse_kv_args of class LookupModule
def test_LookupModule_parse_kv_args():
    args = {
        'count': '3',
        'stride': '1',
        'start': '0',
        'end': '2',
        'format': '%d'
    }
    lookup_obj = LookupModule()
    lookup_obj.parse_kv_args(args)
    assert lookup_obj.start == 0
    assert lookup_obj.end == 2
    assert lookup_obj.stride == 1
    assert lookup_obj.count == 3
    assert lookup_obj.format == '%d'


# Generated at 2022-06-13 14:14:41.295736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Imports
    import os
    import json
    import tempfile

    # Globals
    options = dict()
    options["_ansible_verbosity"] = 4
    options["_ansible_syslog_facility"] = "LOG_USER"

    # Create temp file on disk
    _, temp_path = tempfile.mkstemp()

    # Remove the file
    os.remove(temp_path)

    # Instantiate LookupModule class
    lookup_module = LookupModule()

    # Run the tests
    result = lookup_module.run(["5"], variables=None, **options)
    assert result == ["1", "2", "3", "4", "5"]

    result = lookup_module.run(["5-8"], variables=None, **options)

# Generated at 2022-06-13 14:14:50.111546
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    # Test with a None term
    assert SHORTCUT.match(None) is None

    # Test with a term with only one starting digit
    assert SHORTCUT.match("5") is None

    # Test with a term with only one starting digit, a dash and an ending digit
    assert SHORTCUT.match("2-10") is not None

    # Test with a term with only one starting digit, a dash, an ending digit and
    # a slash
    assert SHORTCUT.match("2-10/2") is not None

    # Test with a term with only one starting digit, a dash, an ending digit, a
    # slash and a colon
    assert SHORTCUT.match("2-10/2:testuser%02x") is not None

    # Test with a term with only one starting digit, a dash, an ending digit

# Generated at 2022-06-13 14:15:02.702173
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    args = LookupModule()
    # Term test_case[0] is the value we try to parse, the remaining ones are the
    # expected results, if any.
    # start is None if the '-' is missing
    # end is None if the '-' is missing
    # stride is None if the '/' is missing
    # format is None if the ':' is missing
    test_cases = (
        ("5", 1, 5, None, None),
        ("5-8", 5, 8, None, None),
        ("2-10/2", 2, 10, 2, None),
        ("4:host%02d", 4, None, None, 'host%02d'),
        ("0xff00:host%04x", 0xff00, None, None, 'host%04x'),
    )


# Generated at 2022-06-13 14:15:12.235721
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    setattr(lookup_module, 'start', 0)
    setattr(lookup_module, 'end', None)
    setattr(lookup_module, 'stride', 1)
    setattr(lookup_module, 'format', "%d")

    try:
        lookup_module.sanity_check()
    except:
        pass
    else:
        assert False


# Generated at 2022-06-13 14:15:19.526211
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
  input_end = 10
  input_count = 0
  input_stride = 0
  input_start = 6
  
  lu = LookupModule()
  
  with pytest.raises(AnsibleError):
    lu.sanity_check()

  lu.count = input_count
  lu.end = None
  lu.stride = input_stride
  lu.start = input_start

  with pytest.raises(AnsibleError):
    lu.sanity_check()

  lu.count = input_count
  lu.end = input_end
  lu.stride = input_stride
  lu.start = input_start

  with pytest.raises(AnsibleError):
    lu.sanity_check()

  lu

# Generated at 2022-06-13 14:15:26.266411
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup = LookupModule()
    lookup.sanity_check()  # no exception is expected here
    lookup.start = 1
    lookup.end = 2
    lookup.sanity_check()  # no exception is expected here
    lookup.start = 2
    lookup.end = 1
    lookup.stride = 1
    try:
        lookup.sanity_check()
    except AnsibleError as e:
        assert "to count backwards make stride negative" in str(e)

# Generated at 2022-06-13 14:15:33.703524
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    lookup = LookupModule()
    assert not lookup.parse_simple_args('')
    assert not lookup.parse_simple_args('a=1')
    assert not lookup.parse_simple_args('10') #arguments should be start and end
    assert not lookup.parse_simple_args('1-10-10') #arguments are start, end and stride
    assert not lookup.parse_simple_args('10-10/10') #arguments are end and stride
    assert not lookup.parse_simple_args('10-/10') #arguments are end and stride
    assert not lookup.parse_simple_args('-10/10') #arguments are end and stride
    assert not lookup.parse_simple_args('10-10/') #arguments are end and stride
    assert not lookup.parse_simple_args('/10') #

# Generated at 2022-06-13 14:15:44.019851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term = '2-10/2'
    numbers = [2, 4, 6, 8, 10]
    assert LookupModule().run(terms=term, variables={
    }) == numbers, 'running sequence with values(2-10/2) should return ' + numbers.__str__()

    terms = {
        "start": 2,
        "end": 10,
        "stride": 2,
        "format": "%02x",
    }
    format_numbers = ['02', '04', '06', '08', '0a']
    assert LookupModule().run(terms=terms, variables={
    }) == format_numbers, 'running sequence with ' + terms.__str__() + ' should return ' + format_numbers.__str__()
    terms['format'] = '%2c'

# Generated at 2022-06-13 14:15:55.114544
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    t = LookupModule()
    assert list(t.generate_sequence()) == []
    t.start = 0
    t.end = 0
    t.stride = 0
    assert list(t.generate_sequence()) == []
    t.stride = 1
    assert list(t.generate_sequence()) == ['0']
    t.end = -1
    assert list(t.generate_sequence()) == []
    t.end = 1
    assert list(t.generate_sequence()) == ['0', '1']
    t.end = 2
    assert list(t.generate_sequence()) == ['0', '1', '2']
    t.end = 3
    assert list(t.generate_sequence()) == ['0', '1', '2', '3']
    t.end = 4
   

# Generated at 2022-06-13 14:16:05.253281
# Unit test for method parse_simple_args of class LookupModule

# Generated at 2022-06-13 14:16:15.218008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First test, shorthand form, even numbers between 1 and 10
    result = LookupModule().run([u"1-10/2"], variables={}, **{})
    assert result == [u'1', u'3', u'5', u'7', u'9']

    # Second test, key-value form, odd numbers between 1 and 10
    result = LookupModule().run([u"start=1 end=10 stride=2"], variables={}, **{})
    assert result == [u'1', u'3', u'5', u'7', u'9']

    # Third test, with_subelements and count.
    # More subelements than items in sequence.
    result = LookupModule().run([u"1-10/2"], variables={}, with_subelements=True, **{})

# Generated at 2022-06-13 14:16:22.662788
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():

    look_up = LookupModule()

    # Test case 1: For shortcut format: start-end/stride:format
    result = look_up.parse_simple_args("5-12/2:debug%02d")
    assert result == True
    assert look_up.start == 5
    assert look_up.end == 12
    assert look_up.stride == 2
    assert look_up.format == "debug%02d"

    # Test case 2: For shortcut format: start-end/stride
    result = look_up.parse_simple_args("5-12/2")
    assert result == True
    assert look_up.start == 5
    assert look_up.end == 12
    assert look_up.stride == 2
    assert look_up.format == "%d"

    # Test case 3: For

# Generated at 2022-06-13 14:16:35.443577
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup = LookupModule()
    # testing generation of list without format
    lookup.start = 1
    lookup.count = 10
    lookup.stride = 2

    result = list(lookup.generate_sequence())
    assert result == [1, 3, 5, 7, 9]
    # testing the case : end = start (even numbers)
    lookup.start = 0
    lookup.end = 0
    lookup.stride = 2
    result = list(lookup.generate_sequence())
    assert result == [0]
    lookup.start = 0
    lookup.end = 5
    lookup.stride = 2
    result = list(lookup.generate_sequence())
    assert result == [0, 2, 4]
    # testing the case : end < start (even numbers)
    lookup.start = 5

# Generated at 2022-06-13 14:16:48.158131
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    args = LookupModule()
    res = args.parse_simple_args("1-1")
    assert res == True
    assert args.start == 1
    assert args.count == None
    assert args.end == 1
    assert args.stride == 1
    assert args.format == "%d"

    args = LookupModule()
    res = args.parse_simple_args("1-1/1")
    assert res == True
    assert args.start == 1
    assert args.count == None
    assert args.end == 1
    assert args.stride == 1
    assert args.format == "%d"

    args = LookupModule()
    res = args.parse_simple_args("1-1:test")
    assert res == True
    assert args.start == 1
    assert args.count == None
    assert args

# Generated at 2022-06-13 14:17:01.329607
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    print("\n===== Test parse_simple_args =====")
    lm = LookupModule()
    lm.reset()

    print("---- Invalid terms ----")

# Generated at 2022-06-13 14:17:03.406848
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    module = LookupModule()
    assert module.stride >= 0



# Generated at 2022-06-13 14:17:12.706131
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lm = LookupModule()
    assert(lm.sanity_check() == None)
    lm.end = 2
    lm.start = 2
    lm.stride = 2
    try:
        lm.sanity_check()
    except:
        pass
    else:
        assert "Expected sanity_check to throw exception when end == start and stride > 0"
    lm.end = 4
    lm.start = 2
    lm.stride = 2
    lm.sanity_check()



# Generated at 2022-06-13 14:17:20.767419
# Unit test for method parse_simple_args of class LookupModule

# Generated at 2022-06-13 14:17:31.997961
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup_module = LookupModule()
    lookup_module.start = 1
    lookup_module.end = 10
    lookup_module.stride = 1
    lookup_module.format = "%s"

    result = []
    for i in lookup_module.generate_sequence():
        result.append(i)
    assert result == ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    result = []
    lookup_module.start = 4
    lookup_module.end = 10
    for i in lookup_module.generate_sequence():
        result.append(i)
    assert result == ["4", "5", "6", "7", "8", "9", "10"]

    result = []
    lookup_module.start = 10
    lookup_

# Generated at 2022-06-13 14:17:44.790940
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test for correct results
    l = LookupModule()
    assert l.run(terms='1-4', variables=None) == ['1', '2', '3', '4']
    assert l.run(terms='0x12-0x15', variables=None) == ['18', '19', '20', '21']
    assert l.run(terms='0b11-0b100', variables=None) == ['3', '4']
    assert l.run(terms='3-1', variables=None) == []
    assert l.run(terms='3-1/1', variables=None) == []
    assert l.run(terms='3-1/-1', variables=None) == ['3', '2', '1']
    assert l.run(terms='0-0', variables=None) == ['0']

# Generated at 2022-06-13 14:17:46.615531
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup_module = LookupModule()
    lookup_module.sanity_check()

# Generated at 2022-06-13 14:17:57.170921
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # All tests have to be run with the same object instance, because
    # LookupModule stores its state in self.start, self.count, etc.
    l = LookupModule()
    assert list(l.generate_sequence()) == []
    # Test for handling of a bad format string
    l.reset()
    try:
        l.format = "%%"
        l.generate_sequence()
        assert False, "Should have gotten error"
    except AnsibleError:
        pass
    # Test for handling of bad arguments

# Generated at 2022-06-13 14:18:09.192727
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup = LookupModule()
    lookup.start = 2
    lookup.end = 10
    lookup.stride = 1

    # Test for error if format contains more than one %
    lookup.format = '%d'
    assert list(lookup.generate_sequence()) == ['2', '3', '4', '5', '6', '7', '8', '9', '10']

    # Test for ValueError if format is bad
    lookup.format = '%d %d'
    try:
        list(lookup.generate_sequence())
    except ValueError:
        pass
    else:
        assert False

    # Test for TypeError if number is not integer

    lookup.start = 2.3
    lookup.format = '%d'

# Generated at 2022-06-13 14:18:17.467417
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    l = LookupModule()
    l.start = 0
    l.end = 4
    l.stride = 1
    l.format = "%d"

    assert l.generate_sequence() == ['0', '1', '2', '3', '4']



# Generated at 2022-06-13 14:18:22.203088
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    l = LookupModule()
    l.start = 0
    l.end = 4
    l.format = "test%d"

    assert list(l.generate_sequence()) == ['test0', 'test1', 'test2', 'test3', 'test4']

    l.stride = 2
    assert list(l.generate_sequence()) == ['test0', 'test2', 'test4']


# Generated at 2022-06-13 14:18:34.673177
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():

    gen = LookupModule()

    # testing for negative strides
    gen.start = 5
    gen.end = 10
    gen.stride = -1
    result = list(gen.generate_sequence())
    assert(len(result) == 0)

    gen.end = -1
    gen.stride = -1
    result = list(gen.generate_sequence())
    assert(len(result) == 5)
    assert(result == ["5", "4", "3", "2", "1"])

    # testing format string
    gen.start = 1
    gen.end = 10
    gen.stride = 1
    gen.format = "%02d"
    result = list(gen.generate_sequence())
    assert(len(result) == 10)

# Generated at 2022-06-13 14:18:44.182974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    y9 = []
    y10 = []
    y11 = []
    y12 = []
    y13 = []

    lookup_module = LookupModule()
    result1 = lookup_module.run([
        'start=5 end=8 format=testuser%02x'], variables=None, **{})
    result2 = lookup_module.run([
        '5-8'], variables=None, **{})
    result3 = lookup_module.run([
        '5-'], variables=None, **{})
    result4 = lookup_module.run([
        '-4'], variables=None, **{})


# Generated at 2022-06-13 14:18:56.188058
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_class = LookupModule()

# Generated at 2022-06-13 14:19:05.953142
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    print("Testing LookupModule_sanity_check")

    lookup_module = LookupModule()
    lookup_module.start = 5
    lookup_module.count = 4
    lookup_module.end = None
    lookup_module.stride = 1
    lookup_module.sanity_check()

    lookup_module = LookupModule()
    lookup_module.start = 5
    lookup_module.count = 0
    lookup_module.end = 0
    lookup_module.stride = 0
    lookup_module.sanity_check()

    lookup_module = LookupModule()
    lookup_module.start = 5
    lookup_module.count = -2
    lookup_module.end = None
    lookup_module.stride = 1
    with pytest.raises(AnsibleError):
        lookup_module.sanity

# Generated at 2022-06-13 14:19:17.285956
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    assert LookupModule.parse_simple_args("start=0 end=0") == False
    assert LookupModule.parse_simple_args("start=0 end=0/0") == False
    assert LookupModule.parse_simple_args("start=0 end=0/0:hi") == False
    assert LookupModule.parse_simple_args("0") == True
    assert LookupModule.parse_simple_args("0/0") == True
    assert LookupModule.parse_simple_args("0/0:hi") == True
    assert LookupModule.parse_simple_args("0:hi") == True
    assert LookupModule.parse_simple_args("0-0") == True
    assert LookupModule.parse_simple_args("0-0/0") == True
    assert LookupModule.parse_simple_args

# Generated at 2022-06-13 14:19:28.754379
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    # Test success
    tl = LookupModule()
    tl.start = 1
    tl.end = 3
    tl.stride = 1
    tl.format = "%d"
    tl.sanity_check()

    # Test failure
    tl = LookupModule()
    tl.start = 1
    tl.end = 3
    tl.stride = 1
    tl.format = "%d"
    tl.count = 4
    try:
        tl.sanity_check()
        raise
    except AnsibleError as e:
        assert "can't specify both count and end in with_sequence" in e.message

    # Test failure
    tl = LookupModule()
    tl.start = 1
    tl.stride = 1

# Generated at 2022-06-13 14:19:35.716362
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    instance = LookupModule()
    # Sequence from 0 to 5 with a step of 1.
    instance.start = 0
    instance.end = 5
    instance.stride = 1
    expected = ['0', '1', '2', '3', '4', '5']
    assert list(instance.generate_sequence()) == expected
    # Sequence from 0 to 5 with a step of 2.
    instance.start = 0
    instance.end = 5
    instance.stride = 2
    expected = ['0', '2', '4']
    assert list(instance.generate_sequence()) == expected
    # Sequence from 0 to 5 with a step of -1.
    instance.start = 0
    instance.end = 5
    instance.stride = -1
    expected = ['0', '1', '2', '3', '4']

# Generated at 2022-06-13 14:19:48.160277
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    t = LookupModule()
    t.start = 1
    t.end = 5
    t.stride = 1
    t.format = "%d"
    assert list(t.generate_sequence()) == ['1','2','3','4','5']
    assert list(t.generate_sequence()) == list(t.generate_sequence())
    t = LookupModule()
    t.start = 1
    t.count = 5
    t.stride = 1
    t.format = "%d"
    assert list(t.generate_sequence()) == ['1','2','3','4','5']
    t = LookupModule()
    t.start = 5
    t.end = 8
    t.stride = 1
    t.format = "%d"

# Generated at 2022-06-13 14:20:02.784579
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lm = LookupModule()
    lm.start = 0
    lm.count = 4
    lm.stride = 2
    counted = lm.generate_sequence()
    assert counted == ["0", "2", "4", "6"]

# Generated at 2022-06-13 14:20:14.017171
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Generate a sequence of integers from 1 to 5 with default values for start, end, stride and format"""
    test_obj = LookupModule()
    test_obj.reset()
    test_str = "1-5"
    test_terms = [test_str]
    test_vars = {}
    test_kwargs = {}
    returned = test_obj.run(test_terms, test_vars, **test_kwargs)
    assert returned == ["1", "2", "3", "4", "5"]

    """Generate a sequence of integers from 1 to 9 by steps of 2 with default values for start, end, stride and format"""
    test_obj = LookupModule()
    test_obj.reset()
    test_str = "1-9/2"
    test_terms = [test_str]
    test

# Generated at 2022-06-13 14:20:22.745971
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    module = LookupModule()
    assert module.run(['3-10/2'], {}) == [3,5,7,9]
    assert module.run(['3-10/-2'], {}) == []
    assert module.run(['-3--10/-2'], {}) == [-3, -5, -7, -9]
    assert module.run(['1-1'], {}) == []
    assert module.run(['0x01-0x01'], {}) == []
    assert module.run(['-10-10'], {}) == []


# Generated at 2022-06-13 14:20:31.025755
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    l = LookupModule()
    l.lookup_kind = "sequence"
    l.lookup_basedir = ""

    terms = [
        'start=5 end=11 stride=2 format=0x%02x',
        'count=5'
    ]

    result = l.run(terms, None)

    assert type(result) is list
    assert result == [ "0x05", "0x07", "0x09", "0x0a", "1", "2", "3", "4", "5"]

# Generated at 2022-06-13 14:20:39.058812
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    # Test for method generate_sequence(self)
    #
    #   Will create a lookup object with the start of 1, end of 2 and stride
    #   of 2. This will return ['1', '2']. We then call the generate_sequence
    #   method and verify it returns data.
    #

    # Verify the method returns a list with the correct data
    #
    # There are other tests in the test_lookup_plugins.py that verify the
    # sequence generator works correctly.
    lookup_obj = LookupModule()
    lookup_obj.start = 1
    lookup_obj.end = 2
    lookup_obj.stride = 2
    assert(list(lookup_obj.generate_sequence()) == ['1', '2'])

# Generated at 2022-06-13 14:20:51.671056
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup_module = LookupModule()
    lookup_module.reset()
    lookup_module.start = 2
    lookup_module.end = 8
    lookup_module.stride = 3
    lookup_module.format = '%02d'
    sequence = lookup_module.generate_sequence()
    assert(list(sequence) == ['02', '05', '08'])

    lookup_module = LookupModule()
    lookup_module.reset()
    lookup_module.start = 10
    lookup_module.end = -3
    lookup_module.stride = -2
    lookup_module.format = '%02d'
    sequence = lookup_module.generate_sequence()
    assert(list(sequence) == ['10', '08', '06', '04'])

    lookup_module = LookupModule()
    lookup

# Generated at 2022-06-13 14:21:01.195681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print ("testing LookupModule.run")

    # Exercise the sequence generator, print the result and compare to
    # expected output
    my_result = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20"
    ]

    lkup_obj = LookupModule()
    result = lkup_obj.run(["count=21"], {})

    # Print the result (for manual debug) and compare to expected output
    print("result : ")

# Generated at 2022-06-13 14:21:13.978354
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create test object
    lm = LookupModule()

    # Declare some helpful vars
    a = 1
    b = 10
    c = 2

    # Test different options
    # Option : with_sequence: start=a end=b stride=c
    # Expected result : ['1', '3', '5', '7', '9']
    terms = "start=%d end=%d stride=%d" % (a, b, c)
    results = lm.run(terms, variables=dict())
    assert results == ['1', '3', '5', '7', '9']

    # Option : with_sequence: a-b
    # Expected result : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Generated at 2022-06-13 14:21:18.901013
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    sequence = LookupModule()
    sequence.count = 6
    sequence.start = 1
    sequence.end = 0
    sequence.stride = -1
    sequence.sanity_check()
    assert sequence.end == 6
    sequence.count = None
    sequence.start = 0
    sequence.end = 0
    sequence.stride = 0
    sequence.sanity_check()
    assert sequence.end == 0

# Generated at 2022-06-13 14:21:29.869589
# Unit test for method parse_simple_args of class LookupModule
def test_LookupModule_parse_simple_args():
    l = LookupModule()

    # Test for shortcut format without specifying start
    term = "5-8"
    if not l.parse_simple_args(term):
        raise AssertionError("Failed to parse shortcut format without specifying start")
    if l.start != 1:
        raise AssertionError("Start is not 1", term)
    if l.end != 8:
        raise AssertionError("End is not 8", term)
    if l.stride != 1:
        raise AssertionError("Stride is not 1", term)
    if l.format != '%d':
        raise AssertionError("Format is not %d", term)

    # Test for shortcut format with specifying start
    term = "0-8"
    if not l.parse_simple_args(term):
        raise AssertionError

# Generated at 2022-06-13 14:21:43.574136
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    list = [{'name': 'first', 'value': 1, 'stride': 2, 'format': 'test%02d'}, {'name': 'second', 'end': 5, 'format': 'test%02d'}]
    lookup_module = LookupModule()
    results = lookup_module.run(list, variables=None)
    assert(results == ['test01', 'test03', 'test05', 'test02', 'test04'])

# Generated at 2022-06-13 14:21:47.886267
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test for method run of class LookupModule
    # Result of lookup is supposed to be string.
    # The sequence plugin returns a list of ints.
    # The expected result is a list of strings
    term = "start=1 end=10"
    variables = None

    result = LookupModule().run(term, variables)

    assert len(result) == 9
    is_string_list = all([isinstance(i, str) for i in result])
    assert is_string_list

# Generated at 2022-06-13 14:21:59.372874
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    sequence = LookupModule()
    sequence.start = 1
    sequence.stride = 1
    sequence.format = "%d"
    expected = ["3", "4", "5", "6", "7", "8", "9"]
    result = sequence.generate_sequence(3, 9)
    assert expected == list(result)

    sequence = LookupModule()
    sequence.start = 3
    sequence.stride = 1
    sequence.format = "%x"
    expected = ["f", "10", "11", "12", "13", "14", "15"]
    result = sequence.generate_sequence(3, 15)
    assert expected == list(result)

    sequence = LookupModule()
    sequence.start = 3
    sequence.stride = 3
    sequence.format = "%d"

# Generated at 2022-06-13 14:22:08.793557
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():    # pylint: disable=invalid-name
    """Unit test for method LookupModule.generate_sequence"""

    # trivial cases
    assert list(LookupModule(None, {}).generate_sequence()) == []
    assert list(LookupModule(None, {}).generate_sequence(start=1)) == []
    assert list(LookupModule(None, {}).generate_sequence(start=1, format='%d')) == []

    # some simple cases
    assert list(LookupModule(None, {}).generate_sequence(start=1, end=3)) == ["1", "2", "3"]
    assert list(LookupModule(None, {}).generate_sequence(end=2)) == ["1", "2"]

# Generated at 2022-06-13 14:22:22.375383
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    assert LookupModule.sanity_check(None, start=0, end=5, stride=1) == None
    try:
        LookupModule.sanity_check(None, end=5)
    except AnsibleError:
        pass
    else:
        assert False
    try:
        LookupModule.sanity_check(None, count=5, end=5)
    except AnsibleError:
        pass
    else:
        assert False
    try:
        LookupModule.sanity_check(None, start=6, end=5, stride=1)
    except AnsibleError:
        pass
    else:
        assert False
    try:
        LookupModule.sanity_check(None, start=5, end=6, stride=-1)
    except AnsibleError:
        pass

# Generated at 2022-06-13 14:22:29.689282
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup = LookupModule()
    lookup.format = '%02d'
    assert list(lookup.generate_sequence()) == ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

    lookup.start = 4
    assert list(lookup.generate_sequence()) == ['04', '05', '06', '07', '08', '09', '10']

    lookup.end = 13
    assert list(lookup.generate_sequence()) == ['04', '05', '06', '07', '08', '09', '10', '11', '12', '13']

    lookup.stride = 2
    assert list(lookup.generate_sequence()) == ['04', '06', '08', '10', '12', '14']


# Generated at 2022-06-13 14:22:39.895817
# Unit test for method sanity_check of class LookupModule
def test_LookupModule_sanity_check():
    lookup = LookupModule()
    lookup.start = 0       # not specified in test for
    lookup.stride = 0      # LookupModule.sanity_check
    lookup.end = 5         # method, so it is Zero
    lookup.format = "%d"
    lookup.count = 5

    with pytest.raises(AnsibleError) as excinfo:
        lookup.sanity_check()
    assert "can't specify both count and end in with_sequence" in str(excinfo.value)
    lookup.count = None
    lookup.end = None
    with pytest.raises(AnsibleError) as excinfo:
        lookup.sanity_check()
    assert "must specify count or end in with_sequence" in str(excinfo.value)
    lookup.count = 5
    lookup.sanity_check

# Generated at 2022-06-13 14:22:52.166619
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    """
    Check multiple combinations of arguments to generate_sequence()
    """

    # test_LookupModule_generate_sequence() will generate 12 tests with
    # 2 x 3 x 2 x 2 combinations of arguments:

    # 1. start = [1, 5]
    # 2. end = [10, 15]
    # 3. stride = [1, -1]
    # 4. format = ['%d', '%x']

    from parameterized import parameterized
    import inspect
    import sys


# Generated at 2022-06-13 14:23:05.087727
# Unit test for method generate_sequence of class LookupModule

# Generated at 2022-06-13 14:23:09.654731
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup = LookupModule()
    lookup.start = 1
    lookup.end = 32
    lookup.stride = 1
    lookup.format = "%01d"
    expected = [str(v) for v in range(1,33)]
    assert lookup.generate_sequence() == expected

# Generated at 2022-06-13 14:23:28.157222
# Unit test for method generate_sequence of class LookupModule
def test_LookupModule_generate_sequence():
    lookup = LookupModule()
    lookup.format = "%d"
    lookup.start = 3
    lookup.end = 10
    lookup.stride = 2
    results = [x for x in lookup.generate_sequence()]
    assert results == ["3", "5", "7", "9"]
    lookup.start = 13
    lookup.end = 17
    lookup.stride = 1
    results = [x for x in lookup.generate_sequence()]
    assert results == ["13", "14", "15", "16", "17"]
    lookup.start = 0xFF
    lookup.end = 0x107
    lookup.stride = 1
    lookup.format = "0x%04x"
    results = [x for x in lookup.generate_sequence()]