

# Generated at 2026-11-01 20:30:35.290069
# Unit test for function is_bored
def test_is_bored():
    # Single sentence starting with "I "
    assert module_0.is_bored("I love this weather") == 1

    # No sentences starting with "I "
    assert module_0.is_bored("Hello world") == 0

    # Multiple sentences, one starts with "I "
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple sentences, several start with "I "
    assert module_0.is_bored("I am happy today. I feel great! The weather is nice.") == 2

    # Multiple sentences all starting with "I "
    assert module_0.is_bored("I like pizza. I like pasta. I like salad.") == 3

    # Empty string
    assert module_0.is_bored("") == 0

    # Sentence starting with "I" but not "I " (no space)
    assert module_0.is_bored("Ice cream is tasty") == 0

    # Mixed punctuation with exclamation and question marks
    assert module_0.is_bored("I am bored! Are you? I think so.") == 2

    # "I" appears mid-sentence but not at start
    assert module_0.is_bored("You know I am here. Yes I am.") == 0

    # Extra whitespace before exclamation
    assert module_0.is_bored("I love it !") == 1

    # No terminal punctuation
    assert module_0.is_bored("I am here") == 1

    # Sentence with just "I "
    assert module_0.is_bored("I .") == 1

    # Consecutive punctuation
    assert module_0.is_bored("I said it!! I meant it?") == 2

    print("All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_is_bored()

# Generated at 2026-11-01 20:31:00.792372
# Unit test for function is_bored
def test_is_bored():
    # Basic cases
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("I love this weather") == 1
    assert module_0.is_bored("The sky is blue. I love it.") == 1

    # Multiple sentences with bored ones
    assert module_0.is_bored("I love It ! The sky is blue.") == 1
    assert module_0.is_bored("Is the sky blue? I think so.") == 1
    assert module_0.is_bored("I am bored. I want to go home! Are you coming?") == 2

    # No sentences starting with 'I '
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("You and I are friends.") == 0
    assert module_0.is_bored("It is sunny today.") == 0

    # Edge cases with punctuation
    assert module_0.is_bored("I.") == 0
    assert module_0.is_bored("I !") == 0
    assert module_0.is_bored("I love pizza?I also love pasta!I eat daily.") == 3

    # Sentences split by different punctuation marks
    assert module_0.is_bored("I like apples. Do you? I do!") == 2

    # Case sensitivity check
    assert module_0.is_bored("i like apples. I like oranges.") == 1

    # Sentence starting with 'I' but not 'I '
    assert module_0.is_bored("Ice cream is tasty.") == 0

    print("All tests passed!")

# Generated at 2026-11-01 20:31:21.985910
# Unit test for function is_bored
def test_is_bored():
    # Single sentence starting with "I"
    assert module_0.is_bored("I love it.") == 1

    # Multiple sentences, some starting with "I"
    assert module_0.is_bored("The weather is nice. I went outside. It was fun!") == 1
    assert module_0.is_bored("I went outside. The weather is nice. I had fun!") == 2

    # No sentences starting with "I"
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0
    assert module_0.is_bored("You and I are friends.") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Different delimiters: exclamation and question marks
    assert module_0.is_bored("I am bored! Are you? I think so.") == 2

    # Words starting with 'I' but not the standalone word "I"
    assert module_0.is_bored("It is cold.") == 0
    assert module_0.is_bored("Iron man is here.") == 0

    # Lone "I" without a following space
    assert module_0.is_bored("I") == 0

    # Sentence starting with "I" but no ending punctuation
    assert module_0.is_bored("I am here") == 1

    # Multiple spaces after punctuation
    assert module_0.is_bored("Hello.  I am fine.") == 1

    # Leading whitespace before "I"
    assert module_0.is_bored("  I am happy today.") == 1

    print("All tests passed!")


test_is_bored()

# Generated at 2026-11-01 20:31:35.912387
# Unit test for function is_bored
def test_is_bored():
    # Non-bored input: no sentence starting with "I "
    assert module_0.is_bored("Hello world") == 0
    
    # Bored input: single sentence starting with "I "
    assert module_0.is_bored("I love it.") == 1
    
    # Mixed sentences: only one starts with "I "
    assert module_0.is_bored("The sky is blue. I love it.") == 1
    
    # Multiple bored sentences
    assert module_0.is_bored("I love It ! I am happy.") == 2
    
    # Different punctuation types
    assert module_0.is_bored("I see it? Yes! I do.") == 2
    
    # Sentence starting with "I" but not "I " should not count
    assert module_0.is_bored("It is sunny.") == 0
    
    # Question starting with "Is" does not count
    assert module_0.is_bored("Is the sky blue?") == 0
    
    # Empty string
    assert module_0.is_bored("") == 0
    
    # Single word without terminal punctuation still evaluated
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("I am") == 1

# Generated at 2026-11-01 20:31:55.674467
# Unit test for function is_bored
def test_is_bored():
    # Basic case: one bored sentence
    assert module_0.is_bored("I love it.") == 1
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple bored sentences
    assert module_0.is_bored("I am bored. I want to sleep.") == 2

    # No bored sentences
    assert module_0.is_bored("Hello world") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Different delimiters: ? and !
    assert module_0.is_bored("I like you? Yes!") == 1
    assert module_0.is_bored("Is it raining? I think so.") == 1

    # "I" not followed by a space doesn't count
    assert module_0.is_bored("It is sunny. Ice cream is cold.") == 0

    # "I" in the middle of a sentence doesn't count
    assert module_0.is_bored("And I say hello.") == 0

    # Lone "I" without trailing space doesn't count
    assert module_0.is_bored("I") == 0

    # Leading bored sentence counts
    assert module_0.is_bored("I stand alone. Nobody cares.") == 1

    # Trailing delimiter creating empty sentence still works
    assert module_0.is_bored("I go home! ") == 1

    print("All tests passed!")


test_is_bored()