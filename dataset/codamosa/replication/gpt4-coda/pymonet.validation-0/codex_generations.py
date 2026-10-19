

# Generated at 2024-03-18 06:57:32.640099
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:57:37.565390
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:57:41.394574
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() == None

# Generated at 2024-03-18 06:57:45.083741
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:57:48.436102
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:57:52.056755
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:57:55.407519
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() is None

# Generated at 2024-03-18 06:57:59.161423
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() == None

# Generated at 2024-03-18 06:58:03.561585
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:07.770840
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:17.248491
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:20.963476
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:24.015716
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:27.473134
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:31.111887
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:34.514671
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() == None

# Generated at 2024-03-18 06:58:36.894096
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Arrange
    success_validation = Validation.success(10)
    fail_validation = Validation.fail(['error'])

    # Act
    success_lazy = success_validation.to_lazy()
    fail_lazy = fail_validation.to_lazy()

    # Assert
    assert success_lazy() == 10
    assert fail_lazy() == None

# Generated at 2024-03-18 06:58:39.702332
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:44.596104
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:47.680983
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:58:59.009346
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:01.913878
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:05.132016
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:08.566883
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:12.186034
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error1', 'error2'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() is None

# Generated at 2024-03-18 06:59:16.360392
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 06:59:20.981757
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() == None

# Generated at 2024-03-18 06:59:24.316293
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:27.789651
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:30.317896
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:51.247012
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:54.569885
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 06:59:57.535170
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:00:01.736415
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:00:04.490750
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:00:07.625521
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:00:12.443980
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:00:15.266400
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() is None

# Generated at 2024-03-18 07:00:18.133647
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() is None

# Generated at 2024-03-18 07:00:21.556371
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:01:01.070146
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error1', 'error2'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() is None

# Generated at 2024-03-18 07:01:06.720500
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:01:11.541137
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:01:14.979544
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error1', 'error2'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() is None

# Generated at 2024-03-18 07:01:17.995323
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error1', 'error2'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() == None

# Generated at 2024-03-18 07:01:22.201030
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:01:25.251711
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:01:29.856861
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:01:32.407830
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:01:36.191211
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:02:50.243891
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:02:52.947864
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:02:57.943469
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:03:03.403858
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:03:07.037681
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:03:10.548251
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:03:14.722993
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:03:19.923576
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:03:22.906455
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:03:26.418827
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:05:42.953151
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:05:46.101927
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:05:49.537714
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:05:53.173323
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:05:55.953519
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test successful Validation to Lazy transformation
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failed Validation to Lazy transformation
    fail_validation = Validation.fail(['error1', 'error2'])
    lazy_fail = fail_validation.to_lazy()
    assert lazy_fail.run() is None

# Generated at 2024-03-18 07:05:59.024683
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:06:02.597282
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:06:05.509665
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    # Test success case
    success_validation = Validation.success(10)
    lazy_success = success_validation.to_lazy()
    assert lazy_success.run() == 10

    # Test failure case
    failure_validation = Validation.fail(['error'])
    lazy_failure = failure_validation.to_lazy()
    assert lazy_failure.run() is None

# Generated at 2024-03-18 07:06:08.953912
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case

# Generated at 2024-03-18 07:06:11.967441
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():    from pymonet.lazy import Lazy

    # Test success case