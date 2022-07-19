import zeep
from odoo import models
import requests
import re
from odoo.exceptions import UserError, ValidationError
from lxml import etree

class ResPartner(models.Model):

    _inherit = 'res.partner'

    def get_nit_name_from_vat(self, vat):
        

        request_url = "apiv2"
        request_path = ""
        request_url_firma = ""
        if self.env.company.pruebas_fel:
            request_url = "dev2.api"
            request_path = ""
            request_url_firma = "dev."
          
        if vat and vat != 'CF':
            nit = vat.replace("-", "")

            headers = { "Content-Type": "application/xml" }
            data = '<?xml version="1.0" encoding="UTF-8"?><SolicitaTokenRequest><usuario>{}</usuario><apikey>{}</apikey></SolicitaTokenRequest>'.format(self.env.company.usuario_fel, self.env.company.clave_fel)
            r = requests.post('https://'+request_url+'.ifacere-fel.com/'+request_path+'api/solicitarToken', data=data.encode('utf-8'), headers=headers)
            resultadoXML = etree.XML(bytes(r.text, encoding='utf-8'))
            if len(resultadoXML.xpath("//token")) > 0:
                token = resultadoXML.xpath("//token")[0].text
            else:
                raise UserError('Credenciales Inválidas')
            direcciones = []    
            body = '<?xml version="1.0" encoding="UTF-8"?><RetornaDatosClienteRequest><nit>{}</nit></RetornaDatosClienteRequest>'.format(nit)
            headers = { "Content-Type": "application/xml", "authorization": "Bearer "+token }
            r = requests.post('https://'+request_url+'.ifacere-fel.com/'+request_path+'api/retornarDatosCliente', data=body.encode('utf-8'), headers=headers)
            resultadoXML = etree.XML(bytes(r.text, encoding='utf-8'))


            if len(resultadoXML.xpath("//nombre")) > 0:
                return {'name': resultadoXML.xpath("//nombre")[0].text}
            else:
                return {'error': 'Datos no encontrados. Verifique si el NIT es correcto.'}
        return {'error': 'Datos no encontrados. Verifique si el NIT es correcto.'}
