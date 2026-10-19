

# Generated at 2024-06-01 06:16:08.301340
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:16:09.586148
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:16:11.199718
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:16:13.890099
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello world!', for_qs=True) == 'hello+world%21'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode(' ', for_qs=False) == '%20'

# Generated at 2024-06-01 06:16:16.711954
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('hello world', for_qs=False) == 'hello%20world'
    assert unicode_urlencode('hello/world', for_qs=False) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=False) == 'hello%2Bworld'
    assert unicode_urlencode('') == ''

# Generated at 2024-06-01 06:16:20.454456
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode(' ', for_qs=False) == '%20'
    assert unicode_urlencode('a/b/c', for_qs=False) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:16:22.217923
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:24.026880
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:25.348024
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:16:27.200932
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:31.702964
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:33.299225
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:16:35.344355
# Unit test for function do_urlencode
def test_do_urlencode():    assert do_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:16:37.370526
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:40.429787
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:16:41.866375
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:16:44.034090
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:45.994278
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:49.762712
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:16:53.330575
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello world/again') == 'hello%20world%2Fagain'
    assert unicode_urlencode('hello world/again', for_qs=True) == 'hello+world%2Fagain'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ', for_qs=True) == '+'

# Generated at 2024-06-01 06:16:57.938140
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:01.197459
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'value with spaces'}) == 'key=value+with+spaces'
    assert do_urlencode(['a', 'b', 'c']) == 'a&b&c'
    assert do_urlencode('special&chars') == 'special%26chars'
    assert do_urlencode('') == ''
    assert do_urlencode(' ') == '%20'
    assert do_urlencode('a/b?c=d&e=f') == 'a%2Fb%3Fc%3Dd%26e%3Df'

# Generated at 2024-06-01 06:17:02.927144
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('hello%20world') == 'hello world'
    assert unicode_urldecode('foo%2Bbar') == 'foo+bar'
    assert unicode_urldecode('%E4%BD%A0%E5%A5%BD') == '你好'
    assert unicode_urldecode('') == ''
    assert unicode_urldecode('%21%40%23%24%25%5E%26%2A%28%29') == '!@#$%^&*()'

# Generated at 2024-06-01 06:17:04.731213
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:06.328219
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:08.148795
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:10.372447
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:12.315896
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:14.228434
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:15.503133
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:19.827497
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:22.276637
# Unit test for function unicode_urlencode
def test_unicode_urlencode():    assert unicode_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:17:25.396539
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'value with spaces'}) == 'key=value+with+spaces'
    assert do_urlencode(['a', 'b', 'c']) == 'a&b&c'
    assert do_urlencode('special&chars') == 'special%26chars'
    assert do_urlencode('') == ''
    assert do_urlencode(' ') == '%20'
    assert do_urlencode('a+b=c') == 'a%2Bb%3Dc'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:17:26.763239
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:29.599885
# Unit test for function unicode_urlencode

# Generated at 2024-06-01 06:17:33.515698
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:17:35.342218
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:37.462052
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:39.473312
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:41.322148
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:45.371078
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:47.724180
# Unit test for function unicode_urlencode
def test_unicode_urlencode():    assert unicode_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:17:49.778393
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:51.492837
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:53.295989
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:56.669467
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:17:58.333964
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:17:59.785141
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:18:01.657216
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:03.368938
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:11.433009
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:18:13.418647
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:14.840156
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:18:16.604329
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:17.819897
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:18:19.260416
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:18:22.939904
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:18:24.242534
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:18:25.477486
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:18:28.217646
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:35.227331
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:37.466034
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:39.763107
# Unit test for function do_urlencode
def test_do_urlencode():    assert do_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:18:41.787463
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:18:44.678867
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'
    assert unicode

# Generated at 2024-06-01 06:18:46.365429
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:48.213063
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:51.064441
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:18:53.381154
# Unit test for method filters of class FilterModule

# Generated at 2024-06-01 06:18:55.507906
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:04.235645
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('!@#$%^&*()') == '%21%40%23%24%25%5E%26%2A%28%29'

# Generated at 2024-06-01 06:19:06.464792
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:09.267335
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:11.514158
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:12.889570
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:19:14.583678
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:15.922477
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:19:18.445835
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:19:21.517834
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:19:23.266462
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:19:30.460368
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:31.776808
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:19:33.052159
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:19:34.968005
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:36.644501
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:19:39.288504
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'value with spaces'}) == 'key=value+with+spaces'
    assert do_urlencode(['a', 'b', 'c']) == 'a&b&c'
    assert do_urlencode('special&chars') == 'special%26chars'
    assert do_urlencode('') == ''
    assert do_urlencode(' ') == '%20'
    assert do_urlencode('a+b=c') == 'a%2Bb%3Dc'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:19:42.046514
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('!@#$%^&*()') == '%21%40%23%24%25%5E%26%2A%28%29'

# Generated at 2024-06-01 06:19:43.919101
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:45.897978
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:19:47.382990
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:19:55.202447
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:19:57.490399
# Unit test for function do_urlencode
def test_do_urlencode():    assert do_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:19:58.784491
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:20:00.681186
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:02.799848
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:04.192338
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:20:06.628611
# Unit test for function unicode_urlencode
def test_unicode_urlencode():    assert unicode_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:20:08.054898
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:20:09.867251
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:20:11.288500
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:20:18.156272
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:19.461268
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:20:22.188586
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:27.843533
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:20:30.728513
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:20:32.102675
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:20:33.819344
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:35.269551
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:20:37.099280
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:38.445790
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:20:45.225711
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:20:48.166540
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:20:49.968421
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:51.760743
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:53.554101
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:20:57.153340
# Unit test for function unicode_urlencode

# Generated at 2024-06-01 06:21:00.297034
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello%20world') == 'hello%2520world'
    assert unicode_urlencode('hello%20world', for_qs=True) == 'hello%2520world'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode(' ', for_qs=False) == '%20'

# Generated at 2024-06-01 06:21:01.784347
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:21:04.231784
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:21:06.804678
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello%world') == 'hello%25world'
    assert unicode_urlencode('hello%world', for_qs=True) == 'hello%25world'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode('', for_qs=True) == ''

# Generated at 2024-06-01 06:21:13.957129
# Unit test for function do_urlencode
def test_do_urlencode():    assert do_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:21:15.658308
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:21:17.724452
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:21:20.086517
# Unit test for function unicode_urlencode
def test_unicode_urlencode():    assert unicode_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:21:23.359298
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('!@#$%^&*()') == '%21%40%23%24%25%5E%26%2A%28%29'

# Generated at 2024-06-01 06:21:25.146204
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:21:26.493964
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:21:27.788818
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:21:31.211895
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'
    assert do_urlencode({'key': 'value with spaces'}) == 'key=value+with+spaces'
    assert do_urlencode('ümlaut') == 'ümlaut'

# Generated at 2024-06-01 06:21:33.325764
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:21:40.408960
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:21:42.217768
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:21:44.275493
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:21:45.615300
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:21:49.055962
# Unit test for function unicode_urlencode

# Generated at 2024-06-01 06:21:50.481505
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:21:51.789085
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:21:56.375743
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode(' ', for_qs=False) == '%20'
    assert unicode_urlencode('a/b/c', for_qs=False) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:21:58.144315
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:00.858391
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:09.549793
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'();:@&=+$,/?%#[]') == 'special%20chars%20%21%2A%27%28%29%3B%3A%40%26%3D%2B%24%2C%2F%3F%25%23%5B%5D'

# Generated at 2024-06-01 06:22:13.769716
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'
    assert do_urlencode({'key': 'value with spaces'}) == 'key=value+with+spaces'
    assert do_urlencode('ümlaut') == 'ümlaut'

# Generated at 2024-06-01 06:22:15.633403
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:17.645372
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:19.542760
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:21.360689
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:22:23.090086
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:24.810791
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:28.239863
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:22:29.468719
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:22:36.540940
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:38.767473
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:22:40.506078
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:42.794580
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:22:44.699237
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:47.433551
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:22:49.398567
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:52.009195
# Unit test for function unicode_urlencode

# Generated at 2024-06-01 06:22:53.870139
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:22:58.005240
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:05.112322
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:23:06.712620
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:23:08.201255
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:23:09.981550
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:12.521140
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:13.797625
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:23:16.557123
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('!@#$%^&*()') == '%21%40%23%24%25%5E%26%2A%28%29'

# Generated at 2024-06-01 06:23:18.204423
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:20.585960
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:22.215383
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:28.924791
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:23:30.715192
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:32.035007
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:23:33.393169
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:23:35.854472
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:23:38.219584
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a+b=c') == 'a%2Bb%3Dc'
    assert unicode_urlencode('a+b=c', for_qs=True) == 'a%2Bb%3Dc'

# Generated at 2024-06-01 06:23:41.195350
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:23:42.858369
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:44.329636
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:23:46.167681
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:23:52.728401
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:23:55.703979
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a+b=c&d=e', for_qs=True) == 'a%2Bb%3Dc%26d%3De'
    assert unicode_urlencode('a+b=c&d=e') == 'a%2Bb%3Dc%26d%3De'

# Generated at 2024-06-01 06:23:56.906996
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:23:58.942913
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('hello world', for_qs=True) == 'hello+world'
    assert do_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'

# Generated at 2024-06-01 06:24:00.211652
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:24:01.954591
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:03.272958
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:24:04.952389
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:06.858503
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:08.215212
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:24:15.401456
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:18.666751
# Unit test for function unicode_urlencode

# Generated at 2024-06-01 06:24:20.623530
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:22.455910
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:24.197322
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:27.022722
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'
    assert do_urlencode({'key': 'value with spaces'}) == 'key=value+with+spaces'
    assert do_urlencode('ümlaut') == 'ümlaut'

# Generated at 2024-06-01 06:24:29.669068
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:34.445309
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'
    assert do_urlencode({'key': 'value with spaces'}) == 'key=value+with+spaces'
    assert do_urlencode('ümlaut') == 'ümlaut'

# Generated at 2024-06-01 06:24:36.101501
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:37.442841
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:24:44.325869
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:46.524553
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:48.117983
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:49.447640
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:24:51.929078
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:24:55.048501
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('こんにちは') == '%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF'
    assert unicode_urlencode('こんにちは', for_qs=True) == '%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ', for_qs=True) == '+'

# Generated at 2024-06-01 06:24:58.231844
# Unit test for function unicode_urlencode
def test_unicode_urlencode():    assert unicode_urlencode('hello world') == 'hello%20world'

# Generated at 2024-06-01 06:24:59.776258
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:25:01.672517
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:03.357972
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:25:10.777356
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:12.072228
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:25:13.933540
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:15.737241
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:17.368755
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:25:19.861272
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:21.107152
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:25:24.488034
# Unit test for function unicode_urldecode
def test_unicode_urldecode():
    assert unicode_urldecode('hello%20world') == 'hello world'
    assert unicode_urldecode('foo%2Bbar') == 'foo+bar'
    assert unicode_urldecode('%E4%BD%A0%E5%A5%BD') == '你好'
    assert unicode_urldecode('') == ''
    assert unicode_urldecode('%21%40%23%24%25%5E%26%2A%28%29') == '!@#$%^&*()'

# Generated at 2024-06-01 06:25:26.236132
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:28.453285
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:25:37.692622
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('hello+world', for_qs=True) == 'hello%2Bworld'
    assert unicode_urlencode('hello+world') == 'hello%2Bworld'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ') == '%20'
    assert unicode_urlencode(' ', for_qs=True) == '+'
    assert unicode_urlencode('a/b/c') == 'a%2Fb%2Fc'
    assert unicode_urlencode('a/b/c', for_qs=True) == 'a%2Fb%2Fc'

# Generated at 2024-06-01 06:25:43.487777
# Unit test for function do_urlencode
def test_do_urlencode():
    assert do_urlencode('hello world') == 'hello%20world'
    assert do_urlencode('hello/world') == 'hello%2Fworld'
    assert do_urlencode({'key': 'value'}) == 'key=value'
    assert do_urlencode({'key': 'hello world'}) == 'key=hello+world'
    assert do_urlencode(['hello', 'world']) == 'hello&world'
    assert do_urlencode('') == ''
    assert do_urlencode('special chars !*\'()') == 'special%20chars%20%21%2A%27%28%29'
    assert do_urlencode({'key1': 'value1', 'key2': 'value2'}) == 'key1=value1&key2=value2'

# Generated at 2024-06-01 06:25:46.530530
# Unit test for function unicode_urlencode
def test_unicode_urlencode():
    assert unicode_urlencode('hello world') == 'hello%20world'
    assert unicode_urlencode('hello/world') == 'hello%2Fworld'
    assert unicode_urlencode('hello world', for_qs=True) == 'hello+world'
    assert unicode_urlencode('hello/world', for_qs=True) == 'hello%2Fworld'
    assert unicode_urlencode('こんにちは') == '%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF'
    assert unicode_urlencode('こんにちは', for_qs=True) == '%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF'
    assert unicode_urlencode('') == ''
    assert unicode_urlencode(' ', for_qs=True) == '+'

# Generated at 2024-06-01 06:25:47.743381
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()
    
    assert 'urldecode' in filters
    assert callable(filters['urldecode'])
    
    if not HAS_URLENCODE:
        assert 'urlencode' in filters
        assert callable(filters['urlencode'])
    else:
        assert 'urlencode' not in filters

# Generated at 2024-06-01 06:25:49.477507
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:51.368395
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:53.233969
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:55.337861
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:56.999664
# Unit test for function unicode_urldecode
def test_unicode_urldecode():    assert unicode_urldecode('hello%20world') == 'hello world'

# Generated at 2024-06-01 06:25:58.313648
# Unit test for method filters of class FilterModule
def test_FilterModule_filters():    filter_module = FilterModule()

# Generated at 2024-06-01 06:26:18.356047
# Unit test for function split_url

# Generated at 2024-06-01 06:26:21.014000
# Unit test for function split_url

# Generated at 2024-06-01 06:26:24.349782
# Unit test for function split_url

# Generated at 2024-06-01 06:26:27.138285
# Unit test for function split_url

# Generated at 2024-06-01 06:26:30.516625
# Unit test for function split_url
def test_split_url():    # Test case 1: Split a full URL
    url = "http://www.example.com:80/path;params?query=arg#frag"
    expected_result = {
        'scheme': 'http',
        'netloc': 'www.example.com:80',
        'path': '/path',
        'params': 'params',
        'query': 'query=arg',
        'fragment': 'frag',
        'username': None,
        'password': None,
        'hostname': 'www.example.com',
        'port': 80
    }
    assert split_url(url) == expected_result

    # Test case 2: Split a URL and get the 'scheme' component
    assert split_url(url, query='scheme') == 'http'

    # Test case 3: Split a URL and get the 'netloc' component
    assert split_url(url, query='netloc') == 'www.example.com:80'



# Generated at 2024-06-01 06:26:33.256809
# Unit test for function split_url

# Generated at 2024-06-01 06:26:35.914223
# Unit test for function split_url

# Generated at 2024-06-01 06:26:38.271104
# Unit test for function split_url

# Generated at 2024-06-01 06:26:40.666674
# Unit test for function split_url
def test_split_url():    # Test case 1: Split URL without query
    url = "http://example.com/path?query=1#fragment"
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert split_url(url) == expected_result

    # Test case 2: Split URL with query for 'scheme'
    assert split_url(url, 'scheme') == 'http'

    # Test case 3: Split URL with query for 'netloc'
    assert split_url(url, 'netloc') == 'example.com'

    # Test case 4: Split URL with invalid query

# Generated at 2024-06-01 06:26:43.404228
# Unit test for function split_url
def test_split_url():    # Test case 1: Split URL without query
    url = "http://example.com/path?query=1#fragment"
    expected_result = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/path',
        'query': 'query=1',
        'fragment': 'fragment',
        'username': None,
        'password': None,
        'hostname': 'example.com',
        'port': None
    }
    assert split_url(url) == expected_result

    # Test case 2: Split URL with query for 'scheme'
    assert split_url(url, 'scheme') == 'http'

    # Test case 3: Split URL with query for 'netloc'
    assert split_url(url, 'netloc') == 'example.com'

    # Test case 4: Split URL with invalid query