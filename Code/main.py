from re import search
from typing import Optional, Tuple, Union
import customtkinter as ctk

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

        editButton = ctk.CTkButton(buttonframe, text="edit", 
                                        command=lambda : self.show_frame(SearchPage))
        editButton.grid(row=0, column=0, sticky=ctk.W)

        navSearchButton = ctk.CTkButton(buttonframe, text="Search", 
                                        command=lambda : self.show_frame(SearchPage))
        navSearchButton.grid(row=0, column=0, sticky=ctk.W+ctk.E)

        navDashboardButton = ctk.CTkButton(buttonframe, text="Dashboard", 
                                        command=lambda : self.show_frame(Dashboard))
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
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)


        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting of the different page layouts
        for F in (SearchPage, Dashboard, MyBookOffersPage, MyBookRequestsPage,
                  MyFavoritesPage, NotificationsPage, TransactionHistory, MyProfilePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(SearchPage)


        # To display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    
 
class SearchPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.pageName = ctk.CTkLabel(self, text="Please Enter Your Search Term", font=("Arial", 25), text_color="#3A7ABF")
        self.pageName.pack(padx=20, pady=20)

        self.searchframe = ctk.CTkFrame(self)
        self.searchframe .columnconfigure(0, weight=1)

        self.searchEntry = ctk.CTkEntry(self.searchframe, placeholder_text="Enter Search Term")
        self.searchEntry.grid(row=0, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.searchButton = ctk.CTkButton(self.searchframe, text="Search", command=self.get_search_term)
        self.searchButton.grid(row=0, column=1, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.radiobutton_variable = ctk.StringVar()

        self.chooseBooks = ctk.CTkRadioButton(self.searchframe, text="Books", variable=self.radiobutton_variable)
        self.chooseBooks.grid(row=1, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.chooseUser = ctk.CTkRadioButton(self.searchframe, text="Users", variable=self.radiobutton_variable)
        self.chooseUser .grid(row=2, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.chooseRequest = ctk.CTkRadioButton(self.searchframe, text="Requests", variable=self.radiobutton_variable)
        self.chooseRequest.grid(row=3, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.searchframe.pack()

    def get_search_term(self):
        print(self.searchEntry.get())


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Dashboard")
        label.pack(padx=10, pady=10)

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
        label = ctk.CTkLabel(self, text="Notifications")
        label.pack(padx=10, pady=10)

class TransactionHistory(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Transaction History")
        label.pack(padx=10, pady=10)

class MyProfilePage(ctk.CTkFrame):

      
      
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        
        def username1():
          def use1():
            Buttonn1.destroy()
            text11.destroy()
          Buttonn1= ctk.CTkButton(buttf,text="Store Usname",command=use1) 
          Buttonn1.grid(row=0, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =1)
          text11= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=5)  
          text11.grid(row=0, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 50, pady =1)
          
          
        def email1():
          def use1():
            Buttonn2.destroy()
            text11.destroy()
          Buttonn2= ctk.CTkButton(buttf,text="Store mail",command=use1) 
          Buttonn2.grid(row=1, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=15, pady =11)
          text11= ctk.CTkTextbox(buttf,width=185,height=4,corner_radius=5)  
          text11.grid(row=1, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 50, pady =1)
         

        def location1():
          def use1():
            Buttonn3.destroy()
            text11.destroy()
          text11= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=5)  
          text11.grid(row=2, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 50, pady =1)
          Buttonn3= ctk.CTkButton(buttf,text="Store Loc",command=use1) 
          Buttonn3.grid(row=2, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
        
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
          
        
          
          
          label9=ctk.CTkLabel(popupwindow,text="Enter amount")
          
          buttonP=ctk.CTkButton(popupwindow,text="add",command=popupwindow.destroy)
          
          label9.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 14, pady =1)
          
          text7= ctk.CTkTextbox(popupwindow,width=150,height=4,corner_radius=10) 
          
          text7.grid(row=1, column=0, sticky=ctk.W)
          
          buttonP.grid(row=2, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 1, pady =1)

          
          
          label92=ctk.CTkLabel(popupwindow,text="Enter amount")
          
          buttonP2=ctk.CTkButton(popupwindow,text="reduce/remove",command=popupwindow.destroy)
          
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
        Label44= ctk.CTkLabel(buttf,text="10.00€") 
        Label44.grid(row=3, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 100, pady =2)


        Button5= ctk.CTkButton(buttf,text="edit",command=ps) 
        Button5.grid(row=6, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)
        
        Label5= ctk.CTkLabel(buttf,text="new pass") 
        Label5.grid(row=4, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)

        text5= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
        text5.grid(row=4, column=1, sticky=ctk.W)

        Label6= ctk.CTkLabel(buttf,text="old pass") 
        Label6.grid(row=5, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)

        text6= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
        text6.grid(row=5, column=1, sticky=ctk.W)

        Label7= ctk.CTkLabel(buttf,text="new pass") 
        Label7.grid(row=6, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=14, pady =11)

        text7= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10) 
        text7.grid(row=6, column=1, sticky=ctk.W)  
        
        buttf.pack(side="top")

        

        button1= ctk.CTkButton(buttf,text="edit Picture") 
        button1.grid(row=2, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)
        
        label1= ctk.CTkLabel(buttf,text="holder  for profile  pic") 
        label1.grid(row=0, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)

        button2= ctk.CTkButton(buttf,text="edit Balance",command=popup) 
        button2.grid(row=3, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)











        
        
        

        
        

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
         buttonnn2.grid(row=3, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=1, pady =11)
        pass


      
    
app = GUI()
app.mainloop()
