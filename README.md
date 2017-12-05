## Decimal to roman numerals converter


### Limitations

Solution does not cover large roman numeric systems like
`Apostrophus`, and `Vinculum` and fractions.

### Python requirements

Solution works with Python 3.
No external dependencies.


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

Task itself consists of making a mapping between roman literals
and respective decimal value.
