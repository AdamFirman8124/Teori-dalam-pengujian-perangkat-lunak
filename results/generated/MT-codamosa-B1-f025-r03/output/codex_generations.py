

# Generated at 2026-10-24 06:41:38.907991
# Unit test for function factorize

# Generated at 2026-10-24 06:41:41.319670
# Unit test for function factorize

# Generated at 2026-10-24 06:41:43.733332
# Unit test for function factorize

# Generated at 2026-10-24 06:41:46.146714
# Unit test for function factorize

# Generated at 2026-10-24 06:41:48.561130
# Unit test for function factorize

# Generated at 2026-10-24 06:41:50.976723
# Unit test for function factorize

# Generated at 2026-10-24 06:41:53.392809
# Unit test for function factorize

# Generated at 2026-10-24 06:41:55.807554
# Unit test for function factorize

# Generated at 2026-10-24 06:41:58.221407
# Unit test for function factorize

# Generated at 2026-10-24 06:42:00.635599
# Unit test for function factorize

# Generated at 2026-10-24 06:42:03.053491
# Unit test for function factorize

# Generated at 2026-10-24 06:42:05.469539
# Unit test for function factorize

# Generated at 2026-10-24 06:42:07.885256
# Unit test for function factorize

# Generated at 2026-10-24 06:42:10.300119
# Unit test for function factorize

# Generated at 2026-10-24 06:42:12.715300
# Unit test for function factorize

# Generated at 2026-10-24 06:42:15.128960
# Unit test for function factorize

# Generated at 2026-10-24 06:42:17.545691
# Unit test for function factorize

# Generated at 2026-10-24 06:42:19.965781
# Unit test for function factorize

# Generated at 2026-10-24 06:42:22.380472
# Unit test for function factorize

# Generated at 2026-10-24 06:42:24.796579
# Unit test for function factorize

# Generated at 2026-10-24 06:42:27.214332
# Unit test for function factorize

# Generated at 2026-10-24 06:42:29.632219
# Unit test for function factorize

# Generated at 2026-10-24 06:42:32.047817
# Unit test for function factorize

# Generated at 2026-10-24 06:42:34.465717
# Unit test for function factorize

# Generated at 2026-10-24 06:42:36.886571
# Unit test for function factorize

# Generated at 2026-10-24 06:42:39.296973
# Unit test for function factorize

# Generated at 2026-10-24 06:42:48.348813
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 06:43:05.079493
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:06.398706
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:07.712066
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:09.025922
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:11.449359
# Unit test for function factorize

# Generated at 2026-10-24 06:43:13.865002
# Unit test for function factorize

# Generated at 2026-10-24 06:43:16.283971
# Unit test for function factorize

# Generated at 2026-10-24 06:43:18.700522
# Unit test for function factorize

# Generated at 2026-10-24 06:43:21.118327
# Unit test for function factorize

# Generated at 2026-10-24 06:43:23.671223
# Unit test for function factorize

# Generated at 2026-10-24 06:43:26.083642
# Unit test for function factorize

# Generated at 2026-10-24 06:43:28.500980
# Unit test for function factorize

# Generated at 2026-10-24 06:43:30.920332
# Unit test for function factorize

# Generated at 2026-10-24 06:43:33.332435
# Unit test for function factorize

# Generated at 2026-10-24 06:43:35.746966
# Unit test for function factorize

# Generated at 2026-10-24 06:43:38.163133
# Unit test for function factorize

# Generated at 2026-10-24 06:43:40.575103
# Unit test for function factorize

# Generated at 2026-10-24 06:43:41.941987
# Unit test for function factorize
def test_factorize():assert module_0.factorize(1) == []

# Generated at 2026-10-24 06:43:43.322692
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:44.624909
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:45.935700
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:47.310362
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:48.741674
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:50.071826
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:51.408213
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:52.722366
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:54.023276
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:55.356643
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:56.655662
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:57.964785
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:43:59.274152
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:00.586218
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:01.923884
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:03.236534
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:04.543621
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:05.857274
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:07.170500
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:08.505034
# Unit test for function factorize
def test_factorize():
    def check(n, expected):
        got = module_0.factorize(n)
        assert got == expected, f"module_0.factorize({n}) -> {got}, expected {expected}"
        prod = 1
        for p in got:
            prod *= p
        assert prod == n, f"product of {got} is {prod}, not {n}"

    # primes
    check(2, [2])
    check(3, [3])
    check(13, [13])
    check(97, [97])
    check(999983, [999983])

    # composites, with multiplicity
    check(4, [2, 2])
    check(6, [2, 3])
    check(12, [2, 2, 3])
    check(49, [7, 7])
    check(100, [2, 2, 5, 5])
    check(360, [2, 2, 2, 3, 3, 5])
    check(2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13])
    check(2 ** 10, [2] * 10)
    check(999979 * 999983, [999979, 999983])

    # 1 has no prime

# Generated at 2026-10-24 06:44:11.031725
# Unit test for function factorize

# Generated at 2026-10-24 06:44:13.448870
# Unit test for function factorize

# Generated at 2026-10-24 06:44:15.866035
# Unit test for function factorize

# Generated at 2026-10-24 06:44:18.285330
# Unit test for function factorize

# Generated at 2026-10-24 06:44:20.700403
# Unit test for function factorize

# Generated at 2026-10-24 06:44:23.198419
# Unit test for function factorize

# Generated at 2026-10-24 06:44:25.613631
# Unit test for function factorize

# Generated at 2026-10-24 06:44:28.190978
# Unit test for function factorize

# Generated at 2026-10-24 06:44:30.609399
# Unit test for function factorize

# Generated at 2026-10-24 06:44:33.024001
# Unit test for function factorize

# Generated at 2026-10-24 06:44:35.438833
# Unit test for function factorize

# Generated at 2026-10-24 06:44:37.857359
# Unit test for function factorize

# Generated at 2026-10-24 06:44:40.276359
# Unit test for function factorize

# Generated at 2026-10-24 06:44:42.692877
# Unit test for function factorize

# Generated at 2026-10-24 06:44:45.103145
# Unit test for function factorize

# Generated at 2026-10-24 06:44:47.517366
# Unit test for function factorize

# Generated at 2026-10-24 06:44:49.934992
# Unit test for function factorize

# Generated at 2026-10-24 06:44:52.345543
# Unit test for function factorize

# Generated at 2026-10-24 06:44:54.761253
# Unit test for function factorize

# Generated at 2026-10-24 06:44:57.181050
# Unit test for function factorize

# Generated at 2026-10-24 06:44:59.598682
# Unit test for function factorize