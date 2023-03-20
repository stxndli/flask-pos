import json

from flask import request
from flask_restx import Api, Resource
from werkzeug.datastructures import MultiDict


from apps.api import blueprint
from apps.authentication.decorators import token_required

from apps.api.forms import *
from apps.models    import *

api = Api(blueprint)


@api.route('/products/', methods=['POST', 'GET', 'DELETE', 'PUT'])
@api.route('/products/<int:model_id>/', methods=['GET', 'DELETE', 'PUT'])
class ProductRoute(Resource):
    def get(self, model_id: int = None):
        if model_id is None:
            all_objects = Product.query.all()
            output = [{'id': obj.product_id, **ProductForm(obj=obj).data} for obj in all_objects]
        else:
            obj = Product.query.get(model_id)
            if obj is None:
                return {
                           'message': 'matching record not found',
                           'success': False
                       }, 404
            output = {'id': obj.product_id, **ProductForm(obj=obj).data}
        return {
                   'data': output,
                   'success': True
               }, 200

    @token_required
    def post(self):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}
        form = ProductForm(MultiDict(body_of_req))
        if form.validate():
            try:
                obj = Product(**body_of_req)
                Product.query.session.add(obj)
                Product.query.session.commit()
            except Exception as e:
                return {
                           'message': str(e),
                           'success': False
                       }, 400
        else:
            return {
                       'message': form.errors,
                       'success': False
                   }, 400
        return {
                   'message': 'record saved!',
                   'success': True
               }, 200

    @token_required
    def put(self, model_id: int):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}

        to_edit_row = Product.query.filter_by(product_id=model_id)

        if not to_edit_row:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        obj = to_edit_row.first()

        if not obj:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        form = ProductForm(MultiDict(body_of_req), obj=obj)
        if not form.validate():
            return {
                       'message': form.errors,
                       'success': False
                   }, 404

        table_cols = [attr.name for attr in to_edit_row.__dict__['_raw_columns'][0].columns._all_columns]

        for col in table_cols:
            value = body_of_req.get(col, None)
            if value:
                setattr(obj, col, value)
        Product.query.session.add(obj)
        Product.query.session.commit()
        return {
            'message': 'record updated',
            'success': True
        }

    @token_required
    def delete(self, model_id: int):
        to_delete = Product.query.filter_by(product_id=model_id)
        if to_delete.count() == 0:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404
        to_delete.delete()
        Product.query.session.commit()
        return {
                   'message': 'record deleted!',
                   'success': True
               }, 200


@api.route('/discounts/', methods=['POST', 'GET', 'DELETE', 'PUT'])
@api.route('/discounts/<int:model_id>/', methods=['GET', 'DELETE', 'PUT'])
class DiscountRoute(Resource):
    @token_required
    def get(self, model_id: int = None):
        if model_id is None:
            all_objects = Discount.query.all()
            output = [{'id': obj.discount_id, **DiscountForm(obj=obj).data} for obj in all_objects]
        else:
            obj = Discount.query.get(model_id)
            if obj is None:
                return {
                           'message': 'matching record not found',
                           'success': False
                       }, 404
            output = {'id': obj.discount_id, **DiscountForm(obj=obj).data}
        return {
                   'data': output,
                   'success': True
               }, 200

    @token_required
    def post(self):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}
        form = DiscountForm(MultiDict(body_of_req))
        if form.validate():
            try:
                obj = Discount(**body_of_req)
                Discount.query.session.add(obj)
                Discount.query.session.commit()
            except Exception as e:
                return {
                           'message': str(e),
                           'success': False
                       }, 400
        else:
            return {
                       'message': form.errors,
                       'success': False
                   }, 400
        return {
                   'message': 'record saved!',
                   'success': True
               }, 200

    @token_required
    def put(self, model_id: int):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}

        to_edit_row = Discount.query.filter_by(discount_id=model_id)

        if not to_edit_row:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        obj = to_edit_row.first()

        if not obj:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        form = DiscountForm(MultiDict(body_of_req), obj=obj)
        if not form.validate():
            return {
                       'message': form.errors,
                       'success': False
                   }, 404

        table_cols = [attr.name for attr in to_edit_row.__dict__['_raw_columns'][0].columns._all_columns]

        for col in table_cols:
            value = body_of_req.get(col, None)
            if value:
                setattr(obj, col, value)
        Discount.query.session.add(obj)
        Discount.query.session.commit()
        return {
            'message': 'record updated',
            'success': True
        }

    @token_required
    def delete(self, model_id: int):
        to_delete = Discount.query.filter_by(discount_id=model_id)
        if to_delete.count() == 0:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404
        to_delete.delete()
        Discount.query.session.commit()
        return {
                   'message': 'record deleted!',
                   'success': True
               }, 200
@api.route('/discount/<string:model_name>/', methods=['GET'])
class TokenlessDiscountRoute(Resource):
    def get(self, model_name: str = None):
        if model_name is None:
            return{
                    'message': 'discount name required',
                    'success': False
                    }, 403
        else:
            obj = Discount.query.filter_by(name=model_name)
            if obj.count() == 0:
                return {
                           'message': 'matching record not found',
                           'success': False
                       }, 404
            obj = obj.first()
            output = {'id': obj.discount_id, **DiscountForm(obj=obj).data}
        return {
                   'data': output,
                   'success': True
               }, 200
