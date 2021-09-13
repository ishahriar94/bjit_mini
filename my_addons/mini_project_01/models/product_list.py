
from datetime import timedelta
from odoo import models, fields, api


class productList(models.Model):
    _name = 'product.list'
    _description = 'Product Details'
   

    sequence = fields.Integer(default=10)
    pname = fields.Char(string='Product Name',required=True)
    avaiable_from = fields.Date(string='Available From')
    available_till = fields.Date(string='Available Till')
    country = fields.Selection([('option1', 'Bangladesh'), ('option2', 'United States'), ('option3', 'Canada')], string='Country')
    description = fields.Char(string='Description')
    cost = fields.Float(string='Cost')
    sale_price = fields.Float(string='Sale Price', compute='total_cost')
    cus_sold = fields.Boolean(string='Can be Sold')
    cus_purchase = fields.Boolean(string='Can be Purchased')
    product_image = fields.Image(string="Upload", max_width=100, max_height=100, verify_resolution=False)
    status = fields.Selection([
        ('available','Available'),
        ('unavailable', 'Unavailable')
    ])



    @api.depends('cost','country')
    def total_cost(self):
        if(self.country == 'option1'):
            for record in self:
                record.sale_price = (record.cost + (record.cost*0.5))
        if(self.country == 'option2'):
            for record in self:
                record.sale_price = (record.cost + (record.cost*0.1))
        else:
            for record in self:
                record.sale_price = (record.cost + (record.cost*0.7))
        
        



    

    
