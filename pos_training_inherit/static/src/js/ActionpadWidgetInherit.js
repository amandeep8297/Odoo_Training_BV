// odoo.define("pos_training_inherited.actionpad_extension", function (require) {
//   "use strict";

//   const ProductScreen = require("point_of_sale.ProductScreen");
//   const Registries = require("point_of_sale.Registries");

//   var core = require("web.core");
//   var _t = core._t;

//   const ActionpadWidgetInherit = (ProductScreen) =>
//     class extends ProductScreen {
//       setup() {
//         super.setup();

//         // _onPaymentError() {
//         //     this.displayNotification({
//         //         type: 'danger',
//         //         title: _t('Error'),
//         //         message: _t('Please select a customer before proceeding with payment.'),
//         //     });
//         // }}
//       }

//     };

//   // ActionpadWidgetInherit.template = "ActionpadWidgetInherit";
//   Registries.Component.add(ProductScreen, ActionpadWidgetInherit);

//   return ActionpadWidgetInherit;
// });
