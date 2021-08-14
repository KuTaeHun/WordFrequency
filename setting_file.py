#텍스트 문서 혹은 워드 파일에 대해 사용자가 원하는 방향으로 세팅하는 패키지
import copy

import setting_crawling
from file_save import click_callback_txt, click_callback_docx
import main_screen
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


# 처음 화면 클래스
class first_screen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        first_screen_title_label = tk.Label(self, text="단어 빈도수 체크 프로그램")

        first_screen_title_label.grid(row=0, column=0)
        first_screen_explain_label = tk.Label(self, text="조사하고 싶은 파일을 업로드하시오. .docx, .txt만 가능")
        # frist_screen_explain_label.config(justify = CENTER)
        first_screen_explain_label.grid(row=1, column=0)
        txt_button = tk.Button(self, text="txt 파일 첨부", command=click_callback_txt)
        txt_button.grid(row=2, column=0)
        # txt_button.config(compound = LEFT)
        docx_button = tk.Button(self, text="docx 파일 첨부", command=click_callback_docx)
        docx_button.grid(row=2, column=1)
        previous_button = tk.Button(self, text="이전",height=1, command=lambda: master.switch_frame(main_screen,main.collect_directory))
        previous_button.grid(row=3, column=0)
        next_button = tk.Button(self, text="다음",height=1, command=lambda: master.switch_frame(second_screen,main.collect_directory))
        next_button.grid(row=3, column=1)
    # docx_button.config(compound = RIGHT)
    # confirm_button = ttk.Button(window,text="확인",command)

# 크롤링 언어 선택
class second_screen(tk.Frame):
    def __init__(self, master):
        main.search_method = "문서"
        tk.Frame.__init__(self, master)

        first_screen_title_label = tk.Label(self, text="문서 단어 빈도 분석")

        first_screen_title_label.grid(row=0, column=0)
        first_screen_explain_label = tk.Label(self, text="무슨 언어를 분석할까요?")
        # frist_screen_explain_label.config(justify = CENTER)
        first_screen_explain_label.grid(row=1, column=0)
        self.listbox = tk.Listbox(self, selectmode='single', height=0)
        self.listbox.insert(0, "한국어")
        self.listbox.insert(1, "영어")
        self.listbox.insert(2, "힌디어")

        self.listbox.grid(row=2, column=0)

        self.listbox.bind('<<ListboxSelect>>', self.selectmotion)

        previous_button = tk.Button(self, text="이전",height = 1,
                                    command=lambda: master.switch_frame(main_screen, main.crawling_language))
        previous_button.grid(row=3, column=0)
        next_button = tk.Button(self, text="다음",height = 1,
                                command=lambda: master.switch_frame(setting_crawling.third_web_crawling, main.crawling_language))
        next_button.grid(row=3, column=1)

    def selectmotion(self, event):
        selection = self.listbox.curselection()
        value = self.listbox.get(selection[0])
        global crawling_language
        main.crawling_language = copy.deepcopy(value)

