

# Generated at 2024-06-03 07:00:22.602931
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:00:26.609802
# Unit test for function parse_forwarded

# Generated at 2024-06-03 07:00:32.726694
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:00:36.357193
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:00:39.431165
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:00:42.893559
# Unit test for function fwd_normalize
def test_fwd_normalize():    # Test case 1: Normalizing a simple forwarded header
    fwd = [("for", "192.168.0.1"), ("proto", "HTTP"), ("host", "example.com"), ("port", "8080"), ("path", "/test")]
    expected = {"for": "192.168.0.1", "proto": "http", "host": "example.com", "port": 8080, "path": "/test"}
    assert fwd_normalize(fwd) == expected

    # Test case 2: Normalizing with an IPv6 address
    fwd = [("for", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"), ("proto", "HTTPS")]

# Generated at 2024-06-03 07:00:46.414586
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:00:50.159718
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:00:53.937081
# Unit test for function fwd_normalize
def test_fwd_normalize():    fwd = [("for", "192.168.0.1"), ("proto", "HTTP"), ("host", "example.com"), ("port", "8080"), ("path", "/test")]

# Generated at 2024-06-03 07:00:58.174008
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="othersecret"'
        ]
    }

# Generated at 2024-06-03 07:01:10.820730
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:01:15.549444
# Unit test for function parse_forwarded

# Generated at 2024-06-03 07:01:19.120228
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:01:21.919056
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:01:25.380675
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="wrongsecret"'
        ]
    }

# Generated at 2024-06-03 07:01:30.408514
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:01:33.737052
# Unit test for function parse_host
def test_parse_host():    assert parse_host("example.com") == ("example.com", None)

# Generated at 2024-06-03 07:01:37.543071
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:01:40.378817
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:01:45.032211
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:01:56.878263
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:02:01.099353
# Unit test for function fwd_normalize
def test_fwd_normalize():    fwd = [("for", "192.168.0.1"), ("proto", "HTTP"), ("host", "example.com"), ("port", "8080"), ("path", "/test")]

# Generated at 2024-06-03 07:02:04.627333
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:02:07.686104
# Unit test for function parse_content_header
def test_parse_content_header():    assert parse_content_header('form-data; name=upload; filename="file.txt"') == (
        'form-data', {'name': 'upload', 'filename': 'file.txt'}
    )

# Generated at 2024-06-03 07:02:11.456138
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:02:14.775014
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:02:17.943675
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:02:22.699555
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:02:27.615917
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:02:30.709734
# Unit test for function parse_content_header
def test_parse_content_header():    assert parse_content_header('form-data; name=upload; filename="file.txt"') == (
        'form-data',
        {'name': 'upload', 'filename': 'file.txt'}
    )

# Generated at 2024-06-03 07:02:41.846828
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:02:46.106445
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:02:50.081303
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:02:57.322841
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:02:59.943015
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:03:05.681766
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:03:10.466411
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:03:14.259501
# Unit test for function parse_host
def test_parse_host():    assert parse_host("example.com") == ("example.com", None)

# Generated at 2024-06-03 07:03:18.267189
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:03:22.961949
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:03:34.032098
# Unit test for function parse_forwarded

# Generated at 2024-06-03 07:03:38.173478
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:03:42.809273
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:03:46.353295
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:03:49.904092
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:03:54.683518
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:03:59.289808
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:04:03.986836
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:04:07.587280
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:04:11.598191
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:04:22.258771
# Unit test for function fwd_normalize
def test_fwd_normalize():    fwd = [("for", "192.168.0.1"), ("proto", "HTTP"), ("host", "example.com"), ("port", "8080"), ("path", "/test/path")]

# Generated at 2024-06-03 07:04:27.427340
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:04:31.939351
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:04:36.276192
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:04:40.052054
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:04:43.422749
# Unit test for function parse_host
def test_parse_host():    assert parse_host("example.com") == ("example.com", None)

# Generated at 2024-06-03 07:04:48.297862
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:04:52.319600
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:04:54.497797
# Unit test for function parse_host
def test_parse_host():    assert parse_host("example.com") == ("example.com", None)

# Generated at 2024-06-03 07:04:59.018374
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:05:14.073641
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:05:17.517201
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:05:23.357619
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:05:27.636881
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:05:31.282189
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:05:35.260955
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:05:41.543441
# Unit test for function parse_forwarded

# Generated at 2024-06-03 07:05:45.262894
# Unit test for function parse_host
def test_parse_host():    assert parse_host("example.com") == ("example.com", None)

# Generated at 2024-06-03 07:05:49.488519
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:05:55.691202
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:06:08.553296
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:06:12.482107
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:06:16.822215
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:06:20.578705
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:06:24.478174
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:06:26.845820
# Unit test for function parse_host
def test_parse_host():    assert parse_host("example.com:80") == ("example.com", 80)

# Generated at 2024-06-03 07:06:30.672736
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:06:34.494656
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:06:37.790215
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:06:42.698519
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:07:02.136218
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:07:05.636954
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:07:09.556417
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:07:13.347077
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:07:19.470958
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:07:25.145936
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:07:30.616266
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:07:36.185466
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:07:41.047535
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:07:46.121964
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:07:57.895544
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:08:03.696494
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:08:07.056773
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:08:10.928267
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:08:14.427681
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:08:20.532091
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:08:25.646866
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:08:28.753885
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:08:32.021886
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:08:35.984983
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:08:51.312741
# Unit test for function parse_forwarded

# Generated at 2024-06-03 07:08:57.259943
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:09:00.457565
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:09:06.033921
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:09:10.188260
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:09:17.302844
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:09:21.239056
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:09:24.366687
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }

# Generated at 2024-06-03 07:09:28.037400
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:09:30.896160
# Unit test for function fwd_normalize_address
def test_fwd_normalize_address():    assert fwd_normalize_address("192.168.0.1") == "192.168.0.1"

# Generated at 2024-06-03 07:09:45.660698
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:09:49.409422
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:09:53.620345
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:09:57.871819
# Unit test for function parse_xforwarded

# Generated at 2024-06-03 07:10:03.844858
# Unit test for function parse_forwarded
def test_parse_forwarded():    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="mysecret"',
            'for=198.51.100.17;proto=https;by=203.0.113.44;secret="mysecret"'
        ]
    }