

# Generated at 2024-03-18 06:32:54.180522
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:33:01.096615
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:33:09.222158
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:33:12.278493
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test default new name
    mod1 = MovedModule("example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test specified new name
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"

# Generated at 2024-03-18 06:33:17.564757
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr
    attr = MovedAttribute("example", "old_module", new_attr="new_attribute")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attribute"

    # Test specified old_attr and default new_attr
    attr = MovedAttribute("example", "old_module", old_attr="old_attribute")
    assert attr.name == "example"
    assert attr.new_mod == "example"


# Generated at 2024-03-18 06:33:23.439822
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:33:29.095171
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    ma1 = MovedAttribute("example", "old_module")
    assert ma1.name == "example"
    assert ma1.new_mod == "example"
    assert ma1.new_attr == "example"

    # Test specified new_mod, default new_attr
    ma2 = MovedAttribute("example", "old_module", "new_module")
    assert ma2.name == "example"
    assert ma2.new_mod == "new_module"
    assert ma2.new_attr == "example"

    # Test specified new_attr, default new_mod
    ma3 = MovedAttribute("example", "old_module", None, "old_attr")
    assert ma3.name == "example"
    assert ma3.new_mod == "example"
    assert ma3.new_attr == "old_attr"

    # Test specified new_mod and new_attr

# Generated at 2024-03-18 06:33:34.676996
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test with only the name provided, should default new to name
    move1 = MovedModule("example")
    assert move1.name == "example"
    assert move1.new == "example"

    # Test with both name and new provided
    move2 = MovedModule("example", "old_example", "new_example")
    assert move2.name == "example"
    assert move2.new == "new_example"

    # Test with name and old provided, but new is None
    move3 = MovedModule("example", "old_example")
    assert move3.name == "example"
    assert move3.new == "example"


# Generated at 2024-03-18 06:33:38.743123
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:33:41.661322
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:33:47.655798
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:33:55.455387
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "old_attr"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")
    assert attr.name == "example"


# Generated at 2024-03-18 06:34:02.484020
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "old_attr"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:34:08.481833
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr
    attr = MovedAttribute("example", "old_module", new_attr="new_attribute")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attribute"

    # Test specified old_attr and default new_attr
    attr = MovedAttribute("example", "old_module", old_attr="old_attribute")
    assert attr.name == "example"
    assert attr.new_mod == "example"


# Generated at 2024-03-18 06:34:13.834939
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr and default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "old_attr"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")
    assert attr.name == "example"


# Generated at 2024-03-18 06:34:17.347476
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test default new name
    mod1 = MovedModule("example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test specified new name
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"

# Generated at 2024-03-18 06:34:23.020461
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test with only the name provided, should default new to name
    move1 = MovedModule("example")
    assert move1.name == "example"
    assert move1.new == "example"

    # Test with both name and new provided
    move2 = MovedModule("example", "old_example", "new_example")
    assert move2.name == "example"
    assert move2.new == "new_example"

    # Test with name and old provided, but new is None
    move3 = MovedModule("example", "old_example")
    assert move3.name == "example"
    assert move3.new == "example"


# Generated at 2024-03-18 06:34:29.244633
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "new_attr"

    # Test default new_attr with specified old_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr")
    assert attr.name == "example"


# Generated at 2024-03-18 06:34:34.935967
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attr"

    # Test all specified
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:34:37.627758
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:34:45.026843
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test the default new name assignment
    mod1 = MovedModule("example", "old_example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test the explicit new name assignment
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"


# Generated at 2024-03-18 06:34:54.199714
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:34:59.620918
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:35:02.401746
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test the default new name assignment
    mod1 = MovedModule("example", "old_example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test the explicit new name assignment
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"


# Generated at 2024-03-18 06:35:08.946746
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test with only the name provided, should default new to name
    move1 = MovedModule("example")
    assert move1.name == "example"
    assert move1.new == "example"

    # Test with both name and new provided
    move2 = MovedModule("example", "old_example", "new_example")
    assert move2.name == "example"
    assert move2.new == "new_example"

    # Test with name and old provided, but new is None
    move3 = MovedModule("example", "old_example")
    assert move3.name == "example"
    assert move3.new == "example"


# Generated at 2024-03-18 06:35:11.795356
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test default new name
    mod1 = MovedModule("example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test specified new name
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"

# Generated at 2024-03-18 06:35:22.535214
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test with only the name provided, should default new to name
    move1 = MovedModule("example")
    assert move1.name == "example"
    assert move1.new == "example"

    # Test with both name and new provided
    move2 = MovedModule("example", "old_example", "new_example")
    assert move2.name == "example"
    assert move2.new == "new_example"

    # Test with name and old provided, but new is None
    move3 = MovedModule("example", "old_example")
    assert move3.name == "example"
    assert move3.new == "example"


# Generated at 2024-03-18 06:35:28.834781
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attr"

    # Test all specified
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:35:32.276429
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:35:39.122337
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_attr and new_mod
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "example"

    # Test specified new_attr and default new_mod
    attr = MovedAttribute("example", "old_module", None, None, "new_attribute")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "new_attribute"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "new_module"
    assert attr

# Generated at 2024-03-18 06:35:58.063278
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "old_attr"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:36:01.878504
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:36:05.106921
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:36:08.218549
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:36:14.670685
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:36:18.554812
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test with only the name provided
    mod1 = MovedModule("example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test with both name and old module provided
    mod2 = MovedModule("example", "old_example")
    assert mod2.name == "example"
    assert mod2.new == "example"

    # Test with name, old module, and new module provided
    mod3 = MovedModule("example", "old_example", "new_example")
    assert mod3.name == "example"
    assert mod3.new == "new_example"


# Generated at 2024-03-18 06:36:28.156051
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attr"

    # Test all specified
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:36:31.602087
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test default new name
    mod1 = MovedModule("example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test specified new name
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"

# Generated at 2024-03-18 06:36:34.729072
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test the default new name is the same as the old name
    mod = MovedModule("old_name")
    assert mod.name == "old_name"
    assert mod.new == "old_name"

    # Test the specified new name
    mod = MovedModule("old_name", "old_name", "new_name")
    assert mod.name == "old_name"
    assert mod.new == "new_name"


# Generated at 2024-03-18 06:36:44.234311
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    ma1 = MovedAttribute("example", "old_module")
    assert ma1.name == "example"
    assert ma1.new_mod == "example"
    assert ma1.new_attr == "example"

    # Test specified new_mod, default new_attr
    ma2 = MovedAttribute("example", "old_module", "new_module")
    assert ma2.name == "example"
    assert ma2.new_mod == "new_module"
    assert ma2.new_attr == "example"

    # Test specified new_attr, default new_mod
    ma3 = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert ma3.name == "example"
    assert ma3.new_mod == "example"
    assert ma3.new_attr == "new_attr"

    # Test all specified

# Generated at 2024-03-18 06:37:04.270802
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:37:11.534250
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "new_attr"

    # Test default new_mod with specified old_attr and new_attr

# Generated at 2024-03-18 06:37:17.769276
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_attr and new_mod
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "example"

    # Test specified new_attr and default new_mod
    attr = MovedAttribute("example", "old_module", None, None, "new_attribute")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "new_attribute"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "new_module"
    assert attr

# Generated at 2024-03-18 06:37:24.911839
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_attr and new_mod
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "example"

    # Test specified new_attr and default new_mod
    attr = MovedAttribute("example", "old_module", None, None, "new_attribute")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "new_attribute"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "new_module"
    assert attr

# Generated at 2024-03-18 06:37:27.795115
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:37:32.112513
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:37:37.459762
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test the default new name assignment
    mod1 = MovedModule("example", "old_example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test the explicit new name assignment
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"


# Generated at 2024-03-18 06:37:40.805866
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:37:48.559525
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:37:51.500527
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test the default new name assignment
    mod1 = MovedModule("example", "old_example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test the explicit new name assignment
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"


# Generated at 2024-03-18 06:38:34.389288
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:38:37.919737
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test the default new name is the same as the old name
    mod = MovedModule("example", "old_example")
    assert mod.name == "example"
    assert mod.new == "example"

    # Test the new name is set correctly when provided
    mod = MovedModule("example", "old_example", "new_example")
    assert mod.name == "example"
    assert mod.new == "new_example"


# Generated at 2024-03-18 06:38:42.421094
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:38:46.885738
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:38:50.247825
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:38:53.821726
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test default new module name
    move1 = MovedModule("example", "old_example")
    assert move1.name == "example"
    assert move1.new == "example"

    # Test specified new module name
    move2 = MovedModule("example", "old_example", "new_example")
    assert move2.name == "example"
    assert move2.new == "new_example"


# Generated at 2024-03-18 06:38:57.024917
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test default new name
    mod1 = MovedModule("example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test specified new name
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"

# Generated at 2024-03-18 06:39:06.771693
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "new_attr"

    # Test default new_mod with specified old_attr and new_attr

# Generated at 2024-03-18 06:39:12.412862
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attr"

    # Test all specified
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:39:18.090527
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attr"

    # Test all specified
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:40:48.015534
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_attr and new_mod
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "example"

    # Test specified new_attr and default new_mod
    attr = MovedAttribute("example", "old_module", None, None, "new_attribute")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "example"
    assert attr.old_attr is None
    assert attr.new_attr == "new_attribute"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.old_mod == "old_module"
    assert attr.new_mod == "new_module"
    assert attr

# Generated at 2024-03-18 06:40:51.768296
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:40:59.000741
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod and default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "new_attr"

    # Test default new_mod with specified old_attr and new_attr

# Generated at 2024-03-18 06:41:10.701260
# Unit test for constructor of class SixMovesTransformer
def test_SixMovesTransformer():    transformer = SixMovesTransformer()

# Generated at 2024-03-18 06:41:19.677611
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "old_attr"

    # Test specified new_mod and new_attr
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:41:29.981777
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attr"

    # Test all specified
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:41:33.611074
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test default new module name
    move1 = MovedModule("example", "old_example")
    assert move1.name == "example"
    assert move1.new == "example"

    # Test specified new module name
    move2 = MovedModule("example", "old_example", "new_example")
    assert move2.name == "example"
    assert move2.new == "new_example"


# Generated at 2024-03-18 06:41:36.580097
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test the default new name assignment
    mod1 = MovedModule("example", "old_example")
    assert mod1.name == "example"
    assert mod1.new == "example"

    # Test the explicit new name assignment
    mod2 = MovedModule("example", "old_example", "new_example")
    assert mod2.name == "example"
    assert mod2.new == "new_example"


# Generated at 2024-03-18 06:41:43.905151
# Unit test for constructor of class MovedAttribute
def test_MovedAttribute():    # Test default new_mod and new_attr
    attr = MovedAttribute("example", "old_module")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "example"

    # Test specified new_mod, default new_attr
    attr = MovedAttribute("example", "old_module", "new_module")
    assert attr.name == "example"
    assert attr.new_mod == "new_module"
    assert attr.new_attr == "example"

    # Test specified new_attr, default new_mod
    attr = MovedAttribute("example", "old_module", None, "old_attr", "new_attr")
    assert attr.name == "example"
    assert attr.new_mod == "example"
    assert attr.new_attr == "new_attr"

    # Test all specified
    attr = MovedAttribute("example", "old_module", "new_module", "old_attr", "new_attr")

# Generated at 2024-03-18 06:41:48.754882
# Unit test for constructor of class MovedModule
def test_MovedModule():    # Test with new module name provided
    move_with_new = MovedModule("new_module", "old.module", "new.module")
    assert move_with_new.name == "new_module"
    assert move_with_new.new == "new.module"

    # Test without new module name provided (should default to the same as name)
    move_without_new = MovedModule("same_module", "old.module")
    assert move_without_new.name == "same_module"
    assert move_without_new.new == "same_module"
