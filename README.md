# Marvel API Wrapper

This API wrapper is a work in progress. It gives the ability to interface with the [Marvel API](http://developer.marvel.com/).

I've tried to structure this project logically, since it all boils down to a selection of eight methods for each type. As such, each type will only override the methods that are not available for it and tell you that it won't work. For example, it's not possible to get creators for a character will result in the following message instead:

```shell
Not a valid method for Characters
```

## Usage

To use this, you will need to obtain an API key from Marvel. Using this API key, all you need to do is instantiate the Marvel API object:

```python
from marvel_api import MarvelAPIObject

API_KEY = ""

marvel = MarvelAPIObject(API_KEY)
```

From there, you can get information about characters, comics, creators, events, series, or stories. For example:

```python
print marvel.characters.getOne(15)
```

```python
print marvel.characters.getList(arguments)
```

## Arguments

Apart from the getOne call, which only accepts an "id" argument, all methods require an arguments dict. The arguments for each type may vary, and you'll want to refer to the [API documentation](http://developer.marvel.com/docs#!/public) to see what you can use.

## TODO

* Actually make the API calls (currently only returns the URL to be called)