

# Generated at 2026-11-02 23:41:12.073993
# Unit test for function is_bored
def test_is_bored():
    # Single sentence not starting with "I "
    assert module_0.is_bored("Hello world") == 0

    # Multiple sentences, only one starts with "I "
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Question sentence not starting with "I "
    assert module_0.is_bored("Is the sky blue?") == 0

    # Exclamation sentence starting with "I "
    assert module_0.is_bored("I love It !") == 1

    # Word containing "I" but not starting sentence
    assert module_0.is_bored("bIt") == 0

    # Multiple sentences starting with "I "
    assert module_0.is_bored("I feel good today. I will be productive. will kill It") == 2

    # "I" appears mid-sentence, should not count
    assert module_0.is_bored("You and I are going for a walk") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Sentence that is just "I" with no following space
    assert module_0.is_bored("I") == 0

    # Mixed punctuation delimiters (?, !, .)
    assert module_0.is_bored("I am happy! Are you? I think so. Maybe not.") == 2

# Generated at 2026-11-02 23:42:41.266353
# Unit test for function is_bored
def test_is_bored():
    # Simple case: one bored sentence
    assert module_0.is_bored("I love it.") == 1

    # Multiple sentences, two boredoms
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it. I hate it. It is fine.") == 2

    # No boredoms at all
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("You and I are friends.") == 0

    # "It" should not count (only "I " with a space)
    assert module_0.is_bored("It is sunny. I am happy.") == 1

    # Empty string
    assert module_0.is_bored("") == 0

    # Sentences separated by ! and ?
    assert module_0.is_bored("I am bored! Are you? I think so.") == 2

    # Sentence starts with "I" but no following space
    assert module_0.is_bored("Ice cream is great.") == 0

    # Word containing I at start of word
    assert module_0.is_bored("Isn't it nice? I agree.") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_is_bored()

# Generated at 2026-11-02 23:44:32.575882
# Unit test for function is_bored
def test_is_bored():
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from solution import is_bored

    # Basic case: no sentence starts with "I "
    assert module_0.is_bored("Hello world") == 0

    # One sentence starts with "I "
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Sentence starts with "I "
    assert module_0.is_bored("I love this weather") == 1

    # Empty string
    assert module_0.is_bored("") == 0

    # Just "I" without following space
    assert module_0.is_bored("I") == 0

    # Multiple bored sentences
    assert module_0.is_bored("I am bored. I want to sleep. You are fine.") == 2

    # Question and exclamation endings
    assert module_0.is_bored("I like pizza! Do you? I think so.") == 2

    # "I" at start of word should not count
    assert module_0.is_bored("Ice cream is good.") == 0

    # "I" after punctuation with no space
    assert module_0.is_bored("You know. I know.") == 1

    # Sentence starting with "I" but not "I "
    assert module_0.is_bored("It is raining.") == 0

    # All sentences bored
    assert module_0.is_bored("I am here. I am there. I am everywhere.") == 3

    # No punctuation at end still counts
    assert module_0.is_bored("I am tired") == 1

    # Single word sentence
    assert module_0.is_bored("I. You. We.") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_is_bored()

# Generated at 2026-11-02 23:45:34.526868
# Unit test for function is_bored
def test_is_bored():
    # Basic case: one bored sentence
    assert module_0.is_bored("I love it.") == 1
    assert module_0.is_bored("The sky is blue. I love it.") == 1

    # No bored sentences
    assert module_0.is_bored("The sky is blue.") == 0
    assert module_0.is_bored("You and I are friends.") == 0  # "I " not at sentence start

    # Multiple bored sentences
    assert module_0.is_bored("I love it. I hate it. I am bored.") == 3

    # Different delimiters: ?, !
    assert module_0.is_bored("I am happy? I am sad! I am angry.") == 3
    assert module_0.is_bored("Am I happy? I am sad!") == 1

    # Empty string and whitespace-only
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("   ") == 0

    # Sentence that is just "I"
    assert module_0.is_bored("I") == 0  # "I" alone, no trailing space
    assert module_0.is_bored("I.") == 0  # "I" followed by period, no space

    # "I" as part of a word at sentence start
    assert module_0.is_bored("It is sunny. Ice is cold.") == 0

    # Multiple sentences without trailing whitespace after delimiter
    assert module_0.is_bored("I think so.I am sure.") == 2

    # Mixed case check: lowercase "i " should not count
    assert module_0.is_bored("i think. I know.") == 1

    # Newline as whitespace after delimiter
    assert module_0.is_bored("I am here.\nI am there.") == 2

# Generated at 2026-11-02 23:47:04.025733
# Unit test for function is_bored
def test_is_bored():
    # Basic cases
    assert module_0.is_bored("I love it.") == 1
    assert module_0.is_bored("I love it. I hate it.") == 2
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Different sentence delimiters
    assert module_0.is_bored("I am bored! I am tired? I am sleepy.") == 3

    # Edge cases
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I") == 0                    # 'I' alone lacks trailing space
    assert module_0.is_bored("i love it.") == 0           # lowercase 'i' does not count
    assert module_0.is_bored("It is raining.") == 0       # 'It' != 'I '
    assert module_0.is_bored("Ice cream is tasty.") == 0  # 'Ic' != 'I '

    # 'I' mid-sentence does not count
    assert module_0.is_bored("And I said hello.") == 0
    assert module_0.is_bored("You are here. We are there.") == 0

    # Consecutive delimiters produce empty sentences (not counted)
    assert module_0.is_bored("I am here.. I am there") == 2
    assert module_0.is_bored("I am!! I am") == 2

    # Whitespace (including newlines) after delimiters is skipped
    assert module_0.is_bored("I am here.   I am there.") == 2
    assert module_0.is_bored("I am here.\nI am there.") == 2

    print("test_is_bored passed")


if __name__ == "__main__":
    test_is_bored()