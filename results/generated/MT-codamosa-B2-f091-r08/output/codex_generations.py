

# Generated at 2026-11-03 02:14:59.826141
# Unit test for function is_bored
def test_is_bored():
    # Simple case: one bored sentence
    assert module_0.is_bored("I love it.") == 1

    # No bored sentences
    assert module_0.is_bored("You love it.") == 0
    assert module_0.is_bored("The sky is blue.") == 0

    # Multiple bored sentences
    assert module_0.is_bored("I love It. I hate him. You are good.") == 2

    # Empty string
    assert module_0.is_bored("") == 0

    # Sentence starting with 'I' but not 'I ' (e.g., 'It')
    assert module_0.is_bored("It is sunny.") == 0

    # Different delimiters: question mark and exclamation mark
    assert module_0.is_bored("I am bored! I want to go? You stay.") == 2

    # Word 'I' alone at start without following space
    assert module_0.is_bored("I") == 0

    # Multiple sentences with mixed cases
    assert module_0.is_bored("I think I am bored. I am also tired.") == 2

    # Sentences separated without space after delimiter
    assert module_0.is_bored("I am here.I am there.") == 2

    # No delimiters at all
    assert module_0.is_bored("I am happy") == 1

    print("All test cases passed!")

# Run tests
test_is_bored()

# Generated at 2026-11-03 02:16:42.226321
# Unit test for function is_bored
def test_is_bored():
    # Empty string
    assert module_0.is_bored("") == 0

    # No sentences starting with "I "
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0

    # Single sentence starting with "I " with various terminators
    assert module_0.is_bored("I love it") == 1
    assert module_0.is_bored("I love it.") == 1
    assert module_0.is_bored("I love it?") == 1
    assert module_0.is_bored("I love it!") == 1

    # Multiple sentences, some starting with "I "
    assert module_0.is_bored("I love it. The weather is nice. I am happy!") == 2

    # All sentences starting with "I "
    assert module_0.is_bored("I am bored. I want to sleep. I need coffee.") == 3

    # Starts with "I" but not "I " (e.g., "It", "Ice")
    assert module_0.is_bored("It is a nice day") == 0
    assert module_0.is_bored("Ice cream is good. I like it.") == 1

    # Case sensitivity: lowercase "i" should not count
    assert module_0.is_bored("i am bored") == 0

    # Lone "I" without a following space
    assert module_0.is_bored("I") == 0

    # Punctuation without trailing whitespace
    assert module_0.is_bored("I am here.You are there.I am fine") == 2

    # Sentence ending with punctuation produces empty trailing split
    assert module_0.is_bored("I am here.") == 1

    # Question and exclamation mixed with "I " starts
    assert module_0.is_bored("Is it raining? I think so! You decide.") == 1

# Generated at 2026-11-03 02:18:01.185530
# Unit test for function is_bored
def test_is_bored():
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it") == 1
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("You are great. I am bored.") == 1
    assert module_0.is_bored("I love It. I hate it!") == 2
    assert module_0.is_bored("Is the sky blue?") == 0
    assert module_0.is_bored("I am bored! I want to sleep. I dream of you.") == 3
    assert module_0.is_bored("i am not capitalized. I am.") == 1
    assert module_0.is_bored("It's fine. I think so? I believe.") == 2
    print("All tests passed!")

if __name__ == "__main__":
    test_is_bored()

# Generated at 2026-11-03 02:19:48.903873
# Unit test for function is_bored
def test_is_bored():
    # Empty string -> no sentences starting with 'I '
    assert module_0.is_bored("") == 0

    # No bored sentences
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0

    # Single bored sentence
    assert module_0.is_bored("I love it !") == 1

    # Bored sentence among others
    assert module_0.is_bored("You love it ! I hate it !") == 1
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple bored sentences
    assert module_0.is_bored("I love it ! I hate it !") == 2
    assert module_0.is_bored("I am. I was. I will be.") == 3

    # Question mark delimiter
    assert module_0.is_bored("I am bored? Yes.") == 1

    # 'I' without following space does not count
    assert module_0.is_bored("It is raining.") == 0
    assert module_0.is_bored("Ice cream is good.") == 0

    # Trailing delimiters produce empty sentence fragments (not counted)
    assert module_0.is_bored("I like pizza. ") == 1

    print("All tests passed!")


test_is_bored()

# Generated at 2026-11-03 02:22:09.205662
# Unit test for function is_bored
def test_is_bored():
    # Basic case: no sentence starts with "I "
    assert module_0.is_bored("Hello world") == 0

    # Classic example: one bored sentence
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Single sentence starting with "I "
    assert module_0.is_bored("I love it") == 1

    # Multiple bored sentences
    assert module_0.is_bored("I love it. I hate it") == 2

    # Different punctuation marks: . ! ?
    assert module_0.is_bored("I am bored! Are you? I think so.") == 2

    # No bored sentences
    assert module_0.is_bored("You are nice. We are friends.") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Words starting with "I" but not "I " don't count
    assert module_0.is_bored("Ice cream is tasty. It is cold.") == 0

    # Trailing "I" without a following space doesn't count
    assert module_0.is_bored("Is it fine? I hope so. I") == 2

    # Multiple spaces after punctuation still split correctly
    assert module_0.is_bored("I am here.  I am there.") == 2

    # "I" appearing mid-sentence doesn't count
    assert module_0.is_bored("You and I are friends.") == 0

    # Question mark and exclamation separated bored sentences
    assert module_0.is_bored("I like Python! I code every day? Yes.") == 2

    print("All tests passed!")


test_is_bored()