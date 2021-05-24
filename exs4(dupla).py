import math

x1 = int(input(print('Valor de x do primeiro ponto: ')))
y1 = int(input(print('Valor de y do primeiro ponto: ')))

x2 = int(input(print('Valor de x do segundo ponto: ')))
y2 = int(input(print('Valor de y do segundo ponto: ')))

ponto1 = (x1, y1)
ponto2 = (x2, y2)

distancia = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(f'A distancia entre {ponto1} e {ponto2} é de {distancia}.')