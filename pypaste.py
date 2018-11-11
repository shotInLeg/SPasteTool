#!/usr/bin/env python
# coding: utf8
import os
import click

import pastebin


PASTEBIN_TOKEN = '3051a3f3d2fd2ebc83212e5ebba55fcb'

PASTESERVICES = {
    'pastebin': pastebin.Pastebin(PASTEBIN_TOKEN)
}


def paste(service, file, name, lang, token=PASTEBIN_TOKEN):
    with open(file, 'r') as code:
        text = code.read()

    paste_service = PASTESERVICES[service]
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

