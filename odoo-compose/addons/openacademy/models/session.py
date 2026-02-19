from odoo import models, fields
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy clase Session'

    name = fields.Char(string='Name')

    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    active = fields.Boolean(default=True)

    duration = fields.Float(string='Duration (in days)', digits=(6,2), help='Duration in days')
    seats = fields.Integer(string='Number of seats')
    color = fields.Integer(String='color')

    instructor_id = fields.Many2one('openacademy.person', string='Instructor', domain=['|',('instructor', '=', True), ('teacher_level', '!=', False)])

    course_id = fields.Many2one('openacademy.course', string='Course', required=True)

    attendee_ids = fields.Many2many('openacademy.person', string='Attendees', relation='openacademy_session_person_rel')

    taken_seats = fields.Float(string='Taken seats', compute='_compute_taken_seats')
    attendees_count = fields.Integer(string='Attendees_count', compute='_get_attendees_count', store=True)

    @api.depends('seats','attendee_ids')
    def _compute_taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
            
    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'tittle': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative"
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'tittle': "Too many attendees",
                    'message': "Increase seats or remove excess attendees"
                }
            }
        
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id and r.attendee_ids:
                raise ValidationError("A session's instructor can't be an attendee")