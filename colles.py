import os

def compile_tex(name):
    os.system("pdflatex "+name+'.tex')
    # os.system("pdflatex "+name+'.tex')
    extension=['fdb_latexmk', 'fls', 'aux','log','out','toc']
    auxfile=[name+'.'+ext for ext in extension]
    for f in auxfile:
        os.system("mv "+f+" aux/")