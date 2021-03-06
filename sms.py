from tkinter import *
from tkinter.scrolledtext import *			
from tkinter.messagebox import *			
from sqlite3 import *					 
import requests						
import random						
import matplotlib.pyplot as plt				
from random import randrange

def f1():
	root.withdraw()   
	add_stu.deiconify() 
def f2():
	add_stu.withdraw() 
	root.deiconify() 
def f3():
	root.withdraw()   
	view_stu.deiconify() 
	view_stu_stdata.delete(1.0,END)
	con=None
	try:
		con=connect("meher.db")
		cursor=con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "ROLL NO.: " + str(d[0]) +" "+ "NAME: " + str(d[1]) +" "+ "MARKS: " + str(d[2]) + "\n"
		view_stu_stdata.insert(INSERT,info)			
	except Exception as e:
		showerror("Issue",str(e))
	finally:
		if con is not None:
			con.close()
def f4():
	view_stu.withdraw() 
	root.deiconify() 
def f5():
	con=None
	try:
		con=connect("meher.db")
		cursor=con.cursor()
		sql = "insert into student values('%d', '%s', '%f')"
		rno = int(add_stu_entRno.get())			
		name = add_stu_entName.get()
		marks = float(add_stu_entMarks.get())
		letters = 0
		for i in name:
			if i.isalpha():
				letters+=1
		d = name
		if(rno > 0):
			if(d.isalpha() and letters >= 2):
				m = marks
				if (0.0 <= m < 101.0):
					cursor.execute(sql % (rno,name,marks))
					con.commit()
					showinfo("Success","Record added successfully!")
					add_stu_entRno.delete(0,END) 
					add_stu_entRno.focus() 
					add_stu_entName.delete(0,END) 
					add_stu_entName.focus() 
					add_stu_entMarks.delete(0,END) 
					add_stu_entMarks.focus()  
					
				else:
					showerror("Invalid Marks","It should be between 0 to 100") 
					add_stu_entMarks.delete(0,END) 
					add_stu_entMarks.focus() 
					con.rollback()
				
			else:
				showerror("ERROR","Name should have 2 alphabets")
				add_stu_entName.delete(0,END) 
				add_stu_entName.focus() 
				con.rollback()	
		else:
			showerror("ERROR","Invalid Rollno.!")	
			add_stu_entRno.delete(0,END) 
			add_stu_entRno.focus() 
			con.rollback()
			
	except ValueError:
		showerror("ERROR","Please fill in the details correctly!")		
		con.rollback()
	
	except Exception as e:
		showerror("Issue","Rollno. already there in database!")
		add_stu_entRno.delete(0,END) 
		add_stu_entRno.focus() 
		add_stu_entName.delete(0,END) 
		add_stu_entName.focus() 
		add_stu_entMarks.delete(0,END) 
		add_stu_entMarks.focus() 
		con.rollback()
	
	finally:
		if con is not None:
			con.close()
def f6():
	root.withdraw()   
	update_stu.deiconify()
def f7():
	con=None
	try:
		con=connect("meher.db")
		cursor=con.cursor()
		sql = "update student set name = '%s', marks = %f where rno=%d"
		rno = int(update_stu_entRno.get())
		name = update_stu_entName.get()
		marks = float(update_stu_entMarks.get())
		#length = len(name)
		letters = 0
		for i in name:
			if i.isalpha():
				letters+=1
		d = name
		cursor.execute("select * from student")
		rows = cursor.fetchall()
		l1 = list(rows)	
		print(l1)				
		r1 = [l[0] for l in l1]			
		print(r1)
		if (rno > 0):
			if rno in r1:
				if(d.isalpha() and letters >= 2):
					m = marks
					if (0.0 <= m < 101.0):
						cursor.execute(sql % (name,marks,rno))
						con.commit()
						showinfo("Success","Record updated successfully!")
						update_stu_entRno.delete(0,END) 
						update_stu_entRno.focus() 
						update_stu_entName.delete(0,END) 
						update_stu_entName.focus() 
						update_stu_entMarks.delete(0,END) 
						update_stu_entMarks.focus() 
					else:
						showerror("Invalid Marks","It should be between 0 to 100") 
						update_stu_entMarks.delete(0,END) 
						update_stu_entMarks.focus() 
						con.rollback()
				else:
					showerror("ERROR","Name should have 2 alphabets")
					update_stu_entName.delete(0,END)
					update_stu_entName.focus() 
					con.rollback()	
			else:
				showerror("ERROR","??? Rollno. not found in database!")
				update_stu_entRno.delete(0,END) 
				update_stu_entRno.focus() 
				con.rollback()
		else:
			showerror("ERROR","Invalid Rollno.!")	
			update_stu_entRno.delete(0,END) 
			update_stu_entRno.focus() 
			con.rollback()
	except ValueError:
		showerror("ERROR","Please fill in the details correctly!")
		con.rollback()		
	except Exception as e:
		showerror("Issue",str(e))
		update_stu_entRno.delete(0,END) 
		update_stu_entRno.focus() 
		update_stu_entName.delete(0,END) 
		update_stu_entName.focus() 
		update_stu_entMarks.delete(0,END) 
		update_stu_entMarks.focus() 
		con.rollback()
	finally:
		if con is not None:
			con.close()
def f8():
	update_stu.withdraw() 
	root.deiconify() 
def f9():
	root.withdraw()   
	del_stu.deiconify() 

def f10():
	con=None
	try:
		con=connect("meher.db")
		cursor=con.cursor()
		sql = "delete from student where rno=%d"
		rno = int(del_stu_entRno.get())
		cursor.execute("Select * FROM student")
		rows = cursor.fetchall()
		l1 = list(rows)	
		r1 = [l[0] for l in l1]
		if rno in r1:
			cursor.execute(sql % (rno))
			con.commit()
			showinfo("Success","??? Record deleted successfully!")
			del_stu_entRno.delete(0,END) 
			del_stu_entRno.focus() 
		elif rno < 1:
			showerror("ERROR"," ??? Invalid Rollno. \n Expected to be positive numbers")
			del_stu_entRno.delete(0,END) 
			del_stu_entRno.focus() 
		else:
			showerror("ERROR","??? Rollno. not found in database!")
			del_stu_entRno.delete(0,END)
			del_stu_entRno.focus() 
			
	except ValueError:
		showerror("Invalid","??? Rollno. is expected to be an integer!")
		del_stu_entRno.delete(0,END) 
		del_stu_entRno.focus() 
		con.rollback()
	except Exception as e:
		showerror("ERROR", str(e))
		del_stu_entRno.delete(0,END) 
		del_stu_entRno.focus() 
		con.rollback()	
	finally:
		if con is not None:
			con.close()
def f11():
	del_stu.withdraw()
	root.deiconify() 
def f12():
	con = connect("meher.db")
	c = con.cursor()
	c.execute("select * from student")
	rows = c.fetchall()
	l1 = list(rows)	
	print(l1)
	r1 = [l[1] for l in l1]
	print(r1)
	r2 = [l[2] for l in l1]
	print(r2)
	color_label = ["red","green","blue"]
	plt.title("Batch Information!")
	plt.ylabel("Marks")
	plt.bar(r1,r2,color=color_label)
	plt.xticks(rotation=45)			
	plt.show()
	
root = Tk()
root.title("S. M. S")
root.geometry("950x520+270+150")
root.configure(bg='PaleGreen1')

btnAdd = Button(root,text="Add", width=10, font=('arial', 18, 'bold'),bg="lavender",command = f1)
btnView = Button(root,text="View", width=10, font=('arial', 18, 'bold'),bg="lavender",command = f3)
btnUpdate = Button(root,text="Update", width=10, font=('arial', 18, 'bold'),bg="lavender",command = f6)
btnDelete = Button(root,text="Delete", width=10, font=('arial', 18, 'bold'),bg="lavender",command = f9)
btnCharts = Button(root,text="Charts", width=10, font=('arial', 18, 'bold'),bg="lavender",command = f12)
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnCharts.pack(pady=10)

try:
	web_address = "https://ipinfo.io/"			
	res = requests.get(web_address)
	data = res.json() #json converts data into dictionary
	city_name = data['city']		
	state = data['region']
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city_name
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	web_address = a1 + a2 + a3
	res = requests.get(web_address)
	data = res.json()
	
	main = data['main']   
	temp = str(main['temp'])	
except Exception as e:
	print("Issue ",e)

motivational_quotes = [
"Challenges are what make life interesting and overcoming them is what makes life meaningful.",
"It always seems impossible until it is done.",
"Don't let anyone dull your sparkle!",
"It is during our darkest moments that we must focus on the light.",
"Success comes from having dreams that are bigger than your fears.", 
"The best view comes after the hardest climb.",
"Happiness is not by chance, but my choice.",
"Tough times never last but tough people do."]

r3 = randrange(len(motivational_quotes))		

labelframe1 = LabelFrame(root,bg="PaleGreen1", height=9)
labelframe1.pack(expand="yes",fill="both") 
l1 = Label(labelframe1,text="Location: " + city_name + "," + state, bg="PaleGreen1",font=('arial',15))
l1.place(x=20, y=30)
l2 = Label(labelframe1,text="Temperature: " + temp + "??C", bg="PaleGreen1",font=('arial',15))
l2.place(x=700,y=30)

labelframe2 = LabelFrame(root,bg="pale green",font=('arial',15),height=9)
labelframe2.pack(expand="yes",fill="both")
l3 = Label(labelframe2,text="QOTD: " + motivational_quotes[r3], bg="PaleGreen1",font=('arial',15))	
l3.place(x=20, y=30)

add_stu = Toplevel(root)
add_stu.title("Add student")
add_stu.geometry("550x400+300+200")
add_stu.configure(bg="lavender")

add_stu_lblRno = Label(add_stu, text="enter rno", font=('arial',18,'bold'),bg="lavender")
add_stu_entRno = Entry(add_stu, bd=5, font=('arial',18,'bold'))
add_stu_lblName = Label(add_stu, text="enter name", font=('arial',18,'bold'),bg="lavender")
add_stu_entName = Entry(add_stu, bd=5, font=('arial',18,'bold'))
add_stu_lblMarks = Label(add_stu, text="enter marks", font=('arial',18,'bold'),bg="lavender")
add_stu_entMarks = Entry(add_stu, bd=5, font=('arial',18,'bold'))
add_stu_btnSave = Button(add_stu, text="save", width=10,font=('arial',18,'bold'),command = f5,bg="lavender")
add_stu_btnBack = Button(add_stu, text="back", width=10,font=('arial',18,'bold'), command = f2,bg="lavender")

add_stu_lblRno.pack(pady=5) 
add_stu_entRno.pack(pady=5) 
add_stu_lblName.pack(pady=5) 
add_stu_entName.pack(pady=5) 
add_stu_lblMarks.pack(pady=5)
add_stu_entMarks.pack(pady=5)
add_stu_btnSave.pack(pady=5)  
add_stu_btnBack.pack(pady=5) 

add_stu.withdraw()	

update_stu = Toplevel(root)
update_stu.title("Update student")
update_stu.geometry("550x400+300+200")
update_stu.configure(bg="misty rose")

update_stu_lblRno = Label(update_stu, text="enter rno", font=('arial',18,'bold'),bg="misty rose")
update_stu_entRno = Entry(update_stu, bd=5, font=('arial',18,'bold'))
update_stu_lblName = Label(update_stu, text="enter name", font=('arial',18,'bold'),bg="misty rose")
update_stu_entName = Entry(update_stu, bd=5, font=('arial',18,'bold'))
update_stu_lblMarks = Label(update_stu, text="enter marks", font=('arial',18,'bold'),bg="misty rose")
update_stu_entMarks = Entry(update_stu, bd=5, font=('arial',18,'bold'))
update_stu_btnSave = Button(update_stu, text="save", width=10,font=('arial',18,'bold'),command = f7,bg="misty rose")
update_stu_btnBack = Button(update_stu, text="back", width=10,font=('arial',18,'bold'), command = f8,bg="misty rose")

update_stu_lblRno.pack(pady=5) 
update_stu_entRno.pack(pady=5) 
update_stu_lblName.pack(pady=5) 
update_stu_entName.pack(pady=5) 
update_stu_lblMarks.pack(pady=5)
update_stu_entMarks.pack(pady=5)
update_stu_btnSave.pack(pady=5)  
update_stu_btnBack.pack(pady=5) 

update_stu.withdraw()	

del_stu = Toplevel(root)
del_stu.title("Delete student")
del_stu.geometry("550x400+300+200")
del_stu.configure(bg="LightSkyBlue1")

del_stu_lblRno = Label(del_stu, text="enter rno", font=('arial',18,'bold'),bg="LightSkyBlue1")
del_stu_entRno = Entry(del_stu, bd=5, font=('arial',18,'bold'))
del_stu_btnSave = Button(del_stu, text="Delete", width=10,font=('arial',18,'bold'),command = f10,bg="LightSkyBlue1")
del_stu_btnBack = Button(del_stu, text="Back", width=10,font=('arial',18,'bold'), command = f11,bg="LightSkyBlue1")

del_stu_lblRno.pack(pady=5) 
del_stu_entRno.pack(pady=5) 
del_stu_btnSave.pack(pady=5)  
del_stu_btnBack.pack(pady=5) 

del_stu.withdraw()	

view_stu = Toplevel(root)
view_stu.title("View Student")
view_stu.geometry("550x400+300+200")
view_stu.configure(bg="khaki")

view_stu_stdata = ScrolledText(view_stu, width=40,height=15, font=('arial',14,'bold'),bg="khaki")
view_stu_btnBack = Button(view_stu, text="Back",width=10, font=('arial',18,'bold'), command = f4,bg="lavender")

view_stu_stdata.pack(pady=5)
view_stu_btnBack.pack(pady=5)

view_stu.withdraw()  

root.mainloop()

