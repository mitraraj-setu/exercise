from odoo import fields, models, api, _, Command
import odoorpc

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    # def _create_partner(self, payment, partners, companies):
    #     odoo = odoorpc.ODOO('ishani-setu', port=8016)
    #     odoo.login('real_estate_v16_2023_10_24', 'admin', 'admin')
    #     absent_companies = []
    #     absent_partners = []
    #     payment = self.env['account.payment']
    #     pay_id_list = payment.search([])
    #     for pay in pay_id_list:
    #         payment = self.browse(pay)
    #         if payment.company_id.name not in companies:
    #             absent_companies.append(payment.company_id.name)
    #             continue
    #         if payment.partner_id.name not in partners:
    #             absent_partners.append(payment.partner_id.name)
    #             continue
        # if

    # def create_payments(self):
    #     import odoorpc
    #     odoo = odoorpc.ODOO('ishani-setu', port=8016)
    #
    #     odoo.login('sale_order_v16_2023_10_24', 'admin', 'admin')
    #     odoo.env['ir.config_parameter'].set_param('account.use_invoice_terms', True)
    #     if 'account.payment' in odoo.env:
    #         pay_id_list = self.env['account.payment'].search([])
    #         for pay in pay_id_list:
    #             payment = pay
    #             partner = odoo.env['res.partner'].search([('name', '=', payment.partner_id.name)])
    #             company = odoo.env['res.company'].search([('name', '=', payment.company_id.name)])
    #             vals = {'partner_type': payment.partner_type, 'posted_before': payment.posted_before,
    #                     'company_id': odoo.env['res.partner'].browse(company[0]).id or odoo.env.company.id,
    #                     'paired_internal_transfer_payment_id': payment.paired_internal_transfer_payment_id.id,
    #                     'is_internal_transfer': payment.is_internal_transfer, 'payment_type': payment.payment_type,
    #                     'partner_id': odoo.env['res.partner'].browse(partner[0]).id, 'amount': payment.amount, 'currency_id': payment.currency_id.id,
    #                     'date': str(payment.date), 'ref': payment.ref, 'journal_id': payment.journal_id.id,
    #                     'payment_method_line_id': payment.payment_method_line_id.id,
    #                     'payment_token_id': payment.payment_token_id.id, 'partner_bank_id': payment.partner_bank_id.id,
    #                     'destination_journal_id': payment.destination_journal_id.id,
    #                     'edi_document_ids': [(6, 0, payment.edi_document_ids.ids)]}
    #             odoo.env['account.payment'].create(vals)
