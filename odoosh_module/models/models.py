# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoosh_module(models.Model):
#     _name = 'odoosh_module.odoosh_module'
#     _description = 'odoosh_module.odoosh_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
