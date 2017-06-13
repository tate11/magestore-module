# -*- coding utf-8 -*-
from odoo import fields, models
import requests
import json


class website(models.Model):
    _inherit = 'website'

    recaptcha_site_key = fields.Char(string='reCAPTCHA Site Key')
    recaptcha_private_key = fields.Char(string='reCAPTCHA Private Key')

    def is_captcha_valid(self,response):
        res_con={}
        for website in self:
            get_res = {'secret': website.recaptcha_private_key, 'response':response }
            try:
                response = requests.post('https://www.google.com/recaptcha/api/siteverify', params=get_res)
            except Exception, e:
                raise UserWarning(e.message)
            print response.content
            res_con = json.loads(response.content)

        return res_con