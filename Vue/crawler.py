from bs4 import BeautifulSoup
from app.lib.lib import delay, sortUserAgent
import requests
import re
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
import tabulate

cls = os.system('cls')
dir = os.system('dir')
delay

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://loterias.caixa.gov.br/Paginas/default.aspx')
    sleep(2)
    pagina.locator('xpath=//*[@id="ctl48_g_02bfeca0_05ba_4876_bea5_5efdfa91f8e3"]/div/div[2]/div[1]/div[2]/p[3]/a').click()
    sleep(2)
    
    a = pagina.locator('xpath=//*[@id="WebPartWPQ3"]').all_text_contents()
    with open('teste1.html', 'w', encoding='utf-8') as arquivo:
        arquivo.write(str(a))

    navegador.close()

