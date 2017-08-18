"""
Converts a HAR file (which contains a sequence of HTTP requests) into
a Python script that performs the same requests via the
"requests" module.
"""

import argparse
import collections
import json
import os
import string
import urllib

SEP = os.linesep

fn='Archive 17-08-17 22-30-48.har'

def fobj_to_pystring(fobj):
    result_lines = [
        'import requests',
    ]

    for entry in json.load(fobj)['log']['entries']:
        request_el = entry['request']
        method = request_el['method']
        url = request_el['url']
        data = None
        if 'postData' in request_el:
            if 'text' in request_el['postData']:
                data = request_el['postData']['text']
            elif 'params' in request_el['postData']:
                raise NotImplementedError(
                    "Haven't seen 'params' in the wild yet.")
        data = data or None
        headers = dict(
            (d['name'], d['value']) for d in request_el['headers'])
        call_code_format = (
            'response = requests.{method}({args}{sep})'
        )
        arg_lines = [
            '{sep}    {url},'.format(
                sep = SEP,
                url = repr(url),
            ),
            '{sep}    headers={headers},'.format(
                sep = SEP,
                headers = repr(headers)
            ) if headers else None,
            '{sep}    data={data},'.format(
                sep = SEP,
                data = repr(data)
            ) if data else None,
        ]
        call_code = call_code_format.format(
            sep = SEP,
            method = method.lower(),
            args = SEP.join(l for l in arg_lines if l),
        )
        result_lines.append(call_code)

    result = SEP.join(result_lines)

    try:
        import autopep8
        result = autopep8.fix_code(
            result, options={'aggressive': 1})
    except ImportError as e:
        pass

    return result

def main():
    parser = argparse.ArgumentParser(
        description = ('Open a HAR file (that can be exported by '
                       'Firefox or Chrome "Inspect") and write a '
                       'python script that performs the same '
                       'HTTP requests using the Python "requests" '
                       'module.')
    )
    parser.add_argument(
        '-i',
        dest = 'infile',
        default = '-',
        type = argparse.FileType('rb'),
    )
    parser.add_argument(
        '-o',
        dest = 'outfile',
        default = '-',
        type = argparse.FileType('wb'),
    )
    args = parser.parse_args()

    args.outfile.write(fobj_to_pystring(args.infile))

if __name__ == '__main__':
    main()
