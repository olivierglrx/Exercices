import os


def compile_tex(name):
    os.system("pdflatex "+name+'.tex')
    # os.system("pdflatex "+name+'.tex')
    extension=['fdb_latexmk', 'fls', 'aux','log','out','toc']
    auxfile=[name+'.'+ext for ext in extension]
    for f in auxfile:
        os.system("mv "+f+" aux/")


def compile_tex_moove_pdf(name):
    os.system("pdflatex "+name+'.tex')
    # os.system("pdflatex "+name+'.tex')
    extension=['pdf']
    auxfile=[name+'.'+ext for ext in extension]
    for f in auxfile:
        os.system("mv "+f+" pdf/")

def find_exercice(name):
    f=open('exercices/new/'+name)
    lines=f.readlines()
    i=0
    ideb,iend=0,0
    for line in lines:
        
        if "\\begin{exerci" in line:
            ideb=i+1
            print(line,i)
        if "\\end{exercic" in line:
            print(line)
            iend=i
        i=i+1
    return(lines[ideb:iend])
    
    

def transform_ex_to_preview():
    exercices=[f for f in os.listdir('exercices/new') if f[-3:]=='tex']

    already_treated=[f[:-3] for f in os.listdir('pdf')]
    
    for ex in exercices:
        if ex[:-3] in already_treated:
            pass
        else:
            try:
                
                exo_lines=find_exercice(ex)

                preambule=open('test.tex','r')
                p=preambule.read()
                create_tex=open('preview.tex','w')
                create_tex.write(p)
                create_tex.writelines(exo_lines)
                create_tex.write('\\end{preview}\n')
                create_tex.write('\\end{document}\n')
                preambule.close()
                create_tex.close()
                os.system("pdflatex "+'preview.tex')
                os.rename('preview.pdf', ex[:-4]+'.pdf' )
                os.system("mv " + ex[:-4]+'.pdf' + " pdf/")
            except Exception as e:
                create_log=open('notworking.txt','a')
                create_log.write(ex)


        
        
transform_ex_to_preview()












