import graphics
# import tkinter as tk
from pyvirtualdisplay import Display
import tkinter as tk

win = graphics.GraphWin("My Window", 500, 500) 
# Wait for user interaction before closing (prevents instant close)
win.getMouse()  # Click to close
win.close() 
