from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
class HRMSEmployee(models.Model):
    _name = 'hrms.employee'
    _description = 'HRMS Employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'employee_id asc'
    # Personal Info
    name = fields.Char(string='Full Name', required=True, tracking=True)
    employee_id = fields.Char(string='Employee ID', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    email = fields.Email(string='Email', required=True, tracking=True)  # Built-in validation
    phone = fields.Char(string='Phone')
    image_1920 = fields.Image(string='Profile Picture', max_width=1920, max_height=1920)
    # Address (Split for better DB design)
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='ZIP')
    country_id = fields.Many2one('res.country', string='Country')
    # Professional Info
    department = fields.Char(string='Department', tracking=True)
    job_title = fields.Char(string='Job Title', tracking=True)
    user_id = fields.Many2one('res.users', string='User Account', ondelete='restrict')
    active = fields.Boolean(string='Active', default=True)
    # Payroll (Monetary field with currency)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    salary = fields.Monetary(string='Monthly Salary', currency_field='currency_id', tracking=True)
    _sql_constraints = [
        ('unique_employee_id', 'UNIQUE(employee_id)', 'Employee ID must be unique!'),
        ('unique_email', 'UNIQUE(email)', 'Email must be unique!'),
    ]
    @api.model
    def create(self, vals):
        if vals.get('employee_id', _('New')) == _('New'):
            vals['employee_id'] = self.env['ir.sequence'].next_by_code('hrms.employee') or _('New')
        return super(HRMSEmployee, self).create(vals)
    def action_toggle_active(self):
        for rec in self:
            rec.active = not rec.active
