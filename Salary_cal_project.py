import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pandas
import subprocess

# Creating tkinter window
window = tk.Tk()
window.title('Employee Salary calculation')
window.geometry('500x300')
print('---------------------------------------------------')


def calculat():

    basic_salary=(t.get(1.0, "end-1c"))
    choosen_value=choosen.get()
    print("*******",choosen_value)
    if choosen_value=="":
        popup = tkinter.messagebox.showinfo("Alert", "Please select employee name ")
    elif basic_salary=="":
         popup = tkinter.messagebox.showinfo("Alert", "Basic salary is empty")
    else:
        basic=int(basic_salary)
        da = float(basic * 0.25)
        hra = float(basic * 0.15)
        pf = float((basic + da) * 0.12)
        ta = float(basic * 0.075)
        netpay = float(basic + da + hra + ta)
        grosspay = float(netpay - pf)
        print(grosspay)
        try:
            fileptr = open("D:/file.txt",'w')
            if(fileptr):
                pass
            else:
                fileptr = open("D:/file.txt", 'X')

            fileptr.writelines('S A L A R Y D E T A I L E D B R E A K U P\n')
            fileptr.writelines("==============================================\n")
            fileptr.writelines(" NAME OF EMPLOYEE :")
            fileptr.writelines(choosen_value)
            fileptr.write("\n")
            fileptr.writelines(" BASIC SALARY : ")
            fileptr.write(str(        basic ))
            fileptr.write("\n")
            fileptr.write(" DEARNESS ALLOW. : ")
            fileptr.writelines(str(da))
            fileptr.write("\n")
            fileptr.write(" HOUSE RENT ALLOW.: ")
            fileptr.write(str(hra))
            fileptr.write("\n")
            fileptr.write(" TRAVEL ALLOW. : ")
            fileptr.writelines(str(ta))
            fileptr.write("\n")
            fileptr.write("==============================================\n")
            fileptr.write(" NET SALARY PAY : ")
            fileptr.writelines(str(netpay))
            fileptr.write("\n")
            fileptr.write(" PROVIDENT FUND : ")
            fileptr.writelines(str(pf))
            fileptr.write("\n")
            fileptr.write("==============================================\n")
            fileptr.write(" GROSS PAYMENT : ")
            fileptr.writelines(str(grosspay))
            fileptr.write("\n")
            fileptr.write("==============================================")
            salary_dis.insert(0.0,grosspay,grosspay)
        except Exception as e:
                print("exception",e)
        finally:
            fileptr.close()


def clear():
    basic = (t.get(1.0, "end-1c"))
    salary_dis1 = (salary_dis.get(1.0, "end-1c"))
    t.replace(0.0,"end","",basic)
    salary_dis.replace(0.0, "end", "", salary_dis1)
    choosen.set("")

print('---------------------------------------------------')
# label text for title
ttk.Label(window, text="Employee Salary details",
          background='green', foreground="white",
          font=("Times New Roman", 10)).grid(row=0, column=1)
ttk.Label(window, text="Employee Name  :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=5, padx=10, pady=25)
ttk.Label(window, text="Basic Salary       :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=10, padx=10, pady=25)
ttk.Label(window, text="Grass Salary       :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=20, padx=10, pady=25)

# Combobox creation
ex=pandas.read_excel('D:/Salary_details.xlsx')
#excel_data_df = pandas.read_excel('D:\Salary_details.xlsx', sheet_name='Sheet1')
n = tk.StringVar()
choosen = ttk.Combobox(window, width=27, textvariable=n)
# Adding combobox drop down list
a=(ex['Emp Name'].values)
name_list=list(a)
choosen['values'] = (name_list)

t=tk.Text(window, height = 2, width = 22)
salary_dis=tk.Text(window, height = 2, width = 22)
b = tk.Button(window, height = 2,
                 width = 10,
                 text ="Gross pay",
                 command = calculat)
clear_btn = tk.Button(window, height = 2,
                 width = 10,
                 text ="clear",
                 command = clear)

choosen.grid(column=1, row=5)
choosen.current()
t.grid(row=10, column=1)
salary_dis.grid(row=20, column=1)
b.grid(row=30, column=1)
clear_btn.grid(row=30, column=2)


window.mainloop()

