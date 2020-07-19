import pytest
from phonetizer import word_to_phonem, WordNotFoundError, sentence_to_phonem

def test_word_to_phonem():
    with pytest.raises(WordNotFoundError):
        phonems = word_to_phonem('zorglub')
    assert word_to_phonem('bonjour') == 'b§ZuR'

def test_sentence_to_phonem():
    assert sentence_to_phonem('bonjour bonjour') == 'b§ZuRb§ZuR'
    with pytest.raises(WordNotFoundError):
        phonems = sentence_to_phonem("bonjour'bonjour")
