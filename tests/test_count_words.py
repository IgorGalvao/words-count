from count_words import count_words


class TestCountWords:
  def test_word_count(self):
    text = "This is a simple test"
    assert count_words(text) == 5

  def test_empty_input(self):
    text = ""
    assert count_words(text) == 0

  def test_multiple_spaces(self):
    text = "   This is a test with   multiple     spaces   "
    assert count_words(text) == 7

  def test_text_with_punctuation(self):
    text = "Hello, world! This is a test."
    assert count_words(text) == 6

  def test_text_with_numbers(self):
    text = "This is 1 test"
    assert count_words(text) == 4

  def test_text_with_special_characters(self):
    text = "The test is $10.99!\nThis is another\t@test"
    assert count_words(text) == 8

  def test_large_text(self):
    text = "This is a repeated sentence " * 1000
    assert count_words(text) == 5000
