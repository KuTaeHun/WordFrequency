#사용자가 원하는 방식으로 크롤링 세팅한 것을 결과를 보여주는 클래스
import _tkinter
import matplotlib.font_manager as fm
import numpy as np
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import platform

import analysis_file
import setting_crawling
import crawling_web
import main
import file_save


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

from collections import Counter

class result_web_crawling(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        result_check_label = tk.Label(self, text="다른 그래프를 만들기 위해서는 프로그램을 재시작 해주세요.")
        result_check_label.grid(row=0, column=0)
        previous_button = tk.Button(self, text="종료",
                                    command= self.quit())
        previous_button.grid(row=1, column=0)

        self.word_plot = []
        self.num_plot = []
        if main.crawling_language == '한국어':
            if main.search_method =="크롤링":
                self.text = crawling_web.crawling_korean(main.input_url)
            else:
                self.text = analysis_file.analysis_korean(main.file_data)
        elif main.crawling_language == '영어':
            if main.search_method =="크롤링":
                self.text = crawling_web.crawling_english(main.input_url)
            else:
                self.text = analysis_file.analysis_english(main.file_data)
        else:
            if main.search_method == "크롤링":
                self.text = crawling_web.crawling_hindi(main.input_url)
            else:
                self.text = analysis_file.analysis_hindi(main.file_data)

        self.length = int(main.input_word_length)

        self.count = Counter(self.text)

        self.result = self.count.most_common(self.length)

        for temp in self.result:
            temp_word = temp[0]
            temp_num = temp[1]
            self.word_plot.append(temp_word)
            self.num_plot.append(temp_num)

        self.data1 = {'단어': self.word_plot, '빈도': self.num_plot}
        self.df1 = DataFrame(self.data1, columns=['단어', '빈도'])

        # 운영체제마다 폰트가 다르기 때문에 선언
        os = platform.system()

        if main.crawling_language == '한국어':
            barfontsize = 20
        elif main.crawling_language == '영어':
            barfontsize = 20
        else:
            barfontsize =20

        title_font = {
            'fontsize': barfontsize,
            'fontweight': 'bold'
        }

        if main.crawling_graph == '막대 그래프':


            if os == "Windows":
                if main.crawling_language == '한국어':
                    plt.rc('font', family='Malgun Gothic')
                elif main.crawling_language == '힌디어':
                    plt.rc('font', family ="./Mukta-Medium.ttf")
            if os == "Darwin":
                if main.crawling_language == '한국어':
                    plt.rc("font", family="AppleGothic")
                elif main.crawling_language == '힌디어':
                    plt.rc('font', family="./DevanagariFont.otf")




            #
            # figure1 = Figure(figsize=(8, 6), dpi=80)
            # ax1 = figure1.add_subplot(111)
            # bar1 = FigureCanvasTkAgg(figure1, self)
            # bar1.draw()
            # bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            try:
                colors = ['black', 'dimgray', 'dimgrey', 'darkgray', 'silver', 'lightgrey']
                x = np.arange(self.length)
                plt.figure(figsize=(10, 8))
                plt.subplot(1,1,1)
                plt.bar(x, self.num_plot,color= colors,label = '빈도')

                if main.input_word_length >13:
                    plt.xticks(x, self.word_plot,rotation=90)
                else:
                    plt.xticks(x, self.word_plot)
                plt.autofmt_xdate(rotation=45)
                plt.title(main.crawling_graph_title, fontdict=title_font)

                plt.show()
                # self.df1 = self.df1[['단어', '빈도']].groupby('단어').sum()
                # self.df1.plot(kind='bar', legend=True, ax=ax1)
                # ax1.set_title(main.crawling_graph_title, fontsize=barfontsize)
                # file_save.take_screenshot()

            except _tkinter.TclError:
                tk.messagebox.showerror(title="종료", message="프로그램을 종료합니다.")
                self.destroy()
            except:
                tk.messagebox.showerror(title="오류", message="그래프가 생성되지 못했습니다.\n URL 혹은 파일을 확인하세요.")
                self.destroy()


        elif main.crawling_graph == '파이 그래프':
            try:
                if os == "Windows":
                    if main.crawling_language == '한국어':
                        plt.rc('font', family='Malgun Gothic')
                    elif main.crawling_language == '힌디어':
                        font_name = fm.FontProperties(fname="./Mukta-Medium.ttf", size=20)
                        plt.rc('font', family =font_name)
                if os == "Darwin":
                    if main.crawling_language == '한국어':
                        plt.rc("font", family="AppleGothic")
                    elif main.crawling_language == '힌디어':
                        font_name = fm.FontProperties(fname="./DevanagariFont.otf", size=20)
                        plt.rc('font', family=font_name)
                my_colors2 = ['lightblue', 'lightsteelblue', 'silver', 'bisque', 'moccasin', 'rosybrown', 'mistyrose',
                              'lightskyblue', 'linen', 'pink']

                x = np.arange(self.length)
                plt.figure(figsize=(8, 6))
                plt.subplot(1,1,1)
                plt.pie(self.num_plot, labels=self.word_plot,startangle=90,shadow=False,colors=my_colors2, autopct='%.1f%%')
                plt.title(main.crawling_graph_title, fontdict=title_font)
                plt.show().then(self.destroy())
                figure2 = Figure(figsize=(10, 8), dpi=100)
                ax2 = figure2.add_subplot(111)

                # self.df1 = self.df1[['단어','빈도']].groupby('단어').sum()
                # self.df1.plot(kind='line', legend=True, ax=ax2, color='b',marker='o', fontsize=10)
                # ax2.plot(self.word_plot,self.num_plot,color="blue", marker="x", linestyle="")
                # ax2.pie(self.num_plot, colors=my_colors2, labels=self.word_plot, autopct='%1.1f%%', shadow=True,
                #         startangle=90)
                # line1 = FigureCanvasTkAgg(figure2, self)
                # line1.draw()
                #
                # line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                # file_save.take_screenshot()
            except _tkinter.TclError:
                tk.messagebox.showerror(title="종료", message="프로그램을 종료합니다.")
                self.destroy()
            except:
                tk.messagebox.showerror(title="오류", message="그래프가 생성되지 못했습니다.\n URL 혹은 파일을 확인하세요.")
                self.destroy()


        else:


            if os == "Windows":
                if main.crawling_language == '한국어':
                    font = './SEBANG Gothic Bold.ttf'
                elif main.crawling_language == '힌디어':
                    font = './Muka-Mediium.ttf'
            if os == "Darwin":
                if main.crawling_language == '한국어':
                    font = './SEBANG Gothic OTF Bold.otf'
                elif main.crawling_language == '힌디어':
                    font = './DevanagariFont.otf'



            try:
                a = WordCloud(font_path=font, background_color="white", width = 1000, height = 600, max_words= self.length)
                a.generate_from_frequencies(dict(self.result))


                plt.figure(figsize=(10, 8))
                plt.imshow(a, interpolation='bilinear')
                plt.axis('off')
                plt.show().then(self.destroy())

            except _tkinter.TclError:
                tk.messagebox.showerror(title="종료", message="프로그램을 종료합니다.")
                self.destroy()
            except:
                tk.messagebox.showerror(title="오류", message="그래프가 생성되지 못했습니다.\n URL을 확인하세요.")
                self.destroy()
