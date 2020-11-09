import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';
import {Navbar, Nav} from 'react-bootstrap';

export class Navigation extends Component {
  render(){
    return (
      <Navbar bg="dark" expand="lg">
        <Navbar.Toggle aria-controls="basic-navbar-nav"/>
        <Navbar.Collapse id="basic-navbar-nav">
        <Nav>

          <NavLink className="d-inline p-2 bg-dark text-white" to="/">Login</NavLink>
          <NavLink className="d-inline p-2 bg-dark text-white" to="/dashboard">Dashboard</NavLink>
          <NavLink className="d-inline p-2 bg-dark text-white" to="/outcome">Outcomes</NavLink>
          <NavLink className="d-inline p-2 bg-dark text-white" to="/matrix">Matricies</NavLink>
          <NavLink className="d-inline p-2 bg-dark text-white" to="/risk">Risk Analysis</NavLink>
          
        </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}
