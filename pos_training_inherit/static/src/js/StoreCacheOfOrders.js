odoo.define("pos_inherit.paymentScreenExtension", function (require) {
  "use strict";
  const { Order } = require("point_of_sale.models");
  const Registries = require("point_of_sale.Registries");
  const storeCache = (Order) =>
    class storeCache extends Order {
      constructor() {
        super(...arguments);
      
      }
      init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.set_details(json.details);
        // this.set_details(json.add_details);
      }

      export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.details = this.details;
        // json.mobile = this.mobile;
        return json;
      }
      
      
      set_details(num) {
        this.details = num;
      }
      get_details() {
        return this.details;
      }

      // set_add_details(phone) {
      //   this.mobile = phone;
      // }
      // get_add_details() {
      //   return this.mobile;
      // }
      export_for_printing() {
        const result = super.export_for_printing(...arguments);
        if (this.get_details()) {
          result.details = this.get_details();
        }
        return result;
      }
    };
  Registries.Model.extend(Order, storeCache);
  return storeCache;
});
