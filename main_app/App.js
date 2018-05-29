import React, { Component } from 'react';

import './App.css';
import { TransitionGroup, CSSTransition } from "react-transition-group";
import Home from './home'
import Crafts from './crafts'
import Weddings from './weddings'
import {
BrowserRouter as Router,
Route,
Link
} from 'react-router-dom';

class App extends Component {
  render() {
    return (
      <Router>
        <div className='App'>
        <nav>
          <Link to='/'>Home</Link>{'  '}
          <Link to='/crafts'>Crafts</Link>{'  '}
          <Link to='/weddings'>Weddings</Link>{'  '}
        </nav>




        <Route exact path='/' component={Home} />
        <Route path='/crafts' component={Crafts} />
        <Route path='/weddings' component={Weddings} />
      </div>
    </Router>
    );
  }
}

export default App;
