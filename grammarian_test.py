import unittest
import grammarian as gm


class MyTestCase(unittest.TestCase):

    ### phrases from letter substitution
    def test_grammarize_phrase_substitute_generates_phrase_with_substitution(self):
        phrases = gm.grammarize_phrase_substitute('make fear')
        self.assertIn('bake fear', phrases)
        self.assertIn('make bear', phrases)
        self.assertIn('make feat', phrases)
        self.assertIn('made fear', phrases)

    def test_grammarize_phrase_substitute_does_not_include_original_phrase(self):
        phrases = gm.grammarize_phrase_substitute('make fear')
        self.assertNotIn('make fear', phrases)
        self.assertNotIn('bake bear', phrases)

    def test_grammarize_phrase_substitute_does_not_include_multiple_words_with_substitutions(self):
        phrases = gm.grammarize_phrase_substitute('make fear')
        self.assertNotIn('bake bear', phrases)

    ### phrases from letter removal
    def test_grammarize_phrase_delete_generates_phrases_with_deletions(self):
        phrases = gm.grammarize_phrase_delete('fear fare')
        self.assertIn('far fare', phrases)
        self.assertIn('fear far', phrases)

    def test_grammarize_phrase_delete_includes_words_with_no_deletions(self):
        phrases = gm.grammarize_phrase_delete('make fear fare')
        self.assertIn('make far fare', phrases)
        self.assertIn('make ear fare', phrases)

    def test_grammarize_word_delete_does_not_include_original_word(self):
        phrases = gm.grammarize_phrase_delete('fear fare')
        self.assertNotIn('fear fare', phrases)

    def test_grammarize_word_delete_does_not_include_word_with_multiple_removals(self):
        phrases = gm.grammarize_phrase_delete('fear fare')
        self.assertNotIn('ear far', phrases)

    ### phrases from letter shifting
    def test_grammarize_phrase_shift_generates_phrase_with_letter_shift(self):
        phrases = gm.grammarize_phrase_shift('make fear')
        self.assertIn('make fare', phrases)

    def test_grammarize_phrase_shift_does_not_include_original_phrase(self):
        phrases = gm.grammarize_phrase_shift('make fear')
        self.assertNotIn('make fear', phrases)

    def test_grammarize_phrase_shift_does_not_include_multiple_shifted_letters(self):
        phrases = gm.grammarize_phrase_shift('make fear')
        self.assertNotIn('fake mare', phrases)

    ### full grammarian function

    def test_grammarize_phrase_generates_phrases_from_substitution(self):
        phrases = gm.grammarize_phrase('make fear')
        self.assertIn('bake fear', phrases)
        self.assertIn('make bear', phrases)
        self.assertIn('make feat', phrases)
        self.assertIn('made fear', phrases)

    def test_grammarize_phrase_generates_phrases_from_deletion(self):
        phrases = gm.grammarize_phrase('make fear')
        self.assertIn('make far', phrases)
        self.assertIn('make ear', phrases)

    def test_grammarize_phrase_generates_phrases_from_shift(self):
        phrases = gm.grammarize_phrase('make fear')
        self.assertIn('make fare', phrases)



if __name__ == '__main__':
    unittest.main()

