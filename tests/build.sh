#!/bin/bash
echo
echo
echo " [scentamint] Step 1: Executing Unit Tests (Python 2)"
echo
#nosetests tests/test.py --with-coverage --cover-package=scentamint --cover-min-percentage 100
#rm -f .coverage*
echo -e "\nExit Code:" $?
echo
echo " [scentamint] Step 1: Executing Unit Tests (Python 3)"
echo
#nosetests3 tests/test.py --with-coverage --cover-package=scentamint --cover-min-percentage 100
#rm -f .coverage*
echo -e "\nExit Code:" $?

echo
echo " [scentamint] Step 2: Executing pep8 and pyflakes Tests (flake8). (Python 2)"
echo
flake8 scentamint tests
echo "Exit Code:" $?
echo
echo " [scentamint] Step 2: Executing pep8 and pyflakes Tests (flake8). (Python 3)"
echo
flake83 scentamint tests
echo "Exit Code:" $?

echo
echo " [scentamint] Step 3: Executing pylint Tests (Python 2)"
echo
pylint scentamint tests --reports=no
echo "Exit Code:" $?
echo
echo " [scentamint] Step 3: Executing pylint Tests (Python 3)"
echo
pylint3 scentamint tests --reports=no
echo "Exit Code:" $?
echo
