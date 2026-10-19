#!/bin/bash
# Called by eval_codamosa.py to run tests and measure coverage.

# copy package to make it writable
cp -R /package .
cd package

# install dependencies
pip install -r package.txt #|| exit 1

# no longer needed: 'slipcover-runner' image now has these
#pip install --upgrade slipcover || exit 1
#pip install pytest-timeout pytest-cleanslate || exit 1

PKG=$1
JSON=$2
SLIPCOVER_ARGS=$3
PYTEST_ARGS=$4

CMD="python3 -m slipcover --source $PKG --branch --json --out /output/$JSON $SLIPCOVER_ARGS -m pytest --rootdir . -c /dev/null -p no:cacheprovider --timeout 120 $PYTEST_ARGS /tests"
echo $CMD
eval $CMD
