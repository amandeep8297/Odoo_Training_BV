from odoo import fields,models

class NewAdmissionWizard(models.TransientModel):
    _name="admission.wizard"
    _description="New Admission Wizard"
    
    signature=fields.Char(required=True)
    birth_year=fields.Many2one('school.student',required=True)
    def action_create_admission(self):
        print("Button is clicked")