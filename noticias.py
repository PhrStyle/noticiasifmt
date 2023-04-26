import requests
from bs4 import BeautifulSoup
import pandas as pd
import correcao_arquivo_csv

#Função responsável por executar o Web Scraping da página de notícias do IFMT
def scraping_noticias():
    lista_noticias = []
    #URL da página de notícias do IFMT a ser requisitada
    response = requests.get('https://cba.ifmt.edu.br/conteudo/noticias/')
    content = response.content
    #Faz a busca através das tags HTML da página
    site = BeautifulSoup(content, 'html.parser')
    noticias = site.findAll('div', attrs = {'class':'small-12 columns borda-esquerda'})
    for noticia in noticias:
        titulo = noticia.find('p', attrs= {'class':'no-margin espacamento-medio'})
        #Cria uma lista com todos os títulos das notícias encontrados     
        lista_noticias.append([titulo.text])
    news = pd.DataFrame(lista_noticias)
    #Cria um arquivo .csv para armazenar os títulos
    news.to_csv('noticias.csv', index=False)
    #Chama a função de correção das falhas no arquivo .csv
    correcao_arquivo_csv.correcao_csv()