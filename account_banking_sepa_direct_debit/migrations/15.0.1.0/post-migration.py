# Copyright 2024 Aures TIC - Jose Zambudio Bernabeu
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
            INSERT INTO account_payment_method_line
            (name, payment_method_id, journal_id)
            SELECT apm.name, apm.id, aj.id
            FROM account_payment_method apm
            JOIN account_journal aj ON aj.type IN ('bank', 'cash')
            WHERE apm.code = 'sepa_direct_debit'
        """,
    )
