

# Generated at 2022-06-13 15:38:41.981451
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestResult("something")
    assert(test_result.get_xml_element().tag == 'result')
    assert(test_result.get_xml_element().text == "something")


# Generated at 2022-06-13 15:38:51.639629
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    import datetime
    a = TestSuite('names')
    a.timestamp = None
    a = TestSuite('names')
    a.timestamp = datetime.datetime.now()
    b = TestSuite('names')
    c = TestSuite('names')
    a.timestamp = '1234'
    b.timestamp = datetime.datetime.now()
    assert a.get_attributes() != b.get_attributes()
    assert c.get_attributes() == b.get_attributes()
    a = TestSuite('names')
    b = TestSuite('names')
    c = TestSuite('names')
    d = TestSuite('names')
    a.timestamp = datetime.datetime.now().isoformat(timespec='seconds')

# Generated at 2022-06-13 15:39:01.554588
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name='test_name',
        hostname='test_hostname',
        id='test_id',
        package='test_package',
        timestamp=datetime.datetime(2020, 2, 10, 11, 34, 4),
        properties={'key1': 'value1', 'key2': 'value2'},
        cases=[TestCase(name='test_case_name', assertions=0, classname='test_classname', status='test_status', time=0)]
    )
    suite_xml = suite.get_xml_element()
    assert(suite_xml.tag == 'testsuite')
    assert(suite_xml.attrib['name'] == suite.name)
    assert(suite_xml.attrib['hostname'] == suite.hostname)

# Generated at 2022-06-13 15:39:04.844662
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    error = TestError('an error occured', message='a message', type='error')
    assert error.get_attributes() == {
        'message': 'a message',
        'type': 'error'
    }



# Generated at 2022-06-13 15:39:16.961690
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    expected='''<testsuite errors="0" failures="0" hostname="x.x.x.x" id="1" name="TestSuite" package="com.package.name" skipped="0" tests="1" time="0">
  <testcase assertions="1" classname="com.package.name.ClassName" name="test_case_name" status="PASS" time="0"><system-out>TestCase Output</system-out></testcase>
</testsuite>'''

    case = TestCase(name='test_case_name', assertions=1, classname='com.package.name.ClassName')
    case.system_out = 'TestCase Output'

    suite = TestSuite(name='TestSuite', hostname='x.x.x.x', id='1', package='com.package.name')

# Generated at 2022-06-13 15:39:21.698508
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    expected_attributes = {'type': 'some type', 'message': 'some message'}

    test_result = TestFailure(type='some type', message='some message')

    assert(test_result.get_attributes() == expected_attributes)


# Generated at 2022-06-13 15:39:29.364492
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    # type: () -> None
    """Test method get_xml_element of class TestResult."""

    # testcase: TestResult attributes
    test_result = TestResult()

    # TestResult.output
    test_result.output = b'output'
    result = test_result.get_xml_element()
    assert result.text == 'output'

    test_result.output = 'output'
    result = test_result.get_xml_element()
    assert result.text == 'output'

    test_result.output = 'output\n'
    result = test_result.get_xml_element()
    assert result.text == 'output\n'

    test_result.output = 'output\r\n'
    result = test_result.get_xml_element()

# Generated at 2022-06-13 15:39:34.221636
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    output = 'this is the output'
    message = 'this is the message'
    type = 'this is the type'

    test_result = TestResult(output, message, type)
    assert test_result.get_attributes() == dict(message='this is the message', type='this is the type')


# Generated at 2022-06-13 15:39:37.750141
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    result = TestError(output='failure', message='test', type='test')
    assert result.get_attributes() == {'message': 'test', 'type': 'test'}


# Generated at 2022-06-13 15:39:45.305288
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    output = "zzz"
    message = "xxx"
    type = "yyy"
    tr = TestError(output, message, type)
    assert _attributes(
            message=message,
            type=type,
        ) == tr.get_attributes()
    tr = TestError(output, message)
    assert _attributes(
            message=message,
            type=type,
        ) != tr.get_attributes()
    tr = TestError(output)
    assert _attributes(
            message=message,
            type=type,
        ) != tr.get_attributes()
    tr = TestError()
    assert _attributes(
            message=message,
            type=type,
        ) != tr.get_attributes()
    tr = TestError(output, message, type)
    assert _

# Generated at 2022-06-13 15:39:51.897549
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    result = TestResult(output='output')
    assert result.get_xml_element().text == 'output'
    assert result.get_xml_element().tag == 'system-out'


# Generated at 2022-06-13 15:39:56.956428
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestResult(output='test output', type='test type', message='test message')
    test_result_element = test_result.get_xml_element()

    assert test_result_element.text == 'test output'
    assert test_result_element.get('type') == 'test type'
    assert test_result_element.get('message') == 'test message'


# Generated at 2022-06-13 15:39:59.198547
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testCaseObject = TestCase('TEST', 'TESTING', 'PASSED', '10')
    assert testCaseObject.get_xml_element() is not None


# Generated at 2022-06-13 15:40:08.734462
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Set up
    test_suite = TestSuite(name = 'TestSuite A Name', hostname = 'TestSuite A Hostname', package = 'TestSuite A Package',
                           id = 'TestSuite A Id', timestamp = datetime.datetime(2020, 7, 15, 8, 10, 0, 0),
                           system_out = 'TestSuite A System Out', system_err = 'TestSuite A System Error')

    # Run method to be tested
    result = test_suite.get_xml_element()

    # Assert
    # Assert that the root element is "testsuite"
    assert result.tag == 'testsuite'
    # Assert that all the expected attributes are present
    assert result.attrib['disabled'] == '0'

# Generated at 2022-06-13 15:40:21.237172
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    time = datetime.datetime.now()
    testsuite = TestSuite(
        cases=[
            TestCase(
                classname='TestSuite',
                name='test_TestSuite_get_xml_element',
                time=0.1
            )
        ],
        failures=0,
        hostname='localhost',
        id=1,
        name='TestSuite',
        package='tests',
        skipped=0,
        system_out='',
        system_err='',
        timestamp=time,
        tests=1,
        time=0.1
    )
    xml_element = testsuite.get_xml_element()
    assert xml_element.attrib['classname'] == 'TestSuite'
    assert xml_element.attrib['failures'] == '0'
    assert xml

# Generated at 2022-06-13 15:40:32.385616
# Unit test for method get_xml_element of class TestSuites

# Generated at 2022-06-13 15:40:34.270069
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    tag = ET.Element('failure')
    assert(isinstance(tag, ET.Element))


# Generated at 2022-06-13 15:40:42.496164
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    my_TestSuite = TestSuite(name='my TestSuite',
                             packages = 'my package',
                             id = '1',
                             hostname = 'my hostname',
                             timestamp = 'my timestamp',
                             properties = 'my property',
                             system_out = 'my system_out',
                             system_err = 'my system_err',)
    my_TestCase = TestCase(name='my TestCase')
    my_TestSuite.cases.append(my_TestCase)
    my_TestError = TestError("my TestError")
    my_TestCase.errors.append(my_TestError)
    my_TestFailure = TestFailure("my TestFailure")
    my_TestCase.failures.append(my_TestFailure)

    assert my_TestSuite.get_xml_element

# Generated at 2022-06-13 15:40:50.625597
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name='TestCase',
        assertions='0',
        classname='sdk.test.TestCase',
        status='run',
        time=decimal.Decimal('0.1'),
        errors=[
            TestError(
                output='Traceback (most recent call last):\n',
                message='AssertionError: expected success response but received error',
                type='AssertionError',
            ),
        ],
        failures=[
            TestFailure(
                output='Traceback (most recent call last):\n',
                message='AssertionError: expected success response but received error',
                type='AssertionError',
            ),
        ],
        skipped='1',
        system_out='This is system out',
        system_err='This is system err',
    )
   

# Generated at 2022-06-13 15:40:59.148295
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case1 = TestCase('case1')
    assert test_case1.get_xml_element().__str__() == '<testcase name="case1"/>'
    test_case2 = TestCase('case2',
                          assertions=123,
                          classname='SomeClass',
                          status='OK',
                          time=decimal.Decimal(12.345))
    assert test_case2.get_xml_element().__str__() == '<testcase assertions="123" classname="SomeClass" name="case2" status="OK" time="12.345"/>'
    test_case3 = TestCase('case3')
    test_case3.failures.append(TestFailure('Failure message', 'Failure output', 'Failure type'))
    assert test_case3.get_xml_element().__str__()

# Generated at 2022-06-13 15:41:06.904072
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_output = "Test output"
    test_message = "Test message"
    output = TestOutput(output = test_output, message = test_message)
    assert output.get_xml_element().text == test_output


# Generated at 2022-06-13 15:41:09.766019
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='TestCase1')
    expected_xml_element = '<testcase name="TestCase1" />'
    actual_xml_element = test_case.get_xml_element()
    assert _pretty_xml(actual_xml_element) == expected_xml_element


# Generated at 2022-06-13 15:41:11.039283
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testCase=TestCase(name='TestCase')
    assert testCase.get_xml_element() != None


# Generated at 2022-06-13 15:41:20.917258
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test0 = TestCase(name='test0', assertions = 1, classname='Yolo', status='passed', time=0.0)
    test1 = TestCase(name='test1', assertions = 4)
    test2 = TestCase(name='test2', assertions = 0, classname='Yolo', status='passed', time=0.0)
    test0.errors.append(TestError())
    test2.errors.append(TestError())
    test2.errors.append(TestError())
    test2.failures.append(TestFailure())
    ts = TestSuite(name='testsuite1', hostname='host1', id=1, package='py', timestamp=datetime.datetime.now())
    ts.properties.update(foo='bar')

# Generated at 2022-06-13 15:41:26.395565
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():

    testsuite = TestSuite('GlyphClassLib')
    testsuite.properties = {'engine':'GlyphLib'}
    testsuite.cases.append(TestCase('ZapfDingbats case 4'))

    element = testsuite.get_xml_element()
    print(ET.tostring(element))

# Generated at 2022-06-13 15:41:27.529437
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    pass


# Generated at 2022-06-13 15:41:32.091866
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    # Arrange
    expected_xml = """<test></test>"""
    result = TestResult()

    # Act
    actual_xml = ET.tostring(result.get_xml_element(), encoding='unicode')

    # Assert
    assert expected_xml == actual_xml
    

# Generated at 2022-06-13 15:41:42.232872
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name='name',
        id='id',
        package='package',
        hostname='hostname',
        timestamp=datetime.datetime(2020, 1, 1, 0, 0, 0),
        cases=[TestCase(name='test1'), TestCase(name='test2')],
        system_out='system_out',
        system_err='system_err')
    result = suite.get_xml_element()

# Generated at 2022-06-13 15:41:44.092901
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    x = TestFailure(output="output")
    xml_element = x.get_xml_element()
    assert xml_element.tag == "failure"
    assert xml_element.text == "output"


# Generated at 2022-06-13 15:41:46.453130
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    xml_element = TestResult().get_xml_element()
    assert xml_element.tag == 'testresult'
    assert xml_element.attrib == {}


# Generated at 2022-06-13 15:42:00.874983
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(name="Test Suite", hostname="localhost", timestamp=datetime.datetime(2020, 1, 1, 0, 0, 0))
    ts.cases.append(TestCase(name="Test Case 1", classname="TestCase1", time=0.1))
    ts.cases.append(TestCase(name="Test Case 2", classname="TestCase2", time=0.2))
    ts.cases.append(TestCase(name="Test Case 3", classname="TestCase3", time=0.3))
    ts.cases[0].errors.append(TestError(output="Test Case 1 Error"))
    ts.cases[2].failures.append(TestFailure(output="Test Case 3 Failure"))

# Generated at 2022-06-13 15:42:11.262189
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    import datetime

    test_case = TestCase(name = "test_TestCase_get_xml_element")
    result = test_case.get_xml_element()
    assert ET.tostring(result, encoding='unicode') =='<testcase name="test_TestCase_get_xml_element" />'

    test_case = TestCase(name = "test_TestCase_get_xml_element", assertions = 1, classname = "test_class_name", status = "failed", time = 0.033)
    test_case.errors = [TestError(message = "test error message", type = "test_error_type", output = "test_error_output")]

# Generated at 2022-06-13 15:42:22.846177
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # test case 1
    test_case_1 = TestCase(
        name='test',
    )
    exp_str = '''<testcase name="test"></testcase>'''
    xml_ele = test_case_1.get_xml_element()
    act_str = ET.tostring(xml_ele, encoding='unicode')
    assert exp_str == act_str
    # test case 2
    test_case_2 = TestCase(
        name='test',
        classname='class_1',
        time=decimal.Decimal('15.0')
    )
    exp_str = '''<testcase name="test" classname="class_1" time="15.0"></testcase>'''
    xml_ele = test_case_2.get_xml_element()
    act_str

# Generated at 2022-06-13 15:42:30.412048
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    c = """<testcase name="test_async_bilibili" assertions="0" classname="test_async_bilibili" status="run" time="0.164">
    <skipped></skipped>
    <system-out></system-out>
    <system-err></system-err>
    </testcase>"""
    str1 = TestCase(name="test_async_bilibili",status='run',time = '0.164').get_xml_element()
    assert str(str1) == c


# Generated at 2022-06-13 15:42:34.772673
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = create_test_suite()
    element = test_suite.get_xml_element()
    assert any(element.find(key) for key in [test_suite.name, test_suite.hostname, test_suite.id, test_suite.package]) == True,\
    "test suite's name, hostname, id, or package is in the test suite element's child"



# Generated at 2022-06-13 15:42:46.102853
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():

    def pretty_xml(xml_string: str) -> str:
        """Return a pretty formatted XML string."""
        return minidom.parseString(xml_string).toprettyxml()

    test_case = TestCase(
        classname='test.module.foo.Bar',
        name='test_function_name',
        assertions=12,
        status='Test status',
        time=decimal.Decimal('0.000123'),
        errors=[
            TestError('Exception: Error!', 'message'),
        ],
        failures=[
            TestFailure('Assertion error', 'message'),
        ],
        skipped='skipped',
        system_out='system_out',
        system_err='system_err',
    )


# Generated at 2022-06-13 15:42:53.639237
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:42:58.085927
# Unit test for method get_xml_element of class TestSuites
def test_TestSuites_get_xml_element():
    """Unit test for method get_xml_element of class TestSuites"""
    suite_1 = TestSuite('suite_1')
    suite_2 = TestSuite('suite_2')
    suite_1.cases.append(TestCase('case_1'))
    suite_1.cases.append(TestCase('case_2'))
    suite_2.cases.append(TestCase('case_3'))

    suites = TestSuites()
    suites.suites.append(suite_1)
    suites.suites.append(suite_2)

    result = suites.to_pretty_xml()

# Generated at 2022-06-13 15:43:04.672956
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name='My Test Suite')
    test_case_1 = TestCase(
        name = 'My Test Case 1',
        time = decimal.Decimal('1.0'),
    )
    test_case_2 = TestCase(
        name = 'My Test Case 2',
        time = decimal.Decimal('1.5'),
    )
    test_suite.cases.append(test_case_1)
    test_suite.cases.append(test_case_2)

    print(test_suite.get_xml_element())


# Generated at 2022-06-13 15:43:10.405138
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name="testCase_0",
        classname="test_cases.TestCase_0",
        time=0.00800000037997961,
        status="POSITIVE"
    )
    assert test_case.get_xml_element().attrib == {'name': 'testCase_0', 'classname': 'test_cases.TestCase_0', 'time': '0.00800000037997961', 'status': 'POSITIVE'}

# Generated at 2022-06-13 15:43:28.814511
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(
        hostname='localhost',
        id='Framework',
        name='Framework',
        package='framework.tests',
        timestamp=datetime.datetime(
            year=2020,
            month=5,
            day=5,
            hour=8,
            minute=15,
            second=38,
        ),
    )


# Generated at 2022-06-13 15:43:39.831520
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    
    testcases = [
        TestCase(name='name',
            status='status',
            classname='classname',
            assertions=1,
            time=2.3
            ),
        TestCase(name='name2',
            ),
    ]

    result = TestSuite(name='suite_name',
            hostname='hostname',
            id=1,
            package='package',
            time=2.3,
            timestamp=datetime.datetime(2020, 9, 24),
            properties={
                'name': 'value'
            },
            cases=testcases,
            system_out='system_out',
            system_err='system_err',
        )

    result_element = result.get_xml_element()
    assert result_element.tag == 'testsuite'

# Unit test

# Generated at 2022-06-13 15:43:51.950246
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Arrange
    case1 = TestCase(
        name='test_foo1',
        assertions='2',
        classname='tests.foo.FooTests',
        status='passed',
        time=decimal.Decimal('0.123'),
    )
    case2 = TestCase(
        name='test_foo2',
        assertions='2',
        classname='tests.foo.FooTests',
        status='passed',
        time=decimal.Decimal('0.124'),
    )
    case3 = TestCase(
        name='test_bar',
        assertions='2',
        classname='tests.bar.BarTests',
        status='passed',
        time=decimal.Decimal('0.125'),
    )

# Generated at 2022-06-13 15:43:58.692341
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase("First Test", assertions=1, classname="com.nfq.TestFirst",
                  status="FAILED", time=0.1, errors=[], failures=[],
                  skipped="", system_out="", system_err="")

    tc_tree = tc.get_xml_element()

    assert tc_tree.attrib["assertions"] == "1"
    assert tc_tree.attrib["classname"] == "com.nfq.TestFirst"
    assert tc_tree.attrib["name"] == "First Test"
    assert tc_tree.attrib["status"] == "FAILED"
    assert tc_tree.attrib["time"] == "0.1"

    assert tc_tree.find("skipped") is None
    assert len(tc_tree.findall("error")) == 0


# Generated at 2022-06-13 15:44:03.124553
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():

    # Initialize result object
    case = TestCase(name="test_initialize_robot", assertions=1, classname="TestSuite.TestCase", status="RUN", time=1)
    suite = TestSuite(name="suite_name", hostname="host", id="12345", package="package_name", timestamp=datetime.datetime.now())
    suite.cases.append(case)

    # Check for correct XML output
    xml_output = ET.tostring(suite.get_xml_element(), encoding='unicode')
    assert '<testcase assertions="1" classname="TestSuite.TestCase" name="test_initialize_robot" status="RUN" time="1"></testcase>' in xml_output

# Generated at 2022-06-13 15:44:14.008415
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    assert TestCase(name='test').get_xml_element().tag == 'testcase'
    assert TestCase(name='test', classname='testsuite').get_xml_element().find('classname').text == 'testsuite'
    assert TestCase(name='test', classname='testsuite').get_xml_element().attrib['classname'] == 'testsuite'
    assert len(TestCase(name='test', classname='testsuite').get_xml_element().findall('classname')) == 1
    assert TestCase(name='test', classname='testsuite').get_xml_element().findall('classname')[0].attrib['name'] == 'testsuite'

# Generated at 2022-06-13 15:44:23.442429
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # create the test case
    test_case = TestCase(
        name="test_case_1",
        assertions=1,
        classname="class_1",
        status="passed",
        time=.01,
        errors=[TestError(output="err1", message="error message 1", type="error1")],
        failures=[TestFailure(output="fail1", message="failure message 1", type="failure1")],
        skipped="skipped 1",
        system_out="std out",
        system_err="std err",
        is_disabled=True
    )

    # create the expected element

# Generated at 2022-06-13 15:44:32.236604
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Return an XML element representing this instance."""
    test_case = TestCase(name = 'testcase', classname = 'classname', time = 10.0)
    test_suite = TestSuite(name = 'testsuite', timestamp = datetime.datetime.now(), cases = [test_case])
    assert test_suite.get_xml_element() == ET.Element('testsuite', {'name': 'testsuite', 'time': '10.0', 'tests': '1', 'errors': '0', 'disabled': '0', 'failures': '0', 'skipped': '0', 'timestamp': '2020-06-06T21:05:34'})


# Generated at 2022-06-13 15:44:43.465801
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_properties = {'Test1': 'Pass', 'Test2': 'Pass', 'Test3': 'Pass'}
    test_case = TestCase(name='tests.Test1')
    test_suite = TestSuite(name='test_suite', timestamp=datetime.datetime.now(), properties=test_properties, cases=[test_case])
    expected_xml = '<testsuite name="test_suite"><properties><property name="Test1" value="Pass" /><property name="Test2" value="Pass" /><property name="Test3" value="Pass" /></properties><testcase name="tests.Test1" /><system-out /></testsuite>'
    result = _pretty_xml(test_suite.get_xml_element())
    assert result == expected_xml


# Generated at 2022-06-13 15:44:49.722449
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase(name='test_0', assertions=1, disabled=False, classname='my.classname', status='my.status', time=1.0)
    assert(testcase.get_xml_element().attrib == {'assertions': '1', 'classname': 'my.classname', 'name': 'test_0', 'status': 'my.status', 'time': '1.0'})


# Generated at 2022-06-13 15:45:26.698620
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    fail_case = TestCase(name="fail", time=0)
    fail_case.failures.append(TestFailure(message="Missing resource"))
    assert fail_case.get_xml_element().tostring() == b'<testcase name="fail" time="0.0"><failure message="Missing resource"></failure></testcase>'



# Generated at 2022-06-13 15:45:31.377355
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_error = TestError(type='test', output='test output')
    test_failure = TestFailure(type='test', output='test output')
    test_case = TestCase(name='test')
    test_case.errors.append(test_error)
    test_case.failures.append(test_failure)

    tag_name = test_case.get_xml_element().tag
    assert tag_name == 'testcase'

    expected_attributes = {'name': 'test'}
    assert test_case.get_xml_element().attrib == expected_attributes

    assert test_case.get_xml_element()[0].tag == 'failure'
    assert test_case.get_xml_element()[1].tag == 'error'


# Generated at 2022-06-13 15:45:39.129161
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:45:48.965089
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Create a testsuite with one testcase
    ts = TestSuite(name="testsuite_01", hostname='testHost', id='testId', package='testPackage', timestamp=datetime.datetime.now(), properties={'key1':'value1'}, cases=[TestCase(name="testcase_01", status='testStatus', time=123.456, skipped='testSkipped', system_out='testSysOut', system_err='testSysError')], system_out='testSysOut', system_err='testSysError')
    ts_xml_result = ts.get_xml_element()
    # Create a testsuite with one testcase and add it to a testsuites instance

# Generated at 2022-06-13 15:45:57.014488
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase("test_case")
    test_suite = TestSuite(name="test_suite", hostname="1.1.1.1", id="1", package="testing",
                           timestamp=datetime.datetime.now(), cases=[test_case])
    xml_element = test_suite.get_xml_element()
    assert isinstance(xml_element, ET.Element)
    assert xml_element.tag == 'testsuite'
    assert xml_element[0].tag == 'testcase'

# Generated at 2022-06-13 15:46:00.484123
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="test_name")
    element = test_case.get_xml_element()

    assert element.tag == "testcase"
    assert element.attrib["name"] == "test_name"


# Generated at 2022-06-13 15:46:04.481046
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='UnitTest')
    xml = suite.get_xml_element()
    assert(xml.tag == 'testsuite')
    assert(xml.attrib['name'] == 'UnitTest')


# Generated at 2022-06-13 15:46:13.475495
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name='test_case_name',
        assertions=10,
        classname='test_case_classname',
        status='test_case_status',
        time=10.0
    )
    xml_element = test_case.get_xml_element()
    assert xml_element.tag == 'testcase'
    assert xml_element.attrib == {
        'assertions': '10',
        'classname': 'test_case_classname',
        'name': 'test_case_name',
        'status': 'test_case_status',
        'time': '10.0'
    }


# Generated at 2022-06-13 15:46:18.187990
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Create TestSuite object
    suite = TestSuite(name = "suite", timestamp = datetime.datetime.now())
    
    print (suite.get_xml_element())
    
if __name__ == "__main__":
    test_TestSuite_get_xml_element()

# Generated at 2022-06-13 15:46:30.338905
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # TestCase with no attributes
    tc = TestCase(name='test_name')
    el = tc.get_xml_element()
    assert(el.tag == 'testcase')
    assert(el.attrib == {'name': 'test_name'})
    assert(el.text is None)
    assert(el[0].tag == 'skipped')
    assert(el[0].attrib == {})
    assert(el[0].text is None)

    # TestCase with skipped
    tc = TestCase(name='test_name')
    tc.skipped = 'skipped'
    el = tc.get_xml_element()
    assert(el.tag == 'testcase')
    assert(el.attrib == {'name': 'test_name'})
    assert(el.text is None)

# Generated at 2022-06-13 15:46:56.850831
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name='Hello')
    assert(ET.tostring(test_suite.get_xml_element(), encoding='unicode').strip() == '<testsuite name="Hello"/>')



# Generated at 2022-06-13 15:47:01.619528
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase("Test case name", classname="Test class name")
    xml_element = testcase.get_xml_element()
    expected_xml_element = ET.fromstring("""<testcase name="Test case name" classname="Test class name"></testcase>""")
    assert xml_element == expected_xml_element

# Generated at 2022-06-13 15:47:07.830307
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tcase = TestCase(name='test_example', classname='ExampleTests')
    xml = tcase.get_xml_element()

    assert ET.tostring(xml, encoding='unicode') == '<testcase assertions="None" classname="ExampleTests" name="test_example" status="None" time="None" />'

# Generated at 2022-06-13 15:47:10.061478
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="testcase_name")
    
    expected_element = ET.Element('testcase', _attributes(name="testcase_name"))

    assert test_case.get_xml_element() == expected_element


# Generated at 2022-06-13 15:47:16.853178
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:47:26.757920
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('name')
    assert ET.tostring(test_case.get_xml_element(), encoding='unicode') == '<testcase name="name" />'

    test_case = TestCase('name', assertions=5)
    assert ET.tostring(test_case.get_xml_element(), encoding='unicode') == '<testcase assertions="5" name="name" />'


# Generated at 2022-06-13 15:47:28.792692
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='TestCase')
    root_element = test_case.get_xml_element()

    assert root_element.tag == 'testcase'
    assert root_element.attrib == {'name': 'TestCase'}


# Generated at 2022-06-13 15:47:40.749213
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # This test was only used to debug the output of xml.
    # Now just keep it for possible future use.
    test_suite = TestSuite(name='salt-minion',
                           hostname='salt-minion',
                           id='salt-minion',
                           package='salt.wheel',
                           timestamp=datetime.datetime.fromtimestamp(1594376827.0),
                           )
    test_case = TestCase(name='test_call',
                         assertions=None,
                         classname='Tests.salt.wheel.wheel_call_TestCase',
                         status='run',
                         time=decimal.Decimal('0.00'),
                         )

# Generated at 2022-06-13 15:47:51.557223
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(
        name='testsuite01',
        hostname='test_hostname',
        id='test_id',
        package='test_package',
        timestamp=datetime.datetime.min,
        properties = {'prop_key' : 'prop_value'},
        system_out = 'test_system_out',
    )

# Generated at 2022-06-13 15:47:56.112086
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suites = TestSuites(name = 'Test-Suite',
                         suites = [TestSuite(name = 'Test-Suite', id = 'Test-Suite1',
                             hostname = 'Test-Suite2',
                             timestamp = datetime.datetime.now(),
                             system_out = 'TestSuite1',
                             system_err = 'TestSuite2',
                             cases = [TestCase(name = 'Test', assertions = 3, classname = 'test1',
                                               status = 'test2',
                                               time = 3.12,
                                               )])])

# Generated at 2022-06-13 15:48:18.037889
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name='project')
    testsuite.cases.append(TestCase(name="test1", assertions=1, classname="test.project.test1", status="PASSED", time=decimal.Decimal("2.30")))
    testsuite.cases.append(TestCase(name="test2", assertions=1, classname="test.project.test2", status="PASSED", time=decimal.Decimal("1.50")))
    testsuite.cases.append(TestCase(name="test3", classname="test.project.test3", status="PASSED", time=None))
    testsuite.cases.append(TestCase(name="test4", classname="test.project.test4", status="PASSED"))

# Generated at 2022-06-13 15:48:27.183936
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testsuite = TestSuite(name='test', timestamp=None)
    testcase = TestCase(name='test', time=None, classname=None)
    testcase.errors.append(TestError())
    testcase.failures.append(TestFailure())
    testsuite.cases.append(testcase)

    xml_element = testsuite.get_xml_element()
    expected = '''<testsuite tests="1" errors="1" failures="1" name="test">
    <testcase name="test" assertions="None" classname="None" status="None" time="None">
        <error></error>
        <failure></failure>
    </testcase>
</testsuite>'''
    assert str(xml_element) == expected


# Generated at 2022-06-13 15:48:28.996931
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # ToomkyGames test data
    t.NoReturn



# Generated at 2022-06-13 15:48:38.977679
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    import datetime

    name = "my_suite"
    hostname = "localhost"
    id = "id"
    package = "package"
    timestamp = datetime.datetime.now()
    properties = {
        "property1": "value1",
        "property2": "value2"
    }
    cases = [
        TestCase(name="a_test", time=2),
        TestCase(name="b_test", time=5)
    ]
    system_out = "some stdout"
    system_err = "some stderr"