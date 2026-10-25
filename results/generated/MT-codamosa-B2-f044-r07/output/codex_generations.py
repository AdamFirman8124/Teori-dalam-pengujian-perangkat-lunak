

# Generated at 2026-10-24 11:40:17.707251
# Unit test for function change_base

# Generated at 2026-10-24 11:40:20.124853
# Unit test for function change_base

# Generated at 2026-10-24 11:40:22.544114
# Unit test for function change_base

# Generated at 2026-10-24 11:40:24.965266
# Unit test for function change_base

# Generated at 2026-10-24 11:40:27.389321
# Unit test for function change_base

# Generated at 2026-10-24 11:40:29.806302
# Unit test for function change_base

# Generated at 2026-10-24 11:40:32.225332
# Unit test for function change_base

# Generated at 2026-10-24 11:40:42.569973
# Unit test for function change_base
def test_change_base():assert module_0.change_base(8, 2) == "1000"

# Generated at 2026-10-24 11:40:59.671546
# Unit test for function change_base
def test_change_base():
    # base 10
    assert module_0.change_base(1, 10) == "1"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(123, 10) == "123"

    # binary
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(2, 2) == "10"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(255, 2) == "11111111"

    # octal / other bases
    assert module_0.change_base(8, 8) == "10"
    assert module_0.change_base(64, 8) == "100"
    assert module_0.change_base(100, 3) == "10201"
    assert module_0.change_base(5, 5) == "10"

# Generated at 2026-10-24 11:41:02.201804
# Unit test for function change_base

# Generated at 2026-10-24 11:41:04.750586
# Unit test for function change_base

# Generated at 2026-10-24 11:41:07.322634
# Unit test for function change_base