

# Generated at 2024-05-30 23:27:23.123384
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:26.152233
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:28.525239
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    expected_subclasses = {B, C, D, E}
    assert get_all_subclasses(A) == expected_subclasses

    expected_subclasses_B = {D}
    assert get_all_subclasses(B) == expected_subclasses_B

    expected_subclasses_C = {E}
    assert get_all_subclasses(C) == expected_subclasses_C

    assert get_all_subclasses(D) == set()
    assert get_all_subclasses(E) == set()

# Generated at 2024-05-30 23:27:31.090881
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(B)
    expected = {C}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(C)
    expected = set()
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(D)
    expected = set()
    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:27:32.509104
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:27:34.087650
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:36.439955
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:37.709063
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:27:40.697303
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:42.533324
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:27:49.253140
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:27:52.449180
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:55.409065
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:56.842771
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:27:58.376101
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:28:02.289848
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:04.014694
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:28:07.784097
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(B)
    expected = {D}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(C)
    expected = {E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(D)
    expected = set()
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(E)
    expected = set()

# Generated at 2024-05-30 23:28:09.270804
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:28:10.977036
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:23.084479
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(B)
    expected = {D}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(C)
    expected = {E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(D)
    expected = set()
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(E)
    expected = set()

# Generated at 2024-05-30 23:28:25.681920
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:28.983141
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:31.254179
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:34.269008
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:28:36.092321
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:38.793741
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:40.365288
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:28:43.789092
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:28:45.289713
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:28:55.703423
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:28:57.711341
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:01.116059
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(B)
    expected = {D}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(C)
    expected = {E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(D)
    expected = set()
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(E)
    expected = set()

# Generated at 2024-05-30 23:29:04.525382
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:29:06.235488
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:08.214951
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:09.855802
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:11.265947
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:14.397264
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(B)
    expected = {D}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(C)
    expected = {E}
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(D)
    expected = set()
    assert result == expected, f"Expected {expected}, but got {result}"

    result = get_all_subclasses(E)
    expected = set()

# Generated at 2024-05-30 23:29:15.896959
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:32.750030
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:34.150465
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:35.971747
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:38.065236
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:41.618654
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:29:45.314744
# Unit test for function get_all_subclasses

# Generated at 2024-05-30 23:29:48.294406
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:54.203769
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    subclasses_of_a = get_all_subclasses(A)
    assert B in subclasses_of_a
    assert C in subclasses_of_a
    assert D in subclasses_of_a
    assert E in subclasses_of_a
    assert len(subclasses_of_a) == 4

    subclasses_of_b = get_all_subclasses(B)
    assert D in subclasses_of_b
    assert len(subclasses_of_b) == 1

    subclasses_of_c = get_all_subclasses(C)
    assert E in subclasses_of_c
    assert len(subclasses_of_c) == 1

    subclasses_of_d = get_all_subclasses(D)
    assert len(subclasses_of_d) == 0

    subclasses_of_e = get_all_subclasses(E)

# Generated at 2024-05-30 23:29:55.941381
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"

# Generated at 2024-05-30 23:29:58.372677
# Unit test for function get_all_subclasses
def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    result = get_all_subclasses(A)
    expected = {B, C, D, E}

    assert result == expected, f"Expected {expected}, but got {result}"