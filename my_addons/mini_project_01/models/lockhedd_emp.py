from odoo import models, fields,api



class hr_lockheed(models.Model):
   
    _inherit     = 'hr.employee'
    _description = 'Employee Details'

    
    name = fields.Char("Employee Name")
    
    job_title = fields.Char("Job Title")
    # department_id = fields.Char("Department")
    work_email = fields.Char('Work Email')
   