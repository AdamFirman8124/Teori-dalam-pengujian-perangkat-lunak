

# Generated at 2022-06-13 16:25:22.337415
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    obj = JsonRpcServer()
    setattr(obj, '_identifier', '1')
    response = obj.response()
    assert response == {
        'id': '1',
        'jsonrpc': '2.0',
        'result': None
    }
    response = obj.response('hello')
    assert response == {
        'id': '1',
        'jsonrpc': '2.0',
        'result': 'hello'
    }
    response = obj.response({'a': '1', 'b': '2'})
    assert response == {
        'id': '1',
        'jsonrpc': '2.0',
        'result': '{"a": "1", "b": "2"}',
        'result_type': 'pickle'
    }

# Unit test

# Generated at 2022-06-13 16:25:30.237264
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import pytest
    from ansible.errors import AnsibleConnectionFailure
    from ansible.module_utils.basic import AnsibleModule

    class DummyJsonRpcServer(JsonRpcServer):
        pass
    test_module = AnsibleModule(argument_spec=dict())
    test_module.test_jrpc_server = DummyJsonRpcServer()
    test_module.test_jrpc_server.register(test_module)

    def a_method(*args, **kwargs):
        return {"result": "a_method_returned_message", "additional_key": "value"}
    test_module.a_method = a_method

    def b_method(*args, **kwargs):
        raise AnsibleConnectionFailure("my database is unavailabe right now.")

    test_module.b_

# Generated at 2022-06-13 16:25:35.806869
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    result = {'test': False}
    obj = JsonRpcServer()
    obj._identifier = 'test_unit'
    response = obj.response(result)
    assert response['jsonrpc'] == '2.0'
    assert response['id'] == 'test_unit'
    assert json.dumps(response['result']) == '{"test":false}'



# Generated at 2022-06-13 16:25:37.549297
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass


# Generated at 2022-06-13 16:25:41.146730
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    error = server.error(code=2, message="test error message")
    expected_error = {'jsonrpc': '2.0', 'id': None, 'error': {'code': 2, 'message': "test error message"}}
    assert error == expected_error


# Generated at 2022-06-13 16:25:45.778729
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    test_obj = JsonRpcServer()
    test_obj.register(JsonRpcServer())

    # data deconstruction
    attr_id = '1234567890'
    setattr(test_obj, '_identifier', attr_id)

    # unit test
    result = test_obj.response(result={"value": "test"})

    # result processing
    assert result['id'] == attr_id
    assert result['jsonrpc'] == '2.0'
    assert result['result'] == cPickle.dumps({"value": "test"}, protocol=0)
    assert result['result_type'] == 'pickle'

    delattr(test_obj, '_identifier')

# Generated at 2022-06-13 16:25:58.094189
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    setattr(server, '_identifier', 'testid')
    result = {"test_key":"test_value"}
    response = server.response(result)
    assert(response["jsonrpc"] == '2.0')
    assert(response["id"] == 'testid')
    assert(response["result"] == '{"test_key": "test_value"}')
    assert(response["result_type"] == "json")
    result = {"test_key":to_text("binary_string","utf-8")}
    response = server.response(result)
    assert(response["result"] == '{"test_key": "binary_string"}')
    assert(response["result_type"] == "json")
    result = to_text("binary_string","utf-8")

# Generated at 2022-06-13 16:25:59.722048
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    assert JsonRpcServer().error('code', 'message', 'data') == {'id': None, 'jsonrpc': '2.0', 'error': {'code': 'code', 'message': 'message', 'data': 'data'}}

# Generated at 2022-06-13 16:26:04.501194
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    class MockObj(object):

        @staticmethod
        def hello(*args, **kwargs):
            pass

    obj = MockObj()

    server = JsonRpcServer()
    server.register(obj)

    response = server.handle_request('{"jsonrpc": "2.0", "method": "hello", "id": "test", "params": []}')
    response = json.loads(response)

    assert response == {'jsonrpc': '2.0', 'id': 'test', 'result': 'None'}


# Generated at 2022-06-13 16:26:09.618050
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    jsonrpc = JsonRpcServer()
    jsonrpc._identifier = "abcd1234"
    result = jsonrpc.error(code=5, message="Error")
    assert result == {'jsonrpc': '2.0', 'id': 'abcd1234', 'error': {'code': 5, 'message': 'Error'}}

# Generated at 2022-06-13 16:26:26.357704
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.plugins.connection.json_rpc import MyConnection
    from ansible.plugins.connection import ConnectionBase

    conn = MyConnection()
    server = JsonRpcServer()
    server.register(conn)
    content = '{"jsonrpc": "2.0", "method": "execute", "params": [["ls", "-l"]], "id": 1}'
    contents = '{"jsonrpc": "2.0", "method": "execute", "params": [["ls", "-l"]], "ids": 1}'
    response = server.handle_request(content)
    expected = '{"jsonrpc": "2.0", "id": 1, "result": "result of execute"}'

# Generated at 2022-06-13 16:26:36.304458
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request1 = json.dumps({
        'jsonrpc': '2.0',
        'method': 'rpc.method',
        'id': 3
    })
    request2 = json.dumps({
        'jsonrpc': '2.0',
        'method': '_internal_method',
        'id': 3
    })
    request3 = json.dumps({
        'jsonrpc': '2.0',
        'method': 'non_existent_method',
        'id': 3
    })

    class DummyClass():
        def test():
            return 'success'

    dummy_instance = DummyClass()
    server = JsonRpcServer()
    server.register(dummy_instance)

    response = server.handle_request(request1)
    response = json.loads(response)


# Generated at 2022-06-13 16:26:40.977039
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():

    jsonrpc_server = JsonRpcServer()
    setattr(jsonrpc_server, '_identifier', 4)
    result = {'msg':'Hello'}
    response = jsonrpc_server.response(result)
    jsonrpc = "2.0"
    assert response['jsonrpc'] == jsonrpc

# Generated at 2022-06-13 16:26:45.795572
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.json_rpc import JsonRpcServer

    server = JsonRpcServer()
    request = '{"jsonrpc": "2.0", "method": "test", "params": [{"key": "value"}], "id": 1}'
    response = server.handle_request(request)
    assert response == '{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 1}'

# Generated at 2022-06-13 16:26:56.928236
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Test with an invalid request
    requestdata = b'{"jsonrpc": "2.0", "method": "rpc.test", "params": [1]}'
    proxy = JsonRpcServer()
    response = proxy.handle_request(requestdata)
    assert json.loads(response)['error']['code'] == -32600
    requestdata = b'{"jsonrpc": "2.0", "method": "_test", "params": [1]}'
    proxy = JsonRpcServer()
    response = proxy.handle_request(requestdata)
    assert json.loads(response)['error']['code'] == -32600

    # Test with an valid request to an unwrapped method

# Generated at 2022-06-13 16:27:02.786375
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    """
    JsonRpcServer is a JSON RPC 2.0 server that handles requests and
    returns a response
    """

    server = JsonRpcServer()
    request = '{"jsonrpc": "2.0", "method": "echo", "params": ["echo"], "id": 1}'
    returned = server.handle_request(request)
    assert returned, '{"jsonrpc": "2.0", "result": "echo", "id": 1}'

# Generated at 2022-06-13 16:27:03.370824
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass

# Generated at 2022-06-13 16:27:10.279138
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jsonrpc_request = '{"jsonrpc": "2.0", "method": "rpc.echo", "params": {"001": 123}}'
    jsonrpc_server = JsonRpcServer()
    print(jsonrpc_server.handle_request(jsonrpc_request))
    jsonrpc_request = '{"jsonrpc": "2.0", "method": "_echo", "params": {"001": 123}}'
    jsonrpc_server = JsonRpcServer()
    print(jsonrpc_server.handle_request(jsonrpc_request))
    jsonrpc_request = '{"jsonrpc": "2.0", "method": "echo", "params": {"001": 123}}'
    jsonrpc_server = JsonRpcServer()

# Generated at 2022-06-13 16:27:16.427915
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    test_server = JsonRpcServer()
    test_server.handle_request('{"jsonrpc":"2.0", "method":"_run", "params":[[{"name":"R1","port":22,"passwd":"lab123"}], {"task": {"name":"config replace", "src":"R1_new.cfg"}}], "id":0}')

if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:27:26.470615
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # test the json rpc parse error
    request = 'request'
    server = JsonRpcServer()
    result = server.handle_request(request)
    assert result == '{"jsonrpc": "2.0", "id": null, "error": {"code": -32700, "message": "Parse error"}}'

    # test the json rpc invalid_request error
    request = '{"jsonrpc": "2.0", "method": "foobar", "params": "bar", "baz]'
    server = JsonRpcServer()
    result = server.handle_request(request)
    assert result == '{"jsonrpc": "2.0", "id": null, "error": {"code": -32600, "message": "Invalid request"}}'
    # test the json rpc method not found exception
   

# Generated at 2022-06-13 16:27:41.704993
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    
    # Unit test for method handle_request of class JsonRpcServer
    # Set the results of the class methods that are called in the method
    # handle_request, mock_json and mock_json_dumps
    JsonRpcServer.header = lambda self: {'jsonrpc': '2.0', 'id': self._identifier, 'result': 'test'}
    JsonRpcServer.error = lambda self, code, message, data=None: {'code': 1, 'message': 'test_error', 'data': 'test_data'}
    JsonRpcServer.method_not_found = lambda self, data=None: '{"code":"-32601","message":"Method not found"}'

# Generated at 2022-06-13 16:27:51.448350
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from mock import Mock
    from mock import call

    class TestClass():
        def test_method(self, test_arg):

            fake_result = {'arg': test_arg}
            return fake_result

    test_server = JsonRpcServer()
    test_server.register(TestClass())

    test_request = {
        "jsonrpc": "2.0",
        "method": "test_method",
        "params": {
            "args": [
                "test argument"
            ],
            "kwargs": {}
        },
        "id": "1"
    }

    expected_response = {
        "jsonrpc": "2.0",
        "result": {
            "arg": "test argument"
        },
        "id": "1"
    }

    #import pdb;

# Generated at 2022-06-13 16:28:02.309745
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    class TestJsonRpcServer(JsonRpcServer):
        def test(self):
            return {'a': 'b', 'c': 42}
        def _private(self):
            return {'a': 'b', 'c': 42}

    j = TestJsonRpcServer()

    assert j.response() == {
        'jsonrpc': '2.0',
        'id': None,
        'result': None,
    }

    assert j.response(1) == {
        'jsonrpc': '2.0',
        'id': None,
        'result': '1',
    }

    assert j.response(b'hi') == {
        'jsonrpc': '2.0',
        'id': None,
        'result': 'hi',
    }

    assert j.response

# Generated at 2022-06-13 16:28:07.478616
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jrpc = JsonRpcServer()
    request = b'{"jsonrpc": "2.0", "method": "hello", "params": [], "id": 1}'
    response = b'{"jsonrpc":"2.0","error":{"code":-32601,"message":"Method not found"},"id":1}'
    assert jrpc.handle_request(request) == response

# Generated at 2022-06-13 16:28:18.063079
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    server = JsonRpcServer()

    # test with invalid request
    result = server.handle_request('{"jsonrpc": "2.0"}')
    json_result = json.loads(result)
    assert json_result['error']['code'] == -32600

    # test with invalid jsonrpc version
    result = server.handle_request('{"jsonrpc": "1.0", "method": "test"}')
    json_result = json.loads(result)
    assert json_result['error']['code'] == -32600

    # test with method call
    result = server.handle_request('{"jsonrpc": "2.0", "method": "test", "id": 1}')
    json_result = json.loads(result)
    assert json_result['error']['code'] == -326

# Generated at 2022-06-13 16:28:28.401863
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    class TestClass:
        def test_handle_request(self, key, value):
            return {key: value}

    json_rpc_server = JsonRpcServer()
    json_rpc_server.register(TestClass())
    request = '{"jsonrpc": "2.0", "method": "test_handle_request", "params": ["instance", "MSS"], "id": 1}'

    result = json_rpc_server.handle_request(request)
    assert result == '{"id": 1, "jsonrpc": "2.0", "result": {"instance": "MSS"}}'

    request = '{"jsonrpc": "2.0", "method": "test_handle_request", "params": ["asdf", "MSS"], "id": 1}'

    result = json_rpc_

# Generated at 2022-06-13 16:28:34.208406
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # pylint: disable=line-too-long
    server = JsonRpcServer()
    assert json.loads(server.handle_request(b'{"id":1,"params":["arg1","arg2"],"method":"test"}')) == {"id": 1, "jsonrpc": "2.0", "result": "test"}

# Generated at 2022-06-13 16:28:42.136782
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jrs = JsonRpcServer()
    request = b"""{
    "jsonrpc": "2.0",
    "method": "run_command",
    "params": ["show clock"],
    "id": "1"
    }"""
    response = b"""{
    "jsonrpc": "2.0",
    "result": "Mon Jun 12 15:20:24.742 UTC\n",
    "id": "1"
    }"""
    print(jrs.handle_request(request))
    assert jrs.handle_request(request) == response



# Generated at 2022-06-13 16:28:46.068243
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = {'method': 'echo', 'params': [1, 2], 'id': 1}
    request = json.dumps(request)

    result = server.handle_request(request)
    result = json.loads(result)

    assert result['id'] == 1
    assert result['result'] == [1, 2]



# Generated at 2022-06-13 16:28:49.157710
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    rpc_server = JsonRpcServer()
    request = json.loads('{"jsonrpc": "2.0", "method": "run", "id": "1"}')
    response = json.loads(rpc_server.handle_request(json.dumps(request)))
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == "1"

# Generated at 2022-06-13 16:28:59.701276
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = {'method': 'get_connection', 'id': 2, 'params': [[], {}]}
    request = json.dumps(request)
    result = server.handle_request(request)
    response = json.loads(result)
    assert response["id"] == 2
    assert response["error"] == {"code": -32601, "message": "Method not found"}


# Generated at 2022-06-13 16:29:07.418205
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc_client = JsonRpcServer()

    request = {
        "jsonrpc": "2.0",
        "method": "echo",
        "id": "1",
        "params": ["Hello, World!"]
    }
    response = json_rpc_client.handle_request(request)


if __name__ == "__main__":
    test_JsonRpcServer_handle_request()

# vim: ai et ts=4 sw=4 sts=4 ft=python

# Generated at 2022-06-13 16:29:17.231407
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    def test_func(*args, **kwargs):
        return 1

    jrs = JsonRpcServer()
    jrs.register(test_func)

    request = {}
    request['id'] = 1
    request['method'] = 'test_func'
    request['params'] = [['test'], {'test': 'test'}]
    request_str = json.dumps(request)

    response = jrs.handle_request(request_str)
    result = json.loads(response)
    assert result.get('result') == '1'


if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:29:22.260319
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = '{"method": "hello", "params": [1], "id" : 1}'
    server.handle_request(request)

# Generated at 2022-06-13 16:29:31.215292
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    # data is the JSON-RPC request
    data = json.dumps({
        'jsonrpc': '2.0',
        'method': 'test_method',
        'params': [],
        'id': 327
    })

    # server is an instance of the jrpclib.JsonRpcServer class
    server = JsonRpcServer()

    # TODO: Mock the method test_method

    response = server.handle_request(data)
    response = json.loads(response)

    assert set(response.keys()) == set(['jsonrpc', 'result', 'id'])
    assert response['id'] == 327
    assert response['jsonrpc'] == '2.0'
    assert response['result'] == None


# Generated at 2022-06-13 16:29:34.737067
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = '{"jsonrpc": "2.0", "method": "test", "params": [1,2], "id": 1}'
    response = server.handle_request(request)
    assert response == '{"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found"}}'


# Generated at 2022-06-13 16:29:46.468194
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    s = JsonRpcServer()
    r = s.handle_request('{"method": "get_connection", "params": [], "id": "id"}')
    assert r == '{"id": "id", "result": "{\\"host\\": \\"localhost\\", \\"port\\": 22}", "jsonrpc": "2.0"}'
    r = s.handle_request('{"method": "get_connection", "params": [], "id": "id"}')
    assert r == '{"id": "id", "result": "{\\"host\\": \\"localhost\\", \\"port\\": 22}", "jsonrpc": "2.0"}'
    r = s.handle_request('{"method": "get_connection", "params": [], "id": "id"}')

# Generated at 2022-06-13 16:29:55.157861
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    rpc_server = JsonRpcServer()
    rpc_server._identifier = 'test-id'
    response = rpc_server.response()
    assert response['jsonrpc'] == '2.0'
    assert response['id'] == 'test-id'
    assert response['result'] == None
    assert response['result_type'] == None

    response = rpc_server.response('test-result')
    assert response['jsonrpc'] == '2.0'
    assert response['id'] == 'test-id'
    assert response['result'] == 'test-result'
    assert response['result_type'] == None

    result = dict()
    response = rpc_server.response(result)
    assert response['jsonrpc'] == '2.0'

# Generated at 2022-06-13 16:29:57.284719
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    assert JsonRpcServer().response({'foo': 'bar'}) == {'jsonrpc': '2.0', 'id': 'None', 'result': {'foo': 'bar'}}

# Generated at 2022-06-13 16:30:05.760352
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.six import PY3

    class TestClass(object):
        def __init__(self, *args, **kwargs):
            self.connection = Connection(*args, **kwargs)
            self.call = self.connection.call

    server = JsonRpcServer()
    obj = TestClass('local')

    # method that returns a string responses
    method = 'get_config'
    args, kwargs = (), {}
    expected = {'jsonrpc':'2.0', 'result': '', 'id': 0}
    result = server.response(obj.call(method, *args, **kwargs))
    assert result == expected

    # method that returns a dictionary (json does not support complex objects)

# Generated at 2022-06-13 16:30:18.347674
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # Tests for successful response
    assert JsonRpcServer().response() == {'jsonrpc': '2.0', 'id': None, 'result': None}
    assert JsonRpcServer().response(result="hello") == {'jsonrpc': '2.0', 'id': None, 'result': 'hello'}
    assert JsonRpcServer().response(result=True) == {'jsonrpc': '2.0', 'id': None, 'result': True}
    assert JsonRpcServer().response(result=False) == {'jsonrpc': '2.0', 'id': None, 'result': False}
    assert JsonRpcServer().response(result=1234) == {'jsonrpc': '2.0', 'id': None, 'result': 1234}
    assert JsonRpcServer

# Generated at 2022-06-13 16:30:27.634056
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    result = server.response()
    assert result == {
        'jsonrpc': '2.0',
        'id': None,
        'result': 'None'
    }
    result = server.response(1)
    assert result == {
        'jsonrpc': '2.0',
        'id': None,
        'result': '1'
    }
    result = server.response('hello')
    assert result == {
        'jsonrpc': '2.0',
        'id': None,
        'result': 'hello'
    }
    result = server.response(True)
    assert result == {
        'jsonrpc': '2.0',
        'id': None,
        'result': 'True'
    }

# Generated at 2022-06-13 16:30:30.111311
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
  import pprint
  pp = pprint.PrettyPrinter(indent=2)
  pp.pprint(JsonRpcServer().handle_request(request))

# Generated at 2022-06-13 16:30:30.970291
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
  import unittest


# Generated at 2022-06-13 16:30:35.502214
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    test_request = '{"jsonrpc": "2.0", "method": "run_command", "params": [[0,0]], "id": 1}'
    assert server.handle_request(test_request) == '{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 1}'

# Generated at 2022-06-13 16:30:44.053680
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import json
    server = JsonRpcServer()

    class Methods(object):

        def run(self):
            return {'test': 'run'}

    server.register(Methods())
    request = {'jsonrpc': '2.0', 'id': 1, 'method': 'run'}
    message = json.dumps(request)
    result = json.loads(server.handle_request(message))
    assert result.get('jsonrpc') == '2.0'
    assert result.get('id') == 1
    assert result.get('result') == {'test': 'run'}
    assert 'error' not in result

    def test():
        raise ValueError('test')

    request = {'jsonrpc': '2.0', 'id': 1, 'method': 'test'}

# Generated at 2022-06-13 16:30:53.459141
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = {
        'jsonrpc': '2.0',
        'method': 'rpc.test',
        'params': {
            'args': [5, 9],
            'kwargs': {'a': 1, 'b': 2}
        },
        'id': 1
    }
    request = json.dumps(request)
    result = server.handle_request(request=request)
    result = json.loads(result)

    assert 'Parse error' in result['error']['message']
    assert result['error']['code'] == -32700
    assert 'json_response' in result['error']['data']

# Generated at 2022-06-13 16:30:57.886720
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    display.display(u'starting test')
    myserver = JsonRpcServer()
    setattr(myserver, '_identifier', u'1')
    response = myserver.response({'a': 1})
    display.display(response)
    assert response == {'jsonrpc': '2.0', 'id': u'1', 'result': {'a': 1}}

# Generated at 2022-06-13 16:31:03.588517
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = {'jsonrpc': '2.0', 'method': 'test', 'params': [1, 2], 'id': 0}
    request = json.dumps(request)
    with pytest.raises(AttributeError):
        server.handle_request(request)


# Generated at 2022-06-13 16:31:12.111545
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    test_JsonRpcServer_handle_request.test_server = server

    # Failing to provide any request method
    request = {
        'jsonrpc': '2.0',
        'id': 'test-id'}
    expected_response = {
        'id': 'test-id',
        'jsonrpc': '2.0',
        'error': {
            'code': -32600,
            'data': None,
            'message': 'Invalid request'
        }
    }
    response = json.loads(server.handle_request(request))
    assert expected_response == response

    # Using a system RPC method

# Generated at 2022-06-13 16:31:26.197952
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    #setup
    jsonRpcServer = JsonRpcServer()
    #test
    result = jsonRpcServer.handle_request(json.dumps({'jsonrpc': '2.0', 'method': '_test', 'params': [], 'id': 1}))
    #verify:
    assert result == json.dumps({'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32601, 'message': 'Method not found'}})

    #setup
    jsonRpcServer = JsonRpcServer()
    #test
    result = jsonRpcServer.handle_request(json.dumps({'jsonrpc': '2.0', 'method': 'rpc._test', 'params': [], 'id': 1}))
    #verify:
    assert result == json

# Generated at 2022-06-13 16:31:33.945676
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class MockedObj(object):
        def __init__(self, name):
            self.name = name
    test_obj = MockedObj("MyMockedObject")
    test_server = JsonRpcServer()
    test_server.register(test_obj)
    test_server.handle_request("""{
                                    "jsonrpc": "2.0",
                                    "method": "name",
                                    "params": [],
                                    "id": 0
                                }""")


# Generated at 2022-06-13 16:31:41.276952
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    jrs = JsonRpcServer()

    class TestClass(object):

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def sum(self, z):
            return self.x + self.y + z

        def diff(self, z):
            return self.x + self.y - z

    request = {'jsonrpc': '2.0', 'method': 'sum', 'params': [3], 'id': '123'}
    response = {'jsonrpc': '2.0', 'id': '123', 'result': 10}

    tc1 = TestClass(5, 5)
    jrs.register(tc1)

    assert jrs.handle_request(json.dumps(request)) == json.dumps(response)


# Generated at 2022-06-13 16:31:50.734963
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.parsing.ajson import AnsibleJSONEncoder
    import json

    server = JsonRpcServer()
    server.header = lambda: {}

    def hello(text):
        return "hello %s" % text

    def bye():
        return "bye"

    def echo(text):
        return text

    def fail():
        raise ValueError("failed")

    server.register(hello)
    server.register(bye)
    server.register(echo)
    server.register(fail)

    def serialize(obj):
        return json.dumps(obj, cls=AnsibleJSONEncoder)

    def handle_request(request):
        return server.handle_request(serialize(request))


# Generated at 2022-06-13 16:31:57.015003
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # The method handle_request is called by the server.
    # The following test is for unit testing only.
    # Data for the request
    server = JsonRpcServer()

    request = {"method":"sum_two_numbers","params":[34,2],"id":1}
    request_json_bytes = json.dumps(request).encode('utf-8')
    response_json_bytes = server.handle_request(request_json_bytes)

    assert response_json_bytes.decode('utf-8') == '{"jsonrpc": "2.0", "id": 1, "result": 36}'


# Generated at 2022-06-13 16:32:03.263133
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import os
    import tempfile
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common import load_provider
    from ansible.module_utils.network.iosxr.iosxr import iosxr_provider_spec
    from ansible.module_utils.network.iosxr.iosxr import iosxr_argument_spec
    from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.iosxr import iosxr_provider_spec
    from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.iosxr import iosxr_argument_spec
    from ansible.module_utils.network.common.config import NetworkConfig

# Generated at 2022-06-13 16:32:13.907075
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'test_method',
        'params': [[], {}]
    }
    request = json.dumps(request)
    response = server.handle_request(request)
    assert response == '{"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found"}}'
    class TestClass(object):
        def test_method(self):
            return 'test_method'
    server.register(TestClass())
    response = json.loads(server.handle_request(request))
    assert response['result'] == 'test_method'


# Generated at 2022-06-13 16:32:21.878685
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    result = {}
    result['jsonrpc'] = '2.0'
    result['id'] = 'id_test_JsonRpcServer_handle_request'
    result['result'] = 'result_test_JsonRpcServer_handle_request'
    rpc_server = JsonRpcServer()
    request = dict()
    request['jsonrpc'] = '2.0'
    request['id'] = 'id_test_JsonRpcServer_handle_request'
    request['method'] = 'test_method'
    request['params'] = [ 'test_param' ]
    response = rpc_server.handle_request(request)
    assert response == result


# Generated at 2022-06-13 16:32:31.967100
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    class TestObject(object):
        def test_method(self):
            return 2

    server = JsonRpcServer()
    server.register(TestObject())

    # Test valid request
    request = json.dumps({'method' : 'test_method', 'params' : [], 'id' : 'req-001'})
    response = json.loads(server.handle_request(request))
    assert response['result'] == 2
    assert response['id'] == 'req-001'

    # Test valid request with error
    request = json.dumps({'method' : 'invalid_method', 'params' : [], 'id' : 'req-002'})
    response = json.loads(server.handle_request(request))
    assert response['error']['code'] == -32601

# Generated at 2022-06-13 16:32:40.266817
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Test(JsonRpcServer):
        def __init__(self):
            super(JsonRpcServer, self).__init__()
            self.register(self)

        def test(self, arg1, arg2=None):
            return [arg1, arg2]

    test = Test()

    request = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "test",
        "params": ["a", "b"]
    }

    response = test.handle_request(json.dumps(request))
    assert json.loads(response) == {
        "jsonrpc": "2.0",
        "result": ["a", "b"],
        "id": "1"
    }

# Generated at 2022-06-13 16:32:56.475353
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    # Testing method from class JsonRpcServer: Example of request
    request = {u'params': [{u'host': u'10.0.0.1', u'port': 80, u'username': u'john', u'password': u'doe'},
                           u'config'], u'id': 100, u'method': u'get_connection'}
    # Testing method from class JsonRpcServer: Example of response
    expected_response = {u'error': {u'code': -32600, u'message': u'Invalid request'}, u'id': 100, u'jsonrpc': u'2.0'}
    response = server.handle_request(request)
    # Testing method from class JsonRpcServer: Does the expected response match the response got?


# Generated at 2022-06-13 16:33:04.763907
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Test with invalid path
    request = {"method": "foo/bar", "params": [[], {}]}
    request = json.dumps(request)
    test_server = JsonRpcServer()
    response = test_server.handle_request(request)
    response = json.loads(response)
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == None
    assert response["error"]["code"] == -32700

# Generated at 2022-06-13 16:33:12.890462
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    import sys
    import codecs

    def object_decoder(obj):
        return codecs.decode(obj, 'base64')

    a = {'b':'c'}
    a_pickle = cPickle.dumps(a, protocol=0)

    j = {'b': codecs.encode(a_pickle, 'base64')}
    j_json = json.dumps(j)

    response = {'jsonrpc':'2.0','id':'c','result': j_json}


# Generated at 2022-06-13 16:33:18.826630
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jrpc_server = JsonRpcServer()

# Generated at 2022-06-13 16:33:25.937282
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "update",
            "params": [
                "banana",
                {
                    "city": "chicago",
                    "state": "illinois",
                    "zip": 60606
                }
            ],
            "id": 3
        }, indent=4)

    expected = (
        "method not found\n"
        "request  = {'jsonrpc': '2.0', 'method': 'update', 'params': ['banana', "
        "{'zip': 60606, 'state': 'illinois', 'city': 'chicago'}], 'id': 3}"
    )

    server = JsonRpcServer()
    result = server.handle_request(request)


# Generated at 2022-06-13 16:33:36.623849
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Create instance of JsonRpcServer
    jsonrpc_server = JsonRpcServer()
    
    # Mock the input request
    request_dict = {
        "id": 1, 
        "method": "echo", 
        "params": {
            "args": [
                "one", 
                "two"
            ], 
            "kwargs": {
                "key1": "value1"
            }
        }
    }
    request_str = json.dumps(request_dict)
    
    # Call method handle_request of JsonRpcServer
    jsonrpc_server.handle_request(request_str)


# Generated at 2022-06-13 16:33:43.155695
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    rpc = JsonRpcServer()

    msg = json.dumps({
        'jsonrpc': '2.0',
        'method': 'test',
        'params': [],
        'id': 1
        })
    result = json.loads(rpc.handle_request(msg))
    assert result == {'jsonrpc': '2.0', 'id': 1, 'error': {'code': -32601, 'message': 'Method not found'}}



# Generated at 2022-06-13 16:33:47.510251
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = "abc"
    response = server.handle_request(request)
    assert response == {"id": None, "jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid request", "data": None}}

if __name__ == "__main__":
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:33:59.492713
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = json.dumps({
        "jsonrpc": "2.0",
        "method": "__test_method_on_dummy_class",
        "params": [{
            "name": "test",
            "age": 41
        }],
        "id": "1"
    })

    server = JsonRpcServer()

    for obj in JsonRpcServer._objects:
        server._objects.remove(obj)

    class Dummy:
        def __test_method_on_dummy_class(self, *args, **kwargs):
            return args[0]+" "+kwargs['name']

    dummy = Dummy()

    server.register(dummy)

    response = server.handle_request(request)

# Generated at 2022-06-13 16:34:09.515484
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class MyObject():

        def some_method(self, a, b, c=None, d=None, e=None):
            return dict(a=a, b=b, c=c, d=d, e=e)

    obj = MyObject()

    server = JsonRpcServer()
    server.register(obj)

    response = server.handle_request(json.dumps(dict(
        jsonrpc='2.0',
        id='unit test',
        method='some_method',
        params=(('a', 'b'), dict(c='c', e='e'))
    )))

    response = json.loads(response)

# Generated at 2022-06-13 16:34:32.380312
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from six import StringIO
    import sys
    stdout = StringIO()
    sys.stdout = stdout
    # save previous stderr and restore it at the end of the test
    stderr = sys.stderr
    sys.stderr = StringIO()

    json_rpc_server = __import__('ansible.module_utils.remote_management.json_rpc')
    json_rpc_server = json_rpc_server.module_utils.remote_management.json_rpc.JsonRpcServer()

    try:
        json_rpc_server.handle_request('{"jsonrpc": "2.0", "method": "__start__", "params": [], "id": 0}')
    except Exception as err:
        assert err.message == 'Method not found'

# Generated at 2022-06-13 16:34:38.684658
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.errors import AnsibleConnectionFailure
    server = JsonRpcServer()
    request = json.dumps({
        'id': 'request_id-1',
        'method': 'invalid_method'
    })
    response = json.loads(server.handle_request(request))
    assert response['jsonrpc'] == '2.0'
    assert response['id'] == 'request_id-1'
    assert response['error']['code'] == -32601
    assert response['error']['message'] == 'Method not found'
    request = json.dumps({
        'id': 'request_id-1',
        'method': 'invalid_method',
        'params': [42,21]
    })
    response = json.loads(server.handle_request(request))
    assert response

# Generated at 2022-06-13 16:34:41.977527
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    assert server.response() == {'id': None, 'jsonrpc': '2.0'}


# Generated at 2022-06-13 16:34:47.605823
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
        import types
        jrpcs = JsonRpcServer()
        jrpcs._identifier = 100
        result = "test"
        obj = types.SimpleNamespace(**{'result':result})
        header = {'jsonrpc': '2.0', 'id': 100}
        expected = {'result': result, 'jsonrpc': '2.0', 'id':100}
        assert jrpcs.response(obj.result) == expected

# Generated at 2022-06-13 16:34:54.745517
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    s = JsonRpcServer()
    t = {'id': 1, 'method': 'foo', 'params': [['bar', 'baz'], {'foo': 'bar'}]}

    # test parse error
    assert s.handle_request('-') == '{"jsonrpc": "2.0", "id": null, "error": {"code": -32700, "message": "Parse error"}}'

    # test method not found
    assert s.handle_request(json.dumps(t)) == '{"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found"}}'

    # test invalid request
    t['method'] = 'rpc.foo'

# Generated at 2022-06-13 16:34:57.565872
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = {
        'jsonrpc': '2.0',
        'method': 'ping',
        'params': [],
        'id': 0
    }
    response = server.handle_request(request)


if __name__ == '__main__':
    test_JsonRpcServer_handle_request()

# Generated at 2022-06-13 16:35:04.675333
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Test(object):
        def hello(self, arg1, arg2, arg3=None):
            return arg1 + arg2

    server = JsonRpcServer()
    server.register(Test())

    request = {
        'jsonrpc': '2.0',
        'method': 'hello',
        'params': [[1, 2], {}],
        'id': 2
    }

    result = server.handle_request(json.dumps(request).encode('utf-8'))

    request = {
        'jsonrpc': '2.0',
        'method': 'hello',
        'params': [[1, 2], {'arg3': 'arg3'}],
        'id': 3
    }
