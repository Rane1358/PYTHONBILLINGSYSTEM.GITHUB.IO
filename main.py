from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile

class Bill_App:
    def __init__(self,root):    
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("BILLING SOFTWARE")
        
        
        # =====================(variables)==========================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        # product categories list
        
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
        
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=700
        self.price_spykar=8000
        
        self.t_shirt=["Polo","Roadster","Jack & Jones"]
        self.price_polo=1500
        self.price_roadster=1800
        self.price_jackjones=2000
        
        self.Shirt=["Peter England","Louis Phillipe","Park Avenue"]
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_park=1740
        
        self.SubCatLifeStyle=["Bath Soap","Face Creame","Hair Oil"]
        
        self.bath_soap=["Lifebuy","Lux","Santoor","Pearl"]
        self.price_Lifebuy=20
        self.price_Lux=20
        self.price_Santoor=20
        self.price_Pearl=20
        
        self.Face_Creame=["Fair&Lovely","Ponds","Olay","Garnier"]
        self.price_fair=20
        self.price_Ponds=20
        self.price_garnier=30
        self.price_olay=20
        
        self.Hair_oil=["Parachute","Jashmin","Bajaj"]
        self.price_Parachute=25
        self.price_Jashmin=22
        self.price_Bajaj=30
        
        self.SubCatMobiles=["Iphone","Sumsung","Xiome","RealMe","One+"]
        self.Iphone=["Iphone x","Iphone 11","Iphone 12"]
        self.price_Iphone_x=40000
        self.price_Iphone_11=60000
        self.price_Iphone_12=85000
        
        self.Samsung=["Samsung M16","Samsung M12","Samsung M21"]
        self.price_M16=16000
        self.price_M12=12000
        self.price_M21=18000
        
        self.Xiome=["Redmi 11","Redmi 12","Redmi PRO"]
        self.price_rm11=11000
        self.price_rm12=12000
        self.price_rmpro=9000
        
        self.RealMe=["RealMe 12","RealMe 13","RealMe Pro"]
        self.price_r12=25000
        self.price_r13=22000
        self.price_rProk=30000
        
        self.OnePlus=["OnePlus 1","OnePlus 2","OnePlus 3"]
        self.price_OnePlus1=45000
        self.price_OnePlus2=60000
        self.price_OnePlus3=45000
        
        
        
        
        
        
        
        
        
        
        
        # #img1
        # img=Image.open("image/lifestyle.png")
        # img=img.resize((500,120),Image.LANCZOS) #ANtialias used to convert high level img to low level img
        # self.photoimg=ImageTk.PhotoImage(img) #image tk is used covert port  into img    
        
        # lbl_img=Label(self.root,image=self.photoimg)
        # lbl_img.place(x=0,y=0,width=200,height=80)
        
        
        
        # #img2
        # img_1=Image.open("image/girls.jpg")
        # img_1=img_1.resize((500,120),Image.LANCZOS) #ANtialias used to convert high level img to low level img
        # self.photoimg_1=ImageTk.PhotoImage(img_1) #image tk is used covert port  into img    
        
        # lbl_img=Label(self.root,image=self.photoimg_1)
        # lbl_img.place(x=500,y=0,width=200,height=80)
        
        
        # #img3
        # img_2=Image.open("image/girl1.jpg")
        # img_2=img_2.resize((500,120),Image.LANCZOS) #ANtialias used to convert high level img to low level img
        # self.photoimg_2=ImageTk.PhotoImage(img_2) #image tk is used covert port  into img    
        
        # lbl_img=Label(self.root,image=self.photoimg_2)
        # lbl_img.place(x=1000,y=0,width=200,height=800)
        
        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=0,width=1380,height=55)
        
        
        
        
        # MAIN FRAME
        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=50,width=1400,height=1000)
        
        #CUSTOMER FRAME
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=330,height=140)
        
        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24) #tkinter.ttk module provides access to the Tk themed widget set 
        self.entry_mob.grid(row=0,column=1)
        
        self.ldlCustName=Label(Cust_Frame,font=('times new roman',12,'bold'),bg="white",text="Customer Name",bd=4)
        self.ldlCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('times new roman',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.ldlEmail=Label(Cust_Frame,font=('times new roman',12,'bold'),bg="white",text="Email",bd=4)
        self.ldlEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('times new roman',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        # PRODUCT LABELFRAME
        
        Prod_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Prod_Frame.place(x=350,y=5,width=600,height=140)
        
        # CATEGORY
        self.ldlCategory=Label(Prod_Frame,font=('times new roman',12,'bold'),bg="white",text="Select Categories",bd=4)
        self.ldlCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_Category=ttk.Combobox(Prod_Frame,value=self.Category,font=('times new roman',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.categories)
        
        # SUBCATEGORY
        self.ldlCategory=Label(Prod_Frame,font=('times new roman',12,'bold'),bg="white",text="Subcategory",bd=4)
        self.ldlCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_SubCategory=ttk.Combobox(Prod_Frame,value=[""],font=('times new roman',10,'bold'),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        
        
        #Prodduct Name
        self.lblproduct=Label(Prod_Frame,font=('times new roman',12,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.ComboProduct=ttk.Combobox(Prod_Frame,textvariable=self.product,state="readonly",font=('times new roman',10,'bold'),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        
        #Price
        self.lblPrice=Label(Prod_Frame,font=('times new roman',12,'bold'),bg="white",text="Price",bd=4) 
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        
        self.ComboPrice=ttk.Combobox(Prod_Frame,state="readonly",textvariable=self.prices,font=('times new roman',10,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
        
        #Qty
        self.lblQty=Label(Prod_Frame,font=('times new roman',12,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        
        self.ComboQty=ttk.Entry(Prod_Frame,textvariable=self.qty,font=('times new roman',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        #middle frame
        
        # MiddleFrame=Frame(Main_Frame,bd=10)
        # MiddleFrame.place(x=10,y=150,width=980,height=340)
        
        # # # img1
        # img12=Image.open("image/good.jpeg")
        # img12=img12.resize((490,340),Image.ANTIALIAS)
        # self.photoimg12=ImageTk.PhotoImage(img12)
        
        # lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        # lbl_img12.place(x=0,y=0,width=490,height=340)
        
        
        # #img13
        
        # img13=Image.open("image/mall.jpeg")
        # img13=img12.resize((490,340),Image.ANTIALIAS)
        # self.photoimg13=ImageTk.PhotoImage(img13)
        
        
        # lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        # lbl_img13.place(x=490,y=0,width=500,height=340)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # SEARCH Search_
        Search_frame=Frame(Main_Frame,bd=2,bg="white")
        Search_frame.place(x=990,y=10,width=500,height=40)
        
        self.lblBill=Label(Search_frame,font=('times new roman',12,'bold'),bg="red",text="BILL NUMBER")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)
        
        self.txt_Entry_Search=ttk.Entry(Search_frame,textvariable=self.search_bill,font=('times new roman',15,'bold'),width=16)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)
        
        self.btnSearch=Button(Search_frame,command=self.find_bill,text="SEARCH",font=('times new roman',10,'bold'),bg="orangered",fg="white",width=10,cursor="hand2")
        self.btnSearch.grid(row=0,column=2)
        
        
        
        
        # Rightframe bill area
        RightLabelFrame=LabelFrame(Main_Frame,text="BILL AREA",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=955,y=45,width=405,height=440)
        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        # Bill counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="BILL COUNTER",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1400,height=125)
        
        self.lblSubTotal=Label(Bottom_Frame,font=('times new roman',12,'bold'),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.EntySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('times new roman',10,'bold'),width=24)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.lbl_tax=Label(Bottom_Frame,font=('times new roman',12,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('times new roman',10,'bold'),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblAmountTotal=Label(Bottom_Frame,font=('times new roman',12,'bold'),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('times new roman',10,'bold'),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        # button frame
        btn_frame=Frame(Bottom_Frame,bd=2,bg="white")
        btn_frame.place(x=320,y=0)
        
        self.btnAddToCart=Button(btn_frame,command=self.Additem,text="ADD TO CART",font=('times new roman',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btnAddToCart.grid(row=0,column=0)
        
        self.btngenerate_bill=Button(btn_frame,command=self.gen_bill,text="GENERATE BILL",font=('times new roman',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.btngenerate_bill.grid(row=0,column=1)
        
        self.btnSave=Button(btn_frame,text="SAVE",command=self.save_bill,font=('times new roman',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnSave.grid(row=0,column=2)
        
        self.btnPrint=Button(btn_frame,text="PRINT",command=self.iprint,font=('times new roman',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnPrint.grid(row=0,column=3)
        
        self.btnClear=Button(btn_frame,text="CLEAR",command=self.clear,font=('times new roman',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnClear.grid(row=0,column=4)
        
        self.btnExit=Button(btn_frame,text="EXIT",command=self.root.destroy,font=('times new roman',15,'bold'),bg="orangered",fg="white",width=12,cursor="hand2")
        self.btnExit.grid(row=0,column=5)
        
        self.welcome()
        self.l=[]
        
        
    def Additem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n  {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('RS.%.2f'%(sum(self.l))))
            self.tax_input.set(str('RS.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('RS.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
    
    
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ===================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n =================================================== \n")
            
            
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You WAnt To Save The Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w') 
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saveed",f"BILL NO:{self.bill_no.get()} saved successfully")
            f1.close()
    
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
    
    
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invaild Bill Number")
    
    
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()
        
        
    
    
    
    
            
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END," \t WELCOME PATEL MART")    
        self.textarea.insert(END,f"\n BILL NUMBER: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n CUSTOMER NAME: {self.c_name.get()}")
        self.textarea.insert(END,f"\n PHONE NUMBER: {self.c_phon.get()}")
        self.textarea.insert(END,f"\n CUSTOMER EMAIL: {self.c_email.get()}")
        
        
        self.textarea.insert(END,"\n===================================================")
        self.textarea.insert(END,f"\n PRODUCTS\t\tQTY\t\tPRICE")
        self.textarea.insert(END,"\n===================================================")
        
        
    def categories(self,events=""):
        if self.Combo_Category.get()=="Clothing":
            self.Combo_SubCategory.config(value=self.SubCatClothing)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="LifeStyle":
            self.Combo_SubCategory.config(value=self.SubCatLifeStyle)
            self.Combo_SubCategory.current(0)
        
        if self.Combo_Category.get()=="Mobiles":
            self.Combo_SubCategory.config(value=self.SubCatMobiles)
            self.Combo_SubCategory.current(0)
        
    
    def Product_add(self,events=""):
        if self.Combo_SubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)
        
        if self.Combo_SubCategory.get()=="T-Shirt":
            self.ComboProduct.config(value=self.t_shirt)
            self.ComboProduct.current(0)
        
        if self.Combo_SubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)
        
        # lifestyle
        # 
        if self.Combo_SubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.bath_soap)
            self.ComboProduct.current(0)
            
        if self.Combo_SubCategory.get()=="Face Creame":
            self.ComboProduct.config(value=self.Face_Creame)
            self.ComboProduct.current(0)
            
        if self.Combo_SubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)
            
        if self.Combo_SubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)
            
        if self.Combo_SubCategory.get()=="Sumsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)
            
        if self.Combo_SubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)
            
        if self.Combo_SubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0) 
        
        if self.Combo_SubCategory.get()=="One+":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)
            
            
    def price(self,event=""):
        #pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
            # t-shirt
        
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Jack & Jones":
            self.ComboPrice.config(value=self.price_jackjones)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
            # shirt
        
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_park)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        #bath_soap
        
        if self.ComboProduct.get()=="Lifebuy":
            self.ComboPrice.config(value=self.price_Lifebuy)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_Lux)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_Santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Pearl":
            self.ComboPrice.config(value=self.price_Pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        # face creame
        
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_Ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        
        # Hair_oil
        
        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_Parachute)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_Bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Jashmin":
            self.ComboPrice.config(value=self.price_Jashmin)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        # Iphone
        if self.ComboProduct.get()=="Iphone x":
            self.ComboPrice.config(value=self.price_Iphone_x)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Iphone 11":
            self.ComboPrice.config(value=self.price_Iphone_11)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Iphone 12":
            self.ComboPrice.config(value=self.price_Iphone_12)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # Samsung
        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_M16)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        
        if self.ComboProduct.get()=="Samsung M12":
            self.ComboPrice.config(value=self.price_M12)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        
        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_M21)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        # Xiome
        if self.ComboProduct.get()=="Redmi 11":
            self.ComboPrice.config(value=self.price_rm11)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        if self.ComboProduct.get()=="Redmi 12":
            self.ComboPrice.config(value=self.price_rm12)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        if self.ComboProduct.get()=="Redmi PRO":
            self.ComboPrice.config(value=self.price_rmpro)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        # RealMe
        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_r13)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_rProk)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        # OnePlus
        if self.ComboProduct.get()=="OnePlus 1":
                self.ComboPrice.config(value=self.price_OnePlus1)
                self.ComboPrice.current(0)
                self.qty.set(1)     
        
        if self.ComboProduct.get()=="OnePlus 2":
            self.ComboPrice.config(value=self.price_OnePlus2)
            self.ComboPrice.current(0)
            self.qty.set(1)     
        
        if self.ComboProduct.get()=="OnePlus 3":
            self.ComboPrice.config(value=self.price_OnePlus3)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
if __name__ =='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop() 