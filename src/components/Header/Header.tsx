import * as React from 'react'

import './Header.sass'
import logo from '../../assets/logo.png'


export default function Header() {
  return (
    <div className='header-container'>
      <img className='logo' src={logo} alt='pywebview' />
      <h2>pywebview</h2>
      <button onClick={() => {
        let res = (window as any).pywebview.api.get_all_ports().then((data: string[])=>{
          console.log(data)
          alert(data)
        })
      }}> Premi </button>
      <div className='links'>
        <a href='https://pywebview.flowrl.com/' target='_blank' rel='noreferrer'>Documentation</a>
      </div>
    </div>
  );
};
