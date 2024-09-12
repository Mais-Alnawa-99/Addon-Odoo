from logging import warning
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request
import json


class ApiPoint(http.Controller):
    @http.route("/property", methods=["POST"], type="json", auth="none", csrf=False)
    def create_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        try:
            res = request.env['property'].sudo().create(vals)
            return {
                'message': "we  create the record",
            }

        except Exception as error:
            return ({
                'error': error
            })

    @http.route("/up_property/<int:property_id>", methods=["PUT"], type="json", auth="none", csrf=False)
    def update_property(self, property_id):
        try:
            if not property_id:
                return {
                    'error': "the id is not validation"}
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            property_id.write(vals)
            print(property_id.postcode)
            return {
                'message': "we  update the record",
                'postcode': property_id.postcode
            }

        except Exception as error:
            return request.make_json_response({
                'error': error
            })

    @http.route("/re_property/<int:property_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def read_property(self, property_id):
        try:
            if not property_id:
                return request.make_json_response({
                    'error': "the id is not validation"})
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            return request.make_json_response({
                'postcode': property_id.postcode,
                "name": property_id.name,
                "bedrooms": property_id.bedrooms,
                "date_availability": property_id.date_availability,
                "description": property_id.description
            })
        except Exception as error:
            return request.make_json_response({
                'error': error
            })

    @http.route("/de_property/<int:property_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_property(self, property_id):
        try:
            if not property_id:
                return request.make_json_response({
                    'error': "the id is not validation"})
            property_id = request.env['property'].sudo().search([('id', '=', property_id)])
            print(property_id)
            property_id.unlink()

            return request.make_json_response({
                "message": "the record delete"
            })
        except Exception as error:
            return request.make_json_response({
                'error': error
            })

    @http.route("/properties", methods=["GET"], type="http", auth="none", csrf=False)
    def read_property_list(self):
        try:
            params = parse_qs(request.httprequest.query_string.decode('utf-8'))
            print(params)
            property_domain = []
            print(property_domain)
            if params.get('state'):
                property_domain += [('state', '=', params.get('state')[0])]  #the first item in state
            property_ids = request.env['property'].sudo().search(property_domain)
            if not property_ids:
                return request.make_json_response({
                    'error': "the list is empty"})
            return request.make_json_response([{
                'postcode': property_id.postcode,
                "name": property_id.name,
                "bedrooms": property_id.bedrooms,
                "date_availability": property_id.date_availability,
                "description": property_id.description
            } for property_id in property_ids])
        except Exception as error:
            return request.make_json_response({
                'error': error
            })
