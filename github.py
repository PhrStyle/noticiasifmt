from git import Repo
import git
import os
import shutil

#Função responsável por clonar o repositório remoto do GitHub
def git_clone():
    path = 'static/github'
    Repo.clone_from('https://github.com/nairamouras/instaview-dep', path)

def git_refresh():
    if os.path.exists('/noticiasifmt/github/'):
        shutil.rmtree('/noticiasifmt/github/')
    Repo.clone_from('https://github.com/nairamouras/instaview-dep', '/noticiasifmt/github/')
    os.system('mv /noticiasifmt/github/* /noticiasifmt/static/github/')

#Função responsável por excluir o repositório clonado
def exclui_repositorio(path):
    if os.path.exists(path):
        git.rmtree(path)


git_refresh()
