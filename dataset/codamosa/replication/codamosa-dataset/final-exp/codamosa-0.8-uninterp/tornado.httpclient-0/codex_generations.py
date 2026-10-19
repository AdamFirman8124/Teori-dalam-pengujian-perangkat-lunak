

# Generated at 2022-06-22 13:15:14.794996
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():


    class _Response(HTTPResponse):
        def __init__(self, request: HTTPRequest, code: int, buffer: "BytesIO") -> None:
            super().__init__(request, code, buffer=buffer)


    # Use this to make sure we never call `set_result` twice (this can
    # happen if `callback` is called more than once).
    _UNSET = object()


    class MyHTTPClient(AsyncHTTPClient):
        def __init__(self, defaults: Optional[Dict[str, Any]] = None, **kwargs: Any) -> None:
            super().__init__(defaults=defaults, **kwargs)
            self._fetch_result = _UNSET



# Generated at 2022-06-22 13:15:21.570942
# Unit test for method __getattr__ of class _RequestProxy
def test__RequestProxy___getattr__():
    def_dict = {"a": 1, "b": 2}
    req = HTTPRequest("www.baidu.com", "GET", "abc", "abc")
    req_pro = _RequestProxy(req, def_dict)
    assert req_pro.a == 1
    assert req_pro.b == 2
    assert req_pro.request == req
    assert req_pro.defaults == def_dict

test__RequestProxy___getattr__()



# Generated at 2022-06-22 13:15:22.631197
# Unit test for method close of class AsyncHTTPClient
def test_AsyncHTTPClient_close():   
    pass 


# Generated at 2022-06-22 13:15:30.773449
# Unit test for function main
def test_main():
    import doctest
    import sys
    import os
    import pkgutil
    import tornado.httpclient

    # Run the main function via doctest in a subprocess so that it
    # doesn't mess with our HTTPClient instance.
    thisdir = os.path.dirname(__file__)
    testmod = tornado.httpclient
    argv = sys.argv
    args = [sys.executable, "-m", testmod.__name__] + argv[1:]
    with open(os.devnull, "w") as null:
        status = subprocess.call(args, stdout=null, stderr=null)
    if status != 0:
        sys.exit(status)
    return []


# Generated at 2022-06-22 13:15:31.352424
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-22 13:15:32.681212
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():    
    AsyncHTTPClient.fetch_impl(request, callback)


# Generated at 2022-06-22 13:15:34.416519
# Unit test for method fetch_impl of class AsyncHTTPClient
def test_AsyncHTTPClient_fetch_impl():
    pass
    # self.io_loop.run_sync(self.make_client)

# Generated at 2022-06-22 13:15:38.291455
# Unit test for function main
def test_main():
    print(main())

"""
if __name__ == "__main__":
    main()
"""

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    #test_main()

# Generated at 2022-06-22 13:15:40.025249
# Unit test for method initialize of class AsyncHTTPClient
def test_AsyncHTTPClient_initialize():
    assert(isinstance(AsyncHTTPClient().initialize(), None))


# Generated at 2022-06-22 13:15:45.338919
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        pass


# Note: these tests depend on the server running on localhost.
# However, they will run even if the server is not running;
# the only indication that they were skipped is a warning
# message in the test logs.