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
        response = request('get', 'https://api.fintechspace.com.tw/realtime/v0/intraday/chart')
        data = json.loads(response.text)
        for i in data['chart']:
            for j in next(iter(i)):
                self.sto_pri = j['close']

        #########################介面
        self.root = tk.Tk()
        self.root.title("股票交易APP")
        title = tk.Label(self.root,text='股票交易平台',font =('微軟正黑體', 40,"bold"),bg=back,fg='#3Fe4ac',width=15,height=1).grid(column=0,row=7)
        self.root.configure(bg=back)
        ############################

        #################輸入私鑰和地址
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

        #################創帳號
        create_btn = Button(text='創建帳戶')
        create_btn.config(command=self.createInfo)
        create_btn.grid(column=1,row=10)
        #################創帳號

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

        if(self.priv_key == '0x8d37eafd6953fc0d09ec77a53409e590d764d17f496bb7a74bfad79bb37fcfa9' and self.address == '0x5677Ef7312ae71Cc99435fa7B81B0978ebBC67d9'):
            messagebox.showinfo('Info','歡迎，證券商')
            self.user = accounts(self.priv_key,self.address)
            self.IsSecurity = True
            self.Security_firms()
        else:
            messagebox.showinfo('Info','歡迎，投資者')
            self.user = accounts(self.priv_key,self.address)
            self.IsInvestor = True
            self.investor()

    def Security_firms(self):
        if(self.IsSecurity != True):
            return
        title = tk.Label(self.root,text='證券商',font =('微軟正黑體', 40,"bold"),bg=back,fg='#3Fe4ac').grid(column=0,row=0)

        ###給錢###(row=1)
        send = tk.Label(self.root,text='給投資者錢:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=1)
        Address_text=StringVar()
        Address_text.set('輸入要給的帳戶地址')
        self.toAddress_value = tk.Entry(self.root,text=Address_text)
        self.toAddress_value.grid(column=1,row=1)
        self.money_value = tk.Entry(self.root)
        self.money_value.grid(column=2,row=1)
        issue_btn = Button(text='送出',bg=btn_back,fg='white')
        issue_btn.config(command=self.send_issue)
        issue_btn.grid(column=3,row=1)
        ###給錢###(row=1)

        ###更新股票價錢####(row=2)
        self.stockPri_text = tk.Label(self.root,text='更新股票價錢:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=2)
        # self.stockPri_value = tk.Entry(self.root)
        # self.stockPri_value.grid(column=1,row=2)
        updatePrice_btn = Button(text='送出更新的股票價錢',bg=btn_back,fg='white')
        updatePrice_btn.config(command=self.send_stockPri)
        updatePrice_btn.grid(column=2,row=2)
        ###更新股票價錢####(row=2)

        ###更新股票數目####(row=3)
        self.stockQua_text = tk.Label(self.root,text='更新股票數目:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=3)
        self.stockQua_value = tk.Entry(self.root)
        self.stockQua_value.grid(column=1,row=3)
        updateQua_btn = Button(text='送出更新的股票數量',bg=btn_back,fg='white')
        updateQua_btn.config(command=self.send_stockQua)
        updateQua_btn.grid(column=2,row=3)
        ###更新股票數目####(row=3)

        ###確認股票價錢####(row=4)
        checkPrice_btn = Button(text='股票價錢:',bg=btn_back,fg='white')
        checkPrice_btn.config(command=self.checkPri)
        checkPrice_btn.grid(column=0,row=5)
        ###確認股票價錢####(row=4)

        ###確認股票數目####(row=5)
        checkStock_btn = Button(text='剩餘股票:',bg=btn_back,fg='white')
        checkStock_btn.config(command=self.checkQua)
        checkStock_btn.grid(column=0,row=6)       
        ###確認股票數目####(row=5)

    def investor(self):
        if(self.IsInvestor != True):
            return

        title = tk.Label(self.root,text='投資者',font =('微軟正黑體', 40,"bold"),bg=back,fg='#3Fe4ac').grid(column=0,row=0)

        ###購買股票####(row=1)
        self.buy_text = tk.Label(self.root,text='你想購買的股票數:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=1)
        self.buy_value = tk.Entry(self.root)
        self.buy_value.grid(column=1,row=1)
        buy_btn = Button(text='送出你想買的股票數',bg=btn_back,fg='white')
        buy_btn.config(command=self.buying)
        buy_btn.grid(column=2,row=1)
        ###購買股票####(row=1)    

        ###販賣股票####(row=2)
        self.sell_text = tk.Label(self.root,text='你想販賣的股票數:',font =('微軟正黑體', 12 ,"bold"),bg=back,fg='white').grid(column=0,row=2)
        self.sell_value = tk.Entry(self.root)
        self.sell_value.grid(column=1,row=2)
        sell_btn = Button(text='送出你想賣出的股票數',bg=btn_back,fg='white')
        sell_btn.config(command=self.selling)
        sell_btn.grid(column=2,row=2)
        ###販賣股票####(row=2)

        ###查看你的餘額####(row=4)
        checkPrice_btn = Button(text='查看你的餘額:',bg=btn_back,fg='white')
        checkPrice_btn.config(command=self.myBalance)
        checkPrice_btn.grid(column=0,row=3)
        ###查看你的餘額####(row=4)

        ###查看你的股票數目####(row=5)
        checkStock_btn = Button(text='查看你的股票數目:',bg=btn_back,fg='white')
        checkStock_btn.config(command=self.myStock)
        checkStock_btn.grid(column=0,row=4)       
         ###查看你的股票數目####(row=5)

        ###確認股票價錢####(row=4)
        checkPrice_btn = Button(text='股票價錢:',bg=btn_back,fg='white')
        checkPrice_btn.config(command=self.checkPri)
        checkPrice_btn.grid(column=0,row=5)
        ###確認股票價錢####(row=4)

        ###確認股票數目####(row=5)
        checkStock_btn = Button(text='剩餘股票:',bg=btn_back,fg='white')
        checkStock_btn.config(command=self.checkQua)
        checkStock_btn.grid(column=0,row=6)       
        ###確認股票數目####(row=5)


    #按鈕的事件區
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
        # stockPri = int(self.stockPri_value.get())
        hash= self.user.updatePrice(self.sto_pri)
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

    def selling(self):
        selled = int(self.sell_value.get())
        hash= self.user.sell(selled)
        sell_hash = tk.Text(self.root,width=20,height=4,font =('微軟正黑體', 10 ,"bold"))
        sell_hash.insert(1.0,hash)
        sell_hash.configure(state='disable')
        sell_hash.grid(column=3,row=2)
        messagebox.showinfo('Info','已送出')

    def myBalance(self):
        value= self.user.checkOwnBalance()
        balan = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=3)     
    def myStock(self):
        value= self.user.checkOwnStock()
        sto = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=4)     

    def checkPri(self):
        value= self.user.checkPrice()
        Price = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=5)        
        
    def checkQua(self):
        value = self.user.checkStockQuantity()
        Stock = tk.Label(self.root,text=value,font =('微軟正黑體', 10 ,"bold"),bg=back,fg='white').grid(column=1,row=6)
app()