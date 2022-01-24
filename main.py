from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

navegador = webdriver.Firefox()

link = 'https://br.pinterest.com/login/'
navegador.get(url=link)

email = ''
senha = ''

campo_email = navegador.find_element(By.CSS_SELECTOR, "#email")
sleep(1)
campo_email.send_keys(email)

campo_senha = navegador.find_element(By.CSS_SELECTOR, "#password")
sleep(1)
campo_senha.send_keys(senha)

botao_entrar = navegador.find_element(By.CSS_SELECTOR, '.red')
sleep(0.5)
botao_entrar.click()