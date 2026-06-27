from odoo import models, fields
from odoo.exceptions import UserError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_number = fields.Char(
        string="Employee Number",
        copy=False
    )

    def action_generate_employee_number(self):
        for employee in self:
            if not employee.employee_number:
                employee.employee_number = self.env['ir.sequence'].next_by_code(
                    'hr.employee.number'
                )
