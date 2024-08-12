# *Phrasegen*: Little package for making phrases

**Phrasegen** is a package that can help you generate *variable sized* Random phrases.\
We use word lists from [**one of the Trezor projects**](https://github.com/trezor/python-mnemonic/tree/master/src/mnemonic/wordlist), thus, support multiple languages.

## Installation

### From PyPI
```bash
# Install the latest version with pip
pip install phrasegen
```
### You can also Clone and install:
```bash
git clone https://github.com/NotStatilko/phrasegen
pip install ./phrasegen
```

## Usage Example
```python3
from phrasegen import Generator

gen = Generator() # Generator() is a class provider for Word lists
print(gen.supported_languages) # ('ja', 'ru', 'cs', 'ko', 'zh_cn'...

# .generate() method just randomly select words from
# the list of words. Dead simple process.

print(gen.en.generate()) # 'poem flock future since whisper plate'
print(gen.it.generate()) # 'risultato molosso irlanda oasi scuro proroga'
print(gen.fr.generate()) # 'citrus najisto podzim podivit buchta prodej'

# V 'used+warm+coffee+fox+task+purity+light+neck'
print(gen.en.generate(count=8, separator='+'))
```
