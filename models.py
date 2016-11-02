# -*- coding: utf-8 -*-
import datetime
from openerp import models, fields, api, tools

class mutabaah(models.Model):
     _name = 'mutabaah.mutabaah'

     name = fields.Date(required=True)
     ashar = fields.Boolean (string="Sholat Ashar Berjamaah", default= False)
     maghrib = fields.Boolean (string="Sholat Maghrib Berjamaah", default= False)
     isya = fields.Boolean (string="Sholat Isya Berjamaah", default= False)
     tahajjud = fields.Boolean (string="Sholat Tahajjud", default= False)
     dzikirpagi = fields.Boolean(string="Dzikir Pagi", default= False)
     dzikirsore = fields.Boolean(string="Dzikir Sore", default= False)
     infaq = fields.Boolean(string="Infaq/Shadaqah", default= False)
     kajianpagi = fields.Boolean(string="Kajian Kamis Pagi", default= False)
     bina = fields.Boolean(string="Bina Ruhiyah", default= False)
     MQ = fields.Boolean(string="Kajian MQ Kamis", default= False)
     dhuha = fields.Boolean (string="Sholat Dhuha", default= False)
     tilawah = fields.Char()
     shaum = fields.Boolean(string="Shaum Sunnah Senin-Kamis", default=False)
     itikaf = fields.Boolean (string="I'tikaf", default= False,required=True)
     zuhur = fields.Boolean(string="Sholat Zuhur Berjamaah", default=False)
     shubuh = fields.Boolean(string="Sholat Shubuh Berjamaah", default=False)

     graph = fields.Integer(string="")


     #@api.onchange('shubuh', 'ashar', 'isya', 'maghrib', 'tilawah')
     #def _onchange_graph(self):
          #countSubuh=0
         #z = self.browse()
         #for y in z :
              #if y.shubuh:
                   #countSubuh+= 1

              #= self.shubuh + self. ashar + self.isya + self.maghrib + self.tilawah