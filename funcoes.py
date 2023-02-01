#funcoes.py
#uma funçao deve ter um objetivo unico a ser pequena
def rodar():
    print('rodando...')
def acelerar():
    print('acelerando... ran ran dandandan pah pah pah')

def abastecer(litros):
    preco = 5.5 #preco litro gasolina
    total = litros * preco
    
    print('abastecendo...', litros, 'litros por R$', total)

def contador():
    for x in range(10):
        print(x)
        
abastecer(50)
acelerar()
rodar()


contador()
