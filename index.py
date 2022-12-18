from tkinter.constants import GROOVE, RIDGE
from contract import accounts
from create_account import Create
import tkinter as tk
from tkinter import Button, StringVar, messagebox,W ,FLAT, NW
from requests import request
import json

back = '#22243d'
red_back='#f14d58'
# red_front='#f14d58'
btn_back = '#3a3c52'


class app():
    def __init__(self):
        self.IsSecurity = False
        self.IsInvestor = False
        self.main()
        
        
    def main(self):

        #########################UI
        self.root = tk.Tk()
        self.root.title("Recharge")
        title = tk.Label(self.root,text='Selling',font =('微軟正黑體', 40,"bold"),bg=back,fg='#3Fe4ac',width=15,height=1).grid(column=0,row=7)
        self.root.configure(bg=back)
        ############################

        #################input private key and address
        p=StringVar()
        a=StringVar()
        p.set('輸入你的私鑰')
        a.set('輸入你的地址')
        self.p_value = tk.Entry(self.root,text=p,font='微軟正黑體',bg=btn_back,fg='white')
        self.a_value = tk.Entry(self.root,text=a,font='微軟正黑體',bg=btn_back,fg='white')                    
        self.p_value.grid(column=0,row=8)
        self.a_value.grid(column=0,row=9)

        account_btn = Button(text='送出你的地址與帳戶',font='微軟正黑體',bg=red_back,fg='white')
        account_btn.config(command=self.your_account)
        account_btn.grid(column=0,row=10)
        #############################

        #################
        create_btn = Button(text='創建帳戶')
        create_btn.config(command=self.createInfo)
        create_btn.grid(column=1,row=10)
        #################

        self.root.mainloop()

    def createInfo(self):
        self.info = Create()
        send = tk.Label(self.root,text='輸入你的密碼:',font =('微軟正黑體', 10,"bold")).grid(column=2,row=10)
        self.password = tk.Entry(self.root)
        self.password.grid(column=3,row=10)
        create_btn = Button(text='送出')
        create_btn.config(command=self.create_success)
        create_btn.grid(column=4,row=10)

    def create_success(self):
        p = tk.Label(self.root,text='私鑰:',font =('微軟正黑體', 10,"bold")).grid(column=5,row=10)
        pri,adr = self.info.create_new(int(self.password.get()))
        priv = tk.Text(self.root,width=20,height=4,font = ('微軟正黑體', 10 ,"bold"))
        priv.insert(1.0,pri)
        priv.configure(state='disable')
        priv.grid(column=6,row=10)

        a = tk.Label(self.root,text='地址:',font =('微軟正黑體', 10,"bold")).grid(column=7,row=10)
        addr = tk.Text(self.root,width=20,height=4,font = ('微軟正黑體', 10 ,"bold"))
        addr.insert(1.0,adr)
        addr.configure(state='disable')
        addr.grid(column=8,row=10)

        messagebox.showinfo('Info','請保存你的私鑰和地址')


    def your_account(self):
        
        self.priv_key = str(self.p_value.get())
        self.address = str(self.a_value.get()) 

        if(self.priv_key == '0x7b841d6fe1d196eeb5c876f949aa4f4bf786b5db3d8a3e31663e193bac6b28cd' and self.address == '0x5e15d3AD58b0238f9ff617DF6cC7B5e8cc43DCee'):
            messagebox.showinfo('Info','歡迎，Owner')
            self.user = accounts(self.priv_key,self.address)
            self.IsSecurity = True
            self.Owner_UI()
        else:
            messagebox.showinfo('Info','歡迎，Buyer')
            self.user = accounts(self.priv_key,self.address)
            self.IsInvestor = True
            self.Buyer_UI()

    def Owner_UI(self):
        if(self.IsSecurity != True):
            return
        title = tk.Label(self.root,text='Owner',font =('微軟正黑體', 40,"bold"),bg=back,fg='#3Fe4ac').grid(column=0,row=0)

        send = tk.Label(self.root,text='給Buyer錢:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=1)
        Address_text=StringVar()
        Address_text.set('輸入要給的帳戶地址')
        self.toAddress_value = tk.Entry(self.root,text=Address_text)
        self.toAddress_value.grid(column=1,row=1)
        self.money_value = tk.Entry(self.root)
        self.money_value.grid(column=2,row=1)
        issue_btn = Button(text='送出',bg=btn_back,fg='white')
        issue_btn.config(command=self.send_issue)
        issue_btn.grid(column=3,row=1)
  
        self.stockPri_text = tk.Label(self.root,text='更新產品價錢:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=2)
        self.stockPri_value = tk.Entry(self.root)
        self.stockPri_value.grid(column=1,row=2)
        updatePrice_btn = Button(text='送出更新的產品價錢',bg=btn_back,fg='white')
        updatePrice_btn.config(command=self.send_stockPri)
        updatePrice_btn.grid(column=2,row=2)

        self.stockQua_text = tk.Label(self.root,text='更新產品數目:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=3)
        self.stockQua_value = tk.Entry(self.root)
        self.stockQua_value.grid(column=1,row=3)
        updateQua_btn = Button(text='送出更新的產品數量',bg=btn_back,fg='white')
        updateQua_btn.config(command=self.send_stockQua)
        updateQua_btn.grid(column=2,row=3)

        checkPrice_btn = Button(text='產品價錢:',bg=btn_back,fg='white')
        checkPrice_btn.config(command=self.checkPri)
        checkPrice_btn.grid(column=0,row=5)

        checkStock_btn = Button(text='剩餘產品:',bg=btn_back,fg='white')
        checkStock_btn.config(command=self.checkQua)
        checkStock_btn.grid(column=0,row=6)       

    def Buyer_UI(self):
        if(self.IsInvestor != True):
            return

        title = tk.Label(self.root,text='Buyer',font =('微軟正黑體', 40,"bold"),bg=back,fg='#3Fe4ac').grid(column=0,row=0)

        self.buy_text = tk.Label(self.root,text='你想購買的產品數:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=1)
        self.buy_value = tk.Entry(self.root)
        self.buy_value.grid(column=1,row=1)
        buy_btn = Button(text='送出你想買的產品數',bg=btn_back,fg='white')
        buy_btn.config(command=self.buying)
        buy_btn.grid(column=2,row=1)
    
        checkPrice_btn = Button(text='查看帳戶餘額:',bg=btn_back,fg='white')
        checkPrice_btn.config(command=self.myBalance)
        checkPrice_btn.grid(column=0,row=3)
 
        checkStock_btn = Button(text='查看帳戶產品數:',bg=btn_back,fg='white')
        checkStock_btn.config(command=self.myStock)
        checkStock_btn.grid(column=0,row=4)       

        checkPrice_btn = Button(text='產品價錢:',bg=btn_back,fg='white')
        checkPrice_btn.config(command=self.checkPri)
        checkPrice_btn.grid(column=0,row=5)

        checkStock_btn = Button(text='剩餘產品:',bg=btn_back,fg='white')
        checkStock_btn.config(command=self.checkQua)
        checkStock_btn.grid(column=0,row=6)       


    #Event
    def send_issue(self):
        toAddress = self.toAddress_value.get()
        money = int(self.money_value.get())
        hash = self.user.issue(toAddress,money)
        isu_hash = tk.Text(self.root,width=20,height=4,font =('微軟正黑體', 10 ,"bold"))
        isu_hash.insert(1.0,hash)
        isu_hash.configure(state='disable')
        isu_hash.grid(column=4,row=1)
        messagebox.showinfo('Info','已送出')        

    def send_stockPri(self):
        stockPri = int(self.stockPri_value.get())
        hash= self.user.updatePrice(stockPri)
        pri_hash = tk.Text(self.root,width=20,height=4,font =('微軟正黑體', 10 ,"bold"))
        pri_hash.insert(1.0,hash)
        pri_hash.configure(state='disable')
        pri_hash.grid(column=2,row=5)
        messagebox.showinfo('Info','已送出')   

    def send_stockQua(self):
        stockQua = int(self.stockQua_value.get())
        hash= self.user.updateQuantity(stockQua)
        qua_hash = tk.Text(self.root,width=20,height=4,font =('微軟正黑體', 10 ,"bold"))
        qua_hash.insert(1.0,hash)
        qua_hash.configure(state='disable')
        qua_hash.grid(column=2,row=6)
        messagebox.showinfo('Info','已送出')
    
    def buying(self):
        buyed = int(self.buy_value.get())
        hash= self.user.buy(buyed)
        buy_hash = tk.Text(self.root,width=20,height=4,font =('微軟正黑體', 10 ,"bold"))
        buy_hash.insert(1.0,hash)
        buy_hash.configure(state='disable')
        buy_hash.grid(column=3,row=1)
        messagebox.showinfo('Info','已送出')

    def myBalance(self):
        address = self.a_value.get()
        value= self.user.checkAddressBalance(address)
        balan = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=3)     
    
    def myStock(self):
        address = self.a_value.get()
        value= self.user.checkAddressQunatity(address)
        sto = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=4)     

    def checkPri(self):
        value= self.user.checkPrice()
        Price = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=5)        
        
    def checkQua(self):
        value = self.user.checkStockQuantity()
        Stock = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=6)
app()