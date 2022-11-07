import sqlite3
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

navegador = Chrome(service=Service(ChromeDriverManager().install()))

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

class produto():
    def __init__(self, url, categ):
        self.url = url
        self.categ = categ

    def listarProduto(self):
        navegador.get(self.url)
        time.sleep(5)
        produtos = navegador.find_elements(By.CSS_SELECTOR, 'div.sc-ff8a9791-7.dZlrn.productCard')
        for produto in produtos:
            item = produto.find_element(By.TAG_NAME, 'h2').text
            preco = float(produto.find_element(By.CSS_SELECTOR, 'span.sc-3b515ca1-2.jTvomc.priceCard').text.replace("R$ ", "").replace(".", "").replace(",", "."))
            categoria = self.categ
            sql = f'INSERT INTO posblackfriday (categoria, item, preco) VALUES (?, ?, ?)'
            valores = [categoria, item, preco]
            cursor.execute(sql, valores)

link_headset = produto("https://www.kabum.com.br/perifericos/headset-gamer/com-fio?page_number=1&page_size=100&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiUmVkcmFnb24iLCJSRUREUkFHT04iXX0=&sort=most_searched", "headset")
link_gabinete = produto("https://www.kabum.com.br/perifericos/gabinetes/gabinete-mid-tower?page_number=1&page_size=100&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiUmVkcmFnb24iXX0=&sort=most_searched", "gabinete")
link_gpu = produto("https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=100&facet_filters=eyJNZW3Ds3JpYSI6WyI4IEdCIiwiMTIgR0IiXX0=&sort=most_searched", "gpu")
link_ssd = produto("https://www.kabum.com.br/hardware/ssd-2-5/ssd-sata?page_number=1&page_size=100&facet_filters=&sort=most_searched", "ssd")
link_mesa = produto("https://www.kabum.com.br/espaco-gamer/mesa-gamer?page_number=1&page_size=100&facet_filters=&sort=most_searched", "mesa")

lista = [link_headset, link_gabinete, link_gpu, link_ssd, link_mesa]

for i in lista:
    i.listarProduto()

navegador.close()
conexao.commit()
conexao.close()