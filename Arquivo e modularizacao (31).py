import os
num: int =0
cont: int = 0
dir: str = ''
arq: str = ''
contp: int = 1

def grava(n):
    global contp
    global dir
    global arq
    dir = '/home/nathi/exercicios/'
    arq = 'Ex31.txt'
    os.makedirs(dir, exist_ok = True)
    os.chmod(dir, 0o744)
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(n) + '\n'
    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        if (os.path.exists(file)):
            tipo = 'a'
            if contp ==1:
                tipo = 'w'

        with open (file, tipo, encoding=enc) as file:
            file.write(linha)

    contp+=1



def main():
    global num
    global cont
    cont = 10
    while cont<=150:
        num = cont ** 2
        print (num)
        grava(num)
        cont +=1
        


if (__name__ == '__main__'):
    main()