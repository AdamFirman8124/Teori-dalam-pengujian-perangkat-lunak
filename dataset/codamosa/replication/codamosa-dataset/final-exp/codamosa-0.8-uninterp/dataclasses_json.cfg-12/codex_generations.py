

# Generated at 2022-06-13 19:09:43.627853
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    print(Exclude.ALWAYS(10))
    print(Exclude.ALWAYS("10"))



# Generated at 2022-06-13 19:09:45.474013
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('abc') == True


# Generated at 2022-06-13 19:10:02.591731
# Unit test for function config
def test_config():
    from dataclasses import dataclass
    from dataclasses_json.api import dataclass_json

    @dataclass
    @dataclass_json
    class MyClass:
        a: int
        b: str

    c = MyClass(a=1, b="2")
    assert c.to_json() == '{"a":1,"b":"2"}'

    @dataclass_json
    @dataclass
    class MyClass:
        a: int
        b: str

    c = MyClass(a=1, b="2")
    assert c.to_json() == '{"a":1,"b":"2"}'

    @dataclass_json
    @config(letter_case=lambda s: s.upper())
    @dataclass
    class MyClass:
        a: int


# Generated at 2022-06-13 19:10:08.387148
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({1:2})
    assert Exclude.ALWAYS(('a','b','c'))
    assert Exclude.ALWAYS(['a','b','c'])
    assert Exclude.ALWAYS(None)

# Generated at 2022-06-13 19:10:09.562895
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:10:11.557826
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True, 'Result should be True'

# Generated at 2022-06-13 19:10:13.675240
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS("aaa")


# Generated at 2022-06-13 19:10:19.865221
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('') == True
    assert Exclude.ALWAYS(None) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(not None) == True
    assert Exclude.ALWAYS('a') == True
    assert Exclude.ALWAYS([]) == True
    assert Exclude.ALWAYS({}) == True
    assert Exclude.ALWAYS(()) == True
    assert Exclude.ALWAYS(set()) == True
    assert Exclude.ALWAYS(tuple()) == True
    assert Exclude.ALWAYS(dict()) == True
    assert Exclude.ALWAYS(list()) == True
    assert Exclude.ALWAYS(int()) == True
    assert Exclude.ALWAYS(float()) == True

# Generated at 2022-06-13 19:10:21.562785
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert False == Exclude.NEVER(None)
    assert False == Exclude.NEVER(1)


# Generated at 2022-06-13 19:10:22.792575
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:10:25.310060
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:10:31.418509
# Unit test for function config
def test_config():
    from dataclasses import dataclass, fields
    from marshmallow import fields as mm_fields
    from dataclasses_json import DataClassJsonMixin

    @config(letter_case=lambda x: x.upper(), exclude=Exclude.ALWAYS)
    @dataclass
    class MyDataClass(DataClassJsonMixin):
        a: int = 5
        b: str = "hi"

    assert MyDataClass.config().letter_case('lowercase') == 'LOWERCASE'
    assert MyDataClass.config().exclude('a', MyDataClass)
    assert MyDataClass.config().undefined == Undefined.EXCLUDE


# Generated at 2022-06-13 19:10:38.545540
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    def age_not_under_70(data_class_field_name: str, data_class_field_value: T) -> bool:
        return data_class_field_value < 70
    assert Exclude.NEVER("age_not_under_70", 70)
    assert Exclude.NEVER("age_not_under_70", 80)
    assert Exclude.NEVER("age_not_under_70", 90)
    assert Exclude.NEVER == age_not_under_70


# Generated at 2022-06-13 19:10:43.538610
# Unit test for function config
def test_config():
    import dataclasses_json as djs
    @djs.config(undefined="EXCLUDE")
    @dataclasses.dataclass
    class Test:
        a: int

    t = Test(a="")
    djs.encode(t, skip_defaults=True)

# Generated at 2022-06-13 19:10:48.170891
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(1) == True)
    assert(Exclude.ALWAYS('A') == True)
    assert(Exclude.ALWAYS([1,2,3]) == True)
    assert(Exclude.ALWAYS(None) == True)


# Generated at 2022-06-13 19:10:49.579142
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True


# Generated at 2022-06-13 19:10:50.702882
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    sl = Exclude.NEVER("test")
    assert sl is False

# Generated at 2022-06-13 19:10:51.281593
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False

# Generated at 2022-06-13 19:10:53.322745
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    #GIVEN
    test_value = 'Test'
    #WHEN
    result = Exclude.ALWAYS(test_value)
    #THEN
    assert result == True


# Generated at 2022-06-13 19:10:54.514180
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('a') is False


# Generated at 2022-06-13 19:10:58.184970
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(Exclude) is False


# Generated at 2022-06-13 19:11:00.477245
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:11:09.347440
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from dataclasses import dataclass, field

    @dataclass
    class S:
        a: str = field(
                metadata=dict(
                    dataclasses_json=dict(exclude=Exclude.NEVER)
                )
            )
    s = S(a='I am s.')
    assert True == s.a == s.__dict__['a']



# Generated at 2022-06-13 19:11:11.814830
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    cfg = config(exclude=Exclude.ALWAYS)
    assert cfg['dataclasses_json']['exclude'](None, None)


# Generated at 2022-06-13 19:11:13.784433
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True


# Generated at 2022-06-13 19:11:23.207032
# Unit test for function config
def test_config():
    class Test:
        def __init__(self, a: int, b: int = 1, c: int = 1, d: int = 1, e: int = 1, f: int = 1, g: int = 1, h: int = 1, i: int = 1, j: int = 1, k: int = 1, l: int = 1, m: int = 1, n: int = 1, o: int = 1, p: int = 1, q: int = 1, r: int = 1, s: int = 1, t: int = 1, u: int = 1, v: int = 1, w: int = 1, x: int = 1, y: int = 1, z: int = 1):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

# Generated at 2022-06-13 19:11:25.407762
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2) == False


# Generated at 2022-06-13 19:11:26.660635
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2)

# Generated at 2022-06-13 19:11:27.658471
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a") == False

# Generated at 2022-06-13 19:11:29.437596
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:11:32.796177
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:11:35.839920
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(None)



# Generated at 2022-06-13 19:11:36.597268
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False

# Generated at 2022-06-13 19:11:37.589779
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:11:43.034555
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = [1,2,3,4]
    assert Exclude.NEVER(a)
    assert Exclude.NEVER(None)
    assert Exclude.NEVER("")
    assert Exclude.NEVER("yes")
    assert Exclude.NEVER(False)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER("False")
    assert Exclude.NEVER("True")


# Generated at 2022-06-13 19:11:49.893353
# Unit test for function config
def test_config():
    from dataclasses import dataclass
    from marshmallow import Schema, fields
    from marshmallow.schema import BaseSchema
    from marshmallow.validate import Length
    from dataclasses_json import DataClassJsonMixin
    class Example(Schema, DataClassJsonMixin):
        class Meta:
            fields = ('id', 'name')

    example_schema = Example(strict=True)
    # NOTE: This could be a property, but the underlying field is a function,
    # and properties based on functions are weird.
    #
    # This is not a problem in marshmallow-dataclass, as the field is
    # serialization-only, and the underlying field is set to the serialization
    # only field.
    def name_field():
        # NOTE: More shorthand for this
        return fields.Function

# Generated at 2022-06-13 19:11:51.938250
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:12:01.290358
# Unit test for function config
def test_config():
    from unittest.mock import Mock
    from marshmallow import fields

    # common fields
    encoder = Mock(return_value='encoded')
    decoder = Mock(return_value='decoded')
    mm_field = fields.Field()
    field_name = 'field'
    letter_case = Mock(return_value='case')
    exclude = Mock(return_value=True)

    # const fields
    undefined = Undefined.EXCLUDE
    metadata = {}

    # test one by one
    config(
        metadata=metadata,
        encoder=encoder,
    )

    config(
        metadata=metadata,
        decoder=decoder,
    )

    config(
        metadata=metadata,
        mm_field=mm_field,
    )


# Generated at 2022-06-13 19:12:06.122868
# Unit test for function config
def test_config():
    metadata = {}
    @dataclass
    class Ad:
        name: str

    @global_config
    def func(x: str):
        return x

    new_metadata = config(metadata=metadata, exclude=func)
    assert new_metadata['dataclasses_json']['exclude'] is func

    @config(metadata=new_metadata, exclude=func)
    class Test:
        ad: Ad

    assert Test.__dataclass_fields__['ad'].metadata['dataclasses_json']['exclude'] is func

# Generated at 2022-06-13 19:12:07.654120
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)
    assert Exclude.NEVER('1')
    assert Exclude.NEVER(1.1)

# Generated at 2022-06-13 19:12:14.814964
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    df = {'a': 1, 'b': 2, 'c': 3}
    fields = ['a', 'b', 'c']
    assert Exclude.NEVER(fields) == False
    assert Exclude.NEVER(df) == False

# Generated at 2022-06-13 19:12:15.864724
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Setup
    obj = object()
    expected = False
    # Exercise
    actual = Exclude.NEVER(obj)
    # Verify
    assert (expected == actual)

# Generated at 2022-06-13 19:12:23.664180
# Unit test for function config
def test_config():
    def letter_case(x): return x

    @dataclass
    class _JSON:
        pass

    _metadata = config(encoder='_encoder', decoder='_decoder',
                       mm_field='_mm_field', letter_case=letter_case,
                       undefined='_undefined', exclude='_exclude')
    assert _metadata == {
        'dataclasses_json': {
            'encoder': '_encoder',
            'decoder': '_decoder',
            'mm_field': '_mm_field',
            'letter_case': letter_case,
            'undefined': '_undefined',
            'exclude': '_exclude',
        }
    }

# Generated at 2022-06-13 19:12:33.804952
# Unit test for function config
def test_config():
    import marshmallow
    from dataclasses import dataclass

    @dataclass
    class Foo:
        bar: str
        baz: str

        class Meta:
            dataclass_json = config(
                encoder=int,
                decoder=str,
                mm_field=marshmallow.fields.Integer(),
                undefined=Undefined.EXCLUDE,
                letter_case=lambda s: s.upper(),
                field_name='baz',
            )

    global_config.encoders[type(Foo())] = Foo.Meta.dataclass_json['encoder']
    global_config.decoders[type(Foo())] = Foo.Meta.dataclass_json['decoder']
    global_config.mm_fields[type(Foo())] = Foo.Meta.datac

# Generated at 2022-06-13 19:12:35.241980
# Unit test for method NEVER of class Exclude

# Generated at 2022-06-13 19:12:37.575483
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
test_Exclude_ALWAYS()


# Generated at 2022-06-13 19:12:40.012410
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER('string') == False


# Generated at 2022-06-13 19:12:42.049714
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('anything') == True


# Generated at 2022-06-13 19:12:48.360383
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER({})
    assert Exclude.NEVER(None)
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(0)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)
    assert Exclude.NEVER([])
    assert Exclude.NEVER([1])
    assert Exclude.NEVER(("test",))
    assert Exclude.NEVER("test")
    assert Exclude.NEVER("")


# Generated at 2022-06-13 19:12:49.827862
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:12:56.969095
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:12:57.868717
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:12:59.150921
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
  assert Exclude.ALWAYS(1) and Exclude.ALWAYS(-1) and Exclude.ALWAYS(0)


# Generated at 2022-06-13 19:13:00.803693
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:13:13.089432
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    input = {"a": 1, "b": 2}
    expected = False
    actual = Exclude.NEVER(input)
    # Verify that the actual value is correct
    assert expected == actual


# Generated at 2022-06-13 19:13:14.486500
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("never") == False


# Generated at 2022-06-13 19:13:22.292811
# Unit test for function config
def test_config():
    class Example:
        def __init__(self):
            self.x = 0

    # Test the config function
    lcase = lambda s: s.lower()
    ucase = lambda s: s.upper()

    conf = config(letter_case=lcase, exclude=Exclude.NEVER, field_name='select')
    assert conf.get('dataclasses_json').get('letter_case') == lcase
    assert conf.get('dataclasses_json').get('exclude') == Exclude.NEVER
    assert conf.get('dataclasses_json').get('field_name') == 'select'

    conf = config(letter_case=ucase, field_name='select')
    assert conf.get('dataclasses_json').get('letter_case') == ucase

# Generated at 2022-06-13 19:13:23.737129
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('foo') == False

# Generated at 2022-06-13 19:13:26.472033
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER([])
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(-1)

# Generated at 2022-06-13 19:13:27.709428
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(8)

# Generated at 2022-06-13 19:13:49.118771
# Unit test for function config
def test_config():
    import pytest

    @dataclasses.dataclass
    @config(mm_field=int)
    class A:
        a: int

    a = A(1)
    assert A.__annotations__['a'] == int
    assert a.__dict__['a'] == 1

    with pytest.raises(UndefinedParameterError):
        @dataclasses.dataclass
        @config(undefined='asdf')
        class A:
            a: int



# Generated at 2022-06-13 19:13:50.302678
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a")


# Generated at 2022-06-13 19:13:59.349019
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	assert Exclude.NEVER("ANYTHING"), "Exclude.NEVER is not False"


# Generated at 2022-06-13 19:14:08.133204
# Unit test for function config
def test_config():
    from dataclasses import dataclass
    @dataclass
    class Test:
        pass
    assert Test()._config == {'dataclasses_json': {}}
    assert Test()._config == Test()._config
    assert config() == Test()._config
    assert Test()._config is not config()

    assert Test()._config is not Test()._config

    assert config(mm_field=type('', (), {}))['dataclasses_json']['mm_field'] == type('', (), {})

# Generated at 2022-06-13 19:14:09.910022
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    #Arange
    field=Exclude.ALWAYS('')
    #Act
    #Assert
    assert field == True


# Generated at 2022-06-13 19:14:13.268253
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER('1') == False
    assert Exclude.NEVER('0') == False
    assert Exclude.NEVER('') == False


# Generated at 2022-06-13 19:14:23.328480
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    from typing import get_type_hints, Undefined, UndefinedType
    from dataclasses import dataclass

    @dataclass
    class MyClass:
        a: float = 5.0

    class MySubclass(MyClass):
        pass

    def is_superclass(x):
        return issubclass(x, MyClass)

    assert is_superclass(MyClass)
    assert is_superclass(MySubclass)
    # assert not is_superclass(dict)

    assert Exclude.NEVER(MyClass)
    assert Exclude.NEVER(MySubclass)
    # assert not Exclude.NEVER(dict)



# Generated at 2022-06-13 19:14:24.228374
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    Exclude.ALWAYS(1)

# Generated at 2022-06-13 19:14:26.195800
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("abc") == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS(" ") == True
    assert Exclude.ALWAYS("\n") == True


# Generated at 2022-06-13 19:14:28.614724
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Test that the method NEVER always returns false
    assert not Exclude.NEVER(True)
    assert not Exclude.NEVER(False)
    assert not Exclude.NEVER(None)


# Generated at 2022-06-13 19:15:06.284281
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    NEVER = Exclude.NEVER

    def assert_NEVER_False(false_value: bool):
        assert NEVER(false_value) is False, \
            f"NEVER({false_value}) should be false"

    assert_NEVER_False(0)
    assert_NEVER_False(1)
    assert_NEVER_False(-1)
    assert_NEVER_False(0.0)
    assert_NEVER_False(1.0)
    assert_NEVER_False(-1.0)
    assert_NEVER_False(0j)
    assert_NEVER_False(1j)
    assert_NEVER_False(-1j)
    assert_NEVER_False([])
    assert_NEVER_False([1])
    assert_NEVER_False(())
    assert_NEVER_False

# Generated at 2022-06-13 19:15:07.272219
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(datetime.datetime.now()) == False



# Generated at 2022-06-13 19:15:08.317607
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('Any Input')


# Generated at 2022-06-13 19:15:09.236347
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)  # returns False


# Generated at 2022-06-13 19:15:12.356936
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class Test:
        def __init__(self, *, a: int):
            self.a = a
    test_object = Test(a=5)
    assert(Exclude.NEVER(test_object.a) is True)
    assert(Exclude.NEVER(test_object) is False)


# Generated at 2022-06-13 19:15:14.447725
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True


# Generated at 2022-06-13 19:15:18.876523
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    from dataclasses import dataclass

    @dataclass
    class Test:
        name: str = config(exclude=Exclude.ALWAYS)

    assert Test.name.exclude == Exclude.ALWAYS


# Generated at 2022-06-13 19:15:21.208754
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    my_exclude = Exclude()
    assert my_exclude.NEVER(2) == False

# Generated at 2022-06-13 19:15:23.997530
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # given
    a = 1
    # when
    b = Exclude.NEVER(a)
    # then
    assert b


# Generated at 2022-06-13 19:15:32.061370
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True

# Generated at 2022-06-13 19:16:35.154569
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:16:37.984047
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS('Bob')
    assert Exclude.ALWAYS(1234)


# Generated at 2022-06-13 19:16:40.688751
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS("abc") == True
    assert Exclude.ALWAYS("True") == True


# Generated at 2022-06-13 19:16:45.221490
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) is True
    assert Exclude.ALWAYS(None) is True
    assert Exclude.ALWAYS(0) is True
    assert Exclude.ALWAYS(True) is True
    assert Exclude.ALWAYS('') is True
    assert Exclude.ALWAYS({}) is True
    assert Exclude.ALWAYS([]) is True
    assert Exclude.ALWAYS(False) is True


# Generated at 2022-06-13 19:16:47.275673
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:16:49.920298
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)


# Generated at 2022-06-13 19:16:51.620626
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)



# Generated at 2022-06-13 19:16:53.683562
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True



# Generated at 2022-06-13 19:16:57.244354
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	assert(Exclude.NEVER("") == False)
	assert(Exclude.NEVER("Anything") == False)


# Generated at 2022-06-13 19:17:00.994653
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
  dataclasses_json.config(exclude=Exclude.ALWAYS)
  assert dataclasses_json.config()['dataclasses_json']['exclude'].__name__ == '<lambda>'


# Generated at 2022-06-13 19:19:27.924079
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    print("test function test_Exclude_NEVER in test_config.py")
    class mytestdataclass(dataclasses.dataclass):
        field1: str = dataclasses.field(metadata=config(exclude=Exclude.NEVER))
        field2: str = dataclasses.field()

    test_instance = mytestdataclass("test","test")

    expected = {'field1': "test"}
    actual = dataclasses_json.dump(test_instance)
    assert expected == actual

    # expected = {'field2': 'test'}
    # actual = dataclasses_json.dump(test_instance)
    # assert expected == actual

    # expected = {'field2': 'test'}
    # actual = dataclasses_json.dump(test_instance)
    # assert expected

# Generated at 2022-06-13 19:19:29.661983
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS(object)

# Generated at 2022-06-13 19:19:37.131873
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(True)
    assert Exclude.NEVER(False)
    assert Exclude.NEVER("test")
    assert Exclude.NEVER(None)
    assert Exclude.NEVER([])
    assert Exclude.NEVER({})
    assert Exclude.NEVER(("test", 1, []))


# Generated at 2022-06-13 19:19:38.847732
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    obj = object()
    assert Exclude.ALWAYS(obj)
    

# Generated at 2022-06-13 19:19:40.701547
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)
    assert Exclude.NEVER("foo")
    assert Exclude.NEVER(b"foo")
