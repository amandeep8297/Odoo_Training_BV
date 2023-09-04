odoo.define("partnerInherit", function (require) {
  "use strict";
  const PartnerDetailsEdit = require("point_of_sale.PartnerDetailsEdit");
  const Registries = require("point_of_sale.Registries");

  const InheritPartnerDetailsEdit = (PartnerDetailsEdit) =>
    class extends PartnerDetailsEdit {
      setup() {
        super.setup();
        console.log(this.props.partner.mobile_no);
        this.changes.mobile_no = this.props.partner.mobile_no || "";
      }
    };
  Registries.Component.extend(PartnerDetailsEdit, InheritPartnerDetailsEdit);
  return InheritPartnerDetailsEdit;
});
