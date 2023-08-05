from odoo import models,api,fields


class SchoolConfig(models.TransientModel):
    _inherit = 'res.config.settings'
    
    school = fields.Char(string="School Name", config_parameter='school_management.school')
    module_enabled = fields.Boolean(string="Enable School Module", default=True)
    student_registration_fee = fields.Float(string="Student Registration Fee", default=100.0)
    allow_multiple_courses = fields.Boolean(string="Allow Multiple Courses", default=True)
    allow_student_transfers = fields.Boolean(string="Allow Student Transfers", default=True)
    teacher_contract_period = fields.Integer(string="Teacher Contract Period (Months)", default=12)
    allow_teacher_leave_management = fields.Boolean(string="Allow Teacher Leave Management", default=True)
    defult_class_capacity = fields.Integer(string="Default Class Capacity", default=30)
    allow_online_classes = fields.Boolean(string="Allow Online Classes", default=True)
    enable_exam_management = fields.Boolean(string="Enable Exam Management", default=True)
    enable_grading_system = fields.Boolean(string="Enable Grading System", default=True)

    def set_values(self):
        super(SchoolConfig, self).set_values()
        config_param = self.env['ir.config_parameter'].sudo()
        self.env['school.student'].sudo().search([]).write({'name': self.school})
        config_param.set_param('school_management.school', self.school)
        config_param.set_param('school_management.module_enabled', self.module_enabled)
        config_param.set_param('school_management.student_registration_fee', str(self.student_registration_fee))
        config_param.set_param('school_management.allow_multiple_courses', self.allow_multiple_courses)
        config_param.set_param('school_management.allow_student_transfers', self.allow_student_transfers)
        config_param.set_param('school_management.teacher_contract_period', str(self.teacher_contract_period))
        config_param.set_param('school_management.allow_teacher_leave_management', self.allow_teacher_leave_management)
        config_param.set_param('school_management.defult_class_capacity', str(self.defult_class_capacity))
        config_param.set_param('school_management.allow_online_classes', self.allow_online_classes)
        config_param.set_param('school_management.enable_exam_management', self.enable_exam_management)
        config_param.set_param('school_management.enable_grading_system', self.enable_grading_system)

    def get_values(self):
        res = super(SchoolConfig, self).get_values()
        config_param = self.env['ir.config_parameter'].sudo()
        res.update(
            module_enabled=config_param.get_param('school_management.module_enabled', default=True),
            student_registration_fee=float(config_param.get_param('school_management.student_registration_fee', default=100.0)),
            allow_multiple_courses=config_param.get_param('school_management.allow_multiple_courses', default=True),
            allow_student_transfers=config_param.get_param('school_management.allow_student_transfers', default=True),
            teacher_contract_period=int(config_param.get_param('school_management.teacher_contract_period', default=12)),
            allow_teacher_leave_management=config_param.get_param('school_management.allow_teacher_leave_management', default=True),
            defult_class_capacity=int(config_param.get_param('school_management.defult_class_capacity', default=0)),
            allow_online_classes=config_param.get_param('school_management.allow_online_classes', default=True),
            enable_exam_management=config_param.get_param('school_management.enable_exam_management', default=True),
            enable_grading_system=config_param.get_param('school_management.enable_grading_system', default=True),
        )

        return res