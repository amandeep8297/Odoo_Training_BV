odoo.define("treeinherit", function (require) {
  "use strict";
  const TicketScreen = require("point_of_sale.TicketScreen");
  const Registries = require("point_of_sale.Registries");
  const { useState } = owl;

  const ShowPhoneInTree = (TicketScreen) =>
    class extends TicketScreen {
      setup() {
        super.setup();
        // const customerPhone = this.env.pos.get_order().get_add_details();
        console.log(this.env.pos.get_order().partner);
        this.customerPhone = useState({ phone: "qwertyui" });
      }
    };
  ShowPhoneInTree.template = "ShowPhoneInTree";
  Registries.Component.extend(TicketScreen, ShowPhoneInTree);
  return ShowPhoneInTree;
});
