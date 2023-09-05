from git import Repo
import git
import os
import shutil

#Função responsável por clonar o repositório remoto do GitHub
def git_clone():
    path = 'static/github'
    Repo.clone_from('https://github.com/PhrStyle/noticiasarquivos', path)

def git_refresh():
    if os.path.exists('github/'):
        shutil.rmtree('github/')
    Repo.clone_from('https://github.com/PhrStyle/noticiasarquivos', 'github/')
    os.system('mv github/* static/github/')

#Função responsável por excluir o repositório clonado
def exclui_repositorio(path):
    if os.path.exists(path):
        git.rmtree(path)

