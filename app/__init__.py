from flask import Flask, render_template
from utils import utils
import sys

app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config['SECRET_KEY'] = 'super-secret'


_db_utils = utils.db_utils(app.config['DATABASE_HOST'],app.config['DATABASE_USERNAME'],app.config['DATABASE_PASSWORD'],app.config['DATABASE_NAME'] )
    

# Setup Flask-Security


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from vendor.controllers import app_vendor as vendor_mod

#from auth import controllers as auth_ctl
app.register_blueprint(vendor_mod)
#auth_ctl.init_security()


