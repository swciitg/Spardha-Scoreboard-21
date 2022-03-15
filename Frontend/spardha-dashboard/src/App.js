import React from 'react';
import './App.css';
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Standings from './pages/Standings';
import Results from './pages/Results';
import Schedule from './pages/Schedule';
import Navigation from './Navigation';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Navigation />
        <Switch>
          <Route path="/standings" component={Standings} />
          <Route path="/results" component={Results} />
          <Route path="/schedule" component={Schedule} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;