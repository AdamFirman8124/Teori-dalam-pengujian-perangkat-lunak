

# Generated at 2022-06-13 15:38:48.907278
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    TestSuite_end = TestSuite("testSuiteExample")
    #create a new TestCase
    test1 = TestCase("test1", time=1.0)
    #create a new TestResult (error)
    error1 = TestError("output_error1", "message_error1", "error_type1")
    #add error1 to test1
    test1.errors.append(error1)
    #create another TestResult (error)
    error2 = TestError("output_error2", "message_error2", "error_type2")
    #add error2 to test1
    test1.errors.append(error2)
    #create another TestCase
    test2 = TestCase("test2", time=1.0)
    #add test1 and test2 to TestSuite

# Generated at 2022-06-13 15:39:00.204052
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:39:05.152453
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    test_output_str = 'test_output_str'
    test_message_str = 'test_message_str'
    test_result_type_str = 'test_result_type_str'

    test_result = TestResult(output=test_output_str, message=test_message_str, type=test_result_type_str)
    test_result_dict = {'message': test_message_str, 'type': test_result_type_str}
    assert test_result.get_attributes() == test_result_dict
    

# Generated at 2022-06-13 15:39:17.050439
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite('test suite name', hostname='test hostname', id='test id', package='test package', timestamp=datetime.datetime(2020, 10, 29, 10, 41, 59), properties={'test property': 'test value'}, system_out='test system out', system_err='test system err')

# Generated at 2022-06-13 15:39:27.394650
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name='test_test_name',
        classname='test_classname',
        status='test_status',
        time=decimal.Decimal(1.23),
        errors=[
            TestError(
                output='test_error_output',
                message='test_error_message',
                type='test_error_type',
            ),
        ],
        failures=[
            TestFailure(
                output='test_failure_output',
                message='test_failure_message',
                type='test_failure_type',
            ),
        ],
        skipped='test_skipped',
        system_out='test_system_out',
        system_err='test_system_err',
    )
    root_element = ET.Element('testsuite')

# Generated at 2022-06-13 15:39:32.299184
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    ti = TestResult(output = 'Output', message = 'Message', type = 'Type')
    el = ti.get_xml_element()
    assert el.text == 'Output'
    assert el.tag == 'system-out'
    assert el.get('message') == 'Message'
    assert el.get('type') == 'Type'


# Generated at 2022-06-13 15:39:36.159172
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    xml_string = """\
<?xml version="1.0" ?>
<testResult/>
"""
    result = TestResult()
    assert _pretty_xml(result.get_xml_element()) == xml_string


# Generated at 2022-06-13 15:39:41.901492
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    result = TestResult()
    result.output = "Test output"
    result.message = "Test message"
    result.type = "Test type"
    expected = '''\
<TestResult>
  <failure message="Test message" type="Test type">Test output</failure>
</TestResult>\
'''
    actual = _pretty_xml(result.get_xml_element())
    assert actual == expected


# Generated at 2022-06-13 15:39:44.364021
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    test_result = TestResult(output='output', message='message')
    assert test_result.get_attributes() == {'message': 'message', 'type': 'TestResult'}


# Generated at 2022-06-13 15:39:53.019257
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test = TestSuite(name = 'TestName')
    testCase = TestCase(name = 'TestCaseName')
    test.cases.append(testCase)
    xml = test.get_xml_element()
    element = ET.fromstring(ET.tostring(xml))
    assert element.get('name') == 'TestName'
    assert len(element.findall('./testcase')) == 1
    assert element.findall('./testcase')[0].get('name') == 'TestCaseName'


# Generated at 2022-06-13 15:40:05.659186
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    tc = TestResult(message="failure message", type="type of failure")
    assert tc.get_attributes() == {'message': 'failure message', 'type': 'type of failure'}


# Generated at 2022-06-13 15:40:07.569057
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    type=TestError(type='aaa')
    tt=type.get_attributes()
    assert tt['type'] == 'aaa'

# Generated at 2022-06-13 15:40:10.186644
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    attr = _attributes(
            message='message',
            type='type',
        )
    assert attr == {'message': 'message', 'type': 'type'}


# Generated at 2022-06-13 15:40:22.251266
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    t_case = TestCase(name="Test1", assertions=1, classname = "TestClass", status = "Success", time = 0)
    t_case2 = TestCase(name="Test2", assertions=2, classname = "TestClass2", status = "Success", time = 0)
    t_suite = TestSuite(name="MyTestSuite", hostname = "localhost", id = "id", package = "MyPackage", timestamp = datetime.datetime.now())
    t_suite.properties = {"a" : "b", "c" : "d"}
    t_suite.cases.extend([t_case, t_case2])
    t_suite.system_out = "This is the first suite"
    t_suite.system_err = "This is the second suite"

# Generated at 2022-06-13 15:40:29.372896
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:40:39.356874
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Create a test suite
    suite = TestSuite(
        name='MyTestSuite',
        hostname='hostname',
        id='id',
        package='package',
        timestamp=datetime.datetime(2020, 6, 22),
    )

    # Add properties
    suite.properties['key'] = 'value'

    # Add a test case
    suite.cases.append(TestCase(
        name='MyTestCase',
        assertions=42,
        classname='classname',
        status='status',
        time=decimal.Decimal('1.2345678'),
    ))

    # Add another test case

# Generated at 2022-06-13 15:40:41.044206
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name='TestSuite')
    assert test_suite.get_xml_element() is not None

# Generated at 2022-06-13 15:40:43.114248
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(hostname='hostname')
    assert test_suite.get_xml_element()



# Generated at 2022-06-13 15:40:49.127901
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    test_output = '0'
    test_message = '1'
    test_type = '2'
    attributes = _attributes(
        message=test_message,
        type=test_type,
    )
    # Prepare test object
    test_result = TestResult(
        output=test_output,
        message=test_message,
        type=test_type,
    )
    # Execute method get_attributes
    result = test_result.get_attributes()
    # Check result
    assert attributes == result



# Generated at 2022-06-13 15:40:58.660316
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(
        name='Suite',
        hostname='localhost',
        id='01',
        package='suite',
        timestamp=datetime.datetime.now(),
        system_err='Error',
        system_out='Output',
        properties={
            "namespace": "http://example.com/namespace",
            "param1": "value1",
        }
    )
    # TODO: Add test cases
    ts.cases = [
        TestCase(
            name='Case',
            assertions='0',
            classname='class',
            status='status',
            time='1.234',
            skipped='Skipped',
            system_err='Error',
            system_out='Output',
            is_disabled=True,
        )
    ]
    x = ts.get_xml_

# Generated at 2022-06-13 15:41:12.822800
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    result = TestResult(output="This is a string", message="This is another string")
    assert result.get_xml_element().text == "This is a string"
    assert result.get_xml_element().get('message') == 'This is another string'


# Generated at 2022-06-13 15:41:21.945181
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    assert 1 == 1
    test_case1 = TestCase(name='TestCase1', assertions=1, classname='TestCase1', status='passed', time=1.234)
    test_case2 = TestCase(name='TestCase2', assertions=2, classname='TestCase2', status='failed', time=2.345)
    test_suite1 = TestSuite(name='TestSuite1', hostname='hostname', id='id', package='package', timestamp=datetime.datetime.now(), properties={'property1':'property1', 'property2':'property2'})
    test_suite1.cases.append(test_case1)
    test_suite1.cases.append(test_case2)
    test_suite1.system_out = 'system_out'
    test_suite

# Generated at 2022-06-13 15:41:28.990890
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestResult('this is output')
    test_result.message = 'this is message'
    test_result.type = 'this is type'

    root = test_result.get_xml_element()
    assert root.tag == 'result'
    assert dict(root.attrib) == dict(message='this is message', type='this is type')
    assert root.text == 'this is output'


# Generated at 2022-06-13 15:41:39.390155
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    for ResultClass in (TestFailure, TestError):
        assert ET.tostring(ResultClass().get_xml_element()) == b'<test_tag/>'

        assert ET.tostring(ResultClass(output='output').get_xml_element()) == b'<test_tag>output</test_tag>'
        assert ET.tostring(ResultClass(message='message').get_xml_element()) == b'<test_tag message="message"/>'
        assert ET.tostring(ResultClass(type='type').get_xml_element()) == b'<test_tag type="type"/>'

        assert ET.tostring(ResultClass(output='output', message='message').get_xml_element()) == b'<test_tag message="message">output</test_tag>'

# Generated at 2022-06-13 15:41:44.271616
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    class TestSuite:
        def __init__(self, name, id, timestamp, cases):
            self.name = name
            self.id = id
            self.timestamp = timestamp
            self.cases = cases

        def get_attributes(self):
            return {'name': self.name, 'id': self.id, 'timestamp': self.timestamp.isoformat(timespec='seconds')}

        def get_xml_element(self):
            element = ET.Element('testsuite', self.get_attributes())
            element.extend([case.get_xml_element() for case in self.cases])
            return element

    class TestCase:
        def __init__(self, name, classname, time):
            self.name = name
            self.classname = classname
            self.time = time

# Generated at 2022-06-13 15:41:53.791538
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite("name","hostname")
    element = suite.get_xml_element()
    assert element.tag == "testsuite"
    assert element.get("name") == "name"
    assert element.get("hostname") == "hostname"
    assert element.get("tests") == "0"
    assert element.get("errors") == "0"
    assert element.get("failures") == "0"
    assert element.get("disabled") == "0"
    assert element.get("skipped") == "0"
    assert element.get("time") == "0"


# Generated at 2022-06-13 15:41:54.890169
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    pass


# Generated at 2022-06-13 15:41:57.035422
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
	element = ET.Element("testcase")
	
	assert(element.tag == "testcase")


# Generated at 2022-06-13 15:42:02.081207
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    output_message = "Test"
    error_type = "test_error"
    error_instance = TestError(output=output_message, type=error_type)

    root = ET.Element('error')
    root.text = output_message
    root.set('type', error_type)

    assert root == error_instance.get_xml_element()
    # Unit test for method get_xml_element of class TestCase

# Generated at 2022-06-13 15:42:08.545886
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    output = 'output'
    message = 'message'
    type = 'type'
    tresult = TestResult(output=output, message=message, type=type)
    xml_result = tresult.get_xml_element()

    assert xml_result.tag == 'failure'
    assert xml_result.text == output
    assert xml_result.get('message') == message
    assert xml_result.get('type') == type
    


# Generated at 2022-06-13 15:42:22.990171
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='test_unconstrained', assertions=1)
    assert ET.tostring(test_case.get_xml_element(), encoding='unicode') == "<testcase assertions=\"1\" name=\"test_unconstrained\" />"
    
    test_case = TestCase(name='test_unconstrained', assertions=1, is_disabled=True)
    assert ET.tostring(test_case.get_xml_element(), encoding='unicode') == "<testcase assertions=\"1\" name=\"test_unconstrained\" />"
    
    test_case = TestCase(name='test_unconstrained', assertions=1, errors=[TestError(output="ERROR DETAIL WITH &", message="Generic Error", type="TypeSpecificError")])

# Generated at 2022-06-13 15:42:33.306116
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(
        name='test_add',
        assertions=None,
        classname='TestCalculator',
        status=None,
        time='.001',
        errors=None,
        failures=None,
        skipped=None,
        system_out=None,
        system_err=None,
        is_disabled=False
    )
    test_suite = TestSuite(
        name='test_suite_calculator',
        hostname=None,
        id=None,
        package=None,
        timestamp=None,
        properties=None,
        cases=[test_case],
        system_out=None,
        system_err=None
    )
    xml_element = test_suite.get_xml_element()
    assert xml_element.attrib['tests']

# Generated at 2022-06-13 15:42:45.210826
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    ts = TestSuite(name='testsuite name', id='testsuite id')
    ts.cases.append(TestCase('testcase name'))
    ts.system_out = 'system out'
    ts.system_err = 'system err'

    xmlString = ts.to_pretty_xml()

# Generated at 2022-06-13 15:42:52.657233
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name = "TestName",
        assertions = 1,
        classname = "com.test.ClassName",
        status = "Success",
        time = decimal.Decimal(1.234),
        system_out = "Test Output",
        system_err = "Test Errors"
    )
    expected_xml = \
    """<testcase assertions="1" classname="com.test.ClassName" name="TestName" status="Success" time="1.234">
        <system-out>Test Output</system-out>
        <system-err>Test Errors</system-err>
    </testcase>"""
    assert _pretty_xml(test_case.get_xml_element()) == expected_xml



# Generated at 2022-06-13 15:42:55.870495
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase("Test case name")
    assert _pretty_xml(tc.get_xml_element()) == (
        '<?xml version="1.0" ?>\n'
        '<testcase name="Test case name"/>\n'
    )

# Generated at 2022-06-13 15:43:05.314027
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():

    test_suite = TestSuite(name='Test Suite')
    test_suite.cases.append(TestCase(name='Test Case 1'))
    test_suite.cases.append(TestCase(name='Test Case 2'))

    test_suite.properties['Test'] = 'Value'

    test_suite.system_out = 'Hello world'
    test_suite.system_err = 'This is an error'


# Generated at 2022-06-13 15:43:12.619525
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(
        name = "suite_name",
        hostname = None,
        id = None,
        package = None,
        timestamp = None,
    )
    tcs = TestCase(
        name = "case_name",
        assertions = None,
        classname = "class_name",
        status = None,
        time = None,
    )
    ts.cases.append(tcs)
    assert str(ts.get_xml_element()) == "<testsuite name='suite_name'><testcase name='case_name' classname='class_name' /></testsuite>"

# Generated at 2022-06-13 15:43:25.309564
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    #  Create an object of TestCase
    testCase = TestCase("MyName", 2, "MyClass", "PASS", 1.0)
    # Add a error to testCase
    error = TestError("MyMessage", "MyOutput")
    testCase.errors.append(error)
    # Add a failure to testCase
    failure = TestFailure("MyMessage", "MyOutput")
    testCase.failures.append(failure)
    # Return the xml element of testCase and then convert it to string
    testCaseXML = testCase.get_xml_element()
    testCaseXMLStr = ET.tostring(testCaseXML, encoding = 'unicode')
    # Return the xml element of TestCase created with the default factory and convert it to string

# Generated at 2022-06-13 15:43:35.611346
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase(name='TestCase_name')
    tc.time = decimal.Decimal(3.3)
    tc.system_err = 'TestCase_system_err'
    tc.system_out = 'TestCase_system_out'

    e = tc.get_xml_element()
    assert e.tag == 'testcase'
    assert 'name="TestCase_name"' in e.attrib
    assert 'time="3.3"' in e.attrib
    assert len(e.findall('system-err')) == 1
    assert len(e.findall('system-out')) == 1
    assert e.find('system-err').text == 'TestCase_system_err'
    assert e.find('system-out').text == 'TestCase_system_out'


# Generated at 2022-06-13 15:43:46.139733
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_result = TestError()
    test_result.output = 'dummy'
    test_result.message = 'dummy'
    test_result.type = 'dummy'
    test_case = TestCase()
    test_case.name = "test_name"
    test_case.assertions = "test_assertions"
    test_case.classname = "test_classname"
    test_case.status = "test_status"
    test_case.time = decimal.Decimal(1)
    test_case.errors = [test_result]
    test_case.failures = []
    test_case.skipped = "test_skipped"
    test_case.system_out = "test_system_out"
    test_case.system_err = "test_system_err"
    test

# Generated at 2022-06-13 15:44:10.537749
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    hostname = 'localhost'
    time = decimal.Decimal('0.46')
    suite = TestSuite(
        name='BasicTest',
        hostname=hostname,
        time=time,
        properties={'foo': 'bar'},
        cases=[
            TestCase(
                name='test_foo',
                time=time,
                system_out='System out',
                system_err='System error'
            )
        ],
    )

    element = suite.get_xml_element()

    assert element.tag == 'testsuite'

# Generated at 2022-06-13 15:44:15.091806
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    x = TestCase('name', 'classname', 1.5)
    assert x.get_xml_element().tag == 'testcase'
    assert x.get_xml_element().attrib['name'] == 'name'
    assert x.get_xml_element().attrib['classname'] == 'classname'
    assert x.get_xml_element().attrib['time'] == '1.500000'



# Generated at 2022-06-13 15:44:18.508667
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():

    testcase = TestCase(name='TestCase', assertions='3')

    assert TestCase.get_xml_element(testcase) == ET.Element("testcase", {'name':'TestCase', 'assertions':'3'})


# Generated at 2022-06-13 15:44:23.247481
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name='test_case_1',
        classname='TestCase',
        time='0.001',
    )
    expected = """<testcase classname="TestCase" name="test_case_1" time="0.001" />"""
    assert ET.tostring(test_case.get_xml_element(), encoding='unicode') == expected


# Generated at 2022-06-13 15:44:28.886407
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    t1 = TestCase(name="TestCase 1")
    result = t1.get_xml_element()
    expected_result = ET.fromstring(
        ET.tostring(ET.fromstring('''<testcase name="TestCase 1"></testcase>''')))
    assert result == expected_result

    t2 = TestCase(name="TestCase 2", system_out="System output")
    result = t2.get_xml_element()
    expected_result = ET.fromstring(
        ET.tostring(ET.fromstring('''<testcase name="TestCase 2"><system-out>System output</system-out></testcase>''')))
    assert result == expected_result


# Generated at 2022-06-13 15:44:41.065728
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase("name",
                         assertions=None,
                         classname=None,
                         status=None,
                         time=None)

    assert prettyXml(test_case.get_xml_element()) == '''
<testcase name="name" />
'''
    test_case = TestCase("name",
                         assertions=1,
                         classname="classname",
                         status="status",
                         time=decimal.Decimal("0.123"))

    assert prettyXml(test_case.get_xml_element()) == '''
<testcase assertions="1" classname="classname" name="name" status="status" time="0.123" />
'''

    test_case.skipped = "skipped"


# Generated at 2022-06-13 15:44:45.355541
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase("KalkulatorTest.test_add_numbers")
    assert ET.tostring(testcase.get_xml_element(), encoding='unicode') == "<testcase name=\"KalkulatorTest.test_add_numbers\"/>"


# Generated at 2022-06-13 15:44:53.909614
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(
        name="pytest suite",
        timestamp='2019-12-02T13:42:00',
        errors=0,
        failures=1,
        disabled=1,
        skipped=0,
        tests=2,
        time=0.9
    )

    testcase1 = TestCase(
        name="test_method1", classname="test_class1",
        time=0.1, assertions=1, status="success",
        system_out="System out 1", system_err="System error 1"
    )

# Generated at 2022-06-13 15:45:05.902011
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
        ts1=TestSuite(name='example_suite_name',properties={'example_property_key': 'example_property_value'},)
        tc1=TestCase(name='example_test_name',classname='example_class_name',time=decimal.Decimal('1.000'),)
        te1=TestError(output='example_test_output',message='example_test_message',type='example_test_type',)
        tf1=TestFailure(output='example_test_output',message='example_test_message',type='example_test_type',)

        ts1.cases.append(tc1)
        tc1.errors.append(te1)
        tc1.failures.append(tf1)
        
        #test if test cases, errors, failures and properties are added to the xml_element


# Generated at 2022-06-13 15:45:16.876666
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    expected_xml = ('<testcase name="testCaseName" time="0.0" assertions="1">'
                    '<failure message="message" type="type">output</failure>'
                    '<error message="message" type="type">output</error>'
                    '</testcase>')
    test_case = TestCase(name='testCaseName', time=0, assertions=1)
    test_case.failures.append(TestFailure('output', 'message', 'type'))
    test_case.errors.append(TestError('output', 'message', 'type'))

    actual_xml = ET.tostring(test_case.get_xml_element(), encoding='unicode')

    assert expected_xml == actual_xml


# Generated at 2022-06-13 15:45:36.783845
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_case')
    assert test_case.get_xml_element().tag == 'testcase'
    assert test_case.get_xml_element().attrib == {'name': 'test_case'}
    assert _pretty_xml(test_case.get_xml_element()) == '<testcase name="test_case"/>'

    test_case = TestCase(name='test_case', assertions=1, classname='TestCase', status='STATUS', time=1.0)
    assert test_case.get_xml_element().tag == 'testcase'
    assert test_case.get_xml_element().attrib == {'name': 'test_case', 'assertions': '1', 'classname': 'TestCase', 'status': 'STATUS', 'time': '1.0'}


# Generated at 2022-06-13 15:45:41.778453
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(name="testsuite")
    ts.cases.append(TestCase(name="testcase"))
    assert ET.tostring(ts.get_xml_element()) == b'<testsuite name="testsuite" tests="1">\n  <testcase name="testcase"></testcase>\n</testsuite>'

# Generated at 2022-06-13 15:45:51.198399
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    import xml.etree.ElementTree as ET
    import datetime
    test_case1=TestCase("test name 1",
                        assertions=None,
                        classname=None,
                        status=None,
                        time=decimal.Decimal("3.12"))
    test_case1.skipped="skipped text 1"
    test_case1.system_out="some system out text 1"
    test_case1.system_err="some system err text 1"
    
    test_case2=TestCase("test name 2",
                        assertions=None,
                        classname=None,
                        status=None,
                        time=decimal.Decimal("1.12"))
    test_case2.skipped=None
    test_case2.system_

# Generated at 2022-06-13 15:45:55.807835
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite('test', timestamp=datetime.datetime.now())
    print(ET.tostring(ts.get_xml_element(), encoding='utf8').decode('utf8'))

# Generated at 2022-06-13 15:46:04.687036
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    expected = """<testcase assertions="1" classname="com.my.package" name="method_name" status="PASSED" time="1.234">
  <error message="&amp;&lt;&gt;&amp;&amp;&quot;&apos;"><![CDATA[TRACE]]></error>
  <failure message="&amp;&lt;&gt;&amp;&amp;&quot;&apos;"><![CDATA[TRACE]]></failure>
  <skipped>skip reason</skipped>
  <system-out>stdout</system-out>
  <system-err>stderr</system-err>
</testcase>"""

# Generated at 2022-06-13 15:46:08.411664
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="test_case_name")
    element = test_case.get_xml_element()
    assert element.tag == 'testcase'
    assert element.attrib["name"] == 'test_case_name'

# Generated at 2022-06-13 15:46:11.608792
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testSuite = TestSuite('my_name', 'my_hostname', 'my_id', 'my_package', datetime.datetime.now())
    print(testSuite.get_xml_element())


# Generated at 2022-06-13 15:46:17.580394
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tcase = TestCase(name='MyPackage.MyTestCase')
    assert tcase.get_xml_element().tag == 'testcase'
    ET.SubElement(tcase.get_xml_element(), 'system-out').text = 'This is a test'
    assert tcase.get_xml_element().find('system-out').text == 'This is a test'


# Generated at 2022-06-13 15:46:20.183750
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite("My Test Suite", timestamp=datetime.datetime.now())
    assert test_suite._get_xml_element() == ET.Element("testsuite", test_suite.get_attributes())


# Generated at 2022-06-13 15:46:30.622994
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testSuite = TestSuite(
        "testSuite",
        timestamp=datetime.datetime.now(),
        properties={"language": "Python"},
    )
    testSuite.cases = [
        TestCase("testCase"),
    ]
    element = ET.fromstring(testSuite.get_xml_element().tostring())
    assert element.tag == 'testsuite'
    assert element[0].tag == 'properties'
    assert element[0][0].tag == 'property'
    assert element[2].tag == 'testcase'
    assert element[2].attrib['name'] == 'testCase'

# Generated at 2022-06-13 15:46:50.889109
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    system_out = 'out'
    system_err = 'err'
    disabled = 'disabled'
    errors = 'errors'
    failures = 'failures'
    hostname = 'hostname'
    id = 'id'
    name = 'name'
    package = 'package'
    skipped = 'skipped'
    tests = 'tests'
    time = 'time'
    timestamp = datetime.datetime.now().isoformat(timespec='seconds')
    properties = {'prop': 'val'}
    cases = [TestCase('test1')]

# Generated at 2022-06-13 15:47:01.842490
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite."""
    print("Test for method get_xml_element of class TestSuite")

# Generated at 2022-06-13 15:47:12.549183
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(
        id='1',
        name='Suite1',
        hostname='localhost',
        tests=1,
        errors=0,
        failures=1,
        timestamp=datetime.datetime(2020, 7, 14, 23, 24, 26, 448627),
        skipped=0,
        time=0.005,
        disabled=0,
    )

    element = test_suite.get_xml_element()
    assert element.get('id') == '1'
    assert element.get('name') == 'Suite1'
    assert element.get('hostname') == 'localhost'
    assert element.get('tests') == '1'
    assert element.get('errors') == '0'
    assert element.get('failures') == '1'
    assert element

# Generated at 2022-06-13 15:47:22.710384
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(
        name='Suite 1',
        cases=[TestCase(name='Case 1', time=decimal.Decimal(1))],
    )
    test_suite_string = r'''
<testsuite disabled="0" errors="0" failures="0" hostname="localhost" name="Suite 1" skipped="0" tests="1" time="1">
  <testcase assertions="None" classname="None" name="Case 1" status="None" time="1"/>
</testsuite>
'''.strip()

    test_suite_xml_string = _pretty_xml(test_suite.get_xml_element())

    assert test_suite_xml_string == test_suite_string


# Generated at 2022-06-13 15:47:30.364384
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase('test_name')
    assert ET.tostring(tc.get_xml_element(), encoding='unicode') == '''
        <testcase assertions="None" classname="None" name="test_name" status="None" time="None" />
    '''.strip()

    tc = TestCase('test_name', assertions=1)
    assert ET.tostring(tc.get_xml_element(), encoding='unicode') == '''
        <testcase assertions="1" classname="None" name="test_name" status="None" time="None" />
    '''.strip()

    tc = TestCase('test_name', classname='test_classname')

# Generated at 2022-06-13 15:47:41.311386
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase('my_test')
    tc.time = 1.5

    assert ET.tostring(tc.get_xml_element(), encoding='unicode') == '<testcase name="my_test" time="1.5" />'

    tc.errors.append(TestError(message='An error', output='Some output'))

    assert ET.tostring(tc.get_xml_element(), encoding='unicode') == '<testcase name="my_test" time="1.5"><error message="An error">Some output</error></testcase>'

    tc.failures.append(TestFailure(message='A failure', output='Some other output'))


# Generated at 2022-06-13 15:47:42.138827
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    p = TestSuite("example")
    p.get_xml_element()


# Generated at 2022-06-13 15:47:52.848946
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # test with empty set of testcases
    testsuite = TestSuite("suite", timestamp=datetime.datetime.now())
    element = testsuite.get_xml_element()
    assert element.tag == 'testsuite'
    for testcase in element:
        if testcase.tag == 'testcase':
            raise ValueError("Unexpected testcase {}".format(testcase.attrib))
    # test with non-empty set of testcases
    testsuite = TestSuite("suite", timestamp=datetime.datetime.now())
    testcase = TestCase("testcase")
    testsuite.cases.append(testcase)
    element = testsuite.get_xml_element()
    assert element.tag == 'testsuite'
    found_testcase = False

# Generated at 2022-06-13 15:48:04.524480
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    test_suite = TestSuite('testsuite_name')
    test_suite.properties = {'key': 'value'}
    test_suite.system_out = 'system_out'
    test_suite.system_err = 'system_err'
    test_suite.cases = [
        TestCase(
            name='testcase_name',
            failures=[TestFailure(message='failure_message', output='failure_output')],
            errors=[TestError(message='error_message', output='error_output')],
            skipped='skipped',
            system_out='system_out',
            system_err='system_err',
        ),
        TestCase(
            name='testcase_name',
        ),
    ]

# Generated at 2022-06-13 15:48:16.075548
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase(name='test_case')
    tc.errors = [TestError(output='error_output', message='error_message', type='error_type')]
    tc.failures = [TestFailure(output='failure_output', message='failure_message', type='failure_type')]
    tc.skipped = 'skipped'
    tc.system_out = 'system_out'
    tc.system_err = 'system_err'

    root = tc.get_xml_element()

    assert root.tag == 'testcase'
    assert root.attrib == {'name': 'test_case'}
    assert root[0].tag == 'error'
    assert root[0].attrib == {'message': 'error_message',
                              'type': 'error_type'}
    assert root

# Generated at 2022-06-13 15:48:30.448878
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # build a TestCase
    case = TestCase(name="testcase_name")

    # build a TestSuite
    suite = TestSuite(name="test_name")
    suite.cases.append(case)

    # get xml for TestSuite
    xml = suite.get_xml_element()

    # check the name of the TestSuite
    assert xml.get('name') == suite.name

    # check the number of testcases inside the TestSuite
    assert xml.find('testcase').get('name') == case.name