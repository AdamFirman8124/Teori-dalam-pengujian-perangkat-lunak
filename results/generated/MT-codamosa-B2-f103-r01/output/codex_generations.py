

# Generated at 2026-10-25 12:48:36.127048
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:38.540490
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:40.954384
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:43.368916
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:45.782753
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:48.194818
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:50.610508
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:53.023039
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:55.451176
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:48:57.859920
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:00.271086
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:02.685437
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:05.103821
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:07.520276
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:09.964379
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:12.375843
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:14.789990
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:17.204276
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:19.617694
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:22.033851
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:24.447364
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:26.863118
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:29.276379
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:31.691302
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:34.106388
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:36.521834
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:38.938178
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:41.355137
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:43.769298
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:46.182168
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:48.597858
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:51.012097
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:53.426330
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:55.844573
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:49:58.258837
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:50:00.672229
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:50:03.086001
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:50:05.501081
# Unit test for function rounded_avg

# Generated at 2026-10-25 12:50:14.296596
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == "0b11"        # avg of 1..5 = 3
    assert module_0.rounded_avg(7, 5) == -1            # m < n
    assert module_0.rounded_avg(10, 20) == "0b1111"    # avg of 10..20 = 15
    assert module_0.rounded_avg(4, 4) == "0b100"       # single element = 4
    assert module_0.rounded_avg(20, 33) == "0b11010"   # avg 26.5 -> round to 26

# Generated at 2026-10-25 12:50:39.283206
# Unit test for function rounded_avg
def test_rounded_avg():
    # n > m â -1
    assert module_0.rounded_avg(7, 5) == -1
    assert module_0.rounded_avg(10, 1) == -1

    # Single element
    assert module_0.rounded_avg(5, 5) == bin(5)          # "0b101"

    # Clean integer average
    assert module_0.rounded_avg(1, 5) == "0b11"          # avg = 3
    assert module_0.rounded_avg(10, 20) == "0b1111"      # avg = 15

    # .5 cases â Python round() uses banker's rounding
    assert module_0.rounded_avg(1, 2) == bin(2)          # 1.5 â 2
    assert module_0.rounded_avg(20, 33) == bin(26)       # 26.5 â 26 (ties to even)
    assert module_0.rounded_avg(1, 4) == bin(2)          # 2.5 â 2 (ties to even)

    # Negative range
    assert module_0.rounded_avg(-5, -1) == bin(-3)       # avg = -3 â "-0b11"

    print("All tests passed.")

test_rounded_avg()

# Generated at 2026-10-25 12:50:48.708790
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == "0b11"      # Average: 3
    assert module_0.rounded_avg(10, 20) == "0b1111"  # Average: 15
    assert module_0.rounded_avg(7, 7) == "0b111"     # Single value
    assert module_0.rounded_avg(2, 3) == "0b10"      # round(2.5) == 2 in Python
    assert module_0.rounded_avg(5, 1) == -1           # Invalid range