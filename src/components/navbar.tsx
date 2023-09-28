import React from 'react';
import logo from "../assets/logo.png";
import '../css/navbar.css';

interface NavbarProps {
  title: string;
  links: Array<{ name: string, url: string }>;
}

const Navbar: React.FC<NavbarProps> = ({ title, links }) => {
  return (
    <nav className='nav'>
      <div>
        <div>
          <img src={logo} className='logo'></img>
        </div>
        <div>
          <ul style={{ listStyle: 'none', display: 'flex', gap: '1rem', margin: 0, padding: 0 }}>
            {links.map((link, index) => (
              <li key={index}>
                <a href={link.url} style={{ color: '#fff' }}>
                  {link.name}
                </a>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
