# harreplay
Convert a HAR file to a Python script that performs the same requests

## Description
HAR files can be exported by Firefox or Chrome (via the Inspect-Network menu).
They contain a JSON description of a sequence of HTTP requests including
headers and request body.

`harreplay` reads a HAR file and outputs a Python script that performs the same
requests using the `requests` module. It can be used as a script or
programmatically as a Python module.

harreplay should be used with Python 2.7

## Installation
Just copy the `harreplay.py` file inside your pythonpath.

If you have the `autopep8` module installed then the output will be PEP8
compliant (this means it will be pretty-printed as well).

## Usage

### As a script
    
    $ python -m harreplay -i test_data/readme_example.har -o code.py
    $ cat code.py
    import requests
    response = requests.post(
        u'http://www.bgtrain.com/',
    
        headers={
            u'Content-Length': u'25',
            u'Accept-Language': u'en-US,en;q=0.5',
            u'Accept-Encoding': u'gzip, deflate',
            u'Connection': u'keep-alive',
            u'Accept': u'text/html,application/xhtml+xml',
            u'Host': u'www.bgtrain.com',
            u'Referer': u'http://www.bgtrain.com/',
            u'Cookie': u'session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70',
            u'Upgrade-Insecure-Requests': u'1',
            u'Content-Type': u'application/x-www-form-urlencoded'},
    
        data=u'username=foo&password=bar',
    )
    response = requests.get(
        u'http://www.bgtrain.com/',
    
        headers={
            u'Accept-Language': u'en-US,en;q=0.5',
            u'Accept-Encoding': u'gzip, deflate',
            u'Connection': u'keep-alive',
            u'Accept': u'text/html,application/xhtml+xml',
            u'Host': u'www.bgtrain.com',
            u'Referer': u'http://www.bgtrain.com/',
            u'Cookie': u'session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70',
            u'Upgrade-Insecure-Requests': u'1'},
    )

### As a module
    >>> import harreplay
    >>> print(harreplay.fobj_to_pystring(open('test_data/readme_example.har')))
    import requests
    response = requests.post(
        u'http://www.bgtrain.com/',
    
        headers={
            u'Content-Length': u'25',
            u'Accept-Language': u'en-US,en;q=0.5',
            u'Accept-Encoding': u'gzip, deflate',
            u'Connection': u'keep-alive',
            u'Accept': u'text/html,application/xhtml+xml',
            u'Host': u'www.bgtrain.com',
            u'Referer': u'http://www.bgtrain.com/',
            u'Cookie': u'session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70',
            u'Upgrade-Insecure-Requests': u'1',
            u'Content-Type': u'application/x-www-form-urlencoded'},
    
        data=u'username=foo&password=bar',
    )
    response = requests.get(
        u'http://www.bgtrain.com/',
    
        headers={
            u'Accept-Language': u'en-US,en;q=0.5',
            u'Accept-Encoding': u'gzip, deflate',
            u'Connection': u'keep-alive',
            u'Accept': u'text/html,application/xhtml+xml',
            u'Host': u'www.bgtrain.com',
            u'Referer': u'http://www.bgtrain.com/',
            u'Cookie': u'session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70',
            u'Upgrade-Insecure-Requests': u'1'},
    )

### Warning
There are probably ways in which someone can mess you up if you run the code
that is produced by processing a HAR file from an untrusted source.
    
