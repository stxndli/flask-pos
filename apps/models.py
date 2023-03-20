# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db

'''
Add your models below
'''

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.TEXT)
    price = db.Column(db.Float)
    tax = db.Column(db.Float)
    image = db.Column(db.String(255))
class Discount(db.Model):
    discount_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    percentage = db.Column(db.Integer)
