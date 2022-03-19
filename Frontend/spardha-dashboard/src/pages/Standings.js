import React, { useState, useEffect } from 'react';
import axios from 'axios';
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
  },];

/*   const sport = [
    {
      name: 'Cricket',
    },
    {
      name: 'Basketball',
    },
    {
      name: 'Volleyball',
    },
    {
      name: 'Badminton',
    },
    {
      name: 'Football',
    },
    {
      name: 'Hockey',
    },
    {
      name: 'Chess',
    },
    {
      name: 'Squash',
    },
  ]; */
  

const Standings = (props) => {
  const baseApiURL = 'http://localhost:8000/spardhaApi/';
  const [hostelApiURL, setHostelApiURL] = useState(baseApiURL+'hostels/');
  const [sportApiURL, setSportApiURL]  = useState(baseApiURL+'sports/');
  const [standingsApiURL, setStandingsApiURL] = useState(baseApiURL+'standings/');
  const [hostels, setHostels] = useState([]);
  const [sports, setSports] = useState([]);
  const [standings, setStandings] = useState([]);
  const [selectedSport, setSelectedSport] = useState('');
  const [selectedStandings, setSelectedStandings] = useState([]);

  useEffect(() => {
    axios.get(hostelApiURL).then((response) =>{
      console.log(response.data);
      setHostels(response.data);
    })
  }, [hostelApiURL]);
  useEffect(() => {
    axios.get(sportApiURL).then((response) =>{
      console.log(response.data);
      setSports(response.data);
    })
  }, [sportApiURL]);
  useEffect(() => {
    axios.get(standingsApiURL).then((response) =>{
      console.log(response.data);
      setStandings(response.data);
    })
  }, [standingsApiURL]);

return (
    <div className="p-4">
        <div className="standings_header d-flex flex-row align-items-center">
            <div className="standings_text">STANDINGS</div>
            <select className="standings_dropdown" name='' id=''>
                <option className="standings_dropdown_text">Overall</option>
                {sports.map((sport, i) => (
                  <option value={i} className="standings_dropdown_text">{sport.name}</option>
                ))}
            </select>
           {/*  <div className="standings_dropdown_text">Overall</div>
            <FontAwesomeIcon icon={faCaretDown} className="standings_dropdown_icon" size="l"/> */}
        </div>
        <div className="w-100 black_line" />
        <div className="standings_h2">
            TABULAR FORM
        </div>
        {standings.map((hostel, i) =>(
            <StandingsItem Name={hostel.name} Points={hostel.points} Index={i}/>
        ))}
    </div>
  )
};

export default Standings;