import tkinter as tk
from tkinter import Label, Entry, Button

from expense_manager import ExpenseManeger
window=tk.Tk()

manager=ExpenseManeger()

window.title("Expense Manager")
window.geometry("500x500")
titel_lable=tk.Label(window,text="Expense Manager",font=("Arial",20))
titel_lable.pack(pady=10)

lable_1=tk.Label(window,text=":عنوان",font=("Arial",15))
lable_1.place(x=450,y=50)
input_name=Entry(window)
input_name.place(x=320,y=60)

lable_2=tk.Label(window,text=":مبلغ",font=("Arial",15))
lable_2.place(x=460,y=90)

input_amount=tk.Entry(window)
input_amount.place(x=320,y=95)

lable_3=tk.Label(window,text=":دسته بندی",font=("Arial",15))
lable_3.place(x=420,y=130)

input_category=tk.Entry(window)
input_category.place(x=295,y=140)

lable_4=tk.Label(window,text=":توضیحات",font=("Arial",15))
lable_4.place(x=425,y=170)

input_description=tk.Entry(window)
input_description.place(x=300,y=173)


def add_click():
    manager.add_expense(input_name.get(),int(input_amount.get()),input_category.get(),input_description.get())
    print(manager.expenses)
    show_expenses_guii()
    input_name.delete(0,tk.END)
    input_amount.delete(0,tk.END)
    input_category.delete(0,tk.END)
    input_description.delete(0,tk.END)

def show_expenses_guii():
    expense_listbox.delete(0,tk.END)
    manager.load_expenses()
    expenses=manager.show_expense()
    for item in expenses:
        expense_listbox.insert(tk.END,item)

def search_click():
    result=manager.searech_expense(input_name.get())
    expense_listbox.delete(0,tk.END)
    for item in result:
        expense_listbox.insert(tk.END,str(item))

def remove_click():
    number=int(input_name.get())
    result=manager.remove_expense(number)
    expense_listbox.delete(0,tk.END)
    expense_listbox.insert(tk.END,result)


def total_click():
    result=manager.total_expense()
    expense_listbox.delete(0,tk.END)
    expense_listbox.insert(tk.END,result)

def max_click():
   result= manager.show_max_expense()
   expense_listbox.delete(0,tk.END)
   expense_listbox.insert(tk.END,result)


lable_show=tk.Label(window,text=" نمایش --->",font=("Arial",15))
lable_show.place(x=70,y=285)
expense_listbox=tk.Listbox(window,width=40,height=10)
expense_listbox.place(y=250,x=160)


button_add=tk.Button(window,bg="cyan",text="افزودن هزینه",command=add_click)
button_add.place(x=20,y=65)

button_show=tk.Button(window,text="نمایش هزینه",bg="red",command=show_expenses_guii)
button_show.place(x=120,y=65)

button_search=tk.Button(window,text="جستوجو هزینه",bg="yellow",command=search_click)
button_search.place(x=20,y=115)

button_remove=tk.Button(window,text="حذف هزینه",bg="pink",command=remove_click)
button_remove.place(x=120,y=115)

button_total=tk.Button(window,text="مجموع هزینه",bg="orange",command=total_click)
button_total.place(x=20,y=155)

button_max_expense=tk.Button(window,text="بیشترین هزینه",bg="purple",command=max_click)
button_max_expense.place(x=115,y=155)


window.mainloop()
