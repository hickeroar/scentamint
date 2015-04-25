#!/bin/bash
echo
echo " [scentamint] Step 1: Executing pep8 and pyflakes Tests (flake8). (Python 2)"
echo
flake8 scentamint
echo "Exit Code:" $?
echo
echo " [scentamint] Step 2: Executing pep8 and pyflakes Tests (flake8). (Python 3)"
echo
flake83 scentamint
echo "Exit Code:" $?

echo
echo " [scentamint] Step 3: Executing pylint Tests (Python 2)"
echo
pylint scentamint --reports=no
echo "Exit Code:" $?
echo
echo " [scentamint] Step 4: Executing pylint Tests (Python 3)"
echo
pylint3 scentamint --reports=no
echo "Exit Code:" $?
echo
