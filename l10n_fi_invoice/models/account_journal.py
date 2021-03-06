##############################################################################
#
#    Author: Avoin.Systems
#    Copyright 2019 Avoin.Systems
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    include_on_invoice = fields.Boolean(
        "Include on Invoice",
        help="Include this bank account in Finnish invoices generated for the associated company",
        default=True
    )
