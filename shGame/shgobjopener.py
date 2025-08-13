class shg():
	def open():
		file=open("shg_objects.shf")
		l=list(map(str,(file.read()).split('\nEND\n')))
		a=[]
		for x in range(len(l)):
			a.append(list(map(str,l[x].split('\n'))))
		b=[]
		for x in range(len(l)):
			b.append([])
			for y in range(len(a[x])):
				b[x].append(list(map(str,a[x][y].split('_'))))
		c=[]
		for x in range(len(l)):
			c.append([])
			for y in range(len(a[x])):
				c[x].append([])
				for z in range(len(b[x][y])):
					c[x][y].append(list(map(str,b[x][y][z].split('^'))))
		return c
	
	def save(n,l):
		s=open('shg_objsave'+str(n)+'.shf','w')
		g=''
		for x in range(len(l)):
			for y in range(len(l[x])):
				for z in range(len(l[x][y])):
					for w in range(len(l[x][y][z])):
						g+=(l[x][y][z][w]+'^')
					g=g[:-1]
					g+=('_')
				g=g[:-1]
				g+=('\n')
			g=g[:-1]
			g+=('\nEND\n')
		g=g[:-5]
		s.write(g)
	
	def load(n):
		file=open('shg_objsave'+str(n)+'.shf')
		l=list(map(str,(file.read()).split('\nEND\n')))
		a=[]
		for x in range(len(l)):
			a.append(list(map(str,l[x].split('\n'))))
		b=[]
		for x in range(len(l)):
			b.append([])
			for y in range(len(a[x])):
				b[x].append(list(map(str,a[x][y].split('_'))))
		c=[]
		for x in range(len(l)):
			c.append([])
			for y in range(len(a[x])):
				c[x].append([])
				for z in range(len(b[x][y])):
					c[x][y].append(list(map(str,b[x][y][z].split('^'))))
		return c
print(shg.open()[1][11][0])
print(shg.open()[1][12][0])
#a=shg.open()
#shg.save(0,a)
#a=shg.load(0)