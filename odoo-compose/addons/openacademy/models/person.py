from odoo import models, fields

class Person(models.Model):
    _name = 'openacademy.person'
    _description = 'OpenAcademy clase Persona'

    name = fields.Char(string='Name', required=True)
    
    instructor = fields.Boolean(string='Instructor', default=False)

    teacher_level = fields.Selection([
        ('1', 'Teacher / Level 1'),
        ('2','Teacher / Level 2')
    ], string='Teacher Level ')

    session_ids = fields.Many2many('openacademy.session', relation='openacademy_session_person_rel', string='Attended Sessions')