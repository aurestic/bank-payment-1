# Copyright 2017 Tecnativa - Luis M. Ontalba
# Copyright 2021 Tecnativa - João Marques
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class AccountPaymentLineCreate(models.TransientModel):
    _inherit = "account.payment.line.create"

    include_returned = fields.Boolean(string="Include move lines from returns")

    @api.depends(
        "date_type",
        "move_date",
        "due_date",
        "journal_ids",
        "invoice",
        "target_move",
        "allow_blocked",
        "payment_mode",
        "partner_ids",
    )
    def _compute_move_line_domain(self):
        result = super()._compute_move_line_domain()
        domain = self.move_line_domain
        if not self.include_returned:
            domain += [
                ("move_id.returned_payment", "=", False),
            ]
        self.move_line_domain = domain
        return result
