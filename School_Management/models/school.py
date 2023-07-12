from datetime import date
from odoo import fields, api, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.translate import _
import re
class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ["mail.thread"]
    _description = 'Student Management Module'
    _rec_name="roll_number"
    _order="enroll asc"

    name = fields.Char(required=True)
    std_div = fields.Char()
    roll_number = fields.Integer()
    phone = fields.Char(required=True, tracking=True)
    enroll = fields.Char(readonly=1,tracking=True)
    class_teacher = fields.Many2one('school.teacher', compute="_compute_class_teacher", store=True)
    dob = fields.Date(tracking=True)
    age = fields.Integer(compute="_compute_age", store=True)
    birth_month = fields.Selection([
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ],tracking=True, store=True)
    active = fields.Boolean('Active', default=True)
    parent_name = fields.Char()
    relation_with_student = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian'),
    ], tracking=True, default='father')
    phone_parent = fields.Char(tracking=True)
    email_parent = fields.Char()
    student_prev_school = fields.Char()
    enroll_prev_school = fields.Integer()
    prev_school_adm_date = fields.Date()
    prev_school_leaving_date = fields.Date()
    stream = fields.Selection([
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
    ],store=True)    
    fee_status = fields.Selection([
        ('paid', 'Paid'), 
        ('half_paid', 'Half Paid'), 
        ('pending', 'Pending')
    ], string='Fee Status',store=True)
    transport=fields.Many2one('res.users',string="Transport Incharge")
    image=fields.Image(string="Display picture")
    street = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=', country_id)]")
    country_id = fields.Many2one('res.country')
    country_code=fields.Char(related="country_id.code")
    zip = fields.Char(string='ZIP')
    phone_code = fields.Char(readonly=True)
    formatted_address = fields.Char(string='Student Address', compute='_compute_formatted_address')

    @api.depends('street', 'city', 'state_id', 'zip', 'country_id')
    def _compute_formatted_address(self):
        for partner in self:
            address_parts = [partner.street, partner.city, partner.state_id.name, partner.zip, partner.country_id.name]
            partner.formatted_address = ', '.join(filter(None, address_parts))
            
    grade_level = fields.Integer(string='Grade Level')

    def action_url(self):
        return{
            'type':'ir.actions.act_url',
            'target':'new',
            'url':'https://www.odoo.com/documentation/16.0/'
        }
    @api.depends('std_div', 'stream', 'grade_level')
    def _compute_class_teacher(self):
        for student in self:
            if student.grade_level and student.grade_level >= 11:
                if student.stream:
                    teacher = self.env['school.teacher'].search([
                    ('std_div', '=', student.std_div),
                    ('stream', '=', student.stream)
                ], limit=1)
                    student.class_teacher = teacher.id if teacher else False
                else:
                    student.class_teacher = False
            else:
                if student.std_div:
                    teacher = self.env['school.teacher'].search([
                    ('std_div', '=', student.std_div)
                ], limit=1)
                    student.class_teacher = teacher.id if teacher else False
                else:
                    student.class_teacher = False
                    
    @api.constrains('name')
    def check_name(self): 
        for rec in self:    
            if not 4 <= len(rec.name) <= 15 or not re.match(r"^[a-zA-Z][ a-zA-Z]*", rec.name):
                raise ValidationError(_('Name field only contain 10-15 alphabets and spaces'))   
                       
    status=fields.Selection([
        ('applied',"Applied"),
        ('cleared_entrance_test',"Cleared"),
        ('selected',"Selected"),
        ('joined_school',"Joined"),
        ('rejected',"Rejected"),
    ],default="applied",string="Status",required=True)            

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            self.phone_code = self.country_id.phone_code
        else:
            self.phone_code = False
            
    def change_status(self):
        for rec in self:
            if rec.status == 'joined_school':
                rec.fee_status = 'paid'
            else:
                rec.fee_status = 'pending'
            
    def action_done(self):
        for rec in self:
            rec.status='selected'
    
    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for student in self:
            if student.dob:
                check_age = today.year - student.dob.year
                if check_age < 4:
                    raise ValidationError('Age cannot be less than 4')
                student.age = check_age
            else:
                student.age = 0
    def name_get(self):
        return [(record.id, '%s - %s' %(record.enroll,record.name)) for record in self]

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|',('name', operator, name), ('enroll', operator, name)]
        return super(SchoolStudent, self).search(domain, limit=limit).name_get()
    
    @api.constrains('phone')
    def _check_unique_phone_number(self):
        for student in self:
            if student.phone:
                duplicate_phone = self.search([('phone', '=', student.phone), ('id', '!=', student.id)])
                if duplicate_phone:
                    raise ValidationError('Phone number is already assigned to another student!')

    @api.model
    def create(self,vals):
        vals['enroll']=self.env['ir.sequence'].next_by_code("school.student")
        return super(SchoolStudent,self).create(vals)

    @api.constrains('phone','phone_parent')
    def _check_phone_number(self):
        for rec in self:
            if rec.phone and rec.phone_parent and len(rec.phone) != 10:
                raise ValidationError(_("Phone number should be 10 digits long."))
        return True

    @api.constrains('dob')
    def validation_constraints(self):
        today = fields.Date.today()
        for rec in self:
            if rec.dob and rec.dob > today:
                raise ValidationError(_("Invalid Date of Birth."))



