from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    responsible_id = fields.Many2one('res.users', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session','course_id', string="Sessions")

    # Ejercicio: SQL constraints
    _sql_constraints = [
        ('name_description_check', 'CHECK(name != description)', "The title of the course should not be the description"),
        ('name_unique', 'UNIQUE(name)', "The course title must be unique"),
    ]

    # Ejercicio: Add a duplicate option
    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count([('name', '=like', f"Copy of {self.name}%")])
        if not copied_count:
            new_name = f"Copy of {self.name}"
        else:
            new_name = f"Copy of {self.name} ({copied_count})"
        default['name'] = new_name
        return super(Course, self).copy(default)