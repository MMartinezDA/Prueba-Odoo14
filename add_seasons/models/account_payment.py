from odoo import models, fields, _

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    season_ids = fields.Many2many('season.tag', String='Seasons')

    def action_post(self):
        
        seasons = self.env['account.move'].search([('id', '=', self.move_id.id)])
        self.season_ids = seasons.season_ids
        super(AccountPayment, self).action_post()
        

