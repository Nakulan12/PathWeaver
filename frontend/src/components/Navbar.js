import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/" style={{ textDecoration: "none", color: "white" }}>
        <h2>PathWeaver</h2>
      </Link>
      <div>
        <Link to="/">Home</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/features">Features</Link>
        <Link to="/about">About</Link>
      </div>
    </nav>
  );
}

export default Navbar;
