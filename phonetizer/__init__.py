import os

import pandas as pd

class WordNotFoundError(Exception):
    def __init__(self, word):
        super(WordNotFoundError, self).__init__(f"Word [{word}] was not found in Lexique.")
        
def word_to_phonem(word):
    module_dir = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_parquet(os.path.join(module_dir, 'lexique.parquet'))
    matches = df.loc[lambda row: row.ortho == word].phon
    if matches.shape[0] == 0:
        raise WordNotFoundError(word)
    else:
        return matches.value_counts().index[0]

