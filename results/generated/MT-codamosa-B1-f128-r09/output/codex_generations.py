

# Generated at 2026-10-24 21:50:32.291831
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:35.408144
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:37.928843
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:40.345862
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:42.764546
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:45.182239
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:47.599356
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:50.018988
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:52.432756
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:54.853990
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:57.271347
# Unit test for function prod_signs

# Generated at 2026-10-24 21:50:59.690228
# Unit test for function prod_signs

# Generated at 2026-10-24 21:51:06.222470
# Unit test for function prod_signs
def test_prod_signs():
    assert module_0.prod_signs([]) is None
    assert module_0.prod_signs([1, 2, 3, 4]) == 10
    assert module_0.prod_signs([1, -2, 3, 4]) == -10
    assert module_0.prod_signs([-1, -2, 3, 4]) == 10
    assert module_0.prod_signs([-1, -2, -3]) == -6
    assert module_0.prod_signs([0, 1, -2, 3]) == 0
    assert module_0.prod_signs([5]) == 5
    assert module_0.prod_signs([-5]) == -5