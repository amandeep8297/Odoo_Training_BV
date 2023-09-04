odoo.define("paymentScreenInherit", function (require) {
    "use strict";
    const PaymentScreen = require("point_of_sale.PaymentScreen");
    const Registries = require("point_of_sale.Registries");
    const { Gui } = require("point_of_sale.Gui");
    const { _lt } = require("@web/core/l10n/translation");
  
    const ValidatePaymentScreen = (PaymentScreen) =>
      class extends PaymentScreen {
        setup() {
          super.setup();
        }
        async _isPartnerValid() {
          if (this.env.pos.get_order().partner == null) {
            Gui.showPopup("ErrorPopup", {
              title: _lt("Error"),
              body: _lt(`Customer selection required!`),
            });
          }
        }
     
      };
    Registries.Component.extend(PaymentScreen, ValidatePaymentScreen);
    return ValidatePaymentScreen;
  });
  