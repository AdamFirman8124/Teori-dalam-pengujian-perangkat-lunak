

# Generated at 2026-10-25 01:58:33.022962
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:35.556586
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:38.072150
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:40.594258
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:43.272179
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:45.687877
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:48.105984
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:50.520709
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:52.935571
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:58:55.353681
# Unit test for function rounded_avg

# Generated at 2026-10-25 01:59:10.862271
# Unit test for function rounded_avg
def test_rounded_avg():assert module_0.rounded_avg(1, 1) == '0b1'

# Generated at 2026-10-25 01:59:12.200481
# Unit test for function rounded_avg
def test_rounded_avg():
    assert module_0.rounded_avg(1, 5) == "0b11"      # avg 3
    assert module_0.rounded_avg(1, 1) == "0b1"       # avg 1
    assert module_0.rounded_avg(7, 13) == "0b1010"   # avg 10
    assert module_0.rounded_avg(5, 10) == "0b1000"   # avg 7.5 -> round() -> 8
    assert module_0.rounded_avg(1, 4) == "0b10"      # avg 2.5 -> round() -> 2
    assert module_0.rounded_avg(10, 5) == -1         # m < n
    assert module_0.rounded_avg(30, 2) == -1         # m < n

if __name__ == "__main__":
    test_rounded_avg()
    print("all passed")