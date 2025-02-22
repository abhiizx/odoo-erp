# -*- coding: utf-8 -*-
# from odoo import http


# class RegistrationForm(http.Controller):
#     @http.route('/registration_form/registration_form/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registration_form/registration_form/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('registration_form.listing', {
#             'root': '/registration_form/registration_form',
#             'objects': http.request.env['registration_form.registration_form'].search([]),
#         })

#     @http.route('/registration_form/registration_form/objects/<model("registration_form.registration_form"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registration_form.object', {
#             'object': obj
#         })
