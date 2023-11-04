#Capitulo 4 Funcoes e modulos

#def funcao(<parametros>):

def calcular_desconto(valor, desconto):
    vlr_desconto = valor * desconto / 100
    return vlr_desconto
def totalizar_item(vlr_unit, quantidade):
    valor_total = vlr_unit * quantidade
    return valor_total

produto_a = calcular_desconto(1500,20)
print(produto_a)