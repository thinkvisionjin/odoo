# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model): 
    _name = 'xmgl.project'
    _desciption  = '招标代理项目'
    _order = 'state desc';
    name = fields.Char(required=True, string='项目名称',help='项目名称')
    project_no = fields.Char(string='项目编号',help='项目编号-审核完成后自动生成')   #project_no 应在审批结束之后自动生成
    customer_id = fields.Many2one('res.partner', string="采购单位",required=True, help='采购单位-关联采购人表')
    contactor_id = fields.Many2one('res.partner', string="采购单位联系人",required=True, help='采购单位-关联采购人表')
    incharge_id = fields.Many2one('res.partner',  string="项目负责人",required=True, help='项目负责人-关联员工表')
    assistant_id = fields.Many2one('res.partner',  string="项目协助人",required=True, help='项目协助人-关联员工表')
    amount = fields.Float(required=True, string="项目金额",help='项目金额')
    sale_date =  fields.Date(string="招标文件发售时间",help='招标文件发售时间')
    open_date = fields.Date(string="开标时间",help='开标时间')
    state = fields.Selection([('open', '初始登记'),('waiting', '待审批'), ('approved', '审批通过')],
                              string='审批状态', default='open', readonly=True, help='提交项目审批',
                              copy=False)
    description = fields.Text()

    
    @api.multi
    def act_approve_submit(self):
        for record in self:
            record.state = 'waiting'

    @api.multi
    def act_approve_project(self):
        for record in self:
            record.state = 'approved'
    
    @api.multi
    def act_reject_project(self):
        for record in self:
            record.state = 'open'

class Package(models.Model):
    _name = 'xmgl.package'
    name = fields.Char(required=True, help='包件名称')
    package_no = fields.Char(help='包件编号')
    
class ProjectType(models.Model):
    _name = 'xmgl.projecttype'
    name = fields.Char(required=True,help='项目类型名称')
    code = fields.Char(required=True,help='项目类型编码')

