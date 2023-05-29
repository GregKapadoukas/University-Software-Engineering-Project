import customtkinter as ctk
from review import Review
from user import User
from transaction import Transaction

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ReviewPage():
    def __init__(self, transaction:Transaction, reviewer:User):
        self.transaction = transaction
        self.reviewer = reviewer

        if transaction.getOwner() != reviewer:
            self.reviewee = transaction.getOwner()
        else:
            self.reviewee = transaction.getRenter()
            
        self.root=ctk.CTk()
        self.pageText = ctk.CTkLabel(self.root, text="Please Select Your Review Type:", font=("Arial", 25), text_color="#3A7ABF")
        self.pageText.pack(padx=20, pady=20)
        
        self.buttonframe=ctk.CTkFrame(self.root)
        self.buttonframe.columnconfigure(0,weight=1)
        self.button1=ctk.CTkButton(self.buttonframe,compound='left',height=250,width=250,text="Star based review",fg_color="black",command=self.starReview)
        self.button1.grid(row=0,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)
        self.button2=ctk.CTkButton(self.buttonframe,compound="right",height=250,width=250,text="Comment",command=self.bothReview)
        self.button2.grid(row=0,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)
        self.buttonframe.pack(padx = 20, pady = 20)

        self.starFrame=ctk.CTkFrame(self.root)
        self.commentFrame=ctk.CTkFrame(self.root)

        self.score = 0

        
        self.root.mainloop()

    def starReview(self):
        self.clearFrames()

        self.checkButtonvariable=ctk.IntVar()

        self.zerostar=ctk.CTkButton(self.starFrame,text="0",command=lambda score=0: self.updateStarScore(score,0))
        self.zerostar.grid(row=0,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.halfstar=ctk.CTkButton(self.starFrame,text="0.5",command=lambda score=0.5: self.updateStarScore(score,0))
        self.halfstar.grid(row=0,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.onestar=ctk.CTkButton(self.starFrame,text="1",command=lambda score=1: self.updateStarScore(score,0))
        self.onestar.grid(row=1,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.onehalfstar=ctk.CTkButton(self.starFrame,text="1.5",command=lambda score=1.5: self.updateStarScore(score,0))
        self.onehalfstar.grid(row=1,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)
      
        self.twostar=ctk.CTkButton(self.starFrame,text='2',command=lambda score=2: self.updateStarScore(score,0))
        self.twostar.grid(row=2,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.twohalfstar=ctk.CTkButton(self.starFrame,text='2.5',command=lambda score=2.5: self.updateStarScore(score,0))
        self.twohalfstar.grid(row=2,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.threestar=ctk.CTkButton(self.starFrame,text='3',command=lambda score=3: self.updateStarScore(score,0))
        self.threestar.grid(row=3,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.threehalfstar=ctk.CTkButton(self.starFrame,text='3.5',command=lambda score=3.5: self.updateStarScore(score,0))
        self.threehalfstar.grid(row=3,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.fourstar=ctk.CTkButton(self.starFrame,text='4',command=lambda score=4: self.updateStarScore(score,0))
        self.fourstar.grid(row=4,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.fourhalfstar=ctk.CTkButton(self.starFrame,text='4.5',command=lambda score=4.5: self.updateStarScore(score,0))
        self.fourhalfstar.grid(row=4,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.fivestar=ctk.CTkButton(self.starFrame,text='5',command=lambda score=5: self.updateStarScore(score,0))
        self.fivestar.grid(row=5,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)


        self.applybutton=ctk.CTkButton(self.starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.transaction, reviewer=self.reviewer, reviewee=self.reviewee, score=self.score, text='':
                                       transaction.addReview(reviewer, reviewee, score, text))
        self.applybutton.grid(row=5,column=1)
        self.starFrame.pack()

    def bothReview(self):
        self.clearFrames()

        self.checkButtonVariable=ctk.IntVar()

        self.zerostar=ctk.CTkButton(self.starFrame,text="0",command=lambda score=0: self.updateStarScore(score,1))
        self.zerostar.grid(row=0,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.halfstar=ctk.CTkButton(self.starFrame,text="0.5",command=lambda score=0.5: self.updateStarScore(score,1))
        self.halfstar.grid(row=1,column=0,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.onestar=ctk.CTkButton(self.starFrame,text="1",command=lambda score=1: self.updateStarScore(score,1))
        self.onestar.grid(row=0,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.onehalfstar=ctk.CTkButton(self.starFrame,text="1.5",command=lambda score=1.5: self.updateStarScore(score,1))
        self.onehalfstar.grid(row=1,column=1,sticky=ctk.W+ctk.E, padx=10, pady=10)
      
        self.twostar=ctk.CTkButton(self.starFrame,text='2',command=lambda score=2: self.updateStarScore(score,1))
        self.twostar.grid(row=0,column=2,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.twohalfstar=ctk.CTkButton(self.starFrame,text='2.5',command=lambda score=2.5: self.updateStarScore(score,1))
        self.twohalfstar.grid(row=1,column=2,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.threestar=ctk.CTkButton(self.starFrame,text='3',command=lambda score=3: self.updateStarScore(score,1))
        self.threestar.grid(row=0,column=3,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.threehalfstar=ctk.CTkButton(self.starFrame,text='3.5',command=lambda score=3.5: self.updateStarScore(score,1))
        self.threehalfstar.grid(row=1,column=3,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.fourstar=ctk.CTkButton(self.starFrame,text='4',command=lambda score=4: self.updateStarScore(score,1))
        self.fourstar.grid(row=0,column=4,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.fourhalfstar=ctk.CTkButton(self.starFrame,text='4.5',command=lambda score=4.5: self.updateStarScore(score,1))
        self.fourhalfstar.grid(row=1,column=4,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.fivestar=ctk.CTkButton(self.starFrame,text='5',command=lambda score=5: self.updateStarScore(score,1))
        self.fivestar.grid(row=0,column=5,sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.entry=ctk.CTkEntry(self.commentFrame,height=300,width=400)
        self.entry.pack(padx=10,pady=10)

        self.applybutton=ctk.CTkButton(self.starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.transaction, reviewer=self.reviewer, reviewee=self.reviewee, score=self.score, text=self.entry.get():
                                       transaction.addReview(reviewer, reviewee, score, text))
        self.applybutton.grid(row=1,column=5)

        self.commentFrame.pack()
        self.starFrame.pack()

    def clearFrames(self):
        for widget in self.starFrame.winfo_children():
            widget.destroy()
        for widget in self.commentFrame.winfo_children():
            widget.destroy()
        self.starFrame.pack_forget()
        self.commentFrame.pack_forget()
    
    def updateStarScore(self, score, mode):
        self.score = score
        self.applybutton.destroy()
        if mode == 0:
            self.applybutton=ctk.CTkButton(self.starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.transaction, reviewer=self.reviewer, reviewee=self.reviewee, score=self.score, text='':
                                       transaction.addReview(reviewer, reviewee, score, text))
            self.applybutton.grid(row=5,column=1)
            self.applybutton.grid(row=5,column=1)
        else:
            self.applybutton=ctk.CTkButton(self.starFrame,text="Apply",fg_color="Green",command=
                                       lambda transaction=self.transaction, reviewer=self.reviewer, reviewee=self.reviewee, score=self.score, text=self.entry.get():
                                       transaction.addReview(reviewer, reviewee, score, text))
            self.applybutton.grid(row=1,column=5)
