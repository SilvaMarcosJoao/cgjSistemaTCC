from tkinter import * 
from tkinter import ttk
from customtkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser