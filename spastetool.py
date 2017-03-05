from Tkinter import *
import requests


def Quit(ev):
    global root
    root.destroy()


def Send(ev):
    user_key = '3051a3f3d2fd2ebc83212e5ebba55fcb'
    name = nameBox.get('1.0', 'end')
    lang = langBox.get('1.0', '3.0')
    priv = privBox.get('1.0', 'end')
    code = codeBox.get('1.0', 'end')

    '''$api_user_key.'&api_paste_private='.$api_paste_private.'&api_paste_name='.$api_paste_name.'&api_paste_expire_date='.$api_paste_expire_date.'&api_paste_format='.$api_paste_format.'&api_dev_key='.$api_dev_key.'&api_paste_code='.$api_paste_code.'');'''
    payload = {'api_option': 'paste',
               'api_dev_key': user_key,
               'api_paste_private': priv,
               'api_paste_name': name,
               'api_paste_code': code}

    r = requests.post("http://pastebin.com/api/api_post.php", data=payload)
    resBox.delete('1.0', 'end')
    resBox.insert('1.0', r.text)




root = Tk()

panelFrame = Frame(root, height=40, bg='gray')
textFrame = Frame(root, height=340, width=640)

panelFrame.pack(side='bottom', fill='x')
textFrame.pack(side='top', fill='both')

lCode = Label(textFrame, text='Paste your code here', font='Arial 12')
lCode.place(x=5, y=5, width=150, height=30)
codeBox = Text(textFrame, font='Arial 10', wrap='word')
codeBox.place(x=5, y=40, width=630, height=200)

lLang = Label(textFrame, text='Language: ', font='Arial 12')
lLang.place(x=5, y=250, width=80, height=30)
langBox = Text(textFrame, font='Arial 12')
langBox.place(x=90, y=250, width=150, height=25)

lName = Label(textFrame, text='Name: ', font='Arial 12')
lName.place(x=5, y=280, width=80, height=30)
nameBox = Text(textFrame, font='Arial 12')
nameBox.place(x=90, y=280, width=150, height=25)

lPriv = Label(textFrame, text='Private: ', font='Arial 12')
lPriv.place(x=5, y=310, width=80, height=30)
privBox = Text(textFrame, font='Arial 12')
privBox.place(x=90, y=310, width=150, height=25)
lPrivI = Label(textFrame, text='0 - public, 1 -unlisted, 2 - private', font='Arial 10')
lPrivI.place(x=245, y=310, width=200, height=30)

privBox = Text(textFrame, font='Arial 12')
privBox.place(x=90, y=310, width=150, height=25)

bSend = Button(panelFrame, text='Load')
bSend.place(x=5, y=5, width=90, height=30)
bSend.bind("<Button-1>", Send)

bQuit = Button(panelFrame, text='Quit')
bQuit.place(x=100, y=5, width=90, height=30)
bQuit.bind("<Button-1>", Quit)

resBox = Text(panelFrame, font='Arial 12')
resBox.place(x=385, y=8, width=250, height=25)


root.mainloop()