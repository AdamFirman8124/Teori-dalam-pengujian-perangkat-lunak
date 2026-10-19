

# Generated at 2022-06-13 16:25:15.727778
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    server._identifier = '123'
    result = server.response('abc')
    assert result['id'] == '123'
    assert result['result'] == 'abc'
    assert result['result_type'] is None

    result = server.response('ÄÖÜäöüß')
    assert result['id'] == '123'
    assert result['result'] == 'ÄÖÜäöüß'
    assert result['result_type'] is None

    result = server.response(u'ÄÖÜäöüß')
    assert result['id'] == '123'
    assert result['result'] == 'ÄÖÜäöüß'
    assert result['result_type'] is None


# Generated at 2022-06-13 16:25:26.310604
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import io
    import os
    import shutil
    import sys
    import tempfile
    import unittest
    from .my_test_cls import MyTestClass
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.connection import ConnectionError

    # load fake __file__, sys.argv, and import module
    class Options:
        def __init__(self, verbosity=0, connection='network_cli', module_path=None, forks=10, become=None, become_method=None, become_user=None, check=False, diff=False):
            self.verbosity = verbosity
            self.connection = connection
            self.module_path = module_path
            self.forks = forks

# Generated at 2022-06-13 16:25:31.989368
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    err = server.error(code=1, message='hello')
    assert err['jsonrpc'] == '2.0'
    assert err['id'] is None
    assert err['error'] == {'code': 1, 'message': 'hello'}

# Generated at 2022-06-13 16:25:40.415493
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.module_utils.network.common.parsing import Conditional

    fields = {
        'transport': dict(default='cli', choices=['cli'])
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=True)

    # Create a connection to be able to execute commands
    provider = load_provider(module)
    conn = Connection(module._socket_path)
    conn.set_socket_path = module._socket_path

    # Set the connection used by the module to be the connection that was just created
    module.connection = conn

    # Create a J

# Generated at 2022-06-13 16:25:45.841556
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = """{"jsonrpc": "2.0", "id": 1, "method": "status", "params": []}"""
    result = server.handle_request(request)
    assert 'Parse error' in result

# Generated at 2022-06-13 16:25:50.151119
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    response = JsonRpcServer().error(99, 'foo')
    assert response['jsonrpc'] == '2.0'
    assert response['id'] == None
    assert response['error']['code'] == 99
    assert response['error']['message'] == 'foo'

# Generated at 2022-06-13 16:25:56.891740
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
   server = JsonRpcServer()
   setattr(server, '_identifier', 1)
   error = server.error(-32600, 'Invalid request')

   assert error.get('error').get('code') == -32600
   assert error.get('error').get('message') == 'Invalid request'
   assert error.get('jsonrpc') == '2.0'
   assert error.get('id') == 1


# Generated at 2022-06-13 16:26:01.073505
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    error = server.error(1, "test error")
    expected = '{"jsonrpc": "2.0", "error": {"code": 1, "message": "test error"}, "id": null}'
    assert error == expected


# Generated at 2022-06-13 16:26:03.554736
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc = JsonRpcServer()
    #This method parses the request and returns the response.
    assert json_rpc


# Generated at 2022-06-13 16:26:07.059772
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    from ansible.module_utils.network.parsers.jsonrpc import JsonRpcServer
    jsonRpcServer = JsonRpcServer()
    setattr(jsonRpcServer, '_identifier', 1)
    jsonRpcServer.response()


# Generated at 2022-06-13 16:26:15.503047
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    result = 1
    server = JsonRpcServer()
    server._identifier = '123456789'
    response = server.response(result)
    assert (response == {'jsonrpc': '2.0', 'id': '123456789', 'result': '1'})


# Generated at 2022-06-13 16:26:26.618018
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import to_list
    from ansible.module_utils.network.common.parsing import Conditional
    from ansible.module_utils.network.common.facts.legacy import fact_legacy_file
    from ansible.module_utils.network.common.facts.legacy import write_facts
    import json
    import os

    s = JsonRpcServer()
    c = Connection()

    s.register(c)
    # Can't test private method
    #r = s.handle_request(json.dumps({"method": "unsupported_method", "params": [], "id": 0}))
    #Instead test_JsonRpcServer_method_not_found()
    r = s.handle

# Generated at 2022-06-13 16:26:36.185997
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    instance = JsonRpcServer()
    setattr(instance, '_identifier', '1')

    assert instance.error(code=2, message='test') == {
        'id': '1',
        'jsonrpc': '2.0',
        'error': {
            'code': 2,
            'message': 'test'
        }
    }

    assert instance.error(code=2, message='test', data='test2') == {
        'id': '1',
        'jsonrpc': '2.0',
        'error': {
            'code': 2,
            'message': 'test',
            'data': 'test2'
        }
    }

    delattr(instance, '_identifier')


# Generated at 2022-06-13 16:26:37.027708
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass

# Generated at 2022-06-13 16:26:40.968916
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible_collections.community.general.tests.unit.compat import unittest
    from ansible_collections.community.general.plugins.modules.network.common import utils

    class TestClass(object):
        def __init__(self):
            self.module = utils.load_module_spec(os.path.join(os.path.dirname(__file__),
                                                              '../../fixtures/dellos6_module.spec'))

        def run_dellos6_command(self, command):
            return dict(message='dellos6_command', command=command)

    server = JsonRpcServer()
    provider = TestClass()

    server.register(provider)


# Generated at 2022-06-13 16:26:46.943511
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    obj = MyClass()
    server.register(obj)

    print("### test1: Method handle_request of class JsonRpcServer ###")
    request = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method':'test_method', 'params': []})
    response = server.handle_request(request)
    print("Assertion: {}".format(response))
    print("Response is:")
    print("{}".format(response))
    print("\n")



# Generated at 2022-06-13 16:26:52.580352
# Unit test for method handle_request of class JsonRpcServer

# Generated at 2022-06-13 16:27:02.845487
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    class TestClass(object):
        def __init__(self):
            self.rpc_server = JsonRpcServer()
            self.rpc_server.register(self)
            
        def test(self):
            return "test"

        def test_1(self, arg1):
            return arg1

        def test_2(self, arg1, arg2):
            return arg1 + arg2

        def test_3(self, arg1=None, arg2=None):
            return arg1 + arg2

        def fail_test(self):
            raise Exception("Failed")

    obj = TestClass()

    res = obj.rpc_server.handle_request(b'{"id": 1}')

# Generated at 2022-06-13 16:27:10.257716
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc_server = JsonRpcServer()
    request_data = '{"jsonrpc": "2.0", "method": "show_version", "id": 1, "params": []}'
    import os
    import sys
    sys.path.append(os.getcwd())
    from library import ios
    class_object = ios.Ios()
    json_rpc_server.register(class_object)
    response_data = json_rpc_server.handle_request(request_data)

# Generated at 2022-06-13 16:27:19.546550
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import ast

    class Test(object):
        def foo(self, *args, **kwargs):
            return {'args': args, 'kwargs': kwargs}

        def bar(self, data):
            return {'data': data}

    class Module(object):
        def __init__(self, params):
            self.params = params

    class Client(object):
        def __init__(self, module):
            self.module = module

    class Connections(object):
        def __init__(self, params):
            self.params = params

        def __call__(self, *args, **kwargs):
            return Connection(self.params, *args, **kwargs)

    class Connection(object):
        def __init__(self, params, *args, **kwargs):
            self.params = params

# Generated at 2022-06-13 16:27:33.109219
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    params_integer = json.dumps({
        "method": "list_facts",
        "params": [[], {}],
        "id": 1
    })
    json_response = {
        "result": "hello",
        "jsonrpc": "2.0",
        "id": 1
    }
    response = {
        'jsonrpc': '2.0',
        'id': 1,
        'result': 'hello'
    }
    params_dict = json.dumps({
        "method": "list_facts",
        "params": [[], {}],
        "id": "1"
    })
    params_list = json.dumps({
        "method": "list_facts",
        "params": [["1"], {}],
        "id": 1
    })
    params_exception = json

# Generated at 2022-06-13 16:27:35.248463
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    rpc = JsonRpcServer()
    # TODO
    pass

# Generated at 2022-06-13 16:27:43.735454
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    setattr(server, '_identifier', '12345')

    response = server.response('Hello, World!')
    assert response == {
        'jsonrpc': '2.0',
        'id': '12345',
        'result': 'Hello, World!'
    }

    response = server.response(u'Hello, World!')
    assert response == {
        'jsonrpc': '2.0',
        'id': '12345',
        'result': u'Hello, World!'
    }

    response = server.response({'jsonrpc': '2.0', 'result': 'Hello, World!'})
    assert response == {'jsonrpc': '2.0', 'id': '12345', 'result': 'Hello, World!'}


# Generated at 2022-06-13 16:27:55.621569
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    test = JsonRpcServer()
    test.identifier = 10
    test.register(JsonRpcServer())
    #test.handle_request('{"jsonrpc": "2.0", "method":"handle_request", "params":["test"], "id": 10}')
    print((test.handle_request('{"jsonrpc": "2.0", "method":"handle_request", "params": ["test"], "id": 10}')))
    print((test.handle_request('{"jsonrpc": "2.0", "method":"handle_request", "params": ["test"], "id": 10}')))
    print((test.handle_request('{"jsonrpc": "2.0", "method":"handle_request", "params": ["test", ["test"]], "id": 10}')))


# Generated at 2022-06-13 16:28:02.965513
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    expected_error = '''{"id": "test1", "jsonrpc": "2.0", "error": {"message": "Method not found", "code": -32601}}'''
    server = JsonRpcServer()
    testJson = json.dumps({'method': 'test', 'params': [[], {}], 'id': 'test1'})
    ret = server.handle_request(testJson)
    assert expected_error == ret


# Generated at 2022-06-13 16:28:12.775201
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.common._text import to_text
    from ansible.module_utils.six.moves import cPickle
    import json

    # registers dummy object for test
    test_obj = DummyJsonRpcObj()
    json_rpc = JsonRpcServer()
    json_rpc.register(test_obj)

    # response test
    request = {'method': 'response_method', 'params': [[], {}], 'id': 1}
    response = json.dumps(json_rpc.handle_request(json.dumps(request)))
    assert response == '{"jsonrpc": "2.0", "result": "response_method_result", "result_type": "pickle", "id": 1}'


# Generated at 2022-06-13 16:28:22.495373
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    # test invalid request
    test_request = {'id': '1', 'params': ['okay']}
    response = server.handle_request(json.dumps(test_request))
    assert json.loads(response) == server.invalid_request()
    # test method not found
    test_request = {'jsonrpc': '2.0', 'id': '1', 'method': 'run', 'params': ['okay']}
    response = server.handle_request(json.dumps(test_request))
    assert json.loads(response) == server.method_not_found()
    # test error
    test_request = {'jsonrpc': '2.0', 'id': '1', 'method': 'run', 'params': ['okay']}

# Generated at 2022-06-13 16:28:30.429180
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # First create a test target class
    class MyClass(object):
        def _rpc_test_method(self, *args, **kwargs):
            message = "We are in the target method."
            return message

        def _rpc_test_method_with_args(self, *args, **kwargs):
            message = str(args) + str(kwargs)
            return message

    # Then create the sut
    sut = JsonRpcServer()

    # And register the test target class
    sut.register(MyClass())

    # Get a test request
    request = {
        "jsonrpc": "2.0",
        "method": "_rpc_test_method",
        "params": [],
        "id": 1
    }
    request = json.dumps(request)

    #

# Generated at 2022-06-13 16:28:39.264839
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    json_rpc_server = JsonRpcServer()
    json_rpc_server._identifier = 2
    result = json_rpc_server.response({'key':'value'})
    assert result == {'id': 2, 'jsonrpc': '2.0', 'result_type': 'pickle', 'result': 'gAJ9cQBYBAAAAAAdWZXJiMgAAAAAEuA==\n'}
    result = json_rpc_server.response('result_string')
    assert result == {'id': 2, 'jsonrpc': '2.0', 'result': 'result_string'}
    result = json_rpc_server.response(1)

# Generated at 2022-06-13 16:28:45.753410
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()

    class Foo(object):
        def __init__(self):
            server.register(self)

        def bar(self):
            return 'Hello from bar'

    f = Foo()
    request = json.dumps({
        'method': 'bar',
        'params': [[], {}],
        'id': 'myidentifier'
    })
    rsp = server.handle_request(request)
    assert rsp == '{"jsonrpc": "2.0", "id": "myidentifier", "result": "Hello from bar"}'

# Generated at 2022-06-13 16:29:00.510902
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import json
    import unittest
    import tempfile
    import os
    import shutil

    class Test(object):

        def __init__(self, module):
            self.module = module

        def method(self, *args, **kwargs):
            return (args, kwargs)

        def method1(self, *args, **kwargs):
            raise ValueError('Test Exception')

        def method2(self, *args, **kwargs):
            raise ConnectionError('Test Connection Error', code=123)

        def method3(self, *args, **kwargs):
            self.module.fail_json(msg='Test Failure')

        def _method(self):
            """ Ignore private methods """


# Generated at 2022-06-13 16:29:05.282470
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    uuid = "f1d75878-083a-49c9-92f7-1c9dea7f8b96"
    server.response(uuid)
    assert server._identifier == 1


# Generated at 2022-06-13 16:29:11.862275
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jr = JsonRpcServer()
    rq = '''{
    "jsonrpc": "2.0",
    "method": "rpc.run_command",
    "params": [
        "show version"
    ],
    "id": 12
    }'''
    res = jr.handle_request(rq)
    assert res['jsonrpc'] == '2.0'

# Generated at 2022-06-13 16:29:15.884515
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jrpc_server = JsonRpcServer()
    request = '{"jsonrpc": "2.0", "method": "rpc.ping", "params": [], "id": 0}'

    response = jrpc_server.handle_request(request)
    response_dict = json.loads(response)
    assert response_dict['id'] == 0
    assert response_dict['jsonrpc'] == '2.0'
    assert response_dict['result'] == 'pong'


# Generated at 2022-06-13 16:29:25.539185
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jrpc = JsonRpcServer()
    request_input = '{"id": 1, "method": "foo"}'
    expected_output = '{"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found", ' \
                      '"data": null}}'
    assert jrpc.handle_request(request_input) == expected_output, 'Error raised while testing handle_request(request) ' \
                                                                  'of JsonRpcServer'



# Generated at 2022-06-13 16:29:27.379685
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass

# Generated at 2022-06-13 16:29:37.949000
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    json_rpc_server = JsonRpcServer()
    json_method = '["system", "reboot", 10]'
    expected_result = '{"id": null, "jsonrpc": "2.0", "result_type": "pickle", "result": "gAJ9cQAoVQBlAHMATQBpAG4AIABNAGkAbgBhAGwAIABJAHMAdAByAHUAZABlAHIAAABJAAUAGkAbgAgAE0AaQBuAGEAbAAgAEkAcwB0AHIAcwBlAGUAcgAAAEkABQBpAG4AIABNAGkAbgBhAGwAIABJAHMAdAByAHMAZQByAAAAOgA="}'

    # The result_type cannot be None
    #

# Generated at 2022-06-13 16:29:48.045564
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestJsonRpcServer(unittest.TestCase):
        def setUp(self):
            self.json_rpc_server = JsonRpcServer()

        def test_normal_request(self):
            # Prepare
            self.json_rpc_server.register(self)
            request = '{"jsonrpc": "2.0", "method": "this_is_normal", "params": [1, 2, 3], "id": 123}'

            # Execute
            result = self.json_rpc_server.handle_request(request)

            # Verify
            dict_result = json.loads(result)
            self.assertEqual(dict_result["result"], 6)

# Generated at 2022-06-13 16:29:53.961288
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    j_server = JsonRpcServer()
    test_valid_request = {'jsonrpc': '2.0', 'id': '1',
                          'method': 'test', 'params': [[], {}]}
    test_valid_request = json.dumps(test_valid_request)

    class test_class(object):
        def test(self):
            return

    testobj = test_class()
    j_server.register(testobj)

    assert j_server.handle_request(test_valid_request) == '{}'



# Generated at 2022-06-13 16:30:02.575779
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    # Test handle_request for correct request
    request=b'{"jsonrpc": "2.0", "method": "rpc.demo", "params": [1,2,{"test":"test"}], "id": 1}'
    result = server.handle_request(request)
    assert result == b'{"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found", "data": null}}'
    # Test handle_request for request without jsonrpc
    request=b'{"method": "rpc.demo", "params": [1, 2, {"test": "test"}], "id": 1}'
    result = server.handle_request(request)

# Generated at 2022-06-13 16:30:16.210557
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class FakeObject:
        def rpc(self):
            return {}

        def rpc2(self, _x, _y):
            return _x + _y

    jsonrpc = JsonRpcServer()
    jsonrpc.register(FakeObject())

    request = to_text(json.dumps({
        'jsonrpc': '2.0',
        'id': 'test',
        'method': 'rpc'
    }))

    jsonrpc.handle_request(request)

    request = to_text(json.dumps({
        'jsonrpc': '2.0',
        'id': 'test',
        'method': 'rpc2',
        'params': [1, 2]
    }))

    jsonrpc.handle_request(request)


# Generated at 2022-06-13 16:30:27.981367
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.json_rpc_server import JsonRpcServer
    import json
    import traceback

    class DummyClass:
        def dummy_add_to_queue(self, *args, **kwargs):
            return json.dumps(args) + json.dumps(kwargs)

    dummyobj = DummyClass()

    jrpc_server = JsonRpcServer()
    jrpc_server._identifier = 'dummy_reponse_id'
    jrpc_server.register(dummyobj)

    json_rpc_request = '{"jsonrpc": "2.0", "method": "dummy_add_to_queue", "params": [1, 2, 3, 4], "id": "some_random_id"}'

# Generated at 2022-06-13 16:30:36.849852
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    testJsonRpcServer = JsonRpcServer()
    # Test a well formed request
    request = b'{"jsonrpc": "2.0", "method": "echo", "params": ["echo message"], "id": 5}'
    response = testJsonRpcServer.handle_request(request)
    assert json.loads(response.decode('utf-8')) == {
        'id': 5,
        'jsonrpc': '2.0',
        'result': 'echo message'
    }
    # Test a malformed request
    request = b'{"jsonrpc": "2.0", "method": "echo", "params": ["echo message"]}'
    response = testJsonRpcServer.handle_request(request)

# Generated at 2022-06-13 16:30:40.876249
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
	s = JsonRpcServer()
	data = {"method":"is_alive","params":[],"id":1}
	data = json.dumps(data)
	result = s.handle_request(data)
	print("test_JsonRpcServer_handle_request", result)


# Generated at 2022-06-13 16:30:52.578885
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = dict(id=1, method='resolve_hostname',
        params=dict(args=['1.1.1.1'], kwargs=dict()))
    server = JsonRpcServer()
    response = server.handle_request(json.dumps(request))
    response = json.loads(response)

    network_resources = dict(
        resolve_hostname=dict(
            return_value=dict(
                fqdn='localhost.localdomain',
                hostname='localhost',
                ip='127.0.0.1',
                ipv6=''
            )
        )
    )
    server.register(network_resources)


# Generated at 2022-06-13 16:31:01.183817
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = b'{ "jsonrpc": "2.0", "method": "foo", "id": 1 }'
    result = server.handle_request(request)
    assert json.loads(result) == {"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found"}}

    request = b'"jsonrpc": "2.0", "method": "foo", "id": 1 }'
    result = server.handle_request(request)
    assert json.loads(result) == {"jsonrpc": "2.0", "id": 1, "error": {"code": -32700, "message": "Parse error"}}


# Generated at 2022-06-13 16:31:09.534948
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = '{"jsonrpc": "2.0", "method": "get_info", "id": "1"}'
    from ansible.module_utils.common.remotefuncs import RemoteFuncs
    connmgr = RemoteFuncs()
    srv = JsonRpcServer()
    assert srv.handle_request(request) == '{"jsonrpc": "2.0", "id": "1", "error": {"code": -32601, "message": "Method not found"}}'
    srv.register(connmgr)
    assert srv.handle_request(request) == '{"jsonrpc": "2.0", "result": "2.0", "id": "1"}'

# Generated at 2022-06-13 16:31:14.784300
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    json_rpc_server = JsonRpcServer()
    json_rpc_server._identifier = 'test'
    json_server_response = json_rpc_server.response('test')
    assert json_server_response == {'jsonrpc': '2.0', 'id': 'test', 'result': 'test', 'result_type': None}


# Generated at 2022-06-13 16:31:25.238391
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    s = JsonRpcServer()
    setattr(s, '_identifier', '12')

    # no result
    response = s.response()
    assert response == {'id': '12',
                        'jsonrpc': '2.0',
                        'result': None}

    # with result
    response = s.response('some result')
    assert response == {'id': '12',
                        'jsonrpc': '2.0',
                        'result': 'some result'}

    # result is bytes
    response = s.response(b'some result')
    assert response == {'id': '12',
                        'jsonrpc': '2.0',
                        'result': 'some result'}

    # result is non-JSON serializable
    class Foo:
        pass


# Generated at 2022-06-13 16:31:36.341605
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    jsonServer = JsonRpcServer()
    # test with raw string
    jsonServer._identifier = "2f4ffe3e-d2b9-4134-a766-e4e1eb7ec394"
    response = jsonServer.response("Return string")
    expected = {'jsonrpc': '2.0', 'id': jsonServer._identifier, 'result': "Return string"}
    assert response == expected

    # test with pickle object
    response = jsonServer.response({"jsonrpc" : "2.0" , "id" : "2f4ffe3e-d2b9-4134-a766-e4e1eb7ec394", "result" : "success"})

# Generated at 2022-06-13 16:31:50.138341
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc_test = JsonRpcServer()
    test_request = {
        'method': 'test_method',
        'id': 'test_id',
        'params': [['test_arg1', 'test_arg2'], {'test_kwarg1': 'test_kwarg2'}]
    }

    # test invalid request
    invalid_request = json_rpc_test.invalid_request().get('error')
    response = json_rpc_test.handle_request(json.dumps({'method': 'rpc.invalid_request'}))
    assert invalid_request == json.loads(response).get('error')
    response = json_rpc_test.handle_request(json.dumps({'method': '_invalid_request'}))
    assert invalid_request == json

# Generated at 2022-06-13 16:31:58.486720
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
    from ansible.module_utils.compat import ipaddress
    import json

    # The JsonRpcServer object for testing
    jrpc_server = JsonRpcServer()

    # request with no id provided
    request = json.dumps({'jsonrpc': '2.0', 'method': 'test_module.run', 'params': [['a']], 'id': jrpc_server._identifier})
    test_id = jrpc_server._identifier
    response = json.loads(jrpc_server.handle_request(request))
    assert response["jsonrpc"] == '2.0'
    assert response["id"] == test_id

    # request with bad id provided

# Generated at 2022-06-13 16:32:10.696994
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
	jsonrpc_server = JsonRpcServer()
	jsonrpc_server._objects.add({})
	assert jsonrpc_server.handle_request('{"jsonrpc": "2.0", "method": "missing_method", "id": "1"}') == '{"jsonrpc": "2.0", "id": "1", "error": {"code": -32601, "message": "Method not found"}}'
	assert jsonrpc_server.handle_request('{"jsonrpc": "2.0", "method": "has_method", "id": "1"}') == '{"jsonrpc": "2.0", "id": "1", "error": {"code": -32602, "message": "The has_method() method does not take any arguments"}}'

# Generated at 2022-06-13 16:32:11.353355
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass


# Generated at 2022-06-13 16:32:18.711001
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    rpc_method = 'sample'

    def method():
        return True

    def method2():
        return True

    server.method = method
    server.method2 = method2


# Generated at 2022-06-13 16:32:29.830634
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import inspect

    class MyObject(object):
        def __init__(self, path):
            self.path = path

        def simple_method(self):
            return True

        def method(self, arg1, arg2, arg3=None, arg4=None):
            return (arg1, arg2, arg3, arg4)

    class MyOtherObject(object):
        def __init__(self, path):
            self.path = path

        def other_method(self, arg1, arg2, arg3=None, arg4=None):
            return (arg1, arg2, arg3, arg4)

    obj1 = MyObject('/foo')
    obj2 = MyOtherObject('/bar')

    server = JsonRpcServer()
    server.register(obj1)

# Generated at 2022-06-13 16:32:38.019897
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = {"id": "1", "method": "method1", "params": [["a", "b"], {"c": "d"}]}

    class TargetClass:
        def method1(self, a, b, c=None):
            return "a {} b {} c {}".format(a, b, c)

    obj = TargetClass()
    server = JsonRpcServer()
    server.register(obj)

    response = server.handle_request(json.dumps(request))
    assert response == '{"jsonrpc": "2.0", "id": 1, "result": "a a b b c d"}'


# Generated at 2022-06-13 16:32:48.688436
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    method = "get_config"
    request = {"method": method, "params": [[], {}], "id": 2}
    request_string = json.dumps(request)
    result = server.handle_request(request_string)

    result_json = json.loads(result)
    if "jsonrpc" in result_json:
        assert result_json["jsonrpc"] == "2.0"
    else:
        assert result_json["jsonrpc"] != "2.0"

    assert result_json["id"] == 2

    if "error" not in result_json:
        assert result_json["result"] == ""
    else:
        assert result_json["error"]["code"] == -32601

# Generated at 2022-06-13 16:32:54.865688
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # http://www.jsonrpc.org/specification#examples
    request = '{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}'
    expected = '{"jsonrpc": "2.0", "id": 1, "result": 19}'

    obj = JsonRpcServer()
    obj.register(Handler())
    response = obj.handle_request(request)

    assert response == expected


# Generated at 2022-06-13 16:33:01.225811
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    test_obj = {
        "method": "valid_request",
        "params": [[], {}],
        "id": 42
    }

    expected_obj = {
        "jsonrpc": "2.0",
        "id": 42,
        "result": ""
    }

    test_obj_json = json.dumps(test_obj)
    rpc_obj = JsonRpcServer()
    rpc_obj.register(TestJsonRpcMethods())
    response_obj_json = rpc_obj.handle_request(test_obj_json)

    response_obj = json.loads(response_obj_json)

    assert response_obj == expected_obj



# Generated at 2022-06-13 16:33:12.764219
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Test(object):
        pass

    obj = Test()

    def test_method(a, b):
        return a + b

    setattr(obj, 'test_method', test_method)

    server = JsonRpcServer()
    server.register(obj)
    assert server.handle_request(json.dumps({"method": "test_method", "params": (1, 2), "id": 1})) == '{"id": 1, "jsonrpc": "2.0", "result": "3"}'

# Generated at 2022-06-13 16:33:21.236050
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import unittest
    import tempfile

    class MockConnection(object):
        def __init__(self):
            self.connected = False
            self.connections = {}

        def get_connection(self, module_name, transport, params):
            if params is None:
                raise ConnectionError(msg='You must specify connection parameters')

            connection = self.connections.get(params['host'])
            if connection:
                return connection

            if params['host'] == 'test2':
                raise ConnectionError(msg='Unable to connect')

            if params['host'] == 'test3':
                raise ValueError('test')

            self.connections[params['host']] = tempfile.NamedTemporaryFile()

            return self.connections[params['host']]


# Generated at 2022-06-13 16:33:29.857809
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection import Connection

    class ConnectionMock(Connection):

        def run(self, *args, **kwargs):
            return {'msg': 'hello'}

    def my_run(self):
        return {'msg': 'hello'}

    srv = JsonRpcServer()
    srv.register(ConnectionMock())

    result = srv.handle_request('{"jsonrpc": "2.0", "method": "run", "params": [], "id": 1}')
    result = json.loads(result)
    assert result['result'] == '{"msg": "hello"}'

    result = srv.handle_request('{"jsonrpc": "2.0", "method": "my_run", "params": [], "id": 1}')
    result = json.loads

# Generated at 2022-06-13 16:33:38.526353
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = {'jsonrpc': '2.0', 'method': 'test_method', 'params': [], 'id': 0}
    request = json.dumps(request)

    class Obj():
        def test_method(self):
            pass

    obj = Obj()

    jrpc = JsonRpcServer()
    jrpc.register(obj)
    response = jrpc.handle_request(request)

    assert json.dumps(response) == '{"jsonrpc": "2.0", "id": 0, "result": ""}'

# Generated at 2022-06-13 16:33:43.754882
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    print("----- test_JsonRpcServer_handle_request -----")
    try:
        rpc_server = JsonRpcServer()
        # method_not_found
        rpc_server.handle_request(json.dumps({'jsonrpc': '2.0', 'method': 'dummy', 'params': [], 'id': 'abc'}))
        # invalid_request
        rpc_server.handle_request(json.dumps({'jsonrpc': '2.0', 'params': [], 'id': 'abc'}))
    except Exception as exc:
        display.vvv(traceback.format_exc())
        print('Exception: ' + repr(exc) + '\n')
    finally:
        print('test_JsonRpcServer_handle_request completed\n')


# Unit test

# Generated at 2022-06-13 16:33:47.434987
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    data = {
        'method': 'get_config',
        'params': [""],
        'id': 0
        }
    data = json.dumps(data)

# Generated at 2022-06-13 16:33:59.493441
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    result_json = {'jsonrpc': u'2.0', 'result': u'a string', 'id': 2}
    result_pickle = {'jsonrpc': u'2.0', 'result': u'\x80\x02U\rtest_stringq\x01.', 'id': 2, 'result_type': 'pickle'}
    error = {'jsonrpc': u'2.0', 'error': {'code': -32603, 'message': u'Internal error', 'data': u'test_error_data'}, 'id': 2}
    msg_id = 2

    obj1 = object()
    obj2 = object()
    def rpc_test(*args, **kwargs):
        return 'test_string'

# Generated at 2022-06-13 16:34:09.515832
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    class MyTestObj:
        def my_method(self, arg1, arg2, kwarg1=None):
            return "my_method({}, {}, kwarg1={})".format(arg1, arg2, kwarg1)

    rpc = JsonRpcServer()
    rpc.register(MyTestObj())


# Generated at 2022-06-13 16:34:16.497660
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Create an object of JsonRpcServer class
    jsonrpc = JsonRpcServer()
    # Create an object of "dict" class
    obj_1 = dict()
    # Create a method in dict class
    def dict_value_from_key(self, key):
        # return the value for the specified key
        # in the dictionary
        return self[key]
    obj_1['dict_value_from_key'] = dict_value_from_key
    # Create an object of "file" class
    obj_2 = file()
    # Register two objects with JsonRpcServer class
    jsonrpc.register(obj_1)
    jsonrpc.register(obj_1)
    # Create request dictionary

# Generated at 2022-06-13 16:34:28.628610
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    j = JsonRpcServer()
    request = {"jsonrpc": "2.0", "method": "echo", "params": {"args": ["hello, world"], "kwargs": {}}, "id": "1"}
    request = json.dumps(request)
    expected_response = '{"jsonrpc": "2.0", "result": "hello, world", "id": "1"}'
    assert j.handle_request(request) == expected_response
    j.register(JsonRpcServer())
    request = {"jsonrpc": "1.0", "method": "echo", "params": {"args": ["hello, world"], "kwargs": {}}, "id": "1"}
    request = json.dumps(request)

# Generated at 2022-06-13 16:34:41.379703
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import unittest
    class Test(unittest.TestCase):
        @staticmethod
        def _check_JsonRpcServer_handle_request_error_method_not_found(json_req_str, code, message):
            json_server = JsonRpcServer()
            json_response = json.loads(json_server.handle_request(json_req_str))
            assert json_response['jsonrpc'] == '2.0'
            assert json_response['error']['code'] == code
            assert json_response['error']['message'] == message


# Generated at 2022-06-13 16:34:50.279575
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    server = JsonRpcServer()
    request = {
        "jsonrpc": "2.0",
        "method": "rpc.Dummy",
        "id": "9caa18a6-28d6-4fb8-b33f-c1ddcc5d5eb0",
        "params": [
            10,
            20
        ]
    }
    request_str = json.dumps(request)

    response_str = server.handle_request(request_str)
    response = json.loads(response_str)
    assert response['error']['code'] == -32601
    assert response['error']['message'] == 'Method not found'

    server.register(Dummy())
    response_str = server.handle_request(request_str)

# Generated at 2022-06-13 16:34:56.700690
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = '{"jsonrpc": "2.0", "method": "foobar", "params": [1, 2, 3], "id": "1"}'
    result = JsonRpcServer().handle_request(request)
    assert result == json.dumps({"id": "1", "error": {"code": -32601, "message": "Method not found"}, "jsonrpc": "2.0"})


# Generated at 2022-06-13 16:35:02.383920
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    # setup of variables
    rpc_server = JsonRpcServer()
    rpc_server._identifier = "1"
    request = '{"jsonrpc": "2.0", "method": "say_hello", "params": ["2",3], "id": "1"}'
    expected_result = '{"id": "1", "jsonrpc": "2.0", "result": "Hello2 3"}'

    # test of method
    result = rpc_server.handle_request(request)

    # assert of results
    assert result == expected_result
