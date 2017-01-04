# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FundSource(models.Model):
    _name = 'xmgl.fundsource'
    name = fields.Char(required=True,string='资金来源名称')
    code = fields.Char(required=True,string='资金来源编码')

class ProjectProperty(models.Model):
    _name = 'xmgl.projectproperty'
    name = fields.Char(required=True,string='项目性质名称')
    code = fields.Char(required=True,string='项目性质编码')

class ProjectStatus(models.Model):
    _name = 'xmgl.projectstatus'
    name = fields.Char(required=True,string='项目状态名称')
    code = fields.Char(required=True,string='项目状态编码')

class ProjectType(models.Model):
    _name = 'xmgl.projecttype'
    name = fields.Char(required=True,string='项目类型名称')
    code = fields.Char(required=True,string='项目类型编码')

class PurchaseType(models.Model):
    _name = 'xmgl.purchasetype'
    name = fields.Char(required=True,string='采购名称')
    code = fields.Char(required=True,string='采购编码')

class PackageStatus(models.Model):
    _name = 'xmgl.packagestatus'
    name = fields.Char(required=True,string='包件状态名称')
    code = fields.Char(required=True,string='包件状态编码')


class Package(models.Model):
    _name = 'xmgl.package'
    name = fields.Char(string='包件名称')
    package_no = fields.Char(string='包件编号')
    package_status = fields.Many2one('xmgl.packagestatus', string='包件状态')
    package_amount = fields.Float(string='委托金额')
    package_assurance_amount = fields.Float(string='投标保证金金额')
    package_public_date = fields.Date(string='公告时间')
    package_open_date = fields.Date(string='开标时间')
    package_review_date = fields.Date(string='评标时间')
    
    #采购文件管理相关内容
    bidding_document_amount = fields.Float(string='可发售文件售价')
    bidding_document_start_date = fields.Date(string='开始发售时间')
    bidding_document_end_date = fields.Date(string='结束发售时间')
    bidding_document_state = fields.Selection([('open', '新建'),('waiting', '待审批'), ('approved', '审批通过')],
                              string='审批状态', default='open', readonly=True, help='提交审批',
                              copy=False)
    bidding_document_file  = fields.Char(string='采购文件附件')
    
    
    #中标通知书管理内容  
    win_date = fields.Date(string='签约时间')
    win_amount_ = fields.Float(string='中标金额')
    win_compnay = fields.Many2one('res.partner',string='中标单位')
    win_service_rate = fields.Float(string='中标服务费')
    win_document_file = fields.Char(string='中标通知书附件')
    
    description = fields.Text()
    
    @api.multi
    def act_bidding_document_submit(self):
        for record in self:
            record.bidding_document_state = 'waiting'
    @api.multi
    def act_bidding_document_reject(self):
        for record in self:
            record.bidding_document_state = 'open'
    @api.multi
    def act_bidding_document_approve(self):
        for record in self:
            record.bidding_document_state = 'approved'


class Project(models.Model): 
    _name = 'xmgl.project'
    _desciption  = '招标代理项目'
    _order = 'state desc';
    _inherits = {'xmgl.package': 'inner_package_id'}
    _inherit = 'mail.thread'
    name = fields.Char(required=True, string='项目名称')
    project_no = fields.Char(string='项目编号')   #project_no 应在审批结束之后自动生成
    project_type = fields.Many2one('xmgl.projecttype', string='项目类型')
    project_property = fields.Many2one('xmgl.projectproperty',  string='项目性质')
    purchase_type = fields.Many2one('xmgl.purchasetype',  string='采购类型')
    fund_source = fields.Many2one('xmgl.fundsource', string='资金来源')
    customer_id = fields.Many2one('res.partner', string="采购单位",help='采购单位-关联采购人表')
    contactor_id = fields.Many2one('res.partner', string="采购单位联系人", help='采购单位-关联采购人表')
    incharge_id = fields.Many2one('res.partner', default=lambda self: self.env.user.partner_id.id, string="项目负责人",help='项目负责人-关联员工表')
    assistant_id = fields.Many2one('res.partner',  string="项目协助人", help='项目协助人-关联员工表')
    amount = fields.Float(string="项目金额")
    prequalification_boolean = fields.Boolean(default=False,string='是否采用资格预审');
    
    #不拆包项目信息 ,包含默认的包件 
    inner_package_id = fields.Many2one('xmgl.package', '包件', ondelete='cascade')
    package_name = fields.Char(related='inner_package_id.name',string='包件名称',default=name)   #包件名称和项目名称相同
    package_no = fields.Char(related='inner_package_id.package_no',string='包件编号',default=project_no)
    
    package_status = fields.Many2one(related='inner_package_id.package_status', string='包件状态')
    package_amount = fields.Float(related='inner_package_id.package_amount',string='委托金额')
    package_assurance_amount = fields.Float(related='inner_package_id.package_assurance_amount',string='投标保证金金额')
    package_public_date = fields.Date(related='inner_package_id.package_public_date',string='公告时间')
    package_open_date = fields.Date(related='inner_package_id.package_open_date',string='开标时间')
    package_review_date = fields.Date(related='inner_package_id.package_review_date',string='评标时间')
    
    #采购文件管理相关内容
    bidding_document_amount = fields.Float(related='inner_package_id.bidding_document_amount',string='可发售文件售价')
    bidding_document_start_date = fields.Date(related='inner_package_id.bidding_document_start_date',string='开始发售时间')
    bidding_document_end_date = fields.Date(related='inner_package_id.bidding_document_end_date',string='结束发售时间')
    bidding_document_state = fields.Selection(related='inner_package_id.bidding_document_state',
                              string='审批状态', default='open', readonly=True, help='提交审批',
                              copy=False)
    bidding_document_file  = fields.Char(related='inner_package_id.bidding_document_file',string='采购文件附件')
    
    
    #中标通知书管理内容  
    win_date = fields.Date(related='inner_package_id.win_date',string='签约时间')
    win_amount_ = fields.Float(related='inner_package_id.win_amount_',string='中标金额')
    win_compnay = fields.Many2one(related='inner_package_id.win_compnay',string='中标单位')
    win_service_rate = fields.Float(related='inner_package_id.win_service_rate',string='中标服务费')
    win_document_file = fields.Char(related='inner_package_id.win_document_file',string='中标通知书附件')


#   拆包项目信息
    unpack_boolean = fields.Boolean(default=False, string='是否拆包');
    packages_list = fields.One2many('xmgl.package','name', string='项目包件')
    
    #项目审批状态  
    state = fields.Selection([('open', '初始登记'),('waiting', '待审批'), ('approved', '审批通过')],
                              string='审批状态', default='open', readonly=True, help='提交项目审批',
                              copy=False)
    description = fields.Text()
    
    @api.multi
    def act_project_submit(self):
        for record in self:
            record.state = 'waiting'

    @api.multi
    def act_project_approve(self):
        for record in self:
            record.state = 'approved'
    
    @api.multi
    def act_project_reject(self):
        for record in self:
            record.state = 'open'


