from phonetizer.utils.lexicon import load_lexicon

def test_fetches_cloud_storage():
    assert load_lexicon().shape[0] > 10
