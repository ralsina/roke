# Roke

Roke is a tool and a library to create identifiers. The goal is that these
identifiers should be:

* More or less unique.
* Easy to read, so you can read it to someone else over a phone, for example.
* Configurable: not a single format in how they look
* Customizable: it should be easy to do things like "make it work in spanish"

To do this, inspired by a talk about [Magic Wormhole](https://github.com/warner/magic-wormhole) ... 
I did pretty much the same thing they did.

## Command Line Tool

By default, Roke will give you identifiers made out of two nouns and a small number. Like this:

```
$ roke
19-hassock-disregard
```

You can tell roke to print more than one identifier, so you can choose a nice one.

```
$ roke --count 5
9-vibrissae-truth
4-bathrobe-somewhere
10-dysfunction-overview
19-aardvark-viola
5-mutt-pamphlet
```

You can change the format of the identifiers:

```
$ roke --count 5 --format '{noun}+{noun}'
plate+pasture
pickle+syrup
colloquy+bracelet
prisoner+businessman
membrane+approach
```

Roke comes with two basic dictionaries:

* "noun" which is a list of english nouns taken from http://www.desiquintans.com/nounlist
* "smallnum" which is the numbers from 1 to 20

You can add more dictionaries by putting files with the ".txt" extension and one 
word per line in any of the following places:

```
~/.local/roke
.roke
```

## Python Library

You can use Roke inside your own projects by using it as a library. This example 
shows how:

```
>>> import roke
>>> roke.load_dicts()
>>> roke.gen_identifier('{noun}-{smallnum}')
'village-18'
```

That's all there is to it.

## Technical Notes

So, how unique are the identifiers?

If you use the default format `{smallnum}-{noun}-{noun}` there are only 
925 072 020 possible identifiers. So: NOT VERY UNIQUE.

**Do not use this as a password or a secret!** ... at least not using that format.

They should be unique **enough** for situations where you just need something 
to be "unique for a while" in a certain environment. Like, container names, 
or maybe your children.

Mandatory XKCD:

![XKCD](https://imgs.xkcd.com/comics/password_strength.png)

[Full Comic](https://xkcd.com/936/)

## Why the name?

Roke is the name of an island in Earthsea. To know more about Roke and names,
just read the Earthsea books by Ursula K LeGuin, they are awesome.