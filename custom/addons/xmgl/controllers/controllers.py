# -*- coding: utf-8 -*-
from odoo import http

class Xmgl(http.Controller):
    @http.route('/xmgl/xmgl/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/xmgl/xmgl/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('xmgl.listing', {
            'root': '/xmgl/xmgl',
            'objects': http.request.env['xmgl.xmgl'].search([]),
        })

    @http.route('/xmgl/xmgl/objects/<model("xmgl.xmgl"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('xmgl.object', {
            'object': obj
        })