import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { NavList } from './asset/AppData';
import './asset/style/App.css';

function App(params) {
  return (
    <div className="app">

      {/* Navigation Bar */}
      <div className='app-nav'>
        {
          NavList.map((nav, index) => {
            return (
              <a
                key={index}
                href={nav.path}
                className='app-nav-item'
              >
                {nav.name}
              </a>
            )
          })
        }
      </div>

      <div className='app-main'>
        <BrowserRouter>
          <Routes>
            {
              NavList.map((nav, index) => {
                return (
                  <Route
                    key={index}
                    path={nav.path}
                    element={<nav.component />}
                    className='app-main-item'
                  />
                )
              })
            }
          </Routes>
        </BrowserRouter>
      </div>

      {/* Footer - Added globally */}
      <div className="app-footer">
        <div className="footer-text">
          Developed by <a href="/team" target="_blank" rel="noopener noreferrer">@OurTeam</a>
        </div>
        <div className="copyright">
          &copy; {new Date().getFullYear()} Apache License, Version 2.0.
        </div>
      </div>
    </div>
  )
}

export default App;
