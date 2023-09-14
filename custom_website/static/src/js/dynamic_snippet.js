/** @odoo-module **/

import publicWidget from "web.public.widget";

publicWidget.registry.Employee = publicWidget.Widget.extend({
  selector: ".basic_snippet3_select",
  start() {
    // console.log("******************************************");

    let empData = this.el.querySelector("#basic_snippet3_id");

    if (empData) {
      this._rpc({
        route: "/employee/",
        params: {},
      }).then((data) => {
        let html = ``;
        data.forEach((empData) => {
          html += `<div class="col-lg-3 mb-5">
                <div class="d-flex align-items-center">
                    <div class="img-container mr-3 rounded">
                        <img class="country-image rounded" src="data:image/png;base64,${
                          empData.emp_img
                        }"/>
                    </div>
                    <div>
                        <h5 class="mb-0">${
                          empData.state_id ? empData.state_id[1] : ""
                        }</h5>
                        <div>${
                          empData.country_id ? empData.country_id[1] : ""
                        }</div>
                    </div>
                </div>
            </div>`;
        });
        empData.innerHTML = html;
      });
    }
  },
});
export default publicWidget.registry.Employee;
