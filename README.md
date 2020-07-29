# Phonetizer - French

Utils library that converts French word or text into phonems.
Provides python functions and CLI.

## Usage

Install as pip package, then use command line:
```
$ sentence_to_phonem maison
-> mEz§
```

## Under the cogs

- Cuts sentence into words
- Checks if word is in dictionary
- If so returns phonemic translation
- Else returns WordNotFoundError

## Todo

- Create a lib for a transformer model, which infers prononciation of not found words. The lib can train a model to generate weights, and provides a model object which can load weights and infer phonemic translations.
- Parse Wiktionaire for more comprehensive dictionary
- Create POS-Tagging to resolve non-homophonic homograms 
