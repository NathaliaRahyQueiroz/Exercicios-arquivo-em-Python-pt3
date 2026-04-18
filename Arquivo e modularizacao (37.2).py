import os

def validacao(n):
    if (n%2) != 0:
        return (n)
    else:
        return (-1)

def leitura(dir2, arq2):
    arquivo: str = ''
    num: int = 0
    arquivo = dir2 + arq2
    resultado: int = 0
    if (os.path.exists(dir2) and os.path.isdir(dir2)):
        with open (arquivo) as file:
            for linha in file:
                num = int(linha)
                resultado = validacao(num)
                if resultado != -1:
                    print (resultado)


    

def main():
    dir: str = ''
    arq: str = ''
    dir = '/home/nathi/exercicios/'
    arq = 'ex37.txt'
    leitura(dir, arq)
    



if __name__ == '__main__':
    main()