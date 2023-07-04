import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

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
    correcao_csv()

#Função que corrige e cria novo arquivo .csv com as notícias
def correcao_csv():
    #Abre o arquivo .csv atual apenas para leitura
    arquivo_noticias = 'noticias.csv'
    file = open(arquivo_noticias, 'r')
    linhas = file.readlines()
    qtd = 6
    file.close()
    #Cria novo arquivo para gravação
    new_file = open('noticias-ifmt.csv', 'w')
    #A intenção é manter apenas as 5 primeiras notícias (as principais da página inicial)
    for i in range(qtd):
        if i==0:
            #Ele pula a primeira linha, pois o arquivo original inicia com "0"
            new_file.writelines('')
        else:
            #Ele escreve no novo arquivo as linhas restantes
            novas_linhas = linhas[i]+' | '
            new_file.writelines(novas_linhas)
    new_file.close()
    #Exclui o arquivo .csv antigo, se ele existir
    if os.path.exists(arquivo_noticias):
        os.remove(arquivo_noticias)
