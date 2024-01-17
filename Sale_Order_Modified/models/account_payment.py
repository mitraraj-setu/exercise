from odoo import fields, models, api, _, Command
import odoorpc

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    # def _create_partner(self, payment, partners, companies):
        # odoo = odoorpc.ODOO('ishani-setu', port=8016)
        # odoo.login('real_estate_v16_2023_10_24', 'admin', 'admin')
        # absent_companies = []
        # absent_partners = []
        # payment = self.env['account.payment']
        # pay_id_list = payment.search([])
        # for pay in pay_id_list:
        #     payment = self.browse(pay)
        #     if payment.company_id.name not in companies:
        #         absent_companies.append(payment.company_id.name)
        #         continue
        #     if payment.partner_id.name not in partners:
        #         absent_partners.append(payment.partner_id.name)
        #         continue
        # if



    def _create_payment(self):
        odoo = odoorpc.ODOO('ishani-setu', port=8016)

        odoo.login('real_estate_v16_2023_10_24', 'admin', 'admin')

        pay_id_list = []
        if 'account.payment' in odoo.env:
            payment = odoo.env['account.payment']
            pay_id_list = payment.search([])
            companies = odoo.env['res.company'].search_read([], ['name'])
            present_companies = [company.get('name') for company in companies]
            absent_companies = []
            for pay in payment.browse(pay_id_list):
                if pay.company_id.name not in present_companies:
                    absent_companies.append(pay.company_id.name)
                    continue
                vals = {'partner_type': pay.partner_type, 'posted_before': pay.posted_before,
                        'company_id': pay.company_id.id,
                        'paired_internal_transfer_payment_id': pay.paired_internal_transfer_payment_id.id,
                        'is_internal_transfer': pay.is_internal_transfer, 'payment_type': pay.payment_type,
                        'partner_id': pay.partner_id.id, 'amount': pay.amount, 'currency_id': pay.currency_id.id,
                        'date': str(pay.date), 'ref': pay.ref, 'journal_id': pay.journal_id.id,
                        'payment_method_line_id': pay.payment_method_line_id.id,
                        'payment_token_id': pay.payment_token_id.id, 'partner_bank_id': pay.partner_bank_id.id,
                        'destination_journal_id': pay.destination_journal_id.id, 'edi_document_ids': [(6, 0, pay.edi_document_ids.ids)]}
                payment.create(vals)

        # payment = self.env['account.payment']
        # pay_id_list = payment.search([])
        # for pay in pay_id_list:
        #     vals = {'partner_type': pay.partner_type, 'posted_before': pay.posted_before,
        #             'company_id': pay.company_id.id,
        #             'paired_internal_transfer_payment_id': pay.paired_internal_transfer_payment_id,
        #             'is_internal_transfer': pay.is_internal_transfer, 'payment_type': pay.payment_type,
        #             'partner_id': pay.partner_id, 'amount': pay.amount, 'currency_id': pay.currency_id.id,
        #             'date': pay.date, 'ref': pay.ref, 'journal_id': pay.journal_id.id,
        #             'payment_method_line_id': pay.payment_method_line_id.id,
        #             'payment_token_id': pay.payment_token_id.id, 'partner_bank_id': pay.partner_bank_id.id,
        #             'destination_journal_id': pay.destination_journal_id.id,
        #             'edi_document_ids': pay.edi_document_ids}
        #     payment.create(vals)
