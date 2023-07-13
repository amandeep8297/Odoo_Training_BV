from odoo import fields,models,api
import datetime
class CancelAdmissionWizard(models.TransientModel):
    _name="cancel_admission.wizard"
    _description="Cancel Admission Wizard"
    
    student_id=fields.Many2one('school.student',required=True)
    reason=fields.Text()
    date_cancel=fields.Date(string="Cancellation Date")

    @api.model
    def default_get(self,fields):
        res=super(CancelAdmissionWizard,self).default_get(fields)
        res['date_cancel']=datetime.date.today()
        return res
    
    def action_cancel_admission(self):
        for rec in self:
            rec.student_id.unlink()
            
