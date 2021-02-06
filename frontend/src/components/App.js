import React, { Component } from "react";
import { render } from "react-dom";
import Home from "./Home";

export class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      key: "value",
    };
  }

  render() {
    return (
      <div>
        <Home />
      </div>
    );
  }
}
const appDiv = document.getElementById("app");
render(<App name="Brett" />, appDiv);
