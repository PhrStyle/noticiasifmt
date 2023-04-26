import os

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