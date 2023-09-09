odoo.define("deleteButton", function (require) {
  "use strict";

  const Orderline = require("point_of_sale.models").Orderline;
  const Registries = require("point_of_sale.Registries");

  class OrderlineDeleteButton extends Orderline {
    setup() {
      super.setup();
    }
   removeOrderline(){
      console.log("+++++++++++++++++++++++++++++++++++");
    }
  }

  OrderlineDeleteButton.template = "pos_training_inherit.Orderline";
  Registries.Component.add(OrderlineDeleteButton);
  return OrderlineDeleteButton;
});
