from flask import Flask

app = Flask(__name__)

from gitwil.views import homepage