from odoo import fields, models

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'
    _inherit = ["mail.thread"]
    name = fields.Char(string='Class Teacher Name',tracking=True, required=True,store=True)
    active = fields.Boolean('Active', default=True)
    teacher_id = fields.Integer(string='Class-Teacher ID',tracking=True, required=True)
    grade_level = fields.Integer(string='Grade Level',required=True,store=True)
    std_div = fields.Char(string='Standard-Division', required=True,store=True)
    phone = fields.Char(string='Contact no',  tracking=True)
    student_id = fields.One2many('school.student', 'class_teacher', string='students')
    image=fields.Image(string="Display picture")
    stream = fields.Selection([
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
    ], string='Stream', store=True)
    _sql_constraints = [
        ('unique_teacher', 'unique (std_div, stream)', 'Teacher name already exists!'),
    ]