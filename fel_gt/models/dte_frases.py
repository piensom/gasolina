# -*- coding: utf-8 -*-

from odoo import fields, models


class DteFrases(models.Model):
    _name = 'dte.frases'
    _description = 'Frases DTE'

    name = fields.Char(string='Descripcion')
    default = fields.Boolean(string='Por Defecto')
    tipo_frase = fields.Char(string='Codigo Tipo Frase')
    nombre_frase = fields.Char(string='Nombre de Frase')
    descripcion_frase = fields.Text(string='Descripcion Frase')
    codigo_escenario = fields.Char(string='Codigo Escenario')
    escenario = fields.Char(string='Descripcion Escenario')
    texto_colocar = fields.Char(string='Texto A Colocar')
DteFrases()
