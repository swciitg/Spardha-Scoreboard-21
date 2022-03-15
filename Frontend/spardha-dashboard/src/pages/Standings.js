import React from 'react';
import StandingsItem from './components/StandingsItem';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCaretDown } from '@fortawesome/free-solid-svg-icons';
const data = [{
    name: "Brahmaputra",
    points: 800,
  },{
    name: "Lohit",
    points: 700,
  },{
    name: "Siang",
    points: 700,
  },{
    name: "Manas",
    points: 600,
  },{
    name: "Kapili",
    points: 500,
  },{
    name: "Disang",
    points: 400,
  },]

const Standings = (props) => {
return (
    <div className="p-4">
        <div className="standings_header d-flex flex-row align-items-center">
            <div className="standings_text">STANDINGS</div>
            <div className="standings_dropdown_text">Overall</div>
            <FontAwesomeIcon icon={faCaretDown} className="standings_dropdown_icon" size="l"/>
        </div>
        <div className="w-100 black_line" />
        <div className="standings_h2">
            TABULAR FORM
        </div>
        {data.map((hostel, i) =>(
            <StandingsItem Name={hostel.name} Points={hostel.points} Index={i}/>
        ))}
    </div>
  )
};

export default Standings;