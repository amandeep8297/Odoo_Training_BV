odoo.define("pos_training.inheritpayment", function (require) {
  "use strict";

  
  const PaymentScreen = require("point_of_sale.PaymentScreen");
  const Registries = require("point_of_sale.Registries");

  const ValidateCustomer = (PaymentScreen) =>
    class extends PaymentScreen {
      setup() {
        super.setup();
      }
      async onClick() {
        console.log("ad");
      }
    };
  ValidateCustomer.template = "pos_training_inherit.ValidateCustomer";
  Registries.Component.extend(PaymentScreen, ValidateCustomer);
  return ValidateCustomer;
});
