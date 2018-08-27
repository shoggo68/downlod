#coding:utf-8
from pytube import YouTube
import tkinter as tk
import tkinter.messagebox as tmsg



def download():
    youtube = editbox.get()
    url = YouTube(youtube)
    url.streams.first().download()
    tmsg.chowerror("完了", "ダウンロードが完了しました")

#ウィンドウを表示
root = tk.Tk()
root.geometry('400x300')
root.title("動画ダウンロードプログラム")

#ラベルを作る
labell = tk.Label(root, text='URLを入力', font=('Helvetica', 14))
labell.place(x = 20, y = 20)

#テキストボックス
editbox = tk.Entry(width = 40)
editbox.place(x = 90, y = 60)

#ボタンを作る
button1 = tk.Button(root, text = "ダウンロード開始", font =("Helvetica", 14),
                    command=download)
button1.place(x = 90, y = 100)

#ウィンドを表示する
root.mainloop()
