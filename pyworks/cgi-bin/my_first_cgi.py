#!/usr/bin/env python

html_body = '''<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>CGI</title>
    </head>
    <body>
    My first CGI
    </body>
</html>'''

print('Content-type: text/html')
print('')
print(html_body)