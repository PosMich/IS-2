scripts = ./scripts/*.py
MAIN = main

foo:test.py
    python test.py > $(MAIN)
