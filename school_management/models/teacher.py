from odoo import fields,api, models
from random import randint
class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'
    _inherit = ["mail.thread"]
   
    name = fields.Char(tracking=True, required=True,store=True)
    active = fields.Boolean('Active', default=True)
    teacher_id = fields.Integer(string='Class-Teacher ID',tracking=True, required=True)
    grade_level = fields.Integer(string='Grade Level',required=True,store=True)
    std_div = fields.Char(string='Standard-Division', required=True,store=True)
    phone = fields.Char(string='Contact no',  tracking=True)
    student_id = fields.One2many('school.student', 'class_teacher', string='students')
    teacher_image=fields.Image(string="Display picture")
    stream = fields.Selection([
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
    ], string='Stream', store=True)
    sibling=fields.Many2one("school.student",string="Sibling ID")
    _sql_constraints = [
        ('unique_teacher', 'unique (std_div, stream)', 'Teacher name already exists!'),
    ]
    street = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=', country_id)]")
    country_id = fields.Many2one('res.country')
    country_code=fields.Char(related="country_id.code")
    zip = fields.Char(string='ZIP')
    phone_code = fields.Char(readonly=True)
    tg_of=fields.One2many('school.student','tg')
    def rainbow_effect(self):
        return{
            'effect':{
                'fadeout':'fast',
                'message':'Saved Successfully',
                'type':'rainbow_man'
            }
        }
       
    def copy(self, default=None):
        if default is None:
            default = {}
            
        default.update({
            'name' : self.name[:-2] + str(self.id),
            'phone' : str(randint(pow(10, 9), pow(10, 10)-1)),
            'std_div' : self.std_div[:-2] + str(self.id)
        })
        return super(SchoolTeacher, self).copy(default)
    def action_to_do_list(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'http://127.0.0.1:5500/school_management/static/src/index.html',
}
    @api.model
    def name_search(self, args=None,limit=100):
        if args is None:
            args = []
        query = """SELECT * FROM school_teacher WHERE name='Prithvi 01'"""
        self.env.cr.execute(query)
        return self.env.cr.fetchall().name_search()       