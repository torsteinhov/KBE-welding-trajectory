from flask import Flask

app = Flask(__name__)

from app import views # to avoid circluar imports
from app import admin_view