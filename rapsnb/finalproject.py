#import files
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Catalog
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.rollback()

@app.route('/')
def catalogupdate():
    show = session.query(Catalog).all()
    return render_template('listview.html',show=show)

@app.route('/catalogupdate/<string:idl>/deletecatalog')
def catalogdelete(idl):
	output=''
	editedItem = session.query(Catalog).filter_by(id=idl).first()
	if editedItem == None:
		flash("incorrect product id")
		return redirect(url_for('catalogupdate'))
	session.delete(editedItem)
	session.commit()
	return redirect(url_for('catalogupdate'))

@app.route('/editcatalog')
def catalogedit(nlink,id):
	editedItem = session.query(Catalog).filter_by(id=id).first()
	if editedItem == None:
		flash("incorrect product id")
		return redirect(url_for('index'))
	editedItem.image=nlink
	session.add(editedItem)
	session.commit()
	return redirect(url_for('catalogupdate'))

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
