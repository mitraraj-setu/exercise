from odoo import models, fields
from odoo.exceptions import ValidationError, UserError
import base64
from collections import defaultdict
import xlrd
import io


class SetuSaleOrderImportWizard(models.TransientModel):
    _name = 'setu.sale.order.import.wizard'
    _description = 'Import order'

    file = fields.Binary(string="Upload File", required=True)
    file_name = fields.Char(string="File Name")

    def action_import(self):

        if not self.file:
            raise ValidationError("Please upload a file.")

        file_content = base64.b64decode(self.file)
        file_stream = io.BytesIO(file_content)

        workbook = xlrd.open_workbook(file_contents=file_stream.read())
        print(f"Workbook: {workbook}")

        sheet = workbook.sheet_by_index(0)
        print(f"Sheet: {sheet.name}")

        headers = [sheet.cell_value(0, col).strip() for col in range(sheet.ncols)]
        print(f"headers: {headers}")

        col_indexes = {col_name: idx for idx, col_name in enumerate(headers)}
        print(f"col_indexes: {col_indexes}")

        required_columns = ["Customer", "Product", "Quantity"]
        if not all(col in col_indexes for col in required_columns):
            raise UserError(f"File must contain columns: Customer, Product, Quantity.")

        orders_dict = defaultdict(list)
        last_customer = None

        for row_idx in range(1, sheet.nrows):
            customer = sheet.cell_value(row_idx, col_indexes.get("Customer")).strip() or last_customer
            product = sheet.cell_value(row_idx, col_indexes.get("Product")).strip()
            quantity = sheet.cell_value(row_idx, col_indexes.get("Quantity")) or 0

            try:
                quantity = float(quantity)
                if quantity <= 0:
                    raise ValueError
            except :
                raise UserError(f"Invalid Quantity. You must enter a positive number.")

            if not customer or not product :
                raise UserError("Missing Customer or Product.")

            last_customer = customer

            orders_dict[customer].append({"product": product, "quantity": quantity})
        print(f"orders_dict: {orders_dict}")

        saleorder_object = self.env["sale.order"]
        partner_object = self.env["res.partner"]
        product_object = self.env["product.product"]

        for customer, products in orders_dict.items():

            customer_id = partner_object.search([("name", "=", customer)], limit=1)
            if not customer_id:
                customer_id = partner_object.create({"name": customer})

            sale_order = saleorder_object.create({"partner_id": customer_id.id})

            for product_info in products:
                product = product_info.get("product")
                quantity = product_info.get("quantity")

                product_id = product_object.search([("name", "=", product)], limit=1)
                if not product_id:
                    product_id = product_object.create({
                        "name": product,
                        "type": "consu",
                        "list_price": 50.0,
                    })

                sale_order.order_line.create({
                    "order_id": sale_order.id,
                    "product_id": product_id.id,
                    "name": product_id.name,
                    "product_uom_qty": quantity,
                    "price_unit": product_id.list_price,
                })

        return {
        "type": "ir.actions.client",
        "tag": "reload",
        }

    def action_cancel(self):
        print("cancel")
        return {'type': 'ir.actions.act_window_close'}


































