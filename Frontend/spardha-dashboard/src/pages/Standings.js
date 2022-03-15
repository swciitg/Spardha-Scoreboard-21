import React from 'react';
import StandingsItem from './components/StandingsItem';

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
      <div className="standings_h2">
          TABULAR FORM
      </div>
      {data.map((hostel, i) =>(
            <StandingsItem Name={hostel.name} Points={hostel.points}/>
      ))}
    </div>
  )
};

export default Standings;