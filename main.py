import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from wordcloud import WordCloud
import platform
import copy

import start_screen

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
#from tkinter import ttk
#from tkinter import filedialog

from konlpy.tag import Hannanum
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from collections import Counter




from PIL import ImageGrab
from pandas import DataFrame

crawling_language = " "

input_url = " "

crawling_wordcase = " "

input_word_length = -1

crawling_graph = " "
crawling_graph_title = " "
file_data = " "

#크롤링인지 파일 탐색인지 선택하는 변수
search_method = "yes"
#제대로 파일이 디렉토리에서 선택되었는지 아는 변수
collect_directory = " "
if __name__ == "__main__":
    app = start_screen.start_screen()
    app.mainloop()



