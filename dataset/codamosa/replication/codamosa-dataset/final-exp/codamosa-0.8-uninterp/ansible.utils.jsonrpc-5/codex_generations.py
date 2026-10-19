

# Generated at 2022-06-13 16:25:12.906109
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # Create instance of JsonRpcServer
    jrs = JsonRpcServer()
    # Set _identifier
    jrs._identifier = 78
    # Wait for result of method response
    result = jrs.response()
    try:
        assert result == {
            'jsonrpc': '2.0',
            'id': 78,
            'result': None
        }
    except AssertionError:
        print("Wrong value in result")

# Generated at 2022-06-13 16:25:21.865915
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():

    server = JsonRpcServer()
    setattr(server,'_identifier','1')

    error_type = -32603
    error_message = 'Internal error'
    error_data = 'This is an error message'

    # Test case - error code exist in the range of -32768 .. -32000
    assert server.error(error_type,error_message,error_data) == {'error': {'code': -32603, 'message': 'Internal error', 'data': 'This is an error message'}, 'id': '1', 'jsonrpc': '2.0'}

    # Test case - error code does not exist in the range of -32768 .. -32000

# Generated at 2022-06-13 16:25:27.456608
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = '{"jsonrpc": "2.0", "method": "echo", "params": ["echo message"], "id": 1}'
    response = JsonRpcServer().handle_request(request)
    if not isinstance(response, str):
        raise AssertionError("response must be str")
    if not isinstance(json.loads(response), dict):
        raise AssertionError("response must be json object")


# Generated at 2022-06-13 16:25:38.342052
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    hostname = 'localhost'
    JsonRpc_initial = {
        "jsonrpc": "2.0",
        "method": "some_method",
        "params": [["arg1", "arg2"]],
        "id": 100
    }
    JsonRpc_initial = json.dumps(JsonRpc_initial)

    server_obj = JsonRpcServer()
    response = server_obj.handle_request(JsonRpc_initial)
    assert response == '{"jsonrpc": "2.0", "id": 100, "error": {"code": -32601, "message": "Method not found"}}'

    class Test_object():
        def some_method(self, arg1, arg2):
            return True

    obj = Test_object()

# Generated at 2022-06-13 16:25:45.112260
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    error = server.error(code=123, message="test")
    assert error.get('id') == None
    assert error.get('error').get('code') == 123
    assert error.get('error').get('message') == "test"
    assert error.get('error').get('data') == None


# Generated at 2022-06-13 16:25:54.408855
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import pytest
    server = JsonRpcServer()
    with pytest.raises(Exception) as excinfo:
        server.handle_request(request='{"method":"rpc.run_commands","params":[], "id":"identifier"}')
    with pytest.raises(Exception) as excinfo:
        server.handle_request(request='{"method":"_up_and_running","params":[], "id":"identifier"}')
    with pytest.raises(Exception) as excinfo:
        server.handle_request(request='{"method":"__class_is_registered","params":[], "id":"identifier"}')


# Generated at 2022-06-13 16:26:00.425212
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    request_data = {
        "jsonrpc": 2.0,
        "method": "test",
        "id": 1,
        "params": {
            "code": -32600,
            "message": "Invalid request",
            "data": None
        }
    }
    server = JsonRpcServer()
    response = server.handle_request(json.dumps(request_data))

    assert json.loads(response)['error']['code'] == request_data['params']['code']


# Generated at 2022-06-13 16:26:04.999859
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer() 
    request = json.loads('{"jsonrpc": "2.0", "method": "foobar", "id":0}')
    result = server.handle_request(request)

    assert result is not None, "Error"



# Generated at 2022-06-13 16:26:15.422578
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    import unittest

    class TestJsonRpcServerResponse(unittest.TestCase):
        def test_response_with_null_result(self):
            from ansible.module_utils.remote_management.jsonrpc import JsonRpcServer
            from ansible.module_utils.remote_management.jsonrpc import ConnectionError

            jsonrpc_server_obj = JsonRpcServer()
            jsonrpc_server_obj._identifier = 1

            response_dict = jsonrpc_server_obj.response()
            self.assertEqual("null", response_dict['result'])

            response_dict = jsonrpc_server_obj.response(None)
            self.assertEqual("null", response_dict['result'])


# Generated at 2022-06-13 16:26:22.882825
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    server._identifier = None
    resp = server.response()
    result = '{"id": null, "jsonrpc": "2.0"}'
    assert resp == result

    server._identifier = 0
    resp = server.response()
    result = '{"id": 0, "jsonrpc": "2.0"}'
    assert resp == result

    server._identifier = 1
    resp = server.response()
    result = '{"id": 1, "jsonrpc": "2.0"}'
    assert resp == result

    server._identifier = "test"
    resp = server.response()
    result = '{"id": "test", "jsonrpc": "2.0"}'
    assert resp == result

    server._identifier = {}
    resp = server.response

# Generated at 2022-06-13 16:26:36.456948
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.common.network import register_transport, to_list
    from ansible.module_utils.connection import Connection

    # initialize the server
    server = JsonRpcServer()
    server.register(Connection())

    # run the server
    response = server.handle_request('{"jsonrpc": "2.0", "method": "network.register_transport", "params": [], "id": 79}')
    rsp = json.loads(response)
    assert rsp['id'] == 79
    assert rsp['result'] == 'pickle'

    # test for invalid json content
    response = server.handle_request('{"jsonrpc": "2.0", "method": "network.register_transport", "params": [], ')
    rsp = json.loads(response)
   

# Generated at 2022-06-13 16:26:41.067955
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    JsonRpcServer_object = JsonRpcServer()
    params = ('', {})
    request = {'method': 'echo', 'params': params, 'id': 1}
    request = json.dumps(request)
#    response = JsonRpcServer_object.handle_request(request)
#    print(response)

# Generated at 2022-06-13 16:26:47.819052
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import json
    rpc_server = JsonRpcServer()
    # Call JsonRpcServer().handle_request()
    request = {"method": "math.add", "id": "1", "params": [1, 2]}
    request = json.dumps(request)
    response = rpc_server.handle_request(request)
    data = json.loads(response)
    if data.get("result") != 3:
        print("Test Failed: In Method test_JsonRpcServer_handle_request")

""" Unit test for method test_JsonRpcServer_handle_request """
test_JsonRpcServer_handle_request()


# Generated at 2022-06-13 16:26:58.290744
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.module_utils.network.common.parsing import Conditional
    from ansible.module_utils.network.common.config import NetworkConfig

    connection_obj = Connection(None)
    connection_obj._play_context = {'network_os': 'ios'}
    config_obj = NetworkConfig(indent=1, contents=None)
    conn_module = load_provider('ios')
    connection = conn_module.Connection(connection_obj._play_context, connection_obj)
    cond = Conditional(None)
    connection._get_capabilities = conn_module._get_capabilities
    connection._load_config = config_obj._load_config
    connection._get

# Generated at 2022-06-13 16:27:03.850871
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    class MockObj():
        def test_method(self):
            return True
    
    server = JsonRpcServer()
    mock_obj = MockObj()
    server.register(mock_obj)
    setattr(server, '_identifier', '1')
    response = server.response(True)
    expected_response = {'result': 'True', 'jsonrpc': '2.0', 'id': '1'}
    assert response == expected_response

# Generated at 2022-06-13 16:27:06.718153
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    server.handle_request('{"jsonrpc": "2.0", "method": "hello", "params": [42, 23], "id": 1}')
    
test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:27:17.332698
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    rpc = JsonRpcServer()
    setattr(rpc, '_identifier', 'ident')
    json_response = rpc.response('abcd')
    assert (json_response['jsonrpc'] == '2.0')
    assert (json_response['id'] == 'ident')
    assert (json_response['result'] == 'abcd')
    assert (len(json_response) == 3)
    json_response = rpc.response(['a', 'b'])
    assert (json_response['jsonrpc'] == '2.0')
    assert (json_response['id'] == 'ident')
    assert (json_response['result_type'] == 'pickle')
    assert (len(json_response) == 3)
    json_response = rpc.response(1)

# Generated at 2022-06-13 16:27:22.630445
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    test_id = "1234"
    test_result = "testresult"
    server = JsonRpcServer()
    setattr(server, '_identifier', test_id)
    response = server.response(test_result)
    assert(response == {'jsonrpc': '2.0', 'id': test_id, 'result': test_result})



# Generated at 2022-06-13 16:27:30.169619
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils import basic

    module_name = 'basic'
    module = basic.AnsibleModule(
        argument_spec=dict(
            my_bool=dict(type='bool', default=False),
            my_int=dict(type='int', default=5),
            my_list=dict(type='list', default=['one', 'two']),
        ))
    rpc = JsonRpcServer()

    rpc.register(module)

    request_1 = json.dumps({
        'jsonrpc': '2.0',
        'method': 'ping',
        'params': [],
        'id': '1'
    })

    response_1 = rpc.handle_request(request_1)

# Generated at 2022-06-13 16:27:40.029056
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    import collections
    jrpc_server = JsonRpcServer()
    jrpc_server._identifier = 1

# Generated at 2022-06-13 16:27:52.411593
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
	from ansible_collections.community.general.tests.unit.compat import unittest
	from ansible_collections.community.general.tests.unit.compat.mock import patch, Mock, MagicMock, call

	class TestJsonRpcServer(unittest.TestCase):
		def setUp(self):
			self.server = JsonRpcServer()

		def test_handle_request_invalid_request(self):
			expected = '{"jsonrpc": "2.0", "id": 4444, "error": {"message": "Invalid request", "code": -32600, "data": null}}'
			response = self.server.handle_request('{"id": 4444, "method": "rpc.something", "params": [null, {}]}')
			

# Generated at 2022-06-13 16:28:02.774511
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    test_method = 0
    def test_func(*args, **kwargs):
        global test_method
        test_method = 1
        return kwargs
    server.register(test_func)
    request = {'jsonrpc': '2.0', 'id': 1, 'method': 'test_func', 'params': {'arg': 'ok'}}
    result = server.handle_request(json.dumps(request))
    assert test_method == 1
    assert json.loads(result) == {'id':1, 'result':{'arg':'ok'}, 'jsonrpc':'2.0'}

if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:28:12.672205
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request_hello_world = b'{ \
            "jsonrpc": "2.0", \
            "id": null, \
            "method": "hello_world" \
        }'
    response_hello_world = b'{ \
            "id": null, \
            "jsonrpc": "2.0", \
            "result": "hello world" \
        }'
    assert server.handle_request(request_hello_world) == response_hello_world

    request_system_exit = b'{ \
            "jsonrpc": "2.0", \
            "id": null, \
            "method": "goodbye_world" \
        }'

# Generated at 2022-06-13 16:28:22.416061
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    class TestObject(object):
        def foo(self):
            return "bar"

    server = JsonRpcServer()
    server.register(TestObject())
    assert json.loads(server.handle_request(json.dumps({"jsonrpc": "2.0", "method": "foo", "params": [], "id": 0}))) == {"jsonrpc": "2.0", "result": "bar", "id": 0}
    assert json.loads(server.handle_request(json.dumps({"jsonrpc": "2.0", "method": "invalidmethod", "params": [], "id": 0}))) == {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 0}

# Generated at 2022-06-13 16:28:29.361351
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    import pickle

    srv = JsonRpcServer()

    setattr(srv, '_identifier', '123')

    result = {'id': '123', 'jsonrpc': '2.0', 'result': 'hello'}
    assert srv.response('hello') == result

    result['result'] = pickle.loads(result['result'])
    assert srv.response(pickle.dumps('hello')) == result

    delattr(srv, '_identifier')
    result = {'id': None, 'jsonrpc': '2.0', 'result': 'hello'}

    assert srv.response('hello') == result



# Generated at 2022-06-13 16:28:38.753414
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    import types

    result = None                                                                 # None
    json_rpc_server = JsonRpcServer()
    response = json_rpc_server.response(result=result)
    assert response == {'jsonrpc': '2.0', 'id': None, 'result': None}

    result = 'Hello World!'                                                       # String
    json_rpc_server = JsonRpcServer()
    response = json_rpc_server.response(result=result)
    assert response == {'jsonrpc': '2.0', 'id': None, 'result': 'Hello World!'}

    result = 123456789                                                            # Number
    json_rpc_server = JsonRpcServer()
    response = json_rpc_server.response(result=result)

# Generated at 2022-06-13 16:28:45.043936
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Test:
        def add(self, a, b=1):
            return a + b

    server = JsonRpcServer()
    server.register(Test())
    request = json.dumps({
        'id': 'test',
        'method': 'add',
        'params': [[1]]
    })
    response = server.handle_request(request)
    assert json.loads(response) == {
        'jsonrpc': '2.0',
        'id': 'test',
        'result': 2
    }

# Generated at 2022-06-13 16:28:51.043383
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import unittest
    import tempfile
    import os
    import shutil
    import copy
    import sys

    # Temporary fake class to handle the test request
    class FakeModule(object):
        def __init__(self, argument_spec):
            self.params = {}
            self.fail_json = None
            self.update = None
            self.deprecated = None
            self.argument_spec = argument_spec

            self.ansible_version = tempfile.mkdtemp()
            self.ansible_module_name = "sample"
            self.ansible_envvar_prefix = tempfile.mkdtemp()
            self.ansible_module_args = "mock=mock"
            self.ansible_facts = None
            self.ansible_diff = None
            self.ansible_ansible_version

# Generated at 2022-06-13 16:29:00.967666
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jr = JsonRpcServer

    # case 1
    request = '{"jsonrpc": "2.0", "method": "rpc.runcmds", "params": [[{"version": 1.2}]], "id": null}'

    # case 2
    # request = '{"jsonrpc": "2.0", "method": "rpc._hello", "params": [[{"version": 1.2}]], "id": null}'

    # case 3
    # request = '{"jsonrpc": "2.0", "method": "_hello", "params": [[{"version": 1.2}]], "id": null}'

    # case 4
    # request = '{"jsonrpc": "2.0", "method": "runcmds", "params": [[{"version": 1.2}]], "id":

# Generated at 2022-06-13 16:29:10.415630
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jsonrpc_server = JsonRpcServer()
    obj = DummyJsonRpcServer('obj')
    jsonrpc_server.register(obj)
    message =  {
        'jsonrpc': '2.0',
        'method': 'dummy_jsonrpc_method',
        'params': [],
        'id': '10'
    }
    message = json.dumps(message)
    response = jsonrpc_server.handle_request(message)
    assert isinstance(response, text_type)
    response = json.loads(response)
    assert response['jsonrpc'] == '2.0'
    assert response['id'] == '10'
    assert response['result'] == 'dummy_jsonrpc_method'

# Dummy class for jsonrpc_server.register()


# Generated at 2022-06-13 16:29:21.818148
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Arrange
    obj = JsonRpcServer()
    obj.register(JsonRpcServer)
    request = b'{"jsonrpc": "2.0", "method": "response", "params": [[], {}], "id": "1"}'

    # Act
    result = obj.handle_request(request)

    # Assert
    assert result == '{"jsonrpc": "2.0", "id": "1", "result": null}'

    # Arrange
    request = b'{"jsonrpc": "2.0", "method": "_response", "params": [[], {}], "id": "1"}'

    # Act
    result = obj.handle_request(request)

    # Assert

# Generated at 2022-06-13 16:29:25.439792
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection._jsonrpc import JsonRpcServer

    json_rpc = JsonRpcServer()
    json_rpc.handle_request('{"method":"test"}')


# Generated at 2022-06-13 16:29:33.171378
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import socket
    import ssl
    import sys

    display.verbosity = 4

    server_address = ('localhost', 10000)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(server_address)
    server.listen(1)

    # Always use SSL for test.
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    ssl_sock = context.wrap_socket(server, server_side=True)

    # class Foo contains a method
    class Foo(object):
        def test(self, foo):
            return foo

    foo = Foo()
    server = JsonRpcServer

# Generated at 2022-06-13 16:29:39.963754
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    obj = JsonRpcServer()
    obj._identifier = "foo"

    assert obj.response() == {'jsonrpc': '2.0', 'id': 'foo', 'result': None}

    assert obj.response([1]) == {'jsonrpc': '2.0', 'id': 'foo', 'result': '[1]'}
    assert obj.response([1,2,3]) == {'jsonrpc': '2.0', 'id': 'foo', 'result': '[1, 2, 3]'}


# Generated at 2022-06-13 16:29:49.691132
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import json

    server = JsonRpcServer()
    # valid request
    method = "rpc_sum"
    params = [[2, 3, 4], {'key1': 'val_1'}]
    id = 0
    valid_request = json.dumps({'method': method, 'params': params, 'id': id})
    valid_response = json.dumps({'result': 9, 'jsonrpc': '2.0', 'id': 0})
    assert server.handle_request(valid_request).decode("utf-8") == valid_response
    # invalid request (method does not exist)
    method = "invalid_method"
    params = [[2, 3, 4], {'key1': 'val_1'}]
    id = 0

# Generated at 2022-06-13 16:29:57.020706
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jrpc = JsonRpcServer()
    # test case #1
    request = '{"jsonrpc":"2.0","id":"0","method":"_debug","params":[]}'
    response = jrpc.handle_request(request)
    assert(response == '{"jsonrpc": "2.0", "id": "0", "error": {"code": -32600, "message": "Invalid request"}}')
    # test case #2
    request = '{"jsonrpc": "2.0", "method": "Test._debug", "params": [], "id": "1"}'
    response = jrpc.handle_request(request)

# Generated at 2022-06-13 16:30:00.047151
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    server._identifier = 'test_identifier'

    result = server.response('test_result')

    assert result == {
        'jsonrpc': '2.0',
        'id': 'test_identifier',
        'result': 'test_result'
    }


# Generated at 2022-06-13 16:30:09.059734
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    from ansible.module_utils.network.cliconf import CliConf
    j = JsonRpcServer()

    obj = CliConf(device_config=dict(host='1.1.1.1', port=22))
    obj.send = lambda *args, **kwargs: 'baba'
    j.register(obj)

    m = 'rpc.run_commands'
    request = json.dumps({
        'jsonrpc': '2.0',
        'id': 'test_id',
        'method': m,
        'params': [[], {}]
    })

    response = j.handle_request(request)
    response = json.loads(response)
    assert response.get('id') == 'test_id'
    assert response.get('result') == 'baba'

# Generated at 2022-06-13 16:30:17.070926
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import requests
    
    class A(object):
        def f1(self, num):
           return num
    server = JsonRpcServer()
    server.register(A())
    a = A()

    request_id = 1
    params = [1]

    payload = {
        "jsonrpc": "2.0", 
        'id': request_id,
        "method": "f1", 
        "params": params
    }

    response = server.handle_request(json.dumps(payload))
    response = json.loads(response)
    assert response['result'] == 1

test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:30:23.305908
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    rpcserver = JsonRpcServer()
    request = {'method': '_mymethod'}
    result = rpcserver.handle_request(request)

    assert result == '{"error": {"data": null, "code": -32600, "message": "Invalid request"}, "id": null, "jsonrpc": "2.0"}'


# Generated at 2022-06-13 16:30:32.188323
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    test_data = {'test':'data'}
    pickled_data = cPickle.dumps(test_data, protocol=0)
    response = JsonRpcServer().response(test_data)
    assert(response['id'] == None)
    assert(response['jsonrpc'] == '2.0')
    assert(response['result'] == pickled_data.decode())
    assert(response['result_type'] == 'pickle')

# Generated at 2022-06-13 16:30:38.378621
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    '''
    Test JsonRpc method response
       Args:   None
       Returns: None
    '''
    try:
        json_rpc_server = JsonRpcServer()
        response = json_rpc_server.response(None)
        assert type(response) == dict
    except Exception:
        display.vvv(traceback.format_exc())
        assert False



# Generated at 2022-06-13 16:30:45.425366
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import json

    server = JsonRpcServer()

    # JSON RPC 1.0
    request = {
        'method': 'unsupported',
        'params': [],
        'id': 1
    }

    response = server.handle_request(json.dumps(request))

    expected = {
        'id': 1,
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found',
            'data': None
        }
    }

    assert json.loads(response) == expected

    # JSON RPC 2.0
    request = {
        'method': 'unsupported',
        'params': [],
        'id': 'rpc_call'
    }


# Generated at 2022-06-13 16:30:51.354326
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    json_rpc_server = JsonRpcServer()
    json_rpc_server._identifier = 1
    result = json_rpc_server.response("Hello World")
    assert result == {'jsonrpc': '2.0', 'id': 1, 'result': 'Hello World'}


# Generated at 2022-06-13 16:31:00.508044
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request_mock = json.dumps({
        "jsonrpc": "2.0",
        "method": "run",
        "id": "123",
        "params": [["ansible_playbook"], {
            "-i": "ansible-inventory",
            "-e": "ansible_user=vagrant",
            "-e": "ansible_port=2222",
            "-e": "ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key",
        }]
    })
    response_mock = json.dumps({"id": "123", "jsonrpc": "2.0", "result": "started"})

    server = JsonRpcServer()
    server.register(server)
    assert server.handle_request(request_mock) == response_

# Generated at 2022-06-13 16:31:10.157068
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import json
    from ansible.module_utils.connection import Connection, ConnectionError

    class JsonRpcServerTest:
        #Test case 1: raise exception when method is not found
        def test_case1(self, request):
            jsonserver = JsonRpcServer()
            jsonserver.register(self)
            result = jsonserver.handle_request(request)
            response = json.loads(result)
            assert 'error' in response
            assert response['error']['code'] == -32601
            assert response['error']['message'] == 'Method not found'
        #Test case 2: raise exception when invalid_request
        def test_case2(self, request):
            jsonserver = JsonRpcServer()
            jsonserver.register(self)
            result = jsonserver.handle_request

# Generated at 2022-06-13 16:31:15.806881
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    mc = JsonRpcServer()
    mc.register(display)
    request1 = json.dumps({'method': 'vvvv', 'params': [[]], 'id': 1})
    request2 = json.dumps({'method': 'vvv', 'params': [[]], 'id': 1})
    request3 = json.dumps({'method': 'display', 'params': [[]], 'id': 1})
    request4 = json.dumps({'method': '_display', 'params': [[]], 'id': 1})
    request5 = json.dumps({'method': 'rpc.display', 'params': [[]], 'id': 1})
    request6 = json.dumps({'method': 'v', 'params': [[]], 'id': 1})
    response1 = mc.handle_request(request1)

# Generated at 2022-06-13 16:31:23.290379
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    server.register(display)
    display.verbosity = 0

    data = {
        "jsonrpc": "2.0", 
        "method": "display", 
        "params":("show something", "always"), 
        "id": 1
    }
    output = server.handle_request(data)
    print("output=",output)

if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:31:30.816879
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.basic import AnsibleModule
    # create server
    server = JsonRpcServer()
    # create module
    args = {}
    kwargs = {}
    module = AnsibleModule(argument_spec=args, **kwargs)
    # register module in server
    server.register(module)
    # create message
    request = {'id': '1', 'method': 'test', 'params': [[], {}]}
    # call handle_request
    response = server.handle_request(json.dumps(request))
    assert response == '{"jsonrpc": "2.0", "id": "1", "result": "hello world"}'
    # create invalid message
    request = {'id': '1', 'method': 'test', 'params': [[], {}]}
    # call handle_request

# Generated at 2022-06-13 16:31:40.069026
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jsonrpc = JsonRpcServer()
    # pass a valid request
    request = b'{"jsonrpc": "2.0", "method": "valid.method", "params": [1, 2], "id": 1}'
    resp = jsonrpc.handle_request(request)
    resp = json.loads(resp)
    assert resp['jsonrpc'] == '2.0'
    assert resp['id'] == 1
    assert resp['result'] == b'(lp0\nI1\naI2\na.'
    # pass a method not found request
    request = b'{"jsonrpc": "2.0", "method": "invalid.method", "params": [1, 2], "id": 1}'
    resp = jsonrpc.handle_request(request)

# Generated at 2022-06-13 16:31:48.691274
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    print(server.response())
    print(server.response(result='This is a test.'))



# Generated at 2022-06-13 16:31:56.333896
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Arrange
    server = JsonRpcServer()
    # set up class
    class dummy_class:
        def test_method(self):
            return "test method"

    # register dummy class
    server.register(dummy_class())

    # create request
    param = {
        "jsonrpc": "2.0",
        "method": "test_method",
        "params": [],
        "id": 1
    }
    request = json.dumps(param)

    # Act
    response = server.handle_request(request)
    # Assert
    # check if response contains error
    assert json.loads(response)["result"] == "test method"



# Generated at 2022-06-13 16:32:00.919151
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    json_rpc_server = JsonRpcServer()
    setattr(json_rpc_server, '_identifier', 1)
    result = {'a': 1, 'b': 2}
    response = json_rpc_server.response(result)
    assert response.get('result_type') == 'pickle'
    assert response.get('result') == to_text(cPickle.dumps(result, protocol=0))


# Generated at 2022-06-13 16:32:08.731670
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = '{"jsonrpc": "2.0", "method": "ping", "params": [], "id": 1}'
    response = '{"id": 1, "jsonrpc": "2.0"}'
    result = server.handle_request(request)
    print(result)
    assert result == response, "test_handle_request failed"

if __name__ == "__main__":
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:32:12.424397
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    json_rpc_server = JsonRpcServer()
    request = '{"params": [[1, 2], {"hello": "world"}], "jsonrpc": "2.0", "id": 1, "method": "test"}'
    response = json_rpc_server.handle_request(request)

    assert response == '{"error":{"code":-32601,"message":"Method not found"},"id":1,"jsonrpc":"2.0"}'

# Generated at 2022-06-13 16:32:18.986760
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Math(object):
        def add(self, x, y):
            return x + y

        def subtract(self, x, y):
            return x - y

        def multiply(self, x, y):
            return x * y

        def divide(self, x, y):
            return x / y

    test_count = 0
    server = JsonRpcServer()
    server.register(Math())
    print('valid_method')
    request = '{"jsonrpc": "2.0", "method": "add", "params": [1, 2], "id": "1"}'
    response = '{"jsonrpc": "2.0", "result": 3, "id": "1"}'
    result = server.handle_request(request)
    if result == response:
        print("PASS")

# Generated at 2022-06-13 16:32:27.588360
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Initialize the class
    json_rpc_server = JsonRpcServer()

    # Check for invalid request
    request = '{"jsonrpc": "2.0", "method": "foo.bar", "params": {"arg1": 2, "arg2": "value"}, "id": 2}'
    expected_response = '{"jsonrpc": "2.0", "id": 2, "error": {"code": -32600, "message": "Invalid request", "data": null}}'
    result = json_rpc_server.handle_request(request)
    assert result == expected_response

# Generated at 2022-06-13 16:32:34.780079
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    server._objects = set([server])
    request = """
    {
        "jsonrpc": "2.0",
        "method": "test",
        "params": [],
        "id": 42
    }
    """
    response = server.handle_request(request)
    assert response == '{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 42}'
    server.test = lambda : 'something'
    response = server.handle_request(request)
    assert response == '{"jsonrpc": "2.0", "id": 42, "result": "something"}'



# Generated at 2022-06-13 16:32:40.921490
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    from ansible.module_utils import basic

    server = JsonRpcServer()
    server.register(basic)


# Generated at 2022-06-13 16:32:49.990137
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    class DummyClass(object):
        def func_test(self):
            pass
    class DummyClass2(object):
        def func_test2(self):
            pass
    class DummyClass3(object):
        def func_test3(self, *args, **kwargs):
            return kwargs
    class DummyClass4(object):
        def func_test4(self, *args, **kwargs):
            return args


# Generated at 2022-06-13 16:33:04.969920
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = json.loads('{ "jsonrpc": "2.0", "method": "foobar", "params": [], "id": 1 }')
    assert server.handle_request('{ "jsonrpc": "2.0", "method": "foobar", "params": [], "id": 1 }') == json.dumps(
        {"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found"}})



# Generated at 2022-06-13 16:33:11.376626
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_test = '{"method": "get_config", "params": [[], {"file_name": "test_file"}], "id": "CISCO-CONFIG-MAN-MIB::ccmHistoryRunningLastChanged.0"}'
    jr = JsonRpcServer()
    assert json.dumps(jr.handle_request(json_test)) == '{"jsonrpc": "2.0", "id": "CISCO-CONFIG-MAN-MIB::ccmHistoryRunningLastChanged.0", "error": {"code": -32601, "message": "Method not found"}}'

# Generated at 2022-06-13 16:33:17.320992
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = json.dumps({
        "jsonrpc": "2.0",
        "method": "rpc.run",
        "params": ["show version"],
        "id": 5
    })
    response = server.handle_request(request)
    assert response == '{"jsonrpc": "2.0", "id": 5, "error": {"code": -32601, "message": "Method not found"}}'

# Generated at 2022-06-13 16:33:21.390137
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    rpc = JsonRpcServer()
    rpc.register(rpc)

    rpc.handle_request('{"jsonrpc": "2.0", "method": "response", "params": [], "id": 1}')
    rpc.handle_request('{"jsonrpc": "2.0", "method": "response", "params": [], "id": "foo"}')

# Generated at 2022-06-13 16:33:27.325990
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    req = '{"id": "id", "method": "echo", "params": ["aaa"]}'
    req = cPickle.dumps(req, protocol=0)
    m_request = to_text(req, errors='surrogate_then_replace')

    svr = JsonRpcServer()
    result = svr.handle_request(m_request)
    assert result == '{"id": "id", "result": "aaa", "jsonrpc": "2.0"}'

# Generated at 2022-06-13 16:33:28.360959
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # TODO: update JsonRpcServer_handle_request()
    pass

# Generated at 2022-06-13 16:33:34.022231
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    jrs = JsonRpcServer()
    setattr(jrs, '_identifier', 23)
    ret = jrs.response()
    assert isinstance(ret, dict)
    assert ret['jsonrpc'] == '2.0'
    assert ret['id'] == 23
    assert ret.get('result') is None
    assert ret.get('result_type') is None
    assert ret.get('error') is None

    ret = jrs.response(123)
    assert isinstance(ret, dict)
    assert ret['jsonrpc'] == '2.0'
    assert ret['id'] == 23
    assert ret['result'] == '123'
    assert ret.get('result_type') is None
    assert ret.get('error') is None

    # Python 3 will send byte str

# Generated at 2022-06-13 16:33:44.013825
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import os
    import sys
    import mock

    class MyTest:
        def __init__(self):
            pass

        def rpc_method(self, params):
            return params

    class TestResult:
        def __init__(self, data):
            self.data = data

    test = MyTest()
    server = JsonRpcServer()
    server.register(test)

    method = 'rpc_method'
    params = 'myparam'
    data = {'id': 1, 'method': method, 'params': [params]}
    data = json.dumps(data)

    # test_run should be called with param (method, args, kwargs)
    expected_result = TestResult(params)
    # Test case 1

# Generated at 2022-06-13 16:33:55.725079
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    # returns a JsonRPC-Response-Object

# Generated at 2022-06-13 16:34:03.834003
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # initialize a JsonRpcServer object
    server = JsonRpcServer()

    # test if the object is of type JsonRpcServer
    assert isinstance(server, JsonRpcServer)

    # test method response with a dictionary as argument
    result = {'msg': 'this is a test'}
    response = server.response(result)
    assert response['result'] == result
    assert response['id'] == None

    # test method response with a str as argument
    result = "this is another test"
    response = server.response(result)
    assert response['result'] == result
    assert response['id'] == None



# Generated at 2022-06-13 16:34:27.942324
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()

    # This is a JsonRpcServer error
    request = '{"jsonrpc": "2.0", "method": "rpc.hello", "id": 1}'
    response = server.handle_request(request)
    assert json.loads(response) == {'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32600, 'message': 'Invalid request'}}

    # This is a JsonRpcServer error
    request = '{"jsonrpc": "2.0", "method": "_hello", "id": 1}'
    response = server.handle_request(request)

# Generated at 2022-06-13 16:34:37.301420
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    class TestServer(JsonRpcServer):
        pass

    server = TestServer()
    server._identifier = "test"

    assert server.response() == {'jsonrpc': '2.0', 'id': 'test', 'result': None}
    assert server.response("result") == {'jsonrpc': '2.0', 'id': 'test', 'result': 'result'}
    assert server.response(b"result") == {'jsonrpc': '2.0', 'id': 'test', 'result': 'result'}

# Generated at 2022-06-13 16:34:45.738629
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    rpcServer = JsonRpcServer()

# Generated at 2022-06-13 16:34:53.468661
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.nios import *
    from .compat import unittest
    from .compat.mock import patch, Mock

    from ansible.module_utils import nios

    mock_module = Mock()
    mock_module.params = dict(
        provider=dict(
            host='172.16.25.10',
            port=8081,
            username='admin',
            password='admin',
            server=None
        ),
        config_file='test.conf',
        state='present'
    )
    mock_module.check_mode = True


    class TestJsonRpcServer(unittest.TestCase):
        def setUp(self):
            self.jsonrpc_server = JsonRpcServer()
            self.nios = NIOSModule(mock_module)

# Generated at 2022-06-13 16:35:01.862037
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    # create a new object of the class under test
    server = JsonRpcServer()

    # create a dummy object of a class MyModule with a method "get_foobar()"
    class MyModule(object):
        def __init__(self):
            self.foobar = "bar"

        def get_foobar(self):
            return self.foobar

    # register the dummy object of MyModule
    server.register(MyModule())

    # create a valid json-rpc request for the method "get_foobar()"
    get_foobar_request = json.dumps({
        "method": "get_foobar",
        "params": [],
        "jsonrpc": "2.0",
        "id": 0,
    })

    # call the method under test