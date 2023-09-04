/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

class Calculator extends Component {
    static template = "fee.calc";

    setup() {
        this.state = useState({
            display: "0",
            currentNumber: "",
            previousNumber: "",
            operator: "",
        });

        this.onNumberClick = (event) => {
            const number = event.target.textContent;
            let currentNumber = this.state.currentNumber + number;
            if (currentNumber === "0") {
                currentNumber = number;
            }
            this.state.currentNumber = currentNumber;
            this.state.display = currentNumber;
        };

        this.onOperatorClick = (event) => {
            this.state.operator = event.target.textContent;
            this.state.previousNumber = this.state.currentNumber;
            this.state.currentNumber = "";
        };

        this.onEqualClick = () => {
            const { previousNumber, currentNumber, operator } = this.state;
            const num1 = parseFloat(previousNumber);
            const num2 = parseFloat(currentNumber);
            let result = 0;
            switch (operator) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    result = num1 / num2;
                    break;
                default:
                    break;
            }
            this.state.display = result.toString();
            this.state.currentNumber = result.toString();
            this.state.previousNumber = "";
            this.state.operator = "";
        };

        this.onClearClick = () => {
            this.state.display = "0";
            this.state.currentNumber = "";
            this.state.previousNumber = "";
            this.state.operator = "";
        };
    }
}

registry.category("actions").add("student.fee", Calculator);
