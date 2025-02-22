
# customer form
from odoo import models, fields,api

class Customer(models.Model):
    _name = 'registration.form'
    _description = 'Customer Form'

    # partner_id = fields.Many2one('res.partner', string="Related Partner", required=True)
    # name = fields.Char(string='Name', related="partner_id.name", readonly=True)
    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone Number')
    product = fields.Char(string='Product')
    product_details = fields.Text(string='Product Details')
    date = fields.Date(string='Purchase Date', default=fields.Date.context_today)


class ComplaintForm(models.Model):
    _name = 'complaint.form'
    _description = 'Complaint Form'

    complaint_id = fields.Char(string='Complaint ID', readonly=True, copy=False, default='New')
    customer_id = fields.Many2one('registration.form', string='Customer', required=True)  # Link to Customer Form
    product = fields.Char(string='Product', related='customer_id.product', readonly=True)
    product_details = fields.Text(string='Product Details', related='customer_id.product_details', readonly=True)
    complaint_details = fields.Text(string='Complaint Details', required=True)
    complaint_date = fields.Date(string='Complaint Date', default=fields.Date.context_today)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ], string="Status", default='new', required=True)

    @api.model
    def create(self, vals):
        """ Generate a unique Complaint ID when creating a record """
        if vals.get('complaint_id', 'New') == 'New':
            vals['complaint_id'] = self.env['ir.sequence'].next_by_code('complaint.sequence') or 'New'
        return super(ComplaintForm, self).create(vals)

    def action_open(self):
        """Change status to 'In Progress' and generate Complaint ID if not set"""
        for record in self:
            if not record.complaint_id or record.complaint_id == 'New':
                record.complaint_id = self.env['ir.sequence'].next_by_code('complaint.sequence')
            record.status = 'in_progress'

    def action_close(self):
        """Change status to 'Closed'"""
        for record in self:
            record.status = 'closed'
