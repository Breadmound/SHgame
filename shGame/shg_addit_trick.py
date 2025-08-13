a=[['0'],['0'],['',''],[''],['0'],['45']]
b='4+=1'
for x in range(5):
	a[int(b[0])][0]=int(a[int(b[0])][0])
	exec('a['+str(b[0])+'][0]'+str(b[1:]))
	a[int(b[0])][0]=str(a[int(b[0])][0])
print(a,b)