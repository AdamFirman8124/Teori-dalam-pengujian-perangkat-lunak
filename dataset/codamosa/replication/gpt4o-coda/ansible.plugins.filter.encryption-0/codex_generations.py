

# Generated at 2024-06-01 06:01:04.575205
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:07.543078
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:10.189728
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:12.798742
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "filter_default"
    encrypted_data = "$ANSIBLE_VAULT;1.1;AES256\n6162636465666768696a6b6c6d6e6f70\n7172737475767778797a7b7c7d7e7f80\n8182838485868788898a8b8c8d8e8f90\n"

    # Test with valid encrypted data
    decrypted_data = do_unvault(encrypted_data, secret, vaultid)
    assert decrypted_data == "mydata", f"Expected 'mydata', but got {decrypted_data}"

    # Test with invalid secret
    try:
        do_unvault(encrypted_data, "wrongsecret", vaultid)
    except AnsibleFilterError as e:
        assert "Unable to decrypt" in str(e), f"Expected decryption error, but got {e}"

   

# Generated at 2024-06-01 06:01:16.105445
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:18.771445
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:22.001684
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:24.894590
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:27.868901
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "filter_default"
    encrypted_data = "$ANSIBLE_VAULT;1.1;AES256\n6162636465666768696a6b6c6d6e6f70\n7172737475767778797a7b7c7d7e7f80\n8182838485868788898a8b8c8d8e8f90\n9192939495969798999a9b9c9d9e9fa0\n"
    
    # Test with valid encrypted data
    decrypted_data = do_unvault(encrypted_data, secret, vaultid)
    assert decrypted_data == "mydata", f"Expected 'mydata', got {decrypted_data}"
    
    # Test with invalid secret

# Generated at 2024-06-01 06:01:30.959389
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "filter_default"
    encrypted_data = "$ANSIBLE_VAULT;1.1;AES256\n6162636465666768696a6b6c6d6e6f70\n7172737475767778797a7b7c7d7e7f80\n8182838485868788898a8b8c8d8e8f90\n"

    # Test with valid encrypted data
    decrypted_data = do_unvault(encrypted_data, secret, vaultid)
    assert decrypted_data == "mydata", f"Expected 'mydata', but got {decrypted_data}"

    # Test with invalid secret

# Generated at 2024-06-01 06:01:38.261489
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:41.005241
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:44.077838
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:47.214512
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:50.969157
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:54.025549
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:56.620825
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:01:59.265099
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:02.200302
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:05.363073
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:16.578436
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:19.353857
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:22.717685
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:25.654843
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:28.389771
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:31.176247
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:34.633610
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:37.579870
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:40.513807
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:43.149796
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:53.304001
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:56.166679
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:02:59.132212
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:02.316609
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:05.353363
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "filter_default"
    encrypted_data = "$ANSIBLE_VAULT;1.1;AES256\n6162636465666768696a6b6c6d6e6f70\n"

    # Test with valid encrypted data
    decrypted_data = do_unvault(encrypted_data, secret, vaultid)
    assert decrypted_data == "abcdefghijklmno", f"Expected 'abcdefghijklmno', got {decrypted_data}"

    # Test with invalid secret
    try:
        do_unvault(encrypted_data, "wrongsecret", vaultid)
    except AnsibleFilterError as e:
        assert "Unable to decrypt" in str(e), f"Expected 'Unable to decrypt' error, got {e}"

    # Test with non-encrypted data
    non_encrypted_data = "plain text"
    decrypted_data = do_unvault(non_encrypted_data, secret, vaultid)


# Generated at 2024-06-01 06:03:08.024005
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:10.758442
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:13.682743
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:19.696993
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:22.474636
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:37.742651
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:40.542710
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:43.595921
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:46.233897
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:49.254000
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "filter_default"
    encrypted_data = "$ANSIBLE_VAULT;1.1;AES256\n6162636465666768696a6b6c6d6e6f70\n"

    # Test with valid encrypted data
    decrypted_data = do_unvault(encrypted_data, secret, vaultid)
    assert decrypted_data == "abcdefghijklmno", f"Expected 'abcdefghijklmno', got {decrypted_data}"

    # Test with invalid secret
    try:
        do_unvault(encrypted_data, "wrongsecret", vaultid)
    except AnsibleFilterError as e:
        assert "Unable to decrypt" in str(e), f"Expected decryption error, got {e}"

    # Test with non-encrypted data
    non_encrypted_data = "plain text"
    decrypted_data = do_unvault(non_encrypted_data, secret, vaultid)
    assert decrypted

# Generated at 2024-06-01 06:03:53.471362
# Unit test for function do_vault
def test_do_vault():
    secret = "mysecret"
    data = "sensitive data"
    encrypted_data = do_vault(data, secret)
    assert isinstance(encrypted_data, str)
    assert encrypted_data.startswith('$ANSIBLE_VAULT;')

    # Test with wrap_object=True
    encrypted_data_wrapped = do_vault(data, secret, wrap_object=True)
    assert isinstance(encrypted_data_wrapped, AnsibleVaultEncryptedUnicode)

    # Test with invalid secret type
    try:
        do_vault(data, 12345)
    except AnsibleFilterTypeError as e:
        assert str(e) == "Secret passed is required to be a string, instead we got: <class 'int'>"

    # Test with invalid data type
    try:
        do_vault(12345, secret)
    except AnsibleFilterTypeError as e:
        assert str(e) == "Can only vault strings, instead we got: <class 'int'>"

# Generated at 2024-06-01 06:03:56.693546
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:03:59.515438
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:02.474584
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:05.918752
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:25.850324
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:29.036110
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:31.491396
# Unit test for function do_unvault
def test_do_unvault():
    secret = "mysecret"
    vaultid = "filter_default"
    encrypted_data = "$ANSIBLE_VAULT;1.1;AES256\n6162636465666768696a6b6c6d6e6f70\n"

    # Test with valid encrypted data
    result = do_unvault(encrypted_data, secret, vaultid)
    assert result == "abcdefghijklmno", f"Expected 'abcdefghijklmno', got {result}"

    # Test with invalid secret
    try:
        do_unvault(encrypted_data, "wrongsecret", vaultid)
    except AnsibleFilterError as e:
        assert "Unable to decrypt" in str(e), f"Expected decryption error, got {e}"

    # Test with non-encrypted data
    non_encrypted_data = "plain text"
    result = do_unvault(non_encrypted_data, secret, vaultid)
    assert result == non_encrypted_data

# Generated at 2024-06-01 06:04:39.895897
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:42.657331
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:45.326046
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:48.470493
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:51.068327
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:54.206886
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:04:58.752085
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:18.667437
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:21.230067
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:23.875467
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:27.195227
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:30.307858
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:34.192794
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:37.861434
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:40.510069
# Unit test for function do_unvault
def test_do_unvault():    secret = "mysecret"

# Generated at 2024-06-01 06:05:43.089639
# Unit test for function do_vault
def test_do_vault():    secret = "mysecret"