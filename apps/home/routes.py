# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps.models    import *
from apps.api.forms import *
from flask import render_template, request, jsonify 
import requests
from flask_login import login_required
from jinja2 import TemplateNotFound

@blueprint.route('/products')
@login_required
def products():
    all_objects = Product.query.all()
    output = [{'id': obj.product_id, **ProductForm(obj=obj).data} for obj in all_objects]
    segment = get_segment(request)
    return render_template('home/products.html', products=output, segment=segment)
@blueprint.route('/discounts')
@login_required
def discounts():
    all_objects = Discount.query.all()
    output = [{'id': obj.discount_id, **DiscountForm(obj=obj).data} for obj in all_objects]
    segment = get_segment(request)
    return render_template('home/discounts.html', discounts=output, segment=segment)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
