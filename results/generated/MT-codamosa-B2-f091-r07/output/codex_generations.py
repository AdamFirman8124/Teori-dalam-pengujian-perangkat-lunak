

# Generated at 2026-11-02 14:07:58.180961
# Unit test for function is_bored
def test_is_bored():
    # Basic case: no boredom sentences
    assert module_0.is_bored("Hello world") == 0

    # One sentence starting with "I "
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple boredom sentences
    assert module_0.is_bored("I love it. I hate it. I want more.") == 3

    # Different delimiters: . ! ?
    assert module_0.is_bored("I am bored! I am tired? I am hungry.") == 3

    # No sentences start with "I "
    assert module_0.is_bored("You are bored. We are bored. They are bored.") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Bare "I" without trailing space does not count
    assert module_0.is_bored("I") == 0

    # Single sentence starting with "I "
    assert module_0.is_bored("I love Python") == 1

    # Mixed sentences, only one starts with "I "
    assert module_0.is_bored("Is the weather nice? It might rain. I hope not.") == 1

    # "I" appearing mid-sentence does not count
    assert module_0.is_bored("You and I know the truth. It is clear.") == 0

    # Whitespace after delimiter handled by regex
    assert module_0.is_bored("I think so.  I am sure.") == 2

    # Sentence starting with "I" as part of another word
    assert module_0.is_bored("Ice cream is great. It is cold.") == 0

# Generated at 2026-11-02 14:09:29.675473
# Unit test for function is_bored
def test_is_bored():import unittest


def module_0.is_bored(S):
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


class TestIsBored(unittest.TestCase):

    def test_single_bored_sentence(self):
        self.assertEqual(module_0.is_bored("I love it."), 1)

    def test_single_not_bored_sentence(self):
        self.assertEqual(module_0.is_bored("The sky is blue."), 0)

    def test_multiple_sentences(self):
        self.assertEqual(module_0.is_bored("I love it. The sky is blue. I like it."), 2)

    def test_empty_string(self):
        self.assertEqual(module_0.is_bored(""), 0)

    def test_exclamation_and_question_marks(self):
        self.assertEqual(module_0.is_bored("I am bored! Are you? I am."), 2)

    def test_word_starting_with_I(self):
        self.assertEqual(module_0.is_bored("It is raining."), 0)

    def test_I_without_space(self):
        self.assertEqual(module_0.is_bored("I"), 0)

    def test_no_punctuation(self):
        self.assertEqual(module_0.is_bored("I am here"), 1)

    def test_multiple_spaces_after_punctuation(self):
        self.assertEqual(module_0.is_bored("I like it.  I mean it."), 2)

    def test_sentence_starting_after_newline(self):
        self.assertEqual(module_0.is_bored("Hello. I am fine."), 1)

    def test_trailing_punctuation(self):
        self.assertEqual(module_0.is_bored("I think so. What about you?"), 1)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 14:11:04.132106
# Unit test for function is_bored
def test_is_bored():
# nonce:62572d59
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love this weather") == 1
    assert module_0.is_bored("You and I are going for a walk") == 0
    assert module_0.is_bored("I am bored. I watch TV. I eat food.") == 3
    assert module_0.is_bored("Is the sky blue?") == 0
    assert module_0.is_bored("I am bored? Yes. I am.") == 2
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I I I") == 1
    assert module_0.is_bored("I like it! I do. I will.") == 3

# Generated at 2026-11-02 14:12:57.113164
# Unit test for function is_bored
def test_is_bored():
    # Single sentence starting with "I"
    assert module_0.is_bored("I love this weather") == 1

    # No sentences starting with "I"
    assert module_0.is_bored("You are great. The sky is blue.") == 0

    # Multiple sentences, some starting with "I"
    assert module_0.is_bored("I love it. The weather is nice. I feel great!") == 2

    # Sentence with "I" not followed by space
    assert module_0.is_bored("It's a beautiful day.") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Single word "I"
    assert module_0.is_bored("I") == 0

    # Sentences separated by different punctuation
    assert module_0.is_bored("I am here?You are there!I like it.") == 2

    # "I" appears mid-sentence, shouldn't count
    assert module_0.is_bored("You and I are friends.") == 0

    # Mixed punctuation and whitespace
    assert module_0.is_bored("I think. I know! I believe?") == 3

    # Sentence starting with "I " but with trailing whitespace variations
    assert module_0.is_bored("  I am bored.  I am sleepy.") == 2

# Generated at 2026-11-02 14:14:50.279377
# Unit test for function is_bored
def test_is_bored():
    from solution import is_bored

    # Empty string
    assert module_0.is_bored("") == 0

    # No sentence starts with "I "
    assert module_0.is_bored("The sky is blue.") == 0
    assert module_0.is_bored("Hello world") == 0

    # Single sentence starting with "I "
    assert module_0.is_bored("I love it.") == 1

    # Multiple sentences, some starting with "I "
    assert module_0.is_bored("I love it. The weather is nice.") == 1
    assert module_0.is_bored("I love it. I hate it.") == 2

    # Different delimiters: '.', '?', '!'
    assert module_0.is_bored("I love it! Do you? I do.") == 2
    assert module_0.is_bored("Is it raining? I think so.") == 1

    # Sentence boundaries without spaces
    assert module_0.is_bored("I love it.The sky is blue.") == 1
    assert module_0.is_bored("I love it?I hate it!") == 2

    # "I" not followed by space should not count
    assert module_0.is_bored("It is sunny. Ice cream is good.") == 0

    # Word starting with I but not the pronoun
    assert module_0.is_bored("It's fine. I agree.") == 1

    # Sentence starting with "I " mid-string
    assert module_0.is_bored("Hello. I am here. Bye. I am gone.") == 2

    # Only "I " with no ending punctuation
    assert module_0.is_bored("I am bored") == 1

    # Multiple delimiters in a row
    assert module_0.is_bored("I am here!! I am there... I am everywhere?") == 3

    # Case sensitivity: lowercase 'i' should not count
    assert module_0.is_bored("i am here. I am there.") == 1

    # Long mixed text
    assert module_0.is_bored(
        "You are what you eat. I say that. Hmm? I wonder why. Yes!"
    ) == 2