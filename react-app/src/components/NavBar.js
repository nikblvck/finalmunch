
import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './Nav.css';

const NavBar = () => {
  return (
		<nav>
			<div className="nav-wrapper">
				<ul className="nav-list">
					<li>
						<NavLink
							className="nav-links"
							to="/"
							exact={true}
							activeClassName="active"
						>
							Home
						</NavLink>
					</li>
					<li>
						<NavLink
							className="nav-links"
							to="/login"
							exact={true}
							activeClassName="active"
						>
							Login
						</NavLink>
					</li>
					<li>
						<NavLink
							className="nav-links"
							to="/sign-up"
							exact={true}
							activeClassName="active"
						>
							Sign Up
						</NavLink>
					</li>
					<li>
						<NavLink
							className="nav-links"
							to="/users"
							exact={true}
							activeClassName="active"
						>
							Users
						</NavLink>
					</li>
					<li className="nav-links">
						<LogoutButton />
					</li>
				</ul>
			</div>
		</nav>
	);
}

export default NavBar;
