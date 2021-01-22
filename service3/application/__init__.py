from flask import Flask
import requests
import os

app = Flask(__name__)


from application import routes