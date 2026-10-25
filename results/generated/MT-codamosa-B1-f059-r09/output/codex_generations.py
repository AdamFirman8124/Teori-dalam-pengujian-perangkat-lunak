

# Generated at 2026-10-24 19:48:21.437950
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:24.125104
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:26.666540
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:29.083315
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:31.503828
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:33.921420
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:36.339752
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:38.756691
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:41.174857
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:43.591927
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:46.008674
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:48.427712
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:50.844498
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:53.259807
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:48:55.676976
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:05.671847
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:08.087318
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:10.504438
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:12.166491
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

# Generated at 2026-10-24 19:49:13.526686
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

# Generated at 2026-10-24 19:49:15.033182
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

# Generated at 2026-10-24 19:49:16.385665
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

# Generated at 2026-10-24 19:49:17.744597
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

# Generated at 2026-10-24 19:49:19.095253
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

# Generated at 2026-10-24 19:49:20.565940
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

# Generated at 2026-10-24 19:49:21.997318
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

# Generated at 2026-10-24 19:49:23.430762
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

# Generated at 2026-10-24 19:49:28.413259
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

# Generated at 2026-10-24 19:49:29.881547
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

# Generated at 2026-10-24 19:49:31.315829
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

# Generated at 2026-10-24 19:49:32.720097
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

# Generated at 2026-10-24 19:49:34.074688
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

# Generated at 2026-10-24 19:49:35.434616
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

# Generated at 2026-10-24 19:49:36.795310
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

# Generated at 2026-10-24 19:49:39.309968
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:41.729956
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:44.160608
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:46.578487
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:48.998894
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:51.412218
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:49:52.775189
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

# Generated at 2026-10-24 19:49:57.222426
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

# Generated at 2026-10-24 19:49:58.656947
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

# Generated at 2026-10-24 19:50:00.091050
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

# Generated at 2026-10-24 19:50:01.525850
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

# Generated at 2026-10-24 19:50:02.956390
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

# Generated at 2026-10-24 19:50:04.325806
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

# Generated at 2026-10-24 19:50:05.741622
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

# Generated at 2026-10-24 19:50:07.154945
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

# Generated at 2026-10-24 19:50:08.587988
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

# Generated at 2026-10-24 19:50:10.022253
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

# Generated at 2026-10-24 19:50:18.132991
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:20.551194
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:22.966280
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:25.381469
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:27.802541
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:30.435703
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:32.851400
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:35.269556
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:37.689011
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:40.105156
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:42.523259
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:44.940613
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:47.356667
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:49.774685
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:52.191402
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:54.610347
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:57.034752
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:50:59.446972
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:01.865314
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:03.270835
# Unit test for function largest_prime_factor
def test_largest_prime_factor():assert module_0.largest_prime_factor(15) == 5

# Generated at 2026-10-24 19:51:04.707721
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

# Generated at 2026-10-24 19:51:06.068239
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

# Generated at 2026-10-24 19:51:07.429871
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

# Generated at 2026-10-24 19:51:24.364792
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

# Generated at 2026-10-24 19:51:25.799311
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

# Generated at 2026-10-24 19:51:28.331119
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:30.869627
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:33.286218
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:35.815022
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:38.232302
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:40.652392
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:43.067033
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:45.482788
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:47.900482
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:50.316342
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:52.734658
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:55.151186
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:57.570803
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:51:59.989747
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:02.409351
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:04.825980
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:07.241240
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:09.658951
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:12.072745
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:14.489982
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:16.905845
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:19.321793
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:21.738123
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:52:24.156294
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:53:16.807346
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

# Generated at 2026-10-24 19:53:18.235485
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

# Generated at 2026-10-24 19:53:19.638642
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

# Generated at 2026-10-24 19:53:21.006788
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

# Generated at 2026-10-24 19:53:22.376593
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

# Generated at 2026-10-24 19:53:23.743655
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

# Generated at 2026-10-24 19:53:25.141743
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

# Generated at 2026-10-24 19:53:26.543913
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

# Generated at 2026-10-24 19:53:27.906670
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

# Generated at 2026-10-24 19:53:29.294576
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

# Generated at 2026-10-24 19:54:57.726290
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:00.253875
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:02.669584
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:05.193703
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:07.609457
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:10.025954
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:12.587628
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:15.005187
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:17.421731
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:19.836418
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:22.254441
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:24.669315
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:27.086295
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:29.501585
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:31.919066
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:34.336174
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:36.753395
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:39.168677
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:41.586239
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:44.007019
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:46.425691
# Unit test for function largest_prime_factor

# Generated at 2026-10-24 19:55:47.835821
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

# Generated at 2026-10-24 19:55:49.187024
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

# Generated at 2026-10-24 19:55:50.605602
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