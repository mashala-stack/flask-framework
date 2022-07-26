import os
from os.path import join,dirname,realpath
from flask import Blueprint
from flask.globals import session
from sqlalchemy.sql.expression import desc, distinct
from sqlalchemy.sql.sqltypes import DateTime, String

from ..models import db
from datetime import date,datetime
from sqlalchemy import cast,Date,func,and_,or_

app_bp = Blueprint('app_bp',__name__,template_folder='templates')

# UPLOAD_PATH = join(dirname(realpath(__file__)),"../static/uploads")


@app_bp.route("/")
def Index():
    return("Hello There, Wellcome to Flask")