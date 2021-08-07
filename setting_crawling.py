# 사용자 설정에 맞는 크롤링을 하기 위해서 만든 클래스 모음
import main_screen
import main
import make_result_crawling
import copy

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


# 크롤링 언어 선택
class first_web_crawling(tk.Frame):
    def __init__(self, master):
        main.search_method = "크롤링"
        tk.Frame.__init__(self, master)
        first_screen_title_label = tk.Label(self, text="웹 문서 단어 빈도 분석")

        first_screen_title_label.grid(row=0, column=0)
        first_screen_explain_label = tk.Label(self, text="웹에서 무슨 언어를 크롤링할까요?")
        # frist_screen_explain_label.config(justify = CENTER)
        first_screen_explain_label.grid(row=1, column=0)
        self.listbox = tk.Listbox(self, selectmode='single', height=0)
        self.listbox.insert(0, "한국어")
        self.listbox.insert(1, "영어")
        self.listbox.insert(2, "힌디어")

        self.listbox.grid(row=2, column=0)

        self.listbox.bind('<<ListboxSelect>>', self.selectmotion)

        previous_button = tk.Button(self, text="이전",
                                    command=lambda: master.switch_frame(main_screen, main.crawling_language))
        previous_button.grid(row=3, column=0)
        next_button = tk.Button(self, text="다음",
                                command=lambda: master.switch_frame(second_web_crawling, main.crawling_language))
        next_button.grid(row=3, column=1)

    def selectmotion(self, event):
        selection = self.listbox.curselection()
        value = self.listbox.get(selection[0])
        global crawling_language
        main.crawling_language = copy.deepcopy(value)



# URL 입력창
class second_web_crawling(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        first_screen_title_label = tk.Label(self, text="URL 입력")

        first_screen_title_label.grid(row=0, column=0)

        self.url_blank = tk.Entry(self, width=50)
        self.url_blank.grid(row=1, column=0)
        confirm_button = tk.Button(self, text="확인", command=self.saved_url)
        confirm_button.grid(row=1, column=1)

        previous_button = tk.Button(self, text="이전", command=lambda: master.switch_frame(first_web_crawling, main.input_url))
        previous_button.grid(row=2, column=0)

        next_button = tk.Button(self, text="다음", command=lambda: master.switch_frame(third_web_crawling, main.input_url))
        next_button.grid(row=2, column=1)


    def saved_url(self):
        global input_url
        main.input_url = copy.deepcopy(self.url_blank.get())


# 형태소 분석
class third_web_crawling(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        if main.crawling_language == '한국어':
            first_screen_title_label = tk.Label(self, text="형태소 분석")

            first_screen_title_label.grid(row=0, column=0)
            first_screen_explain_label = tk.Label(self, text="해당 언어의 어떤 품사를 조사할까요?")
            # frist_screen_explain_label.config(justify CENTER)
            first_screen_explain_label.grid(row=1, column=0)
            self.listbox = tk.Listbox(self, selectmode='single', height=0)
            self.listbox.insert(0, "복합어")
            self.listbox.insert(1, "접사")
            self.listbox.insert(2, "파생어")

            self.listbox.grid(row=2, column=0)

            self.listbox.bind('<<ListboxSelect>>', self.selectmotion)

            second_screen_explain_label = tk.Label(self, text="최대 몇개까지 조사할까요? -최대 20개-")
            second_screen_explain_label.grid(row=3, column=0)
            self.Entryrange = tk.Entry(self, width=10)
            self.Entryrange.grid(row=4, column=0)
            try:
                confirm_button = tk.Button(self, text="확인", command=self.selectmotion_num)
            except IndexError:
                tk.messagebox.showerror(title="오류", message="리스트에 있는 항목을 정확히 클릭해주세요.")
            confirm_button.grid(row=4, column=1)

            previous_button = tk.Button(self, text="이전",
                                        command=lambda: master.switch_frame(second_web_crawling, main.crawling_wordcase))
            previous_button.grid(row=5, column=0)
            next_button = tk.Button(self, text="다음",
                                    command=lambda: master.switch_frame(forth_web_crawling, main.crawling_wordcase))
            next_button.grid(row=5, column=1)
        elif main.crawling_language =='영어':
            global crawling_wordcase
            main.crawling_wordcase = "영어는 선택 불가"
            first_screen_explain_label = tk.Label(self, text="최대 몇개까지 조사할까요? -최대 20개-")
            first_screen_explain_label.grid(row=0, column=0)
            self.Entryrange = tk.Entry(self, width=10)
            self.Entryrange.grid(row=1, column=0)

            confirm_button = tk.Button(self, text="확인", command=self.selectmotion_num)

            confirm_button.grid(row=1, column=1)

            previous_button = tk.Button(self, text="이전",
                                        command=lambda: master.switch_frame(second_web_crawling,
                                                                            main.crawling_wordcase))
            previous_button.grid(row=2, column=0)
            next_button = tk.Button(self, text="다음",
                                    command=lambda: master.switch_frame(forth_web_crawling, main.crawling_wordcase))
            next_button.grid(row=2, column=1)
        else:
            global crawling_wordcase
            main.crawling_wordcase = "힌디어는 선택 불가"
            first_screen_explain_label = tk.Label(self, text="최대 몇개까지 조사할까요? -최대 20개-")
            first_screen_explain_label.grid(row=0, column=0)
            self.Entryrange = tk.Entry(self, width=10)
            self.Entryrange.grid(row=1, column=0)

            confirm_button = tk.Button(self, text="확인", command=self.selectmotion_num)

            confirm_button.grid(row=1, column=1)

            previous_button = tk.Button(self, text="이전",
                                        command=lambda: master.switch_frame(second_web_crawling,
                                                                            main.crawling_wordcase))
            previous_button.grid(row=2, column=0)
            next_button = tk.Button(self, text="다음",
                                    command=lambda: master.switch_frame(forth_web_crawling, main.crawling_wordcase))
            next_button.grid(row=2, column=1)


    def selectmotion(self, event):
        selection = self.listbox.curselection()
        value = self.listbox.get(selection[0])
        global crawling_wordcase
        main.crawling_wordcase = value

    def confirmbutton(self):
        self.Entryrange.bind("<Return>", self.selectmotion_num)

    def selectmotion_num(self):
        global input_word_length
        main.input_word_length = copy.deepcopy(self.Entryrange.get())

        if int(main.input_word_length) > 20 or int(main.input_word_length) < 0:
            tk.messagebox.showwarning("범위 오류", "유효한 범위는 0~20입니다.\n범위를 다시 입력해주세요.")


# 그래프 선택 화면 클래스
class forth_web_crawling(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        first_screen_title_label = tk.Label(self, text="결과값 생성")

        first_screen_title_label.grid(row=0, column=0)
        first_screen_explain_label = tk.Label(self, text="무엇을 생성할까요?")
        # frist_screen_explain_label.config(justify CENTER)
        first_screen_explain_label.grid(row=1, column=0)
        self.listbox = tk.Listbox(self, selectmode='single', height=0)
        self.listbox.insert(0, "막대 그래프")
        self.listbox.insert(1, "파이 그래프")
        self.listbox.insert(2, "WordCloud")

        self.listbox.grid(row=2, column=0)

        self.listbox.bind('<<ListboxSelect>>', self.selectmotion)

        previous_button = tk.Button(self, text="이전",
                                    command=lambda: master.switch_frame(third_web_crawling, main.crawling_graph))
        previous_button.grid(row=3, column=0)
        next_button = tk.Button(self, text="다음",
                                command=lambda: master.switch_frame(fifth_web_crawling, main.crawling_graph))
        next_button.grid(row=3, column=1)

    def selectmotion(self, event):
        global crawling_graph
        selection = self.listbox.curselection()
        value = self.listbox.get(selection[0])
        main.crawling_graph = value


# 막대그래프, 파이 그래프 제목 입력창
class fifth_web_crawling(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        first_screen_title_label = tk.Label(self, text="해당 결과 그래프에 대한 제목을 정해주세요.")

        first_screen_title_label.grid(row=0, column=0)

        self.title_blank = tk.Entry(self, width=50)
        self.title_blank.grid(row=1, column=0)
        confirm_button = tk.Button(self, text="확인", command=self.set_title)
        confirm_button.grid(row=1, column=1)

        previous_button = tk.Button(self, text="이전",
                                    command=lambda: master.switch_frame(forth_web_crawling, main.crawling_graph_title))
        previous_button.grid(row=2, column=0)
        next_button = tk.Button(self, text="다음",
                                command=lambda: master.switch_frame(check_screen, main.crawling_graph_title))
        next_button.grid(row=2, column=1)

    def set_title(self):
        global crawling_graph_title
        main.crawling_graph_title = copy.deepcopy(self.title_blank.get())


class check_screen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        if main.search_method == "크롤링":
            first_screen_title_label = tk.Label(self, text="조건 확인창")

            first_screen_title_label.grid(row=0, column=0)

            first_label = tk.Label(self, text="선택하신 언어는: ")
            first_label.grid(row=1, column=0)
            language_label = tk.Label(self, text=main.crawling_language)
            language_label.grid(row=1, column=1)
            second_label = tk.Label(self, text="선택하신 URL는: ")
            second_label.grid(row=2, column=0)
            url_label = tk.Label(self, text=main.input_url)
            url_label.grid(row=2, column=1)
            third_label = tk.Label(self, text="선택하신 형태소는: ")
            third_label.grid(row=3, column=0)
            word_case_label = tk.Label(self, text=main.crawling_wordcase)
            word_case_label.grid(row=3, column=1)
            forth_label = tk.Label(self, text="선택하신 범위는: ")
            forth_label.grid(row=4, column=0)
            range_label = tk.Label(self, text=main.input_word_length)
            range_label.grid(row=4, column=1)
            fifth_label = tk.Label(self, text="선택하신 그래프는: ")
            fifth_label.grid(row=5, column=0)
            graph_label = tk.Label(self, text=main.crawling_graph)
            graph_label.grid(row=5, column=1)
            sixth_label = tk.Label(self, text="그래프의 제목은: ")
            sixth_label.grid(row=6, column=0)
            title_label = tk.Label(self, text=main.crawling_graph_title)
            title_label.grid(row=6, column=1)
            result_check_label = tk.Label(self, text="위 해당 조건이 맞습니까?")
            result_check_label.grid(row=7, column=0)
            previous_button = tk.Button(self, text="초기화", command=lambda: master.switch_frame(main_screen, main.crawling_graph))
            previous_button.grid(row=8, column=0)
            next_button = tk.Button(self, text="다음",
                                    command=lambda: master.switch_frame(make_result_crawling.result_web_crawling,
                                                                        main.crawling_graph))
            next_button.grid(row=8, column=1)
        else:
            first_screen_title_label = tk.Label(self, text="조건 확인창")

            first_screen_title_label.grid(row=0, column=0)

            first_label = tk.Label(self, text="선택하신 언어는: ")
            first_label.grid(row=1, column=0)
            language_label = tk.Label(self, text=main.crawling_language)
            language_label.grid(row=1, column=1)

            second_label = tk.Label(self, text="선택하신 형태소는: ")
            second_label.grid(row=2, column=0)
            word_case_label = tk.Label(self, text=main.crawling_wordcase)
            word_case_label.grid(row=2, column=1)
            third_label = tk.Label(self, text="선택하신 범위는: ")
            third_label.grid(row=3, column=0)
            range_label = tk.Label(self, text=main.input_word_length)
            range_label.grid(row=3, column=1)
            forth_label = tk.Label(self, text="선택하신 그래프는: ")
            forth_label.grid(row=4, column=0)
            graph_label = tk.Label(self, text=main.crawling_graph)
            graph_label.grid(row=4, column=1)
            fifth_label = tk.Label(self, text="그래프의 제목은: ")
            fifth_label.grid(row=5, column=0)
            title_label = tk.Label(self, text=main.crawling_graph_title)
            title_label.grid(row=5, column=1)
            result_check_label = tk.Label(self, text="위 해당 조건이 맞습니까?")
            result_check_label.grid(row=6, column=0)
            previous_button = tk.Button(self, text="초기화",
                                        command=lambda: master.switch_frame(main_screen, main.crawling_graph))
            previous_button.grid(row=7, column=0)
            next_button = tk.Button(self, text="다음",
                                    command=lambda: master.switch_frame(make_result_crawling.result_web_crawling,
                                                                        main.crawling_graph))
            next_button.grid(row=7, column=1)
