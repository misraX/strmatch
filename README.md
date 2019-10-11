[![Build Status](https://travis-ci.org/misraX/strmatch.svg?branch=master)](https://travis-ci.org/misraX/strmatch)
[![codecov](https://codecov.io/gh/misraX/strmatch/branch/master/graph/badge.svg)](https://codecov.io/gh/misraX/strmatch)

A simple way to find strings into a list of strings, and to minimize the number of external dependencies
Python and it's standard libraries are used to build the project, For advanced usages it will be better to
use nltk.

`strmatch.py` uses Python and it's standard libraries to create a simple way of
finding the matched strings from the list.

`test_strmatch.py` uses Python's unittest along with coverage to test and evaluate the code
coverage.

`start.sh` Simple bash script to build a virtualenv and run test.

### Tools Uses:

1. Python (Standard libraries) set, list, unittest.
2. coverages for code coverage.
3. virtualenv for isolated environment.


#### Prerequisite:

1. virtualenv.
2. python 3.
3. Bash.

### Installation:

```
# clone the repo
$ git clone git@github.com:misraX/strmatch.git
$ cd strmatch
# Run the build script.
$ ./start.sh
```       
