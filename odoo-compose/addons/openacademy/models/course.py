from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")


    # --- Ejercicios de Relaciones --- #
    # Ejercicio: Many2one relations
    # Un curso tiene un usuario responsable (del modelo 'res.users')
    responsible_id = fields.Many2one('res.users', string="Responsible", index=True)

    # Ejercicio: Inverse one2many relations
    # Un curso tiene muchas sesiones (el inverso del 'course_id' en 'session')
    session_ids = fields.One2many('openacademy.session','course_id', string="Sessions")