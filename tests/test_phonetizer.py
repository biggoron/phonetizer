import pytest
import pandas as pd
from phonetizer import word_to_phonem, WordNotFoundError, sentence_to_phonem

dictionary = pd.DataFrame({'ortho': ['bonjour'], 'phon': ['b§ZuR']})

def test_word_to_phonem():
    with pytest.raises(WordNotFoundError):
        _ = word_to_phonem('zorglub', dictionary)
    assert word_to_phonem('bonjour', dictionary) == 'b§ZuR'

def test_sentence_to_phonem():
    assert sentence_to_phonem('bonjour bonjour', dictionary) == 'b§ZuRb§ZuR'
    with pytest.raises(WordNotFoundError):
        phonems = sentence_to_phonem("bonjour'bonjour", dictionary)
