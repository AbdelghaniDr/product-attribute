# coding: utf-8
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Akretion (<http://www.akretion.com>).
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


from openerp import models, fields


class ProductProfile(models.Model):
    _inherit = 'product.profile'

    def _get_types(self):
        return [('product', 'Stockable Product'),
                ('consu', 'Consumable'),
                ('service', 'Service')]

    sale_ok = fields.Boolean(
        string='Can be Sold',
        help="Specify if the product can be selected in a sales order line.")
    purchase_ok = fields.Boolean(
        string='Can be Purchased')
    available_in_pos = fields.Boolean()
    route_ids = fields.Many2many(
        'stock.location.route',
        string='Routes',
        domain="[('product_selectable', '=', True)]",
        help="Depending on the modules installed, this will allow "
             "you to define the route of the product: "
             "whether it will be bought, manufactured, MTO/MTS,...")
    profile_default_categ_id = fields.Many2one(
        'product.category',
        string='Default category')
