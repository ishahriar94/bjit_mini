from odoo import models, fields, api
from odoo import api 
from odoo.exceptions import ValidationError
import re 


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
    

    #name constraint for warehouse
    # @api.constrains('wname')
    # def check_title(self):
    #     for rec in self:
    #         werror = self.env['warehouse.list'].search([('wname', '=', rec.wname)])
    #         if werror:
    #             raise ValidationError(('Same Name Can not be added'))
    
    #Email constraints for warehouse
    # @api.constrains('wemail')
    # def _check_email(self):
    #     for record in self:
    #         valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.wemail)
            
    #         if valid_email == None:
    #             raise ValidationError('Please provide a valid E-mail')
