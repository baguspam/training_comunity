from odoo import http
from odoo.http import request, route

from ..jwt.login import token_required

class ApiProduct(http.Controller):

    @route(route=['/api/v1/product/',
                  '/api/v1/product/<int:product_id>'],
           methods=['GET'], type='json', auth='public', csrf=False)
    @token_required()
    def get_product(self, product_id=False, debug=False, **kwargs):
        product = request.env['product.product'].with_user(
            kwargs.get('uid', 1)).api_get_product(product_id=product_id)
        result = {}
        result['result'] = product
        return result
    
    @route(route=['/api/v1/category/',
                  '/api/v1/category/<int:category_id>'],
           methods=['GET'], type='json', auth='public', csrf=False)
    @token_required()
    def get_category(self, category_id=False, debug=False, **kwargs):
        category = request.env['product.category'].with_user(
            kwargs.get('uid', 1)).api_get_category(category_id=category_id)
        result = {}
        result['result'] = category
        return result
