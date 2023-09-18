odoo.define("website_form.MessagePopupScreen", function (require) {
    "use strict";
  
    var publicWidget = require("web.public.widget");
  
    publicWidget.registry.EmployeeFormWidget = publicWidget.Widget.extend({
      selector: ".employeeForm",
  
      events: {
        submit: "_onFormSubmit",
      },
  
      _onFormSubmit: function (event) {
        event.preventDefault();
        var formData = new FormData(this.$el[0]);
        fetch("/path/to/backend/endpoint", {
          method: "POST",
          body: formData,
        })
          .then(function (response) {
            if (response.ok) {
              return response.text();
            } else {
              throw new Error("Form submission failed");
            }
          })
          .then(function (data) {
            alert("Form data submitted successfully!");
          })
          .catch(function (error) {
            console.error("Form submission failed:", error);
          });
      },
  
      start: function () {
        this.$el.on("submit", this._onFormSubmit.bind(this));
        return this._super.apply(this, arguments);
      },
    });
  
    return publicWidget.registry.EmployeeFormWidget;
  });
  