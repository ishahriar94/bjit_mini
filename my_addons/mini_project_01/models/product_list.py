
from datetime import timedelta
from odoo import models, fields, api
from odoo import api 
from odoo.exceptions import ValidationError
import re 

class productList(models.Model):
    _name = 'product.list'
    _description = 'Product Details'
   

    sequence = fields.Integer(default=10)
    pname = fields.Char(string='Product Name',required=True)

    ##Sql Constraints To validate the Price Fileds Input. 
    _sql_constraints = [ 
        ('check_cost', 'CHECK(cost >= 0)', 'The cost must be strictly positive'),
        
        
    ]
    _sql_constraints = [ 
        ('check_sale_price', 'CHECK(sale_price >= 0)', 'The expected selling price must be positive')
        
    ]

    

    ## model creation
    pname = fields.Char(string='Product Name',required=False)
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
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('classified', 'Classified')
    ])
    country = fields.Selection([('option1', 'Bangladesh'), ('option2', 'United States'), ('option3', 'Canada')], string='Country')
    
    #automatically classified object 
    

    warehouse = fields.Many2many('warehouse.list', string="Warehouse")



    #naming Constraints for products
    # @api.constrains('pname')
    # def check_name_in_products(self):
    #     for rec in self:
    #         error = self.env['product.list'].search([('pname', '=', rec.pname)])
    #         if rec.pname == error:
    #             raise ValidationError(("Name %s Already Exists" % rec.pname))

    #onchange field for products
    @api.onchange('pname')
    def _onchange_status(self):
        #automatically classified object
        autoclass = ['Boing747', 'B12Bomber', 'Drone']
        for record in self:
            if record.pname == 'Boing747':     #we can make a list here
                self.status = 'classified'
    ##Computed Field Based on Taxation
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

        


    def update_status(self):
            for record in self:
                if (record.status == 'available'):
                    record.status = 'unavailable'
                elif (record.status == 'unavailable'):
                     record.status = 'available'
                

                
                

    def action_url(self):
        return {
            'type':'ir.actions.act_url',
            'target': 'new',
            'url': ' http://localhost:8015/web#action=164&model=warehouse.list&view_type=list&cids=&menu_id=129' ,
        }
    

    
