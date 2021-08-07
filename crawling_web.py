
from konlpy.tag import Hannanum
import requests
from bs4 import BeautifulSoup
import re
from  nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
# 한국어 형태소 분석하는 함수
import main
#힌디어 형태소 분석하는 함수
from inltk.inltk import setup
from inltk.inltk import tokenize



def crawling_korean(url):
    html = requests.get(url)
    text = BeautifulSoup(html.text, 'html.parser')
    # text = soup.select_one('.cs_body > .cs_view.text > .text')
    text = text.get_text(' ', strip=True)
    text = re.sub('[0-9]+', '', text)
    text = re.sub('[A-Za-z]+', '', text)
    text = re.sub('[-=+,#/\?:°;↖︎©\ⓒ^$.@*\"※~&%ㆍ★·!』_｜…》]', '', text)
    special = re.compile(r'[^ A-Za-z0-9가-힣+]')
    text = special.sub('', text)
    text = text.strip()

    if main.crawling_wordcase == '복합어':
        hannanum = Hannanum()

        text_list = hannanum.nouns(text)

    elif main.crawling_wordcase == '접사':
        hannanum = Hannanum()
        text_list = hannanum.morphs(text)
    else:
        hannanum = Hannanum()
        text_list = hannanum.pos(text)
    return text_list

def crawling_english(url):
    html = requests.get(url)
    text = BeautifulSoup(html.text, 'html.parser')

    text = text.get_text(' ', strip=True)
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()


    # 불용어 제거
    stops = set(stopwords.words('english'))
    no_stops = [word for word in text if not word in stops]

    # 어간 추출
    stemmer = nltk.stem.SnowballStemmer('english')
    stemmer_words = [stemmer.stem(word) for word in no_stops]

    return stemmer_words

def crawling_hindi(url):
    html = requests.get(url)
    text = BeautifulSoup(html.text, 'html.parser')
    # text = soup.select_one('.cs_body > .cs_view.text > .text')
    text = text.get_text(' ', strip=True)
    text = re.sub(r"[^\u0900-\u097F]+", "", text)
    # text = re.sub('[0-9]+', '', text)
    # text = re.sub('[A-Za-z]+', '', text)
    # text = re.sub('[-=+,#/\?:°;↖︎©\ⓒ^$.@*\"※~&%ㆍ★·!』_｜…》]', '', text)
    setup('hi')
    text = tokenize(text,'hi')
    return text
