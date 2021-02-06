import React, { Component } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Link,
  Redirect,
  Route,
} from "react-router-dom";

export class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      key: null,
    };
  }

  async componentDidMount() {
    fetch("/api/template")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          key: data.key,
        });
      });
  }
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component="">
            <p>Template</p>
            <p>Your session_key is ${this.state.key} </p>
          </Route>
        </Switch>
      </Router>
    );
  }
}

export default Home;
