

# Generated at 2022-06-13 16:25:10.880598
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Test for method handle_request of class JsonRpcServer.
    # We create a JsonRpcServer object, try to send a valid json-rpc request
    # and check that the response is the expected.
    # Since the JsonRpcServer object is only used to call the method
    # handle_request, we do not care about the attribute _objects.
    jrs = JsonRpcServer()
    request = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "sum",
                          "params": [2, 3, 4]})
    response = json.loads(jrs.handle_request(request))
    assert (response["jsonrpc"] == "2.0" and response["id"] == 1 and
            response["result"] == 9)


# Generated at 2022-06-13 16:25:20.566790
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Create a simple class with a single method that returns
    # a list of two strings
    class Simple:
        def method(self):
            return ['a', 'b']

    # create the jsonrpc server
    srv = JsonRpcServer()

    # register the object with the server.
    srv.register(Simple())
    # Create a jsonrpc request that matches the method of the
    # registered object
    request = {
        'jsonrpc': '2.0',
        'id': '1',
        'method': 'method',
        'params': {}
    }

    # Encode the request and pass to handle_request()
    request = json.dumps(request)
    response = srv.handle_request(request)

    # Verify the response is a jsonrpc response with a
    # result that

# Generated at 2022-06-13 16:25:25.471241
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    obj = JsonRpcServer()
    request = '{ "jsonrpc": "2.0", "method": "foo", "params": [1,2,3], "id": 4}'
    assert json.loads(obj.handle_request(request)) == {"jsonrpc": "2.0", "method": "foo", "params": [1,2,3], "id": 4}

if __name__ == "__main__":
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:25:30.420734
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
	json_rpc_test = JsonRpcServer(obj={})
	json_rpc_test.header()
	json_rpc_test.response()


# Generated at 2022-06-13 16:25:39.721905
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import subprocess
    import unittest

    class Custom(object):

        def a(self, b):
            return b

        def b(self, c=None, d=None):
            return c, d

    server = JsonRpcServer()
    server.register(Custom())

    good_request_a = '{"id": 1, "jsonrpc": "2.0", "method": "a", "params": ["foo"]}'
    good_response_a = '{"jsonrpc": "2.0", "id": 1, "result": "foo"}'

    good_request_b = '{"id": 1, "jsonrpc": "2.0", "method": "b", "params": {"c": "bar", "d": "baz"}}'

# Generated at 2022-06-13 16:25:47.482597
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    jrpcserv = JsonRpcServer()
    response = jrpcserv.error(3, 'test', 'data')
    assert response['jsonrpc'] == '2.0'
    assert response['id'] == jrpcserv._identifier
    assert response['error']['code'] == 3
    assert response['error']['message'] == 'test'
    assert response['error']['data'] == 'data'


# Generated at 2022-06-13 16:25:56.786275
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    rpc = JsonRpcServer()
    rpc._identifier = '12345'

    assert rpc.error(code=777, message='abcd') == {'jsonrpc': '2.0', 'id': '12345',
                                                   'error': {'code': 777, 'message': 'abcd'}}
    assert rpc.error(code=777, message='abcd', data='1234') == {'jsonrpc': '2.0', 'id': '12345',
                                                                'error': {'code': 777, 'message': 'abcd', 'data': '1234'}}


# Generated at 2022-06-13 16:26:03.617639
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection import Connection
    import os

    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_cases = os.path.join(test_dir, 'test_cases', 'jsonrpc_server')

    server = JsonRpcServer()
    server.register(Connection())

    def read_input(name):
        with open(os.path.join(test_cases, name), 'r') as f:
            return f.read()

    def assertValidJson(got, expected):
        assert json.loads(got) == json.loads(expected)

    def assertValidPickle(got, expected):
        assert (cPickle.loads(to_text(got).encode()) == to_text(expected)).all()


# Generated at 2022-06-13 16:26:07.798235
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    test_params = '{"jsonrpc": "2.0", "method": "run_command", "params": [["show version"]], "id": "5"}'

    jsrpc = JsonRpcServer()

    test_response = jsrpc.handle_request(test_params)
    assert(test_response == '{"jsonrpc": "2.0", "id": "5", "error": {"code": 0, "message": "Method not found"}}')


if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:26:13.698613
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    class Test():
        pass

    obj = Test()
    obj.id = "TestId"
    server = JsonRpcServer()
    server._objects.add(obj)
    server._identifier = "TestId"
    response = server.error(code=404, message="Test error")
    assert response == {'jsonrpc': '2.0', 'id': 'TestId', 'error': {'code': 404, 'message': 'Test error'}}


# Generated at 2022-06-13 16:26:29.671414
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    # Setup fixture
    json_rpc_server = JsonRpcServer()
    json_rpc_server._identifier = 1234
    
    # Method under test
    code = 1
    message = "Test message"
    data = "Test data"
    result = json_rpc_server.error(code, message, data)
    
    # Unit test asserts
    assert result['jsonrpc'] == '2.0'
    assert result['id'] == 1234
    assert result['error']['code'] == 1
    assert result['error']['message'] == "Test message"
    assert result['error']['data'] == "Test data"

# Generated at 2022-06-13 16:26:34.879482
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    setattr(server, '_identifier', 'ansible')
    result_dict = server.response({'username': 'admin', 'password': 'password'})
    assert result_dict['jsonrpc'] == '2.0'
    assert result_dict['result'] == "{'password': 'password', 'username': 'admin'}"
    assert result_dict['id'] == 'ansible'

# Generated at 2022-06-13 16:26:40.399388
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    setattr(server, '_identifier', 1)
    assert server.error(1, 'test error') == {
        'jsonrpc': '2.0',
        'id': 1,
        'error': {
            'code': 1,
            'message': 'test error'
        }
    }

# Generated at 2022-06-13 16:26:48.411316
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    input = '{"jsonrpc":"2.0","method":"version","params":[],"id":1}'
    output = '{"jsonrpc": "2.0", "result": "{\\"stdout\\": \\"Cumulus VX Release 2.1.0\\", \\"stdout_lines\\": [[\\"Cumulus VX Release 2.1.0\\"]], \\"warnings\\": []}", "id": 1}'

    server = JsonRpcServer()

    from modules.connection import Connection
    from plugins.connection.ssh import Connection as SSHConnection

    inventory = dict(
        host='10.0.0.2',
        port=9022
    )
    connection = SSHConnection(inventory)
    state = dict(
        auto_connect=True,
        persistent=False
    )
    params = dict

# Generated at 2022-06-13 16:26:52.489011
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    server._identifier = 1
    result = server.response({'a':'b'})
    assert(result['id'] == 1 and result['result'] == '{"a": "b"}' and result['result_type'] == 'pickle')

# Generated at 2022-06-13 16:27:01.862341
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # Unit test for JsonRpcServer.response
    server = JsonRpcServer()
    setattr(server, '_identifier', 10)
    result = {
        'jsonrpc': '2.0',
        'id': 10,
        'result': 'success',
    }
    assert server.response(result) == result

    setattr(server, '_identifier', 11)
    result = {
        'jsonrpc': '2.0',
        'id': 11,
        'result_type': 'pickle',
        'result': 'gAJ9cQ=='
    }
    data = {'success': True}
    assert server.response(data) == result


# Generated at 2022-06-13 16:27:06.783230
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    result = server.error(2, 'error message')
    assert result == {
        'error': {
            'code': 2,
            'message': 'error message'
        },
        'id': None,
        'jsonrpc': '2.0'
    }
    assert result['error']['message'] == 'error message'
    assert result['id'] is None


# Generated at 2022-06-13 16:27:10.948301
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = '{"jsonrpc": "2.0", "method": "test", "params": [1, 2, 3], "id": 1}'
    server = JsonRpcServer()
    assert '"result": true' in server.handle_request(request)


# Generated at 2022-06-13 16:27:15.108663
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    error = server.error(code=1, message='test')
    assert error == {"jsonrpc": "2.0", "id": None, "error": {"code": 1, "message": "test"}}


# Generated at 2022-06-13 16:27:25.075562
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jsonrpc_server = JsonRpcServer()
    request1 = {'jsonrpc': '2.0', 'method': 'valid_method', 'params': [[2, 3], {}], 'id': 1}
    request2 = {'jsonrpc': '2.0', 'method': 'valid_method', 'params': [[2, 3], {'id': 1}], 'id': 1}
    request3 = {'method': 'not_valid_method', 'params': [[2, 3], {}], 'id': 1}
    request4 = {'jsonrpc': '2.0', 'method': 'not_valid_method', 'params': [[2, 3], {}], 'id': 1}

# Generated at 2022-06-13 16:27:40.895675
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.json_rpc import JsonRpcServer
    from collections import namedtuple
    import json
    import ansible.module_utils.connection

    RetVal = namedtuple('RetVal', ['result', 'response', 'error'])

    # execute the handle_request method of class JsonRpcServer
    rpc = JsonRpcServer()

    # case 1: valid remote_module_args
    remote_module_args = {'method': 'module_exec', 'params': [[{'spec': '*', 'module': 'shell',
                            'args': 'echo "hello"', 'timeout': 20}], {}]}
    result = rpc.handle_request(json.dumps(remote_module_args))
    ret_obj = json.loads(result)

# Generated at 2022-06-13 16:27:47.841073
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    test_rpc_server = JsonRpcServer()
    test_rpc_server.handle_request(b'{ "jsonrpc": "2.0", "method": "echo", "params": [1,"2"], "id": "1"}')
    test_rpc_server.handle_request(b"{ 'jsonrpc': '2.0', 'method': 'echo', 'params': [1,'2'], 'id': '1'}")
    test_rpc_server.handle_request(b"{ 'jsonrpc': '2.0', 'method': 'echo', 'params': [1,'2'], 'id': '1'} ")

# Generated at 2022-06-13 16:27:55.920394
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Initialise test class
    tjc = JsonRpcServer()
    # Create expected values
    expected_response = json.dumps({'id': None, 'jsonrpc': '2.0', 'error': {'message': 'Internal error', 'code': -32603}})
    
    # Call test method
    # If no exception is raised then test passes
    try:
        tjc.handle_request('{"jsonrpc":"2.0","id":null,"method":"method_that_does_not_exist","params":[]}')
    except:
        assert False

# Generated at 2022-06-13 16:27:58.229928
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    j = JsonRpcServer()
    j.response(result = "This is a result")


# Generated at 2022-06-13 16:28:08.603336
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # If method is rpc. or _
    def mock_json_loads():
        return {"method": "rpc._test"}

    def mock_invalid_request():
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "Invalid request", "data": None}}

    json.loads = mock_json_loads
    JsonRpcServer.invalid_request = mock_invalid_request

    result = JsonRpcServer.handle_request(None, None)
    expected = json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "Invalid request", "data": None}})

    assert result == expected

    # Method not found

# Generated at 2022-06-13 16:28:19.068847
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():

    # Create an instance of JsonRpcServer
    svr = JsonRpcServer()

    # Set the identifier value of our JsonRpcServer instance
    # so the header method will return a valid header for the json rpc
    # response
    setattr(svr, '_identifier', '12345')

    # Set the result value of our JsonRpcServer instance that we expect to
    # be returned from the response method
    result = {'type': 'json', 'result': 'json rpc response'}
    expected_response = {'jsonrpc': '2.0', 'id': '12345', 'result': result}

    # Call the response method with the result value
    rpc_response = svr.response(result)

    # Assert the result value is the same as what was returned by the
    # response

# Generated at 2022-06-13 16:28:26.059375
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    dummy_jsonrpc_server = JsonRpcServer()

    # Nothing is returned, no response_simple is available, so it will be None
    response = dummy_jsonrpc_server.handle_request("""{
        "jsonrpc" : "2.0",
        "method" : "invalid method",
        "params" : [ "foo", "bar" ],
        "id" : 2
    }""")
    assert response == json.dumps(dummy_jsonrpc_server.method_not_found())



# Generated at 2022-06-13 16:28:36.727539
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
 
    # defining the test class, this is the class from which the method will be called
    class Mock(object):
        def __init__(self):
            return

        def jsonrpc(self, *args, **kwargs):
            return posts

    # defining the JsonRpcServer class, this is the class that will be tested
    class JsonRpcServer(object):

        _objects = set()

        def handle_request(self, request):
            request = json.loads(to_text(request, errors='surrogate_then_replace'))

            method = request.get('method')

            if method.startswith('rpc.') or method.startswith('_'):
                error = self.invalid_request()
                return json.dumps(error)


# Generated at 2022-06-13 16:28:45.331419
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc_server = JsonRpcServer()
    try:
        result = json_rpc_server.handle_request(b'{"method": "test", "params": [], "id": 0}')
    except:
        result = 'test fail'
    finally:
        assert result == '"test fail"'
    try:
        result = json_rpc_server.handle_request(b'{"method": "test", "params": [], "id": 1}')
    except:
        result = 'test fail'
    finally:
        assert result == '"test fail"'


if __name__ == "__main__":
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:28:52.912925
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    # No method defined
    request = '{"jsonrpc": "2.0", "method": "foo", "id": 0, "params": []}'
    assert b'"code": -32601' in server.handle_request(request)
    # Method defined but missing argument ('obj')
    server.foo = lambda: None
    assert b'"code": -32602' in server.handle_request(request)
    # Method defined but invalid argument ('bar')
    server.foo = lambda obj: None
    assert b'"code": -32602' in server.handle_request(request)
    # Method defined but invalid argument ('obj')
    server.foo = lambda obj: None

# Generated at 2022-06-13 16:29:03.666132
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    # Test exception ConnectionError
    request = '{"jsonrpc": "2.0", "method": "_connection.connection_error", "params": [], "id": 1}'
    ans = server.handle_request(request)
    assert ans == '{"jsonrpc": "2.0", "id": 1, "error": {"code": -32603, "message": "Internal error", "data": "ConnectionError(\"ConnectionError\")"}}'
    # Test exception Exception
    request = '{"jsonrpc": "2.0", "method": "_connection.internal_error", "params": [], "id": 1}'
    ans = server.handle_request(request)

# Generated at 2022-06-13 16:29:09.916114
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    class A(object):
        def hello(self, test):
            return test

    server.register(A())
    request = {'jsonrpc': '2.0', 'id': 'test', 'method': 'hello', 'params': ["test"]}
    request = json.dumps(request)
    response = server.handle_request(request)
    assert response
    response = json.loads(response)
    assert response['result'] == 'test'
    assert response['id'] == 'test'

# Generated at 2022-06-13 16:29:11.173078
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass


# Generated at 2022-06-13 16:29:15.454094
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    req = '{"id": 17, "jsonrpc": "2.0", "method": "get_config", "params": [{"source":"RUNNING"}]}'
    res = server.handle_request(req)
    assert isinstance(res, text_type)
    assert '{"jsonrpc": "2.0", "id": 17, "error": {"code": -32601, "message": "Method not found"}}' == res

# Generated at 2022-06-13 16:29:22.469010
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Hosts(object):
        def iteritems(self):
            return self

        def next(self):
            raise StopIteration

    class JsonRpcConnection(object):
        def __init__(self, module):
            self.params = {}
            self.module = module

        def get_option(self, value):
            return self.params[value]

        def get_capabilities(self):
            return {'device_info': {}}

        def get_connection(self):
            pass

        def connect(self):
            pass

        def disconnect(self):
            pass

        @staticmethod
        def to_text(value, errors='surrogate_then_replace'):
            return value

        def get_host_args(self):
            return {}

        def run(self, commands):
            pass

   

# Generated at 2022-06-13 16:29:31.597957
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # testing response()
    assert JsonRpcServer().response('test') == \
        dict(result='test', result_type='', id=None, jsonrpc='2.0')
    # testing response() as a boolean value
    assert JsonRpcServer().response(True) == \
        dict(result='True', result_type='', id=None, jsonrpc='2.0')
    # testing response() as a integer value
    assert JsonRpcServer().response(1) == \
        dict(result='True', result_type='', id=None, jsonrpc='2.0')
    # testing response() with dictionary passed
    assert JsonRpcServer().response(dict(test=True)) == \
        dict(result='test', result_type='', id=None, jsonrpc='2.0')

# Generated at 2022-06-13 16:29:42.308275
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    class JsonRpcServerTest(JsonRpcServer):
        def add(self, a, b):
            return a + b

        def _invalid_request(self):
            self.invalid_request()

        def _invalid_params(self):
            self.invalid_params()

        def _internal_error(self, data):
            self.internal_error(data)

        def _method_not_found(self):
            self.method_not_found()

    server = JsonRpcServerTest()
    server.register(server)


# Generated at 2022-06-13 16:29:51.858585
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    # Test handle_request method
    def test_handle_request(
            self,
            check_request=True,
            check_response=True,
            check_response_result=True
    ):
        # Prepare
        request = {
            "jsonrpc": "2.0",
            "method": "register_slave",
            "params": [{"url": "http://127.0.0.1:1234"}],
            "id": 1
        }
        # Verify
        self.assertEqual(
            json.loads(self.server.handle_request(
                json.dumps(request))),
            {
                "jsonrpc": "2.0",
                "id": 1,
                "result": None
            }
        )
        # Cleanup
        self.server.unregister_slave()



# Generated at 2022-06-13 16:29:52.331630
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass

# Generated at 2022-06-13 16:29:55.638740
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import mock
    JsonRpcServer().handle_request("""{"jsonrpc": "2.0", "method": "foo", "params": [1, 2], "id": 1}""")
    assert True


# Generated at 2022-06-13 16:30:06.821468
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Server(JsonRpcServer):
        def method(self, one, two):
            return (one, two)
    try:
        server = Server()
    except Exception as exc:
        assert False, "Failed to create server"
    data = json.dumps({'jsonrpc': '2.0', 'id': 1234, 'params': [['one', 'two'], {}], 'method': 'method'})
    result = json.loads(server.handle_request(data))
    assert 'result' in result
    assert result['result'] == ['one', 'two']

if __name__ == "__main__":
    # execute only if run as a script
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:30:15.220090
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    setattr(server, '_identifier', '12345')
    result = {'unit': 'test'}
    assert server.header() == {'id': '12345', 'jsonrpc': '2.0'}
    assert server.response(result) == {'jsonrpc': '2.0', 'id': '12345', 'result': '{}', 'result_type': 'pickle'}
    assert server.response(text_type(result)) == {'jsonrpc': '2.0', 'id': '12345', 'result': '{}'}


# Generated at 2022-06-13 16:30:21.610679
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Test case for success response
    def handle_request_valid_method_success(request):
        request = json.loads(to_text(request, errors='surrogate_then_replace'))

        if request.get('method') == 'rpc.debug':
            return True
        else:
            return False

    assert(handle_request_valid_method_success('''{"jsonrpc": "2.0", "method": "rpc.debug"}''') == True)
    assert(handle_request_valid_method_success('''{"jsonrpc": "2.0", "method": "rpc.debu"}''') == False)

    # Test case for failure response

# Generated at 2022-06-13 16:30:32.312264
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    js = JsonRpcServer()
    request = {'jsonrpc': '2.0', 'id': 1532937398568, 'method': 'hello', 'params': [{'name': 'dude'}]}
    response = js.handle_request(json.dumps(request))
    assert(json.loads(response) == js.method_not_found())
    request = {'jsonrpc': '2.0', 'id': 1532937398568, 'method': '_hello', 'params': [{'name': 'dude'}]}
    response = js.handle_request(json.dumps(request))
    assert(json.loads(response) == js.method_not_found())

# Generated at 2022-06-13 16:30:42.482746
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network_common import load_provider
    from ..network.iosxr import iosxr_provider_spec
    from ..network.iosxr import iosxr_provider_spec_v2
    from ..network.iosxr import iosxr_argument_spec
    from ..network.iosxr import iosxr_argument_spec_v2

    def call_method(self, params):
        args, kwargs = params
        method = kwargs.get('body').get('method')

        resource = kwargs.get('enable_session')
        resource = resource.run_commands([
            'show run | i hostname'
        ])
        resource = resource[0].get('stdout_lines')

# Generated at 2022-06-13 16:30:53.357691
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Called method process_message with three arguments
    def test_method(arg1, arg2, arg3):
        return arg1, arg2, arg3

    # Unit test params
    class Test:
        def process_message(self, arg1, arg2, arg3):
            return arg1, arg2, arg3

    # Mock module arguments
    args = dict(
        method='process_message',
        params=[[1, 2, 3], [4, 5, 6]]
    )

    server = JsonRpcServer()
    server.register(Test())

    # Called method
    rpc_method = getattr(server, 'handle_request')
    result = rpc_method(json.dumps(args))

    # Assertions

# Generated at 2022-06-13 16:31:03.877402
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils import basic
    from ansible.module_utils.network.cliconf import CliConf

    class MyModule(object):

        def __init__(self):
            self.argument_spec = dict()
            self.params = dict()
            self.connection = CliConf()
            self._result = dict()
        def load_params(self):
            return
        def fail_json(self, **kwargs):
            self._result.update({'params': kwargs})
            return
        def run_command(self, cmd, check_rc=True):
            pass
        def add_argument(self, *args, **kwargs):
            pass
        def exit_json(self, **kwargs):
            self._result.update({'params': kwargs})
            return

# Generated at 2022-06-13 16:31:14.029778
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    """
    Author: Santosh Kumar
    Date: 02.09.2020
    """
    request = json.loads("""{"jsonrpc": "2.0", "method": "my_method", "params": {"arg1": 1, "arg2": "str"}, "id": 1}""")
    obj = json.loads("""{"jsonrpc": "2.0", "method": "my_method", "params": {"arg1": 1, "arg2": "str"}, "id": 1}""")
    my_server = JsonRpcServer()
    my_server.register(obj)
    response = my_server.handle_request(request)
    return response



# Generated at 2022-06-13 16:31:16.622188
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    rpcServer = JsonRpcServer()
    result="hello"
    response=rpcServer.response(result)
    assert(response['result']==result)
    assert(response['id']==None)
    assert(response['jsonrpc']=="2.0")

# Generated at 2022-06-13 16:31:27.326133
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import to_list, to_text

    class TestConnection(Connection):

        def get_config(self, *args, **kwargs):
            return 'test_config'

        def load_config(self, *args, **kwargs):
            return dict(diff=dict(prepared=dict(config='test_config')))

    rpc_command = '{"method": "aaa_authentication", "params": [{"key": "test"}], "jsonrpc": "2.0", "id": 12345}'
    json_rpc_server = JsonRpcServer()

    # create instance of connection and register connection with JsonRpcServer
    connection = TestConnection(None)
    json_rpc_server.register

# Generated at 2022-06-13 16:31:35.936647
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # Test response containing result None
    json_rpc_server = JsonRpcServer()
    json_rpc_server._identifier = 'abc'
    response = json_rpc_server.response()
    assert 'result' not in response
    assert response['id'] == 'abc'
    assert response['jsonrpc'] == '2.0'

    # Test response containing result 123
    json_rpc_server = JsonRpcServer()
    json_rpc_server._identifier = 'abc'
    response = json_rpc_server.response(123)
    assert response['result'] == u'123'
    assert response['id'] == 'abc'
    assert response['jsonrpc'] == '2.0'

    # Test response containing result 'abc'
    json_rpc_server = JsonRpc

# Generated at 2022-06-13 16:31:43.978522
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    print(('\nTest top of handle_request method'))

    # Create mock method that will not fail
    def method():
        return "Test"


    # Create mock JsonRpcServer object
    server = JsonRpcServer()

    # Create mock object
    obj = type('obj', (object,), {'method': method})

    # Register mock object with server
    server.register(obj)

    # Create request
    request = '{"jsonrpc": "2.0", "method": "method", "params": [], "id": 1}'

    # Create error
    error = '{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 1}'

    # Create mock exception
    exception = AttributeError

    # Run test
   

# Generated at 2022-06-13 16:31:45.223774
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jrs = JsonRpcServer()
    assert True


# Generated at 2022-06-13 16:31:53.954666
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    obj = type('object', (object,), {
        'jsonrpc': '2.0',
        'result': 'success'
    })
    result = obj()
    response = server.response(result)
    assert response == result

    obj = type('object', (object,), {
        'jsonrpc': '2.0',
        'error': 'fail'
    })
    result = obj()
    response = server.response(result)
    assert response == result

    result = 'success'
    response = server.response(result)
    assert response == {'jsonrpc': '2.0', 'result': 'success', 'id': None}

    result = 'success'
    server._identifier = 1
    response = server.response(result)

# Generated at 2022-06-13 16:31:59.347767
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = '{"jsonrpc": "2.0", "method": "send_config", "params": [], "id": "1"}'
    response = JsonRpcServer().handle_request(request)
    assert response == '{"error": {"code": -32601, "message": "Method not found"}, "id": "1", "jsonrpc": "2.0"}'

if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:32:11.270006
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    print("Test: method handle_request of class JsonRpcServer")
    service = JsonRpcServer()
    class RPC:
        def add(self, x, y):
            return x+y
    rpc = RPC()

    assert service.handle_request(request='') == json.dumps({'jsonrpc': '2.0', 'id': None, 'error': {'code': -32700, 'message': 'Parse error', 'data': None}})
    
    assert service.handle_request(request='{"jsonrpc":"2.0","method":"add","params":[4,3],"id":1}') == json.dumps({'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32601, 'message': 'Method not found', 'data': None}})


# Generated at 2022-06-13 16:32:17.975539
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc_server=JsonRpcServer()
    import pickle
    def test_func(*args, **kwargs):
        return pickle.dumps(args)
    test_func.__globals__ = globals()
    json_rpc_server.register(test_func)
    test_req = {'method': 'test_func','params': [[{"a":"a"},2,3,4],{"b":1}],'id': 15}
    assert(json_rpc_server.handle_request(test_req))
    assert(json_rpc_server.handle_request("abc"))
    assert(json_rpc_server.handle_request("{}"))

# Generated at 2022-06-13 16:32:25.865801
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    import json

    jr_test = JsonRpcServer()
    result_test = {"test": "test_result"}
    jr_test.register(result_test)
    response = jr_test.response(result_test)
    assert "jsonrpc" in response
    assert response["jsonrpc"] == '2.0'
    assert "result" in response
    assert "result_type" not in response
    assert response["result"] == json.dumps(result_test)


# Generated at 2022-06-13 16:32:32.905656
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    instance = JsonRpcServer()
    setattr(instance, '_identifier', "4ddcd6f9-6d9c-4f7a-a2c1-64a2a8d66084")
    import pdb; pdb.set_trace()
    response = instance.response("Hello world")
    assert(response == {"jsonrpc": "2.0", "id": "4ddcd6f9-6d9c-4f7a-a2c1-64a2a8d66084", "result": "Hello world"})
    print(response)



# Generated at 2022-06-13 16:32:41.171721
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():

    result_pickle = cPickle.dumps([1,2,3], protocol=0)
    result_text = 'result_text'
    server = JsonRpcServer()

    # Case 1: response should be a dict with expected fields,
    # if no result is passed.
    resp = server.response()
    assert resp['jsonrpc'] == '2.0'
    assert resp['id'] == server._identifier
    assert 'result' not in resp
    assert 'result_type' not in resp

    # Case 2: If result is passed as a string, it will be returned
    # as is in response.
    resp = server.response(result_text)
    assert resp['jsonrpc'] == '2.0'
    assert resp['id'] == server._identifier
    assert resp['result'] == result_text

# Generated at 2022-06-13 16:32:51.350282
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    JsonRpcServer_object = JsonRpcServer()

    # method handle_request with invalid request
    request = json.dumps({
        "id": "testId",
        "method": "rpc.method",
        "params": [1, 2]
    })
    result = JsonRpcServer_object.handle_request(request)
    result = json.loads(result)
    assert result['error']['code'] == -32600

    # method handle_request with non-existing method
    request = json.loads(request)
    request['method'] = "method"
    request = json.dumps(request)
    result = JsonRpcServer_object.handle_request(request)
    result = json.loads(result)
    assert result['error']['code'] == -32601

    #

# Generated at 2022-06-13 16:32:59.317583
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
  req = '{"id": 1, "jsonrpc": "2.0", "method": "get_connection_info", "params": [[]]}'

# Generated at 2022-06-13 16:33:05.357439
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()

    for obj in server._objects:
        del obj

    server._objects.clear()

    # Method not found
    request_json = '{"jsonrpc": "2.0", "method": "not_found", "params": [], "id": 1}'
    response_json = server.handle_request(request_json)
    assert response_json == '{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 1}'

    # Invalid request
    request_json = '{"jsonrpc": "2.0", "method": "parse_error", "params": [], "id": 1}'
    response_json = server.handle_request(request_json)

# Generated at 2022-06-13 16:33:11.476823
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import pytest
    import json

    @pytest.fixture
    def server():
        class Foo(object):
            def bar(self):
                return 'bar'

        obj = JsonRpcServer()
        obj.register(Foo())
        return obj

    def test_success(server):
        req = json.dumps({
            'id': 'ansible-test-1',
            'method': 'bar',
            'params': [],
        })

        response = json.loads(server.handle_request(req))

        assert response == {
            'id': 'ansible-test-1',
            'jsonrpc': '2.0',
            'result': 'bar',
        }


# Generated at 2022-06-13 16:33:14.037544
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request(): 
    handle_request_result = JsonRpcServer.handle_request()
    assert handle_request_result == 'JsonRpcServer.handle_request() should return a string'


# Generated at 2022-06-13 16:33:19.537718
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    text = "aaa"
    pickle = cPickle.dumps(text)

    assert json.loads(server.response(text)) == {'jsonrpc': '2.0', 'id': None,
                                                 'result': 'aaa'}
    assert json.loads(server.response(pickle)) == {'jsonrpc': '2.0', 'id': None,
                                                   'result_type': 'pickle',
                                                   'result': '\x80\x02U\x03aaa.'}

# Generated at 2022-06-13 16:33:25.222780
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    testing_result = { "key1": "value1","key2": "value2","key3": "value3"}
    # instantiate the class
    js = JsonRpcServer()
    # create attribute '_identifier' in object js
    js._identifier = 'testing'
    # call the method response
    result = js.response(testing_result)
    # checking a successful message
    if 'jsonrpc' in result and result['id'] == 'testing' and 'result' in result:
        print("Success, the result has 'jsonrpc', 'id' and 'result' key")
    else:
        print("fail")


# Generated at 2022-06-13 16:33:28.677048
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    obj = JsonRpcServer()
    test_result = "response"
    result = obj.response(result=test_result)
    assert result == {'jsonrpc': '2.0', 'id': obj._identifier, 'result': test_result}


# Generated at 2022-06-13 16:33:36.100650
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    json_request = '{"jsonrpc": "2.0", "method": "get_connection", "params": [1, 2, 3], "id": 123}'
    assert server.handle_request(json_request) == '{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 123}'

# Generated at 2022-06-13 16:33:42.417203
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # input
    obj = JsonRpcServer()
    obj._identifier = 'id_test'
    result = 'result_test'
    # output for response
    output_response = {
        'jsonrpc': '2.0', 
        'id': 'id_test',
        'result': 'result_test',
    }
    # test
    assert(output_response == obj.response(result))


# Generated at 2022-06-13 16:33:49.342331
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc_server = JsonRpcServer()
    json_rpc_server._identifier = '1234'
    json_rpc_server._objects = set('{"method":"test_method"}')
    result = json_rpc_server.handle_request('{"method":"test_method"}')
    assert result == '{"jsonrpc": "2.0", "id": "1234"}'

# Generated at 2022-06-13 16:33:58.407911
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.network.common.parsing import Conditional
    from ansible.module_utils.network.common.utils import to_list

    server = JsonRpcServer()
    server.register(Conditional())

    request = {
        "jsonrpc": "2.0",
        "method": "to_list",
        "params": [True],
        "id": "1"
    }
    response = to_text(server.handle_request(json.dumps(request)))
    response = json.loads(response)
    assert response == {'id': '1', 'jsonrpc': '2.0', u'result': [True]}

# Generated at 2022-06-13 16:34:02.648039
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    test_obj = JsonRpcServer()
    request = r'{"jsonrpc": "2.0", "method": "test_method", "params": [], "id": 1}'
    result = test_obj.handle_request(request)
    print(result)

if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:34:05.958973
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    rpc_server = JsonRpcServer()
    setattr(rpc_server, '_identifier', 'test-id')
    rpc_server.response(True)

# Generated at 2022-06-13 16:34:06.336007
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    assert True == False

# Generated at 2022-06-13 16:34:11.365061
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jsonrpc = JsonRpcServer()
    data = """{"jsonrpc": "2.0", "method": "test", "params": [], "id": 0}"""
    response = """{"jsonrpc": "2.0", "id": 0, "error": {"code": -32601, "message": "Method not found", "data": null}}"""
    assert jsonrpc.handle_request(data) == response

# Generated at 2022-06-13 16:34:24.305091
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import sys
    if sys.version_info[:2] == (2, 6):
        import unittest2 as unittest
    else:
        import unittest
    import mock
    from ansible.module_utils import basic

    class TestJsonRpc(unittest.TestCase):

        @classmethod
        def setUp(cls):
            class RpcClass(object):
                def json_method(self):
                    return {'jsonrpc': '2.0', 'id': 'test_id', 'result': 'success'}

                def echo(self, *args, **kwargs):
                    return (args, kwargs)

                def raise_connection_error(self):
                    raise ConnectionError('test-error', code=500)


# Generated at 2022-06-13 16:34:35.565564
# Unit test for method handle_request of class JsonRpcServer

# Generated at 2022-06-13 16:34:39.716229
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    print(server.response())


if __name__ == '__main__':
    server = JsonRpcServer()
    request = '{"jsonrpc":"2.0","method":"hello","params":[],"id":null}'
    print(server.handle_request(request))

# Generated at 2022-06-13 16:34:45.415420
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = '{"jsonrpc": "2.0","method": "get_model_info","params": [], "id": 1}'
    result = server.handle_request(request)
    response = '{"error": {"code": -32601, "message": "Method not found"}, "id": 1, "jsonrpc": "2.0"}'
    assert result == response

# Generated at 2022-06-13 16:35:00.437579
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import json
    import os
    import pytest
    from ansible.module_utils.six import PY3

    server = JsonRpcServer()

    class TestModule(object):
        def test_method(self, param):
            return 'test result %s' % param

        @staticmethod
        def test_staticmethod(param):
            return 'test result %s' % param

        @classmethod
        def test_classmethod(cls, param):
            return 'test result %s' % param

    server.register(TestModule())
