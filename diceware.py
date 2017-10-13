#!/usr/bin/env python3

import argparse, secrets, pyperclip, os
from subprocess import call

parser = argparse.ArgumentParser(description="Generate passphrases from EFF word list")
parser.add_argument('-c','--copy', help="Flag to copy the passphrase to clipboard", action='store_true')
parser.add_argument('-d','--delimiter', default=" ", help="The delimeter for your passphrase words. Defaults to a space")
parser.add_argument('num', nargs=1, type=int, help="How many words you'd like to use")

args = vars(parser.parse_args())
num = args['num'][0]
delimiter = args['delimiter']

script_path = os.path.dirname(os.path.realpath(__file__))
wordlist_path = '%s/eff_large_wordlist.txt' % script_path

def create_passphrase(num, delimiter):
    with open(wordlist_path) as f:
        words = [word.strip() for word in f]
        passphrase = delimiter.join(secrets.choice(words) for i in range(num))
    return passphrase

passphrase = create_passphrase(num, delimiter)

if args['copy']:
    pyperclip.copy(passphrase)
    print("...copied passphrase to clipboard")
else:
    print(passphrase)
