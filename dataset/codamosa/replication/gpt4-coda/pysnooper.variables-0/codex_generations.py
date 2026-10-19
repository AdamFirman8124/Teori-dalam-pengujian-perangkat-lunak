

# Generated at 2024-03-18 00:30:51.590210
# Unit test for method __getitem__ of class Indices
def test_Indices___getitem__():    # Create an instance of Indices with a source that represents a list
    indices = Indices('my_list')

    # Slice the indices to get a new Indices object
    sliced_indices = indices[1:3]

    # Check that the new Indices object has the correct slice
    assert sliced_indices._slice == slice(1, 3), "The slice of the new Indices object is incorrect"

    # Check that the source of the new Indices object is the same as the original
    assert sliced_indices.source == indices.source, "The source of the new Indices object should be the same as the original"

    # Check that the new Indices object is a deepcopy of the original
    assert sliced_indices is not indices, "The new Indices object should be a different instance from the original"
    assert sliced_indices._fingerprint != indices._fingerprint, "The fingerprint of the new Indices object should be different from the original"

    # Check that the exclude attribute is copied

# Generated at 2024-03-18 00:30:57.896259
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('a', 'b'))
    var2 = BaseVariable('test_var', exclude=('a', 'b'))

    # Create a third instance of BaseVariable with a different source
    var3 = BaseVariable('another_var', exclude=('a', 'b'))

    # Create a fourth instance of BaseVariable with a different exclude
    var4 = BaseVariable('test_var', exclude=('c',))

    # Test that var1 and var2 are equal
    assert var1 == var2, "var1 and var2 should be equal"

    # Test that var1 and var3 are not equal (different source)
    assert var1 != var3, "var1 and var3 should not be equal due to different source"

    # Test that var1 and var4 are not equal (different exclude)
    assert var1 != var

# Generated at 2024-03-18 00:31:03.419892
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('a', 'b'))
    var2 = BaseVariable('test_var', exclude=('a', 'b'))

    # Create a third BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('a', 'b'))

    # Create a fourth BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('c',))

    # Test that var1 and var2 are equal
    assert var1 == var2, "var1 and var2 should be equal"

    # Test that var1 and var3 are not equal (different source)
    assert var1 != var3, "var1 and var3 should not be equal"

    # Test that var1 and var4 are not equal (different exclude)

# Generated at 2024-03-18 00:31:09.554727
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('excluded_key',))
    var2 = BaseVariable('test_var', exclude=('excluded_key',))

    # Create another BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('excluded_key',))

    # Create another BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('another_excluded_key',))

    # Test equality of the same instances
    assert var1 == var1, "Same instance should be equal to itself"

    # Test equality of two instances with the same source and exclude
    assert var1 == var2, "Instances with the same source and exclude should be equal"

    # Test inequality with different source
    assert not (var1 == var3), "Instances with different sources should not be equal"

    #

# Generated at 2024-03-18 00:31:17.231983
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import unittest.mock as mock


# Generated at 2024-03-18 00:31:25.703699
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:31:30.676915
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    variable1 = BaseVariable('test_var', exclude=('a', 'b'))
    variable2 = BaseVariable('test_var', exclude=('a', 'b'))

    # Create another instance with a different source
    variable3 = BaseVariable('another_var', exclude=('a', 'b'))

    # Create another instance with a different exclude
    variable4 = BaseVariable('test_var', exclude=('c',))

    # Test equality of the first two variables
    assert variable1 == variable2, "Variables with the same source and exclude should be equal"

    # Test inequality with a different source
    assert not (variable1 == variable3), "Variables with different sources should not be equal"

    # Test inequality with a different exclude
    assert not (variable1 == variable4), "Variables with different excludes should not be equal"

# Generated at 2024-03-18 00:31:32.248186
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:31:41.500195
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import unittest.mock as mock


# Generated at 2024-03-18 00:31:46.897892
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:31:59.364470
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('a', 'b'))
    var2 = BaseVariable('test_var', exclude=('a', 'b'))

    # Create a third BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('a', 'b'))

    # Create a fourth BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('c',))

    # Test that var1 and var2 are equal
    assert var1 == var2, "var1 and var2 should be equal"

    # Test that var1 and var3 are not equal (different source)
    assert not (var1 == var3), "var1 and var3 should not be equal"

    # Test that var1 and var4 are not equal (different exclude)

# Generated at 2024-03-18 00:32:07.164006
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:32:08.378755
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:32:13.137080
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('excluded_key',))
    var2 = BaseVariable('test_var', exclude=('excluded_key',))

    # Create a third BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('excluded_key',))

    # Create a fourth BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('another_excluded_key',))

    # Test that var1 and var2 are considered equal
    assert var1 == var2, "var1 and var2 should be equal"

    # Test that var1 and var3 are not considered equal (different source)
    assert not (var1 == var3), "var1 and var3 should not be equal"

    # Test that var1 and var4 are not considered equal (different exclude)

# Generated at 2024-03-18 00:32:18.859217
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('a', 'b'))
    var2 = BaseVariable('test_var', exclude=('a', 'b'))

    # Create a third BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('a', 'b'))

    # Create a fourth BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('c',))

    # Test that var1 and var2 are considered equal
    assert var1 == var2, "var1 and var2 should be equal"

    # Test that var1 and var3 are not considered equal (different source)
    assert not (var1 == var3), "var1 and var3 should not be equal"

    # Test that var1 and var4 are not considered equal (different exclude)

# Generated at 2024-03-18 00:32:23.736477
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:32:24.840658
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:32:30.564615
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    var1 = BaseVariable('x', exclude=('a',))
    var2 = BaseVariable('x', exclude=('a',))

    # Create another instance with a different source
    var3 = BaseVariable('y', exclude=('a',))

    # Create another instance with a different exclude
    var4 = BaseVariable('x', exclude=('b',))

    # Test equality of the first two instances
    assert var1 == var2, "var1 and var2 should be equal"

    # Test inequality with different source
    assert var1 != var3, "var1 and var3 should not be equal"

    # Test inequality with different exclude
    assert var1 != var4, "var1 and var4 should not be equal"

    # Test equality with itself
    assert var1 == var1, "var1 should be equal to itself"



# Generated at 2024-03-18 00:32:31.601599
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:32:32.375974
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:32:59.328132
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('excluded_key',))
    var2 = BaseVariable('test_var', exclude=('excluded_key',))

    # Create another instance with a different source
    var3 = BaseVariable('another_var', exclude=('excluded_key',))

    # Create another instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('other_excluded_key',))

    # Test equality of the same instances
    assert var1 == var1, "Same instance should be equal to itself"

    # Test equality of two instances with the same source and exclude
    assert var1 == var2, "Instances with the same source and exclude should be equal"

    # Test inequality with different source
    assert not (var1 == var3), "Instances with different sources should not be equal"

    # Test inequality with different exclude


# Generated at 2024-03-18 00:33:00.081214
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:01.155761
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:01.985501
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:09.897938
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    var1 = BaseVariable('x', exclude=('a',))
    var2 = BaseVariable('x', exclude=('a',))

    # Create another instance with a different source
    var3 = BaseVariable('y', exclude=('a',))

    # Create another instance with a different exclude
    var4 = BaseVariable('x', exclude=('b',))

    # Test equality of the first two instances
    assert var1 == var2, "var1 should be equal to var2"

    # Test inequality with different source
    assert var1 != var3, "var1 should not be equal to var3"

    # Test inequality with different exclude
    assert var1 != var4, "var1 should not be equal to var4"

    # Test equality with itself
    assert var1 == var1, "var1 should be equal to itself"

    # Test

# Generated at 2024-03-18 00:33:18.230837
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:18.947494
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:19.701761
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:20.613918
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:28.516651
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('attr1',))
    var2 = BaseVariable('test_var', exclude=('attr1',))

    # Create another instance with a different source
    var3 = BaseVariable('another_var', exclude=('attr1',))

    # Create another instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('attr2',))

    # Test equality of var1 and var2 (should be True)
    assert var1 == var2, "var1 and var2 should be equal"

    # Test equality of var1 and var3 (should be False)
    assert not (var1 == var3), "var1 and var3 should not be equal"

    # Test equality of var1 and var4 (should be False)

# Generated at 2024-03-18 00:33:47.948244
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:48.811084
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:49.859845
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:50.889743
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:51.604107
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:52.807505
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:53.483993
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:33:54.744974
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:34:01.057978
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('attr1',))
    var2 = BaseVariable('test_var', exclude=('attr1',))

    # Create a third BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('attr1',))

    # Create a fourth BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('attr2',))

    # Test equality of the first two variables (should be True)
    assert var1 == var2, "Variables with the same source and exclude should be equal"

    # Test inequality with a different source (should be False)
    assert not (var1 == var3), "Variables with different sources should not be equal"

    # Test inequality with a different exclude (should be False)

# Generated at 2024-03-18 00:34:06.348848
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:34:41.645965
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:34:42.508375
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:34:43.328682
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:34:44.246314
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:34:50.677212
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('a', 'b'))
    var2 = BaseVariable('test_var', exclude=('a', 'b'))

    # Create another instance with a different source
    var3 = BaseVariable('another_var', exclude=('a', 'b'))

    # Create another instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('c',))

    # Test equality of the same instances
    assert var1 == var1, "Same instance should be equal to itself"

    # Test equality of two instances with the same source and exclude
    assert var1 == var2, "Instances with the same source and exclude should be equal"

    # Test inequality with different source
    assert not (var1 == var3), "Instances with different sources should not be equal"

    # Test inequality with different exclude


# Generated at 2024-03-18 00:34:56.344072
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('excluded_key',))
    var2 = BaseVariable('test_var', exclude=('excluded_key',))

    # Create a third instance of BaseVariable with a different source
    var3 = BaseVariable('another_var', exclude=('excluded_key',))

    # Create a fourth instance of BaseVariable with a different exclude
    var4 = BaseVariable('test_var', exclude=('another_excluded_key',))

    # Test that var1 and var2 are equal
    assert var1 == var2, "var1 and var2 should be equal"

    # Test that var1 and var3 are not equal (different source)
    assert not (var1 == var3), "var1 and var3 should not be equal"

    # Test that var1 and var4 are not equal (different exclude)

# Generated at 2024-03-18 00:35:02.614689
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two instances of BaseVariable with the same source and exclude
    variable1 = BaseVariable('test_var', exclude=('excluded_key',))
    variable2 = BaseVariable('test_var', exclude=('excluded_key',))

    # Create a third instance of BaseVariable with a different source
    variable3 = BaseVariable('another_var', exclude=('excluded_key',))

    # Create a fourth instance of BaseVariable with a different exclude
    variable4 = BaseVariable('test_var', exclude=('another_excluded_key',))

    # Test that variable1 and variable2 are equal
    assert variable1 == variable2, "variable1 and variable2 should be equal"

    # Test that variable1 and variable3 are not equal (different source)
    assert not (variable1 == variable3), "variable1 and variable3 should not be equal"

    # Test that variable1 and variable4 are not equal (different exclude)

# Generated at 2024-03-18 00:35:12.047121
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:35:19.504243
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import unittest.mock as mock


# Generated at 2024-03-18 00:35:20.209509
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:36:33.429388
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:36:34.351851
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:36:41.785836
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('a', 'b'))
    var2 = BaseVariable('test_var', exclude=('a', 'b'))

    # Create another BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('a', 'b'))

    # Create another BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('c',))

    # Test equality of the same instances
    assert var1 == var1, "Same instance should be equal to itself"

    # Test equality of two instances with the same source and exclude
    assert var1 == var2, "Instances with the same source and exclude should be equal"

    # Test inequality with different source
    assert not (var1 == var3), "Instances with different sources should not be equal"

    # Test inequality with

# Generated at 2024-03-18 00:36:47.722482
# Unit test for method __eq__ of class BaseVariable
def test_BaseVariable___eq__():    # Create two BaseVariable instances with the same source and exclude
    var1 = BaseVariable('test_var', exclude=('excluded_key',))
    var2 = BaseVariable('test_var', exclude=('excluded_key',))

    # Create a third BaseVariable instance with a different source
    var3 = BaseVariable('another_var', exclude=('excluded_key',))

    # Create a fourth BaseVariable instance with a different exclude
    var4 = BaseVariable('test_var', exclude=('another_excluded_key',))

    # Test that var1 and var2 are equal
    assert var1 == var2, "var1 and var2 should be equal"

    # Test that var1 and var3 are not equal (different source)
    assert var1 != var3, "var1 and var3 should not be equal due to different source"

    # Test that var1 and var4 are not equal (different exclude)
    assert var

# Generated at 2024-03-18 00:36:48.416811
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:36:56.027381
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import sys

# Generated at 2024-03-18 00:36:56.760561
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:36:57.814309
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:36:58.868293
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:36:59.595144
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:16.991142
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:17.681467
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:25.725183
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import unittest.mock as mock


# Generated at 2024-03-18 00:39:40.617644
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():    import types


# Generated at 2024-03-18 00:39:41.369220
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:42.167071
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:43.268597
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:44.486335
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:45.939365
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock


# Generated at 2024-03-18 00:39:46.821782
# Unit test for method items of class BaseVariable
def test_BaseVariable_items():import unittest
from unittest.mock import MagicMock
