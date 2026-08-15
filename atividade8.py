n1 = int(input("Digite um numero"))
n2 = int(input("Digite um numero"))
n3 = int(input("Digite um numero"))
n4 = int(input("Digite um numero"))
n5 = int(input("Digite um numero"))

soma = n1 + n2 + n3 + n4 + n5

print(f'a soma de todos os numeros e:{soma}')

media = soma / 5 
print(f'a media dessa nota e {media}')











soma = 0
for nota in range(5):
    soma += int(input(f"Digite o {nota+1} número: "))
    
media = soma/5

print(f"a soma de todos os numeros e:{soma}")
print(f"A media dos numeros inseridos:{media:.2f}")




#n1 = float(input("Digite um numero"))
#n2 = float(input("Digite um numero"))
#n3 = float(input("Digite um numero"))
#n4 = float(input("Digite um numero"))
#n5 = float(input("Digite um numero"))

#soma = n1 + n2 + n3 + n4 + n5

#print(f'a soma de todos os numeros e:{soma}')

#media = soma / 5 
#print(f'a media dessa nota e {media}')
