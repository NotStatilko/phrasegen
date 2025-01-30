"""This is a main module that stores API classes"""

from os import urandom
from random import Random

from pathlib import Path
from typing import Union, Optional

from .defaults import WORDLISTPATH


__all__ = ['Wordlist', 'Generator']


class Wordlist:
    """
    Wordlist is a class wrapper around the word
    list file. Here you can make random phrase.
    """
    def __init__(
            self, wordlist_path: Path, code: str,
            random_seed: Optional[bytes] = None):
        """
        Arguments:
            wordlist_path (pathlib.Path):
                Path to a directory with a text
                file with words.

            code (str):
                (Language) code is a name of a words
                text file you wish to open. Will be
                processed as (wordlist_path / code)

            random_seed (bytes, Optional):
                Random seed for PRNG. urandom(32) by
                default. Will be used to pick words.
        """
        seed = random_seed or urandom(32)
        self._random = Random(seed)

        self._code_path = wordlist_path / code
        self._list = None

    def _load(self) -> tuple:
        """Will read text file and load words to RAM"""
        if not self._list:
            list_ = open(self._code_path, encoding='utf-8').read()
            self._list = tuple(list_.strip().split('\n'))

        return self._list

    def pick_word(self) -> str:
        """Will return one random word out of list"""
        return self._random.choice(self.list)

    def generate(self, count: Optional[int] = 6,
            separator: Optional[str] = ' ') -> str:
        """
        Will return the <count> random words
        separated by the <separator>.

        Arguments:
            count (int, Optional[6]):
                Specify how many words
                you want in your phrase

            separator (str, Optional[' ']):
                Words separator. Whitespace
                by default.
        """
        return separator.join([self.pick_word() for _ in range(count)])

    @property
    def list(self) -> tuple:
        """
        Will load (if not already loaded) words
        from text file and return tuple.
        """
        return self._load()

class Generator:
    """
    This is a high-level class that loads and stores
    by codes all found Word list text files in the
    <wordlist_path> directory.

    Usage:
        from phrasegen import Generator

        gen = Generator() # Generator() is a class provider for Wordlist(s)
        print(gen.supported_languages) # ('ja', 'ru', 'cs', 'ko', 'zh_cn'...

        print(gen.en.generate()) # 'poem flock future since whisper plate'
        print(gen.it.generate()) # 'risultato molosso irlanda oasi scuro proroga'
        print(gen.fr.generate()) # 'citrus najisto podzim podivit buchta prodej'

        # V 'used+warm+coffee+fox+task+purity+light+neck'
        print(gen.en.generate(count=8, separator='+'))
    """
    def __init__(self, wordlist_path: Optional[Union[str, Path]] = None):
        self._wordlist_path = wordlist_path or WORDLISTPATH

        supported_languages = []
        for code in self._wordlist_path.iterdir():
            wordlist_class = Wordlist(self._wordlist_path, code.name)
            setattr(self, code.name, wordlist_class)
            supported_languages.append(code.name)

        self._supported_languages = tuple(supported_languages)

    @property
    def supported_languages(self) -> tuple:
        """Will return a tuple of supported language codes"""
        return self._supported_languages
