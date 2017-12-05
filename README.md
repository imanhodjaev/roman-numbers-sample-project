## Decimal to roman numerals converter


### Limitations

Solution does not cover large roman numeric systems like
`Apostrophus`, and `Vinculum` and fractions.


### Installing

Solution works with Python 3.

Please install all requirements (only `tox` to run tests)

`$ pip install requirements.txt`


### Running tests

If you installed tox then just run

`$ tox`

Or use pytest to tun tests

`$ pytest`


### Input constraints

1. Input number has to be positive,
2. Input number has to be integer


### Approach

We will use the following table to convert number to roman

| Symbol |  I  |  V  |  X   |   L   |   C   |   D   |   M   |
|--------|-----|-----|------|-------|-------|-------|-------|
| Value  |  1  |  5  |  10  |   50  |  100  |  500  | 1000  |

And we will have extended mapping for the values like

| Symbol |  IV  |  XL  |  9   |  XC   |   CD   |   CM   |
|--------|------|------|------|-------|--------|--------|
| Value  |  4   |  40  |  IX  |  90   |   400  |  900   |


Also [Wiki](https://en.wikipedia.org/wiki/Roman_numerals) has
this table in the introduction section.

Task itself consists of:

1. Making a mapping between roman literals and respective decimal values,
2. Mapping must have descending order so the greater values go first,
3. By iteratively dividing number by the number from table we get the
   number of roman literals to render.


### Usage

#### From command line


First you need to install it using

`$ python setup.py install`

```sh
roman_numerals --help                                               ᴦ/P/ roman-numerals ≡ MASTER
usage: roman_numerals [-h] [-n NUMBER]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Number to convert to roman representation
```


#### As a utility

```py
import roman_numerals

roman_numerals.convert(400)
```


### Commit message format

For commit messages I used [Karma](http://karma-runner.github.io/1.0/dev/git-commit-msg.html)
commit message style with some slight modifications.
