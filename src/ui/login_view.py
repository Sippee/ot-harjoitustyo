from tkinter import *
from tkinter import ttk, StringVar, constants
from functools import partial
from services.service import service, UserError

class LoginView:
    """A class used to present login view.
    """
    def __init__(self, root, handle_login, handle_showcreateview):
        self._root = root
        self._handle_login = handle_login
        self._handle_showcreateview = handle_showcreateview
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            service.login(username, password)
            self._handle_login()
        except UserError:
            self._show_error('Username or Password is invalid')

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground='red')
        self._error_label.grid(row=2, column=1, padx=5, pady=5)

        usernameLabel = Label(self._frame, text="Username")
        usernameLabel.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        username = StringVar()
        self._username_entry = Entry(self._frame, textvariable=username)
        self._username_entry.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)  

        passwordLabel = Label(self._frame,text="Password")
        passwordLabel.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)  

        password = StringVar()
        self._password_entry = Entry(self._frame, textvariable=password, show='*')
        self._password_entry.grid(row=1, column=1, padx=5, pady=5, sticky=constants.EW)  

        loginButton = Button(self._frame, text="Login", command=self._login_handler)
        loginButton.grid(row=3, column=0, padx=5, pady=5, sticky=constants.EW)
        
        registerButton = Button(self._frame, text="Create user", command=self._handle_showcreateview)
        registerButton.grid(row=3, column=1, padx=5, pady=5, sticky=constants.EW)

        self._hide_error()