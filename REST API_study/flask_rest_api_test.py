import requests
from bs4 import BeautifulSoup
# import pyautogui
import json
from class_test import NaverRestApi, DaumRestApi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/naver')
def json_endpoint1():
    return NaverRestApi.naver()

@app.route('/daum')
def json_endpoint2():
    return DaumRestApi.daum()

if __name__ == '__main__':
    # 애플리케이션 실행
    app.run()
