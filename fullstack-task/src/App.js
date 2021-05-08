import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";
import { Provider } from "react-redux";
import Homepage from "./components/Homepage";

import store from "./store";

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Route exact path="/" component={Homepage}></Route>
      </Router>
    </Provider>
  );
}

export default App;
