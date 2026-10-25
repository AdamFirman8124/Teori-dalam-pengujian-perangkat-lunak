

# Generated at 2026-10-24 15:44:10.322844
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:44:13.290717
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:44:18.739260
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:44:21.790044
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:44:27.458002
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:44:36.023418
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:44:39.335276
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:44:49.745608
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:45:02.343847
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:45:13.092088
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:45:27.224776
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:45:36.833974
# Unit test for function factorize

# Generated at 2026-10-24 15:45:57.329250
# Unit test for function factorize
def test_factorize():assert module_0.factorize(12) == [2, 2, 3]

# Generated at 2026-10-24 15:46:00.503975
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:46:03.679040
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:46:06.750868
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:46:18.424406
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:46:31.349001
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:46:54.575449
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:47:02.458645
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:47:05.425355
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:47:22.733548
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:47:25.699091
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:47:28.773321
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:47:32.050486
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]

# Generated at 2026-10-24 15:47:34.917479
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(17) == [17]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(999) == [3, 3, 3, 37]
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(104729) == [104729]
    for n, expected in [(1, []), (2, [2]), (4, [2, 2]), (12, [2, 2, 3]), (100, [2, 2, 5, 5])]:
        result = module_0.factorize(n)
        assert result == expected
        assert result == sorted(result)
    for n in [2, 3, 4, 6, 12, 49, 100, 360, 999, 1024, 30030]:
        result = module_0.factorize(n)
        p = 1
        for x in result:
            p *= x
        assert p == n
        for x in result:
            assert module_0.factorize(x) == [x]