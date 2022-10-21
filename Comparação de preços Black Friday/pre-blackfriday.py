import sqlite3
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

navegador = Chrome(service=Service(ChromeDriverManager().install()))

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

def listarProduto(url, categoria):
    navegador.get(url)
    time.sleep(5)
    produtos = navegador.find_elements(By.CSS_SELECTOR, 'div.sc-ff8a9791-7.dZlrn.productCard')
    for produto in produtos:
        item = produto.find_element(By.TAG_NAME, 'h2').text
        preco = produto.find_element(By.CSS_SELECTOR, 'span.sc-3b515ca1-2.jTvomc.priceCard').text
        sql = f'INSERT INTO {categoria} (item, preco) VALUES (?, ?)'
        valores = [item, preco]
        cursor.execute(sql, valores)

listarProduto('https://www.kabum.com.br/perifericos/headset-gamer?page_number=1&page_size=100&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiUkVERFJBR09OIiwiUmVkcmFnb24iXX0=&sort=most_searched', 'headsetpre')
listarProduto('https://www.kabum.com.br/hardware/ssd-2-5/ssd-sata?page_number=1&page_size=100&facet_filters=&sort=most_searched', 'ssdpre')
listarProduto('https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia?page_number=1&page_size=100&facet_filters=&sort=most_searched', 'placadevideopre')
listarProduto('https://www.kabum.com.br/perifericos/suportes/suporte-para-monitor?page_number=1&page_size=100&facet_filters=&sort=most_searched', 'suporteparamonitorpre')

navegador.close()
conexao.commit()
conexao.close()