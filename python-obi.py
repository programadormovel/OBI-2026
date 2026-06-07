# Comentário de linha
'''
    Comentário 
        de 
            bloco
'''
"""
    Comentário de bloco 
        para documentação - Docstrings   
"""

# Declaração de variáveis
# nome = "João"   # literal ou texto (str)
# sobrenome = 'Silva'
# nome_completo = nome + " " + sobrenome
# idade = 74 # inteiro (int)
# altura = 1.75   # ponto flutuante (float)
# ocupado = True  # lógico (bool) = True ou False

# Tipo de dados
# print(type(nome))   # <class 'str'>
# print(type(idade))  # <class 'int'>
# print(type(altura)) # <class 'float'>   
# print(type(ocupado))    # <class 'bool'>    

# # Saída de dados
# print("Nome:", nome_completo, "!")
# print('Idade: '+ str(idade) + ' anos!') 
# print(f'Altura: {altura}m!')

# # Entrada de dados
# nome_usuario = input("Digite seu nome: ")
# print("Olá, " + nome_usuario + "! Seja bem-vindo(a)!")

# numero1 = int(input("Digite um número inteiro: "))
# numero2 = float(input("Digite um número decimal: "))    
# soma = numero1 + numero2
# print(f"A soma de {numero1} e {numero2} é: {soma}")

# condicionais
# estrutura condicional
# estrutura de decisão
# teste lógico
# if, elif, else
# '''Condicional simples'''
# if idade >= 18:
#     print("Você é maior de idade!") 
    
# Operadores relacionais | de comparação
# ==, !=, >, <, >=, <=
# Operadores lógicos
# and, or, not
# Operadores aritméticos
# +, -, *, /, //, %, **

# '''Condicional composta'''
# if idade >= 18:
#     print("Você é maior de idade!")
#     print("Você pode votar!")
# else:
#     print("Você não é maior de idade!")


# '''Condicional encadeada''' 
# if idade < 18:
#     print("Você é menor de idade!") 
# elif idade >= 18 and idade < 60:
#     print("Você é adulto!")
# else:
#     print("Você é idoso!")
    
# '''Condicional aninhada'''  
# if idade < 18:
#     print("Você é menor de idade!") 
# else:
#     if idade < 60:
#         print("Você é adulto!")
#     else:
#         print("Você é idoso!")
        
# laço de repetição
# # enquanto 
# while(idade <= 100):
#     print(f"Idade: {idade} anos!")
#     idade += 1  # idade = idade + 1 # incremento # idade -= 1  # idade = idade - 1 # decremento
# else:
#     print("Laço encerrado!")

# for indice in range(100): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 99   
#     print(f"Contagem: {indice}")

# listagem - estrutura de dados - coleção de dados
# lista = [1, 2, 3, 4, 5]
# for numero in lista:
#     print(f"Número: {numero}")

# tupla = (1, 2, 3, 4, 5) # tupla é imutável
# for numero in tupla:
#     print(f"Número: {numero}")

# lista = ['João', 'Maria', 'Pedro', 'Ana']
# tupla = ('João', 'Maria', 'Pedro', 'Ana')   

# print(lista[2])   # Pedro
# print(tupla[2])   # Pedro

# lista[2] = 'Simão'
# print(lista[2])   # Simão
# tupla[2] = 'Simão'   # TypeError: 'tuple' object does not support item assignment

# dicionário - dict
dicionario = {
    'nome': 'André',
    'sobrenome': 'Silva',
    'idade': 15,
    'altura': 1.75,
    'ocupado': True
}
print(dicionario['nome'])  # João
print(dicionario['idade'])  # 74

dicionario['nome'] = 'Simão'
print(dicionario['nome'])  # Simão

# conjunto - set
conjunto = {1, 2, 3, 4, 5}
print(conjunto)  # {1, 2, 3, 4, 5}
conjunto.add(6)
print(conjunto)  # {1, 2, 3, 4, 5, 6}
conjunto.remove(3)

lista = [1, 2, 3, 4, 5, 3, 2, 1]
print(lista)
lista.sort()  # ordena a lista
print(lista) 
lista.reverse()  # inverte a ordem da lista 
lista.append(6)  # adiciona um elemento no final da lista
print(lista)
lista.remove(3)  # remove a primeira ocorrência do elemento 3
print(lista)

