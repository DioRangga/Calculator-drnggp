# Calculator-drnggp
Calculator Sederhana by DioRangga

###### @Copyright DIO RANGGA PRADANA ########


from tkinter import *
import tkinter.font as font
import math


root = Tk()
root.title("Calculator by DioRangga")
root.geometry("310x400")
root["bg"] = "#d1d1d1"

myfont = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"] = myfont
e["bg"] = "#d1d1d1"
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))

def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = int(nomor_awal)
    e.delete(0,END)
def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = int(nomor_awal)
    e.delete(0,END)
def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = int(nomor_awal)
    e.delete(0,END)
def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = int(nomor_awal)
    e.delete(0,END)
def akar():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0,END)
    e.insert(0,math.sqrt(n_awal))
def sisabagi():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0,END)
def pangkat():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0,END) 
    e.insert(0,n_awal **2)   
def hapus():
   e.delete(0,END)
def sama():
    nomor_akhir = e.get()
    e.delete(0,END)
    if mtk == "penjumlahan" :
        e.insert(0,n_awal + int(nomor_akhir))
    elif mtk == "pengurangan" :
        e.insert(0,n_awal - int(nomor_akhir))
    elif mtk == "perkalian" :
        e.insert(0,n_awal * int(nomor_akhir))
    elif mtk == "pembagian" :
        try:
            hitung = n_awal / int(nomor_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError :
            e.insert(0,'Itung Sendiri !!!')
    elif mtk == "sisabagi" :
        e.insert(0,n_awal % int(nomor_akhir))

    


btn1 = Button(root,text="1",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(1))
btn2 = Button(root,text="2",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(2))
btn3 = Button(root,text="3",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(3))
btn4 = Button(root,text="4",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(4))
btn5 = Button(root,text="5",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(5))
btn6 = Button(root,text="6",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(6))
btn7 = Button(root,text="7",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(7))
btn8 = Button(root,text="8",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(8))
btn9 = Button(root,text="9",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(9))
btn0 = Button(root,text="0",padx=30,bg="darkslategrey",fg="white",pady=20,command=lambda:angka(0))

tam = Button(root,text="+",padx=30,bg="dimgrey",fg="white",pady=20,command=tambah)
ak2 = Button(root,text="√",padx=30,bg="dimgrey",fg="white",pady=20,command=akar)
sisa = Button(root,text="%",padx=30,bg="dimgrey",fg="white",pady=20,command=sisabagi)
pang = Button(root,text="^",padx=30,bg="dimgrey",fg="white",pady=20,command=pangkat)
kur = Button(root,text="-",padx=30,bg="dimgrey",fg="white",pady=20,command=kurang)
kal = Button(root,text="x",padx=30,bg="dimgrey",fg="white",pady=20,command=kali)
bag = Button(root,text="/",padx=30,bg="dimgrey",fg="white",pady=20,command=bagi)
hap = Button(root,text="C",padx=30,bg="darkred",fg="white",pady=20,command=hapus)
sama = Button(root,text="=",padx=55,bg="darkolivegreen",fg="white",pady=20,command=sama)



btn1.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

tam.grid(row=1,column=3,pady=2)
kur.grid(row=2,column=3,pady=2)
kal.grid(row=3,column=3,pady=2)
bag.grid(row=4,column=3,pady=2)
hap.grid(row=4,column=0,pady=2)
sama.grid(row=5,column=2,pady=2,columnspan=2)

ak2.grid(row=5,column=0,pady=2)
pang.grid(row=5,column=1,pady=2)
sisa.grid(row=4,column=2,pady=2)


root.mainloop()
