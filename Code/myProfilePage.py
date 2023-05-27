#!/usr/bin/python
# -*- coding: utf-8 -*-
import customtkinter as ctk
import globals


class MyProfilePage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.buttf = ctk.CTkFrame(self)
        self.buttf.columnconfigure(9, weight=1)

        self.buttf = ctk.CTkFrame(self)
        self.buttf.columnconfigure(9, weight=1)
        changeUsernameButton = ctk.CTkButton(self.buttf, text='Edit',
                command=self.changeUsername)
        changeUsernameButton.grid(
            row=0,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        usernameLabel = ctk.CTkLabel(self.buttf, text='Username')
        usernameLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        self.firstNameText = ctk.CTkLabel(self.buttf,
                text=globals.currentUser.getFirstName())
        self.firstNameText.grid(
            row=0,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=1,
            )

        changeEmailButton = ctk.CTkButton(self.buttf, text='Edit',
                command=self.changeEmail)
        changeEmailButton.grid(
            row=1,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=15,
            pady=11,
            )

        emailLabel = ctk.CTkLabel(self.buttf, text='Email')
        emailLabel.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=15,
            pady=11,
            )

        self.emailText = ctk.CTkLabel(self.buttf,
                                 text=globals.currentUser.getEmail())
        self.emailText.grid(
            row=1,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        changeAddressButton = ctk.CTkButton(self.buttf, text='Edit',
                command=self.changeAddress)
        changeAddressButton.grid(
            row=2,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        addressLabel = ctk.CTkLabel(self.buttf, text='Address')
        addressLabel.grid(
            row=2,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        self.addressText = ctk.CTkLabel(self.buttf,
                                   text=globals.currentUser.getAddress())
        self.addressText.grid(
            row=2,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        balanceLabel = ctk.CTkLabel(self.buttf, text='Balance')
        balanceLabel.grid(
            row=3,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        phoneNumberLabel = ctk.CTkLabel(self.buttf, text='Phone Number')
        phoneNumberLabel.grid(
            row=4,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        phoneNumberText = ctk.CTkLabel(self.buttf, text=globals.currentUser.getPhoneNumber())
        phoneNumberText.grid(
            row=4,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        descriptionLabel = ctk.CTkLabel(self.buttf, text='Description')
        descriptionLabel.grid(
            row=5,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        descriptionText = ctk.CTkLabel(self.buttf, text=globals.currentUser.getDescription())
        descriptionText.grid(
            row=5,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        changePasswordButton = ctk.CTkButton(self.buttf, text='Change Password',
                command=self.changePassword)
        changePasswordButton.grid(
            row=8,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        newPassLabel = ctk.CTkLabel(self.buttf, text='Enter new password')
        newPassLabel.grid(
            row=6,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        oldPasswordLabel = ctk.CTkLabel(self.buttf, text='Enter old passord')
        oldPasswordLabel.grid(
            row=7,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        repeatPasswordLabel = ctk.CTkLabel(self.buttf,
                text='Repeat new password')
        repeatPasswordLabel.grid(
            row=8,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=11,
            )

        balanceText = ctk.CTkLabel(self.buttf,
                                   text=globals.currentUser.getBalance())
        balanceText.grid(
            row=3,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=100,
            pady=2,
            )

        editPhoneNumberButton = ctk.CTkButton(self.buttf, text='Edit Phone Number',
                                command=self.changePhoneNumber)
        editPhoneNumberButton.grid(
            row=4,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        editPictureButton = ctk.CTkButton(self.buttf, text='Edit Picture')
        editPictureButton.grid(
            row=2,
            column=5,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=11,
            )

        profilePicturePlaceholder = ctk.CTkLabel(self.buttf, text='Profile Picture Placeholder')
        profilePicturePlaceholder.grid(
            row=0,
            column=5,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=11,
            )

        editBalanceButton = ctk.CTkButton(self.buttf, text='Edit Balance',
                                command=self.editBalancePopup)
        editBalanceButton.grid(
            row=3,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        editDescriptionButton = ctk.CTkButton(self.buttf, text='Edit Description',
                                command=self.changeDescription)
        editDescriptionButton.grid(
            row=5,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        # newPassTextBox= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10)
        # newPassTextBox.grid(row=6, column=1, sticky=ctk.W)

        # oldPassTextBox= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10)
        # oldPassTextBox.grid(row=7, column=1, sticky=ctk.W)

        # repeatPassTextBox= ctk.CTkTextbox(buttf,width=150,height=4,corner_radius=10)
        # repeatPassTextBox.grid(row=8, column=1, sticky=ctk.W)
        self.buttf.pack(padx=20, pady=20)

    def changePassword(self):

        def change():
            storeButton.destroy()
            c1 = newPassTextBox.get('0.1', 'end')
            c2 = oldPassTextBox.get('0.1', 'end')
            c2 = c2.replace('\n', '')
            c3 = repeatPassTextBox.get('0.1', 'end')

            f = globals.currentUser.getPassword()

            if (c1 == c3) and (str(c2)==f):
                y = len(c1)
                if y < 35 and y > 0:
                    globals.currentUser.setPassword(c1)
                else:

          # newPassTextBox.destroy()
          # oldPassTextBox.destroy()
          # repeatPassTextBox.destroy()

                    self.invalidPasswordPopup()
            else:

           # newPassTextBox.destroy()
            # oldPassTextBox.destroy()
            # repeatPassTextBox.destroy()

         # globals.currentUser.setPass(c1)
         # f=globals.currentUser.getPassword()
         # print("1")

                self.invalidPasswordPopup()

            f = globals.currentUser.getPassword()
            print(f)
            newPassTextBox.destroy()
            oldPassTextBox.destroy()
            repeatPassTextBox.destroy()

        newPassTextBox = ctk.CTkTextbox(self.buttf, width=150, height=4,
                corner_radius=10)
        newPassTextBox.grid(row=6, column=1, sticky=ctk.W, padx=50, pady=1)

        oldPassTextBox = ctk.CTkTextbox(self.buttf, width=150, height=4,
                corner_radius=10)
        oldPassTextBox.grid(row=7, column=1, sticky=ctk.W, padx=50, pady=1)

        repeatPassTextBox = ctk.CTkTextbox(self.buttf, width=150,
                height=4, corner_radius=10)
        repeatPassTextBox.grid(row=8, column=1, sticky=ctk.W, padx=50, pady=1)
        storeButton = ctk.CTkButton(self.buttf, text='Store Password',
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

            c = storeTextbox.get('0.1', 'end')

            f = globals.currentUser.getFirstName()
            y = len(c) + 1
            if y > 21 or y <= 1:
                storeUsernameButton.destroy()
                storeTextbox.destroy()
                self.invalidUsernamePopup()
            else:
                globals.currentUser.setFirstName(c)
                f = globals.currentUser.getFirstName()
                print(f)
                self.firstNameText = ctk.CTkLabel(self.buttf,
                        text=globals.currentUser.getFirstName())
                self.firstNameText.grid(
                    row=0,
                    column=1,
                    sticky=ctk.W,
                    columnspan=1,
                    rowspan=1,
                    padx=100,
                    pady=1,
                    )
                storeUsernameButton.destroy()
                storeTextbox.destroy()

        self.firstNameText.destroy()
        storeUsernameButton = ctk.CTkButton(self.buttf, text='Store Username',
                command=change)
        storeUsernameButton.grid(
            row=0,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        storeTextbox = ctk.CTkTextbox(self.buttf, width=150, height=4,
                                corner_radius=5)
        storeTextbox.grid(
            row=0,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )

    def changeAddress(self):

        def change():
            storeButton.destroy()
            c1 = storeTextbox.get('0.1', 'end')

            f = globals.currentUser.getAddress()
            y = len(c1)
            if y > 35 or y <= 0:
                self.invalidLocationPopup()
            else:
                globals.currentUser.setAddress(c1)
                f = globals.currentUser.getAddress()
                print(f)
            storeTextbox.destroy()
            self.addressText = ctk.CTkLabel(self.buttf,
                    text=globals.currentUser.getAddress())
            self.addressText.grid(
                row=2,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=2,
                )

        self.addressText.destroy()
        storeTextbox = ctk.CTkTextbox(self.buttf, width=150, height=4,
                                corner_radius=5)
        storeTextbox.grid(
            row=2,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )
        storeButton = ctk.CTkButton(self.buttf, text='Store Location',
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
            c1 = storeTextbox.get('0.1', 'end')
            changeEmailButton.destroy()
            storeTextbox.destroy()
            f = globals.currentUser.getEmail()
            y = len(c1)
            if y > 35 or y <= 0:
                self.invalidEmailPopup()
            else:
                globals.currentUser.setEmail(c1)
                f = globals.currentUser.getEmail()
                print(f)
                self.emailText = ctk.CTkLabel(self.buttf,
                        text=globals.currentUser.getEmail())
                self.emailText.grid(
                    row=1,
                    column=1,
                    sticky=ctk.W,
                    columnspan=1,
                    rowspan=1,
                    padx=100,
                    pady=2,
                    )

        self.emailText.destroy()
        changeEmailButton = ctk.CTkButton(self.buttf, text='Store Email',
                command=change)
        changeEmailButton.grid(
            row=1,
            column=2,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=15,
            pady=11,
            )
        storeTextbox = ctk.CTkTextbox(self.buttf, width=185, height=4,
                                corner_radius=5)
        storeTextbox.grid(
            row=1,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )


    def editBalancePopup(self):
        popupwindow = ctk.CTkToplevel()
        popupwindow.title('Edit Balance')
        popupwindow.geometry('800x800')

        def deposit():

            c1 = repeatPassTextBox.get('0.1', 'end')
            c = int(c1)

            f = globals.currentUser.getBalance()

            if c < 0:

                self.invalidNumberPopup()
            else:

                h = c + f
                globals.currentUser.setBalance(h)

            f = globals.currentUser.getBalance()
            print(f)
            balanceText = ctk.CTkLabel(self.buttf, text=f)
            popupwindow.destroy()
            balanceText.grid(
                row=3,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=2,
                )
            balanceText.destroy()

        def withdraw():

            c1 = withdrawAmount.get('0.1', 'end')
            c = int(c1)

            f = globals.currentUser.getBalance()

            if f - c < 0:

                self.invalidNumberPopup()
            else:

                g = f - c
                globals.currentUser.setBalance(g)

            f = globals.currentUser.getBalance()
            print(f)
            balanceText = ctk.CTkLabel(self.buttf, text=f)
            popupwindow.destroy()
            balanceText.grid(
                row=3,
                column=1,
                sticky=ctk.W,
                columnspan=1,
                rowspan=1,
                padx=100,
                pady=2,
                )
            balanceText.destroy()

        amountLabel = ctk.CTkLabel(popupwindow, text='Enter Amount')

        depositButton = ctk.CTkButton(popupwindow, text='Deposit',
                                command=deposit)

        amountLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        repeatPassTextBox = ctk.CTkTextbox(popupwindow, width=150,
                height=4, corner_radius=10)

        repeatPassTextBox.grid(row=1, column=0, sticky=ctk.W)

        depositButton.grid(
            row=2,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=1,
            )

        withdrawButton = ctk.CTkButton(popupwindow, text='Withdraw',
                command=withdraw)

        amountLabel2 = ctk.CTkLabel(popupwindow, text='Enter Amount')

        amountLabel2.grid(
            row=0,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )

        withdrawAmount = ctk.CTkTextbox(popupwindow, width=150, height=4,
                                corner_radius=10)

        withdrawAmount.grid(row=1, column=1, sticky=ctk.W)

        withdrawButton.grid(
            row=2,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=1,
            pady=1,
            )

        popupwindow.mainloop()

    def changePhoneNumber(self):

        def change():

            c = storeTextbox.get('0.1', 'end')
            c1 = int(c)

            f = globals.currentUser.getPhoneNumber()

            if c1 > 999999999999999 or c1 <= 0:
                self.invalidNumberPopup()
            else:
                globals.currentUser.setPhoneNumber(c1)
                f = globals.currentUser.getPhoneNumber()
            storeTextbox.destroy()
            print(f)
            storeButton.destroy()

        storeTextbox = ctk.CTkTextbox(self.buttf, width=150, height=4,
                                corner_radius=5)
        storeTextbox.grid(
            row=4,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )
        storeButton = ctk.CTkButton(self.buttf, text='Store Phone Number',
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
            c = storeTextbox.get('0.1', 'end')
            f = globals.currentUser.getDescription()
            y = len(c)
            if y > 150 or y <= 0:
                self.invalidDescriptionPopup()
            else:
                globals.currentUser.setDescription(c)
                f = globals.currentUser.getDescription()
            storeTextbox.destroy()
            print(f)
            storeButton.destroy()
        storeTextbox = ctk.CTkTextbox(self.buttf, width=300, height=20,
                                corner_radius=20)
        storeTextbox.grid(
            row=5,
            column=1,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=50,
            pady=1,
            )
        storeButton = ctk.CTkButton(self.buttf, text='Store Description',
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

    def invalidUsernamePopup(self):

        def popup():
            popupwindow1.destroy()

        popupwindow1 = ctk.CTkToplevel()
        popupwindow1.title('Eror')
        popupwindow1.geometry('800x800')
        invalidLabel = ctk.CTkLabel(popupwindow1, text='Invalid Username!'
                              )
        invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        popupButton = ctk.CTkButton(popupwindow1, text='OK', command=popup)
        popupButton.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        popupwindow1.mainloop()

    def invalidLocationPopup(self):

        def popup():
            popupwindow1.destroy()

        popupwindow1 = ctk.CTkToplevel()
        popupwindow1.title('Eror')
        popupwindow1.geometry('800x800')
        invalidLabel = ctk.CTkLabel(popupwindow1, text='Invalid Location!'
                              )
        invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        popupButton = ctk.CTkButton(popupwindow1, text='OK', command=popup)
        popupButton.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=10,
            rowspan=10,
            padx=14,
            pady=1,
            )
        popupwindow1.mainloop()

    def invalidEmailPopup(self):

        def popup():
            popupwindow1.destroy()

        popupwindow1 = ctk.CTkToplevel()
        popupwindow1.title('Eror')
        popupwindow1.geometry('800x800')
        invalidLabel = ctk.CTkLabel(popupwindow1, text='Invalid Email!')
        invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        popupButton = ctk.CTkButton(popupwindow1, text='OK', command=popup)
        popupButton.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=10,
            rowspan=10,
            padx=14,
            pady=1,
            )
        popupwindow1.mainloop()

    def invalidNumberPopup(self):

        def popup():
            popupwindow1.destroy()

        popupwindow1 = ctk.CTkToplevel()
        popupwindow1.title('Eror')
        popupwindow1.geometry('800x800')
        invalidLabel = ctk.CTkLabel(popupwindow1, text='Invalid Number!')
        invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        popupButton = ctk.CTkButton(popupwindow1, text='OK', command=popup)
        popupButton.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=10,
            rowspan=10,
            padx=14,
            pady=1,
            )
        popupwindow1.mainloop()

    def invalidDescriptionPopup(self):

        def popup():
            popupwindow1.destroy()

        popupwindow1 = ctk.CTkToplevel()
        popupwindow1.title('Eror')
        popupwindow1.geometry('800x800')
        invalidLabel = ctk.CTkLabel(popupwindow1,
                              text='Invalid characters or too long Description!')
        invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        popupButton = ctk.CTkButton(popupwindow1, text='OK', command=popup)
        popupButton.grid(
            row=1,
            column=0,
            sticky=ctk.W,
            columnspan=10,
            rowspan=10,
            padx=14,
            pady=1,
            )
        popupwindow1.mainloop()

    def invalidPasswordPopup(self):

        def popup():
            popupwindow1.destroy()

        popupwindow1 = ctk.CTkToplevel()
        popupwindow1.title('Eror')
        popupwindow1.geometry('800x800')
        invalidLabel = ctk.CTkLabel(popupwindow1,
                              text='Invalid characters or wrong old password'
                              )
        invalidLabel.grid(
            row=0,
            column=0,
            sticky=ctk.W,
            columnspan=1,
            rowspan=1,
            padx=14,
            pady=1,
            )
        popupButton = ctk.CTkButton(popupwindow1, text='OK', command=popup)
        popupButton.grid(
            row=1,
            column=1,
            sticky=ctk.W,
            columnspan=10,
            rowspan=10,
            padx=14,
            pady=1,
            )
        popupwindow1.mainloop()
