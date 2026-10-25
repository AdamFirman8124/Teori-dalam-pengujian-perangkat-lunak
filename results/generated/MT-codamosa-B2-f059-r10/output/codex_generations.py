

# Generated at 2026-10-24 15:48:40.556057
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

# Generated at 2026-10-24 15:48:45.369324
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

# Generated at 2026-10-24 15:48:46.811231
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

# Generated at 2026-10-24 15:48:48.236105
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

# Generated at 2026-10-24 15:48:49.671420
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

# Generated at 2026-10-24 15:48:52.536863
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

# Generated at 2026-10-24 15:48:53.970269
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

# Generated at 2026-10-24 15:48:55.404146
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

# Generated at 2026-10-24 15:48:56.837673
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

# Generated at 2026-10-24 15:48:58.186340
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

# Generated at 2026-10-24 15:48:59.602222
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

# Generated at 2026-10-24 15:49:01.036117
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

# Generated at 2026-10-24 15:49:03.450660
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:05.862372
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:08.274850
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:10.687191
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:13.100000
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:15.512308
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:17.925209
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:20.484646
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:22.895975
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:49:34.464672
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

# Generated at 2026-10-24 15:49:36.262210
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

# Generated at 2026-10-24 15:49:52.749646
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

# Generated at 2026-10-24 15:49:55.616765
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

# Generated at 2026-10-24 15:49:56.996898
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

# Generated at 2026-10-24 15:49:58.379459
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

# Generated at 2026-10-24 15:49:59.815721
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

# Generated at 2026-10-24 15:50:01.246991
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

# Generated at 2026-10-24 15:50:02.680517
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

# Generated at 2026-10-24 15:50:04.039260
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

# Generated at 2026-10-24 15:50:16.661311
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

# Generated at 2026-10-24 15:50:19.329735
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:50:21.742534
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:50:24.155996
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:50:26.570843
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:50:38.213341
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 15:50:41.111770
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

# Generated at 2026-10-24 15:50:42.474077
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

# Generated at 2026-10-24 15:50:44.545707
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

# Generated at 2026-10-24 15:50:45.997772
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

# Generated at 2026-10-24 15:50:52.382319
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

# Generated at 2026-10-24 15:50:53.785423
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

# Generated at 2026-10-24 15:50:55.418237
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

# Generated at 2026-10-24 15:51:20.612557
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

# Generated at 2026-10-24 15:51:22.041037
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

# Generated at 2026-10-24 15:51:23.463888
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

# Generated at 2026-10-24 15:51:24.908199
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

# Generated at 2026-10-24 15:51:27.367405
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

# Generated at 2026-10-24 15:51:29.906069
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:51:31.359669
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 15:51:32.793022
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

# Generated at 2026-10-24 15:51:34.143917
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

# Generated at 2026-10-24 15:51:35.559974
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

# Generated at 2026-10-24 15:51:37.095189
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

# Generated at 2026-10-24 15:51:56.896726
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

# Generated at 2026-10-24 15:51:58.290981
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

# Generated at 2026-10-24 15:51:59.695875
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

# Generated at 2026-10-24 15:52:01.047840
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

# Generated at 2026-10-24 15:52:02.470091
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

# Generated at 2026-10-24 15:52:03.836121
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

# Generated at 2026-10-24 15:52:05.255478
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

# Generated at 2026-10-24 15:52:06.613157
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

# Generated at 2026-10-24 15:52:07.967219
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

# Generated at 2026-10-24 15:52:09.324059
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

# Generated at 2026-10-24 15:52:24.301704
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

# Generated at 2026-10-24 15:52:25.670574
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

# Generated at 2026-10-24 15:52:29.626399
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

# Generated at 2026-10-24 15:52:32.041013
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:52:33.516182
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 15:52:34.919420
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

# Generated at 2026-10-24 15:52:38.996857
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

# Generated at 2026-10-24 15:52:40.480399
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

# Generated at 2026-10-24 15:52:41.913485
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

# Generated at 2026-10-24 15:52:43.346960
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

# Generated at 2026-10-24 15:52:44.781049
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

# Generated at 2026-10-24 15:53:35.059889
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

# Generated at 2026-10-24 15:53:36.429723
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

# Generated at 2026-10-24 15:53:37.927586
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

# Generated at 2026-10-24 15:53:39.360232
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

# Generated at 2026-10-24 15:53:40.793664
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

# Generated at 2026-10-24 15:53:42.226872
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

# Generated at 2026-10-24 15:53:43.588517
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

# Generated at 2026-10-24 15:53:44.936459
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

# Generated at 2026-10-24 15:53:46.292232
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

# Generated at 2026-10-24 15:53:47.642969
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

# Generated at 2026-10-24 15:55:27.525786
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

# Generated at 2026-10-24 15:55:28.880467
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

# Generated at 2026-10-24 15:55:30.228402
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

# Generated at 2026-10-24 15:55:31.674879
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

# Generated at 2026-10-24 15:55:33.128149
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

# Generated at 2026-10-24 15:55:34.506964
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

# Generated at 2026-10-24 15:55:36.921670
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 15:55:39.578196
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 15:55:40.996048
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

# Generated at 2026-10-24 15:55:42.348233
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

# Generated at 2026-10-24 15:55:43.781193
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