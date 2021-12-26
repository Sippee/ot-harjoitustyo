"""Handles the main of the application
"""

from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title('Coin Collector Game')

ui = UI(window)
ui.start()

window.mainloop()
