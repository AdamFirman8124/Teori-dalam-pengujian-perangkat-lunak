

# Generated at 2024-06-04 19:16:22.190961
# Unit test for method __eq__ of class Position
def test_Position___eq__():    pos1 = Position(1, 2, 3)

# Generated at 2024-06-04 19:16:25.069065
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():    # Test case with a single message and no index
    error = BaseError(text="An error occurred", code="error_code")
    assert str(error) == "An error occurred"

    # Test case with multiple messages
    messages = [
        Message(text="First error", code="first_code", key="first_key"),
        Message(text="Second error", code="second_code", key="second_key")
    ]
    error = BaseError(messages=messages)
    assert str(error) == "{'first_key': 'First error', 'second_key': 'Second error'}"

    # Test case with nested messages
    nested_messages = [
        Message(text="Nested error", code="nested_code", index=["parent", "child"])
    ]
    error = BaseError(messages=nested_messages)
    assert str(error) == "{'parent': {'child': 'Nested error'}}"


# Generated at 2024-06-04 19:16:28.791093
# Unit test for constructor of class ValidationError
def test_ValidationError():    # Test with a single message
    error = ValidationError(text="Invalid input", code="invalid")
    assert len(error.messages()) == 1
    assert error.messages()[0].text == "Invalid input"
    assert error.messages()[0].code == "invalid"
    assert error.messages()[0].index == []

    # Test with multiple messages
    messages = [
        Message(text="Invalid username", code="invalid", key="username"),
        Message(text="Invalid password", code="invalid", key="password"),
    ]
    error = ValidationError(messages=messages)
    assert len(error.messages()) == 2
    assert error.messages()[0].text == "Invalid username"
    assert error.messages()[0].code == "invalid"
    assert error.messages()[0].index == ["username"]
    assert error.messages()[1].text == "Invalid password"
    assert error.messages()[1].code == "invalid"

# Generated at 2024-06-04 19:16:32.266931
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:16:34.405561
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:16:36.364145
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:16:42.334994
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:16:46.757331
# Unit test for method __eq__ of class Position
def test_Position___eq__():    pos1 = Position(1, 2, 3)

# Generated at 2024-06-04 19:16:48.667419
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:16:53.672073
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():    # Test case 1: Single message without index
    error = BaseError(text="An error occurred", code="error_code")
    assert str(error) == "An error occurred"

    # Test case 2: Multiple messages with index
    messages = [
        Message(text="First error", code="error_code_1", index=["field1"]),
        Message(text="Second error", code="error_code_2", index=["field2"]),
    ]
    error = BaseError(messages=messages)
    assert str(error) == "{'field1': 'First error', 'field2': 'Second error'}"

    # Test case 3: Single message with index
    error = BaseError(messages=[Message(text="Indexed error", code="error_code", index=["field"])])
    assert str(error) == "{'field': 'Indexed error'}"


# Generated at 2024-06-04 19:17:01.701452
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:03.769615
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:06.184058
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:07.845056
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:11.517754
# Unit test for method __eq__ of class Position
def test_Position___eq__():    pos1 = Position(1, 2, 3)

# Generated at 2024-06-04 19:17:13.911715
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:16.593779
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result_with_value = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:19.463086
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:17:21.747528
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:27.883960
# Unit test for method __eq__ of class Message
def test_Message___eq__():    message1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:17:36.478466
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:17:38.457684
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:40.241748
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:42.761760
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:44.987873
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:17:48.007020
# Unit test for method __eq__ of class Position
def test_Position___eq__():    pos1 = Position(1, 2, 3)

# Generated at 2024-06-04 19:17:52.113894
# Unit test for method __eq__ of class Message
def test_Message___eq__():    message1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:17:56.056284
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:17:57.896505
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:00.010279
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:18:05.734275
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:18:08.197125
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result_with_value = ValidationResult(value="some data")

# Generated at 2024-06-04 19:18:11.157944
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:13.612320
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:17.740156
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:18:19.629854
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:21.326376
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:18:23.277096
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:25.079903
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:26.734459
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:43.191638
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:44.894971
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:46.699291
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:50.228104
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="some data")

# Generated at 2024-06-04 19:18:51.937891
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:55.090356
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:57.231380
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:18:59.248808
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result_with_value = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:03.187919
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result_with_value = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:10.510305
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:19:30.692324
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:33.737455
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result_with_value = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:36.944304
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:38.705974
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:40.426507
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:19:42.611658
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:44.690560
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:19:47.626898
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:51.589523
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:19:53.437540
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:20:26.356026
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:29.579032
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:32.135109
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:34.349184
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:36.125872
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:38.411586
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:41.131577
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:43.681560
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:20:45.332796
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:20:49.452376
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:21:22.230526
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result_with_value = ValidationResult(value="some data")

# Generated at 2024-06-04 19:21:24.986165
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:21:27.094223
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:21:28.839377
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:21:30.603135
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:21:32.316915
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:21:34.911523
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:21:38.346889
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="valid_data")

# Generated at 2024-06-04 19:21:40.072660
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result = ValidationResult(value="validated_data")

# Generated at 2024-06-04 19:21:42.097079
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():    result_with_value = ValidationResult(value="some data")

# Generated at 2024-06-04 19:22:48.154576
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:22:52.542430
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:22:56.197262
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:23:00.180581
# Unit test for method __eq__ of class Message
def test_Message___eq__():    message1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:23:08.488579
# Unit test for method __eq__ of class Message
def test_Message___eq__():    message1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:23:11.581856
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:23:15.255742
# Unit test for method __eq__ of class Message
def test_Message___eq__():    message1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:23:20.224683
# Unit test for method __eq__ of class Message
def test_Message___eq__():    message1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:23:24.810368
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:23:29.954315
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:30.430642
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:33.139255
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:37.971971
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:25:41.839503
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:44.677702
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:47.226388
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:51.356361
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:53.304539
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")

# Generated at 2024-06-04 19:25:57.174291
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error message", code="error_code", key="key1")

# Generated at 2024-06-04 19:26:00.181651
# Unit test for method __eq__ of class Message
def test_Message___eq__():    msg1 = Message(text="Error 1", code="code1", key="key1")