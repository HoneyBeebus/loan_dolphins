import React, {Component} from 'react';
import {NavLink, useHistory} from 'react-router-dom';
import {Navbar, Nav} from 'react-bootstrap';
import Cookies from 'js-cookie';

export class Navigation extends Component {
  logout = () => {
    Cookies.remove("username");
    Cookies.remove("password");
    Cookies.remove("uid");
    Cookies.remove("role");
    window.location.reload();
  }
  render(){
    return (
      <Navbar bg="dark" expand="lg">
        <img src="oportun_logo_circle.png" width="45" height="20"alt="Logo" />
        <Navbar.Toggle aria-controls="basic-navbar-nav"/>
        <Navbar.Collapse id="basic-navbar-nav">
        <Nav>
          <NavLink className="d-inline p-2 bg-dark text-white" to="/" onClick={this.logout}>Logout</NavLink>
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
