


from odoo import models, fields, api


class productList(models.Model):
    _name = 'product.list'
    _description = 'Product Details'
   
    pname = fields.Char(string='Product Name',required=True)
    cost = fields.Float(string='Cost',required=True)
    sale_price = fields.Float(string='Sales Price',required=True)
    cus_sold = fields.Boolean(string='Can be Sold')
    cus_purchase = fields.Boolean(string='Can be Purchased')
    status = fields.Selection([
        ('available','Available'),
        ('unavailable', 'Unavailable')
    ])


    

    
