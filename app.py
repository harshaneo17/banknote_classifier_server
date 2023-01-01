import json
import requests
from fpdf import FPDF
from flask import Flask,request,render_template


API_KEY = ''
API_HOST = ''
API_URL = ''

app = Flask(__name__)

