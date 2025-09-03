import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from time import sleep
#from VendaDireta import VendaDireta
import pandas as pd
from logger import *
from datetime import datetime

log = logg()

#Aqui, o script configura as opções para o WebDriver do Chrome. 
#Ele desativa as barras de informação, extensões, 
#bloqueio de popup e inicia o navegador maximizado. 
#Ele também define as preferências para o download de arquivos.

dataAtual = datetime.now().strftime("%d/%m/%Y")
dataInicio = datetime.now().strftime("01/%m/%Y")

options = Options()

options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("disable-popup-blocking")
options.add_argument("start-maximized")

# Leitura dos dados da planilha
    
driver = ChromeDriverManager().install()
driver = os.path.join(os.path.dirname(driver),'chromedriver.exe') if os.path.basename(driver) != 'chromedriver.exe' else driver
service = Service(driver)

nav = webdriver.Chrome(service=service,options=options)

#URL do site
nav.get('https://viasulroute.syonet.com/portal/app.do?modulo=login#/login')

#Login no site
WebDriverWait(nav, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div/form/div[1]/div/input'))).send_keys('carlos.costa')
sleep(0.5)
nav.find_element(By.XPATH,'/html/body/div/main/div[1]/div/form/div[2]/div/input').send_keys('Q!W@E#R$T%q1w2e3r4t5')

#Botão de Entrar
nav.find_element(By.XPATH,'/html/body/div/main/div[1]/div/form/button').click()

#botão gestão
WebDriverWait(nav, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/button[4]'))).click()
sleep(1)

#botão dashboard
nav.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/a[2]/button').click()

sleep(1)
WebDriverWait(nav, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/iframe')))
sleep(1)
#pesquisar pelo relatório 
nav.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/input').send_keys('[ VENDAS ] - KPI - Fluxo de Loja - Diário')
sleep(1)

#pesquisar
WebDriverWait(nav, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/button[1]'))).click()
sleep(3)

#entrando no relatório (KPI FLUXO DE LOJA)
WebDriverWait(nav, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '[ VENDAS ] - KPI - Fluxo de Loja - Diário')]"))).click()
sleep(1)

#selecionar filtro (Tipo de venda - venda direta)
WebDriverWait(nav, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[6]/div/div/ul/li[4]'))).click()
sleep(1)

#retirando filtro "todos" no "Tipo Evento"
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[8]/div/div/ul/li[1]/label').click()
sleep(1)

#selecionando fitro "novos web" no "Tipo Evento"
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[8]/div/div/ul/li[48]/label').click()
sleep(1)

#selecionando fitro "novos web Facebook" no "Tipo Evento"
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[8]/div/div/ul/li[49]/label').click()
sleep(1)

#retirando fitro "Marcar Todos" em "Empresa"
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[1]/div/div/ul[1]/li/label').click()
sleep(1)

#Selecionando o filtro "Bajaj" em "Empresa"
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[1]/div/div/ul[2]/li[1]/label').click()
sleep(1)

nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input').clear()
sleep(1)
#Selecionando a data inicio 
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[2]/div/div/input').send_keys(dataInicio)

#Selecionando a data atual 
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[1]/div[2]/div/div[3]/div/div/input').send_keys(dataAtual)

#Selecionando "Aplicar Filtro"
nav.find_element(By.XPATH, '/html/body/div[6]/div[2]/form/div[2]/button[1]').click()
sleep(1)
