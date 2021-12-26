"""Handles the views of the hiscore and after logging in.
"""

from tkinter import ttk, constants, messagebox
from services.service import service

class HiscoreView:
    """A class used to present hiscore.
    """

    def __init__(self, root, hiscore):
        self._root = root
        self._hiscore = hiscore
        self._frame = None

        self._initialize()

    def pack(self):
        """Packs the frame
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the frame
        """

        self._frame.destroy()

    def _initialize_hiscore_item(self, player):
        item_frame = ttk.Frame(master=self._frame)
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

        hiscore = ttk.Label(master=item_frame, text=player)

        hiscore.grid(row=1, column=1, padx=5, pady=5, sticky=constants.W)



    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for player in service.top10_hiscore():
            self._initialize_hiscore_item(player)


class MainView:
    """A class used to present the main view of the application.
    """

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = service.get_user()
        self._frame = None
        self._hiscore_frame = None
        self._hiscore_view = None

        self._initialize()

    def pack(self):
        """Packs the frame
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the frame
        """

        self._frame.destroy()

    def _logout_handler(self):
        service.logout()
        self._handle_logout()

    def _game_handler(self):
        messagebox.showinfo("Game Over", f"You collected {service.game()} points")
        self._initialize_hiscore()

    def _initialize_hiscore(self):
        if self._hiscore_view:
            self._hiscore_view.destroy()

        hiscore = service.top10_hiscore()

        self._hiscore_view = HiscoreView(self._hiscore_frame, hiscore)

        self._hiscore_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._hiscore_frame = ttk.Frame(master=self._frame)

        logout_button = ttk.Button(master=self._frame, text='Logout', command=self._logout_handler)
        logout_button.grid(row=1, column=0, padx=5, pady=5, sticky=constants.NW)

        play_button = ttk.Button(master=self._frame, text='Play', command=self._game_handler)
        play_button.grid(row=0, column=0, padx=5, pady=5, sticky=constants.NW)

        self._initialize_hiscore()

        hiscore = ttk.Label(self._frame, text="HISCORE", font=("TkDefaultFont", 18, "bold"))
        hiscore.grid(row=0, column=2, padx=5, pady=5, sticky=constants.W)

        self._hiscore_frame.grid(row=1, column=1, columnspan=2, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=0, minsize=100)
        self._frame.grid_columnconfigure(1, weight=0)
