from odoo import fields, api, models

class SportsPlayer(models.Model):
    _name = "sports.player"
    _inherit = ["mail.thread"]
    _description="Sports data"
    _rec_name = 'height'
    
    name = fields.Many2many('school.student','game',string="Student Name ")
    height=fields.Float()
    weight=fields.Float()
    game=fields.Char(string="Game Name")
    drag = fields.Integer()
    sports_img = fields.Image(string="Display picture")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male')
    sports_teacher=fields.Many2one('school.teacher')
    bloodgrp = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'),
        ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('other', 'Other'),
    ])
    
    @api.model
    def name_create(self,game):
        print(self._context)
        return self.create({'game':game}).name_get()[0]
    
    # @api.onchange('images')
    # def check_image(self):
    #     for rec in self:
    #         print(rec.images)