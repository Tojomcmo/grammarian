import unittest
import grammarian as gm


class MyTestCase(unittest.TestCase):
    def test_grammarize_word_generates_word_with_substitution(self):
        words = gm.grammarize_word('fear')
        self.assertIn('bear', words)
        self.assertIn('feat', words)

    def test_grammarize_word_does_not_include_original_word(self):
        words = gm.grammarize_word('fear')
        self.assertNotIn('fear', words)

    def test_grammarize_word_does_not_include_word_with_multiple_substitutions(self):
        words = gm.grammarize_word('fear')
        self.assertNotIn('beer', words)

    def test_grammarize_phrase_generates_phrase_with_substitution(self):
        words = gm.grammarize_phrase('make fear')
        self.assertIn('bake fear', words)
        self.assertIn('make bear', words)
        self.assertIn('make feat', words)
        self.assertIn('made fear', words)

    def test_grammarize_phrase_does_not_include_original_phrase(self):
        words = gm.grammarize_phrase('make fear')
        self.assertNotIn('make fear', words)
        self.assertNotIn('bake bear', words)

    def test_grammarize_phrase_does_not_include_multiple_words_with_substitutions(self):
        words = gm.grammarize_phrase('make fear')
        self.assertNotIn('bake bear', words)




if __name__ == '__main__':
    unittest.main()
