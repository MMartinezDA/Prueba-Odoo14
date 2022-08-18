from email.policy import default
import logging
from odoo import models, fields, _, api

_logger = logging.getLogger(__name__)

class Picking(models.Model):
    _inherit = 'stock.picking'

    season_ids = fields.Many2many('season.tag', String='Seasons')

    def button_validate(self):
        seasons = self.env['purchase.order'].search([('id', '=', self.purchase_id.id)])
        self.season_ids = seasons.season_ids
        return super(Picking, self).button_validate()