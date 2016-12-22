# -*- coding: utf-8 -*-

from odoo import models, fields, api


class xmgl(models.Model):
    _name = 'xmgl.xmgl'
    xmmc = fields.Char(required=True, help='项目名称')
    xmbh = fields.Char(help='项目编号-审核完成后自动生成')
    cgdw = fields.Many2one('res.partner', required=True, help='采购单位-关联采购人表')
    cgdwlxr = fields.Many2one('res.partner', required=True, help='采购单位-关联采购人表')
    xmfzr = fields.Many2one('hr.employee',  required=True, help='项目负责人-关联员工表')
    xmxzr = fields.Many2one('hr.employee',  required=True, help='项目协助人-关联员工表')
    xmje = fields.Float(required=True, help='项目金额')
    date = fields.Date(help='开标时间')
    description = fields.Text()
