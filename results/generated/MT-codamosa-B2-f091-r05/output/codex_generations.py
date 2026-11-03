

# Generated at 2026-11-02 20:49:12.630361
# Unit test for function is_bored
def test_is_bored():
        pass


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 20:50:34.603958
# Unit test for function is_bored
def test_is_bored():
    from solution import is_bored

    # Basic cases
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love this weather") == 1

    # Multiple boredoms
    assert module_0.is_bored("I am bored. I want to sleep. You are fine.") == 2
    assert module_0.is_bored("I think I am bored. I do not know why.") == 2

    # Different sentence-ending punctuation
    assert module_0.is_bored("Is the sky blue?") == 0
    assert module_0.is_bored("I am here! Are you there? I am.") == 2
    assert module_0.is_bored("What is this? I do not know.") == 1

    # Empty string
    assert module_0.is_bored("") == 0

    # No punctuation
    assert module_0.is_bored("I am typing without punctuation") == 1

    # 'I' not followed by space should not count
    assert module_0.is_bored("Ice cream is good.") == 0
    assert module_0.is_bored("It is I.") == 0

    # Sentence starting with I after punctuation without space
    assert module_0.is_bored("Hello.I am here.") == 1

    # Only 'I ' at very start
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("I ") == 1

    print("All tests passed!")

# Generated at 2026-11-02 20:52:08.521602
# Unit test for function is_bored
def test_is_bored():
    # Simple case: single sentence starting with "I"
    assert module_0.is_bored("I love this weather") == 1

    # Sentence not starting with "I"
    assert module_0.is_bored("You love me") == 0

    # Multiple sentences, one starts with "I"
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple sentences starting with "I"
    assert module_0.is_bored("I am bored. I feel lonely. I want to go out!") == 3

    # Empty string
    assert module_0.is_bored("") == 0

    # No sentence starts with "I"
    assert module_0.is_bored("Is the sky blue?") == 0

    # "I" not followed by space does not count
    assert module_0.is_bored("It is raining.") == 0

    # Question mark and exclamation separators
    assert module_0.is_bored("I like it! I mean it? I do.") == 3

    # Word boundary check: "I" alone without following text
    assert module_0.is_bored("I") == 0

    # Sentence starting with "I " after punctuation and whitespace
    assert module_0.is_bored("Hello. I am here.") == 1

    # Case sensitivity: lowercase "i" does not count
    assert module_0.is_bored("i am bored.") == 0

    print("All tests passed!")


test_is_bored()

# Generated at 2026-11-02 20:53:07.959257
# Unit test for function is_bored
def test_is_bored():
    # No sentences starting with "I "
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0

    # Single sentence starting with "I "
    assert module_0.is_bored("I love it") == 1
    assert module_0.is_bored("I am bored") == 1

    # Multiple sentences, one bored sentence
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple bored sentences
    assert module_0.is_bored("I like apples. I eat them daily.") == 2
    assert module_0.is_bored("I am here! I am there? I am everywhere.") == 3

    # Question and exclamation delimiters
    assert module_0.is_bored("I think so! Do you? I do.") == 2
    assert module_0.is_bored("Is it raining? I wonder.") == 1

    # Empty string
    assert module_0.is_bored("") == 0

    # Bored word but not at start of sentence
    assert module_0.is_bored("You know I am bored.") == 0
    assert module_0.is_bored("They say I should go.") == 0

    # Sentence starting with "I" but not "I "
    assert module_0.is_bored("It is sunny. Ice is cold.") == 0

    # "I " must be followed by space
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("I. I am.") == 1

    # Mixed delimiters without trailing space
    assert module_0.is_bored("I am here.I am there.") == 2

    # Word starting with I followed by punctuation
    assert module_0.is_bored("Isn't it great? I think yes.") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_is_bored()

# Generated at 2026-11-02 20:53:54.049760
# Unit test for function is_bored
def test_is_bored():
    # Single sentence starting with "I"
    assert module_0.is_bored("I love it") == 1

    # Sentences not starting with "I"
    assert module_0.is_bored("The sky is blue") == 0
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("Is the sky blue?") == 0

    # Multiple sentences, only one starting with "I"
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple sentences starting with "I"
    assert module_0.is_bored("I love it. I hate it. You love it.") == 2

    # Mix of sentence-ending punctuation
    assert module_0.is_bored("I am bored! Are you bored? I want to go home.") == 2

    # Starts with "I" but no space after (e.g., "It's")
    assert module_0.is_bored("It's a lovely day") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Trailing punctuation creates empty sentence after split, but count unaffected
    assert module_0.is_bored("I am fine.") == 1

    # Punctuation with no following space
    assert module_0.is_bored("I am here!You are there.") == 1

    # Only "I" without space
    assert module_0.is_bored("I") == 0

    print("All tests passed!")


test_is_bored()