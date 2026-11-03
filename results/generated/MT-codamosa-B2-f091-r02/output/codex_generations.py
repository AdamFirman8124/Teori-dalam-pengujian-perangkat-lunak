

# Generated at 2026-11-03 03:08:26.013632
# Unit test for function is_bored
def test_is_bored():
# nonce:8724b4dc
    # No bored sentences
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0
    # Empty string
    assert module_0.is_bored("") == 0
    # Single sentence without ending punctuation
    assert module_0.is_bored("I love it") == 1
    # Multiple sentences, one boredom
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    # Multiple bored sentences
    assert module_0.is_bored("I am bored. I want to sleep. I dream.") == 3
    # Different delimiters (?, !, .)
    assert module_0.is_bored("I am bored? Yes! I am.") == 2
    # Bare "I" without trailing space does not count
    assert module_0.is_bored("I") == 0
    # Words starting with "I" but not "I " do not count
    assert module_0.is_bored("Is it raining? It might. I think so.") == 1
    # Trailing punctuation produces an empty trailing sentence (ignored)
    assert module_0.is_bored("I am here.") == 1

# Generated at 2026-11-03 03:10:33.185921
# Unit test for function is_bored
def test_is_bored():
    # Basic cases
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love It !") == 1

    # Sentence starting with "I" but no space after (should not count)
    assert module_0.is_bored("It is a nice day. I am bored.") == 1

    # No sentence starts with "I "
    assert module_0.is_bored("You and I are friends.") == 0

    # Multiple boredoms
    assert module_0.is_bored("I am bored. I want to sleep. I need coffee.") == 3

    # Empty string
    assert module_0.is_bored("") == 0

    # Different delimiters: ?, !
    assert module_0.is_bored("Is the sky blue? I think so!") == 1
    assert module_0.is_bored("I hate Mondays! I love Fridays? Maybe.") == 2

    # Word "I" alone without following space at end
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("I am") == 1

    # Sentence delimiters without trailing space
    assert module_0.is_bored("I like you.Bored?I think so.") == 2

    # Case sensitivity: lowercase 'i' should not count
    assert module_0.is_bored("i am bored.") == 0

    print("All tests passed!")

# Generated at 2026-11-03 03:12:35.761000
# Unit test for function is_bored
def test_is_bored():
    # Sentence starting with "I "
    assert module_0.is_bored("I love It !") == 1

    # Sentence not starting with "I "
    assert module_0.is_bored("You love me") == 0

    # Multiple sentences, only one starts with "I "
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple "I " sentences
    assert module_0.is_bored("I am bored. I want to sleep. You are nice.") == 2

    # Empty string
    assert module_0.is_bored("") == 0

    # Single word "I" without trailing space
    assert module_0.is_bored("I") == 0

    # Question and exclamation delimiters
    assert module_0.is_bored("Is it raining? I think so!") == 1

    # "If" should not count (only "I " counts)
    assert module_0.is_bored("If I go, I will call") == 0

    # All sentences start with "I "
    assert module_0.is_bored("I like it. I need it! I want it?") == 3

    # "It" and "I'll" should not count
    assert module_0.is_bored("It is nice. I'll go now.") == 0

    # No delimiters, one sentence starting with "I "
    assert module_0.is_bored("I think therefore I am") == 1

# Generated at 2026-11-03 03:13:17.845993
# Unit test for function is_bored
def test_is_bored():
    # No sentence starting with "I "
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0

    # One sentence starting with "I "
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it") == 1
    assert module_0.is_bored("You are great. I am bored.") == 1

    # Multiple sentences starting with "I "
    assert module_0.is_bored("I love it ! I hate it .") == 2
    assert module_0.is_bored("I am bored. I want to sleep. You are fine.") == 2

    # Edge cases
    assert module_0.is_bored("") == 0                      # empty string
    assert module_0.is_bored("I") == 0                     # "I" without trailing space
    assert module_0.is_bored("Is the sky blue?") == 0      # starts with "Is", not "I "
    assert module_0.is_bored("i am bored.") == 0           # lowercase 'i' does not count
    assert module_0.is_bored("I  am here") == 0            # double space breaks "I " prefix? -> "I " matches first two chars, still counts
    assert module_0.is_bored("I  am here") == 1            # sentence[0:2] == 'I ' is True

    # Mixed punctuation
    assert module_0.is_bored("I think? I know! I said.") == 3
    assert module_0.is_bored("I a. I b. I c") == 3

    # Sentence starting with "I" followed by punctuation
    assert module_0.is_bored("I. You. We.") == 0           # "I." -> first two chars "I." not "I "

# Generated at 2026-11-03 03:14:20.107028
# Unit test for function is_bored
def test_is_bored():
    # No sentences starting with "I "
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0
    assert module_0.is_bored("You and I are friends.") == 0

    # Sentences starting with "I "
    assert module_0.is_bored("I love this weather") == 1
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I am bored. I want to sleep. It is late.") == 2
    assert module_0.is_bored("I am. I was. I will be!") == 3

    # Different punctuation marks
    assert module_0.is_bored("I love It ! I am happy.") == 2
    assert module_0.is_bored("I like pizza? Yes!") == 1

    # "I" without following space should not count
    assert module_0.is_bored("Is the sky blue?") == 0
    assert module_0.is_bored("It is raining.") == 0
    assert module_0.is_bored("I") == 0

    # Edge cases
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I  am double spaced.") == 0  # "I " requires exactly one space
    assert module_0.is_bored("I am here.I am there.") == 2  # no space after punctuation