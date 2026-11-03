

# Generated at 2026-11-02 09:11:54.020992
# Unit test for function is_bored
def test_is_bored():
    # Single sentence starting with "I "
    assert module_0.is_bored("I love programming.") == 1

    # Multiple sentences, some starting with "I "
    assert module_0.is_bored("I love coding. The sun is out. I feel great!") == 2

    # No sentences starting with "I "
    assert module_0.is_bored("Hello world. Nice day today.") == 0

    # Word starting with I but not "I " (e.g., "It")
    assert module_0.is_bored("It is a sunny day.") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Sentence starting with "I " with question mark
    assert module_0.is_bored("I am hungry? Yes I am.") == 2

    # Sentence with exclamation
    assert module_0.is_bored("I am so excited! I can't wait.") == 2

    # "I" without trailing space
    assert module_0.is_bored("I") == 0

    # Sentence starting with "I " after punctuation without space
    assert module_0.is_bored("The sky is blue.I like it.") == 1

    # Leading whitespace before "I"
    assert module_0.is_bored("  I think, therefore I am.") == 1

    print("All tests passed!")


test_is_bored()

# Generated at 2026-11-02 09:13:03.747988
# Unit test for function is_bored
def test_is_bored():
    # No sentences starting with "I "
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0

    # Single bored sentence
    assert module_0.is_bored("I love this weather") == 1
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple bored sentences
    assert module_0.is_bored("I am bored. I want to sleep.") == 2
    assert module_0.is_bored("I am. I was! I will be?") == 3

    # Mixed with other sentence starters
    assert module_0.is_bored("You are boring. I am bored.") == 1
    assert module_0.is_bored("Is it raining? I think so.") == 1

    # "I" alone without trailing space does not count
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("It is fine.") == 0
    assert module_0.is_bored("Ice cream is great.") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Trailing delimiters create empty sentences that don't count
    assert module_0.is_bored("I am bored.") == 1
    assert module_0.is_bored("I am bored!!!") == 1

    # Different delimiters: '.', '?', '!'
    assert module_0.is_bored("I like it! Do you? I do.") == 2

    # Delimiter without following space
    assert module_0.is_bored("I am here.I am there.") == 2

# Generated at 2026-11-02 09:13:32.421358
# Unit test for function is_bored
def test_is_bored():
    # Boredom counting tests
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it") == 1
    assert module_0.is_bored("I am bored. I feel like going out.") == 2
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("If you go, I will stay.") == 0
    assert module_0.is_bored("I love it! I hate it? I want it.") == 3
    assert module_0.is_bored("I.I.I.") == 0
    assert module_0.is_bored("I. I. I.") == 3
    assert module_0.is_bored("You and I are friends.") == 0
    assert module_0.is_bored("I am here!Is anyone there? I think so.") == 2
    assert module_0.is_bored("Is it raining? I hope not.") == 1

# Generated at 2026-11-02 09:14:52.221651
# Unit test for function is_bored
def test_is_bored():
    # Basic case: one sentence starting with "I "
    assert module_0.is_bored("The weather is great. I love it.") == 1

    # Multiple sentences starting with "I "
    assert module_0.is_bored("I love it. I hate it. The end.") == 2

    # No sentences starting with "I "
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Question mark as sentence delimiter
    assert module_0.is_bored("Is it raining? I think so.") == 1

    # Exclamation mark as sentence delimiter
    assert module_0.is_bored("Wow! I am amazed! Incredible.") == 1

    # "It" should not count (starts with "It", not "I ")
    assert module_0.is_bored("It is good. I am happy.") == 1

    # Lone "I" without trailing space should not count
    assert module_0.is_bored("I") == 0

    # Mixed delimiters
    assert module_0.is_bored("I am here! Are you? I am bored. Yes.") == 2

    # Leading "I " in the first sentence
    assert module_0.is_bored("I am the first sentence. Then another.") == 1

    # No punctuation at all — single sentence
    assert module_0.is_bored("I am bored without punctuation") == 1

    # Only whitespace-separated "I" mid-sentence should not double count
    assert module_0.is_bored("You and I are friends.") == 0

# Generated at 2026-11-02 09:15:26.031380
# Unit test for function is_bored
def test_is_bored():
    # Empty string
    assert module_0.is_bored("") == 0
    # Single sentence not starting with "I "
    assert module_0.is_bored("Hello world") == 0
    # Single sentence starting with "I "
    assert module_0.is_bored("I love this weather") == 1
    # Multiple sentences, one bored
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    # Multiple bored sentences separated by periods
    assert module_0.is_bored("I am bored. I want to sleep. It is late.") == 2
    # Sentences separated by exclamation marks
    assert module_0.is_bored("I am happy! You are sad. I am excited?") == 2
    # Sentences separated by question marks
    assert module_0.is_bored("I am here? Is anyone there. I think not") == 2
    # "I" at start but not followed by space
    assert module_0.is_bored("It is cold outside") == 0
    assert module_0.is_bored("Icy roads are dangerous") == 0
    # "I" not at start of sentence
    assert module_0.is_bored("You and I are friends") == 0
    # Mixed punctuation with no space after
    assert module_0.is_bored("I am tired.I need rest") == 2
    # Trailing punctuation
    assert module_0.is_bored("I am fine.") == 1
    # Sentence starting with "I " after split with extra spaces
    assert module_0.is_bored("Hello.  I am testing. Test done") == 1
    print("All test cases passed!")

test_is_bored()