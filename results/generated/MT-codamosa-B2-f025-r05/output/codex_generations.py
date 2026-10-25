

# Generated at 2026-10-24 13:11:14.108654
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:11:29.775533
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:11:50.052631
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

# Generated at 2026-10-24 13:12:35.927823
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:13:11.643537
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

# Generated at 2026-10-24 13:14:08.398684
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:14:12.799421
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

# Generated at 2026-10-24 13:14:56.522276
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

# Generated at 2026-10-24 13:15:42.399380
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

# Generated at 2026-10-24 13:15:45.162872
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

# Generated at 2026-10-24 13:15:47.793728
# Unit test for function factorize

# Generated at 2026-10-24 13:16:01.557722
# Unit test for function factorize
def test_factorize():assert module_0.factorize(12) == [2, 2, 3]

# Generated at 2026-10-24 13:16:04.925092
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

# Generated at 2026-10-24 13:16:23.434987
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:16:31.197630
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(13) == [13]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(100) == [2, 2, 5, 5]

# Generated at 2026-10-24 13:16:37.166617
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:16:40.151242
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:16:42.817303
# Unit test for function factorize

# Generated at 2026-10-24 13:16:45.357036
# Unit test for function factorize

# Generated at 2026-10-24 13:16:47.770111
# Unit test for function factorize

# Generated at 2026-10-24 13:16:50.698747
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:16:53.362970
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:16:56.227528
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:16:59.078409
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:17:02.168964
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:17:04.961260
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:17:07.804933
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

# Generated at 2026-10-24 13:17:29.075323
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:17:31.639598
# Unit test for function factorize

# Generated at 2026-10-24 13:17:34.209565
# Unit test for function factorize

# Generated at 2026-10-24 13:17:36.623509
# Unit test for function factorize

# Generated at 2026-10-24 13:17:39.036799
# Unit test for function factorize

# Generated at 2026-10-24 13:17:41.451266
# Unit test for function factorize

# Generated at 2026-10-24 13:17:43.866132
# Unit test for function factorize

# Generated at 2026-10-24 13:17:46.279192
# Unit test for function factorize

# Generated at 2026-10-24 13:17:48.900485
# Unit test for function factorize

# Generated at 2026-10-24 13:17:51.314490
# Unit test for function factorize

# Generated at 2026-10-24 13:17:53.728994
# Unit test for function factorize

# Generated at 2026-10-24 13:17:56.146846
# Unit test for function factorize

# Generated at 2026-10-24 13:17:58.561456
# Unit test for function factorize

# Generated at 2026-10-24 13:18:00.974056
# Unit test for function factorize

# Generated at 2026-10-24 13:18:03.389988
# Unit test for function factorize

# Generated at 2026-10-24 13:18:05.925617
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:18:21.119866
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:18:27.774619
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 13:18:30.541286
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(1) == []
    assert module_0.factorize(2) == [2]
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(5) == [5]
    assert module_0.factorize(6) == [2, 3]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(9) == [3, 3]
    assert module_0.factorize(10) == [2, 5]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(15) == [3, 5]
    assert module_0.factorize(16) == [2, 2, 2, 2]
    assert module_0.factorize(25) == [5, 5]
    assert module_0.factorize(27) == [3, 3, 3]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]
    assert module_0.factorize(100) == [2, 2, 5, 5]
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1024) == [2] * 10
    assert module_0.factorize(30030) == [2, 3, 5, 7, 11, 13]
    assert module_0.factorize(323) == [17, 19]
    assert module_0.factorize(7919) == [7919]
    assert module_0.factorize(104729) == [104729]
    assert module_0.factorize(999983) == [999983]

# Generated at 2026-10-24 13:18:33.402319
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

# Generated at 2026-10-24 13:18:35.826460
# Unit test for function factorize

# Generated at 2026-10-24 13:18:38.247807
# Unit test for function factorize

# Generated at 2026-10-24 13:18:40.662671
# Unit test for function factorize