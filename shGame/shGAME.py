from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import os
import random

#import shgobjopener

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
		
	def loat(n):
		file=open('shg'+str(n)+'.shf')
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

w=Tk()
w.geometry("640x360")
w.title('Sh Game')


page=[-1,-1,-1,-1]
def pag1(a,b,c):
	global page
	page=[0,a,b,c]
def pag0():
	global page
	page=[-1,-1,-1,-1]
c=shg.open()
shrift=[7,10]

def vud(num,g,p):
		global c
		try:
			c[g][2][2][2]=c[g][14][p][num]
		except:
			pass
		try:
			c[g][2][2][0]=c[g][15][p][num]
		except:
			pass
		v.destroy()


luch=['l','t','u','g','tl','i']

zaza=50
#entr=askstring('diff', 'diff:')
#try:
#	if int(entr)<50:
#		pass
#	else:
#		zaza=int(entr)
#except:
#	pass

for x in range(zaza):
		for y in luch:
			if y=='u':
				for z in range(zaza):
#					exec('global '+y+c[x][0][0][0]+'_'+c[z][0][0][0])
					exec('def '+y+str(x)+'_'+str(z)+'():\n\t\t\t\t\t\tallall("'+y+'",'+str(x)+','+str(z)+')')
			else:
#				exec('global '+y+str(x))
				exec('def '+y+str(x)+'():\n\t\t\t\t\tallall("'+y+'",'+str(x)+',0)')

def allall(f,g,h):
	global b7
	global c
	global b6
	global page
	global shrift
	if f=='l':
		try:
			if c[g][3][0][0]!='':
				b7.destroy()
				b7=Label(w,text=c[g][3][0][0],font=('',shrift[0]))
				b7.grid(row=2,column=4)
				try:
					for y in range(len(c)-1):
						for z in range(len(c[g][4])):
							if c[g][4][z][0]==c[y][0][0][0]:
								if c[g][5][z][0]=='0' or c[g][5][z][0]=='-1' or c[g][5][z][0]=='1':
									c[y][2][0][0]=c[g][5][z][0]
								else:
									par(c[y][2],c[g][5][z][0])
				except:
					pass
			else:
				b7.destroy()
				b7=Label(w,text='Не получается рассмотреть',font=('',shrift[0]))
				b7.grid(row=2,column=4)
		except:
			b7.destroy()
			b7=Label(w,text='Не получается рассмотреть',font=('',shrift[0]))
			b7.grid(row=2,column=4)
	elif f=='t':
		try:
			if c[g][6][0][0]!='':
				b7.destroy()
				b7=Label(w,text=c[g][6][0][0],font=('',shrift[0]))
				b7.grid(row=2,column=4)
				try:
					for y in range(len(c)-1):
						for z in range(len(c[g][7])):
							if c[g][7][z][0]==c[y][0][0][0]:
								if c[g][8][z][0]=='0' or c[g][8][z][0]=='-1' or c[g][8][z][0]=='1':
									c[y][2][0][0]=c[g][8][z][0]
								else:
									par(c[y][2],c[g][8][z][0])
				except:
					pass
			else:
				b7.destroy()
				b7=Label(w,text='Не получается взять',font=('',shrift[0]))
				b7.grid(row=2,column=4)
		except:
			b7.destroy()
			b7=Label(w,text='Не получается взять',font=('',shrift[0]))
			b7.grid(row=2,column=4)
	elif f=='u':
		try:
			j=c[g][9].index([c[h][0][0][0]])
			b7.destroy()
			b7=Label(w,text=c[g][10][j][0],font=('',shrift[0]))
			b7.grid(row=2,column=4)
			try:
				for z in range(len(c[g][11][j])):
					for y in range(len(c)-1):
						if c[g][11][j][z]==c[y][0][0][0]:
							if c[g][12][j][z]=='0' or c[g][12][j][z]=='-1' or c[g][12][j][z]=='1':
								c[y][2][0][0]=c[g][12][j][z]
							else:
								par(c[y][2],c[g][12][j][z])
			except:
				pass
			try:
				if c[g][2][1][0]=='0':
					if c[g][2][2][0]=='1':
						if c[h][2][1][0]=='0':
							if c[h][2][2][0]=='1':
								shg.save('SLEEP',c)
			except:
				pass
		except:
			b7.destroy()
			b7=Label(w,text='Не получается так сделать',font=('',shrift[0]))
			b7.grid(row=2,column=4)
	elif f=='g':
		for x in range(len(c)-1):
			if c[x][2][1][0]=='-1':
				if c[x][2][0][0]=='-1':
					a=list()
					b=list()
					for y in range(len(c)-1):
						if c[y][2][0][0]=='-1' and c[y][2][1][0]!='-1':
							pass
						else:
							a.append(list(c[y][0][0]))
							b.append(list(c[y][2][0]))
					c[x][4]=list(a)
					c[x][5]=list(b)
		for x in range(len(c)-1):
			if c[x][2][1][0]=='-1':
				if c[x][2][0][0]=='-1':
					c[x][2][0][0]='0'
		c[g][2][0][0]='-1'
		next()
	elif f=='tl':
		try:
			p=int(c[g][2][2][0])
			try:
				if c[g][2][2][2]==str(p):
					global v
#					if v==Tk():
#						v.destroy()
					v=Tk()
#					v.post(w.x_root,w.y_root)
					v.title('Choice')
					for x in range(len(c[g][13][p])):
						exec('def vutt'+str(x)+'():\n\t\t\t\t\t\t\tvud('+str(x)+','+str(g)+','+str(p)+')')
					for x in range(len(c[g][13][p])):
						exec('vut'+str(x)+'=Button(v,text="'+c[g][13][p][x]+'",font=("",shrift[0]),command=vutt'+str(x)+')')
						exec('vut'+str(x)+'.grid(row='+str(x)+',column=0)')
				else:
					t4lk(g,h,p)
			except:
				t4lk(g,h,p)
		except:
			b7.destroy()
			b7=Label(w,text='Не получается поговорить',font=('',shrift[0]))
			b7.grid(row=2,column=4)
	elif f=='i':
		try:
			if c[g][3][0][0]!='':
				b7.destroy()
				b7=Label(w,text=c[g][3][0][0],font=('',shrift[0]))
				b7.grid(row=2,column=4)
			else:
				b7.destroy()
				b7=Label(w,text='Не получается рассмотреть',font=('',shrift[0]))
				b7.grid(row=2,column=4)
		except:
			b7.destroy()
			b7=Label(w,text='Не получается рассмотреть',font=('',shrift[0]))
			b7.grid(row=2,column=4)
	mmm()

def t4lk(g,h,p):
			global c
			global b7
			p0=int(c[g][2][2][1])
			b7.destroy()
			b7=Label(w,text=c[g][13][p][p0],font=('',shrift[0]))
			b7.grid(row=2,column=4)
			try:
				if c[g][13][p][p0+1]=='':
					c[g][2][2][0]=c[g][2][3][p]
					c[g][2][2][1]='0'
					for y in range(len(c)-1):
						for z in range(len(c[g][14][p])):
							if c[g][14][p][z]==c[y][0][0][0]:
								if c[g][15][p][z]=='0' or c[g][15][p][z]=='-1' or c[g][15][p][z]=='1':
									c[y][2][0][0]=c[g][15][p][z]
								else:
									par(c[y][2],c[g][15][p][z])
				else:
					c[g][2][2][1]=str(p0+1)
			except:
				c[g][2][2][0]=c[g][2][3][p]
				c[g][2][2][1]='0'
				try:
					for y in range(len(c)-1):
						for z in range(len(c[g][14][p])):
							if c[g][14][p][z]==c[y][0][0][0]:
								if c[g][15][p][z]=='0' or c[g][15][p][z]=='-1' or c[g][15][p][z]=='1':
									c[y][2][0][0]=c[g][15][p][z]
								else:
									par(c[y][2],c[g][15][p][z])
				except:
					pass

def par(a,b):
	try:
		a[int(b[0])][0]=int(a[int(b[0])][0])
		exec('a['+str(b[0])+'][0]'+str(b[1:]))
		a[int(b[0])][0]=str(a[int(b[0])][0])
		if a[4][1]==a[4][0]:
			for y in range(len(c)-1):
				for z in range(len(a[5])):
					if a[5][z]==c[y][0][0][0]:
						if a[6][z]=='0' or a[6][z]=='-1' or a[6][z]=='1':
							c[y][2][0][0]=a[6][z]
						else:
							par(c[y][2],a[6][z])
	except:
		pass

def next():
	global c
	global b2
	global b7
	global shrift
	for x in range(len(c)-1):
		if c[x][2][1][0]=='-1':
			if c[x][2][0][0]=='-1':
				b2.destroy()
				b2=Label(w,text=c[x][1][0][0],font=('',shrift[1]))
				b2.grid(row=1,column=4)
				b7.destroy()
				b7=Label(w,text=c[x][3][0][0],font=('',shrift[0]))
				b7.grid(row=2,column=4)
				for y in range(len(c)-1):
					for z in range(len(c[x][4])):
						if c[x][4][z][0]==c[y][0][0][0]:
							if c[y][2][1][0]!='-1' and c[y][2][0][0]=='-1':
								pass
							else:
								if c[x][5][z][0]=='0' or c[x][5][z][0]=='-1' or c[x][5][z][0]=='1':
									c[y][2][0][0]=c[x][5][z][0]
								else:
									par(c[y][2],c[x][5][z][0])
#			for y in range(len(c)-1):
#				for z in range(len(c[x][7])):
#					if c[x][7][z][0]==c[y][0][0][0]:
#						c[y][2][0][0]=c[x][8][z][0]
	mmm()

def msave():
	global c
	entry=askstring('Save', 'Save Number:')
	try:
		shg.save(int(entry),c)
		showinfo(title="Save", message='Saved!',icon='info')
	except:
		showinfo(title="Save", message='Error!',icon='warning')

def mload():
	global c
	entry=askstring('Load', 'Load Number:')
	try:
		c=shg.load(int(entry))
#		mogus()
		next()
		showinfo(title="Load", message='Loaded!',icon='info')
	except:
		showinfo(title="Load", message='Error!',icon='warning')
		
def sleepload():
	global c
	global b7
	entry = askyesno(title="Continue Game?", message="Are you sure you want to continue\ngame from last sleep?")
	if entry == True:
		try:
			c=shg.load('SLEEP')
#			mogus()
			next()
			b7.destroy()
			b7=Label(w,text='Вы проснулись',font=('',shrift[0]))
			b7.grid(row=2,column=4)
			showinfo(title="Continue Game?", message='Loaded!',icon='info')
		except:
			showinfo(title="Continue Game?", message='Error!',icon='warning')

def butt():
#	global c
#	global b7
#	global page
#	global shrift
#	if page[1]=='tl':
#		try:
#			b7.destroy()
#			b7=Label(w,text=c[page[2]][13][page[3]][page[0]],font=('',shrift[0]))
#			b7.grid(row=2,column=4)
#			if c[page[2]][13][page[3]][page[0]]=='':
#				for y in range(len(c)-1):
#					for z in range(len(c[page[2]][14][page[3]])):
#						if c[page[2]][14][page[3]][z]==c[y][0][0][0]:
#							c[y][2][0][0]=c[page[2]][15][page[3]][z]
#				c[page[2]][2][2][0]=c[page[2]][2][3][page[3]]
#				pag0()
#			else:
#				page[0]+=1
#		except:
#			b7.destroy()
#			b7=Label(w,text='',font=('',shrift[0]))
#			b7.grid(row=2,column=4)
#			for y in range(len(c)-1):
#				for z in range(len(c[page[2]][14][page[3]])):
#					if c[page[2]][14][page[3]][z]==c[y][0][0][0]:
#						c[y][2][0][0]=c[page[2]][15][page[3]][z]
#			c[page[2]][2][2][0]=c[page[2]][2][3][page[3]]
#			pag0()
#	elif page[1]=='f':
#		 pass
#	
	pass

def edit0r():
	entry = askyesno(title="To Editor", message="Do you want to open Editor?",detail="Game will be closed WITHOUT saving!\nIf you want to save game please do it\nat first!",icon='warning')
	if entry == True:
		w.destroy()
		import shgEDIT

def restart():
	global c
	entry = askyesno(title="Restart", message="Are you sure you want to restart?")
	if entry == True:
		try:
			c=shg.loat('_objects')
#			mogus()
			next()
			showinfo(title="Load", message='Loaded!',icon='info')
		except:
			showinfo(title="Load",message='Error!',icon='warning')

def quit():
	entry = askyesno(title="Quit", message="Are you sure you want to quit?")
	if entry == True:
		w.destroy()

def mlsc(a):
	global c
	entry = askyesno(title="Load", message="Do you want to load game?",detail="Game will be lost WITHOUT saving!\nIf you want to save game please do it\nat first!",icon='warning')
	if entry == True:
		try:
			c=shg.loat('_objects_'+a)
#			mogus()
			next()
			showinfo(title="Load", message='Loaded!',icon='info')
		except:
			showinfo(title="Load",message='Error!',icon='warning')

#MENU
def mmm():
	global shrift
	m=Menu(w)
	m2=Menu(m)
	mloads=Menu(m2)
	ml=Menu(m)
	mt=Menu(m)
	mu=Menu(m)
	mg=Menu(m)
	mtl=Menu(m)
	mi=Menu(m)

	
	m2.add_command(label='Save As',font=('',shrift[0]),command=msave)
	m2.add_command(label='Load As',font=('',shrift[0]),command=mload)
	m2.add_command(label='Load',font=('',shrift[0]),command=sleepload)
	try:
		ki=shg.loat('_series')
		for x in range(len(ki[0])):
			exec('mls'+str(x)+'=Menu(mloads)')
			kj=shg.loat('_series_'+ki[0][x][1][0])
			for y in range(len(kj[0])):
				exec('def mlsc'+kj[0][y][1][0]+'():\n\t\t\t\t\tmlsc("'+kj[0][y][1][0]+'")')
				exec('mls'+str(x)+'.add_command(label=kj[0][y][0][0],font=("",shrift[0]),command=mlsc'+kj[0][y][1][0]+')')
			exec('mloads.add_cascade(label=ki[0][x][0][0],font=("",shrift[0]),menu=mls'+str(x)+')')
	except:
		pass
	m2.add_cascade(label='Load Series',font=('',shrift[0]),menu=mloads)
	m2.add_command(label='Restart',font=('',shrift[0]),command=restart)
	m2.add_separator()
	m2.add_command(label='Editor',font=('',shrift[0]),command=edit0r)
	m2.add_command(label='Quit',font=('',shrift[0]),command=quit)
	m.add_cascade(label='Game',font=('',shrift[0]),menu=m2)
	for x in range(len(c)-1):
		if c[x][2][0][0]=='1' or (c[x][2][0][0]=='-1' and c[x][2][1][0]=='1'):
			if c[x][2][1][0]!='-1':
				exec('ml.add_command(label=c[x][1][0][0],font=("",shrift[0]),command=l'+c[x][0][0][0]+')')
	m.add_separator()
	m.add_cascade(label='Look',font=('',shrift[0]),menu=ml)
	for x in range(len(c)-1):
		if c[x][2][0][0]=='1':
			if c[x][2][1][0]=='0':
				exec('mt.add_command(label=c[x][1][0][0],font=("",shrift[0]),command=t'+c[x][0][0][0]+')')
	m.add_cascade(label='Take',font=('',shrift[0]),menu=mt)
	for x in range(len(c)-1):
		if c[x][2][0][0]!='0':
			if c[x][2][1][0]=='0':
				exec('mu'+c[x][0][0][0]+'=Menu(mu)')
				for y in range(len(c)-1):
					if c[y][2][0][0]!='0':
						if c[y][2][1][0]!='-1':
							exec('mu'+c[x][0][0][0]+'.add_command(label=c[y][1][0][0],font=("",shrift[0]),command=u'+c[x][0][0][0]+'_'+c[y][0][0][0]+')')
				exec('mu.add_cascade(label=c[x][1][0][0],font=("",shrift[0]),menu=mu'+c[x][0][0][0]+')')
	m.add_cascade(label='Use',font=('',shrift[0]),menu=mu)
	for x in range(len(c)-1):
		if c[x][2][0][0]=='1':
			if c[x][2][1][0]=='-1':
				exec('mg.add_command(label=c[x][1][0][0],font=("",shrift[0]),command=g'+c[x][0][0][0]+')')
	m.add_cascade(label='Go To',font=('',shrift[0]),menu=mg)
	for x in range(len(c)-1):
		if c[x][2][0][0]!='0':
			if c[x][2][1][0]=='1':
				exec('mtl.add_command(label=c[x][1][0][0],font=("",shrift[0]),command=tl'+c[x][0][0][0]+')')
	m.add_cascade(label='Talk',font=('',shrift[0]),menu=mtl)
	for x in range(len(c)-1):
		if c[x][2][0][0]=='-1':
			if c[x][2][1][0]=='0':
				exec('mi.add_command(label=c[x][1][0][0],font=("",shrift[0]),command=i'+c[x][0][0][0]+')')
	m.add_cascade(label='Inventory',font=('',shrift[0]),menu=mi)
	w.configure(menu=m)

mmm()

b1=Label(w,text='        ',font=('',shrift[1]))
b1.grid(row=1,column=3)
b2=Label(w,text='        ',font=('',shrift[1]))
b2.grid(row=1,column=4)
b3=Label(w,text='        ',font=('',shrift[1]))
b3.grid(row=2,column=3)
b4=Label(w,text='        ',font=('',shrift[0]))
b4.grid(row=2,column=4)
b5=Label(w,text='        ',font=('',shrift[1]))
b5.grid(row=0,column=3)
b6=Label(w,text='        ',font=('',shrift[1]))
b6.grid(row=0,column=5)
b7=Label(w,text='  tut  ',font=('',shrift[0]))
b7.grid(row=2,column=4)
b9=Button(w,text='            ©BreadmoundGames            ',font=('',shrift[0]),command=butt,state=DISABLED)
b9.grid(row=3,column=4)

next()


w.mainloop()