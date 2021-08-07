#from setting_crawling import first_web_crawling
import main
import setting_crawling
import setting_file

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

class main_screen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        first_screen_title_label = tk.Label(self, text="단어 빈도수 체크 프로그램")

        first_screen_title_label.grid(row=0, column=0)
        first_screen_explain_label = tk.Label(self, text="무엇을 조사하고 싶나요? 1. 웹 문서 2. 파일 문서")
        # frist_screen_explain_label.config(justify = CENTER)
        first_screen_explain_label.grid(row=1, column=0)


        explain_this_program = tk.Label(self,text="<--주의사항-->")
        explain_this_program.grid(row=2,column=0)
        first_explain = tk.Label(self, text="1.윈도우 전용 프로그램입니다. 리눅스,MAC에서는 오류가 날 수 있습니다.\n2.입력하고나서 꼭 확인 버튼을 눌러주세요.\n"
                                            "3.웹 크롤링시 대부분의 에러는 URL 주소가 정확하지 않은 경우입니다.\n4.웹 크롤링시 꼭 URL은 https:// 로 시작해야합니다.\n"
                                            "5.파일 분석시 *.txt,*.docx만 가능합니다. (*.doc,한글 파일,파워포인트,pdf 불가능)\n6.힌디어,한국어,영어 단어 빈번도를 조사할 수 있습니다.")
        first_explain.grid(row=3, column=0)
        copyright_explain = tk.Label(self, text="<--저작권 및 참고 패키지-->")
        copyright_explain.grid(row=4,column=0)
        first_copyright_explain = tk.Label(self,text="1.논문 및 학업 도움을 위해 만든 무료 프로그램입니다. 따라서 판매는 불가능합니다.\n"
                                                     "2.한국어 형태소 분석 - KONPLY\n3.힌디어 분석 - iNLTK\n4.영어 분석 - NLTK\n5.제작자:) 구태훈(Caleb TaeHun Ku)")
        first_copyright_explain.grid(row=5,column=0)
        web_button = tk.Button(self, text="웹 문서", command=lambda: master.switch_frame(setting_crawling.first_web_crawling, main.search_method))
        web_button.grid(row=6, column=0)
        # txt_button.config(compound = LEFT)
        file_button = tk.Button(self, text="파일 문서", command=lambda: master.switch_frame(setting_file.first_screen, main.search_method))
        file_button.grid(row=6, column=1)