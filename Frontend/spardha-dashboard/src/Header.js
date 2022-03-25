import React from 'react';

const Header = () => {
return (
    <div className="top_header fixed-top w-100 d-flex flex-row justify-content-center align-items-center">
        <img src="/spardha_logo.png" alt="spardha-logo" className="top_header_logo"/>
        <div className="top_header_title">SPARDHA</div>
    </div>
  )
};

export default Header;