/** @odoo-module **/

import { Component, useState, useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";

class TodoTask extends Component {
  btn = useRef("btn");
  btnn = useRef("btn");
  setup() {
    this.count = useState({ value: 1 });
    this.down = useState({ value: 100 });

  }

  increment() {
   

    this.count.value++;
  }
  decrement(){
    this.down.value--;
  }
}

TodoTask.components = {};
TodoTask.template = "school_management.clientaction";

registry.category("actions").add("school_management.task", TodoTask);
