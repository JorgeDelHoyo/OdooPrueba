from odoo import models, fields

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Session'

    # Los campos que pide el ejercicio
    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date")
    duration = fields.Float(string="Duration (in days)",digis=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of Seats")

    # --- Ejercicios de Relaciones ---
    # Ejercicio: Many2one relations
    # Una sesión tiene un instructor (del modelo 'res.partner')
    instructor_id = fields.Many2one('res.partner', string="Instructor")

    # Una sesión pertenece a un curso (del modelo 'openacademy.course')
    # Es obligatorio ('required=True')
    course_id = fields.Many2one('openacademy.course', string="Course", required=True)

    # Ejercicio: Multiple many2many relations
    # Una sesión tiene muchos asistentes (partners, del modelo 'res.partner')
    attendee_ids = fields.Many2many('res.partner', relation='openacademy_session_attendees_rel',string="Attendees")