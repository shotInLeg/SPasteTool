# coding: utf8
import basepasteservice


class Pastebin(basepasteservice.BasePasteService):
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

        response = self.post(self.url, payload)
        return response.text

