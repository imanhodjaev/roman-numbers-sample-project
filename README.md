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


### Input constraints

1. Input number has to be positive,
2. Input number has to be integer

### Approach

We will use the following table to convert number to roman

| Symbol |  I  |  V  |  X   |   L   |   C   |   D   |   M   |
|--------|-----|-----|------|-------|-------|-------|-------|
| Value  |  1  |  5  |  10  |   50  |  100  |  500  | 1000  |

Though we could have extended this table with literals
like `IV=4` and `IX=9` I think it is better to keep it
this way because Roman numerals just use them for convenience.
Also [Wiki](https://en.wikipedia.org/wiki/Roman_numerals) has
this table in the introduction section.

Task itself consists of:

1. Making a mapping between roman literals and respective decimal values,
2. Mapping must have descending order so the greater values go first,
3. By iteratively dividing number by the number from table we get the
   number of roman literals to render.
