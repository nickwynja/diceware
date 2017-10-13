PWD := $(shell pwd)
.PHONY: install

install:
	pip3 install -r requirements.txt
	ln -fs $(PWD)/diceware.py /usr/local/bin/diceware
