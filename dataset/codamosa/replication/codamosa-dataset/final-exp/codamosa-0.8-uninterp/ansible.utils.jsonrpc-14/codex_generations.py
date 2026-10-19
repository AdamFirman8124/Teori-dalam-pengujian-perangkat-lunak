

# Generated at 2022-06-13 16:25:20.011477
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    
    class Plugin:
        def to_text(self, *args, **kwargs):
            return 'test handle_request of JsonRpcServer'

    class TestJsonRpcServer(JsonRpcServer):
        def internal_error(self, data=None):
            return 'test internal_error'

        def response(self, result=None):
            return 'test response'

        def error(self, code, message, data=None):
            return 'test error'

    json_rpc_server = TestJsonRpcServer()
    json_rpc_server.plugin = Plugin()
    json_rpc_server.register(json_rpc_server.plugin)

    # Test invalid request

# Generated at 2022-06-13 16:25:22.442381
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    response = JsonRpcServer().error(code=1, message="Something")
    assert response["error"]["code"] == 1
    assert response["error"]["message"] == "Something"


# Generated at 2022-06-13 16:25:30.263246
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.connection import ConnectionError
    import json

    class TestClass1(object):
        def test_method(self, *args, **kwargs):
            return args, kwargs

    class TestClass2(object):
        def test_method2(self, *args, **kwargs):
            return args, kwargs

    class TestClass3(object):
        def test_method(self, *args, **kwargs):
            raise ConnectionError(1, 'test_method exception')

    class TestClass4(object):
        def test_method(self, *args, **kwargs):
            raise Exception('test_method exception')

    server = JsonRpcServer()

    server.register(TestClass1())
    server.register(TestClass2())
    server.register(TestClass3())


# Generated at 2022-06-13 16:25:40.771861
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    test_request = '{"method":"yum_list","id":12345}'

    # Expected returns when server is unresolved
    result1 = '{"id": 12345, "jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}}'
    result2 = '{"id": 12345, "jsonrpc": "2.0", "error": {"code": -32603, "message": "Internal error"}}'

    # Mark server as unresolved
    JsonRpcServer._objects = set()

    jrss = JsonRpcServer()
    received1 = jrss.handle_request(test_request)
    received2 = jrss.handle_request(test_request)

    assert result1 == received1
    assert result2 == received2

    # JsonRpcServer

# Generated at 2022-06-13 16:25:49.008723
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    # Test if the JsonRpcServer response with correct header
    header = {'jsonrpc': '2.0', 'id': 1}
    result = {'test': True}
    response = {'result': {'test': True}, 'jsonrpc': '2.0', 'id': 1}
    jsr = JsonRpcServer()
    setattr(jsr, '_identifier', 1)
    assert jsr.response(result) == response


# Generated at 2022-06-13 16:25:56.295509
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    _dict = {
        "error": {
            "code": -32700,
            "message": "Parse error"
        },
        "id": 1,
        "jsonrpc": "2.0"
    }
    _json = json.dumps(_dict)
    obj = JsonRpcServer()
    obj._identifier = 0
    _send = obj.response(data=None)
    assert _send == _json

# Generated at 2022-06-13 16:26:00.592174
# Unit test for method error of class JsonRpcServer
def test_JsonRpcServer_error():
    server = JsonRpcServer()
    setattr(server, '_identifier', to_text(123))
    result = server.error(-32603, 'Internal error', 'data')
    print(result)
    assert result == {'jsonrpc': '2.0', 'id': '123', 'error': {'code': -32603, 'message': 'Internal error', 'data': 'data'}}

# Generated at 2022-06-13 16:26:11.738891
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Create an object of class JsonRpcServer
    obj = JsonRpcServer()

    # Create an object of class One for help in testing (with a valid test function)
    class One:
        def one(self, a, b):
            return a + b

    # Creating an instance of class One
    obj_one = One()

    # Register the One class to the list of objects of JsonRpcServer
    obj.register(obj_one)

    # Test the result of a request with valid method and parameters (the 'parse_error' method)
    request = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': 'parse_error'})

# Generated at 2022-06-13 16:26:16.691761
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = '{"jsonrpc": "2.0", "method": "test", "params": [], "id": 1}'
    server = JsonRpcServer()
    result = server.handle_request(request)
    assert isinstance(result, text_type)
    assert result == '{"error": {"code": -32601, "message": "Method not found"}, "id": 1, "jsonrpc": "2.0"}'

# Generated at 2022-06-13 16:26:27.952079
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    foo = type('Foo', (object,), {
        'bar': lambda self, a, b: a + b,
        'baz': lambda self, a, b: a + b,
    })()

    server = JsonRpcServer()
    server.register(foo)

    request = json.dumps({
        "jsonrpc": "2.0",
        "method": "bar",
        "params": [[1, 2], {}],
        "id": "2"
    })

    response = server.handle_request(request)
    assert "Invalid request" not in response
    assert "Internal error" not in response
    assert "Method not found" not in response
    assert json.loads(response)["result"] == 3
    assert json.loads(response)["id"] == "2"


# Generated at 2022-06-13 16:26:32.697508
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    return 0

# Generated at 2022-06-13 16:26:35.512228
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # setup
    print("Setup")

    # execute
    print("Execute")

    # verify
    print("Verify")

    # cleanup
    print("Cleanup")

# Generated at 2022-06-13 16:26:45.136913
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    '''
    Ansible's JsonRpcServer.response() method returns a dictionary, having
    the following keys:

        "jsonrpc": string
        "id": int or string (depends on the call)
        "result": string (if pickle serialized) or any object (if not serialized)
        "result_type": string (if pickle serialized)

    This test makes sure "jsonrpc" is a string, "id" is an integer, "result"
    is a string and "result_type" is "pickle", for pickle serialized objects.
    '''
    test_jsonrpc_server = JsonRpcServer()
    test_dictionary = {'key1': 'value1'}
    test_jsonrpc_server.register(test_dictionary)
    test_jsonrpc_server

# Generated at 2022-06-13 16:26:51.792973
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = r'''{"jsonrpc": "2.0", "method": "test", "params": [], "id": 1}'''
    server = JsonRpcServer()
    response = server.handle_request(request)
    assert json.loads(response) == {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": 1}



# Generated at 2022-06-13 16:27:02.302242
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.network.common.utils import to_list
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    jrpc = JsonRpcServer()
    class ActionModule(_ActionModule):
        def __init__(self, *args, **kwargs):
            pass
        def run(self, tmp=None, task_vars=None):
            pass
    jrpc.register(ActionModule)


# Generated at 2022-06-13 16:27:09.381344
# Unit test for method response of class JsonRpcServer
def test_JsonRpcServer_response():
    server = JsonRpcServer()
    setattr(server, '_identifier', '123-abc')
    response = server.response('success')
    assert response == {'jsonrpc': '2.0', 'id': '123-abc', 'result': 'success'}
    response = server.response({'a':'b'})
    assert response == {'jsonrpc': '2.0', 'id': '123-abc', 'result_type': 'pickle', 'result': "cs'a'pt2\nRp1\n(U'a'\nNU'b'\ntp3\nRp4\n."}
    response = server.response(b'b')

# Generated at 2022-06-13 16:27:19.031140
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc_server = JsonRpcServer()
    class Test:
        def __init__(self):
            pass

        def hello(self):
            return "Hi there!"

        def hi(self):
            return "Hi there!"

        def hello_there(self):
            return "Hi there!"

        def hola(self):
            return "Hi there!"

        def echo(self, some_text):
            return some_text

        def no_func(self):
            return "Hi there!"


# Generated at 2022-06-13 16:27:28.487957
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.network_common import load_provider
    from ansible.module_utils.network_common import NetworkModule

    task_vars = dict(
        ansible_connection='network_cli',
        ansible_network_os='junos',
        ansible_become=True,
        ansible_become_method='enable',
        ansible_become_pass='foo',
        ansible_ssh_user='foo',
        ansible_ssh_pass='bar'
    )

    source = load_provider('junos')
    source.params = dict()
    source.params['provider'] = dict()
    source.params['provider']['transport'] = task_vars['ansible_connection']

# Generated at 2022-06-13 16:27:40.785518
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    """Unit test for method handle_request of class JsonRpcServer"""
    from ansible.module_utils.network.netconf.netconf import NetconfConnection

    conn = NetconfConnection()
    jsonrpc_server = JsonRpcServer()

    conn.register_jsonrpc_server(jsonrpc_server)

    # Test RPC methods that do not take any arguments
    request = '{"jsonrpc": "2.0", "method": "rpc.lock", "id": 1}'
    response = '{"jsonrpc": "2.0", "id": 1, "result": "configuration locked"}'
    assert jsonrpc_server.handle_request(request) == response

    request = '{"jsonrpc": "2.0", "method": "rpc.unlock", "id": 1}'
   

# Generated at 2022-06-13 16:27:46.974243
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    id = 1
    # register a class with method 'add'
    class cls:
        def add(self, a, b):
            return a + b
    server.register(cls())
    # normal json-rpc request
    request = '{"jsonrpc":"2.0", "id":' + str(id) + ', "method":"add", "params":[0, 1]}'
    response = server.handle_request(request)
    assert json.loads(response) == {"jsonrpc": "2.0", "result": 1, "id": id}
    # json-rpc request without parameters
    request = '{"jsonrpc":"2.0", "id":' + str(id) + ', "method":"_"}'
    response = server.handle_request(request)

# Generated at 2022-06-13 16:27:58.711068
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    test_request = '{"jsonrpc": "2.0", "method": "hello", "params": {"arg1": "value1"}, "id": 1}'
    test_response = '{"jsonrpc": "2.0", "result": "hello", "id": 1}'
    jsonrpc_server = JsonRpcServer()

    # registering a mock class with method hello
    class Mock(object):
        def hello(self, *args, **kwargs):
            return "hello"
    jsonrpc_server.register(Mock())

    assert jsonrpc_server.handle_request(test_request) == test_response


# Generated at 2022-06-13 16:28:04.805521
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = {"jsonrpc": "2.0", "method": "rpc.test", "params": [], "id": "1"}
    response = {"jsonrpc": "2.0", "id": "1", "error": {"code": -32600, "message": "Invalid request", "data": None}}
    assert json.loads(JsonRpcServer().handle_request(request)) == response


# Generated at 2022-06-13 16:28:16.324478
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Instantiate the object
    obj = JsonRpcServer()

    # Test function handle_request of class JsonRpcServer
    method = "rpc.test_jsonrpc_server"

    params = ["jsonrpc_server"]
    params_json = {"params": [params], "method": method, "id": "test_id"}
    json_obj = json.dumps(params_json)
    data = obj.handle_request(json_obj)
    json_data = json.loads(data)
    if json_data['result'] != "jsonrpc_server":
        raise Exception("Error: The result is not correct")

    params = [""]
    params_json = {"params": [params], "method": method, "id": "test_id"}

# Generated at 2022-06-13 16:28:25.138696
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # create the server object
    obj = JsonRpcServer()
    # create the rpc_object
    rpc_obj = object()
    # register the rpc_object in the server object
    obj.register(rpc_obj)
    # create the rpc_method that will be called by handle_request method
    def test_method(arg1, arg2):
        assert arg1 == 'hello_arg1'
        assert arg2 == 'hello_arg2'
        return 'hello_result'
    # add the rpc_method to the rpc_obj
    setattr(rpc_obj, 'test_method', test_method)
    # create the request
    arg1 = 'hello_arg1'
    arg2 = 'hello_arg2'

# Generated at 2022-06-13 16:28:32.793481
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.remote_management.network.nxos import cli, nxapi

    jrpc = JsonRpcServer()
    jrpc.register(cli)


# Generated at 2022-06-13 16:28:42.300962
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    js = JsonRpcServer()
    from ansible.module_utils.network.junos.junos import load_config, load_candidate_config, commit_configuration, Connection
    from ansible.module_utils.network.junos.junos import junos_argument_spec, check_args
    from ansible.module_utils.network.common.utils import load_provider, validate_provider_dict, remove_default_spec
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network.common.config import NetworkConfig

# Generated at 2022-06-13 16:28:51.432415
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    server._objects = ['abc']

    request = '{"method":"abc", "params":[]}'
    result = server.handle_request(request)
    result = json.loads(result)
    assert result == {'jsonrpc': '2.0', 'result': '234'}

    request = '{"method":"abc", "params":[[], {}]}'
    result = server.handle_request(request)
    result = json.loads(result)
    assert result == {'jsonrpc': '2.0', 'result': '234'}

    request = '{"method":"abc", "params":[[1], {1:"1"}]}'
    result = server.handle_request(request)
    result = json.loads(result)

# Generated at 2022-06-13 16:28:52.711358
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass


# Generated at 2022-06-13 16:29:01.610189
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()

    class TestClass(object):
        def return_one_param(self, first_param, second_param):
            return 'first_param = {} second_param = {}'.format(first_param, second_param)

    server.register(TestClass())

    result = server.handle_request('{"jsonrpc": "2.0", "method": "return_one_param", "params": ["test", "test"], "id": 1}')
    result = json.loads(result)
    assert result['result'] == 'first_param = test second_param = test'

    result = server.handle_request('{"jsonrpc": "2.0", "method": "return_one_param", "params": [1], "id": 2}')
    result = json.loads(result)
   

# Generated at 2022-06-13 16:29:06.812472
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    msg = server.handle_request(b'''{"jsonrpc": "2.0", "method": "hello", "params": [1,2,3], "id": "123"}''')
    msg = json.loads(msg)
    assert msg['error']['code'] == -32601



# Generated at 2022-06-13 16:29:19.410886
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jsonrpc = JsonRpcServer()
    request = {
        "jsonrpc": '2.0',
        "id": 1,
        "method": 'login',
        "params": ['user','pass']
    }
    string_request='{"jsonrpc": "2.0", "id": 1, "method": "login", "params": ["user","pass"]}'
    assert jsonrpc.handle_request(string_request) == '{"jsonrpc": "2.0", ' + \
                                         '"id": 1, "error": ' + \
                                         '{"code": -32601, ' + \
                                         '"message": "Method not found"}}'

# Generated at 2022-06-13 16:29:25.990774
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    rpc = JsonRpcServer()
    rpc.register(Display())
    rpc.register(ConnectionError())
    request = '''{
        "jsonrpc": "2.0",
        "method": "vvv",
        "id": 1,
        "params": ["text"]
    }'''

    response = rpc.handle_request(request)

    print(response)


# Generated at 2022-06-13 16:29:30.104175
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    request = '{"jsonrpc": "2.0", "method": "echo", "params": ["foo", "bar"], "id": 1}'
    response = server.handle_request(request)
    assert response == '{"result":"foo bar","id":1,"jsonrpc":"2.0"}'

# Generated at 2022-06-13 16:29:39.399663
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    object = object()
    object.message = 'test message'
    server.register(object)

    import socket
    address = ('localhost', 5555)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(1)

    def handle_debug_print(data):
        print('Debug:', data)

    def handle_server_listen(server_socket):
        print('Waiting for a connection')
        connection, client_address = server_socket.accept()
        print('Connection from', client_address)

        data = connection.recv(1024)
        request = server.handle_request(data)
        print('Request:', request)

        connection.send

# Generated at 2022-06-13 16:29:45.990312
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()
    obj1 = type("obj1", (), {"test": lambda self: 'Hello World'})
    obj1 = obj1()
    server.register(obj1)
    jsonString = '{"jsonrpc": "2.0", "method": "test", "params": {}, "id": 1}'
    response = server.handle_request(jsonString)
    assert response == '{"jsonrpc": "2.0", "id": 1, "result": "Hello World"}'

# Generated at 2022-06-13 16:29:54.400955
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import get_file_content
    test_handle_requests = get_file_content(__file__, "tests/unit/utils/jsonrpc/jsonrpc_handle_requests.json")
    tests = test_handle_requests['tests']
    for test in tests:
        # Create instance of JsonRpcServer for each testcase
        server = JsonRpcServer()
        # Register module object for use in rpc calls
        server.register(server)
        request = test['request']
        # Call method handle_request with request
        response = server.handle_request(request)
        # Convert response to dict
        response_dict = json.loads(response)
        expected_response = test['expected_response']


# Generated at 2022-06-13 16:30:03.753465
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.network.common.cfg.base import ConfigBase
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.module_utils.network.ios.providers.providers import CliProvider

    rpc = JsonRpcServer()
    config = ConfigBase()

    provider = CliProvider()
    provider.load_provider()
    load_provider(provider, {'transport': 'cli'})
    config._provider = provider

    assert rpc
    assert config

    rpc.register(config)

    request = '{"method": "run", "params": [["show version"], {}], "id": 1}'

    response = rpc.handle_request(request)
    assert response


# Generated at 2022-06-13 16:30:13.885554
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Initialize a new JsonRpcServer class object
    server = JsonRpcServer()
    # Unit test for the method _handle_request()
    request = {
        'jsonrpc': '2.0',
        'method': 'is_alive',
        'params': ([], {}),
        'id': 'some_id'
    }
    request = json.dumps(request)
    assert server.handle_request(request) == '{"jsonrpc": "2.0", "id": "some_id", "result": "{\\\\"result_type\\\\": \\"pickle\\\\", \\"result\\\\": \\"K\\\\001.\\u000b."}"}'



# Generated at 2022-06-13 16:30:20.837722
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():


    # Create an instance of JsonRpcServer
    jsrvr = JsonRpcServer();
    assert(isinstance(jsrvr, JsonRpcServer))

    # Create a fake request
    request = {'method': '__init__', 'params': [], 'id': 0}

    # Call method handle_request with our fake request
    result = jsrvr.handle_request(json.dumps(request))

    assert(isinstance(result, str))
    result = json.loads(result)

    assert(isinstance(result, dict))
    assert('jsonrpc' in result)
    assert('id' in result)
    assert('error' in result)

    assert(result['jsonrpc'] == u'2.0')
    assert(result['id'] == 0)

# Generated at 2022-06-13 16:30:32.227605
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    message = b'''{"method":"get_config","params":[],"id":1}'''
    server = JsonRpcServer()
    response = server.handle_request(message)
    assert response == '{"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "Method not found"}}'

    class Module:
        def get_config(*args):
            return dict(jsonrpc='2.0', id=1, result='''gigabitEthernet1/10
 description ansible test
 duplex full''')

    server.register(Module())
    response = server.handle_request(message)

# Generated at 2022-06-13 16:30:44.591012
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import sys
    import unittest
    from unittest.mock import Mock

    from ansible.module_utils.six import StringIO
    from ansible.module_utils.connection import ConnectionError

    class FakeModule(object):
        def __init__(self):
            self.params = {}
            self.result = {}

    def handle_response_1():
        return  {'jsonrpc': '2.0', 'id': 1, 'result': True}

    def handle_response_2():
        return  {'jsonrpc': '2.0', 'id': 2, 'result': "Hello"}

    def handle_response_3():
        return  {'jsonrpc': '2.0', 'id': 3, 'result': "Hello"}


# Generated at 2022-06-13 16:30:51.034583
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = {"jsonrpc": "2.0", "method": "test", "params": [4, [3, 2, 1]], "id": 2}
    request = json.dumps(request)
    class Dummy:
        def test(self, a, b):
            return to_text(sum(b))
    server = JsonRpcServer()
    server.register(Dummy())
    assert "6" == server.handle_request(request)

# Generated at 2022-06-13 16:31:00.294179
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    server = JsonRpcServer()

    # request with wrong method name
    request = {
        'jsonrpc': '2.0',
        'id': '18',
        'method': '_version',
        'params': [
            [],
            {},
        ],
    }
    request = json.dumps(request)
    response = server.handle_request(request)
    assert json.loads(response) == {
        'jsonrpc': '2.0',
        'id': '18',
        'error': {
            'code': -32600,
            'message': 'Invalid request',
        }
    }

    # correct request

# Generated at 2022-06-13 16:31:10.125919
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Test1(object):
        pass

    class Test2(object):
        pass

    test1 = Test1()
    test2 = Test2()

    test1.test = lambda: "result"
    test2._test = lambda: "result"

    jr = JsonRpcServer()
    jr.register(test1)
    jr.register(test2)

    result = jr.handle_request('{"id": 1, "method": "test", "params": [1, 2]}')
    assert result == '{"id": 1, "result_type": "pickle", "result": "S\\\'result\'", "jsonrpc": "2.0"}'

    result = jr.handle_request('{"id": 1, "method": "_test", "params": [1, 2]}')
    assert result

# Generated at 2022-06-13 16:31:15.786102
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Creating instance of class JsonRpcServer
    obj = JsonRpcServer()

    # Creating request
    method = 'hello'
    data = '{"method": "hello", "params": [[]], "id": 1}'

    # Unit test: handle_request with json object
    request = json.loads(to_text(data))
    response = obj.handle_request(request)
    assert response == '{"error": {"code": -32601, "message": "Method not found"}, "id": 1, "jsonrpc": "2.0"}'

    def add_method(obj, method):
        def hello(self):
            return None
        setattr(obj, method, hello)

    # Adding method to the request
    add_method(obj, 'hello')

    # Unit test: handle_request with json object


# Generated at 2022-06-13 16:31:26.486628
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
  import unittest
  from ansible.module_utils.connection import Connection

  class TestServer(object):
      """ test class to be used in json rpc server """
      def method(self, *args, **kwargs):
          return "Hello World!"

  server = JsonRpcServer()
  server.register(TestServer())
  request = {
              'jsonrpc': '2.0',
              'id': '0',
              'method': 'method',
              'params': ([], {})
              }
  server.handle_request(json.dumps(request))

  class TestServer(object):
      """ test class to be used in json rpc server """
      def method(self, *args, **kwargs):
          raise Exception("General Exception")

  server = JsonRpcServer()
  server.register

# Generated at 2022-06-13 16:31:37.298027
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.connection import ConnectionError

    req = dict(method='test_handle_request', params=[tuple(), dict()])
    request = json.dumps(req)

    # expected result
    res = dict(jsonrpc='2.0', id=None, result=True)
    expected_result = json.dumps(res)

    test_module = dict(
        argument_spec=dict(),
        supports_check_mode=False
    )

    def test_handle_request(*args, **kwargs):
        raise ConnectionError('connection error')

    am = AnsibleModule(**test_module)
    c = Connection(am)
    c.test_handle_request = test_

# Generated at 2022-06-13 16:31:45.023850
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import sys
    import ansible.module_utils.network.nso.nso as nso
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network.nso.nso import NSOClient
    import ansible.module_utils.network.nso.nso as nso_client

    #configuring nso client
    nso_host = '127.0.0.1'
    nso_port = '8080'
    nso_username = 'admin'
    nso_password = 'test'
    display.vvvv(sys._getframe().f_code.co_name, "NSO_CLIENT:", nso_client)

# Generated at 2022-06-13 16:31:53.626046
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = """
        {"jsonrpc": "2.0", "method": "system.connect", "params": [], "id": 1}
    """
    import sys
    from ansible.module_utils.network.common.utils import Connection
    from ansible.module_utils.connection import ConnectionError
    from ansible.module_utils.six.moves import input
    from ansible.module_utils.select import select

    class Test(object):

        def system_hello(self, *args, **kwargs):
            return 'world'

        def connect(self, *args, **kwargs):
            if kwargs.get('key') == 'test_error':
                raise ConnectionError(msg='test error')

            return dict(jsonrpc='2.0', result=None, error=None)

    # FIXME (

# Generated at 2022-06-13 16:31:56.237013
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = dict(method="test_method")
    response = json.dumps(request)
    assert JsonRpcServer().handle_request(response) == response

# Generated at 2022-06-13 16:32:11.270459
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.six.moves import cPickle as pickle


    class TestModule(object):

        def get_config(self):
            return '#'

        def load_config(self, config):
            return '!'

    # prepare correct JSON-RPC request to load_config method
    identifier = 123
    method = 'load_config'
    params = ['#']
    request = {'id': identifier, 'method': method, 'params': params}
    request = json.dumps(request)
    # create server and test correct request
    server = JsonRpcServer()
    server.register(TestModule())
    response = server.handle_request(request)
    response = json.loads(response)
    assert response["id"] == identifier
    assert response["result"] == '!'
    #

# Generated at 2022-06-13 16:32:18.657257
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    class Sample(object):
        def echo(self, *args, **kwargs):
            return args, kwargs

        def raises(self):
            raise Exception('test')

    server = JsonRpcServer()
    server.register(Sample())

    result = server.handle_request(json.dumps(dict(id=1, method='echo', params=(1, 2, 3))))
    result = json.loads(result)

    assert result['id'] == 1
    assert result['jsonrpc'] == '2.0'
    assert result['result'] == [1, 2, 3]

    result = server.handle_request(json.dumps(dict(id=1, method='raises', params={})))
    result = json.loads(result)

    assert result['id'] == 1

# Generated at 2022-06-13 16:32:29.787610
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    """This will test the handle_request() function of the
    JsonRpcServer class. This is a unit test the way it is build.
    """
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.ajson import AnsibleJSONEncoder

    rpc_server = JsonRpcServer()

    # Test 1:
    #   This will test the response of a successful echo request.
    test_value = "TestValue"

    def echo(value):
        return value

    rpc_server.register(echo)
    request = json.dumps({
        'jsonrpc': '2.0',
        'method': 'echo',
        'params': [test_value],
        'id': 0
    }, cls=AnsibleJSONEncoder)
    response = rpc

# Generated at 2022-06-13 16:32:39.710424
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import unittest
    import sys
    import ansible.module_utils.shell.ansible_shell_common as common
    sys.path.insert(0, '..')
    import shell

    class TestJsonRpcServer(unittest.TestCase):
        """
        Test handle_request of class JsonRpcServer
        """
        def setUp(self):
            self.obj = shell.ShellModule()
            self.json_rpc = JsonRpcServer()
            self.json_rpc.register(self.obj)

        def test_handle_request_1(self):
            """
            Test handle_request with valid request
            """
            request = '{"method": "has_capability", "params": ["shell_capability"], "id": 1}'

# Generated at 2022-06-13 16:32:42.792938
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jsrs = JsonRpcServer()
    cmd_request = {'jsonrpc': '2.0', 'method': 'exec_command',
                   'params': [['show version']], 'id': 24}
    try:
        jsrs.handle_request(cmd_request)
    except Exception as e:
        if "object has no attribute" in str(e):
            return True
        else:
            raise e
    return False

# Generated at 2022-06-13 16:32:50.824157
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import tempfile
    import sys
    # Create temporary file to redirect stdout
    temp = tempfile.TemporaryFile(mode='w+')
    sys.stdout = temp
    # Test handle_request
    request = '{ "params": [ [ "1_test_1" ], { "a": "test_a" } ], "method": "test_method", "jsonrpc": "2.0", "id": 0 }'
    rpc = JsonRpcServer()
    rpc.register(TestObject())
    # Output of method handle_request
    output = rpc.handle_request(request)
    # Test invalid_request method

# Generated at 2022-06-13 16:32:59.008657
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
  import json
  import unittest

  class Foo(object):
      def baz(self, *args, **kwargs):
          return 'OK'

  class TestJsonRpcServer(unittest.TestCase):

      def test_handle_request(self):
          request = '{"jsonrpc": "2.0", "method": "baz", "params": [], "id": "1"}'
          server = JsonRpcServer()
          server.register(Foo())
          expected = '{"jsonrpc":"2.0","id":"1","result":"OK"}'
          self.assertEqual(json.loads(server.handle_request(request)),
              json.loads(expected))

  return unittest.TestSuite([TestJsonRpcServer('test_handle_request')])

# Unit test

# Generated at 2022-06-13 16:33:05.181072
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Create a new instance of JsonRpcServer
    json_obj = JsonRpcServer()

    # Case 1: Test for method_not_found exception
    request = json.dumps({
        "jsonrpc": "2.0",
        "method": "run_command",
        "params": ["show version"],
        "id": 1
    })
    result = json_obj.handle_request(request)
    assert json.loads(result) == {
        'id': 1,
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found',
            'data': None,
        }
    }

    # Case 2: Test for result

# Generated at 2022-06-13 16:33:13.155967
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    # handle_request - Test
    # Check handle_request when method starts with rpc.
    # Expected result: error with code -32600 and message "Invalid request"
    request = {"jsonrpc" : "2.0", "method" : "rpc.test", "id" : "123"}
    expected = {"jsonrpc" : "2.0", "error" : { "code" : -32600, "message" : "Invalid request"}, "id" : "123"}
    result = JsonRpcServer().handle_request(json.dumps(request))
    assert result == json.dumps(expected)

    # handle_request - Test
    # Check handle_request when method starts with _.
    # Expected result: error with code -32600 and message "Invalid request"

# Generated at 2022-06-13 16:33:13.862466
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    pass


# Generated at 2022-06-13 16:33:26.836025
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    jr = JsonRpcServer()
    assert jr.handle_request('{"jsonrpc": "2.0", "method": "rpc.echo"}') == '{"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid request"}, "id": null}'
    assert jr.handle_request('{"jsonrpc": "2.0", "method": "_echo"}') == '{"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid request"}, "id": null}'

# Generated at 2022-06-13 16:33:38.808212
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # Create a server object for testing
    server = JsonRpcServer()
    # Create a request
    request_text={"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}
    request_text = json.dumps(request_text)
    # Create a parameter object to be used in testing
    class MyObj(object):
        def subtract(self, a, b):
            return a - b
    my_obj = MyObj()
    # Register the parameter object
    server.register(my_obj)
    # Call the method and save the result
    result = server.handle_request(request_text)
    # Create the reference result.

# Generated at 2022-06-13 16:33:43.921117
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    json_rpc = JsonRpcServer()
    # invalid request
    assert json_rpc.handle_request({})
    # method not found
    assert json_rpc.handle_request(json.dumps({'jsonrpc': '2.0', 'method': 'foo', 'params': {}})) == '{"jsonrpc": "2.0", "id": "None", "error": {"data": null, "message": "Method not found", "code": -32601}}'
    # internal error
    json_rpc.register(object())

# Generated at 2022-06-13 16:33:51.073076
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    from ansible.module_utils.network.common.netconf import NetconfConnection
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.module_utils.network.nxos.nxos import get_connection
    from ansible.module_utils.network.common.providers.nxapi.provider import NxapiProvider
    from ansible.module_utils.network.common.providers.nxos.provider import CliProvider
    from ansible.module_utils.network.common.providers.nxos.provider import NxosProvider

    obj_conn = NetconfConnection(load_provider(get_connection({}, {})))
    obj_conn._provider = NxapiProvider(obj_conn._device)
    obj_conn._provider._cli_prov

# Generated at 2022-06-13 16:33:52.548990
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
	pass


# Generated at 2022-06-13 16:33:56.806712
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    request = {
        'jsonrpc': '2.0',
        'id': '123',
        'method': 'test',
        'params': {'args': ['arg1'], 'kwargs': {}}
    }

    # assert handle_request(request) == expected


# Generated at 2022-06-13 16:34:06.371782
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    '''
    unit test for method handle_request of class JsonRpcServer
    '''
    class MyClass(object):
        '''
        class to test methods
        '''
        def my_method(self, *args, **kwargs):
            '''
            my_method
            '''
            return args, kwargs

        def my_method2(self, *args, **kwargs):
            '''
            my_method 2
            '''
            return args, kwargs

        def _my_method3(self, *args, **kwargs):
            '''
            my_method 3
            '''
            return args, kwargs

    json_rpc = JsonRpcServer()
    instance = MyClass()
    json_rpc.register(instance)

    # test a method without

# Generated at 2022-06-13 16:34:15.158461
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    """
    Unit test for method handle_request of class JsonRpcServer
    """

    result = {}

    result["truncate_method"] = {
        "params": [[], {}],
        "method": "rpc.truncate_method",
        "id": 1
    }

    result["method_not_found"] = {
        "params": [[], {}],
        "method": "method_not_found",
        "id": 1
    }

    result["invalid_request"] = {
        "params": [[], {}],
        "method": "invalid_request",
        "id": 1
    }

    result["connection_error"] = {
        "params": [[], {}],
        "method": "connection_error",
        "id": 1
    }


# Generated at 2022-06-13 16:34:27.873828
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():

    # This is a dummy class which contains function of ErrorHandler 
    class ErrorHandler():

        def _check_args(self):
            pass

        def _load_provider(self):
            pass

        def run(self):
            pass

        def get(self):
            pass

    # This is a dummy class which contains function of CliHandler 
    class CliHandler():

        def run(self):
            pass

        def run_commands(self):
            pass

    # This is a dummy class which contains function of HttpAPIHandler 
    class HttpAPIHandler():

        def run(self):
            pass

        def run_commands(self):
            pass

    # This is a dummy class which contains function of ConfigModule 
    class ConfigModule():

        def run(self):
            pass


# Generated at 2022-06-13 16:34:37.269984
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    # module_exit is mocked and ensure_connect is set to true
    module_exit = JsonRpcServer.module_exit
    JsonRpcServer.module_exit = lambda: True
    JsonRpcServer.ensure_connect = lambda: True

    # Create a new instance of the class
    jsonRpcServer = JsonRpcServer()

    # Create a mock for the method register that does nothing
    def mock_register():
        pass

    # Replace the original method with the mock
    jsonRpcServer.register = mock_register

    # Create a mock for the method read of the NetconfConnection class
    # that returns a request
    def mock_read():
        return '{"id": "ID", "params": [[], {}], "method": "mock_method"}'

    # Replace the original method with the mock
    set

# Generated at 2022-06-13 16:34:59.835931
# Unit test for method handle_request of class JsonRpcServer
def test_JsonRpcServer_handle_request():
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    #from units.compat.mock import patch
    #from units.modules.utils import set_module_args
    from ansible.modules.network.aoscx import aoscx_config

    aoscx_module = aoscx_config.AoscxModule(argument_spec=dict())
    aoscx_module.async_timeout = 15
    aoscx_module.TMOUT = 5

    # Make sure we are not sending environment variables
    aoscx_module