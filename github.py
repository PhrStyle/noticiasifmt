from git import Repo
import git
import os

#Função responsável por clonar o repositório remoto do GitHub
def git_clone():
    path = 'github'
    Repo.clone_from('https://github.com/nairamouras/instaview-dep', path)

#Função responsável por excluir o repositório clonado
def exclui_repositorio(path):
    if os.path.exists(path):
        git.rmtree(path)