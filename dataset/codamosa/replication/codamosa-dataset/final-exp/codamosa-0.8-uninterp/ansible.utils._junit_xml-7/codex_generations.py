

# Generated at 2022-06-13 15:38:42.146056
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    output = 'Something went wrong'
    message = 'Something went wrong'
    type = 'TestResult'
    tr = TestResult(output=output, message=message, type=type)

    assert len(tr.get_attributes()) == 3
    assert tr.get_attributes()['output'] == output
    assert tr.get_attributes()['message'] == message
    assert tr.get_attributes()['type'] == type


# Generated at 2022-06-13 15:38:51.706519
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    # Input:
    # - TestResult object
    # - TestResult object with output, message, and type attributes
    test_result = TestResult()
    test_result_with_attributes = TestResult(output="test output", message="test message", type="test type")
    # Expected output:
    # - XML element with tag "skipped" without any attribute
    # - XML element with tag "skipped" with attributes output, message, and type with corresponding values
    expected_output = ET.Element("skipped")
    expected_output_with_attributes = ET.Element("skipped", {"output": "test output", "message": "test message", "type": "test type"})
    # For test_result
    assert test_result.get_attributes() == {}
    assert test_result.get_xml_element().tag == expected

# Generated at 2022-06-13 15:38:56.385373
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestResult(message='test message')
    xml_element = test_result.get_xml_element()

    assert sorted(test_result.get_attributes().items()) == sorted(xml_element.attrib.items())


# Unit tests for method get_xml_element of class TestError

# Generated at 2022-06-13 15:39:04.050658
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    case = TestCase("suite_1",10,"System.out", "passed", 0.23)
    case2 = TestCase("suite_2",12,"System.out", "passed", 0.24)
    case.failures.append(TestFailure("output1", "message1"))
    case.failures.append(TestFailure("output2", "message2"))
    case.errors.append(TestError("output3", "message3"))
    case.errors.append(TestError("output4", "message4"))
    case.system_out = "output"
    case.system_err = "error"
    testSuit = TestSuite("suite", "hostname", "id", "package", datetime.datetime.now())
    testSuit.system_out = "output"
    testSuit.system

# Generated at 2022-06-13 15:39:06.500539
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    tr = TestResult('OUTPUT', 'MESSAGE', 'TYPE')
    tr.get_xml_element()
    assert True


# Generated at 2022-06-13 15:39:13.117458
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestResult(type="test",message="test message",output="test output")
    assert test_result.get_xml_element().get("type") == "test"
    assert test_result.get_xml_element().get("message") == "test message"
    assert test_result.get_xml_element().text == "test output"


# Generated at 2022-06-13 15:39:17.006687
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_output = "Output"
    test_message = "Message"
    test_type = "Type"

    expected_tag = "failure"
    expected_attributes = {"message": test_message, "type": test_type}
    expected_text = test_output

    result = TestFailure(test_output, test_message, test_type)
    actual_element = result.get_xml_element()

    assert actual_element.tag == expected_tag
    assert actual_element.get("message") == expected_attributes["message"]
    assert actual_element.get("type") == expected_attributes["type"]
    assert actual_element.text == expected_text


# Generated at 2022-06-13 15:39:24.791775
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    # Test for method get_xml_element of class TestResult
    # Tests empty output string
    def test_get_xml_element(result, tag, output = None):
        result.output = output
        assert result.get_xml_element().tag == tag
        assert result.get_xml_element().text == output

    test_get_xml_element(TestFailure(), 'failure')
    test_get_xml_element(TestError(), 'error')


if __name__ == '__main__':
    test_TestResult_get_xml_element()

# Generated at 2022-06-13 15:39:31.068269
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    """
    Verifications for method get_xml_element of class TestResult

    """

    test_case = TestResult(output='output', message='message', type='type')
    assert (
        test_case.get_xml_element().toxml() ==
        '<testresult type="type" message="message">output</testresult>'
    )
    del test_case.message
    assert (
        test_case.get_xml_element().toxml() ==
        '<testresult type="type">output</testresult>'
    )
    del test_case.type
    assert (
        test_case.get_xml_element().toxml() ==
        '<testresult>output</testresult>'
    )



# Generated at 2022-06-13 15:39:41.866789
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('My test case',
                         'my.class.name',
                         dataclasses.field(default_factory=list)
                         )
    target_element = ET.Element(test_case.name, test_case.get_attributes())

    # Test result elements
    target_element.extend([error.get_xml_element() for error in test_case.errors])
    target_element.extend([failure.get_xml_element() for failure in test_case.failures])
    target_element.extend([test_case.get_xml_element() for test_case in test_case.cases])

    # Test result data
    if test_case.skipped:
        ET.SubElement(target_element, 'skipped').text = test_case.skipped

# Generated at 2022-06-13 15:39:57.181569
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(
        name = 'TEST_SUITE_NAME',
        hostname = 'TEST_HOSTNAME',
        id = 'TEST_ID',
        package = 'TEST_PACKAGE',
        timestamp = 'TEST_TIMESTAMP',
        tests = 1,
        time = 1.0,
        errors = 0,
        failures = 0,
        disabled = 0,
        skipped = 0,
    )
    tests = [
        TestCase(
            name = 'TEST_CASE_NAME',
            assertions = 1,
            classname = 'TEST_CLASSNAME',
            status = 'SKIPPED',
            time = 2.0,
    )]
    testsuite.cases.extend(tests)

# Generated at 2022-06-13 15:39:57.728799
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    pass

# Generated at 2022-06-13 15:40:03.112983
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test = TestCase(name="first test", time=0.123456)
    root = test.get_xml_element()
    assert root.tag == 'testcase'
    assert root.attrib['name'] == 'first test'
    assert root.attrib['time'] == '0.123456'
    assert root.attrib['status'] == 'null'
    assert not root.text


# Generated at 2022-06-13 15:40:11.204409
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testcase = TestCase(
        name='test_TestSuite_get_xml_element',
        classname='test_junit_xml.TestSuite',
        assertions=1)

    testsuite = TestSuite(
        name='junit_xml',
        hostname='localhost',
        id='1',
        package='junit_xml',
        timestamp=datetime.datetime.now(),
        properties={'key': 'value'},
        cases=[testcase],
        system_out='success',
        system_err='error')

    # comparision between assert for get_xml_element and schema validation

# Generated at 2022-06-13 15:40:23.320248
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():

    
    test_case1 = TestCase('name1', 1212)
    test_case2 = TestCase('name2', 1212)

    test_suite1 = TestSuite('Test_Suite_1')
    test_suite2 = TestSuite('Test_Suite_2')

    test_suites = TestSuites()

    test_suite1.cases.append(test_case1)
    test_suite2.cases.append(test_case2)

    test_suites.suites.append(test_suite1)
    test_suites.suites.append(test_suite2)


# Generated at 2022-06-13 15:40:27.594228
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('name', time=10)
    assert ET.tostring(test_case.get_xml_element()) == (
        b'<testcase assertions="0" classname="None" name="name" status="None" time="10" />'
    )


# Generated at 2022-06-13 15:40:37.871504
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:40:47.724963
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_my_simple_test')
    assert _pretty_xml(test_case.get_xml_element()) == '''\
<?xml version="1.0" ?>
<testcase name="test_my_simple_test"/>
'''
    test_case = TestCase('test_my_simple_test', classname='testmodule.Tests', time=1.0)
    assert _pretty_xml(test_case.get_xml_element()) == '''\
<?xml version="1.0" ?>
<testcase classname="testmodule.Tests" name="test_my_simple_test" time="1.0"/>
'''

# Generated at 2022-06-13 15:40:50.372994
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase(name='Test', classname='Test')
    expected_element = ET.fromstring("""<testcase classname="Test" name="Test"></testcase>""")
    assert ET.tostring(tc.get_xml_element()) == ET.tostring(expected_element)


# Generated at 2022-06-13 15:40:59.045526
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:41:06.852024
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='name')
    element = test_case.get_xml_element()
    assert(element.tag == 'testcase')
    assert(element.attrib['name'] == 'name')



# Generated at 2022-06-13 15:41:14.333582
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='JUnitTestSuite')
    result = suite.get_xml_element()
    assert(result.attrib['tests'] == '0')
    assert(result.attrib['failures'] == '0')
    assert(result.attrib['disabled'] == '0')
    assert(result.attrib['errors'] == '0')
    assert(result.attrib['time'] == '0.0')
    assert(result.attrib['name'] == 'JUnitTestSuite')


# Generated at 2022-06-13 15:41:22.782954
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    a = TestCase(name='TestCase_a')
    assert a.is_failure == False
    assert a.is_error == False
    assert a.is_skipped == False
    assert len(a.get_xml_element()) == 2
    assert a.get_xml_element().attrib['name'] == 'TestCase_a'

    b = TestCase(name = 'TestCase_b', classname = 'TestCase_b', status = 'TestCase_b', time = 1)
    assert b.get_xml_element().attrib['name'] == 'TestCase_b'
    assert b.get_xml_element().attrib['classname'] == 'TestCase_b'
    assert b.get_xml_element().attrib['status'] == 'TestCase_b'
    assert b.get_xml_element

# Generated at 2022-06-13 15:41:28.587905
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="Test Case Name")
    
    expected_result = ET.Element('xml')
    expected_result.append(ET.Element('testcase', {'name': 'Test Case Name'}))

    assert ET.tostring(test_case.get_xml_element()) == ET.tostring(expected_result)



# Generated at 2022-06-13 15:41:39.110011
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc_assertions = 2
    tc_classname = "MyTestClass"
    tc_name = "MyTestCase"
    tc_status = "run"
    tc_time = 33.4

    tc_message = "Something is wrong!"
    tc_output = "Here is the output!"
    tc_type = "MyTestType"
    tc_skipped = "I don't wanna test this!"
    tc_system_out = "Here is the system output!"
    tc_system_err = "Here is the system error!"

    test_case = TestCase(name=tc_name, assertions=tc_assertions, classname=tc_classname, status=tc_status, time=tc_time)

# Generated at 2022-06-13 15:41:46.757440
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:41:59.201411
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(
        name = 'Visitor',
        hostname = 'localhost',
        id = 'Visitor',
        package = 'Tester',
        timestamp = datetime.datetime(year=2020, month=8, day=9, hour=0, minute=0, second=0),

        properties = {'key': 'value'},
        cases = [TestCase(name='test_get_type')],
        system_out = '',
        system_err = '',
    )


# Generated at 2022-06-13 15:42:09.248013
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite('name',hostname='hostname',id = 'id',package='package',timestamp='timestamp')
    properties = {'prop1': 'value1', 'prop2': 'value2'}
    suite.properties = properties
    suite.system_out = 'system-output'
    suite.system_err = 'system-error'
    case = TestCase('name',assertions=1,classname='classname',status='status',time=1.0)
    case.errors = [
        TestError(output='output1',message='message1',type='type1'),
        TestError(output='output2',message='message2',type='type2')
    ]

# Generated at 2022-06-13 15:42:14.948449
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    dummy_test_case1 = TestCase(name='TestCase1', classname='test_case1', status='passed', time=2.2)
    dummy_test_case2 = TestCase(name='TestCase2', classname='test_case2', status='failed', time=3.3, errors=[TestError(message='This is a runtime error. ')], failures=[TestFailure(message='This is an assertion error.')])
    ts = TestSuite(name='TestSuite1', hostname='hostname1', id='id1', package='package1', timestamp=datetime.datetime(2020, 3, 3, 3, 3, 3), cases=[dummy_test_case1, dummy_test_case2])
    root = ts.get_xml_element()

    assert root.tag == 'testsuite'

# Generated at 2022-06-13 15:42:25.430088
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase(name='test_method_name', classname='TestClassName')
    tc.errors.append(TestError(output='Error message'))
    tc.failures.append(TestFailure(output='Failure message', message='Failure detail message'))
    tc.skipped = 'Skipped reason'
    tc.system_out = 'System out message'
    tc.system_err = 'System err message'

    xml = _pretty_xml(tc.get_xml_element())

# Generated at 2022-06-13 15:42:44.677050
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Given
    test_case_a = TestCase(
            name='foo',
            assertions=1,
            classname='fooClass',
            status='pass',
            time=decimal.Decimal('0.1'),
            errors=[
                TestError(
                    output='error',
                    message='message',
                    type='type'
                )
            ],
            failures=[
                TestFailure(
                    output='failure',
                    message='message',
                    type='type'
                )
            ],
            skipped='skipped',
            system_out='system-out',
            system_err='system-err'
        )


# Generated at 2022-06-13 15:42:48.543981
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_one', time='0.1')
    node = test_case.get_xml_element()
    assert node.tag == 'testcase'
    assert node.attrib == {'name': 'test_one', 'time': '0.1'}


# Generated at 2022-06-13 15:42:58.607871
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:07.534165
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:15.087967
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name="test_case_name",
        assertions=10,
        classname="classname",
        status="status",
        time="10.1",
        errors=[
            TestError(
                output="output_error",
                message="error_message"
            )
        ],
        failures=[
            TestFailure(
                output="output_failure",
                message="failure_message"
            )
        ],
        skipped="skipped_reason",
        system_out="system_out_content",
        system_err="system_err_content"
    )

# Generated at 2022-06-13 15:43:27.033146
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:38.334421
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    t_case1 = TestCase('test_case_name', classname='test_case_name_test', time=1.3)
    t_case1.errors.append(TestError(output='test_error_output1'))
    t_case1.errors.append(TestError(output='test_error_output2'))
    t_case1.failures.append(TestFailure(output='test_failure_output1'))
    t_case1.failures.append(TestFailure(output='test_failure_output2'))

# Generated at 2022-06-13 15:43:50.408401
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:57.796210
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    user_errors = ["Error"]
    user_failures = ["Failure"]
    user_skipped = "Skipped"
    user_systemout = "SystemOut"
    user_systemerr = "SystemErr"
    user_testcase_name = "test_TestCase_get_xml_element"

# Generated at 2022-06-13 15:44:03.493884
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase("test case 1")
    xml = test_case.get_xml_element()
    assert xml.tag == "testcase"
    assert xml.attrib == {'name': 'test case 1'}
    assert xml.text == None
    assert len(xml) == 0
    assert xml[:] == []



# Generated at 2022-06-13 15:44:21.574360
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name='TestSuite',
        hostname='HostName',
        id='ID',
        package='Package',
        properties={'key': 'value'},
        timestamp=datetime.datetime.utcnow(),
        cases=[
            TestCase(
                name='TestCase',
                assertions=1,
                classname='ClassName',
                status='Status',
                time=10.01,
                errors=[TestError(output='Output', message='Message', type='Type')],
                failures=[TestFailure(output='Output', message='Message', type='Type')],
                skipped='Skipped',
                system_out='SystemOut',
                system_err='SystemErr',
            )
        ],
        system_out='SystemOut',
        system_err='SystemErr',
    )



# Generated at 2022-06-13 15:44:25.281956
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name="foo", timestamp=datetime.datetime.strptime("2020-04-23T12:41:40", "%Y-%m-%dT%H:%M:%S"))
    res = testsuite.get_xml_element()
    value = res.attrib['timestamp']
    expected = '2020-04-23T12:41:40'
    assert(value == expected)

# Generated at 2022-06-13 15:44:37.363960
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name='SomeTestSuite',
        errors=3,
        hostname='localhost',
        id=str(id(suite)),
        package='some.package',
        timestamp=datetime.datetime.now(),
        cases=[TestCase(
            name='SomeTestCase',
            assertions=1,
            classname='SomeClass',
            status='OK',
            time=1.23,
            errors=[TestError(
                output='error-output',
                message='error-message',
                type='error-type',
            )],
            failures=[TestFailure(
                output='failure-output',
                message='failure-message',
                type='failure-type',
            )],
        )]
    )

    element = suite.get_xml_element()


# Generated at 2022-06-13 15:44:47.215329
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase(
        name='testDemo',
        assertions=None,
        classname='com.tencent.xkx',
        status=None,
        time=None
    )
    test_case_xml = testcase.get_xml_element()
    assert test_case_xml.attrib['name'] == 'testDemo', 'TestCase name not right!'
    assert test_case_xml.attrib['classname'] == 'com.tencent.xkx', 'TestCase classname not right!'
    assert 'time' not in test_case_xml.attrib, 'TestCase time not right!'
    assert 'assertions' not in test_case_xml.attrib, 'TestCase assertions not right!'

# Generated at 2022-06-13 15:44:50.857144
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    TestSuite(
        name='test',
        testcases=[
            TestCase(
                name='test',
                assertion=1,
                classname='classname',
                status='status',
                time=123
            )
        ]
    )

# Generated at 2022-06-13 15:44:55.498524
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name="Test Suite")
    test_suite.cases.append(TestCase(name="Test Case"))
    expected_response = '<?xml version="1.0" ?><testsuite failures="0" name="Test Suite" tests="1"><testcase assertions="" classname="" name="Test Case" status="" time=""/></testsuite>'
    assert test_suite.get_xml_element() == expected_response


# Generated at 2022-06-13 15:45:06.831458
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_case_name')
    ET.tostring(test_case.get_xml_element())

    test_case = TestCase('test_case_name', time=0.1)
    ET.tostring(test_case.get_xml_element())

    test_case = TestCase('test_case_name', classname='TestCase')
    ET.tostring(test_case.get_xml_element())

    test_case = TestCase('test_case_name', assertions=1)
    ET.tostring(test_case.get_xml_element())

    test_case = TestCase('test_case_name', status='none')
    ET.tostring(test_case.get_xml_element())


# Generated at 2022-06-13 15:45:11.509486
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    assert TestCase(
        name='test1',
        classname='test.Class',
        status='run',
        time=decimal.Decimal('0.000001'),
    ).get_xml_element().tag == 'testcase'


# Generated at 2022-06-13 15:45:19.885365
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="TestCase name")
    test_case.classname = 'TestCase classname'
    test_case.status = 'TestCase status'
    test_case.time = 2.0
    test_case.output = "TestCase output"

    root = test_case.get_xml_element()
    xml_string = ET.tostring(root, encoding='unicode')

    reference_string = """
    <testcase assertions="None" classname="TestCase classname" name="TestCase name" status="TestCase status" time="2.0">
      <system-out>TestCase output</system-out>
    </testcase>
    """

    assert xml_string == reference_string



# Generated at 2022-06-13 15:45:25.824338
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name="TestSuite", hostname="localhost", id="123", package="package name")
    test_case = TestCase(name="TestCase", assertions="2", classname="Class name", status="status", time=1.0)
    test_case.errors.append(TestError(output="abc", message="abc message"))
    test_case.failures.append(TestFailure(output="def", message="def message"))
    test_case.skipped = "skipped"
    test_case.system_out = "sysout"
    test_case.system_err = "syserr"
    test_suite.cases.append(test_case)
    test_suite.system_out = "sysout"
    test_suite.system_err = "syserr"
    
   

# Generated at 2022-06-13 15:45:36.621509
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite('Test_Suite')
    # test_suite.cases = [TestCase('Test_Case')]
    xml_tree = test_suite.get_xml_element()
    print(xml_tree)
    assert 'test-suite' == xml_tree.tag



# Generated at 2022-06-13 15:45:40.591802
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('Test')
    result = test_case.get_xml_element()
    expected = ET.fromstring('<testcase assertions="None" classname="None" name="Test" status="None" time="None"/>')
    assert result == expected

# Generated at 2022-06-13 15:45:50.290291
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(classname='foo.bar.TestClass', name='test_method', assertions='0', status='passed', time='0.0042')
    test_case.failures = [TestFailure(type='assertion', message='AssertionError', output='self.assertTrue(False)')]
    test_case.errors = [TestError(type='exception', message='ZeroDivisionError', output='1/0')]

    test_suite = TestSuite(name='foo.bar.TestClass', hostname='foobar.local', id='0', package='foo.bar',
                           timestamp=datetime.datetime(2020, 1, 1, 0, 0, 0))
    test_suite.properties = {'key': 'value'}

# Generated at 2022-06-13 15:45:54.382023
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    try:
        suite = TestSuite(name='test', hostname='host', package='package')
        suite.get_xml_element()
    except:
        pass


# Generated at 2022-06-13 15:45:59.194297
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name='test_case')
    test_suite = TestSuite(name='test_suite', cases=[test_case])

    assert 'testsuite' == test_suite.get_xml_element().tag
    assert ['testcase'] == [element.tag for element in test_suite.get_xml_element()]

# Generated at 2022-06-13 15:46:02.421307
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase("name")
    xml = tc.get_xml_element()
    assert(xml.tag == "testcase")
    assert(xml.attrib.get("name") == "name")
    assert(len(xml) == 0)


# Generated at 2022-06-13 15:46:05.185237
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='titanic')
    actual = test_case.get_xml_element()
    expected = ET.fromstring("""\
<testcase name="titanic"></testcase>""")
    assert actual == expected


# Generated at 2022-06-13 15:46:10.695003
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    """Unit test for method get_xml_element of class TestCase"""
    test_case = TestCase(name="Fail test", classname="TestCase", status="1")
    test_case.failures.append(TestFailure())
    xml_element = test_case.get_xml_element()
    try:
        xml_element.findall("./failure")
    except:
        assert False


# Generated at 2022-06-13 15:46:21.294149
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_cases = [
        TestCase('Test', time=1.1),
        TestCase('Test1', time=1.11, status='skipped'),
        TestCase('Test2', time=1.12),
    ]
    test_suite = TestSuite('Suite', cases=test_cases, timestamp=datetime.datetime.fromtimestamp(0))

    actual = test_suite.get_xml_element()
    assert actual.tag == 'testsuite'
    assert actual.attrib == {'tests': '3', 'disabled': '0', 'errors': '0', 'time': '2.33', 'timestamp': '1970-01-01T00:00:00', 'failures': '0', 'name': 'Suite'}

    assert actual[0].tag == 'testcase'

# Generated at 2022-06-13 15:46:32.901430
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    error_text = 'error text'
    failure_text = 'failure text'
    output = 'output'
    testname = 'testname'

    tc = TestCase(name=testname)
    tc.errors.append(TestError(output=error_text))
    tc.failures.append(TestFailure(output=failure_text))
    tc.system_out = output

    test_result = tc.get_xml_element()

    assert test_result.tag == 'testcase'
    assert test_result.attrib['name'] == testname

    assert len(test_result) == 3
    assert test_result[0].tag == 'error'
    assert test_result[0].text == error_text
    assert test_result[1].tag == 'failure'
    assert test_result[1].text

# Generated at 2022-06-13 15:46:52.772452
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(
        classname='com.example.FooTest',
        name='testSomething',
        time=1.234,
        output='test output',
        errors=[TestError(message='test error message')],
    )

    test_suite = TestSuite(
        name='com.example.FooTest',
        timestamp=datetime.datetime(2015, 3, 2, 20, 59, 53),
        cases=[test_case],
    )
    element = test_suite.get_xml_element()
    assert element.attrib.get('tests') == '1'
    assert element.attrib.get('disabled') == '0'
    assert element.attrib.get('errors') == '1'
    assert element.attrib.get('failures') == '0'

# Generated at 2022-06-13 15:47:03.773654
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # TestCase with errors
    tc = TestCase(name='test-name', assertions='11', classname='test-class', status='PASS', time='1.1')
    tc.errors.append(TestError('error-message-1', 'error-output-1', 'error-type-1'))
    tc.errors.append(TestError('error-message-2', 'error-output-2'))
    tc.errors.append(TestError('error-message-3'))
    tc.failures.append(TestFailure('failure-message-1', 'failure-output-1', 'failure-type-1'))
    tc.failures.append(TestFailure('failure-message-2', 'failure-output-2'))
    tc.failures.append(TestFailure('failure-message-3'))

# Generated at 2022-06-13 15:47:13.198590
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    time = decimal.Decimal(0.001)
    timestamp = datetime.datetime(2020, 1, 18)
    test_case = TestCase(
        name='test_name',
        assertions=1,
        classname='test_classname',
        status='test_status',
        time=time,
        errors=[TestError()],
        failures=[TestFailure()],
        skipped='test_skipped',
        system_out='test_system_out',
        system_err='test_system_err',
    )

# Generated at 2022-06-13 15:47:20.966900
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:47:29.170145
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():

    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
    doctest.testmod(optionflags=doctest.ELLIPSIS)

    my_test_suite = TestSuite(name="Unittesting suite", hostname="localhost", id=1, package="QA",
                              timestamp = datetime.datetime(2019,11,23,19,30,0))
    attr = my_test_suite.get_attributes()
    element = my_test_suite.get_xml_element()
    print(my_test_suite.get_xml_element())
    print(ET.tostring(element, encoding='unicode'))

# Generated at 2022-06-13 15:47:40.790991
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    TestSuite
    TestCase
    TestError
    TestFailure
    

# Generated at 2022-06-13 15:47:51.605050
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    tsuite = TestSuite(name='Maths')
    tcase1 = TestCase('1+1=2')
    tcase2 = TestCase('2+2=4')
    tcase3 = TestCase('3+3=6')
    tsuite.cases.append(tcase1)
    tsuite.cases.append(tcase2)
    tsuite.cases.append(tcase3)

    assert tsuite.get_xml_element().makeelement('testcase', {'name': '1+1=2'}) == tsuite.cases[0].get_xml_element()
    assert tsuite.get_xml_element().makeelement('testcase', {'name': '2+2=4'}) == tsuite.cases[1].get_xml_element()
    assert tsuite

# Generated at 2022-06-13 15:48:03.208277
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    from dataclasses import dataclass, field
    import decimal

    @dataclass
    class TestResult(metaclass=abc.ABCMeta):
        """Base class for the result of a test case."""
        output: t.Optional[str] = None
        message: t.Optional[str] = None
        type: t.Optional[str] = None

        def __post_init__(self):
            if self.type is None:
                self.type = self.tag

        @property
        @abc.abstractmethod
        def tag(self) -> str:
            """Tag name for the XML element created by this result type."""

        def get_attributes(self) -> t.Dict[str, str]:
            """Return a dictionary of attributes for this instance."""

# Generated at 2022-06-13 15:48:09.258557
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase(name='junit.TestCase', assertions=1)
    el = tc.get_xml_element()

    assert el.tag == 'testcase'
    assert el.attrib == {'name': 'junit.TestCase', 'assertions': '1'}



# Generated at 2022-06-13 15:48:18.524188
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='my name', hostname='my hostname', id='my id', package='my package', timestamp=datetime.datetime.now())
    suite.properties['property 1'] = 'value 1'
    suite.properties['property 2'] = 'value 2'
    suite.cases.append(TestCase(name='first name', assertions=1, classname='first classname', status='PASS', time=decimal.Decimal('1.1'), errors=[TestError(output='output 1', message='message 1', type='first type')], failures=[TestFailure(output='output 2', message='message 2', type='second type')], skipped='skipped', system_out='system_out', system_err='system_err', is_disabled=True))