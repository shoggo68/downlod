# -*- coding: utf-8 -*-
import requests as web
import bs4
import csv
import tkinter as tk


def ApointmentList():
    Sarch_Word = editbox.get().split()
    File_mei = str(File_Name.get())
    # キーワードを使って検索するse
    list_keywd = Sarch_Word
    resp = web.get('https://www.google.co.jp/search?num=1000&q=' + '　'.join(list_keywd))
    resp.raise_for_status()

    # 取得したHTMLをパースする
    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    # 検索結果のタイトルとリンクを取得
    link_elem01 = soup.select('.r > a')
    # 検索結果の説明部分を取得
    link_elem02 = soup.select('.s > .st')

    if(len(link_elem02) <= len(link_elem01)):
        leng = len(link_elem02)
    else:
        leng = len(link_elem01)

    # CSVファイルを書き込み用にオープンして整形して書き出す
    with open( File_mei + '.csv','w',newline='',encoding='utf-16') as outcsv:
        csvwriter = csv.writer(outcsv)
        for i in range(leng):
            # リンクのみを取得し、余分な部分を削除する
            url_text = link_elem01[i].get('href').replace('/url?q=','')
            #　URLから jp　or com　までのインデックスを取得
            if 'com/' in url_text:
                index = url_text.find('com/')
            elif 'jp/' in url_text:
                index = url_text.find('jp/')
            title_text = link_elem01[i].get_text()
            csvwriter.writerow([title_text])
            if 'com/' in url_text:
                csvwriter.writerow([url_text[0:index + 3]])
            elif 'jp/' in url_text:
                csvwriter.writerow([url_text[0:index + 2]])
            else:
                csvwriter.writerow([url_text[0:30]])
        outcsv.close()

root = tk.Tk()
root.geometry('400x200')
root.title("アポリス君 -ALM MK-Ⅳ-")

#ラベルを作る
labell = tk.Label(root, text='Sarch Word', font=('Helvetica', 12))
labell.place(x = 20, y = 15)

#テキストボックス
editbox = tk.Entry(width = 40)
editbox.place(x = 90, y = 40)

#ファイル名のラベル
f_name = tk.Label(root, text='File Name', font=('Helvetica', 12))
f_name.place(x = 20, y = 65)

#ファイルテキスト
File_Name = tk.Entry(width = 40)
File_Name.place(x = 90, y = 90)


button1 = tk.Button(root, text = "作成", font =("Helvetica", 14),
                    command=ApointmentList)
button1.place(x = 180, y = 130)

root.mainloop()

