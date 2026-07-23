# O que são testes?
# Testes garantem que o código está funcionando corretamente. Eles ajudam a:

# evitar erros
# validar funcionalidades
# facilitar manutenção

# Testes unitários

def soma(a,b):
    return a+b

# teste simples usando assert
assert soma(2,3) == 5 # testa a função soma() com 2+5, se o resultado for igual a 5, então é True, está funcionando. Se não for igual, o python vai dar erro

#----------------------------------------------------------------------------------------

# Usando pytest
# Pytest é uma ferramenta para criar testes automatizados
# todas as funções que forem criadas para teste devem ter o nome test (ou teste) no inicio para que o pytest reconheça que é um teste

def test_soma():
    assert soma(2,2) == 4

#----------------------------------------------------------------------------------------

# Refatoração
# Refatorar significa melhorar o código sem alterar seu funcionamento.

# refatorar neste caso seria melhorar o nome da função, pois calc pode significar várias coisas
def calc(a,b):
    return a+b

# refatorando...

def calcular_soma(numero1, numero2):
    return numero1 + numero2

# Em pipelines isso é muito importante

#---------------------------------------------------------------------------------------------

# esse exemplo também não está claro pra que serve
# essa função está percorrendo uma lista, selecionando os números maiores que 10 e multiplicando esses números por 2, retornando uma nova lista com os resultados
def processar(lista):
    resultado = []
    for i in lista:
        if i > 10:
            resultado.append(i*2)
    return resultado

# refatorando...

def processar_numeros(lista):
    return [numero * 2 for numero in lista if numero > 10]
    # o return dentro do [] para representar que está percorrendo dentro da lista

