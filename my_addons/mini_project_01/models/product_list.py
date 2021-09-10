
from datetime import timedelta
from odoo import models, fields, api


class productList(models.Model):
    _name = 'product.list'
    _description = 'Product Details'
   
    pname = fields.Char(string='Product Name',required=True)
    avaiable_from = fields.Date(string='Available From')
    available_till = fields.Date(string='Available Till')
    description = fields.Char(string='Description')
    cost = fields.Float(string='Cost',required=True)
    sale_price = fields.Float(string='Sales Price',required=True)
    cus_sold = fields.Boolean(string='Can be Sold')
    cus_purchase = fields.Boolean(string='Can be Purchased')
    product_image = fields.Image(string="Upload", max_width=100, max_height=100, verify_resolution=False)
    status = fields.Selection([
        ('available','Available'),
        ('unavailable', 'Unavailable')
    ])


    

    
