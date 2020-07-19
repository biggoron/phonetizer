import pytest
from phonetizer import word_to_phonem, WordNotFoundError

def test_word_to_phonem():
    with pytest.raises(WordNotFoundError):
        phonems = word_to_phonem('zorglub')
    assert word_to_phonem('bonjour') == 'b§ZuR'
