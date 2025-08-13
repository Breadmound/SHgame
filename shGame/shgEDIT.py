from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
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
		if n==l:
			s=open('shg_'+str(n[0])+'.shf','w')
			l=n[1]
		else:
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
w.geometry("640x720")
w.title('Sh EDITOR')


page=[-1,-1,-1,-1]
def pag1(a,b,c):
	global page
	page=[0,a,b,c]
def pag0():
	global page
	page=[-1,-1,-1,-1]
#c=shg.open()
d=shg.loat('_obj_info')
c=shg.loat('_objects')
shrift=[7,10]
edit=None
ch=0
k=None
ff=None
fname="shg_objects.shf"

def c1():
	pass
def c2():
	pass
def c3():
	pass
def c4():
	pass
def c5():
	pass
def c6():
	pass
def c7():
	pass
def c8():
	pass
def c9():
	pass

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
		showinfo(title="Load", message='Loaded!',icon='info')
		next()
	except:
		showinfo(title="Load", message='Error!',icon='warning')

def madd():
	global edit
	global k
	global c
	try:
		edit=0
		ent1.delete(0,END)
		u=0
		for x in range(len(c)):
			if c[x][0][0][0]==str(x):
				u+=1
		ent1.insert(0,u)
		ent1.config(state=DISABLED)
		try:
			for x in range(15):
				exec('ent'+str(x+2)+'.delete(0,END)')
				tt=''
				for y in range(len(c[k][x+1])):
					for z in range(len(c[k][x+1][y])):
						tt+=c[k][x+1][y][z]
						tt+='^'
					tt=tt[:-1]
					tt+='_'
				tt=tt[:-1]
				exec('ent'+str(x+2)+'.insert(0,tt)')
		except:
			pass
		b9.config(state=NORMAL)
	except:
		pass
	
def medit():
	global edit
	global k
	global c
	global ff
	try:
		edit=1
		k=int(ent1.get())
		tt=''
		for x in range(15):
			exec('ent'+str(x+2)+'.delete(0,END)')
			tt=''
			for y in range(len(c[k][x+1])):
				for z in range(len(c[k][x+1][y])):
					tt+=c[k][x+1][y][z]
					tt+='^'
				tt=tt[:-1]
				tt+='_'
			tt=tt[:-1]
			exec('ent'+str(x+2)+'.insert(0,tt)')
			ent1.config(state=DISABLED)
		b9.config(state=NORMAL)
		ff=''
		fo=[]
		for x in range(16):
			exec('fo.append(ent'+str(x+1)+'.get())')
			fo.append('\n')
		fo.append('END')
		for x in range(len(fo)):
			ff+=fo[x]
	except:
		pass
		
def mloadp():
	global fname
	global c
	entry=askstring('Load Quest File', 'Load: shg_*.shf')
	try:
		fname="shg_"+entry+".shf"
		c=shg.loat(fname[3:-4])
		mmm()
		showinfo(title="Load", message='Loaded!',icon='info')
	except:
		showinfo(title="Load", message='Error!',icon='warning')
		
def mnewp():
	mnewq('n')

def mdublp():
	mnewq('d')
	
def mnewq(a):
	global fname, c
	entry=askstring('Create New Quest File', 'Create: shg_*.shf')
	try:
		fname="shg_"+entry+".shf"
		try:
			file=open(fname,'r')
			showinfo(title="New", message='Error!',detail='File already exist!',icon='warning')
		except:
			if a=='n':
				file=open(fname,'w')
				c=shg.loat(fname[3:-4])
			elif a=='d':
				shg.save([entry,c],[entry,c])
				c=shg.loat(fname[3:-4])
			mmm()
			showinfo(title="New", message='Created!',icon='info')
	except:
		showinfo(title="New", message='Error!',icon='warning')

def canc():
	global tt
	global ch
	global k
	b9.config(state=DISABLED)
	for x in range(16):
		exec('ent'+str(x+1)+'.delete(0,END)')
	if ch==1:
		k=None
		ch=0
	else:
		ch=1
	ent1.config(state=NORMAL)

def appl():
	global tt
	global ch
	global k
	global c
	global edit
	global ff
	global fname
	b9.config(state=DISABLED)
	if edit==0:
		file=open(fname,'a')
		for x in range(16):
			exec('file.write(ent'+str(x+1)+'.get())')
			file.write('\n')
		file.write('END\n')
		file.close()
		c=shg.loat(fname[3:-4])
	else:
		fff=''
		fo=[]
		for x in range(16):
			exec('fo.append(ent'+str(x+1)+'.get())')
			fo.append('\n')
		fo.append('END')
		for x in range(len(fo)):
			fff+=fo[x]
		file=open(fname,'r')
		f2=file.read()
		file.close()
		f2=f2.replace(ff,fff)
		file=open(fname,'w')
		file.write(f2)
		file.close()
		c=shg.loat(fname[3:-4])
	for x in range(16):
		exec('ent'+str(x+1)+'.delete(0,END)')
	if ch==1:
		k=None
		ch=0
	else:
		ch=1
	ent1.config(state=NORMAL)

def restart():
	entry = askyesno(title="Restart", message="Are you sure you want to restart?")
	if entry == True:
		global b
		b=list('_'*9)
		pl()

def ggame():
	entry = askyesno(title="To Game", message="Do you want to open Game?",detail="Editor will be closed!\nIf you want to save edits\nplease press APPLY at first!",icon='warning')
	if entry == True:
		w.destroy()
		import shGAME

def quit():
	entry = askyesno(title="Quit", message="Are you sure you want to quit?")
	if entry == True:
		w.destroy()

#MENU
def mmm():
	global shrift
	global fname
	m=Menu(w)
	m2=Menu(m)
	m3=Menu(m)

	m2.add_command(label='Add',font=('',shrift[0]),command=madd)
	m2.add_command(label='Edit',font=('',shrift[0]),command=medit)
	m2.add_separator()
	m2.add_command(label='New Quest',font=('',shrift[0]),command=mnewp)
	m2.add_command(label='Dublicate Quest',font=('',shrift[0]),command=mdublp)
	m2.add_command(label='Load Quest',font=('',shrift[0]),command=mloadp)
	m2.add_separator()
	m2.add_command(label='Game',font=('',shrift[0]),command=ggame)
	m2.add_command(label='Quit',font=('',shrift[0]),command=quit)
	m.add_cascade(label='Editor',font=('',shrift[0]),menu=m2)
	m.add_cascade(label=fname,font=('',shrift[0]),menu=m3)
	
	w.configure(menu=m)

mmm()

for x in range(16):
	exec('lab'+str(x+1)+'=Label(w,text="'+d[0][x][0][0]+'",font=("",shrift[0]))')
	exec('lab'+str(1+x)+'.grid(row='+str(x)+',column=0)')
	exec('ent'+str(x+1)+'=Entry(w,text="'+str(1+x)+'",font=("",shrift[0]))')
	exec('ent'+str(1+x)+'.grid(row='+str(x)+',column=1)')
b8=Button(w,text='CANCEL+COPY',font=('',shrift[0]),command=canc)
b8.grid(row=16,column=0)
b9=Button(w,text='APPLY',font=('',shrift[0]),command=appl,state=DISABLED)
b9.grid(row=16,column=1)


w.mainloop()