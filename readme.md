# dotsplit
> Transform dot-delimited strings to array of python strings.

[![Build Status](http://img.shields.io/travis/wilmoore/dotsplit.svg)](https://travis-ci.org/wilmoore/dotsplit) [![Code Climate](https://codeclimate.com/github/wilmoore/dotsplit/badges/gpa.svg)](https://codeclimate.com/github/wilmoore/dotsplit) [![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

```shell
❯ poetry install dotsplit
```

## API Example

#### Split on dot

```python
dotsplit('group.0.section.a.seat.3')
//=> ['group', '0', 'section', 'a', 'seat', '3']
```

#### Split on dot preserving escaped characters
> NOT YET IMPLEMENTED

```python
dotsplit('01.document\\.png')
//=> ['01', 'document.png']
```

## API

### `dotsplit(String)`

###### arguments

 - `string (String)` Dot-delimited string.

###### returns

 - `(List)` List of strings.

## Testing
> to run the unit test suite, cd to the root directory and run:

```
❯ poetry install
❯ poetry run pytest
```

## Licenses

[![GitHub license](https://img.shields.io/github/license/wilmoore/dotsplit.svg)](https://github.com/wilmoore/dotsplit/blob/master/license)
