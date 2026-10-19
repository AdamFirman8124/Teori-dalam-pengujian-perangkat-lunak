

# Generated at 2022-06-13 15:38:36.526940
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    r = TestResult(output='test output')
    r.get_attributes()


# Generated at 2022-06-13 15:38:45.478143
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    tr = TestResult(output = "This is an output with no tag", message = "This is an error message", type = "Error")
    element = ET.Element('testresult')
    element.text = 'This is an output with no tag'
    assert tr.get_xml_element().__eq__(element)
    element = ET.Element('testresult', {'message': "This is an error message", 'type': "Error"})
    element.text = 'This is an output with no tag'
    assert tr.get_xml_element().__eq__(element)


# Generated at 2022-06-13 15:38:50.051379
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    ts1 = TestCase('foo')
    ts1.name = 'foo'
    ts1.assertions = None
    ts1.classname = 'bar'
    ts1.status = None
    ts1.time = None
    ts1.errors = []
    ts1.failures = []
    ts1.skipped = None
    ts1.system_out = None
    ts1.system_err = None
    ts1.is_disabled = False
    ts1_xml = ts1.get_xml_element()
    assert ts1_xml.get('name') == 'foo'
    assert ts1_xml.get('classname') == 'bar'
    assert ts1_xml.get('time') == None
    assert ts1_xml.get('disabled') == None

# Generated at 2022-06-13 15:38:51.305067
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    pass


# Generated at 2022-06-13 15:38:58.333931
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    """Test the get_attributes method of the TestResult class."""
    assert TestResult(output="test_output", message="test_message", type="test_type").get_attributes() == {"message": "test_message", "type": "test_type"}

    assert TestResult(output="test_output", message="test_message", type="test_type").get_xml_element() == ET.Element('result', {"message": "test_message", "type": "test_type"})




# Generated at 2022-06-13 15:39:01.573493
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name='test_case_name'
    )
    expected_element = ET.Element(
        'testcase', {
            'name': 'test_case_name'
        }
    )
    assert test_case.get_xml_element() == expected_element



# Generated at 2022-06-13 15:39:10.482109
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_output = 'errors message'
    test_message = 'failure message'
    test_type = 'failure'
    test_tag = 'failure'
    result = TestFailure('output')
    result.output = test_output
    result.message = test_message
    result.type = test_type
    attr = result.get_attributes()
    assert attr == {'message': 'failure message', 'type': 'failure'}
    result.get_xml_element()
    assert result.tag == test_tag



# Generated at 2022-06-13 15:39:20.363798
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    output1 = 'The captured output of test 1'
    message1 = 'Some message for test 1'
    type1 = 'some type for test 1'

    test_result1 = TestResult(output=output1, message=message1, type=type1)
    xml_element1  = test_result1.get_xml_element()

    assert(xml_element1.tag == 'result')
    assert(xml_element1.text == output1)
    assert(xml_element1.get('message') == message1)
    assert(xml_element1.get('type') == type1)

    output2 = 'The captured output of test 2'
    message2 = 'Some message for test 2'
    type2 = 'some type for test 2'


# Generated at 2022-06-13 15:39:28.819531
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    timestamp = datetime.datetime.now()

# Generated at 2022-06-13 15:39:40.432188
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    
    test_case= TestCase(name="myTestCase", time=2)
    
    # Test that the method returns a XML-Element
    assert isinstance(test_case.get_xml_element(), ET.Element)
    
    # Test that the element name is "testcase"
    assert test_case.get_xml_element().tag == "testcase"
    
    # Test that the attribute "time" of the element is "2"
    assert test_case.get_xml_element().attrib == {'time': '2', 'name': 'myTestCase'}
    
    # Test that there are no subelements
    assert test_case.get_xml_element().__len__() == 0
    
    # Test that the element does not have any text
    assert test_case.get_xml_element().text

# Generated at 2022-06-13 15:39:53.368180
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    #create a new test suite
    test_suite = TestSuite(name = "Test Suite Name")
    #create two new test cases
    test_case1 = TestCase(name = "Test Case Name 1")
    test_case2 = TestCase(name = "Test Case Name 2")
    #append test cases to test suite
    test_suite.cases.append(test_case1)
    test_suite.cases.append(test_case2)
    #get the xml element of the test suite
    xml_element = test_suite.get_xml_element()
    #print the xml element
    print(_pretty_xml(xml_element))

# Generated at 2022-06-13 15:39:56.529483
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="aTestCase")

    result = test_case.get_xml_element()

    assert result.tag == 'testcase'
    assert result.attrib == {'name': 'aTestCase'}

# Generated at 2022-06-13 15:40:02.883497
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name="test_case")
    test_case2 = TestCase(name="test_case2")
    test_suite = TestSuite(name="test_suite")
    test_suite.cases.append(test_case)
    test_suite.cases.append(test_case2)

    assert test_suite.get_xml_element().get('tests') == 2
    assert len(test_suite.get_xml_element().findall('testcase')) == 2

# Generated at 2022-06-13 15:40:08.011903
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test1 = TestCase('test_case_1', assertions=2, classname='Tests1', status='passed', time=decimal.Decimal(1.2))
    result1 = test1.get_xml_element()
    assert result1.get('name') == 'test_case_1'
    assert result1.get('assertions') == '2'
    assert result1.get('classname') == 'Tests1'
    assert result1.get('status') == 'passed'
    assert result1.get('time') == '1.2'
    assert result1.text == ''
    assert result1.find('skipped') == None

    test1.errors.append(TestError('out', 'message', 'type'))
    result1 = test1.get_xml_element()

# Generated at 2022-06-13 15:40:20.185864
# Unit test for method get_xml_element of class TestSuites

# Generated at 2022-06-13 15:40:31.123873
# Unit test for method get_xml_element of class TestSuites

# Generated at 2022-06-13 15:40:32.225796
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    assert True


# Generated at 2022-06-13 15:40:41.213256
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase('name', time=2)
    assert(ET.tostring(tc.get_xml_element(), encoding='unicode') == "<testcase time=\"2\" name=\"name\" />\n")

    tc = TestCase('name', time=2, errors=[TestError()])
    assert(ET.tostring(tc.get_xml_element(), encoding='unicode') == "<testcase time=\"2\" name=\"name\">\n<error />\n</testcase>\n")

    tc = TestCase('name', time=2, failures=[TestFailure()])
    assert(ET.tostring(tc.get_xml_element(), encoding='unicode') == "<testcase time=\"2\" name=\"name\">\n<failure />\n</testcase>\n")


# Generated at 2022-06-13 15:40:49.870332
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name='TestSuiteName',tests=1, errors=0, failures=1, hostname='HostName', id='Id', package='Package', timestamp=datetime.datetime(2020, 1, 5, 23, 1, 4), time=decimal.Decimal("0.05"))
    assert testsuite.get_xml_element().tag == 'testsuite'
    assert testsuite.get_xml_element().attrib['name'] == 'TestSuiteName'
    assert testsuite.get_xml_element().attrib['tests'] == '1'
    assert testsuite.get_xml_element().attrib['errors'] == '0'
    assert testsuite.get_xml_element().attrib['failures'] == '1'

# Generated at 2022-06-13 15:40:56.757122
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Setup
    ts = TestSuite(
        name='Hello',
        timestamp=datetime.datetime.now(),
        hostname='',
        id='',
        package='1.0.0',
        properties={},
        cases=[],
        system_out='',
        system_err='',
    )
    # Execute
    xml = ts.get_xml_element()
    # Assert
    assert len(xml.attrib.keys()) == 11
    assert xml.attrib['name'] == 'Hello'
    assert xml.tag == 'testsuite'



# Generated at 2022-06-13 15:41:01.530426
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite_xml=TestSuite(name="test_suite")
    assert test_suite_xml.get_xml_element().tag=='testsuite'

# Generated at 2022-06-13 15:41:09.703189
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name="test_To_Cels_Zero", classname="test.test_test.test_test_test", status="success", time='0.000')
    system_err = "Test case import errors:"
    system_out = "None"

    test_suite = TestSuite(name="test.test_test", hostname="server.com", id="1", package="test", timestamp=datetime.datetime.now())
    test_suite.properties = {"key": "value"}
    test_suite.cases.append(test_case)
    test_suite.system_err = system_err
    test_suite.system_out = system_out

    element = test_suite.get_xml_element()


# Generated at 2022-06-13 15:41:20.010951
# Unit test for method get_xml_element of class TestCase

# Generated at 2022-06-13 15:41:25.368746
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Create object of class TestCase
    test_case = TestCase(
        name='test_case_name'
    )
    # Generate XML element for the test case
    xml_element = test_case.get_xml_element()
    # Convert generated XML element to string
    xml_element_string = ET.tostring(xml_element, encoding='unicode')
    # Define expected XML string
    expected_xml = '<testcase name="test_case_name" />'
    # Check if generated XML string is equal to expected XML string
    assert xml_element_string == expected_xml

# Generated at 2022-06-13 15:41:36.640230
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    timestamp = datetime.datetime.now()
    test_suite = TestSuite('test-suite', 'hostname', '1', 'com.example', timestamp)
    test_suite.properties['property'] = 'value'
    test_suite.system_out = 'stdout'
    test_suite.system_err = 'stderr'
    test_suite.cases.append(TestCase('test-case', 1, 'classname'))
    test_suite.cases.append(TestCase('test-case', 1, 'classname', time=1.0))
    test_suite.cases.append(TestCase('test-case', 1, 'classname', errors=[TestError()]))

# Generated at 2022-06-13 15:41:40.771258
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase(name='test_testcase_verify_output', time=1)
    assert testcase.get_xml_element().attrib['name'] == 'test_testcase_verify_output'
    assert testcase.get_xml_element().attrib['time'] == '1'


# Generated at 2022-06-13 15:41:43.773355
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='name')
    xml = _pretty_xml(suite.get_xml_element())
    expected = """<?xml version="1.0" ?>
<testsuite errors="0" failures="0" name="name" skipped="0" tests="0" time="0"/>
"""
    if xml != expected:
        raise Exception('Expected XML to be: ' + expected + ', but got: ' + xml)


# Generated at 2022-06-13 15:41:55.620764
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    case1 = TestCase(name='test_TestCase_get_xml_element', time=decimal.Decimal('1.234'))
    case2 = TestCase(name='test_TestSuite_get_xml_element', time=decimal.Decimal('0.345'))

    suite = TestSuite(name='unittest_junit_dataclass', timestamp=datetime.datetime(2020, 7, 22, 12, 34, 56))
    suite.cases.append(case1)
    suite.cases.append(case2)
    suite.properties['foo'] = 'bar'
    suite.system_out = 'system out message'
    suite.system_err = 'system error message'

    root = suite.get_xml_element()
    print(ET.tostring(root))

    assert root.tag

# Generated at 2022-06-13 15:42:04.218593
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    timestamp = datetime.datetime(2020, 1, 1, 12, 34, 56)
    properties = {'key1': 'value1', 'key2': 'value2'}
    system_out = 'some stdout message'
    system_err = 'some stderr message'

# Generated at 2022-06-13 15:42:13.233341
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testcase = TestCase(
        'test_case_name',
        classname="class_name",
        status="status",
        assertions=2,
        time="0.1",
    )
    testcase.output = "example output"

    suite = TestSuite(
        "test_suite_name",
        hostname="testhost",
        id="testsuite_id",
        package="testpackage",
        timestamp=datetime.datetime.now(),
    )
    suite.system_out = "suite output"
    suite.system_err = "suite error"
    suite.properties = {"key1": "value1", "key2": "value2"}
    suite.cases = [testcase]
    suite.system_out = "suite system out"

# Generated at 2022-06-13 15:42:31.151268
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name="Test case 1",
        assertions=10,
        classname="Class name",
        status="status",
        time=1.1,
        errors=[TestError('Error message')],
        failures=[TestFailure('Failure message')],
        skipped="Test case is skipped",
    )

    assert test_case.get_xml_element().tag == "testcase"



# Generated at 2022-06-13 15:42:34.962787
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    p = TestSuite('Sample Test Suite')
    print(p.get_xml_element())

if __name__ == '__main__':
    test_TestSuite_get_xml_element()

# Generated at 2022-06-13 15:42:44.304704
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name="abc",
                            testcase=[
                                TestCase(name="abc",time=1.234,
                                         error=[TestError(output="abc",message="abc",type="abc")]),
                                TestCase(name="abc",time=1.234,disabled=True),
                                TestCase(name="abc",time=1.234,skipped="abc"),
                                TestCase(name="abc",time=1.234,
                                         failure=[TestFailure(output="abc",message="abc",type="abc")])
                                ])
    testsuite.get_xml_element()


# Generated at 2022-06-13 15:42:46.849432
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name="TestSuiteName")
    assert test_suite.get_xml_element().tag == "testsuite"


# Generated at 2022-06-13 15:42:54.867380
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
	
	master_error = TestError(message='master_message', output='master_output')
	master_failure = TestFailure(message='master_message', output='master_output')
	master = TestCase(name='master_name', classname='master_class', assertions='1', status='master_status', time='12.34', errors=[master_error], failures=[master_failure], system_out='master_system_out', system_err='master_system_err')
	
	assert master.get_xml_element() == ET.Element('testcase', {'assertions': '1', 'classname': 'master_class', 'name': 'master_name', 'status': 'master_status', 'time': '12.34'})
	assert master.get_xml_element()[0].text == 'master_system_out'

# Generated at 2022-06-13 15:43:04.605462
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Dummy test case
    test_case = TestCase(name="test_case", assertions=0, classname="dummy", status="run", time=0.0)

    # Initialization of a xml element for the test case
    element = ET.Element("testcase", {"name": "test_case", "classname": "dummy", "status": "run", "time": "0.0"})

    # Initialization of an xml element to be compared with the xml element of the test case
    element_to_be_compared = test_case.get_xml_element()

    # Check if the tags are the same
    assert element.tag == element_to_be_compared.tag

    # Check if the attributes are the same
    for key, value in element.attrib.items():
        assert key in element_to_be_

# Generated at 2022-06-13 15:43:13.411826
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(name='testsuite', hostname='localhost', id='ts-id', package='com.example', timestamp=datetime.datetime.now(), properties={'prop1': 'value1', 'prop2': 'value2'}, system_out='system-out', system_err='system-err')
    tc = TestCase(name='testcase', assertions=10, classname='TestSuiteClass', status='OK', time=1.5, system_out='system-out', system_err='system-err')
    tc.errors.extend([TestError(output='error output', message='error message', type='ErrorType'), TestError(output='error2 output', message='error2 message', type='Error2Type')])

# Generated at 2022-06-13 15:43:26.100693
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # class TestSuite:
    #     """A collection of test cases."""
    #     name: str
    #     hostname: t.Optional[str] = None
    #     id: t.Optional[str] = None
    #     package: t.Optional[str] = None
    #     timestamp: t.Optional[datetime.datetime] = None
    #
    #     properties: t.Dict[str, str] = dataclasses.field(default_factory=dict)
    #     cases: t.List[TestCase] = dataclasses.field(default_factory=list)
    #     system_out: t.Optional[str] = None
    #     system_err: t.Optional[str] = None

    ts = TestSuite(name='TestSuite')
    ts_xml = ts

# Generated at 2022-06-13 15:43:37.081139
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:42.094628
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    """Unit test for method get_xml_element of class TestCase"""

    test_case = TestCase(name="test_case_name")
    assert test_case.get_xml_element().tag == 'testcase' and test_case.get_xml_element().get('name') == 'test_case_name'


# Generated at 2022-06-13 15:43:52.938710
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(name='test', timestamp=datetime.datetime(2020, 5, 9, 22, 53, 58, 110000))
    ts.properties = {'foo': 'bar', 'baz': 'qux'}
    ts.system_out = '<out>'
    ts.system_err = '<err>'
    tc = TestCase(name='test', assertions=1, classname='class', status='status', time=1.0)
    tc.skipped = 'skipped'
    tc.system_out = '<out>'
    tc.system_err = '<err>'
    tc.errors.append(TestError(output='output', message='message', type='type'))
    tc.failures.append(TestFailure(output='output', message='message', type='type'))


# Generated at 2022-06-13 15:43:58.624015
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite('TestSuite')
    xml_str = '<testsuite tests="0"></testsuite>'
    assert xml_str == _pretty_xml(test_suite.get_xml_element())


# Generated at 2022-06-13 15:44:02.006761
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name = 'TestSuite')
    print(suite.to_pretty_xml())


if __name__ == '__main__':
    test_TestSuite_get_xml_element()

# Generated at 2022-06-13 15:44:13.154608
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    timestamp = datetime.datetime.now()


# Generated at 2022-06-13 15:44:22.901861
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_name',classname='test_classname',time=1000)
    test_case.errors.append(TestError('error_output','error_message','error_type'))
    test_case.failures.append(TestFailure('failure_output','failure_message','failure_type'))
    test_case.skipped='test_skipped'
    test_case.system_out='system_out'
    test_case.system_err='system_err'
    test_case.is_disabled=True
    element = test_case.get_xml_element()
    assert element.tag == 'testcase'
    assert element.attrib['name'] == 'test_name'
    assert element.attrib['classname'] == 'test_classname'
    assert element.attrib

# Generated at 2022-06-13 15:44:32.081203
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    class Test(TestSuite):
        def __init__(self, name, hostname, id, package, timestamp, properties, cases, system_out, system_err):
            self.name = name
            self.hostname = hostname
            self.id = id
            self.package = package
            self.timestamp = timestamp
            self.properties = properties
            self.cases = cases
            self.system_out = system_out
            self.system_err = system_err
    test = Test(
        "name",
        "hostname",
        "id",
        "package",
        "timestamp",
        "properties",
        "cases",
        "system_out",
        "system_err"
    )


# Generated at 2022-06-13 15:44:43.329879
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:44:52.182509
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Create a test case
    case = TestCase(name="MyTestCase",
                    classname="MyTestCase",
                    time=0.57)
    # Add an error
    case.errors.append(TestError(output="java.lang.Exception: This is the output of the error",
                                 message="This is the error message"))
    # Add a failure
    case.failures.append(TestFailure(output="java.lang.AssertionError: This is the output of the failure",
                                     message="This is the failure message"))
    # Add system out and err
    case.system_out = "This is the system out"
    case.system_err = "This is the system err"
    # Create a test suite

# Generated at 2022-06-13 15:45:00.652880
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    cases = [TestCase(name='test_case_1')]
    suite = TestSuite(name='test_suite_1', cases=cases)
    xml_str = _pretty_xml(suite.get_xml_element())
    print(xml_str)
    assert 'test_case_1' in xml_str
    assert 'test_suite_1' in xml_str


# Generated at 2022-06-13 15:45:09.386669
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name = 'test suite',
        hostname = 'localhost',
        id = '1',
        package = 'package',
        timestamp = datetime.datetime(2020, 1, 1),

        properties = {},
        cases = [],
        system_out = 'text',
        system_err = 'text',
    )

    xml_element = suite.get_xml_element()
    assert xml_element.tag == 'testsuite'


# Generated at 2022-06-13 15:45:24.596605
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='test')
    assert test_case.get_xml_element().tag == 'testcase'
    assert test_case.get_xml_element().attrib == {'name': 'test'}


# Generated at 2022-06-13 15:45:28.985023
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite("TestSuiteTest")
    result = testsuite.get_xml_element()
    assert result.tag == "testsuite"
    return result

# Generated at 2022-06-13 15:45:37.907832
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Test case
    test_case = TestCase(
        name='test_case',
        classname='test_class',
        time=decimal.Decimal('1.2'),
        assertions=decimal.Decimal('4'),
        status='success',
        skipped='skipped',
        is_disabled=True,
    )

    test_case.errors.append(TestError())
    test_case.failures.append(TestFailure())
    test_case.failures.append(TestFailure(message='failure', type='failure_type'))

    # Test call
    xml_element = test_case.get_xml_element()

    # Test expectations

# Generated at 2022-06-13 15:45:48.354416
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Test case with failure
    test_case = TestCase(name="test_case_1")
    test_case_failure = TestFailure()
    test_case.failures.append(test_case_failure)
    test_case_failure_xml = ET.fromstring(test_case.get_xml_element().tostring(encoding='unicode'))
    assert test_case_failure_xml[0].tag == "failure"
    assert test_case_failure_xml[0].text is None

    # Test case with error
    test_case = TestCase(name="test_case_1")
    test_case_error = TestError()
    test_case.errors.append(test_case_error)

# Generated at 2022-06-13 15:46:00.022690
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    # Set attributes of TestSuite object
    testsuite = TestSuite(name='TestSuite1', timestamp=datetime.datetime.now())

    # Set attributes of TestCase object
    testcase = TestCase(name='TestCase1', assertions=10, classname='MyTestClass', status='passed',
                        time=decimal.Decimal('0.123456789'))

    # Set attributes of TestError object
    my_error = TestError(message='This is an error', type='error')

    # Set attributes of TestFailure object
    my_failure = TestFailure(message='This is a failure')

    # Add TestError object to testcase
    testcase.errors.extend([my_error])

    # Add TestFailure object to test

# Generated at 2022-06-13 15:46:05.574041
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():

    test_case = TestCase(name='test_case_name', is_disabled=True)

    result = test_case.get_xml_element()

    assert ET.tostring(result, encoding='unicode') == '<testcase assertions="0" classname="None" name="test_case_name" status="None" time="0" />'


# Generated at 2022-06-13 15:46:08.005101
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():

    # create testcase
    testCase = TestCase(name="testCaseTest")

    # check the xml element
    expected = "<testcase name=\"testCaseTest\"/>"

    actual = ET.tostring(testCase.get_xml_element(), encoding='unicode')

    assert expected == actual



# Generated at 2022-06-13 15:46:11.217932
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    TestSuite(name="test", cases=[TestCase(name="name")])
    assert TestSuite(name="test", cases=[TestCase(name="name")]) == TestSuite(name="test", cases=[TestCase(name="name")])


# Generated at 2022-06-13 15:46:16.466296
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # TestCase with no info
    test_case = TestCase(name='Simple example')
    assert test_case.get_xml_element().attrib == {'name': 'Simple example'}
    assert test_case.get_xml_element().text == None
    assert test_case.get_xml_element().find('failure') == None
    assert test_case.get_xml_element().find('error') == None
    assert test_case.get_xml_element().find('skipped') == None

    # TestCase with no extra info and output
    test_case.system_err = '<system-err>'
    test_case.system_out = '<system-out>'
    test_case_element = test_case.get_xml_element()

# Generated at 2022-06-13 15:46:19.520454
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='TestSuite', cases=[TestCase(name='TestCase')])
    element = suite.get_xml_element()
    assert '<testsuite name="TestSuite" tests="1">' in ET.tostring(element, encoding='unicode').replace('\n', '')
    assert '<testcase name="TestCase" classname="None" time="None">' in ET.tostring(element, encoding='unicode').replace('\n', '')

# Generated at 2022-06-13 15:46:51.075579
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # create an object of TestCase
    testcase = TestCase(name='foo')
    testcase.id = 'bar'
    testcase.classname = 'com.test'
    testcase.status = 'pass'
    testcase.time = '0.010'
    # create a test error
    error = TestError(output='error info')
    testcase.errors.append(error)
    # create a test failure
    failure = TestFailure(message='failure info')
    testcase.failures.append(failure)
    testcase.skipped = 'skip this test'
    testcase.system_out = 'system output'
    testcase.system_err = 'system error'
    # an object of ET.Element representing testcase
    element = testcase.get_xml_element()

# Generated at 2022-06-13 15:46:59.815051
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    assert '<testsuite disabled="2" errors="1" failures="1" hostname="localhost" id="suite-id" name="suite-name" package="com.company" skipped="2" tests="10" time="12.34"></testsuite>' == ET.tostring(TestSuite('suite-name', hostname='localhost', id='suite-id', package='com.company', timestamp=datetime.datetime.now(), disabled=2, errors=1, failures=1, skipped=2, tests=10, time=12.34).get_xml_element(), encoding='unicode')

# Generated at 2022-06-13 15:47:05.107573
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testCase = TestCase(name='test_TestCase_get_xml_element', time='0.00002')
    element = testCase.get_xml_element()
    expected = """<?xml version='1.0' encoding='UTF-8'?>
<testcase name='test_TestCase_get_xml_element' time='0.00002' />
"""
    assert _pretty_xml(element) == expected


# Generated at 2022-06-13 15:47:13.667270
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(
        name = 'XML test generate',
        hostname = '127.0.0.1',
        package = 'Test_suite_name'
    )
    test_case = TestCase(
        name = 'test_name',
        classname = 'test_class_name',
        time = decimal.Decimal('0.0248'),
    )

    test_suite.cases.append(test_case)

    result = test_suite.get_xml_element()
    assert result.get('name') == 'XML test generate'
    assert result.get('hostname') == '127.0.0.1'
    assert result.get('package') == 'Test_suite_name'

    assert result[0].get('name') == 'test_name'
   

# Generated at 2022-06-13 15:47:24.202903
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        errors=0,
        failures=0,
        hostname="localhost",
        id="org.jenkinsci.plugins.workflow.job.WorkflowRunTest",
        name="org.jenkinsci.plugins.workflow.job.WorkflowRunTest",
        package="org.jenkinsci.plugins.workflow.job",
        skipped=0,
        tests=322,
        time=4.94896,
        timestamp="2020-10-15T18:22:32"
    )
    case = TestCase(
        assertions=1,
        classname="org.jenkinsci.plugins.workflow.job.WorkflowRunTest",
        name="doesRunCanComplete",
        status="PASSED",
        time=0.115439,
    )

# Generated at 2022-06-13 15:47:25.315496
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('name')
    assert (test_case.get_xml_element().tag == 'testcase')


# Generated at 2022-06-13 15:47:33.629407
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:47:44.134569
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        classname = 'com.example.tutorial.UnitTest',
        name = 'testMultiplyException',
        time = 100.0
    )
    test_case.errors.append(
        TestError(
            message = "Expected ArithmeticException",
            output = "java.lang.ArithmeticException: / by zero\n\tat com.example.tutorial.Calculator.multiply(Calculator.java:26)\n\tat com.example.tutorial.UnitTest.testMultiplyException(UnitTest.java:38)\n",
            type = "java.lang.ArithmeticException"
        )
    )

# Generated at 2022-06-13 15:47:52.677938
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
	newCase = TestCase(name="TestCase1")
	newSuite = TestSuite(name="TestSuite1")
	newSuite.cases.append(newCase)
	element = newSuite.get_xml_element()
	assert(element.tag == 'testsuite')
	assert(element[0].tag == 'testcase')
	assert(len(element) == 1)
	assert(list(element.items()) == [('name', 'TestSuite1'), ('tests', '1')])
	assert(list(element[0].items()) == [('name', 'TestCase1')])
	

# Generated at 2022-06-13 15:47:59.779746
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
	testsuite = TestSuite('testsuite-name', 'testsuite-hostname', 'testsuite-id', 'testsuite-package', 'testsuite-timestap', 'testsuite-property', 'testsuite-case', 'testsuite-system-out', 'testsuite-system-err')
	testsuite.get_xml_element()
	assertEqual(testsuite.get_xml_element(), 1)
	

# Generated at 2022-06-13 15:48:24.705443
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name='testsuite')
    xml_element = testsuite.get_xml_element()
    assert xml_element.tag == 'testsuite'
    assert len(xml_element.attrib) == 1
    assert xml_element.attrib['name'] == testsuite.name