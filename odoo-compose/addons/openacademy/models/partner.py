from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner' # Herencia de 'res.partner'

    # 1. Campo Boolean 'instructor'
    instructor = fields.Boolean(string="Instructor", default=False)

    # 2. Campo Many2many 'session_ids'
    # Usamos el mismo 'relation' que en el 'attendee_ids' del modelo session
    session_ids = fields.Many2many('openacademy.session', relation='openacademy_session_attendees_rel',string="Attended Sessions")