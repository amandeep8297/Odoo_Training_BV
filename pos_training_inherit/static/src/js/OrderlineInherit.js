odoo.define("deleteButton", function (require) {
    "use strict";
  
    const Orderline = require("point_of_sale.Orderline");
    const { useState, useRef } = owl;
    const Registries = require("point_of_sale.Registries");
    const { _lt } = require("@web/core/l10n/translation");
  
    class OrderlineDeleteButton extends Orderline {
      setup() {
        super.setup();
        console.log("clickedddddd");
        
      }
 
    }
    OrderlineDeleteButton.template = "pos_training_inherit.Orderline";
    Registries.Component.add(OrderlineDeleteButton);
    return OrderlineDeleteButton;
  });
  