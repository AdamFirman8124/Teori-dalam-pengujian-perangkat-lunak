

# Generated at 2022-06-13 19:09:41.418964
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("") == False


# Generated at 2022-06-13 19:09:43.912318
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(4)
    assert Exclude.ALWAYS('string')
    assert Exclude.ALWAYS(object())


# Generated at 2022-06-13 19:09:45.727227
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(5) == True


# Generated at 2022-06-13 19:09:54.319492
# Unit test for function config
def test_config():
    decoder_arg_list = [
        dict(encoder=lambda _: None),
        dict(decoder=lambda _: None),
        dict(mm_field=lambda _: None),
        dict(letter_case=lambda _: _),
        dict(undefined=Undefined.RAISE),
        dict(field_name="field"),
        dict(exclude=lambda x: False),
    ]

    for args in decoder_arg_list:
        assert config(**args)['dataclasses_json'] == args


# Generated at 2022-06-13 19:09:56.259063
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True

test_Exclude_ALWAYS()


# Generated at 2022-06-13 19:09:59.052529
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(1.0) == True
    assert Exclude.ALWAYS("hello") == True


# Generated at 2022-06-13 19:10:00.259264
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert(Exclude.ALWAYS(1))


# Generated at 2022-06-13 19:10:08.739424
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("aaa")

# Generated at 2022-06-13 19:10:10.941393
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Case of single item
    assert Exclude.ALWAYS(1) is True
    # Case of multiple items
    assert Exclude.ALWAYS(1, 2, 3) is True


# Generated at 2022-06-13 19:10:14.845098
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # arrange
    ALWAYS = Exclude.ALWAYS

    # act
    result = ALWAYS(None)

    # assert
    assert result == True


# Generated at 2022-06-13 19:10:25.614908
# Unit test for function config
def test_config():
    import marshmallow as mm

    @dataclasses.dataclass
    @config(
        encoder=lambda i: i * 2,
        decoder=lambda i: i * 3,
        mm_field=mm.fields.Float,
        field_name="x_y",
        letter_case=lambda x: x.upper(),
        exclude=Exclude.ALWAYS,
        undefined=Undefined.EXCLUDE,
    )
    class MyClass:
        value: int

    def encoder(obj):
        return obj.value

    def decoder(value):
        return MyClass(value)


# Generated at 2022-06-13 19:10:29.296788
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(2)
    assert Exclude.NEVER(3)


# Generated at 2022-06-13 19:10:39.977220
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False
    assert Exclude.NEVER('a') == False
    assert Exclude.NEVER(1.1) == False
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(None) == False
    assert Exclude.NEVER(id) == False
    assert Exclude.NEVER(int) == False
    assert Exclude.NEVER(str) == False
    assert Exclude.NEVER(float) == False
    assert Exclude.NEVER(list) == False
    assert Exclude.NEVER(dict) == False
    assert Exclude.NEVER(set) == False
    assert Exclude.NEVER(tuple) == False


# Generated at 2022-06-13 19:10:41.669129
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:10:44.772633
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Arrange
    d = DataClass("dataclass")
    # Act
    actual = Exclude.NEVER(d)
    # Assert
    assert actual == False


# Generated at 2022-06-13 19:10:53.054663
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(0.0)
    assert Exclude.ALWAYS(0.1)
    assert Exclude.ALWAYS('q')
    assert Exclude.ALWAYS(' ')
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS([1])
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS({'a': 1})
    assert Exclude.ALWAYS(Exclude.ALWAYS)
    assert Exclude.ALWAYS(Exclude.NEVER)


# Generated at 2022-06-13 19:10:56.695220
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER
    b = Exclude.NEVER
    c = False
    assert (a == b) == c

# Generated at 2022-06-13 19:10:58.962000
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('hi')


# Generated at 2022-06-13 19:11:00.559129
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None)

# Generated at 2022-06-13 19:11:06.794405
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(4) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(5.5) == True
    # fails
    # assert Exclude.ALWAYS(True) != False


# Generated at 2022-06-13 19:11:09.371141
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("TEST 1") is False


# Generated at 2022-06-13 19:11:11.252255
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    """ Test function test_Exclude_NEVER.
    """
    assert Exclude.NEVER("test") is False

# Generated at 2022-06-13 19:11:12.293063
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("")
    return 0


# Generated at 2022-06-13 19:11:14.870259
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("Hello")


# Generated at 2022-06-13 19:11:18.924977
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(1)


# Generated at 2022-06-13 19:11:21.160368
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(1.5)
    assert Exclude.ALWAYS('a')


# Generated at 2022-06-13 19:11:25.938112
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert(Exclude.NEVER("") == False)
    assert(Exclude.NEVER(" ") == False)
    assert(Exclude.NEVER("1000") == False)
    assert(Exclude.NEVER("     ") == False)
    assert(Exclude.NEVER("False") == False)
    assert(Exclude.NEVER("'False'") == False)
    assert(Exclude.NEVER("True") == False)
    assert(Exclude.NEVER("'True'") == False)
    assert(Exclude.NEVER("'true'") == False)
    assert(Exclude.NEVER("'false'") == False)
    assert(Exclude.NEVER("!@##$%^&*()_") == False)

# Generated at 2022-06-13 19:11:27.479711
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    config(exclude=Exclude.NEVER)


# Generated at 2022-06-13 19:11:31.003540
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(100) == True
    assert Exclude.ALWAYS("hello") == True
    assert Exclude.ALWAYS("") == True
    assert Exclude.ALWAYS([1, 2, 3]) == True
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:11:31.835049
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0) == True

# Generated at 2022-06-13 19:11:38.049037
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1) == True
    assert Exclude.ALWAYS(0) == True
    assert Exclude.ALWAYS(True) == True
    assert Exclude.ALWAYS(False) == True
    assert Exclude.ALWAYS(3.1415) == True
    assert Exclude.ALWAYS("hello") == True


# Generated at 2022-06-13 19:11:41.443234
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS({})
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS(())
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS(set())
    assert Exclude.ALWAYS('string')
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)


# Generated at 2022-06-13 19:11:47.989126
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
  global Exclude
  assert Exclude.NEVER(False) == False
  assert Exclude.NEVER(True) == False
  assert Exclude.NEVER('false') == False
  assert Exclude.NEVER('true') == False
  assert Exclude.NEVER(0) == False
  assert Exclude.NEVER(1) == False
  assert Exclude.NEVER('') == False
  assert Exclude.NEVER('a') == False
  assert Exclude.NEVER(['a', 'b']) == False
  assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:11:49.542734
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    never = Exclude.NEVER
    assert never(None) is True  # True is expected

# Generated at 2022-06-13 19:11:51.317369
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test_string") == False

# Generated at 2022-06-13 19:11:52.258811
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(3) == False

# Generated at 2022-06-13 19:11:53.860705
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("a")



# Generated at 2022-06-13 19:12:02.535681
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    constant=Exclude.NEVER
    assert constant("A")==False
    assert constant("b")==False
    assert constant(1)==False
    assert constant(0.1)==False
    assert constant(True)==False
    assert constant(False)==False
    assert constant(None)==False
    assert constant([1, 2, 3])==False
    assert constant(["A", "B", "C"])==False
    assert constant({"A": 1, "B": 2, "C": 3})==False
    assert constant({"A", "B", "C"})==False
    assert constant((1, 2, 3))==False
    assert constant((False, False, True))==False
    assert constant({"A": 1})==False
    assert constant({"A"})==False

# Generated at 2022-06-13 19:12:03.534870
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER('str') == False


# Generated at 2022-06-13 19:12:06.416858
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1)
    assert Exclude.NEVER(2)
    assert Exclude.NEVER(3)

# Generated at 2022-06-13 19:12:15.846692
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
	assert Exclude.NEVER('example') == False

if __name__ == '__main__':
	test_Exclude_NEVER()

# Generated at 2022-06-13 19:12:21.498354
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS([]) == True
    assert Exclude.ALWAYS(["a"]) == True
    assert Exclude.ALWAYS([1,2,3]) == True
    assert Exclude.ALWAYS({"k": "v", "k1":"v1"}) == True
    assert Exclude.ALWAYS([(1,2), (3,4)]) == True


# Generated at 2022-06-13 19:12:22.986924
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("foo") == True

# Generated at 2022-06-13 19:12:24.403928
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    value = 10
    assert Exclude.ALWAYS(value)


# Generated at 2022-06-13 19:12:26.124878
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)


# Generated at 2022-06-13 19:12:35.264046
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(0)
    assert Exclude.ALWAYS(True)
    assert Exclude.ALWAYS(False)
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(None)
    assert Exclude.ALWAYS(3.14)
    assert Exclude.ALWAYS(1/2)
    assert Exclude.ALWAYS('')
    assert Exclude.ALWAYS('any string')
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS(['x', 'y', 'z'])
    assert Exclude.ALWAYS(())
    assert Exclude.ALWAYS((1, 2, 3))
    assert Exclude.ALWAYS(('x', 'y', 'z'))
    assert Exclude.ALWAYS

# Generated at 2022-06-13 19:12:37.194110
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(2) == False


# Generated at 2022-06-13 19:12:38.759608
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
   assert Exclude.NEVER('asdf') == False


# Generated at 2022-06-13 19:12:40.458659
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test")


# Generated at 2022-06-13 19:12:42.211689
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("test") is True


# Generated at 2022-06-13 19:13:17.639212
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    action_NEVER = Exclude.NEVER
    assert action_NEVER('always') == False
    assert action_NEVER('never') == False
    assert action_NEVER('condition') == False

# Generated at 2022-06-13 19:13:19.638833
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True


# Generated at 2022-06-13 19:13:23.615638
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("yes") is True
    assert Exclude.ALWAYS("no") is True
    assert Exclude.ALWAYS("") is True


# Generated at 2022-06-13 19:13:27.346047
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    ex = Exclude.ALWAYS
    assert ex(1) == True
    assert ex(0.23) == True
    assert ex('') == True
    assert ex(False) == True


# Generated at 2022-06-13 19:13:28.832725
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None)

# Generated at 2022-06-13 19:13:31.207065
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('test') == True


# Generated at 2022-06-13 19:13:32.714998
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS("")

# Generated at 2022-06-13 19:13:42.330269
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # test if function lambda _: True is returned
    assert Exclude.NEVER is not None
    assert Exclude.NEVER.__name__ == '<lambda>'
    assert Exclude.NEVER.__qualname__ == '<lambda>'
    assert Exclude.NEVER.__annotations__ == {}
    assert Exclude.NEVER.__defaults__ is None
    assert Exclude.NEVER.__kwdefaults__ is None
    assert Exclude.NEVER.__code__.co_argcount == 1
    assert Exclude.NEVER.__code__.co_consts == (False,)
    assert Exclude.NEVER.__code__.co_varnames == (_,)
    assert Exclude.NEVER.__code__.co_cellvars == ()

# Generated at 2022-06-13 19:13:43.352561
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("abc")


# Generated at 2022-06-13 19:13:44.687438
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    foo = Exclude.NEVER("hello")
    assert foo is False

# Generated at 2022-06-13 19:14:22.837800
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    a = Exclude.NEVER('I am never True')
    
    assert a == False

# Generated at 2022-06-13 19:14:24.590303
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(True) == False
    assert Exclude.NEVER(False) == False
    assert Exclude.NEVER(0) == False
    assert Exclude.NEVER(0.) == False


# Generated at 2022-06-13 19:14:26.842733
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(10)
    assert Exclude.ALWAYS('adad')
    assert Exclude.ALWAYS([])
    assert Exclude.ALWAYS(())
    assert Exclude.ALWAYS({})

# Generated at 2022-06-13 19:14:27.603977
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) == True

# Generated at 2022-06-13 19:14:28.580729
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test") == False

# Generated at 2022-06-13 19:14:29.547042
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    class TestClass:
        pass
    assert Exclude.NEVER(TestClass())

# Generated at 2022-06-13 19:14:30.531410
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False


# Generated at 2022-06-13 19:14:31.218942
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False

# Generated at 2022-06-13 19:14:32.327206
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER("test") == False


# Generated at 2022-06-13 19:14:38.269311
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    from dataclasses import dataclass, field
    from dataclasses_json import dataclass_json, config

    @dataclass_json
    @dataclass
    class Terrain:
        name: str
        impassable: bool = field(default=True)
        move_cost: int = field(default=1)
        attack_bonus: int = field(default=0)
        defense_bonus: int = field(default=0)
        heal_bonus: int = field(default=0)
        graphic: str = field(default="·")
        color: list = field(
            default_factory=lambda: [255, 255, 255])  # white

        @config(exclude=Exclude.ALWAYS)
        def color(self):
            return self.color


# Generated at 2022-06-13 19:16:11.106051
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # GIVEN
    param1 = 'test1'
    param2 = 'test2'
    # WHEN
    assert Exclude.ALWAYS(param1)
    assert Exclude.ALWAYS(param2)
    # THEN
    assert True


# Generated at 2022-06-13 19:16:12.908262
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # arrange
    test_input = 'A'
    test_output = False
    # act
    result = Exclude.NEVER(test_input)
    # assert
    assert result == test_output


# Generated at 2022-06-13 19:16:13.846104
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(None) == False


# Generated at 2022-06-13 19:16:16.170907
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(1)
    assert Exclude.ALWAYS(('asd', 1, 'gfg'))
    assert Exclude.ALWAYS([1, 2, 3])
    assert Exclude.ALWAYS(23.3)
    assert Exclude.ALWAYS('c')
    assert Exclude.ALWAYS(True)


# Generated at 2022-06-13 19:16:19.156471
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    # Test that NEVER returns a boolean
    assert(isinstance(Exclude.NEVER('a'), bool))

# Generated at 2022-06-13 19:16:22.358883
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    # Given
    obj = Exclude.ALWAYS

    # When
    value = obj(None)

    # Then
    assert value

# Generated at 2022-06-13 19:16:23.823366
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert Exclude.NEVER(1) == False;


# Generated at 2022-06-13 19:16:24.996561
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS(None) 


# Generated at 2022-06-13 19:16:25.785813
# Unit test for method NEVER of class Exclude
def test_Exclude_NEVER():
    assert not Exclude.NEVER(1)

# Generated at 2022-06-13 19:16:26.837086
# Unit test for method ALWAYS of class Exclude
def test_Exclude_ALWAYS():
    assert Exclude.ALWAYS('_') == True
