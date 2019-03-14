
a = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
x = []

for i in range(0,10) :
    y = []
    for j in range(0,10) :
        y.append('%s%s' % (j,a[i]))

    x.append( y )

for i in x :
    print( i )

#
#
#

z = []
for i in range( 0,10 ) :
    z.append(i)

d = dict(zip(a,z))
for i, j in d.items() :
    print('%s %s' % (i,j))


"""

s = []

s['a'] = 'HOLA'
s['b'] = 'csdcsd'

for i in s :
    print(i)
"""
