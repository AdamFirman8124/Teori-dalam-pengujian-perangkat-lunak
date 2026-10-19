

# Generated at 2022-06-13 15:38:40.901084
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestFailure(output='test output')
    assert '<failure>test output' in ET.tostring(test_result.get_xml_element()).decode('utf-8')


# Generated at 2022-06-13 15:38:45.131814
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    # Test instance has no attributes set
    instance = TestResult()
    assert instance.get_xml_element() == ET.Element('testresult')

    # Test instance has all attributes set
    instance = TestResult(
        output='Test output',
        message='Test message',
        type='Test type',
    )
    element = ET.Element('testresult', {
        'message': 'Test message',
        'type': 'Test type',
    })
    element.text = 'Test output'
    assert instance.get_xml_element() == element


# Generated at 2022-06-13 15:38:47.315403
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    result = TestResult()
    attributes = result.get_attributes()
    assert(attributes == {'type': 'TestResult'})



# Generated at 2022-06-13 15:38:50.102372
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    tc = TestResult(message='test_message', output='test_output', type='test_type')
    assert tc.get_attributes() == {'message': 'test_message', 'type': 'test_type'}

# Generated at 2022-06-13 15:38:56.668898
# Unit test for method get_xml_element of class TestSuites
def test_TestSuites_get_xml_element():
    suites = TestSuites(name="suites")
    assert suites.to_pretty_xml() == '<?xml version="1.0" ?>\n<testsuites failures="0" disabled="0" errors="0"/>\n'

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    print("Running unit tests")
    test_TestSuites_get_xml_element()

# Generated at 2022-06-13 15:39:04.785976
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
        # Verify tag name
        result = TestFailure(output='test_output', message='test_message', type='test_type')
        expected_tag_name = 'failure'
        assert result.get_xml_element().tag == expected_tag_name
        assert result.get_xml_element().text == 'test_output'
        assert result.get_xml_element().attrib == {'message': 'test_message', 'type': 'test_type'}

        result = TestError(output='test_output', message='test_message', type='test_type')
        expected_tag_name = 'error'
        assert result.get_xml_element().tag == expected_tag_name
        assert result.get_xml_element().text == 'test_output'

# Generated at 2022-06-13 15:39:10.586681
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    test_result = TestResult(output='test_output', message='test_message', type='test_type')
    expected_attributes = _attributes(message='test_message', type='test_type')
    assert test_result.get_attributes() == expected_attributes


# Generated at 2022-06-13 15:39:17.841454
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    r = TestResult()
    assert 'message' not in r.get_attributes()
    assert 'type' not in r.get_attributes()
    r.message = None
    r.type = None
    assert 'message' not in r.get_attributes()
    assert 'type' not in r.get_attributes()
    r.message = 'Test message'
    r.type = 'Test type'
    assert 'message' in r.get_attributes()
    assert 'type' in r.get_attributes()


# Generated at 2022-06-13 15:39:18.500911
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    pass

# Generated at 2022-06-13 15:39:24.499132
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    TestResult_class = TestResult(output="nose.failure.Failure: Assertion failed", message="Assertion failed", type="Failure")
    assert TestResult_class.get_xml_element().tag == "failure"
    assert TestResult_class.get_xml_element().text == "nose.failure.Failure: Assertion failed"
    assert TestResult_class.get_xml_element().keys() == ["message", "type"]
    assert TestResult_class.get_xml_element().get("type") == "Failure"


# Generated at 2022-06-13 15:39:40.138595
# Unit test for method get_xml_element of class TestCase

# Generated at 2022-06-13 15:39:51.098885
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():

	# Create an instance of class TestSuite
	suite = TestSuite(
		hostname = "hostname",
		name = "name",
		timestamp = datetime.datetime(2020, 6, 9),
	)

	# Get the XML element of suite
	element = suite.get_xml_element()

	# Assert that element has the attribute "hostname" with value "hostname"
	assert element.attrib["hostname"] == "hostname"

	# Assert that element has the attribute "name" with value "name"
	assert element.attrib["name"] == "name"

	# Assert that element has the attribute "timestamp" with value "2020-06-09T00:00:00"

# Generated at 2022-06-13 15:39:59.546529
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='TestCase', time='0.0')
    test_case.errors.append(TestError(message='My Error', output='My Error'))
    test_case.failures.append(TestFailure(message='My Failure', output='My Failure'))
    test_case.system_out = 'My System Out'
    test_case.system_err = 'My System Err'

# Generated at 2022-06-13 15:40:02.437786
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testSuite = TestSuite('name')
    assert testSuite.get_xml_element() == ET.Element('testsuite', {'name': 'name'})


# Generated at 2022-06-13 15:40:07.202443
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    from decimal import Decimal

    timestamps = [
        '1970-01-01T00:00:00',
        '1970-01-01T00:00:01',
        '1970-01-01T00:00:02',
        '1970-01-01T00:00:03',
        '1970-01-01T00:00:04',
        '1970-01-01T00:00:05',
        '1970-01-01T00:00:06',
        '1970-01-01T00:00:07',
        '1970-01-01T00:00:08',
        '1970-01-01T00:00:09',
    ]

# Generated at 2022-06-13 15:40:09.530665
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Case 1 : name and classname are not None but other attributes are None
    test_case = TestCase('MyUnitTest', classname='TestCase')
    assert test_case.get_xml_element().get('name') == 'MyUnitTest'
    assert test_case.get_xml_element().get('classname') == 'TestCase'


# Generated at 2022-06-13 15:40:18.937562
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    print(TestSuite(name="TestPeeler", hostname="hostname", id="1234", package="package", timestamp=datetime.datetime(2012, 9, 5, 14, 27, 15), properties={'hello': 'world'}, cases=[TestCase(name="abc", assertions=5, classname="classname", status="status", time=1), TestCase(name="def", assertions=10, classname="classname", status="status", time=2)], system_out="system_out", system_err="system_err").get_xml_element())


# Generated at 2022-06-13 15:40:28.860716
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    case1=TestCase(name='test1')
    case2=TestCase(name='test2')
    case3=TestCase(name='test3')
    cases=[case1, case2, case3]

    properties={'a':'A', 'b':'B'}

    suite=TestSuite(name='suite1', cases=cases, properties=properties)

    xml_element=suite.get_xml_element()

    assert xml_element.tag=='testsuite'
    assert xml_element.attrib=={'name':'suite1', 'tests':'3'}

    properties_element=xml_element.find('properties')

    assert properties_element.find('property').attrib=={'name':'a', 'value':'A'}

# Generated at 2022-06-13 15:40:38.943195
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Test case 1
    testcase1 = TestCase("name", "classname", "2.2", "error")
    testsuite1 = TestSuite("name", "hostname", "1", "package", "timestamp")
    testsuite1.system_out = "system_out"
    testsuite1.cases.append(testcase1)

    result = testsuite1.get_xml_element()
    assert result.tag == "testsuite"
    assert result.attrib["name"] == "name"
    assert result.attrib["hostname"] == "hostname"
    assert result.attrib["id"] == "1"
    assert result.attrib["package"] == "package"
    assert result.attrib["timestamp"] == "timestamp"

# Generated at 2022-06-13 15:40:48.469156
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """
    Tests for method get_xml_element in class TestSuite
    """

    @dataclasses.dataclass
    class MockTestCase(TestCase):
        name: str
        assertions: int = 3
        classname: str = 'testing.class'
        status: str = 'PASS'
        time: decimal.Decimal = decimal.Decimal('0.001')


# Generated at 2022-06-13 15:41:02.452154
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    expected_xml = '''<testsuite disabled="0" errors="0" failures="0" name="name" tests="1" time="0.0">
  <properties/>
  <testcase assertions="0" classname="classname" name="name" status="PASSED" time="1.1"></testcase>
</testsuite>
'''

    suite = TestSuite(
        name='name',
        cases=[TestCase(name='name', classname='classname', time=decimal.Decimal('1.1'))]
    )
    assert suite.get_xml_element().tag == 'testsuite'
    assert str(ET.tostring(suite.get_xml_element(), encoding='unicode')) == expected_xml

# Generated at 2022-06-13 15:41:09.462720
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    root = ET.Element('TestCase')
    name = ET.SubElement(root, 'name')
    name.text = 'Test1'
    ET.SubElement(root, 'TestSuite').text = 'UnitTest'
    ET.SubElement(root, 'TestMethod').text = 'test1'
    ET.SubElement(root, 'TestClass').text = 'UnitTest1'

    assert root.get_xml_element() == "TestCase"


# Generated at 2022-06-13 15:41:12.980085
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    try:
        testsuite = TestSuite("test")
        xml_element = testsuite.get_xml_element()

        assert xml_element is not None
    except:
        assert False

# Generated at 2022-06-13 15:41:22.078934
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """
    This function tests the xml element created by class TestSuite
    """
    test_case = TestCase(
        classname="AK",
        name="test1",
        time=1.0
    )

    test_suite = TestSuite(
        cases=[test_case],
        name="AK",
        timestamp=datetime.datetime.now()
    )

    actual = test_suite.get_xml_element()

# Generated at 2022-06-13 15:41:30.762057
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(
        name='test_case_name',
        time=decimal.Decimal('0.00034'),
    )
    test_suite = TestSuite(
        name='test_suite_name',
        cases=[test_case]
    )
    assert test_suite.get_xml_element().find('testcase').text == '''<testcase assertions="None" classname="None" name="test_case_name" status="None" time="0.00034">
  </testcase>'''


# Generated at 2022-06-13 15:41:33.590742
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    from xml.etree import ElementTree as ET
    ts = TestSuite(name="1", timestamp=datetime.datetime.now())

    assert ts.get_xml_element() == ET.fromstring("<testsuite name='1' timestamp='2020-09-13T13%3A56%3A27.743312' tests='0' errors='0' failures='0' disabled='0' skipped='0' time='0.00' />")


# Generated at 2022-06-13 15:41:42.848164
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():

    s = TestSuite('TestSuite1', 'localhost', '1', 'com.example.tests', datetime.datetime.utcnow())
    s.add_property('os.name', 'Linux')
    s.add_property('pwd', '/home/test')

    tc1 = TestCase('test_case_1', 3)
    tc2 = TestCase('test_case_2', 5)
    tc3 = TestCase('test_case_3', 4)
    s.add_test_case(tc1)
    s.add_test_case(tc2)
    s.add_test_case(tc3)

    #print(s.get_xml_element())
    assert s.get_xml_element() is not None



# Generated at 2022-06-13 15:41:54.111638
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:42:03.294994
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_cases = [TestCase(name='test1', time=1.0, assertions=1, classname='testclass', status='passed'), TestCase(name='test2', time=2.0, assertions=2, classname='testclass', status='passed', skipped='skipped')]
    properties = {'platform': 'ubuntu'}
    timestamp = datetime.datetime.now()
    error = TestError(message='error1')
    test_cases[0].errors.append(error)
    failure = TestFailure(message='failure1')
    test_cases[1].failures.append(failure)

# Generated at 2022-06-13 15:42:12.628191
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    case = TestCase('MyCase')
    assert case.get_xml_element() == minidom.parseString('<testcase name="MyCase"/>').toprettyxml()
    case = TestCase('MyCase', classname='MyCase.test_case', time=0.1234)
    assert case.get_xml_element() == minidom.parseString('<testcase name="MyCase" classname="MyCase.test_case" time="0.1234"/>').toprettyxml()
    case = TestCase('MyCase', classname='MyCase.test_case', time=0.1234, is_disabled=True, output='Something went wrong')

# Generated at 2022-06-13 15:42:26.186518
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase('TestCaseName')
    testcase.assertions = 1
    testcase.classname = 'ClassName'
    testcase.status = 'passed'
    testcase.time = 0.2

    testcase.errors.append(TestError(output='TestCaseErrorOutput', message='TestCaseErrorMessage', type='TestCaseErrorType'))
    testcase.failures.append(TestFailure(output='TestCaseFailureOutput', message='TestCaseFailureMessage', type='TestCaseFailureType'))
    testcase.skipped = 'TestCaseSkipped'
    testcase.system_out = 'TestCaseSystemOut'
    testcase.system_err = 'TestCaseSystemErr'

    element = testcase.get_xml_element()

    assert element.attrib['assertions'] == '1'
    assert element

# Generated at 2022-06-13 15:42:33.659603
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="test_one")
    test_case.errors.append(TestError(output="test error"))
    test_case.failures.append(TestFailure(output="test fail"))

    expected_output = """\
<?xml version="1.0" ?>
<testcase name="test_one"><error>test error</error><failure>test fail</failure></testcase>
"""
    assert expected_output == _pretty_xml(test_case.get_xml_element())


if __name__ == '__main__':
    test_TestCase_get_xml_element()
    print("Everything passed")

# Generated at 2022-06-13 15:42:45.219438
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    Error = TestError(output="error output")
    Failure = TestFailure(output="failure output")
    Case = TestCase(name = "test_name", status="passed", assertions = 10, time = 0.3, system_out = "system out", system_err = "system err")
    Case.errors.append(Error)
    Case.failures.append(Failure)
    Suite = TestSuite(name="test_suite_name", timestamp=datetime.datetime(2020, 8, 10, 9, 18), hostname="hostname", id="id", package="package")
    Suite.cases.append(Case)
    Suite.properties = {"key1": "value1", "key2": "value2", "key3": "value3"}


# Generated at 2022-06-13 15:42:47.556640
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # arrange
    testcase = TestCase("TestCaseName")

    # act
    result = testcase.get_xml_element()

    assert result.attrib["name"] == "TestCaseName"

# Generated at 2022-06-13 15:42:55.961612
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite_1 = TestSuite(
        name='testsuite_1',
        cases=[
            TestCase(name='case_1'),
            TestCase(name='case_2'),
        ]
    )
    testsuite_2 = TestSuite(
        name='testsuite_2',
        cases=[
            TestCase(name='case_3'),
            TestCase(name='case_4'),
        ]
    )
    testsuites = TestSuites(
        suites=[testsuite_1, testsuite_2]
    )
    assert testsuites.get_xml_element().tag == 'testsuites'



# Generated at 2022-06-13 15:43:01.699823
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='foo', hostname='bar')
    xml_string = _pretty_xml(suite.get_xml_element())
    xml_string_expected = '''<?xml version="1.0" ?>
<testsuite disabled="0" errors="0" failures="0" hostname="bar" name="foo" skipped="0" tests="0" time="0"/>
'''
    assert xml_string == xml_string_expected

# Generated at 2022-06-13 15:43:11.589682
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:21.458655
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Test setup
    test_case = TestCase(name='hello')
    test_suite = TestSuite(name='my_suite', cases=[test_case])

    # Test execution
    result = test_suite.get_xml_element()

    # Test verification
    assert result.tag == 'testsuite'
    assert result.get('name') == 'my_suite'
    assert result.get('tests') == '1'
    assert len(result) == 1

    assert result[0].tag == 'testcase'
    assert result[0].get('name') == 'hello'



# Generated at 2022-06-13 15:43:25.204504
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        classname='test.test_test',
        name='test_test',
        time=0.01
    )
    assert test_case.get_xml_element().tag == 'testcase'

# Generated at 2022-06-13 15:43:35.356991
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:52.161065
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts1 = TestSuite(name="mjml", hostname="fry")
    ts1.cases.append(TestCase(name="test1"))
    ts1.cases.append(TestCase(name="test2"))

    s = _pretty_xml(ts1.get_xml_element())
    assert (s == '''<?xml version="1.0" ?>
<testsuite disabled="0" errors="0" failures="0" hostname="fry" id="" name="mjml" package="" skipped="0" tests="2" time="0">
  <testcase assertions="" classname="" name="test1" status="" time=""/>
  <testcase assertions="" classname="" name="test2" status="" time=""/>
</testsuite>
'''
            )



# Generated at 2022-06-13 15:44:03.856657
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name="Test Suite",
        id="1",
        timestamp=datetime.datetime.now(),
        cases=[
            TestCase(
                name="Test Case",
                classname="Test",
            )
        ],
        system_out="Output",
        system_err="Error",
    )


# Generated at 2022-06-13 15:44:14.492643
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:44:17.135568
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('case_name')
    assert test_case.get_xml_element().attrib['name'] == 'case_name'



# Generated at 2022-06-13 15:44:23.404398
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase('test_case_A', assertions=1, classname='TestClassA', time=0.25)
    test_suite = TestSuite('test_suite_A', name='TestSuiteA', timestamp=datetime.datetime.now())
    test_suite.cases.append(test_case)

    element = test_suite.get_xml_element()
    print(element)

if __name__ == '__main__':
    test_TestSuite_get_xml_element()

# Generated at 2022-06-13 15:44:25.629709
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    TestSuite(name="test", disabled=0, errors=0, failures=0, hostname="host", id="id", package="package", skipped=0, tests=0, time=1, timestamp=datetime.datetime.now())

# Generated at 2022-06-13 15:44:30.257382
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='foo')
    expected = '<testsuite disabled="0" errors="0" failures="0" tests="0" time="0.0" name="foo" />'
    assert ET.tostring(suite.get_xml_element(), encoding='unicode') == expected


# Generated at 2022-06-13 15:44:41.944229
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    t1 = TestCase(
        name='test case 1',
        classname='com.example.TestCase1',
        time=decimal.Decimal('1.234'),
        status='status1',
        assertions=2
    )
    t2 = TestCase(
        name='test case 2',
        classname='com.example.TestCase2',
        time=decimal.Decimal('2.345'),
        status='status2',
        assertions=3
    )
    t3 = TestCase(
        name='test case 3',
        classname='com.example.TestCase3',
        time=decimal.Decimal('3.456'),
        status='status3',
        assertions=4
    )

# Generated at 2022-06-13 15:44:51.180324
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    import unittest.mock
    import xml.etree.ElementTree as ET

    # Create a test case
    test_case = TestCase(name='test_foo')
    test_case.system_err = 'err out'
    test_case.system_out = 'std out'
    test_case.skipped = 'exception'
    test_case.status = '1'
    test_case.time = '0.123'

    # Create an error
    error = TestError(
        message='error message',
        output='error output',
        type='test',
    )
    test_case.errors.append(error)

    # Create a failure
    failure = TestFailure(
        message='failure message',
        output='failure output',
        type='test',
    )

# Generated at 2022-06-13 15:44:53.095287
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    t = TestSuite(name = 'T1', hostname = 'test')
    assert(t.get_xml_element().tag == 'testsuite')

# Generated at 2022-06-13 15:45:03.751767
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_case', time=0.1)
    xml = test_case.get_xml_element()
    assert xml.tag == 'testcase'
    assert not xml.text
    assert xml.attrib['time'] == '0.1'


# Generated at 2022-06-13 15:45:11.408671
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:45:20.332514
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:45:32.574863
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    case_1 = TestCase(
        name = "test_case_1",
        classname = "testmodule.testcase.classname",
        status = "status",
        time = 9.87
    )
    case_2 = TestCase(
        name = "test_case_2",
        classname = "testmodule.testcase.classname",
        status = "status",
        time = 9.87
    )

# Generated at 2022-06-13 15:45:36.554988
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test = TestSuite(name='name')
    xml_element = test.get_xml_element()

    print(ET.tostring(xml_element, encoding='unicode'))
    assert xml_element.tag == 'testsuite'
    assert xml_element.attrib['name'] == 'name'


# Generated at 2022-06-13 15:45:38.321219
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase(name='the name')
    print(tc.get_xml_element())



# Generated at 2022-06-13 15:45:45.108139
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='test_case')
    assert '<testcase name="test_case"/>' == ET.tostring(test_case.get_xml_element(), encoding='unicode')

    test_case = TestCase(name='test_case', classname='test_class')
    assert '<testcase classname="test_class" name="test_case"/>' == ET.tostring(test_case.get_xml_element(), encoding='unicode')


# Generated at 2022-06-13 15:45:53.591856
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name = 'TestCase',
        assertions = '1',
        classname = 'classname',
        status = 'status',
        time = '1.1',
        skipped = 'skipped',
        system_out = 'system_out',
        system_err = 'system_err',
        is_disabled = True,
    )
    test_case.errors.append(TestError(
        output = 'output',
        message = 'message',
        type = 'type',
    ))
    test_case.failures.append(TestFailure(
        output = 'output',
        message = 'message',
        type = 'type',
    ))


# Generated at 2022-06-13 15:46:00.889043
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='TestSuite', hostname='TestHost', timestamp=datetime.datetime.now())
    suite.properties['TestProperty'] = 'TestValue'
    suite.cases = [TestCase(name='TestCase', classname='TestClass')]
    suite.system_out = 'TestSystemOut'
    suite.system_err = 'TestSystemErr'

    element = suite.get_xml_element()

    assert element.tag == 'testsuite'
    assert element.attrib['name'] == 'TestSuite'
    assert element.attrib['hostname'] == 'TestHost'
    assert element.attrib['errors'] == '0'
    assert element.attrib['failures'] == '0'
    assert element.attrib['skipped'] == '0'
    assert element.attrib

# Generated at 2022-06-13 15:46:04.970983
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    result = TestError(output='Testing')
    test_case = TestCase(name='TestCase')
    test_case.errors.append(result)
    expected = '''\
<testcase name="TestCase">
  <error>Testing</error>
</testcase>
'''
    actual = _pretty_xml(test_case.get_xml_element())
    assert actual == expected



# Generated at 2022-06-13 15:46:32.060242
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    aTestCase=TestCase(name='MyTestCase')
    aTestCaseXML=aTestCase.get_xml_element()
    assert aTestCaseXML.tag=='testcase'
    assert aTestCaseXML.get('name')=='MyTestCase'
    assert aTestCaseXML.text==None
    assert aTestCaseXML.tail==None
    assert len(aTestCaseXML)==0


# Generated at 2022-06-13 15:46:38.982359
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        name='TestMethod',
        assertions=1,
        classname='TestClass',
        status='FAILED',
        time=0.5,
        errors=[TestError(output="1", message="this is an error")],
        failures=[TestFailure(output="2", message="this is a failure")],
        skipped="Skipped message",
        system_out="System out message"
    )
    test_case.is_disabled = True
    element = test_case.get_xml_element()

    assert element.tag == 'testcase'
    assert len(element.attrib) == 6
    assert element.attrib["assertions"] == "1"
    assert element.attrib["classname"] == "TestClass"
    assert element.attrib["name"] == "TestMethod"


# Generated at 2022-06-13 15:46:48.636957
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    time = datetime.datetime.now()
    testcase = TestCase("test case name", assertions=1, classname="test class", status="status", time=time, errors=[], failures=[], skipped=None, system_out=None, system_err=None)
    element = testcase.get_xml_element()

    assert element.tag == "testcase"
    assert len(element.keys()) == 7
    assert element.get("name") == "test case name"
    assert element.get("assertions") == "1"
    assert element.get("classname") == "test class"
    assert element.get("status") == "status"
    assert element.get("time") == str(time)



# Generated at 2022-06-13 15:46:52.008333
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_xml = '''<testsuite disabled="0" errors="0" failures="0" name="" tests="1" time="0.0"></testsuite>'''
    suite = TestSuite('', 0, 0, 0, 0)
    root = suite.get_xml_element()
    assert ET.tostring(root, encoding="unicode") == test_xml


# Generated at 2022-06-13 15:47:02.956101
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    cases = [
        TestCase(name='test_case', time=1.0),
        TestCase(name='test_case2', time=2.0, skipped='Skipped reason', is_disabled=True),
    ]
    test_suite = TestSuite(name='test_suite', cases=cases)

# Generated at 2022-06-13 15:47:12.548019
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name='name', hostname='hostname',
                          package='package',
                          disabled = 0,
                          errors = 0,
                          failures = 0,
                          skipped = 0,
                          tests = 0,
                          time = 0,
                          timestamp = datetime.datetime.now()
                          )
    expected = '<?xml version="1.0" ?><testsuite id="name" tests="0" errors="0" disabled="0" skipped="0" failures="0" hostname="hostname" name="name" package="package" time="0.0"><properties></properties></testsuite>'
    assert ET.tostring(testsuite.get_xml_element(), encoding="unicode") == expected



# Generated at 2022-06-13 15:47:14.983602
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Scenario 1: TestCase with no Result
    # nothing to test
    # Scenario 2: TestCase with 1 or more TestResult
    # nothing to test
    pass

# Generated at 2022-06-13 15:47:25.316026
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name='case_1')
    test_cases = [test_case]
    test_suite = TestSuite(name='suite_1', cases=test_cases)
    test_suites = TestSuites(name='suites_1', suites=[test_suite])

# Generated at 2022-06-13 15:47:30.304714
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name='test_name')
    test_cases = [test_case]
    test_suite = TestSuite(
        name='test_suite',
        hostname='test_hostname',
        id='test_id',
        package='test_package',
        timestamp='test_timestamp',
        cases=test_cases,
        system_out='test_system_out',
        system_err='test_system_err'
    )
    element = test_suite.get_xml_element()
    xml = ET.tostring(element, encoding='unicode')

# Generated at 2022-06-13 15:47:41.275253
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite=TestSuite('suite_name','host_name','id','package','timestamp','system_out','system_err')
    test_case=TestCase('case_name','assertions','classname','status','time','output','message','type')
    test_case.errors.append(TestError())
    test_case.failures.append(TestFailure())
    test_suite.cases.append(test_case)
    assert test_suite.get_xml_element().attrib["name"]=='suite_name'
    assert test_case.get_xml_element().attrib["name"]=='case_name'
    assert len(test_case.get_xml_element())==2
    assert len(test_case.get_xml_element().findall('.//error'))==1
   

# Generated at 2022-06-13 15:48:06.108287
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Example from https://junit.org/junit5/docs/current/user-guide/#running-tests-build-xml-reports
    tc0 = TestCase(name='testAdd', time=decimal.Decimal('0.01'), classname='MathUtilsTest')
    tc1 = TestCase(name='testDivide',
                   time=decimal.Decimal('0.02'),
                   classname='MathUtilsTest')
    ts = TestSuite(name='MathUtilsTest', cases=[tc0, tc1], timestamp=datetime.datetime.strptime("2019-09-01T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))

# Generated at 2022-06-13 15:48:17.282620
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # 1. Arrange
    suite = TestSuite('testsuite1', '127.0.0.1', 'id1', 'com.example', datetime.datetime.now(), [TestCase('testcase1')], 'sysout', 'syserr')
    # 2. Act
    result = suite.get_xml_element()
    # 3. Assert
    assert result.tag == 'testsuite'
    assert len(result.attrib) == 8
    assert result[0].tag == 'testcase'
    assert result[0].attrib.get('name') == 'testcase1'
    assert result[1].tag == 'system-out'
    assert result[1].text == 'sysout'
    assert result[2].tag == 'system-err'
    assert result[2].text == 'syserr'

# Generated at 2022-06-13 15:48:27.308517
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    """
    Hier ist ein
    ausführlicher
    Kommentar
    """
    test = TestCase(name="test_TestCase_get_xml_element()")
    test.time = 0.05
    test.assertions = 0
    test.status = "OK"
    test.system_out = "Hier ist ein\nausführlicher\nKommentar"
    test.classname = "def test_TestCase_get_xml_element():"
    test.is_disabled = False
    xml_element = test.get_xml_element()