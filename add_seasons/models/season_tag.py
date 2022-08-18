from email.policy import default
from random import randint
from odoo import models, api, fields, _

class SeasonTag(models.Model):
    _name = 'season.tag'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(required=True)
    color = fields.Integer('Color', default=_get_default_color)