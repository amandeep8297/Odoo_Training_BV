odoo.define("pos_training.inherit", function (require) {
  "use strict";
  const ProductScreen = require("point_of_sale.ProductScreen");
  const Registries = require("point_of_sale.Registries");
  const { Gui } = require("point_of_sale.Gui");
  const { _lt } = require("@web/core/l10n/translation");

  const CustomerDetailsPopupComponent = (ProductScreen) =>
    class extends ProductScreen {
      setup() {
        super.setup();
      }
      async onClick() {
        const selectOrderline = this.env.pos.get_order();
        const { confirmed, payload: details } = await this.showPopup(
          "CustomerDetailsPopup",
          {
            startingValue: selectOrderline.get_details(),
            title: this.env._t("Any additional details"),
          }
        );
        if (confirmed) {
          selectOrderline.set_details(details);
        }
      }
      async _onClickPay() {
        console.log(this.env.pos.get_order().partner);
        if (this.env.pos.get_order().partner == null) {
          Gui.showPopup("ErrorPopup", {
            title: _lt("Error"),
            body: _lt(`Customer selection required!`),
          });
        } else {
          super._onClickPay();
        }
      }
    };
  CustomerDetailsPopupComponent.template =
    "pos_training_inherit.CustomerDetailsPopupComponent";
  Registries.Component.extend(ProductScreen, CustomerDetailsPopupComponent);
  return CustomerDetailsPopupComponent;
});
