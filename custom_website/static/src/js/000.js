/** @odoo-module **/
import publicWidget from "web.public.widget";
import core from "web.core";

var Qweb = core.qweb;

publicWidget.registry.Employee = publicWidget.Widget.extend({
  selector: ".employee_snippet_id",
  events: {},
  start() {
    this._rpc({
      route: "/employee/",
      params: {},
    }).then((data) => {
      this.$target.replaceWith(
        Qweb.render("custom_website.dynamic_snippet_template", { data: data })
      );
    });
  },
});
export default publicWidget.registry.Employee;
