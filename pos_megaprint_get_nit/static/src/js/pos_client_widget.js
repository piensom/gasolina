odoo.define('pos_client_widget.ClientListScreenWidgetInh', function (require) {
    'use strict';

    const ClientDetailsEdit = require('point_of_sale.ClientDetailsEdit');
    const { _t } = require('web.core');
    const { getDataURLFromFile } = require('web.utils');
    const PosComponent = require('point_of_sale.PosComponent');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const rpc = require('web.rpc');

    const ClientDetailsEditInh = (ClientDetailsEdit) =>
        class extends ClientDetailsEdit {
            constructor() {
                super(...arguments);
                useListener('get_nit', this.getNIT);
            }

            getNIT() {
                var self = this;
                var vat;
                if ('id' in self.props.partner && self.props.partner.vat != undefined){
                    vat = self.props.partner.vat;
                }
                else if('vat' in self.changes){
                    vat = self.changes.vat;
                }
                if(vat != undefined){
                    rpc.query({
                        model: 'res.partner',
                        method: 'get_nit_name_from_vat',
                        args: [false, vat],
                    })
                    .then(function(result_dict){
                        if (result_dict && 'name' in result_dict){
                            self.changes.name = result_dict.name
                            self.props.partner.name = result_dict.name
                            self.render();
                        }
                        else{
                            return self.showPopup('ErrorPopup', {
                              title: _t(result_dict.error),
                            });
                        }
                    });
                }
                else{
                    return self.showPopup('ErrorPopup', {
                      title: _t('Please Enter VAT Number To Fetch Name'),
                    });
                }
            }
        };

    Registries.Component.extend(ClientDetailsEdit, ClientDetailsEditInh);

    return ClientDetailsEditInh;
});
