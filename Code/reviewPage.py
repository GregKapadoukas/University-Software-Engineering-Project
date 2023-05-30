import customtkinter as ctk
from review import Review
from user import User
from transaction import Transaction

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ReviewPage():
    def __init__(self, transaction:Transaction, reviewer:User):
        self.__transaction = transaction
        self.__reviewer = reviewer

        if transaction.getOwner() != reviewer:
            self.__reviewee = transaction.getOwner()
        else:
            self.__reviewee = transaction.getRenter()
            
        self.__root=ctk.CTk()
        self.__pageText = ctk.CTkLabel(self.__root, text="Please Select Your Review Type:", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=20, pady=20)
        
        self.__buttonframe=ctk.CTkFrame(self.__root)
        self.__buttonframe.columnconfigure(0,weight=1)
        self.__button1=ctk.CTkButton(self.__buttonframe,compound='left',height=250,width=250,text="Star based review",fg_color="black",command=self.starReview)
        self.__button1.grid(row=0,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)
        self.__button2=ctk.CTkButton(self.__buttonframe,compound="right",height=250,width=250,text="Comment",command=self.bothReview)
        self.__button2.grid(row=0,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)
        self.__buttonframe.pack(padx = 20, pady = 20)

        self.__starFrame=ctk.CTkFrame(self.__root)
        self.__commentFrame=ctk.CTkFrame(self.__root)

        self.__score = 0

        
        self.__root.mainloop()

    def starReview(self):
        self.clearFrames()

        self.__checkButtonvariable=ctk.IntVar()

        self.__zerostar=ctk.CTkButton(self.__starFrame,text="0",command=lambda score=0: self.updateStarScore(score,0))
        self.__zerostar.grid(row=0,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__halfstar=ctk.CTkButton(self.__starFrame,text="0.5",command=lambda score=0.5: self.updateStarScore(score,0))
        self.__halfstar.grid(row=0,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__onestar=ctk.CTkButton(self.__starFrame,text="1",command=lambda score=1: self.updateStarScore(score,0))
        self.__onestar.grid(row=1,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__onehalfstar=ctk.CTkButton(self.__starFrame,text="1.5",command=lambda score=1.5: self.updateStarScore(score,0))
        self.__onehalfstar.grid(row=1,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)
      
        self.__twostar=ctk.CTkButton(self.__starFrame,text='2',command=lambda score=2: self.updateStarScore(score,0))
        self.__twostar.grid(row=2,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__twohalfstar=ctk.CTkButton(self.__starFrame,text='2.5',command=lambda score=2.5: self.updateStarScore(score,0))
        self.__twohalfstar.grid(row=2,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__threestar=ctk.CTkButton(self.__starFrame,text='3',command=lambda score=3: self.updateStarScore(score,0))
        self.__threestar.grid(row=3,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__threehalfstar=ctk.CTkButton(self.__starFrame,text='3.5',command=lambda score=3.5: self.updateStarScore(score,0))
        self.__threehalfstar.grid(row=3,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__fourstar=ctk.CTkButton(self.__starFrame,text='4',command=lambda score=4: self.updateStarScore(score,0))
        self.__fourstar.grid(row=4,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__fourhalfstar=ctk.CTkButton(self.__starFrame,text='4.5',command=lambda score=4.5: self.updateStarScore(score,0))
        self.__fourhalfstar.grid(row=4,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__fivestar=ctk.CTkButton(self.__starFrame,text='5',command=lambda score=5: self.updateStarScore(score,0))
        self.__fivestar.grid(row=5,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)


        self.__applybutton=ctk.CTkButton(self.__starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.__transaction, reviewer=self.__reviewer, reviewee=self.__reviewee, score=self.__score, text='':
                                       transaction.addReview(reviewer, reviewee, score, text))
        self.__applybutton.grid(row=5,column=1)
        self.__starFrame.pack()

    def bothReview(self):
        self.clearFrames()

        self.__checkButtonVariable=ctk.IntVar()

        self.__zerostar=ctk.CTkButton(self.__starFrame,text="0",command=lambda score=0: self.updateStarScore(score,1))
        self.__zerostar.grid(row=0,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__halfstar=ctk.CTkButton(self.__starFrame,text="0.5",command=lambda score=0.5: self.updateStarScore(score,1))
        self.__halfstar.grid(row=1,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__onestar=ctk.CTkButton(self.__starFrame,text="1",command=lambda score=1: self.updateStarScore(score,1))
        self.__onestar.grid(row=0,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__onehalfstar=ctk.CTkButton(self.__starFrame,text="1.5",command=lambda score=1.5: self.updateStarScore(score,1))
        self.__onehalfstar.grid(row=1,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)
      
        self.__twostar=ctk.CTkButton(self.__starFrame,text='2',command=lambda score=2: self.updateStarScore(score,1))
        self.__twostar.grid(row=0,column=2,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__twohalfstar=ctk.CTkButton(self.__starFrame,text='2.5',command=lambda score=2.5: self.updateStarScore(score,1))
        self.__twohalfstar.grid(row=1,column=2,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__threestar=ctk.CTkButton(self.__starFrame,text='3',command=lambda score=3: self.updateStarScore(score,1))
        self.__threestar.grid(row=0,column=3,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__threehalfstar=ctk.CTkButton(self.__starFrame,text='3.5',command=lambda score=3.5: self.updateStarScore(score,1))
        self.__threehalfstar.grid(row=1,column=3,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__fourstar=ctk.CTkButton(self.__starFrame,text='4',command=lambda score=4: self.updateStarScore(score,1))
        self.__fourstar.grid(row=0,column=4,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__fourhalfstar=ctk.CTkButton(self.__starFrame,text='4.5',command=lambda score=4.5: self.updateStarScore(score,1))
        self.__fourhalfstar.grid(row=1,column=4,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__fivestar=ctk.CTkButton(self.__starFrame,text='5',command=lambda score=5: self.updateStarScore(score,1))
        self.__fivestar.grid(row=0,column=5,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__entry=ctk.CTkEntry(self.__commentFrame,height=300,width=400)
        self.__entry.pack(padx=10,pady=10)

        self.__applybutton=ctk.CTkButton(self.__starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.__transaction, reviewer=self.__reviewer, reviewee=self.__reviewee, score=self.__score, text=self.__entry.get():
                                       transaction.addReview(reviewer, reviewee, score, text))
        self.__applybutton.grid(row=1,column=5)

        self.__commentFrame.pack()
        self.__starFrame.pack()

    def clearFrames(self):
        for widget in self.__starFrame.winfo_children():
            widget.destroy()
        for widget in self.__commentFrame.winfo_children():
            widget.destroy()
        self.__starFrame.pack_forget()
        self.__commentFrame.pack_forget()
    
    def updateStarScore(self, score, mode):
        self.__score = score
        self.__applybutton.destroy()
        if mode == 0:
            self.__applybutton=ctk.CTkButton(self.__starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.__transaction, reviewer=self.__reviewer, reviewee=self.__reviewee, score=self.__score, text='':
                                       transaction.addReview(reviewer, reviewee, score, text))
            self.__applybutton.grid(row=5,column=1)
            self.__applybutton.grid(row=5,column=1)
        else:
            self.__applybutton=ctk.CTkButton(self.__starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.__transaction, reviewer=self.__reviewer, reviewee=self.__reviewee, score=self.__score, text=self.__entry.get():
                                       transaction.addReview(reviewer, reviewee, score, text))
            self.__applybutton.grid(row=1,column=5)
