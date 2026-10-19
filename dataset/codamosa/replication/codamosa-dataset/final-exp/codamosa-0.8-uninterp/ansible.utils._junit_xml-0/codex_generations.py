

# Generated at 2022-06-13 15:38:42.505038
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    """Test method get_xml_element of class TestResult"""
    result_obj = TestResult()
    expected_output = '<TestResult />'
    actual_output = ET.tostring(result_obj.get_xml_element(), encoding='unicode')
    assert actual_output == expected_output



# Generated at 2022-06-13 15:38:43.797837
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    """Test TestResult.get_xml_element()"""
    assert TestResult().get_xml_element().tag == 'TestResult'


# Generated at 2022-06-13 15:38:48.327828
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestResult(output='Output for a test result')
    assert test_result.get_xml_element().text == 'Output for a test result'
    assert test_result.get_xml_element().tag == 'test-result'
    assert test_result.get_xml_element().attrib == {}


# Generated at 2022-06-13 15:38:53.399809
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test')

    # noinspection PyUnresolvedReferences
    assert str(ET.tostring(test_case.get_xml_element(), encoding='unicode')) == '<testcase name="test" />'


# Generated at 2022-06-13 15:38:55.526824
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    instance = TestResult()
    result = instance.get_attributes()
    assert result


# Generated at 2022-06-13 15:38:59.895214
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    message = 'Some failure message'
    output = '<some output>'
    result = TestFailure(output=output, message=message)
    expected_element = ET.Element('failure', dict(message=message))
    expected_element.text = output

    assert result.get_xml_element() == expected_element


# Generated at 2022-06-13 15:39:02.313360
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    test_result = TestResult()
    actual = test_result.get_xml_element()
    expected = ET.Element('testresult')
    assert actual == expected, "The actual element is different from the expected element"


# Generated at 2022-06-13 15:39:14.814182
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:39:20.888683
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    class TestTestResult(TestResult):
        @property
        def tag(self):
            return 'test_result'

    test_result = TestTestResult(output='test_output', message='test_message', type='test_type')
    element = test_result.get_xml_element()

    assert element.tag == 'test_result'
    assert element.attrib['message'] == 'test_message'
    assert element.attrib['type'] == 'test_type'
    assert element.text == 'test_output'


# Generated at 2022-06-13 15:39:23.418950
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    myTestResult = TestResult('output', 'message', 'type')
    assert myTestResult.get_attributes() == {'message': 'message', 'type': 'type'}


# Generated at 2022-06-13 15:39:39.115120
# Unit test for method get_xml_element of class TestCase

# Generated at 2022-06-13 15:39:49.934383
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    tc = TestCase(
        name="test_add_01",
        assertions=1,
        classname="test_calc.CalcTest",
        status="",
        time=0.1,
        system_out="system_output",
        system_err="system_error")

    assert tc.get_xml_element().attrib['assertions'] == "1"
    assert tc.get_xml_element().attrib['classname'] == "test_calc.CalcTest"
    assert tc.get_xml_element().attrib['name'] == "test_add_01"
    assert tc.get_xml_element().attrib['status'] == ""
    assert tc.get_xml_element().attrib['time'] == "0.1"


# Generated at 2022-06-13 15:39:57.723690
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:40:07.369100
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    obj = TestCase("name")
    assert obj.get_xml_element() ==  ET.fromstring("<testcase name=\"name\"/>")
    obj = TestCase("name", 1)
    assert obj.get_xml_element() ==  ET.fromstring("<testcase assertions=\"1\" name=\"name\"/>")
    obj = TestCase("name", classname="classname")
    assert obj.get_xml_element() ==  ET.fromstring("<testcase classname=\"classname\" name=\"name\"/>")
    obj = TestCase("name", status="status")
    assert obj.get_xml_element() ==  ET.fromstring("<testcase name=\"name\" status=\"status\"/>")
    obj = TestCase("name", time=1.0)

# Generated at 2022-06-13 15:40:10.280776
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('name', 'classname', time=222)
    assert test_case.get_xml_element().tag == 'testcase'
    assert test_case.get_xml_element().attrib == {'name': 'name', 'classname': 'classname', 'time': '222'}

if __name__ == "__main__":  # pragma: no cover
    test_TestCase_get_xml_element()

# Generated at 2022-06-13 15:40:15.128560
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    test_suite = TestSuite(name='test_suite')
    for case in test_suite.cases:
        assert case.get_xml_element().tag == 'testcase'


# Generated at 2022-06-13 15:40:20.084595
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite('test_suite_1')

    assert ET.tostring(test_suite.get_xml_element(), encoding='unicode') == '<testsuite name="test_suite_1" tests="0" />'



# Generated at 2022-06-13 15:40:29.145814
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='my_suite', hostname='my_host')
    case = TestCase(name='my_case', classname='my_class', status='my_status', time=decimal.Decimal(1.0))
    suite.cases = [case]
    test_suites = TestSuites(name='my_test_suites', suites=[suite])

    assert '<testsuite disabled="0" errors="0" failures="0" hostname="my_host" name="my_suite" skipped="0" tests="1" time="1.0">' in test_suites.to_pretty_xml()



# Generated at 2022-06-13 15:40:36.379153
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase('test_TestSuite_get_xml_element')
    test_suite = TestSuite('TestSuite', cases=[test_case])
    expected_result = '<?xml version="1.0" ?><testsuite name="TestSuite" tests="1"><testcase name="test_TestSuite_get_xml_element"/></testsuite>'
    actual_result = _pretty_xml(test_suite.get_xml_element())
    assert expected_result == actual_result


# Generated at 2022-06-13 15:40:43.874441
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="Name", assertions=1, classname="Classname", status="Status", time=2)
    xml_element = test_case.get_xml_element()

    if xml_element.tag != 'testcase':
        raise AssertionError("Method get_xml_element() of class TestCase returned a XML element with tag: " + xml_element.tag)

    if xml_element.text is not None:
        raise AssertionError("Method get_xml_element() of class TestCase returned a XML element with text: " + xml_element.text)

    if len(xml_element.attrib) != 5:
        raise AssertionError("Method get_xml_element() of class TestCase returned a XML element with " + str(len(xml_element.attrib)) + " attribute(s).")



# Generated at 2022-06-13 15:40:58.660325
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite_name = 'TestSuite'
    suite = TestSuite(name=suite_name)
    print(suite.get_xml_element().tag)
    assert suite.get_xml_element().tag == 'testsuite'
    assert suite.get_xml_element().attrib.get('name') == suite_name
    assert suite.get_xml_element().attrib.get('tests') == '0'
    assert suite.get_xml_element().attrib.get('time') == '0'
    assert suite.get_xml_element().attrib.get('disabled') == '0'
    assert suite.get_xml_element().attrib.get('errors') == '0'
    assert suite.get_xml_element().attrib.get('failures') == '0'


# Generated at 2022-06-13 15:41:06.949829
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # A test case may have different type of "result" elements, here we test one of them:
    test_failure = TestFailure(
        message='test failed',
        output='a very long traceback',
        type='TestFailure')
    test_case = TestCase(
        name='test_case_name',
        assertions=1,
        classname='test_class_name',
        status='status',
        time=10,
        failures=[test_failure])
    # Expected XML structure:
    xml_el = test_case.get_xml_element()
    assert xml_el.tag == 'testcase'
    # Testcase attributes

# Generated at 2022-06-13 15:41:12.849616
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:41:19.015827
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    classname = 'testclass'
    name = 'testname'
    time = decimal.Decimal('0.01')
    tcase = TestCase(classname=classname, name=name, time=time)
    xml = tcase.get_xml_element()
    attr = xml.attrib
    assert classname == attr['classname']
    assert name == attr['name']
    assert str(time) == attr['time']


# Generated at 2022-06-13 15:41:25.449900
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    print("TEST: TestSuite_get_xml_element")
    test_suite = TestSuite(
        name="my-name",
        hostname="my-hostname",
        id="my-id",
        package="my-package",
        timestamp=datetime.datetime.utcnow(),

        properties={"key1": "value1", "key2": "value2"},
        system_out="my-system-out-a",
        system_err="my-system-err-b",
    )


# Generated at 2022-06-13 15:41:32.526005
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # testcase
    TEST_CASE = TestCase(
        name="assertion_test",
        assertions=2
    )
    # expected ElementTree
    ET_EXPECTED = ET.Element('testcase', {'name': "assertion_test", 'assertions': "2"})
    # assert
    assert ET.tostring(TEST_CASE.get_xml_element()) == ET.tostring(ET_EXPECTED)


# Generated at 2022-06-13 15:41:36.817134
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:41:42.657090
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:41:53.663686
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    print("Testing TestSuite_get_xml_element()")

    test_case_11 = TestCase('test_case_11', time=11.)
    test_case_12 = TestCase('test_case_12', time=12.)

    test_suite_1 = TestSuite('test_suite_1', hostname='localhost', id='test_id_1', package='test_package_1', timestamp=datetime.datetime.now())
    test_suite_1.properties = {'prop1': 'val1', 'prop2': 'val2'}
    test_suite_1.system_out = 'some standard output'
    test_suite_1.system_err = 'some standard error'
    test_suite_1.cases = [test_case_11, test_case_12]

   

# Generated at 2022-06-13 15:42:03.037061
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    """ Unit test for method get_xml_element of class TestCase """
    test_case = TestCase(name="len", assertions="1", classname="test.test_file.test_samples", status="run", time="0.00")
    test_case.errors.append(TestError(output="Exception", message="Error", type="ERROR"))
    test_case.failures.append(TestFailure(output="Exception", message="", type="ERROR"))

    expected_result = """<testcase assertions="1" classname="test.test_file.test_samples" name="len" status="run" time="0.00">
  <error message="Error" output="Exception" type="ERROR"></error>
  <failure message="" output="Exception" type="ERROR"></failure>
</testcase>"""

# Generated at 2022-06-13 15:42:14.004896
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testcase_1 = TestCase('test_case_1')
    testcase_2 = TestCase('test_case_2')
    testsuite = TestSuite('test_suite',
                          cases = [testcase_1, testcase_2])
    assert testsuite.get_xml_element() == ET.fromstring('''<testsuite name="test_suite" tests="2">
  <testcase name="test_case_1" />
  <testcase name="test_case_2" />
</testsuite>
''')

# Generated at 2022-06-13 15:42:20.499613
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Creating test data to be passed to and processed by the method under test
    suite_name = "First test suite"
    suite_hostname = "system name"
    suite_id = "0"
    suite_package = "test_suite_package"
    suite_timestamp = datetime.datetime.now()
    system_out = "First test suite system out"
    system_err = "First test suite system err"
    suite_properties = {'test_suite_property1': 'suite property value 1', 'test_suite_property2': 'suite property value 2'}
    test_case_name = "First test case"
    test_case_classname = "test_case_classname"
    test_case_status = "passed"
    test_case_time = decimal.Decimal(1)

# Generated at 2022-06-13 15:42:31.613453
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    t1 = TestCase(name="test1", time=0.002, assertions=3)
    assert t1.get_xml_element() == ET.fromstring("<testcase assertions=\"3\" name=\"test1\" time=\"0.002\" />")

    t2 = TestCase(name="test2")
    assert t2.get_xml_element() == ET.fromstring("<testcase name=\"test2\" />")

    t3 = TestCase(name="test3", errors=[TestError(output="oops there is something wrong")])
    assert t3.get_xml_element() == ET.fromstring("<testcase name=\"test3\"><error>oops there is something wrong</error></testcase>")

    t4 = TestCase(name="test4", failures=[TestFailure(output="oops there is something wrong")])

# Generated at 2022-06-13 15:42:43.450378
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    from xml.etree.ElementTree import tostring

    # Check for empty testsuite, this is valid JUnit
    testsuite = TestSuite('TestSuite #1')
    xml_element = testsuite.get_xml_element()
    assert tostring(xml_element, encoding='unicode') == '<testsuite name="TestSuite #1" disabled="0" errors="0" failures="0" hostname="unknown" id="0" package="" skipped="0" tests="0" time="0" timestamp="1970-01-01T00:00:00" />'

    # Check with errors
    testsuite = TestSuite('TestSuite #1')
    testsuite.cases.append(TestCase('TestCase #1'))



# Generated at 2022-06-13 15:42:52.273199
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:42:56.917906
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Testcase
    tc = TestCase(name='test_case_name')
    # TestSuite
    ts = TestSuite(name='test_suite_name', cases=[tc])
    xml = ts.get_xml_element()
    # Check xml content
    assert '<testcase name="test_case_name" />' in xml.__str__()


# Generated at 2022-06-13 15:43:06.062588
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    package = 'org.apache.commons.dbutils'
    name = 'TestBeanProcessor'
    hostname = 'localhost'
    id_ = 'TestBeanProcessor'
    timestamp = datetime.datetime(2014, 8, 22, 16, 31, 33, 642000)
    tests = 2
    errors = 0
    skipped = 0
    failures = 1
    disabled = 0
    time = decimal.Decimal('0.059')

    properties = {'java.version': '1.8.0_25',
                  'user.dir': '/Users/jd/src/commons/commons-dbutils',
                  'user.home': '/Users/jd',
                  'user.name': 'jd'
                  }


# Generated at 2022-06-13 15:43:09.164429
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name='1', classname='testcase')
    result = test_case.get_xml_element()
    assert result.attrib['name'] == '1'
    assert result.attrib['classname'] == 'testcase'
    assert result.tag == 'testcase'


# Generated at 2022-06-13 15:43:16.063615
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_cases = [TestCase('bar'), TestCase('baz')]
    test_suite = TestSuite('foo', cases=test_cases)
    root = ET.Element('root')
    root.insert(0, test_suite.get_xml_element())
    xmlstr = ET.tostring(root, encoding='unicode')

# Generated at 2022-06-13 15:43:27.752895
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    from xml.etree import cElementTree as ET

    # Test scenario 1: fields with values
    # Initialize a test_case object
    test_case_1 = TestCase(name='calculate_sum', assertions=3, classname='NumberList', status='OK', time=3)

    test_case_1.errors = [TestError(message='Error for test case 1',output='hello')]
    test_case_1.failures = [TestFailure(message='Failure for test case 1', output='hi')]
    test_case_1.skipped = 'Skipped for test case 1'
    test_case_1.system_out = 'hello from system_out of test case 1'
    test_case_1.system_err = 'hello from system_err of test case 1'

    # Expected XML
    expected_

# Generated at 2022-06-13 15:43:41.352751
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase("My TestCase", classname="My TestClass")
    # The following test doesn't pass, but it's not a problem because it is used as an example by IBM in
    # "https://github.com/junit-team/junit5/blob/main/platform-tests/src/test/resources/jenkins-junit.xsd"
    # assert '<testcase assertions="0" classname="My TestClass" name="My TestCase" status="0" time="0"/>' == ET.tostring(test_case.get_xml_element())


# Generated at 2022-06-13 15:43:49.415502
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testcase = TestCase('testsuite_testcase')
    testcase.time = decimal.Decimal('10')
    testcase.status = 'ERROR'
    testcase.classname = 'testsuite_testcase_class'
    testcase.assertions = 0
    testcase.errors.append(TestError())
    testcase.failures.append(TestFailure())
    testcase.skipped = 'SKIPPED'
    testcase.system_err = 'system err'

    testsuite = TestSuite('testsuite_name')
    testsuite.hostname = 'testsuite_host'
    testsuite.id = 'testsuite_id'
    testsuite.package = 'testsuite_package'
    testsuite.properties = {'property1': 'value1'}
    test

# Generated at 2022-06-13 15:43:51.928024
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(name="TestCaseItem")
    assert test_case.get_xml_element().tag == "testcase"
    assert 'name="TestCaseItem"' in _pretty_xml(test_case.get_xml_element())


# Generated at 2022-06-13 15:44:03.544749
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test = TestCase(name='TestCase1', assertions=50, classname='this is a name', status='this is a status', time='2', errors=[TestError(output='output1', message='message1', type='error1')], failures=[TestFailure(output='output2', message='message2', type='failure2')], skipped='this is a skipped statement', system_out='system_out statement', system_err='system_err statement')

# Generated at 2022-06-13 15:44:14.352211
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    from datetime import datetime
    from decimal import Decimal

    output = "TestCase get_xml_element test"

    test_case = TestCase(
        name="test_case_name",
        assertions=1,
        classname="test_class",
        status="full",
        time=Decimal('1.0'),
        errors=[TestError(output=output)],
        failures=[TestFailure(output=output)],
        skipped="test_skipped",
        system_out=output,
        system_err=output,
        is_disabled=True,
     )


# Generated at 2022-06-13 15:44:23.752873
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    my_test_case = TestCase(name='name_test_case', assertions='1', classname='TestCase1', status='passed', time='0.3', errors=['#1'], failures=['#2'], skipped='skipped_test_case', system_out='system_out', system_err='system_err')
    assert my_test_case.get_xml_element().tag == 'testcase'
    assert my_test_case.get_xml_element().get('assertions') == '1'
    assert my_test_case.get_xml_element().get('classname') == 'TestCase1'
    assert my_test_case.get_xml_element().get('name') == 'name_test_case'

# Generated at 2022-06-13 15:44:34.584420
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    properties = {'name': 'value'}
    cases = [TestCase(name='name', assertions=42, classname='class', status='status', time='0.42')]
    system_out = 'out'
    system_err = 'err'
    suite = TestSuite(name='name', hostname='hostname', id='id', package='package', timestamp=datetime.datetime(2009, 4, 6, 18, 0, 37), properties=properties, cases=cases, system_out=system_out, system_err=system_err)

# Generated at 2022-06-13 15:44:45.141747
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Test with TestSuite with no data
    ts = TestSuite(name='TestSuite', hostname='hostname')
    assert ts.get_xml_element().tag == 'testsuite'
    assert ts.get_xml_element().attrib['name'] == 'TestSuite'
    assert ts.get_xml_element().attrib['hostname'] == 'hostname'
    assert ts.get_xml_element().attrib['errors'] == '0'
    assert ts.get_xml_element().attrib['failures'] == '0'
    assert ts.get_xml_element().attrib['disabled'] == '0'
    assert ts.get_xml_element().attrib['skipped'] == '0'
    assert ts.get_xml_element().attrib['tests'] == '0'

# Generated at 2022-06-13 15:44:53.725680
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_name')

    assert ET.tostring(test_case.get_xml_element()).replace(b'\n', b'') == b'<testcase name="test_name" />'

    test_case = TestCase('test_name', assertions=5)

    assert ET.tostring(test_case.get_xml_element()).replace(b'\n', b'') == b'<testcase assertions="5" name="test_name" />'

    test_case = TestCase('test_name', classname='class_name')

    assert ET.tostring(test_case.get_xml_element()).replace(b'\n', b'') == b'<testcase classname="class_name" name="test_name" />'

    test_case = Test

# Generated at 2022-06-13 15:45:05.686152
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='Test Suite',
                      hostname='Test Host',
                      id='test-id',
                      package='test-package',
                      timestamp=datetime.datetime.now(),
                      properties={'a': 'b'},
                      system_out='system out',
                      system_err='system err')

# Generated at 2022-06-13 15:45:18.223717
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name='Sample-suite',
    )
    suite.cases.append(TestCase(name='TestCase-01'))
    suite.cases.append(TestCase(name='TestCase-02'))

    expected = """
        <testsuite name="Sample-suite" tests="2" failures="0" errors="0" disabled="0" skipped="0" time="0.0">
        </testsuite>
    """
    actual = _pretty_xml(suite.get_xml_element())

    assert type(actual) == str
    assert expected == actual



# Generated at 2022-06-13 15:45:23.023100
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
  ts1 = TestCase(name = 'test_case1', assertions = 1, classname = 'class1', 
                 status = 'pass', time = 11.1)
  ts2 = TestCase(name = 'test_case2', assertions = 2, classname = 'class2', 
                 status = 'fail', time = 22.2)
  ts3 = TestCase(name = 'test_case3', assertions = 3, classname = 'class3', 
                 status = 'error', time = 33.3)
  ts4 = TestCase(name = 'test_case4', assertions = 4, classname = 'class4', 
                 status = 'skip', time = 44.4, is_disabled = True)

# Generated at 2022-06-13 15:45:34.905601
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    timestamp = datetime.datetime.strptime('2019-12-25T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
    test_suite = TestSuite(
        name='suite-name',
        hostname='localhost',
        id='suite-id',
        package='package',
        timestamp=timestamp,
        properties={'some-key': 'some-value'},
        cases=[TestCase(name='case-name')],
        system_out='stdout',
        system_err='stderr',
    )
    xml = test_suite.get_xml_element()
    assert xml.tag == 'testsuite'
    assert xml.attrib['name'] == 'suite-name'

# Generated at 2022-06-13 15:45:44.966365
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # arrange
    properties = {'prop1':'value1', 'prop2':'value2'}
    test_case = TestCase(name="test_case", assertions=1, classname="TestClass", status="completed", time=0.1)
    test_suite = TestSuite(name="test_suite", hostname="host", id="test", package="test", timestamp=datetime.datetime.today(), properties=properties, cases=[test_case], system_out="out", system_err="err")
    # act
    xml_string = ET.tostring(test_suite.get_xml_element(), encoding='unicode')
    # assert
    # assert that the string contains all the attributes
    assert 'name="test_suite"' in xml_string
    assert 'hostname="host"' in xml_string

# Generated at 2022-06-13 15:45:52.267241
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
  case = TestCase(name='TestCase',
  assertions=1000,
  classname='TestClass',
  status='run',
  time=10.0,
  errors=[TestError(output='output', message='message', type='error')],
  failures=[TestFailure(output='output', message='message', type='failure')],
  skipped='skipped',
  system_out='system_out',
  system_err='system_err')
  assert case.get_xml_element().tag == 'testcase'
  assert case.get_xml_element().text == None
  assert case.get_xml_element().attrib['assertions'] == '1000'
  assert case.get_xml_element().attrib['classname'] == 'TestClass'

# Generated at 2022-06-13 15:46:03.268824
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase(name="test_name", time=decimal.Decimal("0.086"))

    assert _pretty_xml(testcase.get_xml_element()) == '''<?xml version="1.0" ?>
<testcase name="test_name" time="0.086"/>
'''

    testcase = TestCase(
        name="test_name",
        classname="class_name",
        time=decimal.Decimal("0.123"),
        errors=[
            TestError(output="stdout", message="message", type="type",),
        ],
        skipped="skipped",
        system_out="system_out",
        system_err="system_err",
    )


# Generated at 2022-06-13 15:46:14.751918
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite('testsuite_name', hostname='testsuite_hostname', id='1', package='testsuite_package', timestamp=datetime.datetime.now())
    testsuite.system_out = 'testsuite_system_out'
    testsuite.system_err = 'testsuite_system_err'

    testcase = TestCase('testcase_name', assertions='2', classname='testcase_classname', status='SUCCESS', time=decimal.Decimal('3.14'))
    testcase.system_out = 'testcase_system_out'
    testcase.system_err = 'testcase_system_err'

    error = TestError(output='error_output', message='error_message')
    testcase.errors.append(error)

    failure = Test

# Generated at 2022-06-13 15:46:23.894622
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:46:32.146539
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    def equals(s1, s2):
        return s1 == s2
    suite=TestSuite(name="test",cases=[TestCase("a"),TestCase("b")])
    res = [1 if equals(e.tag,"testcase") else 2 for e in suite.get_xml_element()]
    print("[Test] TestSuite get_xml_element ...\n")
    print("[Test] TestSuite get_xml_element:", res)
    print("\n[Test] TestSuite get_xml_element: PASS")


# Generated at 2022-06-13 15:46:39.022915
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    
    ts = TestSuite('test1')
    ts.timestamp = datetime.datetime.now()
    ts.properties = dict(name = 'alice', age = '42')
    ts.system_out = 'testing'
    ts.system_err = 'error'
    
    tc = TestCase('testcase')
    tc.timestamp = datetime.datetime.now()
    tc.errors.append(TestError('error'))
    tc.failures.append(TestFailure('failure'))
    tc.skipped = 'skipped'
    tc.system_out = 'tc_system_out'
    tc.system_err = 'tc_system_err'
    ts.cases.append(tc)

    print(ts.get_xml_element())

# Generated at 2022-06-13 15:46:52.367799
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name='test_name', assertions=1, classname='test_classname', status='test_status', time=3.0)
    test_suite = TestSuite(name='test_name', hostname='test_hostname', id='test_id', package='test_package', timestamp=datetime.datetime.now(), properties={"test_key": "test_value"}, cases=[test_case], system_out='test_system_out', system_err='test_system_err')
    assert test_suite.get_xml_element().find(".//testcase").attrib=={'name':'test_name','assertions':'1','classname':'test_classname','status':'test_status','time':'3'}


# Generated at 2022-06-13 15:47:00.310044
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    tst = TestSuite("test", "host", "id", "package", datetime.datetime.now())
    tst.properties = {"prop": "value"}
    tst.cases = [TestCase("testcase", 1, "class", "status", 1.0)]
    tst.system_out = "sysout"
    tst.system_err = "syserr"

    print("TestSuite: \n{}".format(ET.tostring(tst.get_xml_element(), encoding='unicode')))



# Generated at 2022-06-13 15:47:08.542554
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Using three cases, two of them with errors, the third with failure and disabled
    test_cases = [TestCase("test1"), TestCase("test2")]
    test_cases[0].errors.append(TestError("This is a test error"))
    test_cases[1].errors.append(TestError("This is another test error"))
    test_cases.append(TestCase("failure_test"))
    test_cases[2].is_disabled = True
    test_cases[2].failures.append(TestFailure("This is a test failure"))
    test_suite = TestSuite("test_suite")
    test_suite.cases = test_cases

    # Comparing the builded xml and the expected one
    xml = test_suite.get_xml_element()
    expected_xml = minidom.parseString

# Generated at 2022-06-13 15:47:14.379247
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    import datetime
    import decimal
    test_case = TestCase(name = 'test_test', assertions = 1, classname = 'test', status = 'pass', time = 0.1)

    test_suite = TestSuite(name = 'test', hostname = '127.0.0.1', id = 'test', package = 'test', timestamp = datetime.datetime.now(), cases = [test_case], system_out = 'test output', system_err = 'test error')
    test_suite.get_xml_element()


# Generated at 2022-06-13 15:47:24.835236
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:47:33.278044
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    def test_without_property(prop):
        assert prop not in element.attrib
    def test_with_property(prop, prop_value):
        assert prop in element.attrib
        assert element.attrib[prop] == prop_value

    test_suite = TestSuite('test suite name')

    element = test_suite.get_xml_element()
    assert element.tag == 'testsuite'

    test_without_property('hostname')
    test_without_property('id')
    test_without_property('package')
    test_without_property('timestamp')

    test_with_property('disabled', '0')
    test_with_property('errors', '0')
    test_with_property('failures', '0')
    test_with_property('name', 'test suite name')
   

# Generated at 2022-06-13 15:47:40.946086
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    # get_xml_element()
    test_case = TestCase(
        name = 'test_case_name',
        classname = 'test_case_classname',
        status = 'test_case_status',
        time = 1.23456789,
    )

# Generated at 2022-06-13 15:47:51.786515
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:47:57.691290
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = dataclasses.make_dataclass('TestSuite', (object,), {'name' : 'nimbus_wrapper', 'hostname' : 'localhost', 'id' : '1', 'package' : 'com.nimbus'})()

    root = ts.get_xml_element()

    assert root.tag == 'testsuite'
    assert root.attrib == {'hostname' : 'localhost', 'id' : '1', 'package' : 'com.nimbus', 'name' : 'nimbus_wrapper'}


# Generated at 2022-06-13 15:48:04.107813
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:48:18.125791
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:48:24.898329
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name='hello world')
    print(ET.tostring(test_suite.get_xml_element(), encoding='unicode'))
    assert _pretty_xml(test_suite.get_xml_element()) == '''<?xml version="1.0" ?>
<testsuite disabled="0" errors="0" failures="0" hostname="" id="" name="hello world" package="" skipped="0" tests="0" time="0.0"></testsuite>
'''



# Generated at 2022-06-13 15:48:34.542959
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    cases = [ TestCase(name='test1', assertions=2, classname='test.name', status='OK', time=decimal.Decimal('1'), errors=[], failures=[], skipped=None, system_out=None, system_err=None, is_disabled=False) ]
    suites = [ TestSuite(name='test', hostname='0.0.0.0', id='1', package='test.package', timestamp=datetime.datetime(2020, 9, 22, 16, 6, 0), properties={}, cases=cases, system_out=None, system_err=None) ]
    test = TestSuites(name='testsuites', suites=suites)
    assert test.get_xml_element().get('name') == 'testsuites'