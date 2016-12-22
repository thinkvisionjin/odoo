# -*- coding: utf-8 -*-
from odoo import http

class Bidding(http.Controller):
    @http.route('/bidding/bidding/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/bidding/bidding/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('bidding.listing', {
            'root': '/bidding/bidding',
            'objects': http.request.env['bidding.bidding'].search([]),
        })

    @http.route('/bidding/bidding/objects/<model("bidding.bidding"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bidding.object', {
            'object': obj
        })