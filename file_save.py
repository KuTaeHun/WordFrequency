#파일 경로를 세팅하고 저장하기 위한 함수 모음 패키지
import os

import docx2txt
from idlelib import window
import platform
from PIL import ImageGrab

import main

try:
    from tkinter import filedialog
    from tkinter import messagebox
    import tkinter.font
    import tkinter as tk
except:
    import Tkinter as tk
    import Tkinter.font
    from tkinter import filedialog
    from tkinter import messagebox

# txt 파일 불러오는 함수
def open_txt_file():

    # 운영체제마다 텍스트 파일 저장 방식이 다르기 때문
    os = platform.system()
    if os == "Windows":
        file_name = filedialog.askopenfile(initialdir="/", title="Select File", mode="r",
                                           filetypes=(("TXT Files", "*.txt"), ("all files", "*.*")))
    if os == "Darwin":
        file_name = filedialog.askopenfile(initialdir="/", title="Select File", mode = "r",
                                           filetypes=(("RTF Files", "*.rtf"), ("all files", "*.*")))
    #text_file = open(file_name)
    data = file_name.read()

    if data != "":
        global collect_directory
        main.collect_directory = "파일이 제대로 선택되어졌음."
        print(main.collect_directory)
    return data


def open_docx_file():

    file_name = filedialog.askopenfilename(initialdir="/", title="Select File",
                                           filetypes=(("DOCX Files", "*.docx"), ("all files", "*.*")))
    #file_name = filedialog.askdirectory(initialdir="/",title="불러올 문서 선택하기",filetypes=(("DOCX Files", "*.docx"), ("all files", "*.*")))
    #print(file_name.read())

    if file_name != '':

        main.collect_directory = "파일이 제대로 선택되어졌음."
        print(main.collect_directory)
    text_file = docx2txt.process(file_name)

    return text_file


def saved_image_file():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                            filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    file_direction = filename.readline()
    return  file_direction


# txt 파일 버튼
def click_callback_txt():

    main.file_data = open_txt_file()


# docs 파일 버튼
def click_callback_docx():
    main.file_data = open_docx_file()

def take_screenshot():
    x = window.winfo_rootx()  # 창의 왼쪽 위의 x 좌표
    y = window.winfo_rooty()  # 창의 왼쪽 위의 y 좌표
    w = window.winfo_width() + x
    h = window.winfo_height() + y

    box = (x, y, w, h)
    img = ImageGrab.grab(box)  # 창의 크기만큼만 이미지저장
    saves = main.crawling_graph_title+".jpg"

    img.save(saves)  # 이미지를 파일로 저장
