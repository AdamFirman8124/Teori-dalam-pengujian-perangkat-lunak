

# Generated at 2024-03-18 06:47:54.015079
# Unit test for method case of class Either

# Generated at 2024-03-18 06:48:00.141428
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:48:03.440228
# Unit test for method case of class Either

# Generated at 2024-03-18 06:48:06.197171
# Unit test for method case of class Either

# Generated at 2024-03-18 06:48:10.610000
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.run() == 10, "Right to_lazy should return Lazy with the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.run() == "error", "Left to_lazy should return Lazy with the original value"


# Generated at 2024-03-18 06:48:13.601800
# Unit test for method case of class Either

# Generated at 2024-03-18 06:48:21.484782
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:48:27.559992
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.run() == 10, "Right to_lazy should return Lazy with the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.run() == "error", "Left to_lazy should return Lazy with the original value"


# Generated at 2024-03-18 06:48:32.997631
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:48:37.800711
# Unit test for method case of class Either

# Generated at 2024-03-18 06:48:52.318794
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:48:55.211965
# Unit test for method case of class Either

# Generated at 2024-03-18 06:48:59.650976
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Transform to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.run() == 10, "Right to_lazy should return Lazy with the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Transform to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.run() == "error", "Left to_lazy should return Lazy with the original value"


# Generated at 2024-03-18 06:49:07.010550
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:49:10.857656
# Unit test for method case of class Either

# Generated at 2024-03-18 06:49:14.791792
# Unit test for method case of class Either

# Generated at 2024-03-18 06:49:20.807457
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with a value
    right_value = Right(10)
    lazy_right = right_value.to_lazy()
    assert lazy_right() == 10, "Right.to_lazy should return a Lazy that evaluates to the Right's value"

    # Create a Left instance with a value
    left_value = Left("Error")
    lazy_left = left_value.to_lazy()
    assert lazy_left() == "Error", "Left.to_lazy should return a Lazy that evaluates to the Left's value"


# Generated at 2024-03-18 06:49:25.635370
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.value() == 10, "The Lazy instance should return the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.value() == "error", "The Lazy instance should return the original value"


# Generated at 2024-03-18 06:49:27.621492
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    lazy_value = Right(10).to_lazy()

# Generated at 2024-03-18 06:49:32.096219
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:49:40.034750
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:49:45.027584
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:49:54.174974
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left = Left("error")

# Generated at 2024-03-18 06:50:00.071302
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.value() == 10, "Right to_lazy should return Lazy with the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.value() == "error", "Left to_lazy should return Lazy with the original value"


# Generated at 2024-03-18 06:50:04.190154
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:50:06.963261
# Unit test for method case of class Either

# Generated at 2024-03-18 06:50:13.601873
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:50:21.294614
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:50:27.343084
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:50:31.133188
# Unit test for method case of class Either

# Generated at 2024-03-18 06:50:38.976215
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:50:43.981380
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:50:46.702786
# Unit test for method case of class Either

# Generated at 2024-03-18 06:50:51.512396
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.value() == 10, "Right to_lazy should return Lazy with the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.value() == "error", "Left to_lazy should return Lazy with the original value"


# Generated at 2024-03-18 06:51:03.564966
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:51:08.023756
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:51:14.829460
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:51:23.175807
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left = Left("error")

# Generated at 2024-03-18 06:51:27.440455
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:51:33.659139
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:51:40.477055
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:51:48.456830
# Unit test for method case of class Either

# Generated at 2024-03-18 06:51:54.442039
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:51:59.099687
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:52:03.715096
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:52:08.399526
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:52:13.973292
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:52:20.213616
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:52:27.097858
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left = Left("error")

# Generated at 2024-03-18 06:52:34.332572
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left = Left("error")

# Generated at 2024-03-18 06:52:41.588178
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    from pymonet.lazy import Lazy

    # Test Right to_lazy

# Generated at 2024-03-18 06:52:50.370517
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:52:53.268928
# Unit test for method case of class Either

# Generated at 2024-03-18 06:52:57.753844
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:53:01.282068
# Unit test for method case of class Either

# Generated at 2024-03-18 06:53:03.545198
# Unit test for method case of class Either

# Generated at 2024-03-18 06:53:07.534531
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:53:09.928382
# Unit test for method case of class Either

# Generated at 2024-03-18 06:53:15.915128
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:53:22.475371
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:53:41.844470
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:53:49.334001
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:53:55.323631
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:53:58.495758
# Unit test for method case of class Either

# Generated at 2024-03-18 06:54:02.792999
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.run() == 10, "Right to_lazy should return Lazy with the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.run() == "error", "Left to_lazy should return Lazy with the original value"


# Generated at 2024-03-18 06:54:07.783860
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:54:12.716961
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:54:15.188401
# Unit test for method case of class Either

# Generated at 2024-03-18 06:54:17.682150
# Unit test for method case of class Either

# Generated at 2024-03-18 06:54:21.120112
# Unit test for method case of class Either

# Generated at 2024-03-18 06:54:31.958590
# Unit test for method case of class Either

# Generated at 2024-03-18 06:54:37.846151
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.value() == 10, "The Lazy instance should return the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.value() == "error", "The Lazy instance should return the original value"


# Generated at 2024-03-18 06:54:44.353659
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:54:48.505148
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    from pymonet.lazy import Lazy

    # Test with Right

# Generated at 2024-03-18 06:54:54.167668
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:54:56.704911
# Unit test for method case of class Either

# Generated at 2024-03-18 06:55:02.414159
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:55:05.154338
# Unit test for method case of class Either

# Generated at 2024-03-18 06:55:08.562289
# Unit test for method case of class Either

# Generated at 2024-03-18 06:55:13.895408
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:55:29.941410
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:55:36.695591
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:55:43.460324
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:55:46.798846
# Unit test for method case of class Either

# Generated at 2024-03-18 06:55:49.687216
# Unit test for method case of class Either

# Generated at 2024-03-18 06:55:54.916816
# Unit test for method case of class Either

# Generated at 2024-03-18 06:56:03.573555
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:56:08.282093
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:56:13.015086
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:56:17.858134
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains the correct function
    assert lazy_value.value() == 10, "Right to_lazy should contain the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains the correct function
    assert lazy_error.value() == "error", "Left to_lazy should contain the original value"


# Generated at 2024-03-18 06:56:41.098944
# Unit test for method case of class Either

# Generated at 2024-03-18 06:56:45.948288
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:56:48.905180
# Unit test for method case of class Either

# Generated at 2024-03-18 06:56:53.625367
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:57:00.649364
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the lazy value returns the original value when called
    assert lazy_value() == 10, "Right to_lazy should return original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the lazy error returns the original value when called
    assert lazy_error() == "error", "Left to_lazy should return original value"


# Generated at 2024-03-18 06:57:06.855265
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left1 = Left("Error")

# Generated at 2024-03-18 06:57:11.753096
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:57:16.981242
# Unit test for method __eq__ of class Either
def test_Either___eq__():    left_a = Left("Error A")

# Generated at 2024-03-18 06:57:18.969033
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    lazy_value = Right(10).to_lazy()

# Generated at 2024-03-18 06:57:25.549171
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():    # Create a Right instance with value 10
    right_value = Right(10)
    # Convert to Lazy
    lazy_value = right_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_value.run() == 10, "The Lazy instance should contain the original value"

    # Create a Left instance with value "error"
    left_value = Left("error")
    # Convert to Lazy
    lazy_error = left_value.to_lazy()
    # Check if the Lazy instance contains a function that returns the original value
    assert lazy_error.run() == "error", "The Lazy instance should contain the original error"
