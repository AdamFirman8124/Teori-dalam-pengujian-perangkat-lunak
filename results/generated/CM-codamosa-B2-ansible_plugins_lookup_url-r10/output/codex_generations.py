

# Generated at 2026-10-25 06:20:43.772186
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:20:46.189876
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:20:48.689476
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:20:51.080062
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:20:53.494680
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:20:55.997753
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:20:58.401433
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:21:00.815358
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:21:03.237639
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:21:05.650784
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:21:08.065079
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:21:10.702173
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 06:21:13.116430
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:02.187233
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:04.603438
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:07.018457
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:09.433687
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:11.847107
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:14.264494
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:16.675950
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:19.092842
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:21.503588
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:23.919921
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:26.335560
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:28.752904
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:31.168644
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:33.582751
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:36.002336
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:38.413080
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:56.331214
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:22:57.763152
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:15.684880
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:18.103253
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:20.520349
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:22.937772
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:25.356985
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:27.771171
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:30.175938
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:32.591963
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:35.006627
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:37.420871
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:39.835586
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:42.249639
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:44.664954
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:47.078908
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:49.495544
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:51.910804
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:54.325063
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:23:57.295911
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    lookup = LookupModule()

    # Case 1: multiple URLs, split_lines default (True) -> flat list of lines
    lookup_1 = LookupModule()
    result = lookup_1.run(terms=['http://www.ansible.com/httpbin/get?a=b&c=d',
                                 'http://www.ansible.com/httpbin/get?e=f&g=h'],
                          variables=None)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == "{'args': {'a': 'b', 'c': 'd'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?a=b&c=d'}"
    assert result[1] == "{'args': {'e': 'f', 'g': 'h'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?e=f&g=h'}"

    # Case 2: single URL, split_lines=False -> single blob entry
    lookup_2 = LookupModule()
    result = lookup_2.run(terms=['http://www.ansible.com/httpbin/get?a=b&c=d'],
                          variables={'ansible_lookup_url_split_lines': False})
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "{'args': {'a': 'b', 'c': 'd'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?a=b&c=d'}"

    # Case 3: HTTPError raised -> AnsibleError with HTTP error message
    lookup_3 = LookupModule()
    try:
        lookup_3.run(terms=['http://www.ansible.com/void'], variables=None)
    except HTTPError as e:
        assert e.code == 404
    except AnsibleError as e:
        assert 'Received HTTP error for' in to_native(e)
    else:
        raise AssertionError("Expected HTTPError or AnsibleError for 'http://www.ansible.com/void'")

    # Case 4: URLError / ConnectionError raised -> AnsibleError with failure message
    lookup_4 = LookupModule()
    try:
        lookup_4.run(terms=['http://localhost:1/'], variables=None)
    except AnsibleError as e:
        assert ('Failed lookup url for' in to_native(e)) or ('Error connecting to' in to_native(e))
    else:
        raise AssertionError("Expected AnsibleError for unreachable URL 'http://localhost:1/'")

    # Case 5: invalid scheme -> URLError style AnsibleError
    lookup_5 = LookupModule()
    try:
        lookup_5.run(terms=['file:///foo/bar.txt'], variables=None)
    except AnsibleError as e:
        assert 'Failed lookup url for' in to_native(e)
    else:
        raise AssertionError("Expected AnsibleError for unsupported scheme 'file:///foo/bar.txt'")

    # Case 6: term without scheme -> ansiblehttpget prepends http://
    lookup_6 = LookupModule()
    result = lookup_6.run(terms=['www.ansible.com/httpbin/get'], variables=None)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "{'args': {}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get'}"

# Generated at 2026-10-25 06:23:58.681907
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:24:16.705921
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:24:34.652607
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:24:36.140743
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:24:54.091466
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:25:25.435962
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-25 06:25:28.045919
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:25:30.463535
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:25:32.875634
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:25:35.352926
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:25:37.726852
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:25:40.144496
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:25:42.558670
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:00.855887
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:18.673520
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:21.336965
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:23.980778
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:26.548625
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:28.979065
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:31.393396
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:33.808515
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:36.222576
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:38.636617
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:41.050976
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:43.465106
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:45.877736
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:48.292114
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:50.707168
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:53.120708
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:55.581562
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:26:57.968334
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:00.379607
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:02.888384
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:05.285250
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:07.700492
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:10.119685
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:12.533853
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:14.950089
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:17.364934
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:19.779164
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:22.191909
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:24.606952
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:27.022144
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:29.436459
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:31.850236
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:34.265323
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:36.678944
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:39.093802
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:41.509651
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:27:43.923347
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:01.647192
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-25 06:28:03.124163
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:21.350917
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-25 06:28:22.759792
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:40.749023
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-25 06:28:42.244829
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:45.012028
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:47.427242
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:49.842375
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:52.255201
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:54.668537
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:57.083143
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:28:59.529124
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:01.943911
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:04.357540
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:06.771969
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:09.187297
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:11.601805
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:14.014779
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:16.431207
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:18.846931
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:21.261288
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:23.675740
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:26.246399
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:29:43.979401
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:01.910407
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:03.546294
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:21.872225
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-25 06:30:23.229820
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:25.847681
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:28.267056
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:30.682841
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:33.329694
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:35.747911
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:38.164808
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:40.599569
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 06:30:43.013284
# Unit test for method run of class LookupModule