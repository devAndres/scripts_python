

FILE_INPUT = "datos.csv"
FILE_OUPUT = "datos_procesado.csv"

users = {}
colores = set()

with open( FILE_INPUT, 'r' ) as f:
    for line in f:
        line = line.strip()
        #primer_valor, delimitador, resto =  line.partition(';')
        name, _, color_pelo = line.split(';')
        users[name] = {'nombre': name, 'color_pelo': color_pelo}
        colores.add(color_pelo)

"""

for user, data in users.items():
    print(user)
    print(data)


for user in users:
    print('Usuario: %s' % user)
    print('Usuario: %s    Color pelo: %s' % (user, users[user]['color_pelo']))

    print('EL usuario {a} le gusta mucho el nombre {a} porque es {moreno}'.format(
        a=user,
        moreno=users[user]['color_pelo']
    ))

    print('EL usuario {0} le gusta mucho el nombre {1} porque es {2}'.format(
        user,
        user,
        users[user]['color_pelo']
    ))
"""


#print(colores)




import csv


