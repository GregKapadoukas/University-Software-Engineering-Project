import customtkinter as ctk
import globals


class MyProfilePage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.__pageText = ctk.CTkLabel(self, text="My Profile", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=20, pady=20)

        self.__userDetails = ctk.CTkFrame(self)
        self.__userDetails.columnconfigure(9, weight=1)

        self.__userDetails = ctk.CTkFrame(self)
        self.__userDetails.columnconfigure(9, weight=1)
        self.__changeUsernameButton = ctk.CTkButton(self.__userDetails, text='Edit',
                command=self.changeUsername)
        self.__changeUsernameButton.grid(
            row=0,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        self.__usernameLabel = ctk.CTkLabel(self.__userDetails, text='Username')
        self.__usernameLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        self.__usernameText = ctk.CTkLabel(self.__userDetails,
                text=globals.currentUser.getFirstName())
        self.__usernameText.grid(
            row=0,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=1,
            )

        self.__changeEmailButton = ctk.CTkButton(self.__userDetails, text='Edit',
                command=self.changeEmail)
        self.__changeEmailButton.grid(
            row=1,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=15,
            pady=11,
            )

        self.__emailLabel = ctk.CTkLabel(self.__userDetails, text='Email')
        self.__emailLabel.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=15,
            pady=11,
            )

        self.__emailText = ctk.CTkLabel(self.__userDetails,
                                 text=globals.currentUser.getEmail())
        self.__emailText.grid(
            row=1,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        self.__changeCityButton = ctk.CTkButton(self.__userDetails, text='Edit',
                command=self.changeCity)
        self.__changeCityButton.grid(
            row=2,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__cityLabel = ctk.CTkLabel(self.__userDetails, text='City')
        self.__cityLabel.grid(
            row=2,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__cityText = ctk.CTkLabel(self.__userDetails,
                                   text=globals.currentUser.getCity())
        self.__cityText.grid(
            row=2,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        self.__balanceLabel = ctk.CTkLabel(self.__userDetails, text='Balance')
        self.__balanceLabel.grid(
            row=3,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__phoneNumberLabel = ctk.CTkLabel(self.__userDetails, text='Phone Number')
        self.__phoneNumberLabel.grid(
            row=4,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__phoneNumberText = ctk.CTkLabel(self.__userDetails, text=globals.currentUser.getPhoneNumber())
        self.__phoneNumberText.grid(
            row=4,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        self.__descriptionLabel = ctk.CTkLabel(self.__userDetails, text='Description')
        self.__descriptionLabel.grid(
            row=5,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__descriptionText = ctk.CTkLabel(self.__userDetails, text=globals.currentUser.getDescription())
        self.__descriptionText.grid(
            row=5,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        self.__changePasswordButton = ctk.CTkButton(self.__userDetails, text='Change Password',
                command=self.changePassword)
        self.__changePasswordButton.grid(
            row=8,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__newPassLabel = ctk.CTkLabel(self.__userDetails, text='Enter new password')
        self.__newPassLabel.grid(
            row=6,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__oldPasswordLabel = ctk.CTkLabel(self.__userDetails, text='Enter old passord')
        self.__oldPasswordLabel.grid(
            row=7,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__repeatPasswordLabel = ctk.CTkLabel(self.__userDetails,
                text='Repeat new password')
        self.__repeatPasswordLabel.grid(
            row=8,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.__balanceText = ctk.CTkLabel(self.__userDetails,
                                   text=globals.currentUser.getBalance())
        self.__balanceText.grid(
            row=3,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        self.__editPhoneNumberButton = ctk.CTkButton(self.__userDetails, text='Edit Phone Number',
                                command=self.changePhoneNumber)
        self.__editPhoneNumberButton.grid(
            row=4,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        self.__editPictureButton = ctk.CTkButton(self.__userDetails, text='Edit Picture')
        self.__editPictureButton.grid(
            row=2,
            column=5,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=11,
            )

        self.__profilePicturePlaceholder = ctk.CTkLabel(self.__userDetails, text='Profile Picture Placeholder')
        self.__profilePicturePlaceholder.grid(
            row=0,
            column=5,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=11,
            )

        self.__editBalanceButton = ctk.CTkButton(self.__userDetails, text='Edit Balance',
                                command=self.editBalancePopup)
        self.__editBalanceButton.grid(
            row=3,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        self.__editDescriptionButton = ctk.CTkButton(self.__userDetails, text='Edit Description',
                                command=self.changeDescription)
        self.__editDescriptionButton.grid(
            row=5,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        # self.newPassTextBox= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10)
        # self.newPassTextBox.grid(row=6, column=1, sticky=ctk.W)

        # self.oldPassTextBox= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10)
        # self.oldPassTextBox.grid(row=7, column=1, sticky=ctk.W)

        # self.repeatPassTextBox= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10)
        # self.repeatPassTextBox.grid(row=8, column=1, sticky=ctk.W)
        self.__userDetails.pack(padx=20, pady=20)

    def changePassword(self):

        def change():
            storeButton.destroy()
            c1 = self.__newPassTextBox.get('0.1', 'end')
            c2 = self.__oldPassTextBox.get('0.1', 'end')
            c2 = c2.replace('\n', '')
            c3 = self.__repeatPassTextBox.get('0.1', 'end')

            f = globals.currentUser.getPassword()
            f = f.replace('\n', '')

            if (c1 == c3) and (str(c2)==f):
                y = len(c1)
                if y < 35 and y > 0:
                    globals.currentUser.setPassword(c1)
                else:
                    print("First")

          # self.newPassTextBox.destroy()
          # self.oldPassTextBox.destroy()
          # self.repeatPassTextBox.destroy()

                    self.invalidPasswordPopup()
            else:

           # self.newPassTextBox.destroy()
            # self.oldPassTextBox.destroy()
            # self.repeatPassTextBox.destroy()

         # globals.currentUser.setPass(c1)
         # f=globals.currentUser.getPassword()
         # print("1")

                self.invalidPasswordPopup()

            f = globals.currentUser.getPassword()
            #print(f)
            self.__newPassTextBox.destroy()
            self.__oldPassTextBox.destroy()
            self.__repeatPassTextBox.destroy()

        self.__newPassTextBox = ctk.CTkTextbox(self.__userDetails, width=150, height=4,
                corner_radius=10)
        self.__newPassTextBox.grid(row=6, column=1, sticky=ctk.W, padx=50, pady=1)

        self.__oldPassTextBox = ctk.CTkTextbox(self.__userDetails, width=150, height=4,
                corner_radius=10)
        self.__oldPassTextBox.grid(row=7, column=1, sticky=ctk.W, padx=50, pady=1)

        self.__repeatPassTextBox = ctk.CTkTextbox(self.__userDetails, width=150,
                height=4, corner_radius=10)
        self.__repeatPassTextBox.grid(row=8, column=1, sticky=ctk.W, padx=50, pady=1)
        storeButton = ctk.CTkButton(self.__userDetails, text='Store Password',
                command=change)
        storeButton.grid(
            row=8,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

    def changeUsername(self):

        def change():

            c = self.__storeTextbox.get('0.1', 'end')

            f = globals.currentUser.getFirstName()
            y = len(c) + 1
            if y > 21 or y <= 1:
                self.__storeUsernameButton.destroy()
                self.__storeTextbox.destroy()
                self.invalidPopup("Username")
            else:
                globals.currentUser.setFirstName(c)
                f = globals.currentUser.getFirstName()
                #print(f)
                self.__usernameText = ctk.CTkLabel(self.__userDetails,
                        text=globals.currentUser.getFirstName())
                self.__usernameText.grid(
                    row=0,
                    column=1,
                    sticky=ctk.W,
                    columnspan=1,
                    rowspan=1,
                    padx=100,
                    pady=1,
                    )
                self.__storeUsernameButton.destroy()
                self.__storeTextbox.destroy()

        self.__usernameText.destroy()
        self.__storeUsernameButton = ctk.CTkButton(self.__userDetails, text='Store Username',
                command=change)
        self.__storeUsernameButton.grid(
            row=0,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        self.__storeTextbox = ctk.CTkTextbox(self.__userDetails, width=150, height=4,
                                corner_radius=5)
        self.__storeTextbox.grid(
            row=0,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )

    def changeCity(self):

        def change():
            storeButton.destroy()
            c1 = self.__storeTextbox.get('0.1', 'end')

            f = globals.currentUser.getCity()
            y = len(c1)
            if y > 35 or y <= 0:
                self.invalidPopup("Location")
            else:
                globals.currentUser.setCity(c1)
                f = globals.currentUser.getCity()
                #print(f)
            self.__storeTextbox.destroy()
            self.__cityText = ctk.CTkLabel(self.__userDetails,
                    text=globals.currentUser.getCity())
            self.__cityText.grid(
                row=2,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=2,
                )

        self.__cityText.destroy()
        self.__storeTextbox = ctk.CTkTextbox(self.__userDetails, width=150, height=4,
                                corner_radius=5)
        self.__storeTextbox.grid(
            row=2,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )
        storeButton = ctk.CTkButton(self.__userDetails, text='Store Location',
                command=change)
        storeButton.grid(
            row=2,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

    def changeEmail(self):

        def change():
            c1 = self.__storeTextbox.get('0.1', 'end')
            self.__changeEmailButton.destroy()
            self.__storeTextbox.destroy()
            f = globals.currentUser.getEmail()
            y = len(c1)
            if y > 35 or y <= 0:
                self.invalidPopup("Email")
            else:
                globals.currentUser.setEmail(c1)
                f = globals.currentUser.getEmail()
                #print(f)
                self.__emailText = ctk.CTkLabel(self.__userDetails,
                        text=globals.currentUser.getEmail())
                self.__emailText.grid(
                    row=1,
                    column=1,
                    sticky=ctk.W,
                    columnspan=1,
                    rowspan=1,
                    padx=100,
                    pady=2,
                    )

        self.__emailText.destroy()
        self.__changeEmailButton = ctk.CTkButton(self.__userDetails, text='Store Email',
                command=change)
        self.__changeEmailButton.grid(
            row=1,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=15,
            pady=11,
            )
        self.__storeTextbox = ctk.CTkTextbox(self.__userDetails, width=185, height=4,
                                corner_radius=5)
        self.__storeTextbox.grid(
            row=1,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )


    def editBalancePopup(self):
        self.__popupwindow = ctk.CTkToplevel()
        self.__popupwindow.title('Edit Balance')
        self.__popupwindow.geometry('800x800')

        def deposit():

            c1 = self.__repeatPassTextBox.get('0.1', 'end')
            c = int(c1)

            f = globals.currentUser.getBalance()

            if c < 0:

                self.invalidPopup("Phone Number")
            else:

                h = c + f
                globals.currentUser.setBalance(h)

            f = globals.currentUser.getBalance()
            #print(f)
            self.__balanceText = ctk.CTkLabel(self.__userDetails, text=f)
            self.__popupwindow.destroy()
            self.__balanceText.grid(
                row=3,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=2,
                )
            self.__balanceText.destroy()

        def withdraw():

            c1 = self.__withdrawAmount.get('0.1', 'end')
            c = int(c1)

            f = globals.currentUser.getBalance()

            if f - c < 0:

                self.invalidPopup("Phone Number")
            else:

                g = f - c
                globals.currentUser.setBalance(g)

            f = globals.currentUser.getBalance()
            #print(f)
            self.__balanceText = ctk.CTkLabel(self.__userDetails, text=f)
            self.__popupwindow.destroy()
            self.__balanceText.grid(
                row=3,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=2,
                )
            self.__balanceText.destroy()

        self.__amountLabel = ctk.CTkLabel(self.__popupwindow, text='Enter Amount')

        self.__depositButton = ctk.CTkButton(self.__popupwindow, text='Deposit',
                                command=deposit)

        self.__amountLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        self.__repeatPassTextBox = ctk.CTkTextbox(self.__popupwindow, width=150,
                height=4, corner_radius=10)

        self.__repeatPassTextBox.grid(row=1, column=0, sticky=ctk.W)

        self.__depositButton.grid(
            row=2,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=1,
            )

        self.__withdrawButton = ctk.CTkButton(self.__popupwindow, text='Withdraw',
                command=withdraw)

        self.__amountLabel2 = ctk.CTkLabel(self.__popupwindow, text='Enter Amount')

        self.__amountLabel2.grid(
            row=0,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        self.__withdrawAmount = ctk.CTkTextbox(self.__popupwindow, width=150, height=4,
                                corner_radius=10)

        self.__withdrawAmount.grid(row=1, column=1, sticky=ctk.W)

        self.__withdrawButton.grid(
            row=2,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=1,
            )

        self.__popupwindow.mainloop()

    def changePhoneNumber(self):

        def change():

            c = self.__storeTextbox.get('0.1', 'end')
            c1 = int(c)

            f = globals.currentUser.getPhoneNumber()

            if c1 > 9999999999 or c1 <= 0:
                self.invalidPopup("Phone Number")
            else:
                globals.currentUser.setPhoneNumber(c1)
                f = globals.currentUser.getPhoneNumber()
            self.__storeTextbox.destroy()
            #print(f)
            storeButton.destroy()
            self.__phoneNumberText = ctk.CTkLabel(self.__userDetails,
                    text=globals.currentUser.getPhoneNumber())
            self.__phoneNumberText.grid(
                row=4,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=1,
                )

        self.__phoneNumberText.destroy()
        self.__storeTextbox = ctk.CTkTextbox(self.__userDetails, width=150, height=4,
                                corner_radius=5)
        self.__storeTextbox.grid(
            row=4,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )
        storeButton = ctk.CTkButton(self.__userDetails, text='Store Phone Number',
                command=change)
        storeButton.grid(
            row=4,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

    def changeDescription(self):
        def change():
            c = self.__storeTextbox.get('0.1', 'end')
            f = globals.currentUser.getDescription()
            y = len(c)
            if y > 150 or y <= 0:
                self.invalidPopup("Description")
            else:
                globals.currentUser.setDescription(c)
                f = globals.currentUser.getDescription()
            self.__storeTextbox.destroy()
            #print(f)
            storeButton.destroy()
            self.__descriptionText = ctk.CTkLabel(self.__userDetails,
                    text=globals.currentUser.getDescription())
            self.__descriptionText.grid(
                row=5,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=1,
                )
        self.__descriptionText.destroy()
        self.__storeTextbox = ctk.CTkTextbox(self.__userDetails, width=300, height=20,
                                corner_radius=20)
        self.__storeTextbox.grid(
            row=5,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )
        storeButton = ctk.CTkButton(self.__userDetails, text='Store Description',
                command=change)
        storeButton.grid(
            row=5,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

    def invalidPopup(self, type):

        def popup():
            self.__popupwindow.destroy()

        self.__popupwindow = ctk.CTkToplevel()
        self.__popupwindow.title('Eror')
        self.__popupwindow.geometry('800x800')
        self.__invalidLabel = ctk.CTkLabel(self.__popupwindow, text=f'Invalid {type}!'
                              )
        self.__invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        self.__popupButton = ctk.CTkButton(self.__popupwindow, text='OK', command=popup)
        self.__popupButton.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        self.__popupwindow.mainloop()

    def invalidPasswordPopup(self):

        def popup():
            self.__popupwindow.destroy()

        self.__popupwindow = ctk.CTkToplevel()
        self.__popupwindow.title('Eror')
        self.__popupwindow.geometry('800x800')
        self.__invalidLabel = ctk.CTkLabel(self.__popupwindow,
                              text='Invalid characters or wrong old password'
                              )
        self.__invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        self.__popupButton = ctk.CTkButton(self.__popupwindow, text='OK', command=popup)
        self.__popupButton.grid(
            row=1,
            column=1,
            sticky=ctk.W,
            columnspan=10,
            rowspan=10,
            padx=14,
            pady=1,
            )
        self.__popupwindow.mainloop()
