import logging
from odoo import models, fields, _, api

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    season_ids = fields.Many2many('season.tag', String='Seasons')


    def _prepare_invoice(self):
        invoice_vals = super(PurchaseOrder, self)._prepare_invoice()
        invoice_vals['season_ids'] = self.season_ids
        return invoice_vals
        