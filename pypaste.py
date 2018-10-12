#!/usr/bin/env python
# coding: utf8
import os
import click
import requests


PASTEBIN_TOKEN = '3051a3f3d2fd2ebc83212e5ebba55fcb'


class BasePasteService(object):
    def __init__(self, token, url):
        self.token = token
        self.url = url

    def paste(self, **kwargs):
        pass


class Pastebin(BasePasteService):
    def __init__(self, token):
        super(Pastebin, self).__init__(token, 'http://pastebin.com/api/api_post.php')

    def paste(self, text='Text', name='Paste from pypaste', lang='Python', private=0):
        payload = {
            'api_option': 'paste',
            'api_dev_key': self.token,
            'api_paste_private': private,
            'api_paste_name': name,
            'api_paste_code': text
        }
        
        response = requests.post(self.url, data=payload)
        return response.text


def paste(service, file, name, lang, token=PASTEBIN_TOKEN):
    with open(file, 'r') as code:
        text = code.read()

    paste_services = {
        'pastebin': Pastebin(token)
    }
    paste_service = paste_services[service]
    name = name or os.path.basename(file)

    url = paste_service.paste(text=text, name=name, lang=lang)
    return url


@click.command()
@click.argument('file')
@click.option('--service', default='pastebin', help='Name of paste service.')
@click.option('--name', default='', help='Name of paste.')
@click.option('--lang', default='Python', help='Syntax highlight language.')
def main(service, file, name, lang):
    print(paste(service, file, name, lang))


if __name__ == '__main__':
    main()

