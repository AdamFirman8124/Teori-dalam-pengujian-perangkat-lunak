

# Generated at 2026-11-03 02:39:22.466464
# Unit test for function is_bored
def test_is_bored():import unittest


class TestIsBored(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(module_0.is_bored(""), 0)

    def test_single_i_sentence(self):
        self.assertEqual(module_0.is_bored("I love this weather"), 1)

    def test_no_boredom(self):
        self.assertEqual(module_0.is_bored("The sky is blue. The sun is shining."), 0)

    def test_multiple_boredoms(self):
        self.assertEqual(module_0.is_bored("I love this weather. I am bored. The sun is shining. I like it."), 3)

    def test_word_starting_with_i_not_counted(self):
        self.assertEqual(module_0.is_bored("It is sunny today."), 0)

    def test_i_without_space(self):
        self.assertEqual(module_0.is_bored("Ibored"), 0)

    def test_question_mark_split(self):
        self.assertEqual(module_0.is_bored("How are you? I am fine."), 1)

    def test_exclamation_split(self):
        self.assertEqual(module_0.is_bored("Wow! I am amazed!"), 1)

    def test_mixed_punctuation(self):
        self.assertEqual(module_0.is_bored("I think so. Really? I do! Yes."), 2)

    def test_leading_sentence(self):
        self.assertEqual(module_0.is_bored("I am here."), 1)

    def test_no_terminal_punctuation(self):
        self.assertEqual(module_0.is_bored("I am still talking"), 1)

    def test_empty_sentences_ignored(self):
        self.assertEqual(module_0.is_bored("I am here.  "), 1)

    def test_lowercase_i_not_counted(self):
        self.assertEqual(module_0.is_bored("i am bored."), 0)

    def test_multiple_spaces_after_punctuation(self):
        self.assertEqual(module_0.is_bored("Hello.   I am fine."), 1)

    def test_consecutive_punctuation(self):
        self.assertEqual(module_0.is_bored("Really?! I can't believe it."), 1)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 02:41:12.918675
# Unit test for function is_bored
def test_is_bored():
    # Basic case: sentence starting with "I "
    assert module_0.is_bored("I love pizza") == 1
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple bored sentences
    assert module_0.is_bored("I am bored. I want to sleep. I need coffee") == 3
    assert module_0.is_bored("I am happy! I am sad? I am okay.") == 3

    # No boredom sentences
    assert module_0.is_bored("The world is big") == 0
    assert module_0.is_bored("You are here. We are there") == 0

    # "I" must be followed by a space to count
    assert module_0.is_bored("It is sunny") == 0
    assert module_0.is_bored("Ice cream is tasty") == 0
    assert module_0.is_bored("I") == 0

    # "I" in the middle of a sentence should not count
    assert module_0.is_bored("You know I am here") == 0
    assert module_0.is_bored("Hello I am bored") == 0

    # Empty string
    assert module_0.is_bored("") == 0

    # Different sentence terminators
    assert module_0.is_bored("I like cats. I like dogs! I like birds?") == 3
    assert module_0.is_bored("I like cats.I like dogs!I like birds?") == 3

    # Single sentence cases
    assert module_0.is_bored("I am here.") == 1
    assert module_0.is_bored("You are there.") == 0

    # Mixed with punctuation and whitespace
    assert module_0.is_bored("I am tired.  The night is long.  I need rest!") == 2

    # Sentence with only whitespace after terminator
    assert module_0.is_bored("I am fine.   ") == 1

    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_is_bored()

# Generated at 2026-11-03 02:44:17.030684
# Unit test for function is_bored
def test_is_bored():
    # Basic case: sentence starting with "I "
    assert module_0.is_bored("I love this weather.") == 1

    # No bored sentences
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0

    # Multiple bored sentences
    assert module_0.is_bored("I love it. I hate it. The end.") == 2

    # Empty string
    assert module_0.is_bored("") == 0

    # Question and exclamation delimiters
    assert module_0.is_bored("I am bored? Yes! I think so.") == 2

    # "I" without trailing space does not count
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("Iron Man is here.") == 0

    # Word starting with 'I' but not "I " does not count
    assert module_0.is_bored("It is cold today.") == 0

    # Mixed delimiters with no space after punctuation
    assert module_0.is_bored("I like dogs.I like cats!Do you?") == 2

    # Sentence with leading whitespace after punctuation
    assert module_0.is_bored("Hello.   I am testing.") == 1

    # Only delimiters
    assert module_0.is_bored(".?!") == 0

    # Non-English / unicode content
    assert module_0.is_bored("I like éclair.") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_is_bored()

# Generated at 2026-11-03 02:46:41.313181
# Unit test for function is_bored
def test_is_bored():
    # No bored sentences
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining.") == 0
    assert module_0.is_bored("You and I are friends") == 0
    assert module_0.is_bored("Is it raining? It is not I who am bored") == 0

    # Empty string and single word edge cases
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I") == 0

    # Single bored sentence
    assert module_0.is_bored("I love it") == 1
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Multiple bored sentences
    assert module_0.is_bored("I am bored! Are you? I think so.") == 2
    assert module_0.is_bored("I love it. I am happy. I feel great!") == 3

    # "I" not followed by space does not count
    assert module_0.is_bored("I. I? I! I") == 0
    assert module_0.is_bored("I'm happy. I am sad.") == 1

    # Case where "I" appears mid-sentence
    assert module_0.is_bored("You and I. We are friends") == 0