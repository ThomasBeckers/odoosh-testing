# -*- coding: utf-8 -*-
# from odoo import http


# class OdooshModule(http.Controller):
#     @http.route('/odoosh_module/odoosh_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoosh_module/odoosh_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoosh_module.listing', {
#             'root': '/odoosh_module/odoosh_module',
#             'objects': http.request.env['odoosh_module.odoosh_module'].search([]),
#         })

#     @http.route('/odoosh_module/odoosh_module/objects/<model("odoosh_module.odoosh_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoosh_module.object', {
#             'object': obj
#         })
