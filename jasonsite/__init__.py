from flask import Flask


app = Flask(__name__)
app._static_folder


# leave here
from jasonsite import routes
