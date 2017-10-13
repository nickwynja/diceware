Inspired by Dr.Drang's [Passphrases via shell pipeline](http://leancrew.com/all-this/2015/04/passphrases-via-shell-pipeline/), this is a python script to generate passphrases from [EFF's wordlist](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases).

# Install

Run `make install` to symlink `diceware.py` to `/usr/local/bin/diceware` and install requirements with `pip3`.

# Usage

```
$ diceware -h
usage: diceware [-h] [-c] [-d DELIMITER] num

Generate passphrases from EFF word list

positional arguments:
  num                   How many words you'd like to use

optional arguments:
  -h, --help            show this help message and exit
  -c, --copy            Flag to copy the passphrase to clipboard
  -d DELIMITER, --delimiter DELIMITER
                        The delimeter for your passphrase words. Defaults to a
                        space
```

`diceware 3` would get you something like `ligament oversleep ammonia` and `diceware -d _ 5` would get you `playmate_smudgy_onscreen_craziness_diaper`.

# Security

I am not a security expert. This script uses [`secrets`](https://docs.python.org/3/library/secrets.html), which is a "used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets." An example similar to this project is shown in the [Recipes and best practices](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices) section, so I trust this is a proper use of `secrets`.

Be aware that the use of `--copy` could expose your passphrase if your system is already compromised. If that's the case, you're already screwed.

Please [create an issue](https://github.com/nickwynja/diceware/issues/new) with any security concerns.
