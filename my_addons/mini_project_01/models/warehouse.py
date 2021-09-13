from odoo import models, fields, api

class warehouseList(models.Model):
    _name = 'warehouse.list'
    _inherit = {'product.list': 'related_product'}
    _description = 'WareHouse Details'
   
    wname = fields.Char(string='WareHouse Name',required=True)
    wtype = fields.Selection([
        ('private','Private'),
        ('open', 'Open')
    ])
    
    wlocation = fields.Char(string='Location')
    wphone = fields.Char(string='Phone')
    wemail = fields.Char(string='Email Address')
    
    ##delegated inheritance
    related_product = fields.Many2many('product.list', string='Available Products')

    wmanage = fields.Many2one('hr.employee', string='Manager')
