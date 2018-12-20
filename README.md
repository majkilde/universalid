# UniversalID
Generates unique id's 

## Features

* Unid includes a datetime stamp - your can extract the creation time from a Unid
* You can assign a custom prefix to your id, e.g. a country code
* Unid is case-insentitive 
* Base 36 encoded (digits + letters from A-Z) 
* Uses the _secrets_ library to generate cryptographically strong pseudo-random numbers 

## Getting started

```python
>>>> from universalid import Unid
>>>> Unid.create(prefix='DK')
'DKDQ2D6JCJXI2Q82J06X0PK16P34XDO0'

>>>> unid = Unid.create()
>>>> Unid.get_time( unid )
datetime.datetime(2018, 12, 20, 11, 36, 27, 756356)

```

## Inspiration
The [Nano id](https://github.com/puyuan/py-nanoid) project<br/>
Nano Id collision [calculator](https://zelark.github.io/nano-id-cc/)

[Universal ID](https://www-01.ibm.com/support/docview.wss?uid=swg21112556) in Lotus Notes  
