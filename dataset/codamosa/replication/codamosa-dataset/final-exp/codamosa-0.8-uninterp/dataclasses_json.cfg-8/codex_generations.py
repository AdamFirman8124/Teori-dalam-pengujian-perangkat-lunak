

# Generated at 2022-06-13 19:09:40.685208
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(5) == False


# Generated at 2022-06-13 19:09:41.297969
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)


# Generated at 2022-06-13 19:09:42.361464
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    test_instance = Exclude.NEVER("test_field")
    assert test_instance is True


# Generated at 2022-06-13 19:09:43.698966
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude()
    assert a.NEVER(1) == False


# Generated at 2022-06-13 19:09:45.982823
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS (1)
    assert Exclude.ALWAYS (2)


# Generated at 2022-06-13 19:09:47.678154
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('foo')


# Generated at 2022-06-13 19:09:52.104883
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    import dataclasses
    @dataclasses.dataclass
    class Test:
        name: str
        age: int

    test= Test("Alex", 25)
    assert Exclude.NEVER(test) == False


# Generated at 2022-06-13 19:10:00.423849
# Unit test for function config
def test_config():
    @dataclass
    class ConfigParameters:
        # test string as encoder
        @config(encoder="json")
        def encoder_string(self):
            pass

        # test string as decoder
        @config(decoder="json")
        def decoder_string(self):
            pass

        # test string as undefined
        @config(undefined="EXCLUDE")
        def undefined_string(self):
            pass

        # test callback as encoder
        @config(encoder=str)
        def encoder_callback(self):
            pass

        # test callback as decoder
        @config(decoder=str)
        def decoder_callback(self):
            pass

        # test callback as undefined

# Generated at 2022-06-13 19:10:15.151328
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True
    assert Exclude.ALWAYS(dict()) == True
    assert Exclude.ALWAYS(set()) == True
    if Exclude.ALWAYS(1) == False: print("ALWAYS wrong")
    if Exclude.ALWAYS(dict([('a',1)])) == False: print("ALWAYS wrong")
    if Exclude.ALWAYS(set([1,2,3])) == False: print("ALWAYS wrong")
    return True


# Generated at 2022-06-13 19:10:17.990589
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Exclude.NEVER()
    result = Exclude.NEVER(1)
    # assert result == False
    assert result == False


# Generated at 2022-06-13 19:10:20.666640
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False


# Generated at 2022-06-13 19:10:21.955266
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("random") == False


# Generated at 2022-06-13 19:10:24.739413
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") is False
    assert Exclude.NEVER("a_field") is False
    assert Exclude.NEVER("a_constant") is False
    assert Exclude.NEVER("_a_private_variable") is False

# Generated at 2022-06-13 19:10:31.082338
# Unit test for function config
def test_config():
    @dataclass
    class A:
        x: int

        @classmethod
        def encoder(cls, value):
            return value

        @classmethod
        def decoder(cls, value):
            return value

        @classmethod
        def mm_field(cls):
            return None

        @classmethod
        def undefined(cls):
            return Undefined.RAISE

        @classmethod
        def letter_case(cls, value):
            return value

        @classmethod
        def exclude(cls, value):
            return False

    # encoder
    assert A.__dataclass_metadata__['dataclasses_json']['encoder'] is A.encoder
    # decoder

# Generated at 2022-06-13 19:10:33.901876
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(True) == False

# Generated at 2022-06-13 19:10:37.110283
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("Any value")
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS({})


# Generated at 2022-06-13 19:10:38.767675
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    def func(value):
        return True
    assert Exclude.ALWAYS == func


# Generated at 2022-06-13 19:10:42.879858
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS([1,2,3])
    assert Exclude.ALWAYS({'a':1})
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:10:44.828457
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    #assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:10:52.425356
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(1.0) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(()) == False
    assert Exclude.NEVER([]) == False
    assert Exclude.NEVER({}) == False
    assert Exclude.NEVER(set()) == False
    assert Exclude.NEVER(object()) == False


# Generated at 2022-06-13 19:10:54.968782
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(os.path)


# Generated at 2022-06-13 19:10:58.706751
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER({})
    assert Exclude.NEVER('')
    assert not Exclude.NEVER(0)


# Generated at 2022-06-13 19:11:00.966293
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:11:10.052523
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(False)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(0)
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(0.0)
    assert Exclude.NEVER(1.0)
    assert Exclude.NEVER('')
    assert Exclude.NEVER('a')
    assert Exclude.NEVER(None)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)
    assert Exclude.NEVER(object())
    assert Exclude.NEVER([])
    assert Exclude.NEVER([1, 2, 3])
    assert Exclude.NEVER([True, False])
    assert Exclude.NEVER(())
    assert Exclude.NEVER((1, 2, 3))


# Generated at 2022-06-13 19:11:11.815903
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    try:
        assert(Exclude.ALWAYS("a"))
    except:
        assert False


# Generated at 2022-06-13 19:11:13.783436
# Unit test for method NEVER of class Exclude

# Generated at 2022-06-13 19:11:23.212746
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("nume")
    assert Exclude.NEVER("undefined")
    assert Exclude.NEVER("")
    assert Exclude.NEVER("field_name")
    assert Exclude.NEVER("letter_case")
    assert Exclude.NEVER("exclude")
    assert Exclude.NEVER("test_global_config_get_and_set_encoder")
    assert Exclude.NEVER("test_global_config_get_and_set_decoder")
    assert Exclude.NEVER("test_global_config_get_and_set_mm_field")
    assert Exclude.NEVER("test_global_config_get_and_set_json_module")
    assert Exclude.NEVER("test_global_config_get_and_set_undefined")

# Generated at 2022-06-13 19:11:25.407381
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:11:27.478607
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:11:32.650283
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS("Hello")
    assert Exclude.ALWAYS("")
    assert Exclude.ALWAYS([1])
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS({"a": 1})
    assert Exclude.ALWAYS({"a": []})
    assert Exclude.ALWAYS({})


# Generated at 2022-06-13 19:11:37.300280
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test")


# Generated at 2022-06-13 19:11:39.061251
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:11:46.091769
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    """
    Test for method ALWAYS of class Exclude that always returns True by passing
    any argument
    :return:
    """
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(True) is True
    assert Exclude.ALWAYS(False) is True
    assert Exclude.ALWAYS(0.0) is True
    assert Exclude.ALWAYS(0.1) is True
    assert Exclude.ALWAYS(123) is True
    assert Exclude.ALWAYS(0b10101010) is True
    assert Exclude.ALWAYS(0x10101010) is True
    assert Exclude.ALWAYS(0o10101010) is True
    assert Exclude.ALWAYS("") is True
    assert Exclude.ALWAYS([]) is True
    assert Exclude.ALWAYS({}) is True

# Generated at 2022-06-13 19:11:47.518457
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    value = Exclude.ALWAYS('5')
    assert value == True


# Generated at 2022-06-13 19:11:58.018247
# Unit test for function config
def test_config():
    assert config() == {'dataclasses_json': {}}
    assert config(encoder={}) == {
        'dataclasses_json': {
            'encoder': {}
        }
    }
    assert config(mm_field=3) == {
        'dataclasses_json': {
            'mm_field': 3
        }
    }
    assert config(letter_case=3) == {
        'dataclasses_json': {
            'letter_case': 3
        }
    }
    assert config(field_name=3) == {
        'dataclasses_json': {
            'letter_case': lambda _: '3'
        }
    }

# Generated at 2022-06-13 19:12:04.818724
# Unit test for function config
def test_config():
    from dataclasses import dataclass
    from marshmallow import fields as mm_fields
    from marshmallow.types import Field, Metadata

    @config(encoder=lambda o: o, decoder=lambda o: o)
    @dataclass(config=config(field_name="test"))
    class Test:
        pass

    m = Test.__dataclass_metadata__
    assert m.encoder == Test.__dataclass_params__.encoder
    assert m.decoder == Test.__dataclass_params__.decoder
    assert m.field_name == "test"


if __name__ == '__main__':
    test_config()

# Generated at 2022-06-13 19:12:07.246701
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(42) == False
    assert Exclude.NEVER("dataclasses") == False
    assert Exclude.NEVER([1, 2, 3, 4, 5]) == False
    assert Exclude.NEVER(tuple([1, 2, 3, 4, 5])) == False
    assert Exclude.NEVER({"test"}) == False
    assert Exclude.NEVER(123.456) == False


# Generated at 2022-06-13 19:12:10.888864
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    """
    This test illustrates that the method ALWAYS of class Exclude 
    will return a True, no matter what.
    We test for a different type of input.
    """
    assert Exclude.ALWAYS (1) == True


# Generated at 2022-06-13 19:12:12.948996
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc") == False
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:12:21.732974
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Case 1:
    # Given:
    #   field_name: dataclasses_json.Exclude.ALWAYS
    #   metadata for this field:
    #     @config(exclude=Exclude.ALWAYS)
    #     name: str
    #   field_name is the return value of method field_name_to_attr_name
    # When:
    #   testing if field_name needs to be excluded
    # Then:
    #   should return True
    #   no attribtues are excluded from serialization
    assert Exclude.ALWAYS(1) is True


# Generated at 2022-06-13 19:12:31.033260
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False



# Generated at 2022-06-13 19:12:33.342282
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Create a variable to test this function
    variable = "variable"
    # Check that the variable is not included (it returns True)
    assert Exclude.NEVER(variable) == True


# Generated at 2022-06-13 19:12:37.037015
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def fTrue():
        return True
    if (fTrue()):
        print("Test for method NEVER of class Exclude passed")
    else:
        print("Test for method NEVER of class Exclude failed")


# Generated at 2022-06-13 19:12:39.867325
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    field = conf.fields | conf.exclude('field', Exclude.ALWAYS)
    assert field.metadata['dataclasses_json']['exclude'](field, field) == True



# Generated at 2022-06-13 19:12:42.212824
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # WHEN
    res = Exclude.ALWAYS(5)
    # THEN
    assert res is True


# Generated at 2022-06-13 19:12:43.490979
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:12:53.009243
# Unit test for function config
def test_config():
    class MyClass:
        pass
    
    assert config(MyClass) == {
        'dataclasses_json': {}
    }
    
    class MyClass:
        @config()
        def method():
            pass
    
    assert config(MyClass) == {
        'dataclasses_json': {}
    }
    
    @config()
    class MyClass:
        pass
    
    assert config(MyClass) == {
        'dataclasses_json': {}
    }
    
    assert config(field_name="myField") == {
        'dataclasses_json': {
            'letter_case': "myField"
        }
    }
    

# Generated at 2022-06-13 19:13:05.337903
# Unit test for function config
def test_config():
    import unittest
    import dataclasses

    @dataclasses.dataclass
    class MyClass:
        a: int
        b: str = dataclasses.field(metadata=config(undefined=Undefined.RAISE))

    with unittest.TestCase():
        with self.assertRaises(TypeError):
            MyClass(a=1)

    @dataclasses.dataclass
    class MyInheritingClass(MyClass):
        a: int
        b: str = dataclasses.field(metadata=config(undefined=Undefined.EXCLUDE))

    with unittest.TestCase():
        self.assertEqual(
            dataclasses_json.encode_dataclass(MyInheritingClass(a=1)),
            '{"a": 1}')

# Generated at 2022-06-13 19:13:06.549903
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:13:11.619800
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(0), "Exclude.NEVER return True"
    assert Exclude.NEVER(1), "Exclude.NEVER return True"
    assert not Exclude.NEVER(0), "Exclude.NEVER return False"
    assert not Exclude.NEVER(1), "Exclude.NEVER return False"
    assert Exclude.NEVER('a'), "Exclude.NEVER return True"
    assert not Exclude.NEVER('a'), "Exclude.NEVER return False"


# Generated at 2022-06-13 19:13:45.372242
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("x")


# Generated at 2022-06-13 19:13:46.390818
# Unit test for method NEVER of class Exclude

# Generated at 2022-06-13 19:13:48.486022
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("abc")


# Generated at 2022-06-13 19:13:54.418345
# Unit test for function config
def test_config():
    # Should be able to update all attributes
    @config(
        encoder=None,
        decoder=None,
        mm_field=None,
        letter_case=None,
        undefined=None,
        field_name=None,
        exclude=None
    )
    class TestClass:
        pass

    # Exclude should override everything
    @config(
        exclude=Exclude.ALWAYS
    )
    class TestClass2:
        pass

    # Exclude should override everything

# Generated at 2022-06-13 19:13:55.066541
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("1") == False

# Generated at 2022-06-13 19:13:57.948344
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(2) == False
    assert Exclude.NEVER(3) == False
    assert Exclude.NEVER(4) == False
    assert Exclude.NEVER(5) == False


# Generated at 2022-06-13 19:13:59.959965
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    test = Exclude.ALWAYS(False)
    assert test == True


# Generated at 2022-06-13 19:14:00.923404
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:14:04.460246
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:14:07.220663
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER('string') == False


# Generated at 2022-06-13 19:14:42.889793
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True

# Generated at 2022-06-13 19:14:43.780867
# Unit test for function config
def test_config():
    config(undefined='ignore')

# Generated at 2022-06-13 19:14:45.471951
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS('a')


# Generated at 2022-06-13 19:14:47.026419
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('x') is False


# Generated at 2022-06-13 19:14:49.931004
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) is False
    assert Exclude.NEVER(2.3) is False
    assert Exclude.NEVER(True) is False
    assert Exclude.NEVER(()) is False


# Generated at 2022-06-13 19:14:56.228841
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(bool)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(0.0)
    assert Exclude.ALWAYS(1.0)
    assert Exclude.ALWAYS("")
    assert Exclude.ALWAYS("str")
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({1: 2})


# Generated at 2022-06-13 19:14:58.207014
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    f = Exclude.NEVER
    assert f(1) is False


# Generated at 2022-06-13 19:14:59.618931
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:15:01.697100
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True



# Generated at 2022-06-13 19:15:03.702714
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # GIVEN
    functionNever = Exclude.NEVER

    # WHEN
    output = functionNever(1)

    # THEN
    assert output == False



# Generated at 2022-06-13 19:16:30.857732
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class Foo:
        pass

    f = Foo()
    assert(Exclude.NEVER(f))


# Generated at 2022-06-13 19:16:38.576221
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    exclude = Exclude.NEVER
    assert exclude(1) == False
    assert exclude("") == False
    assert exclude(object) == False
    assert exclude(Exclude) == False
    assert exclude(Exclude.NEVER) == False
    assert exclude(Exclude.ALWAYS) == False
    config(undefined=Undefined.RAISE)
    # TODO: setup for negative tests
    pass


# Generated at 2022-06-13 19:16:40.465474
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS(None) == True

# Generated at 2022-06-13 19:16:42.579410
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('x') == True
    assert Exclude.ALWAYS('y') == True
    assert Exclude.ALWAYS('z') == True


# Generated at 2022-06-13 19:16:43.963354
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	"""Should return false"""
	assert (Exclude.NEVER(1) == False)

# Generated at 2022-06-13 19:16:44.857959
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER


# Generated at 2022-06-13 19:16:49.743250
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    exclude = Exclude.ALWAYS
    assert exclude('a') == True
    assert exclude(1) == True
    assert exclude(True) == True
    assert exclude('') == True
    assert exclude(dict()) == True


# Generated at 2022-06-13 19:16:52.321968
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER("a") == False
    assert Exclude.NEVER([]) == False


# Generated at 2022-06-13 19:16:54.153191
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(1) == True)


# Generated at 2022-06-13 19:17:00.962095
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('a') is True
    assert Exclude.ALWAYS('b') is True
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(2) is True
    assert Exclude.ALWAYS(True) is True
    assert Exclude.ALWAYS(False) is True
    assert Exclude.ALWAYS(None) is True
