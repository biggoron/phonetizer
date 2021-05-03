# Phonetizer - French

Utils library that checks french phonetization
Provides python functions and CLI.

## Usage

Install as pip package (pip install phonetizer-fr-dan), then use command line:
```
$ check_phonetisation orthophoniste oRtofonist model.pt
-> 1.2
$ check_phonetisation orthophoniste patat model.pt
-> -0.5
```

## Dev

```
from phonetizer import PhonetizerModel
```
