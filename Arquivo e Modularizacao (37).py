import os
contf: int = 1

def grava(num):
    global contf
    dir: str = ''
    arq : str = ''
    dir = '/home/nathi/exercicios/'
    arq = 'ex37.txt'
    os.makedirs(dir, exist_ok = True)
    os.chmod(dir, 0o744)
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''
    linha = str(num) + '\n'
    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        file = dir + arq
        enc = 'utf-8'
        if (os.path.exists(file)):
            tipo = 'a'
            if contf == 1:
                tipo = 'w'
        with open (file, tipo, encoding=enc) as file:
            file.write(linha)
    
            

    contf +=1

def main():
    termo: int = 0
    termo = int(input("Digite a quatidade de termos da sequência: "))
    cont: int = 1
    a: int = 0
    b: int = 1
    c: int = 0   
    while cont <= termo:
        if cont == 1:
            print(b)
            grava(b)

        if cont >= 2:
            c = a+b
            print(c)
            grava(c)
            a = b
            b = c

        cont +=1



if (__name__ == '__main__'):
    main()