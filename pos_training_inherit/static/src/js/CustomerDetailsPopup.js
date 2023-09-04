odoo.define("pos_training_inherit.CustomerDetailsPopup", function (require) {
  "use strict";

  const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
  const { useState, useRef } = owl;
  const Registries = require("point_of_sale.Registries");
  const { _lt } = require("@web/core/l10n/translation");
  const { Gui } = require("point_of_sale.Gui");

  class CustomerDetailsPopup extends AbstractAwaitablePopup {
    /**
     * @param {Object} props
     * @param {string} props.startingValue
     */
    setup() {
      super.setup();

      this.state = useState({ inputValue: this.props.startingValue });
      this.details = useRef("details");

      this.add_details = useState({
        value: "",
        error: "",
      });
    }

    getPayload() {
      return this.state.inputValue;
    }

    async confirm() {
      console.log(this.partner);
      const mob = this.details.el.value;

      const loadedData = await this.env.services.rpc({
        model: "res.partner",
        method: "search_count",
        args: [[["details", "=", this.state.inputValue]]],
      });

      console.log(loadedData);
      if (mob == "") {
        Gui.showPopup("ErrorPopup", {
          confirmText: _lt("Ok"),
          title: _lt("Error"),
          body: "Enter details",
        });
      } else {
        return super.confirm();
      }
    }
  }
  CustomerDetailsPopup.template = "pos_training_inherit.CustomerDetailsPopup";
  CustomerDetailsPopup.defaultProps = {
    cancelText: _lt("Discard"),
    title: _lt("Customer details"),
    save: _lt("Save"),
  };
  Registries.Component.add(CustomerDetailsPopup);
  return CustomerDetailsPopup;
});
