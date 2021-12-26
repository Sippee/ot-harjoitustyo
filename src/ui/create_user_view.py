from tkinter import *
from tkinter import ttk, StringVar, constants
from functools import partial
from services.service import service, UserError


class CreateUserView:
    """A class used to present user creation view.
    """

    def __init__(self, root, handle_create, handle_loginview):
        self._root = root
        self._handle_create = handle_create
        self._handle_loginview = handle_loginview
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

    def _create_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error('Username and password is required')
            return

        try:
            service.create_user(username, password)
            self._handle_create()
        except UserError:
            self._show_error(f'Username {username} already exists')

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

        username_label = ttk.Label(master=self._frame, text='Username')
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

        password_label = ttk.Label(master=self._frame, text='Password')
        password_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)

        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.grid(row=1, column= 1, padx=5, pady=5, sticky=constants.EW)

        login_button = ttk.Button( master=self._frame, text='Login Screen', command=self._handle_loginview)
        login_button.grid(row=3, column=0, padx=5, pady=5, sticky=constants.EW)

        create_user_button = ttk.Button(master=self._frame, text='Create', command=self._create_handler)
        create_user_button.grid(row=3, column=1, padx=5, pady=5, sticky=constants.EW)

        self._hide_error()