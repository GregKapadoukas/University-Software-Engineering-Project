import customtkinter as ctk
import datetime
from address import Address
from book import Book
from bookOffer import BookOffer
from bookRequest import BookRequest
from city import City
from favorite import Favorite
from listing import Listing, DeliveryType
from notification import Notification
from review import Review
from transaction import Transaction
from user import User
from searchPage import SearchPage
from dashboardPage import DashboardPage
import globals

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class GUI(ctk.CTk):
    def __init__(self, *args, **kwargs):

        ctk.CTk.__init__(self, *args, **kwargs)

        self.title("LibShare")

        label=ctk.CTkLabel(self, text="LibShare", font=("Arial", 35), text_color="#3A7ABF")
        label.pack(padx=10, pady=10)

        # Navigation Buttons
        buttonframe = ctk.CTkFrame(self)
        buttonframe.columnconfigure(0, weight=1)

        navSearchButton = ctk.CTkButton(buttonframe, text="Search", 
                                        command=lambda : self.show_frame(SearchPage))
        navSearchButton.grid(row=0, column=0, sticky=ctk.W+ctk.E)

        navDashboardButton = ctk.CTkButton(buttonframe, text="Dashboard", 
                                        command=lambda : self.show_frame(DashboardPage))
        navDashboardButton.grid(row=0, column=1, sticky=ctk.W+ctk.E)

        navMyBookOffersButton = ctk.CTkButton(buttonframe, text="My Book Offers", 
                                        command=lambda : self.show_frame(MyBookOffersPage))
        navMyBookOffersButton.grid(row=0, column=2, sticky=ctk.W+ctk.E)

        navMyBookRequestsButton = ctk.CTkButton(buttonframe, text="My Book Requests", 
                                        command=lambda : self.show_frame(MyBookRequestsPage))
        navMyBookRequestsButton.grid(row=0, column=3, sticky=ctk.W+ctk.E)

        navMyFavoritesButton = ctk.CTkButton(buttonframe, text="My Favorites", 
                                        command=lambda : self.show_frame(MyFavoritesPage))
        navMyFavoritesButton.grid(row=0, column=4, sticky=ctk.W+ctk.E)

        navNotificationsButton = ctk.CTkButton(buttonframe, text="Notifications", 
                                        command=lambda : self.show_frame(NotificationsPage))
        navNotificationsButton.grid(row=0, column=5, sticky=ctk.W+ctk.E)

        navTransactionHistory = ctk.CTkButton(buttonframe, text="Transaction History", 
                                        command=lambda : self.show_frame(NotificationsPage))
        navTransactionHistory .grid(row=0, column=6, sticky=ctk.W+ctk.E)

        navMyProfileButton = ctk.CTkButton(buttonframe, text="My Profile", 
                                        command=lambda : self.show_frame(MyProfilePage))
        navMyProfileButton.grid(row=0, column=7, sticky=ctk.W+ctk.E)

        buttonframe.pack()

        # Creating a container
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting of the different page layouts
        for F in (SearchPage, DashboardPage, MyBookOffersPage, MyBookRequestsPage,
                  MyFavoritesPage, NotificationsPage, TransactionHistory, MyProfilePage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(SearchPage)


        # To display the current frame passed as parameter
    def show_frame(self, cont):
        self.frames = {}
        for F in (SearchPage, DashboardPage, MyBookOffersPage, MyBookRequestsPage,
                  MyFavoritesPage, NotificationsPage, TransactionHistory, MyProfilePage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")
        frame = self.frames[cont]
        frame.tkraise()

class MyBookOffersPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Book Offers")
        label.pack(padx=10, pady=10)

class MyBookRequestsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Book Requests")
        label.pack(padx=10, pady=10)

class MyFavoritesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Favorites")
        label.pack(padx=10, pady=10)

class NotificationsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.pageName = ctk.CTkLabel(self, text="Notifications", font=("Arial", 25), text_color="white",bg_color="#3A7ABF")
        self.pageName.pack(fill="x")
        
        def username1():
          
            
          Label6.destroy()
          Label7.destroy()
          Label8.destroy()
          Label9.destroy()
          Label10.destroy()
           
          
          
        
        buttf = ctk.CTkFrame(self)
        
        buttf.columnconfigure(0,weight=1)
        buttf.columnconfigure(1,weight=1)
        buttf.columnconfigure(2,weight=1)
        buttf.columnconfigure(3,weight=1)
        buttf.columnconfigure(4,weight=1)
        buttf.columnconfigure(5,weight=1)
        buttf.columnconfigure(6,weight=1)
        buttf.columnconfigure(7,weight=1)
        buttf.columnconfigure(8,weight=1)
        buttf.columnconfigure(9,weight=1)
        Button1= ctk.CTkButton(buttf,text="Remove User", text_color="red", bg_color="red",command=username1 )
        Button1.grid(row=1, column=5, sticky=ctk.E, columnspan = 1, rowspan = 1, padx=1, pady =1)
        
        Label1= ctk.CTkLabel(buttf,text="User") 
        Label1.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label2= ctk.CTkLabel(buttf,text="Book") 
        Label2.grid(row=0, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label3= ctk.CTkLabel(buttf,text="Author") 
        Label3.grid(row=0, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1 )
        Label4= ctk.CTkLabel(buttf,text="Price Per Day") 
        Label4.grid(row=0, column=3, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1)
        Label5= ctk.CTkLabel(buttf,text="Delivery Type") 
        Label5.grid(row=0, column=4, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1) 
        Label61= ctk.CTkLabel(buttf,text="Remove us") 
        Label61.grid(row=0, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1)
        
        Label6= ctk.CTkLabel(buttf,text="Greg") 
        Label6.grid(row=1, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label7= ctk.CTkLabel(buttf,text="David Cop") 
        Label7.grid(row=1, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label8= ctk.CTkLabel(buttf,text="Charles dic") 
        Label8.grid(row=1, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1 )
        Label9= ctk.CTkLabel(buttf,text="4 euros") 
        Label9.grid(row=1, column=3, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1)
        Label10= ctk.CTkLabel(buttf,text="Post") 
        Label10.grid(row=1, column=4, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1) 
       

         
        
        buttf.pack(side="top")


        
        
      
        
        




class TransactionHistory(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Transaction")
        label.pack(padx=10, pady=10)
      
class MyProfilePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)





        buttf = ctk.CTkFrame(self)
        buttf.columnconfigure(0,weight=1)
        buttf.columnconfigure(1,weight=1)
        buttf.columnconfigure(2,weight=1)
        buttf.columnconfigure(3,weight=1)
        buttf.columnconfigure(4,weight=1)
        buttf.columnconfigure(5,weight=1)
        buttf.columnconfigure(6,weight=1)
        buttf.columnconfigure(7,weight=1)
        buttf.columnconfigure(8,weight=1)
        buttf.columnconfigure(9,weight=1)







        def Pass1 ():
          def use1():
            Buttonn3.destroy()
            c1=text5.get("0.1","end")
            c2=text6.get("0.1","end")
            c3=text7.get("0.1","end")

            
            f = globals.currentUser.getPass() :
              
            
             
            
            if (c1 == c3):
              y=len(c1)
              if (y<35 and y>0):
                globals.currentUser.chPass(c1)
              
                
              #text5.destroy()
              #text6.destroy()
              #text7.destroy()
              else:
               
                popupWrong5()
               # text5.destroy()
                #text6.destroy()
                #text7.destroy()
            else:  
             
             # globals.currentUser.chPass(c1)
             # f=globals.currentUser.getPass()
             # print("1")
              
              popupWrong5()
              
            f=globals.currentUser.getPass()
           # print(f)
            text5.destroy()
            text6.destroy()
            text7.destroy()
          
          
          text5= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
          text5.grid(row=4, column=1, sticky=ctk.W)
          text6= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
          text6.grid(row=5, column=1, sticky=ctk.W)
          text7= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
          text7.grid(row=6, column=1, sticky=ctk.W)  
          Buttonn3= ctk.CTkButton(buttf,text="Store Pass",command=use1) 
          Buttonn3.grid(row=6, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
        
        def username1():
          def use1():
            
            c=text11.get("0.1","end")
            Buttonn1.destroy()
            text11.destroy()
            f=globals.currentUser.getFirstName()
            y=len(c)+1
            if y>21 or y <=1 :
              popupWrong()
            else :
              globals.currentUser.chFirstName(c)
              f=globals.currentUser.getFirstName()
              print(f)
          Buttonn1= ctk.CTkButton(buttf,text="Store Usname",command=use1) 
          Buttonn1.grid(row=0, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =1)
          text11= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=5)  
          text11.grid(row=0, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 50, pady =1)
         
        
        def location1():
          def use1():
            Buttonn3.destroy()
            c1=text11.get("0.1","end")
            
            f=globals.currentUser.getaddress()
            y=len(c1)
            if y>35 or y <=0 :
              popupWrong1()
            else :
              globals.currentUser.chaddress(c1)
              f=globals.currentUser.getaddress()
              print(f)
            text11.destroy()
          
          text11= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=5)  
          text11.grid(row=2, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 50, pady =1)
          Buttonn3= ctk.CTkButton(buttf,text="Store Loc",command=use1) 
          Buttonn3.grid(row=2, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
          
        def email1():
          def use1():
            c1=text11.get("0.1","end")
            Buttonn2.destroy()
            text11.destroy()
            f=globals.currentUser.getEmail()
            y=len(c1)
            if y>35 or y <=0 :
              popupWrong2()
            else :
              globals.currentUser.chEmail(c1)
              f=globals.currentUser.getEmail()
              print(f)
          Buttonn2= ctk.CTkButton(buttf,text="Store mail",command=use1) 
          Buttonn2.grid(row=1, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=15, pady =11)
          text11= ctk.CTkTextbox(buttf,width=185,height=4,corner_radius=5)  
          text11.grid(row=1, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 50, pady =1)
         

        
        
        def balance1():
          text11= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=5)  
          text11.grid(row=3, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 50, pady =1)


        def ps():
          text5.delete("1.0","end")
          text6.delete("1.0","end")
          text7.delete("1.0","end")
          text72.delete("1.0","end")
          text11.delete("1.0","end")
        def popup():
          popupwindow=ctk.CTkToplevel()
          popupwindow.title("Balacne edit")
          popupwindow.geometry("800x800")
          
          def add():
            
            c1= text7.get("0.1","end")
            c=int(c1)
            
            
            
            f=globals.currentUser.getBalance()
            
            if  c<0 :
              
              popupWrong3()
              
            else :
              h=c+f
              globals.currentUser.chBalance(h)
              
            f=globals.currentUser.getBalance()
            print(f)
            Label443= ctk.CTkLabel(buttf,text=f )
            popupwindow.destroy()
            Label443.grid(row=3, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 100, pady =2)
            Label44.destroy()
            
        
          def reduce():
            
            c1= text72.get("0.1","end")
            c=int(c1)
            
            
            
            f=globals.currentUser.getBalance()
            
            if  f-c<0 :
              
              popupWrong3()
              
            else :
              g=f-c
              globals.currentUser.chBalance(g)
              
            f=globals.currentUser.getBalance()
            print(f)
            Label443= ctk.CTkLabel(buttf,text=f )
            popupwindow.destroy()
            Label443.grid(row=3, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 100, pady =2)
            Label44.destroy()
            
            
          label9=ctk.CTkLabel(popupwindow,text="Enter amount")
          
          buttonP=ctk.CTkButton(popupwindow,text="add",command=add)
          
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          
          text7= ctk.CTkTextbox(popupwindow,width=150,height=4,corner_radius=10) 
          
          text7.grid(row=1, column=0, sticky=ctk.W)
          
          buttonP.grid(row=2, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 1, pady =1)

          
          
          label92=ctk.CTkLabel(popupwindow,text="Enter amount")
          
          buttonP2=ctk.CTkButton(popupwindow,text="reduce/remove",command=reduce)
          
          label92.grid(row=0, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          
          text72= ctk.CTkTextbox(popupwindow,width=150,height=4,corner_radius=10) 
          
          text72.grid(row=1, column=1, sticky=ctk.W)
          
          buttonP2.grid(row=2, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 1, pady =1)
          
          
          
          
            
          
          popupwindow.mainloop() 
        
        buttf = ctk.CTkFrame(self)
        buttf.columnconfigure(0,weight=1)
        buttf.columnconfigure(1,weight=1)
        buttf.columnconfigure(2,weight=1)
        buttf.columnconfigure(3,weight=1)
        buttf.columnconfigure(4,weight=1)
        buttf.columnconfigure(5,weight=1)
        buttf.columnconfigure(6,weight=1)
        buttf.columnconfigure(7,weight=1)
        buttf.columnconfigure(8,weight=1)
        buttf.columnconfigure(9,weight=1)
        Button1= ctk.CTkButton(buttf,text="edit",command=username1) 
        Button1.grid(row=0, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =1)
        
        Label1= ctk.CTkLabel(buttf,text="username") 
        Label1.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)

        Label11= ctk.CTkLabel(buttf,text="Christos") 
        Label11.grid(row=0, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 100, pady =1)

        Button2= ctk.CTkButton(buttf,text="edit",command=email1) 
        Button2.grid(row=1, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=15, pady =11)
        
        Label2= ctk.CTkLabel(buttf,text="email") 
        Label2.grid(row=1, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=15, pady =11 )
        Label22= ctk.CTkLabel(buttf,text="books2011@gmail.com") 
        Label22.grid(row=1, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 100, pady =2) 
  
        
        Button3= ctk.CTkButton(buttf,text="edit",command=location1) 
        Button3.grid(row=2, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)


    
        Label3= ctk.CTkLabel(buttf,text="location") 
        Label3.grid(row=2, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
        Label33= ctk.CTkLabel(buttf,text="Athens") 
        Label33.grid(row=2, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 100, pady =2) 

        
        
        Label4= ctk.CTkLabel(buttf,text="Balance") 
        Label4.grid(row=3, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
        


        Button5= ctk.CTkButton(buttf,text="edit pass",command=Pass1) 
        Button5.grid(row=6, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
        
        Label5= ctk.CTkLabel(buttf,text="new pass") 
        Label5.grid(row=4, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)

        

        Label6= ctk.CTkLabel(buttf,text="old pass") 
        Label6.grid(row=5, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)

        

        Label7= ctk.CTkLabel(buttf,text="new pass") 
        Label7.grid(row=6, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)

        Label44= ctk.CTkLabel(buttf,text=globals.currentUser.getBalance()) 
        Label44.grid(row=3, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 100, pady =2)
        
        
        buttf.pack(side="top")

        


        def phone1():
          
          def use1():
            
            c= text11.get("0.1","end")
            c1=int(c)
            
            f=globals.currentUser.getPhone_num()
            
            if c1>999999999999999 or c1 <=0 :
              popupWrong3()
            else :
              globals.currentUser.chPhone_num(c1)
              f=globals.currentUser.getPhone_num()
            text11.destroy()
            print(f)
            Buttonn3.destroy()
          text11= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=5)  
          text11.grid(row=6, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 1, pady =1)
          Buttonn3= ctk.CTkButton(buttf,text="Store num",command=use1) 
          Buttonn3.grid(row=5, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =1)








        

        button3= ctk.CTkButton(buttf,text="edit phone_num",command=phone1) 
        button3.grid(row=5, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =1)








        

          





        

        

        button1= ctk.CTkButton(buttf,text="edit Picture") 
        button1.grid(row=2, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)
        
        label1= ctk.CTkLabel(buttf,text="holder  for profile  pic") 
        label1.grid(row=0, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)

        button2= ctk.CTkButton(buttf,text="edit Balance",command=popup) 
        button2.grid(row=3, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)

        
      

        





        def Descr1():
          
          def use1():
            
            c= text11.get("0.1","end")
            
            
            f=globals.currentUser.getDescr()
            
            y=len(c)
            if y>150 or y <=0 :
              popupWrong4()
            
            else :
              globals.currentUser.chDescr(c)
              f=globals.currentUser.getDescr()
            text11.destroy()
            print(f)
            Buttonn3.destroy()
          text11= ctk.CTkTextbox(buttf,width=300,height=20,corner_radius=20)  
          text11.grid(row=6, column=6, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 1, pady =1)
          Buttonn3= ctk.CTkButton(buttf,text="Store Descr",command=use1) 
          Buttonn3.grid(row=5, column=6, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =1)

 






        

        button3= ctk.CTkButton(buttf,text="edit Descr",command=Descr1) 
        button3.grid(row=5, column=6, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =1)
























        
        
        

        
        

        def storePass():
         Buttonn5= ctk.CTkButton(buttf,text="store pass") 
         Buttonn5.grid(row=6, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
        pass
       
        def storePic():
         buttonnn1= ctk.CTkButton(buttf,text="store Picture") 
         buttonnn1.grid(row=2, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)
        pass
       
        def storeBal():
         buttonnn1= ctk.CTkButton(buttf,text="store Balance") 
         buttonnn1.grid(row=3, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)
        pass


      
       

        #text5= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
        #text5.grid(row=4, column=1, sticky=ctk.W)

        

        #text6= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
        #text6.grid(row=5, column=1, sticky=ctk.W)

        

        #text7= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
        #text7.grid(row=6, column=1, sticky=ctk.W)  

   
        def popupWrong():
          popupwindow1=ctk.CTkToplevel()
          popupwindow1.title("Eror")
          popupwindow1.geometry("800x800")
          label9=ctk.CTkLabel(popupwindow1,text="invalid username.")
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          popupwindow1.mainloop() 

        def popupWrong1():
          popupwindow1=ctk.CTkToplevel()
          popupwindow1.title("Eror")
          popupwindow1.geometry("800x800")
          label9=ctk.CTkLabel(popupwindow1,text="invalid location.")
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          popupwindow1.mainloop() 
       
        def popupWrong2():
          popupwindow1=ctk.CTkToplevel()
          popupwindow1.title("Eror")
          popupwindow1.geometry("800x800")
          label9=ctk.CTkLabel(popupwindow1,text="invalid email.")
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          popupwindow1.mainloop() 

        def popupWrong3():
          popupwindow1=ctk.CTkToplevel()
          popupwindow1.title("Eror")
          popupwindow1.geometry("800x800")
          label9=ctk.CTkLabel(popupwindow1,text="invalid number.")
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          popupwindow1.mainloop() 

        def popupWrong0():
          popupwindow1=ctk.CTkToplevel()
          popupwindow1.title("Eror")
          popupwindow1.geometry("800x800")
          label9=ctk.CTkLabel(popupwindow1,text="invalid number.")
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          popupwindow1.mainloop() 

        def popupWrong4():
          popupwindow1=ctk.CTkToplevel()
          popupwindow1.title("Eror")
          popupwindow1.geometry("800x800")
          label9=ctk.CTkLabel(popupwindow1,text="invalid Characters or big text")
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          popupwindow1.mainloop() 

        def popupWrong5():
          popupwindow1=ctk.CTkToplevel()
          popupwindow1.title("Eror")
          popupwindow1.geometry("800x800")
          label9=ctk.CTkLabel(popupwindow1,text="invalid Characters or wrong old pass")
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          
          popupwindow1.mainloop() 
