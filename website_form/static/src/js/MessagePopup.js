/** * @odoo-module **/
import publicWidget from "web.public.widget";
publicWidget.registry.formButton = publicWidget.Widget.extend({
  selector: "#wrapwrap",
  events: {
    "click #sub": "click",
  },
  click(e) {
    console.log("ohsohd",this.$el.find("#employeeForm")[0][0].value);
    console.log("ohsohd",this.$el.find("#employeeForm")[0][1].value);
    e.preventDefault();

    this._rpc({
      route: "/employee/form/submit",
      params: { emp_name: this.$el.find("#employeeForm")[0][0].value, emp_code: this.$el.find("#employeeForm")[0][1].value },
    }).then((data) => {
      console.log(data);
      const popup = this.$el.find("#popupmodal");
      popup.modal("show");
      // this.$el.find("#exampleModalLabel")[0].innerHTML = data.
      this.$el.find("#exampleModalLabel")[0].innerHTML = data.msg;
      this.$el.find("#modal-body")[0].innerHTML = data.body;
      console.log(data.stat);
      if (data.stat) {
        this.$el.find("#confirm")[0].innerHTML = "OKAY";
        this.$el.find("#confirm")[0].onclick = function () {
          popup.modal("hide");
        };
      } else {
        console.log($("#confirm"), this.$el);
        this.$el.find("#confirm")[0].innerHTML = "Login";
        this.$el.find("#confirm")[0].onclick = function () {
          window.location = "http://localhost:8069/web/login";
        };
      }
    });
  },
});
