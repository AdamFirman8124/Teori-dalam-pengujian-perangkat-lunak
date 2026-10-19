

# Generated at 2022-06-13 15:38:41.419975
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    result = TestResult(message='Message', type='Missing', 
                        output='The test failed because the button was missing.')
    expected = dict(message='Message', type='Missing')
    actual = result.get_attributes()
    assert actual == expected


# Generated at 2022-06-13 15:38:46.595470
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    result = TestResult(output="Output", message="Message", type="Type")
    assert result.get_xml_element().text == "Output", "Mauvaise gestion de l'attribut output"
    assert result.get_attributes()["message"] == "Message", "Mauvaise gestion de l'attribut message"


# Generated at 2022-06-13 15:38:47.977655
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    # Arrange
    test_result = TestResult()
    # Act
    test_result.get_xml_element()
    # Assert


# Generated at 2022-06-13 15:38:49.044579
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    pass

# Generated at 2022-06-13 15:38:54.126776
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    result = TestResult(message='test_message', type='test_type', output='test_output')
    attributes = result.get_attributes()
    assert attributes['message'] == 'test_message'
    assert attributes['type'] == 'test_type'


# Generated at 2022-06-13 15:39:02.583065
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    sample_message = 'sample message'
    sample_type = 'type'
    sample_output = 'sample output'
    # sample_tag will be different for each of the result classes.
    sample_tag = ''
    # create an instance of a test result class
    test_result = TestResult(output=sample_output, message=sample_message, type=sample_type)
    # get XML element
    element = test_result.get_xml_element()
    # check name
    assert element.tag == test_result.tag
    # check message attribute
    assert element.attrib['message'] == sample_message
    # check type attribute
    assert element.attrib['type'] == sample_type
    # check content
    assert element.text == sample_output


# Generated at 2022-06-13 15:39:12.796111
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    xml_element = ET.Element(TestResult(type = 'my tag', message = 'my message', output = 'my output').tag, TestResult(type = 'my tag', message = 'my message', output = 'my output').get_attributes())
    xml_element.text = str(TestResult(type = 'my tag', message = 'my message', output = 'my output').output)
    assert(ET.tostring(xml_element, encoding='unicode') == ET.tostring(TestResult(type = 'my tag', message = 'my message', output = 'my output').get_xml_element(), encoding='unicode'))


# Generated at 2022-06-13 15:39:15.151490
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    tr = TestResult()
    attributes = tr.get_attributes()
    assert attributes['type'] == 'TestResult'


# Generated at 2022-06-13 15:39:16.267471
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    test_result = TestResult("output123")
    assert test_result.get_attributes() == {'message': None, 'type': 'testresult'}

# Generated at 2022-06-13 15:39:18.591724
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    # Case: No children
    actual = TestResult(output='foo', message='bar', type='baz')
    expected = """\
<testresult>
  <output>foo</output>
  <message>bar</message>
  <type>baz</type>
</testresult>"""
    assert _pretty_xml(actual.get_xml_element()) == expected



# Generated at 2022-06-13 15:39:32.359415
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    result = TestResult("", 'my_type')
    expected = {
        "type": 'my_type'
    }
    assert(result.get_attributes() == expected)


# Generated at 2022-06-13 15:39:35.234228
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    """Unit test for the method get_xml_element of class TestResult."""
    result = TestError()
    assert result.get_xml_element().tag == 'error'



# Generated at 2022-06-13 15:39:41.326658
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    from dataclasses import dataclass
    suite = TestSuite(name='Test1')
    case = TestCase(name='test1')
    suite.cases.append(case)
    root = ET.Element('testsuites')
    root.append(suite.get_xml_element())
    xmlstr = ET.tostring(root, encoding='unicode')
    assert 'Test1' in xmlstr


# Generated at 2022-06-13 15:39:52.374052
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    time = decimal.Decimal('1.234')
    timestamp = datetime.datetime.now()

    test_case_1 = TestCase(
        name='test_name_1',
        classname='test_class_name_1',
        status='test_status_1',
        time=time,
        errors=[TestError(
            output='test_output_1',
            message='test_message_1',
            type='test_type_1',
        )],
        failures=[TestFailure(
            output='test_output_2',
            message='test_message_2',
            type='test_type_2',
        )],
        skipped=True,
        system_out='test_system_out_1',
        system_err='test_system_err_1',
    )

    test_case_

# Generated at 2022-06-13 15:39:58.346263
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    tr = TestResult()
    x = tr.get_xml_element()
    assert x.tag == 'testresult'
    assert x.attrib == {}
    assert x.text == None

    tr.output = 'output'
    tr.type = 'type'
    tr.message = 'message'
    x = tr.get_xml_element()
    assert x.tag == 'testresult'
    assert x.attrib == {'message': 'message', 'type': 'type'}
    assert x.text == 'output'


# Generated at 2022-06-13 15:40:06.272301
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():

    @dataclasses.dataclass
    class TestFailureSub(TestResult):
        """Failure info for a test case."""

        @property
        def tag(self) -> str:
            """Tag name for the XML element created by this result type."""
            return 'failure'

    f = TestFailureSub(output='f', message='message', type='type')
    assert f.get_xml_element().tag == 'failure'
    assert f.get_xml_element().attrib == {'message': 'message', 'type': 'type'}
    assert f.get_xml_element().text == 'f'



# Generated at 2022-06-13 15:40:11.167279
# Unit test for method get_attributes of class TestResult
def test_TestResult_get_attributes():
    t_result = TestResult()
    assert t_result.get_attributes() == {}
    assert t_result.get_attributes() == _attributes()

    t_result = TestResult(
        message='message',
        type='type',
        output='output'
    )
    assert t_result.get_attributes() == _attributes(
        message='message',
        type='type'
    )



# Generated at 2022-06-13 15:40:15.362621
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    tr = TestResult(output = "test output")
    assert tr.get_xml_element().tag == "TestResult"
    assert tr.get_xml_element().text == "test output"


# Generated at 2022-06-13 15:40:22.032842
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    
    path = './TestSuite.xml'
    file = open(path,"r")
    content = file.read()
    file.close()
    testsuite = TestSuite(name = 'testname', hostname = 'myhostname', id = 'myid', package = 'mypackage', timestamp = datetime.datetime.now())

    assert content == _pretty_xml(testsuite.get_xml_element())


# Generated at 2022-06-13 15:40:26.610575
# Unit test for method get_xml_element of class TestResult
def test_TestResult_get_xml_element():
    @dataclasses.dataclass
    class CustomTestResult(TestResult):
        """A custom test status for testing."""
        @property
        def tag(self) -> str:
            """Tag name for the XML element created by this result type."""
            return 'custom'

    custom = CustomTestResult(output='text', message='message', type='type')
    element = custom.get_xml_element()
    assert element.tag == 'custom'
    assert element.attrib['message'] == 'message'
    assert element.attrib['type'] == 'type'
    assert element.text == 'text'

    custom = CustomTestResult(output='text', type='type')
    element = custom.get_xml_element()
    assert element.tag == 'custom'
    assert 'message' not in element.attrib

# Generated at 2022-06-13 15:40:44.274765
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase(
        assertions=42,
        classname='class_name',
        name='name',
        status='PASSED',
        time=1.23,
        errors=[TestError(message='Error message', output='Error output', type='Error type')],
        failures=[TestFailure(message='Failure message', output='Failure output', type='Failure type')],
        skipped='Skipped reason',
        system_out='System out',
        system_err='System err',
    )
    root = test_case.get_xml_element()
    assert root.tag == 'testcase'
    assert root.attrib['assertions'] == '42'
    assert root.attrib['classname'] == 'class_name'
    assert root.attrib['name'] == 'name'

# Generated at 2022-06-13 15:40:50.107301
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    """Unit test for method get_xml_element of class TestCase"""
    time = decimal.Decimal('0.001')
    myElement = TestCase('test_name', assertions=10, classname='test_class_name', status='status', time=time).get_xml_element()
    assert myElement.tag == 'testcase'
    assert myElement.attrib.get('classname') == 'test_class_name'
    assert myElement.attrib.get('name') == 'test_name'
    assert myElement.attrib.get('status') == 'status'
    assert myElement.attrib.get('time') == str(time)
    assert myElement.attrib.get('assertions') == str(10)


# Generated at 2022-06-13 15:40:58.290235
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_cases = TestCase(name="test_test_test", assertions=1, classname="class_class_class", status="status", time=1.1,
                          output="output")
    assert test_cases.get_attributes() == {'assertions': '1', 'classname': 'class_class_class', 'name': 'test_test_test',
                                           'status': 'status', 'time': '1.1'}

    assert test_cases.get_xml_element().attrib == {'assertions': '1', 'classname': 'class_class_class', 'name': 'test_test_test',
                                           'status': 'status', 'time': '1.1'}



# Generated at 2022-06-13 15:41:07.574573
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:41:18.262824
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    # Arrange
    # creation d'un objet test
    test = TestCase(name='test_methode', assertions=None, classname='test_name', status='status_test', time=0.01, errors=None, failures=None, skipped=None, system_out='system_out', system_err='system_err', is_disabled=False)

    # Act
    # appel de la méthode
    xml = test.get_xml_element()

    # Assert
    # vérification du contenu du xml
    assert xml.get('name') == 'test_methode'
    assert xml.get('classname') == 'test_name'
    assert xml.get('status') == 'status_test'
    assert xml.get('time') == '0.01'
    assert xml.get

# Generated at 2022-06-13 15:41:24.997848
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test = TestCase("Empty TestCase")
    xml = test.get_xml_element()
    assert xml.tag == "testcase"
    assert xml.attrib["name"] == "Empty TestCase"
    assert len(xml) == 0
    assert xml.text == None

    test.assertions = 100
    test.classname = "Calculator"
    test.status = "pass"
    test.time = 1.5
    test.skipped = "Not implemented"
    test.system_out = "No output"
    test.system_err = "No error"
    test.is_disabled = True

    xml = test.get_xml_element()
    assert xml.tag == "testcase"
    assert xml.attrib["name"] == "Empty TestCase"

# Generated at 2022-06-13 15:41:30.711229
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    tcase = TestCase('test1')
    tsuite = TestSuite('suite1')
    tsuite.cases.append(tcase)
    xml = tsuite.get_xml_element()
    assert xml.tag == 'testsuite'
    assert 'testcase' in list(map(lambda x: x.tag, xml.getchildren()))

# Generated at 2022-06-13 15:41:41.135187
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:41:43.276839
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    test_case = TestCase('test_name')
    xml_element = test_case.get_xml_element()
    assert xml_element.attrib['name'] == "test_name"
    assert xml_element.tag == "testcase"
    assert len(xml_element) == 0


# Generated at 2022-06-13 15:41:53.604649
# Unit test for method get_xml_element of class TestCase
def test_TestCase_get_xml_element():
    testcase = TestCase(name='test_case')

    assert ET.tostring(testcase.get_xml_element(), encoding='unicode') == '<testcase name="test_case" />'

    testcase = TestCase(name='TestCase.test_method', classname='TestCase', assertions=13, errors=1, failures=1, skipped=1, status=1, time=1)

    assert ET.tostring(testcase.get_xml_element(), encoding='unicode') == '<testcase assertions="13" classname="TestCase" name="TestCase.test_method" status="1" time="1"><skipped /><error /><failure /></testcase>'


# Generated at 2022-06-13 15:42:12.115342
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    #Create a test suite with two test cases
    suite = TestSuite(
        name="SleepTest",
        timestamp=datetime.datetime.now(),
        hostname="localhost",
        cases=[
            TestCase(
                name="sleep.test",
                assertions=1,
                status="PASSED",
                time=decimal.Decimal(0.001),
            ),
            TestCase(
                name="sleep.test",
                assertions=1,
                status="PASSED",
                time=decimal.Decimal(0.005),
            )
        ]
    )

    #Create the XML element representing the test suite
    element = suite.get_xml_element()

    #Check the name of the XML element
    assert element.tag == 'testsuite'
    #Check the number of attributes of the XML element
   

# Generated at 2022-06-13 15:42:14.199851
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='login')
    assert '<?xml version=' in suite.get_xml_element().toString()

# Generated at 2022-06-13 15:42:20.665396
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:42:27.923118
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testSuite = TestSuite(name="name",hostname="hostname",package="package",timestamp=datetime.datetime.now())
    testCase = TestCase(name="name", assertions="10")
    testSuite.cases.append(testCase)

    xml_element = testSuite.get_xml_element()
    assert 'testcase' in ET.tostring(xml_element, encoding='unicode').decode('unicode_escape')



# Generated at 2022-06-13 15:42:33.405199
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    tc = TestCase('test_case')
    ts = TestSuite('test_suite', cases=[tc])
    result = ts.get_xml_element()
    # Validate xml element
    assert result.tag == 'testsuite'
    assert result.attrib['name'] == 'test_suite'
    assert len(result.getchildren()) == 1
    assert result.getchildren()[0].attrib['name'] == 'test_case'


# Generated at 2022-06-13 15:42:45.217763
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:42:49.097827
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(
        name="test_suite",
        hostname="testHost"
    )
    assert testsuite.get_xml_element().tag == 'testsuite'
    assert testsuite.get_xml_element().attrib == {'name': 'test_suite', 'hostname': 'testHost'}



# Generated at 2022-06-13 15:42:55.149644
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name="1", hostname="2", id="3", package="4", timestamp=datetime.datetime.now(),
                        properties={"s":"s"}, cases=[TestCase("5")], system_out="6", system_err="7")
    tree = ET.ElementTree(testsuite.get_xml_element())
    tree.write("test_TestSuite_get_xml_element.xml")



# Generated at 2022-06-13 15:43:04.834562
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name='MySuite', timestamp=datetime.datetime(2020,4,26,15,47,56,222485))
    test_case_1 = TestCase(name='CaseName1', classname='ClassCase1', time=decimal.Decimal(10.345))
    test_case_2 = TestCase(name='CaseName2', classname='ClassCase2', time=decimal.Decimal(20.456))
    test_suite.cases.append(test_case_1)
    test_suite.cases.append(test_case_2)
    element = test_suite.get_xml_element()

# Generated at 2022-06-13 15:43:13.599597
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    name = "testsuite1"
    hostname = "localhost"
    id = "1"
    package = "test"
    timestamp = datetime.datetime.now()

    properties = {"name1": "value1"}
    cases = []
    system_out = "aaa"
    system_err = "bbb"

    suite = TestSuite(
        name=name,
        hostname=hostname,
        id=id,
        package=package,
        timestamp=timestamp,
        properties=properties,
        cases=cases,
        system_out=system_out,
        system_err=system_err,
    )

    xml = suite.get_xml_element()

# Generated at 2022-06-13 15:43:25.103273
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    import unittest
    test_case = TestCase('name')
    test_suite = TestSuite('name')
    test_suite.cases.append(test_case)
    test_suites = TestSuites()
    test_suites.suites.append(test_suite)
    assert unittest.TestCase().assertTrue(test_suites.get_xml_element().find('.//testcase[@name="name"]') is not None)

# Generated at 2022-06-13 15:43:32.278096
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Tests to check if the get_xml_element method of the TestSuite is working as expected."""

# Generated at 2022-06-13 15:43:39.235298
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    TestCase = t.List[TestCase]
    # Make a TestSuite with a single TestCase
    test_suite = TestSuite(name='TestCase', cases=[TestCase(name='TestCase', time=0.0)])
    # Make an ElementTree of the TestSuite
    tree = ET.ElementTree(test_suite.get_xml_element())
    # Check that the ElementTree has the correct name
    assert tree.getroot().tag == 'testsuite'

# Generated at 2022-06-13 15:43:51.238988
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:43:58.348457
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # Test case
    test_case_1 = TestCase(name='test_case_1')
    test_case_2 = TestCase(name='test_case_2')

    # Test suite
    test_suite_1 = TestSuite(name='test_suite_1')
    test_suite_1.cases.append(test_case_1)
    test_suite_1.cases.append(test_case_2)
    test_suite_1.system_out = 'Test results for test suite 1'

    # Test suites
    test_suites = TestSuites(name='test_suites_1')
    test_suites.suites.append(test_suite_1)

    # Create XML element
    test_suite_1_xml_element = test_suite_1.get

# Generated at 2022-06-13 15:44:10.582036
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(name = 'TestSuite',hostname = 'hostname', id = 'id', package = 'package', timestamp=datetime.datetime.now(),properties = {'a':'b','c':'d'}
    ,system_out='system out',system_err='system err')
    ts.cases.append(TestCase(name='name',classname='classname',status='status',time=datetime.datetime.now(),skipped='skipped',system_out='system out',system_err='system err'))
    ts.cases[0].errors.append(TestError(output='error out',message = 'message',type='type'))
    ts.cases[0].failures.append(TestFailure(output='failure out',message = 'message',type='type'))


# Generated at 2022-06-13 15:44:17.656642
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='test_suite_name', timestamp=datetime.datetime.now())
    suite.system_err = 'test_suite_system_err'
    suite.system_out = 'test_suite_system_out'
    suite.properties = {
        'test_suite_property_name': 'test_suite_property_value'
    }
    test_case = TestCase(name='test_case_name', classname='test_case_classname', time=0.1, status='test_case_status')
    test_case.system_err = 'test_case_system_err'
    test_case.system_out = 'test_case_system_out'
    test_case.skipped = 'test_case_skipped'

# Generated at 2022-06-13 15:44:25.964144
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name="test_case_name")
    test_suite = TestSuite(name="test_suite_name",
                           hostname="test_host_name",
                           id="test_id",
                           package="test_package",
                           timestamp=datetime.datetime.now())
    test_suite.cases.append(test_case)
    test_suite.properties['test_property'] = 'test'
    test_suite.system_out = "<system-out>test</system-out>"
    test_suite.system_err = "<system-err>test</system-err>"

    xml_string = test_suite.get_xml_element().tostring(encoding='unicode')
    assert "<testsuite" in xml_string

# Generated at 2022-06-13 15:44:38.137712
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts = TestSuite(name='suite-name')
    assert ET.tostring(ts.get_xml_element()) == b"""
    <testsuite disabled="0" errors="0" failures="0" name="suite-name" skipped="0" tests="0" time="0.0" />
    """.strip()

    ts.cases = [
        TestCase(name='case-name-1', time=1.01),
        TestCase(name='case-name-2', time=2.02),
    ]


# Generated at 2022-06-13 15:44:47.854818
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    from datetime import datetime
    from decimal import Decimal


# Generated at 2022-06-13 15:45:06.871135
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    print("Running TestSuite.get_xml_element() test")
    suite = TestSuite('test_suite')
    suite.cases.append(TestCase('test_case1'))
    suite.cases.append(TestCase('test_case2'))

    assert suite.tests == 2
    assert suite.time is None
    assert suite.errors == 0
    assert suite.failures == 0
    assert suite.skipped == 0
    assert suite.disabled == 0

    element = suite.get_xml_element()
    assert element.tag == 'testsuite'
    assert element.attrib['name'] == 'test_suite'
    assert element.attrib['tests'] == '2'


# Generated at 2022-06-13 15:45:12.604286
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    print("\n<----- start unit test for get_xml_element of class TestSuite ----->")
    test_suite = TestSuite(name='another_one', hostname='host_name')
    test_suite.properties['key1'] = 'value1'
    test_case1 = TestCase(name='A_name')
    test_case2 = TestCase(name='case2_id')
    test_suite.cases.extend([test_case1, test_case2])
    test_suite.system_out = "system output"

    str = test_suite.to_pretty_xml()
    print(str)


# Generated at 2022-06-13 15:45:19.064833
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    # given
    classname = 'test_classname'
    name = 'test_name'
    time = decimal.Decimal('0.01')
    testcase = TestCase(classname=classname, name=name, time=time)

    name = 'test_name'
    testsuite = TestSuite(name=name)
    testsuite.cases.append(testcase)
    # when
    testsuite_xml_element = testsuite.get_xml_element()
    # then
    xml_root = ET.fromstring(ET.tostring(testsuite_xml_element))
    xml_testcase_element = xml_root.find('testcase')
    xml_testcase_attrib = xml_testcase_element.attrib
    assert xml_testcase_attrib['name'] == name

# Generated at 2022-06-13 15:45:27.799806
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name='MyTestSuite')
    assert _pretty_xml(test_suite.get_xml_element()) == u'<?xml version="1.0" ?>\n<testsuite disabled="0" errors="0" failures="0" hostname="None" id="None" name="MyTestSuite" package="None" skipped="0" tests="0" time="None" timestamp="None"/>\n'


# Generated at 2022-06-13 15:45:37.253247
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Test TestSuite.get_xml_element()"""

# Generated at 2022-06-13 15:45:47.709973
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case_1 = TestCase("Test name 1", status="status 1", time=0.0000001)
    test_case_1.errors = [TestError(output="""This is some
                                              output""")]
    test_case_2 = TestCase("Test name 2", status="status 2", time=0.000001)
    test_case_2.failures = [TestFailure(output="""This is some
                                                  output""")]
    test_case_3 = TestCase("Test name 3", status="status 3", time=0.0000001)
    test_case_3.errors = [TestError(output="""This is some
                                              output""")]

    test_suite = TestSuite("Test suite name", hostname="hostname")

# Generated at 2022-06-13 15:45:55.297219
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(
        name='test-suite',
        hostname='testhost',
        id=1,
        package='test-suite.test',
        timestamp=datetime.datetime(2020, 5, 13, 14, 30, 0, 0),
        cases=[
            TestCase(
                name='test-case',
                assertions=1,
                classname='test-suite.test.TestCase',
                status='success',
                time=1.234,
                system_out='system-out',
                system_err='system-err',
            ),
        ],
        properties={
            'foo': 'bar',
        },
    )

    element = suite.get_xml_element()

    assert element.tag == 'testsuite'

    attributes = element.attrib
    assert 'name'

# Generated at 2022-06-13 15:46:04.524845
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite('suite_name', hostname='hostname', id='id', package='package',
                           timestamp=datetime.datetime(year=2020, month=4, day=22, hour=15, minute=47, second=59))
    test_suite.properties = {'key': 'value'}
    test_suite.cases = [
        TestCase(name='case1'),
        TestCase(name='case2')
    ]
    test_suite.system_out = 'system_out'
    test_suite.system_err = 'system_err'
    element = test_suite.get_xml_element()
    assert element.tag == 'testsuite'

# Generated at 2022-06-13 15:46:09.339368
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='testsuite_name')
    assert suite.get_xml_element().tag == 'testsuite'
    assert len(suite.get_xml_element().attrib) == 1
    assert suite.get_xml_element().attrib['name'] == 'testsuite_name'


# Generated at 2022-06-13 15:46:20.058026
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:46:35.630117
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_cases = []
    test_cases.append(TestCase(name="test_name"))
    test_cases.append(TestCase(
        name="test_name2",
        classname="test_class",
        errors=[TestError(output="error1"), TestError(output="error2")],
        failures=[TestFailure(output="failure1"), TestFailure(output="failure2")]
    ))
    test_suite = TestSuite(
        name="test_suite_name",
        timestamp=datetime.datetime.now(),
        cases=test_cases
    )
    assert test_suite.get_xml_element()



# Generated at 2022-06-13 15:46:41.937102
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite"""
    cases = [TestCase(name="test_xml", time=decimal.Decimal('13.37'))]
    suite = TestSuite(name="test_suite", cases=cases)
    xml_element = suite.get_xml_element()
    assert ET.tostring(xml_element) == b'<testsuite disabled="0" errors="0" failures="0" name="test_suite" skipped="0" tests="1" time="13.37"><testcase assertions="" classname="" name="test_xml" status="" time="13.37"/></testsuite>'

# Generated at 2022-06-13 15:46:51.471200
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    timestamp = datetime.datetime(
        year=2019,
        month=11,
        day=11,
        hour=18,
        minute=28,
        second=18,
    )


# Generated at 2022-06-13 15:46:54.556212
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    testsuite = TestSuite(name="Batch_1")
    assert testsuite
    assert testsuite.get_xml_element()


# Generated at 2022-06-13 15:47:04.513329
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    """Unit test for method get_xml_element of class TestSuite. """
    ts = TestSuite('test suite')
    tc = TestCase('test case', classname='TestCase', time=0)
    err = TestError(message='test error')
    tc.errors.append(err)
    f = TestFailure(message='test failure')
    tc.failures.append(f)
    ts.cases.append(tc)
    ts.timestamp = datetime.datetime.now()
    ts.system_out = 'System Out'
    ts.system_err = 'System Err'
    print(ts.to_pretty_xml())
    ts.properties = {'Test Property': 'Test Value'}
    print(ts.to_pretty_xml())


# Generated at 2022-06-13 15:47:13.309133
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    current_time = datetime.datetime.now()
    ts = TestSuite(name='testsuite1', hostname='localhost', package='com.example', timestamp=current_time)
    ts.cases.append(TestCase(name='testcase1', classname='TestClass1', time=1.2345))
    ts.cases.append(TestCase(name='testcase2', classname='TestClass1', time=1.3456))
    ts.cases.append(TestCase(name='testcase3', classname='TestClass2', time=1.4567))
    ts.cases[2].errors.append(TestError(output='error message', type='error type'))
    ts.cases[2].failures.append(TestFailure(output='failure message', type='failure type'))

# Generated at 2022-06-13 15:47:21.586273
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case1 = TestCase(name='tc1', classname='tc1_class')
    test_case2 = TestCase(name='tc2', classname='tc2_class')
    test_case3 = TestCase(name='tc3', classname='tc3_class')
    test_suite = TestSuite(name='ts1', cases=[test_case1, test_case2, test_case3])
    assert test_suite.get_xml_element().tag == 'testsuite'
    assert test_suite.get_xml_element().attrib['name'] == 'ts1'

# Generated at 2022-06-13 15:47:29.582495
# Unit test for method get_xml_element of class TestSuite

# Generated at 2022-06-13 15:47:40.829998
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    suite = TestSuite(name='Test Suite',
                            hostname='localhost',
                            id='1',
                            package='foo.bar',
                            timestamp=datetime.datetime(year=2020, month=6, day=6, hour=6, minute=6, second=6),
                        )
    # Cannot directly test the xml since the order of the xml attributes is not fixed 
    # (see https://stackoverflow.com/questions/10368801/can-i-control-the-order-of-attributes-in-an-elementtree-xml-element)

    # Check that the xml contains the right tags

# Generated at 2022-06-13 15:47:51.652759
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_suite = TestSuite(name='test_suite_name',
                        hostname='test_suite_hostname',
                        id='test_suite_id',
                        package='test_suite_package',
                        timestamp=datetime.datetime.now(),
                        properties={'key1': 'value1', 'key2': 'value2'},
                        system_out='test_suite_out',
                        system_err='test_suite_err')


# Generated at 2022-06-13 15:48:06.863520
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(
        name='TestName',
        assertions='1',
        classname='TestClass',
        time='1.0',
        status='Fail',
        skipped='Slow_Running',
    )
    test_suite = TestSuite(
        timestamp=datetime.datetime.now(),
        name='TestSuite',
        id='1',
        hostname='127.0.0.1',
        package='net.mytestsite.mytestpackage',
        tests='1',
        errors='0',
        skipped='0',
        failures='1',
        time='1.0',
        disabled='0'
    )
    test_suite.system_out = 'System Out'
    test_suite.system_err = 'System Err'

# Generated at 2022-06-13 15:48:12.479358
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    
    xml_output = '''<testsuite name="example" tests="2"></testsuite>'''
    example = TestSuite(name='example', tests=2)

    assert example.get_xml_element().tag == 'testsuite'
    assert _pretty_xml(example.get_xml_element()) == xml_output


# Generated at 2022-06-13 15:48:20.167466
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    ts1 = TestSuite('MyTestSuite',id='TS_ID_1',package='mypackage')
    ts1.timestamp = datetime.datetime(2020,1,1)
    tc1 = TestCase('TestCase_1',time=decimal.Decimal('1.234'))
    tc1.classname = 'ClassName_1'
    tc1.system_out = 'Text output'
    tc2 = TestCase('TestCase_2',time=decimal.Decimal('2.345'))
    tc2.classname = 'ClassName_2'
    tc2.system_err = 'Text error'
    ts1.cases.extend([tc1,tc2])
    ts2 = TestSuite('MyTestSuite',id='TS_ID_2',package='mypackage')
    ts2

# Generated at 2022-06-13 15:48:28.058437
# Unit test for method get_xml_element of class TestSuite
def test_TestSuite_get_xml_element():
    test_case = TestCase(name="TestCase1", classname="some class", status="Status", time=decimal.Decimal("0.05"))
    cases = [test_case]
    test_suite = TestSuite(name="TestSuite1", hostname="Some Hostname", id="12", package="some package",
                           timestamp="2020-10-03T19:38:09+01:00", cases=cases)
    assert TestSuite(name="TestSuite1", hostname="Some Hostname", id="12", package="some package",
                     timestamp="2020-10-03T19:38:09+01:00", cases=cases).get_xml_element() == test_suite.get_xml_element()