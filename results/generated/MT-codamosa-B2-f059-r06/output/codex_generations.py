

# Generated at 2026-10-24 19:14:39.787770
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:14:42.206434
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:14:44.623282
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:14:45.978228
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:14:47.361731
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:14:48.798268
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:14:50.231139
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:14:54.840110
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:14:56.272624
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:14:57.656106
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:14:59.038312
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:00.471829
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:01.871988
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:03.339326
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:05.760069
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:08.178251
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:10.594262
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:13.013099
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:15.427958
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:17.846261
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:20.263313
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:22.678047
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:25.095475
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:15:42.228153
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:43.693258
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:45.118660
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:46.552040
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:47.917861
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:49.316234
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:50.749631
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:52.183954
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:53.552645
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:15:54.925018
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:16:27.330029
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:29.776814
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:32.194877
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:34.611542
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:37.027485
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:39.444308
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:41.861319
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:44.277619
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:46.693424
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:49.113290
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:51.531443
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:53.947105
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:56.363366
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:16:58.777842
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:01.195710
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:03.612555
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:06.029865
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:08.446634
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:10.862399
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:13.282483
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:15.694579
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:18.111901
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:20.527370
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:22.944366
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:25.361157
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:27.933437
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 19:17:29.288229
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:17:41.406041
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:17:42.879326
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:17:44.237595
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:17:45.648704
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:17:48.067008
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:50.484859
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:52.903414
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:55.321036
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:17:57.889870
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:00.305548
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:02.724781
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:05.142132
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:07.557416
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:09.976830
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:12.394873
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:14.811622
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:17.227344
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:19.643354
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:22.061164
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:24.482169
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:26.902056
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:29.320727
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:46.374226
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:48.791533
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:51.206683
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:53.623723
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:56.045332
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:18:58.461460
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:00.890900
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:03.324442
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:05.751644
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:08.195044
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:10.625509
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:13.044827
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:15.457756
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:19:18.070711
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 19:19:19.498785
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:19:20.891502
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:19:22.309352
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:19:23.743516
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:19:25.176932
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:20:08.617941
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:11.034586
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:13.457484
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:15.873066
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:18.289420
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:20.707225
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:23.123913
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:25.581790
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:20:28.297649
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 19:20:29.654213
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:20:31.032658
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:20:32.394529
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:20:33.750956
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:20:35.220665
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:20:36.658105
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:20:38.087581
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:21:55.673254
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:21:58.090233
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:00.513111
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:02.926506
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:05.342223
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:07.759461
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:10.174219
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:12.595139
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:15.175231
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:17.589371
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:20.004193
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:22.420045
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:24.844859
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:27.261059
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:29.679714
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:32.102009
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:34.523111
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:36.938177
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:39.355003
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:41.771905
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:44.190790
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:22:46.831528
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(17) == 17
    assert module_0.largest_prime_factor(28) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(13195) == 29
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:22:48.249538
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1

# Generated at 2026-10-24 19:22:49.604544
# Unit test for function largest_prime_factor
def test_largest_prime_factor():
    # prime numbers return themselves
    assert module_0.largest_prime_factor(2) == 2
    assert module_0.largest_prime_factor(3) == 3
    assert module_0.largest_prime_factor(17) == 17

    # small composites
    assert module_0.largest_prime_factor(4) == 2
    assert module_0.largest_prime_factor(6) == 3
    assert module_0.largest_prime_factor(8) == 2
    assert module_0.largest_prime_factor(9) == 3
    assert module_0.largest_prime_factor(10) == 5
    assert module_0.largest_prime_factor(12) == 3
    assert module_0.largest_prime_factor(15) == 5
    assert module_0.largest_prime_factor(21) == 7
    assert module_0.largest_prime_factor(49) == 7
    assert module_0.largest_prime_factor(100) == 5

    # prime powers return the base prime
    assert module_0.largest_prime_factor(27) == 3

    # known Project Euler case: 13195 = 5 * 7 * 13 * 29
    assert module_0.largest_prime_factor(13195) == 29

    # edge case per current implementation
    assert module_0.largest_prime_factor(1) == 1