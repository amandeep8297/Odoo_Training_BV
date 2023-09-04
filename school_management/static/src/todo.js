/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

class TodoTask extends Component {
    static template = "school_management.clientaction";
    setup() {
        this.state = useState({
            tasks: [],
            newTask: ""
        });
        this.addTask = () => {
            const newTaskName = this.state.newTask.trim();
            if (newTaskName) {
                this.state.tasks.push({ name: newTaskName, done: false });
                this.state.newTask = "";
            }
        };

        this.deleteTask = (task) => {
            const taskIndex = this.state.tasks.indexOf(task);
            this.state.tasks.splice(taskIndex, 1);
        };

        this.toggleTaskDone = (task) => {
            task.done = !task.done;
        };

        this.getTaskDone = (task) => {
            return task.done;
        };

        this.editTask = (task) => {
            const updatedTaskName = prompt("Edit task:", task.name);
            if (updatedTaskName !== null) {
                task.name = updatedTaskName;
            }
        };
    }
}

registry.category("actions").add("school_management.task", TodoTask);