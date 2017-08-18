# harreplay
Convert a HAR file to a Python script that performs the same requests

## Description
HAR files can be exported by Firefox or Chrome (via the Inspect-Network menu).
They contain a JSON description of a sequence of HTTP requests including
headers and request body.

`harreplay` reads a HAR file and outputs a Python script that performs the same
requests using the `requests` module. It can be used as a script or
programmatically as a Python module.

## Installation
Just copy the `harreplay.py` file inside your pythonpath.

If you have the `autopep8` module installed then the output will be PEP8
compliant (this means it will be pretty-printed as well).

## Usage

### As a script
    
    $ cat test_data/readme_example.har
    {
      "log": {
        "version": "1.1",
        "creator": {
          "name": "Firefox",
          "version": "55.0.1"
        },
        "browser": {
          "name": "Firefox",
          "version": "55.0.1"
        },
        "pages": [
          {
            "startedDateTime": "2017-08-18T12:58:48.848+03:00",
            "id": "page_1",
            "title": "New Tab",
            "pageTimings": {
              "onContentLoad": -1,
              "onLoad": -1
            }
          }
        ],
        "entries": [
          {
            "pageref": "page_1",
            "startedDateTime": "2017-08-18T12:58:48.848+03:00",
            "time": null,
            "request": {
              "bodySize": 25,
              "method": "POST",
              "url": "http://www.bgtrain.com/",
              "httpVersion": "HTTP/1.1",
              "headers": [
                {
                  "name": "Host",
                  "value": "www.bgtrain.com"
                },
                {
                  "name": "User-Agent",
                  "value": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
                },
                {
                  "name": "Accept",
                  "value": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                },
                {
                  "name": "Accept-Language",
                  "value": "en-US,en;q=0.5"
                },
                {
                  "name": "Accept-Encoding",
                  "value": "gzip, deflate"
                },
                {
                  "name": "Content-Type",
                  "value": "application/x-www-form-urlencoded"
                },
                {
                  "name": "Content-Length",
                  "value": "25"
                },
                {
                  "name": "Referer",
                  "value": "http://www.bgtrain.com/"
                },
                {
                  "name": "Cookie",
                  "value": "session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70"
                },
                {
                  "name": "Connection",
                  "value": "keep-alive"
                },
                {
                  "name": "Upgrade-Insecure-Requests",
                  "value": "1"
                }
              ],
              "cookies": [],
              "queryString": [],
              "postData": {
                "mimeType": "application/x-www-form-urlencoded",
                "params": [],
                "text": "username=foo&password=bar"
              },
              "headersSize": 489
            },
            "response": {
              "status": 303,
              "statusText": "See Other",
              "httpVersion": "HTTP/1.1",
              "headers": [
                {
                  "name": "Server",
                  "value": "openresty/1.9.15.1"
                },
                {
                  "name": "Date",
                  "value": "Fri, 18 Aug 2017 09:58:50 GMT"
                },
                {
                  "name": "Content-Type",
                  "value": "text/html;charset=utf-8"
                },
                {
                  "name": "Content-Length",
                  "value": "90"
                },
                {
                  "name": "Connection",
                  "value": "keep-alive"
                },
                {
                  "name": "Content-Encoding",
                  "value": "gzip"
                },
                {
                  "name": "Vary",
                  "value": "Accept-Encoding"
                },
                {
                  "name": "Location",
                  "value": "http://www.bgtrain.com/"
                },
                {
                  "name": "Set-Cookie",
                  "value": "session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70; expires=Fri, 17 Nov 2017 17:25:50 GMT; Path=/"
                },
                {
                  "name": "X-Clacks-Overhead",
                  "value": "GNU Terry Pratchett"
                }
              ],
              "cookies": [],
              "redirectURL": "http://www.bgtrain.com/",
              "headersSize": 408,
              "bodySize": 3613
            },
            "cache": {},
            "timings": {
              "blocked": 1,
              "dns": 0,
              "connect": 0,
              "send": 0,
              "wait": 213,
              "receive": 0
            },
            "serverIPAddress": "34.206.101.184",
            "connection": "80"
          },
          {
            "pageref": "page_1",
            "startedDateTime": "2017-08-18T12:58:49.078+03:00",
            "time": 328,
            "request": {
              "bodySize": 0,
              "method": "GET",
              "url": "http://www.bgtrain.com/",
              "httpVersion": "HTTP/1.1",
              "headers": [
                {
                  "name": "Host",
                  "value": "www.bgtrain.com"
                },
                {
                  "name": "User-Agent",
                  "value": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
                },
                {
                  "name": "Accept",
                  "value": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                },
                {
                  "name": "Accept-Language",
                  "value": "en-US,en;q=0.5"
                },
                {
                  "name": "Accept-Encoding",
                  "value": "gzip, deflate"
                },
                {
                  "name": "Referer",
                  "value": "http://www.bgtrain.com/"
                },
                {
                  "name": "Cookie",
                  "value": "session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70"
                },
                {
                  "name": "Connection",
                  "value": "keep-alive"
                },
                {
                  "name": "Upgrade-Insecure-Requests",
                  "value": "1"
                }
              ],
              "cookies": [],
              "queryString": [],
              "postData": {
                "mimeType": "",
                "params": [],
                "text": ""
              },
              "headersSize": 419
            },
            "response": {
              "status": 200,
              "statusText": "OK",
              "httpVersion": "HTTP/1.1",
              "headers": [
                {
                  "name": "Server",
                  "value": "openresty/1.9.15.1"
                },
                {
                  "name": "Date",
                  "value": "Fri, 18 Aug 2017 09:58:50 GMT"
                },
                {
                  "name": "Content-Type",
                  "value": "text/html;charset=utf-8"
                },
                {
                  "name": "Content-Length",
                  "value": "3613"
                },
                {
                  "name": "Connection",
                  "value": "keep-alive"
                },
                {
                  "name": "Content-Encoding",
                  "value": "gzip"
                },
                {
                  "name": "Vary",
                  "value": "Accept-Encoding"
                },
                {
                  "name": "Set-Cookie",
                  "value": "session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70; expires=Fri, 17 Nov 2017 17:25:50 GMT; Path=/"
                },
                {
                  "name": "X-Clacks-Overhead",
                  "value": "GNU Terry Pratchett"
                }
              ],
              "cookies": [],
              "redirectURL": "",
              "headersSize": 368,
              "bodySize": 3613
            },
            "cache": {},
            "timings": {
              "blocked": 0,
              "dns": 0,
              "connect": 0,
              "send": 0,
              "wait": 328,
              "receive": 0
            },
            "serverIPAddress": "34.206.101.184",
            "connection": "80"
          }
        ]
      }
    }

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
            u'Accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            u'User-Agent': u'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
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
            u'Accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            u'User-Agent': u'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            u'Host': u'www.bgtrain.com',
            u'Referer': u'http://www.bgtrain.com/',
            u'Cookie': u'session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70',
            u'Upgrade-Insecure-Requests': u'1'},
    )

### As a module
    import harreplay
    print(harreplay.fobj_to_pystring(
        open('test_data/readme_example.har', 'rb'))
    import requests
    response = requests.post(
        u'http://www.bgtrain.com/',
    
        headers={
            u'Content-Length': u'25',
            u'Accept-Language': u'en-US,en;q=0.5',
            u'Accept-Encoding': u'gzip, deflate',
            u'Connection': u'keep-alive',
            u'Accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            u'User-Agent': u'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
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
            u'Accept': u'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            u'User-Agent': u'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            u'Host': u'www.bgtrain.com',
            u'Referer': u'http://www.bgtrain.com/',
            u'Cookie': u'session_id=b284c54d034935428eefa55c0ed5e3aabc1a4c70',
            u'Upgrade-Insecure-Requests': u'1'},
    )

### Warning
There are probably ways in which someone can mess you up if you run the code
that is produced by processing a HAR file from an untrusted source.
    
