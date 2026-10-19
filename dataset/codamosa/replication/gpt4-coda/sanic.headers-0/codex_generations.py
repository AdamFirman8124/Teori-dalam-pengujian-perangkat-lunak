

# Generated at 2024-03-18 07:29:04.030486
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:29:11.850804
# Unit test for function parse_host
def test_parse_host():    assert parse_host("example.com:80") == ("example.com", 80)

# Generated at 2024-03-18 07:29:19.285184
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Mock configuration and headers
    config = type('Config', (), {'FORWARDED_SECRET': 'secret123'})
    headers = type('Headers', (), {'getall': lambda self, key, default: ['for=192.0.2.60;proto=http;by=secret123'] if key == 'forwarded' else default})()

    # Test with valid secret
    result = parse_forwarded(headers, config)
    assert result == {'for': '192.0.2.60', 'proto': 'http', 'by': 'secret123'}, "Failed to parse Forwarded header with valid secret"

    # Test with invalid secret
    config.FORWARDED_SECRET = 'invalid_secret'
    result = parse_forwarded(headers, config)
    assert result is None, "Parsed Forwarded header with invalid secret"

    # Test with no secret in config
    config.FORWARDED_SECRET = None
    result = parse_forwarded

# Generated at 2024-03-18 07:29:27.086452
# Unit test for function fwd_normalize
def test_fwd_normalize():    # Test normalization of forwarded header values
    assert fwd_normalize([('for', '192.0.2.60'), ('proto', 'https'), ('by', '203.0.113.43')]) == {
        'for': '192.0.2.60',
        'proto': 'https',
        'by': '203.0.113.43'
    }
    # Test normalization of IPv6 addresses
    assert fwd_normalize([('for', '2001:db8:cafe::17')]) == {'for': '[2001:db8:cafe::17]'}
    # Test normalization of obfuscated identifiers
    assert fwd_normalize([('for', '_hidden')]) == {'for': '_hidden'}
    # Test normalization with unknown address
    try:
        fwd_normalize([('for', 'unknown')])
        assert False, "ValueError not raised for 'unknown' address"
    except ValueError:
        pass
   

# Generated at 2024-03-18 07:29:35.325418
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup
    config = type('Config', (), {'FORWARDED_SECRET': 'secret123'})
    headers = {
        'forwarded': [
            'for=192.0.2.60;proto=http;by=203.0.113.43',
            'for=192.0.2.61;proto=https;by=secret123',
            'for=192.0.2.62;proto=http;by=203.0.113.44'
        ]
    }

    # Test parsing with correct secret
    result = parse_forwarded(headers, config)
    assert result == {'for': '192.0.2.61', 'proto': 'https', 'by': 'secret123'}, "Failed to parse Forwarded header with correct secret"

    # Test parsing with incorrect secret
    config.FORWARDED_SECRET = 'wrongsecret'
    result = parse_forwarded(headers, config)
    assert result is None

# Generated at 2024-03-18 07:29:42.501978
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers and config

# Generated at 2024-03-18 07:29:49.645952
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    # Setup headers and config for the test
    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "/path"
    }
    config = {
        "REAL_IP_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
        "FORWARDED_FOR_HEADER": "x-forwarded-for"
    }

    # Call the function with the headers and config
    options = parse_xforwarded(headers, config)

    # Check the results
    assert options is not None
    assert options["for"] == "70.41.3.18"
    assert options["proto"] == "https"
    assert options

# Generated at 2024-03-18 07:29:58.724513
# Unit test for function fwd_normalize
def test_fwd_normalize():    # Test normalization of various forwarded header values
    assert fwd_normalize([('for', '192.0.2.60'), ('proto', 'https'), ('by', '203.0.113.43')]) == {
        'for': '192.0.2.60',
        'proto': 'https',
        'by': '203.0.113.43'
    }
    assert fwd_normalize([('for', '[2001:db8:cafe::17]'), ('proto', 'http'), ('by', 'unknown')]) == {
        'for': '[2001:db8:cafe::17]',
        'proto': 'http'
    }
    assert fwd_normalize([('for', '_secret'), ('proto', 'https'), ('by', '_hidden')]) == {
        'for': '_secret',
        'proto': 'https',
        'by': '_hidden'
    }

# Generated at 2024-03-18 07:30:09.816914
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    # Setup headers and config for the test
    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com:8080",
        "x-forwarded-port": "8080",
        "x-forwarded-path": "/path",
    }
    config = {
        "REAL_IP_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
    }

    # Call the function with the headers and config
    result = parse_xforwarded(headers, config)

    # Expected result

# Generated at 2024-03-18 07:30:18.313968
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock configuration with a secret

# Generated at 2024-03-18 07:30:31.662095
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:30:40.438654
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:30:48.315354
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:30:59.450276
# Unit test for function fwd_normalize
def test_fwd_normalize():    # Test normalization of various forwarded header values
    assert fwd_normalize([('for', '192.0.2.60'), ('proto', 'https'), ('by', '203.0.113.43')]) == {
        'for': '192.0.2.60',
        'proto': 'https',
        'by': '203.0.113.43'
    }
    assert fwd_normalize([('for', '[2001:db8:cafe::17]'), ('proto', 'http'), ('by', 'unknown')]) == {
        'for': '[2001:db8:cafe::17]',
        'proto': 'http'
    }
    assert fwd_normalize([('for', '_secret'), ('proto', 'https'), ('by', '_hidden')]) == {
        'for': '_secret',
        'proto': 'https',
        'by': '_hidden'
    }

# Generated at 2024-03-18 07:31:10.114104
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:31:20.122522
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:31:27.030452
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:31:39.372790
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:31:52.972797
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:32:01.235222
# Unit test for function parse_content_header
def test_parse_content_header():    # Test with simple content-type
    value, options = parse_content_header("text/plain")
    assert value == "text/plain"
    assert options == {}

    # Test with complex content-disposition
    value, options = parse_content_header('form-data; name="upload"; filename="file.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt"}

    # Test with escaped quotes in filename
    value, options = parse_content_header('attachment; filename="file\\"name.txt"')
    assert value == "attachment"
    assert options == {"filename": 'file"name.txt'}

    # Test with multiple parameters and whitespace
    value, options = parse_content_header('multipart/form-data; boundary="----WebKitFormBoundaryePkpFF7tjBAqx29L"; charset=utf-8')
    assert value == "multipart/form-data"

# Generated at 2024-03-18 07:32:13.895004
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:32:24.217562
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    # Setup headers and config for the test
    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com:8080",
        "x-forwarded-port": "8080",
        "x-forwarded-path": "/path",
    }
    config = {
        "REAL_IP_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
    }

    # Call the function with the headers and config
    result = parse_xforwarded(headers, config)

    # Expected result

# Generated at 2024-03-18 07:32:33.795777
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup
    config = type('Config', (), {'FORWARDED_SECRET': 'secret123'})
    headers = {
        'forwarded': [
            'for=192.0.2.60;proto=http;by=203.0.113.43',
            'for=192.0.2.61;proto=https;by=secret123',
            'for=192.0.2.62;proto=http;by=203.0.113.44'
        ]
    }

    # Test parsing with correct secret
    result = parse_forwarded(headers, config)
    assert result == {
        'for': '192.0.2.61',
        'proto': 'https',
        'by': 'secret123'
    }, "Failed to parse Forwarded header with correct secret"

    # Test parsing with incorrect secret
    config.FORWARDED_SECRET = 'wrongsecret'

# Generated at 2024-03-18 07:32:40.135215
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from sanic.request import Request

# Generated at 2024-03-18 07:32:48.248806
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup
    from unittest.mock import MagicMock

    # Mock headers with a Forwarded header containing the secret
    headers = MagicMock()
    headers.getall.return_value = ['by=server;for=192.0.2.60;host=example.com;proto=http;secret=supersecret']

    # Mock config with a matching FORWARDED_SECRET
    config = MagicMock()
    config.FORWARDED_SECRET = 'supersecret'

    # Call the function with the mock objects
    result = parse_forwarded(headers, config)

    # Assert the result is as expected
    assert result == {
        'by': 'server',
        'for': '192.0.2.60',
        'host': 'example.com',
        'proto': 'http',
        'secret': 'supersecret'
    }, "Failed to parse Forwarded header correctly"

    # Test with no Forwarded header present
    headers.getall.return_value = None

# Generated at 2024-03-18 07:32:57.435171
# Unit test for function parse_content_header
def test_parse_content_header():    # Test with simple content-type
    value, options = parse_content_header("text/plain")
    assert value == "text/plain"
    assert options == {}

    # Test with complex content-disposition
    value, options = parse_content_header('form-data; name="upload"; filename="file.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt"}

    # Test with escaped quotes in filename
    value, options = parse_content_header('attachment; filename="file\\"name.txt"')
    assert value == "attachment"
    assert options == {"filename": 'file"name.txt'}

    # Test with multiple parameters and whitespace
    value, options = parse_content_header('multipart/form-data; boundary="----WebKitFormBoundaryePkpFF7tjBAqx29L"; charset=utf-8')
    assert value == "multipart/form-data"

# Generated at 2024-03-18 07:33:05.020159
# Unit test for function parse_forwarded
def test_parse_forwarded():    from sanic.request import Request

# Generated at 2024-03-18 07:33:11.466434
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    headers = {
        "X-Forwarded-For": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Path": "/path"
    }

# Generated at 2024-03-18 07:33:18.738740
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:33:25.383209
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:33:54.523410
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:34:02.851265
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    headers = {
        "X-Forwarded-For": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Path": "/path"
    }

# Generated at 2024-03-18 07:34:09.452275
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    headers = {
        "X-Forwarded-For": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Path": "/path"
    }

# Generated at 2024-03-18 07:34:15.550428
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    headers = {
        "X-Forwarded-For": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Path": "/path"
    }

# Generated at 2024-03-18 07:34:21.576863
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup a mock config with a FORWARDED_SECRET
    class MockConfig:
        FORWARDED_SECRET = "secret123"

    config = MockConfig()

    # Test with no Forwarded header
    headers = {"other-header": "value"}
    assert parse_forwarded(headers, config) is None

    # Test with Forwarded header but no secret
    headers = {"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43"}
    assert parse_forwarded(headers, config) is None

    # Test with Forwarded header containing the secret in 'by' field
    headers = {"forwarded": "for=192.0.2.60;proto=http;by=secret123"}
    expected = {'for': '192.0.2.60', 'proto': 'http', 'by': 'secret123'}

# Generated at 2024-03-18 07:34:27.066741
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:34:35.707165
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup
    from unittest.mock import MagicMock

    # Mock headers with a Forwarded header containing the secret
    headers = MagicMock()
    headers.getall.return_value = ['by=server;for=192.0.2.60;host=example.com;proto=http;secret=supersecret']

    # Mock config with a matching FORWARDED_SECRET
    config = MagicMock()
    config.FORWARDED_SECRET = 'supersecret'

    # Call the function with the mock objects
    result = parse_forwarded(headers, config)

    # Assert the result is as expected
    assert result == {
        'by': 'server',
        'for': '192.0.2.60',
        'host': 'example.com',
        'proto': 'http',
        'secret': 'supersecret'
    }, "Failed to parse Forwarded header correctly"

    # Test with no Forwarded header present
    headers.getall.return_value = None

# Generated at 2024-03-18 07:34:41.424898
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup
    from unittest.mock import MagicMock

    # Mock headers with a Forwarded header containing the secret
    headers = MagicMock()
    headers.getall.return_value = ['by=server;for=192.0.2.60;host=example.com;proto=http;secret=supersecret']

    # Mock config with a matching FORWARDED_SECRET
    config = MagicMock()
    config.FORWARDED_SECRET = 'supersecret'

    # Call the function with the mock objects
    result = parse_forwarded(headers, config)

    # Assert the result is as expected
    assert result == {
        'by': 'server',
        'for': '192.0.2.60',
        'host': 'example.com',
        'proto': 'http',
        'secret': 'supersecret'
    }, "Failed to parse Forwarded header correctly"

    # Test with no Forwarded header present
    headers.getall.return_value = None

# Generated at 2024-03-18 07:34:48.663917
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:34:54.122267
# Unit test for function parse_forwarded
def test_parse_forwarded():    from sanic.request import RequestParameters

    # Mock headers and config

# Generated at 2024-03-18 07:35:30.241523
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "/path"
    }

# Generated at 2024-03-18 07:35:38.428551
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    headers = {
        "X-Forwarded-For": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "X-Forwarded-Host": "example.com",
        "X-Forwarded-Proto": "https",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Path": "/path"
    }

# Generated at 2024-03-18 07:35:49.163184
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers and config

# Generated at 2024-03-18 07:35:57.186466
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:36:05.205871
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers with a dictionary

# Generated at 2024-03-18 07:36:11.433766
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:36:18.132582
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Mock configuration and headers
    class Config:
        FORWARDED_SECRET = "secret123"

    config = Config()
    headers = {
        "forwarded": [
            'for=192.0.2.60;proto=http;by=203.0.113.43;secret="secret123"',
            'for=192.0.2.61;proto=https;by=203.0.113.44;secret="othersecret"'
        ]
    }

    # Test with correct secret
    result = parse_forwarded(headers, config)
    assert result == {
        "for": "192.0.2.60",
        "proto": "http",
        "by": "203.0.113.43",
        "secret": "secret123"
    }, f"Expected options with correct secret, got {result}"

    # Test with incorrect secret
    config.FORWARDED_SECRET = "wrongsecret"

# Generated at 2024-03-18 07:36:24.646495
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup a mock config with a secret
    class MockConfig:
        FORWARDED_SECRET = "secret123"

    config = MockConfig()

    # Test with a single Forwarded header containing the secret
    headers = {"forwarded": "for=192.0.2.60;proto=http;by=secret123"}
    result = parse_forwarded(headers, config)
    assert result == {"for": "192.0.2.60", "proto": "http", "by": "secret123"}

    # Test with multiple Forwarded headers, one of which contains the secret
    headers = {
        "forwarded": [
            "for=192.0.2.60;proto=http",
            "by=secret123;for=192.0.2.61;proto=https",
        ]
    }
    result = parse_forwarded(headers, config)

# Generated at 2024-03-18 07:36:35.751451
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup a mock config with a secret
    class MockConfig:
        FORWARDED_SECRET = "secret123"

    config = MockConfig()

    # Test with a single Forwarded header containing the secret
    headers = {"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43;secret=secret123"}
    result = parse_forwarded(headers, config)
    assert result == {"for": "192.0.2.60", "proto": "http", "by": "203.0.113.43"}

    # Test with multiple Forwarded headers, one of which contains the secret
    headers = {
        "forwarded": [
            "for=192.0.2.60;proto=http",
            "by=203.0.113.43;secret=secret123",
        ]
    }
    result = parse_forwarded(headers, config)

# Generated at 2024-03-18 07:36:41.976609
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    # Mock headers and config for testing
    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "/path"
    }
    config = {
        "REAL_IP_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
        "FORWARDED_FOR_HEADER": "x-forwarded-for"
    }

    # Test with PROXIES_COUNT set to 2
    expected_result = {
        "for": "70.41.3.18",
        "proto": "https",
        "host": "example.com",
        "port": 443,
        "path": "/path"
    }
    assert parse

# Generated at 2024-03-18 07:37:23.561910
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    # Setup headers and config for the test
    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "/path"
    }
    config = {
        "REAL_IP_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
        "FORWARDED_FOR_HEADER": "x-forwarded-for"
    }

    # Call the function with the headers and config
    options = parse_xforwarded(headers, config)

    # Expected result

# Generated at 2024-03-18 07:37:32.166575
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers and config

# Generated at 2024-03-18 07:37:38.463886
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    # Mock headers and config for testing
    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "/path"
    }
    config = {
        "REAL_IP_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
        "FORWARDED_FOR_HEADER": "x-forwarded-for"
    }

    # Test with PROXIES_COUNT = 2
    expected_result = {
        "for": "70.41.3.18",
        "proto": "https",
        "host": "example.com",
        "port": 443,
        "path": "/path"
    }
    assert parse_x

# Generated at 2024-03-18 07:37:48.641138
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    # Mock headers and config for testing
    headers = {
        "x-forwarded-for": "203.0.113.195, 70.41.3.18, 150.172.238.178",
        "x-forwarded-proto": "https",
        "x-forwarded-host": "example.com",
        "x-forwarded-port": "443",
        "x-forwarded-path": "/path",
    }
    config = {
        "REAL_IP_HEADER": "x-forwarded-for",
        "PROXIES_COUNT": 2,
        "FORWARDED_FOR_HEADER": "x-forwarded-for",
    }

    # Expected result

# Generated at 2024-03-18 07:37:55.020524
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:38:02.976258
# Unit test for function parse_xforwarded
def test_parse_xforwarded():    from unittest.mock import MagicMock

    # Mock headers and config

# Generated at 2024-03-18 07:38:08.161591
# Unit test for function parse_forwarded
def test_parse_forwarded():    from unittest.mock import MagicMock

    # Mock headers with a single Forwarded header

# Generated at 2024-03-18 07:38:14.136004
# Unit test for function fwd_normalize
def test_fwd_normalize():    # Test normalization of various forwarded header values
    assert fwd_normalize([('for', '192.0.2.60')]) == {'for': '192.0.2.60'}
    assert fwd_normalize([('for', '[2001:db8:cafe::17]')]) == {'for': '[2001:db8:cafe::17]'}
    assert fwd_normalize([('for', 'unknown')]) == {}
    assert fwd_normalize([('for', '_secret')]) == {'for': '_secret'}
    assert fwd_normalize([('proto', 'HTTP')]) == {'proto': 'http'}
    assert fwd_normalize([('proto', 'HTTPS')]) == {'proto': 'https'}
    assert fwd_normalize([('host', 'example.com')]) == {'host': 'example.com'}
    assert fwd_normalize([('port', '8080')]) == {'port': 8080}
    assert fwd_normalize([('path', '/foo/bar')])

# Generated at 2024-03-18 07:38:22.770012
# Unit test for function parse_forwarded
def test_parse_forwarded():    # Setup a mock config with a secret
    class MockConfig:
        FORWARDED_SECRET = "secret123"

    config = MockConfig()

    # Test with no headers
    headers = {}
    assert parse_forwarded(headers, config) is None

    # Test with no secret in config
    config.FORWARDED_SECRET = None
    headers = {"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43"}
    assert parse_forwarded(headers, config) is None

    # Reset secret in config for further tests
    config.FORWARDED_SECRET = "secret123"

    # Test with a single Forwarded header
    headers = {"forwarded": "for=192.0.2.60;proto=http;by=203.0.113.43;secret=secret123"}

# Generated at 2024-03-18 07:38:35.103248
# Unit test for function fwd_normalize
def test_fwd_normalize():    # Test normalization of various forwarded header values
    assert fwd_normalize([('for', '192.0.2.60'), ('proto', 'https'), ('by', '203.0.113.43')]) == {
        'for': '192.0.2.60',
        'proto': 'https',
        'by': '203.0.113.43'
    }
    assert fwd_normalize([('for', '[2001:db8:cafe::17]'), ('proto', 'http'), ('by', 'unknown')]) == {
        'for': '[2001:db8:cafe::17]',
        'proto': 'http'
    }
    assert fwd_normalize([('for', '_secret'), ('proto', 'https'), ('by', '_hidden')]) == {
        'for': '_secret',
        'proto': 'https',
        'by': '_hidden'
    }