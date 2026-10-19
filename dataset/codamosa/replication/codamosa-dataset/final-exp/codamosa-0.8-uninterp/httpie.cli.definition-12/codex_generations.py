

# Generated at 2022-06-13 21:19:15.145764
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert 'github' in auth_type_lazy_choices
    assert 'spnego' in auth_type_lazy_choices
    assert 'something' not in auth_type_lazy_choices


# Generated at 2022-06-13 21:19:27.482604
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    for item in _AuthTypeLazyChoices():
        pass

_AUTH_TYPES = _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type', '--auth-plugin',
    metavar='AUTH_TYPE',
    default=AUTH_PLUGIN_DEFAULT,
    choices=_AUTH_TYPES,
    help=f'''
    Specify the authentication mechanism. Supported types:

        {', '.join(plugin_manager.get_auth_plugin_mapping())}

    httpie will attempt to guess the AUTH_TYPE unless the url uses a custom
    scheme.

    Use --auth-type=auto to test for the supported mechanisms.
    '''
)


# Generated at 2022-06-13 21:19:39.959700
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [item for item in _AuthTypeLazyChoices()] == sorted(plugin_manager.get_auth_plugin_mapping().keys())


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The authentication mechanism to be used.

    Currently supported plugins:
    {plugin_manager.get_plugin_help().strip()}

    '''
)


# Generated at 2022-06-13 21:19:42.515942
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(sorted(_AuthTypeLazyChoices())) == sorted(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:19:52.328361
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__(): # noqa: E302
    assert 'basic' in _AuthTypeLazyChoices() # noqa: E501
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'whatever' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:19:53.669593
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    list(_AuthTypeLazyChoices())

# Generated at 2022-06-13 21:19:56.761483
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert "hawk" in choices
    assert "hookem" not in choices


# Generated at 2022-06-13 21:19:59.467704
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    for auth_type in _AuthTypeLazyChoices():
        assert type(auth_type) == str

# Generated at 2022-06-13 21:20:03.370725
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'oauth' not in _AuthTypeLazyChoices()
    # Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2022-06-13 21:20:14.628405
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    # type=AuthPluginTypeValidator(plugin_manager.get_auth_plugin_mapping()),
    type=AuthPluginTypeValidator(_AuthTypeLazyChoices()),
    help='''
    Explicitly specify a Auth plugin by name.

    For example, to force Basic Auth use:

        --auth-type basic

    Do ``http --debug --auth-type=basic -a user https://httpbin.org/get`` to
    obtain the list of supported auth plugins.

    '''
)

basic_auth = auth.add_mutually_exclusive_group()

# Generated at 2022-06-13 21:20:23.230241
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'Basic' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default=DEFAULT_AUTH_PLUGIN_NAME,
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism is chosen based on the provided type.
    The type is always a string. The string is case-insensitive but
    otherwise it is assumed to be an exact match of the plugin's name.
    The default auth type is {default_auth_plugin_name}.
    '''.format(default_auth_plugin_name=DEFAULT_AUTH_PLUGIN_NAME)
)


#######################################################################
# Timeouts
#######################################################################

# ``requests.request`` keyword arguments.
timeout = parser.add_argument_

# Generated at 2022-06-13 21:20:29.939335
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'foo' not in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    If specified, the auth method is explicitly set to the value of
    --auth-type.

    The default is to try to automatically detect the auth type based
    on the provided credentials and the response to the request.

    ''',
)

# Generated at 2022-06-13 21:20:32.435587
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(plugin_manager.get_auth_plugin_mapping().keys()) == list(_AuthTypeLazyChoices())


# Generated at 2022-06-13 21:20:42.468526
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    # Only for testing
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices
    assert len(list(lazy_choices))

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help=f'''
    Specify an authentication type. The following are supported:

        {_get_auth_choices_help_text()}

    By default, HTTPie tries to infer the type from the --auth option value.

    '''
)


# Generated at 2022-06-13 21:20:46.001899
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))


# Generated at 2022-06-13 21:20:47.488321
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:00.783374
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()

# httpie.auth module keyword arguments.
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used (default is "{0}").

    Available types: {1}

    '''.format(
        plugin_manager.get_auth_plugin_mapping().get('basic'),
        ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    )
)

# Generated at 2022-06-13 21:21:12.781404
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. Currently supported:

    ''' + wrap(
        ', '.join(sorted(
            plugin_manager.get_auth_plugin_mapping().keys()))
        )
)

#######################################################################
# Custom headers
#######################################################################

headers = parser.add_argument_group(title='Custom Headers')


# Generated at 2022-06-13 21:21:15.646962
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(AuthTypeLazyChoices()) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:21:28.242622
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'hawk' in choices
    assert 'ntlm' in choices
    assert 'aws4-hmac-sha256' in choices
    assert 'oauth1' not in choices
    assert 'oauth2' not in choices

    # Make sure there is no infinite recursion due to __contains__
    # returning a non-bool
    assert 'basic' in sorted(choices)

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help='''
    Specify the auth mechanism via plugin name. By default,
    HTTPie uses the 'basic' plugin.

    ''',
)

# Generated at 2022-06-13 21:21:34.091893
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    list(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:21:36.814351
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert [item for item in _AuthTypeLazyChoices()] == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:21:38.251379
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:21:45.757665
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    collection = _AuthTypeLazyChoices()
    assert 'digest' in collection
    assert 'digest' not in collection


# Generated at 2022-06-13 21:21:56.776436
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert (list(_AuthTypeLazyChoices()) ==
            sorted(plugin_manager.get_auth_plugin_mapping().keys()))

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication mechanism to be used. The default is `auto` which tries
    to guess it based on the provided URL or any credentials passed via --auth.

    Available choices:

        ''' + ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
)



# Generated at 2022-06-13 21:22:05.951314
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()
    assert 'basic' in lazy_choices
    assert 'custom' in lazy_choices
    assert 'digest' in lazy_choices
    assert 'ignored' not in lazy_choices
    assert any(source_code.startswith(
        'class ' + cls_name + '(')
        for cls_name, source_code in [
            (cls.__name__, inspect.getsource(cls))
            for cls in plugin_manager._plugin_classes
            if cls != httpie.plugins.AuthPlugin
        ]
    )

# Generated at 2022-06-13 21:22:19.568511
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(_AuthTypeLazyChoices()) == list(plugin_manager.get_auth_plugin_mapping().keys())

auth_type = auth.add_argument(
    '--auth-type',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
        Override the authentication mechanism. By default, the authentication
        mechanism is automatically inferred from the provided credentials.

    '''
)

#######################################################################
# Cookies
#######################################################################

cookies = parser.add_argument_group(title='Cookies')

# Generated at 2022-06-13 21:22:23.133289
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'digest' in choices
    assert 'token' in choices
    assert 'no_such_auth_type' not in choices



# Generated at 2022-06-13 21:22:27.748872
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    options = _AuthTypeLazyChoices()
    assert isinstance(options, _AuthTypeLazyChoices)
    assert 'basic' in options
    assert iter(options) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2022-06-13 21:22:30.355953
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    c = _AuthTypeLazyChoices()
    assert 'basic' in c


# Generated at 2022-06-13 21:22:41.125219
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    assert list(choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())
test__AuthTypeLazyChoices___iter__()


# Generated at 2022-06-13 21:22:52.138184
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'Basic' in _AuthTypeLazyChoices()

auth_type = auth.add_argument(
    '--auth-type',
    metavar='',
    default=None,
    choices=_AuthTypeLazyChoices(),
    help='''
    The scheme used to authenticate. This can be used to force basic auth
    when using a URL that looks like it needs digest. Or, it can be used to
    choose a one-time-password auth method when using a URL that looks like it
    needs basic auth. (Currently OTP auth is only available for the "digest"
    type.)

    '''
)

#######################################################################
# SSL
#######################################################################

ssl = parser.add_argument_group(title='SSL')

# Generated at 2022-06-13 21:23:00.661457
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'plugin' in _AuthTypeLazyChoices()
    assert 'abraka' not in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='basic',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Which type of HTTP authentication to use. Currently supported
    types are "basic" and "digest". The default is "basic".

    HTTPie can also load custom authentication types from plugins.
    Check out the plugin docs for more info.

    '''
)

# ``requests.request`` keyword arguments.

# Generated at 2022-06-13 21:23:08.231309
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # Only to test the laziness of __contains__
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert "some_nonexistent_auth_type" not in auth_type_lazy_choices
    assert "basic" in auth_type_lazy_choices
test__AuthTypeLazyChoices___contains__()

auth.add_argument(
    '--auth-type',
    metavar='AUTH_TYPE',
    default='auto',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    The scheme to use for authenticating with the API server.
    The default is {repr('auto')}.

    The following schemes are available:

        {plugin_manager.get_auth_plugin_help()}

    '''
)

# Generated at 2022-06-13 21:23:15.496690
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    empty_auth_plugins = plugin_manager.AuthPluginManager()
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    # Auth plugins are empty
    assert not ('basic' in _AuthTypeLazyChoices(empty_auth_plugins))
    assert not ('digest' in _AuthTypeLazyChoices(empty_auth_plugins))
    assert not ('plugin' in _AuthTypeLazyChoices(empty_auth_plugins))



# Generated at 2022-06-13 21:23:17.336063
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """
    _AuthTypeLazyChoices.__contains__
    """
    assert 'basic' in _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:23:33.288328
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'hawk' in _AuthTypeLazyChoices()
    assert 'oauth1' in _AuthTypeLazyChoices()
    assert 'ntlm' in _AuthTypeLazyChoices()
    assert 'kerberos' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify  which authentication mechanism to use.
    If not provided, the plugin will try to guess based on the --auth option.
    '''
)

# Generated at 2022-06-13 21:23:46.849825
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()


auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    HTTP auth type to use for the request. The default (auto) means the
    following:

    * Basic auth if both username and password are provided.
    * Digest auth if the username is provided and the password is not,
      or has not been provided explicitly with the -a option.
    * No auth if neither the username nor the password is provided.

    ''',
)

# Generated at 2022-06-13 21:23:58.382778
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for method __iter__ of class _AuthTypeLazyChoices."""
    assert list(_AuthTypeLazyChoices()) == list(plugin_manager.get_auth_plugin_mapping().keys())


# Generated at 2022-06-13 21:24:01.186063
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    assert 'basic' in choices

# Generated at 2022-06-13 21:24:28.118755
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()


# Dynamically generated keyword arguments.
auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    Explicitly specify a custom auth plugin to use. The plugin must be
    installed via `pip install httpie-<type>-auth`.

    ''',
)
auth.add_argument(
    '--auth-plugin',
    default=None,
    metavar='MODULE',
    help='''
    Explicitly specify the auth plugin module to use.  The module must be
    installed via `pip install <module>`.

    ''',
)

#######################################################################
# SSL
#######################################################################



# Generated at 2022-06-13 21:24:30.726358
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    if not isinstance(_AuthTypeLazyChoices(), Iterable):
        assert False, 'class _AuthTypeLazyChoices must implement __contains__'

# Generated at 2022-06-13 21:24:33.964737
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    items = []
    i = iter(_AuthTypeLazyChoices())
    while True:
        try:
            items.append(next(i))
        except StopIteration:
            break
    assert sorted(items) == ['basic', 'digest']

# Generated at 2022-06-13 21:24:44.055736
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    choices=_AuthTypeLazyChoices()
)

# Generated at 2022-06-13 21:24:51.678626
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'hawk']

auth.add_argument(
    '--auth-type',
    default=None,
    metavar='TYPE',
    help='''
    Specify the auth mechanism. Defaults to "basic", the standard HTTP
    authentication.

    The following auth types are available:

        {auth_types}

    Use `http --debug` to see the full list of available --auth-type plugins
    and their options.

    '''.format(
        auth_types=', '.join(plugin_manager.get_auth_plugin_mapping())
    )
)

# Generated at 2022-06-13 21:24:53.276289
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:24:54.748213
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'digest' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:25:00.130762
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    # Needed to import the class because of circular import
    from httpie.plugins.manager import PluginManager
    plugin_manager = PluginManager()
    plugin_manager.discover_plugins()
    choices = _AuthTypeLazyChoices()
    assert choices.__contains__('digest') is True
    assert choices.__contains__('non-existent') is False



# Generated at 2022-06-13 21:25:03.967171
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'myauth' in _AuthTypeLazyChoices()


auth_plugin_mapping = _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:25:06.164872
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    # Should match already loaded plugins in plugin_manager
    assert 'basic' in choices
    # Should match plugins in test_packages
    assert 'test_package' in choices
    # Should not match non-existing plugins
    assert 'non-existing' not in choices


# Generated at 2022-06-13 21:25:43.036644
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    name = "__iter__"
    choices = _AuthTypeLazyChoices()
    actual_result = list(choices)
    expected_result = list(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    try:
        assert actual_result == expected_result
    except AssertionError:
        print(f"{name}: FAILED")
        print(f"expected: {expected_result}")
        print(f"actual: {actual_result}")
    else:
        print(f"{name}: PASSED")


# Generated at 2022-06-13 21:25:53.287905
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'oauth2' in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:25:59.415513
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['digest', 'jwt', 'netrc']

auth.add_argument(
    '--auth-type',
    default='auto',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Type of the HTTP auth.

    By default (--auth-type=auto), HTTPie infers the auth type from the
    provided credentials. If only the username is provided (--auth username),
    HTTPie prompts for the password and uses Basic auth. Otherwise, HTTPie
    uses the credentials as a Bearer token (--auth token) and uses the
    Authorization: Bearer HTTP header.

    {_AuthTypeLazyChoices.__doc__}
    '''
)


# Generated at 2022-06-13 21:26:06.856309
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'fake' in _AuthTypeLazyChoices()
    assert 'not-fake' not in _AuthTypeLazyChoices()


auth_type_lazy_choices = _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    choices=auth_type_lazy_choices,
    help='''
    Force the HTTPie to use a specific authentication type. By default,
    HTTPie auto-detects authentication type by looking at the HTTP Authorization
    header and the URL of the request (for Digest auth).

    A value of {digest_auth_type} forces Digest auth.
    '''.format(digest_auth_type=DIGEST_AUTH)
)


# Generated at 2022-06-13 21:26:10.105333
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(_AuthTypeLazyChoices()) == ['digest', 'netrc', 'plugin']

# Generated at 2022-06-13 21:26:22.905173
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():  # noqa: E501
    pass

auth.add_argument(
    '--auth-type',
    choices=_AuthTypeLazyChoices(),
    default=None,
    help='''
    Specify the auth mechanism. The default is "auto" and will attempt to
    do Digest Authentication, falling back to Basic.

    Available types:

        {types}

    '''.format(
        types=wrap(
            ', '.join(sorted(plugin_manager.get_auth_plugin_mapping().keys())),
            60
        ).strip()
    ),
)

digest_auth_group = auth.add_mutually_exclusive_group()

# Generated at 2022-06-13 21:26:37.439470
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    c = _AuthTypeLazyChoices()
    for i in c:
        assert i in c


auth.add_argument(
    '--auth-type', '-t',
    dest='auth_type',
    metavar='{0}',
    choices=_AuthTypeLazyChoices(),
    help='''
    Force usage of a specific authentication type.
    Available auth types: {1}.

    '''.format(
        '/'.join(sorted(
            plugin_manager.get_auth_plugin_mapping().keys()
        )),
        ' '.join(sorted(
            plugin_manager.get_auth_plugin_mapping().keys()
        ))
    ),
)


# Generated at 2022-06-13 21:26:53.672427
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    AuthTypeLazyChoices = _AuthTypeLazyChoices()
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices
    assert 'digest' in AuthTypeLazyChoices


# Generated at 2022-06-13 21:27:02.960002
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert list(plugin_manager.get_auth_plugin_mapping().keys()) == list(_AuthTypeLazyChoices())
    assert 'digest' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    metavar='TYPE',
    dest='auth_plugin_name',
    choices=_AuthTypeLazyChoices(),
    help=f'''
    Choose an authentication plugin. By default, the automatic plugin is
    used, which takes into account the URL and .netrc. Available plugins:

        {_AuthTypeLazyChoices()}

    See `http --help-auth` for details.

    '''
)

# Generated at 2022-06-13 21:27:04.184849
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert list(iter(_AuthTypeLazyChoices())) == ['basic', 'digest']


# Generated at 2022-06-13 21:28:05.440684
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    assert 'basic' in _AuthTypeLazyChoices()

auth.add_argument(
    '--auth-type',
    default='basic',
    metavar='TYPE',
    choices=_AuthTypeLazyChoices(),
    help='''
    The authentication type to be used. The value is used to look up an
    authentication plugin in the `httpie.plugins.auth` namespace.
    For example, `--auth-type digest` would look up the `DigestAuthPlugin`
    plugin class.

    The following built-in plugins are available:

        basic, digest

    To use Basic or Digest authentication without a plugin, just use the
    `--auth` option.

    '''
)

# Generated at 2022-06-13 21:28:11.473143
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """Unit test for method ``__contains__`` of class ``_AuthTypeLazyChoices``"""
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'custom' not in _AuthTypeLazyChoices()
    assert 'nonexistent' not in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:28:14.217846
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    _AuthTypeLazyChoices()



# Generated at 2022-06-13 21:28:19.353907
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    for value in _AuthTypeLazyChoices():
        assert value in _AuthTypeLazyChoices()


# Generated at 2022-06-13 21:28:22.344677
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'basic' in _AuthTypeLazyChoices()

# Generated at 2022-06-13 21:28:34.151916
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_types = _AuthTypeLazyChoices()
    for item in auth_types:
        assert item in _AuthTypeLazyChoices()
    assert set(auth_types) == set(plugin_manager.get_auth_plugin_mapping())


# Generated at 2022-06-13 21:28:45.801319
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type = _AuthTypeLazyChoices()
    assert iter(auth_type) == iter(sorted(plugin_manager.get_auth_plugin_mapping().keys()))



# Generated at 2022-06-13 21:28:49.425075
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins.builtin import AuthBasicPlugin
    assert 'basic' in _AuthTypeLazyChoices()
    plugin = AuthBasicPlugin()
    plugin_manager.deregister(plugin)
    assert 'basic' not in _AuthTypeLazyChoices()
    plugin_manager.register(plugin)

# Generated at 2022-06-13 21:28:52.532186
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    assert sorted(list(iter(_AuthTypeLazyChoices()))) == sorted(list(iter(plugin_manager.get_auth_plugin_mapping().keys())))

# Generated at 2022-06-13 21:28:54.706369
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    assert 'none' in _AuthTypeLazyChoices()
    assert 'basic' in _AuthTypeLazyChoices()
    assert 'digest' in _AuthTypeLazyChoices()
    assert 'disabled' not in _AuthTypeLazyChoices()

