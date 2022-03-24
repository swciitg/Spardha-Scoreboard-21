import StandingsItem from './components/StandingsItem';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'react-datepicker/dist/react-datepicker.css';

const Standings = (props) => {
  const baseApiURL = 'https://swc.iitg.ac.in/spardhaApi/';
  const [hostelApiURL, setHostelApiURL] = useState(baseApiURL + 'hostels/');
  const [standingsApiURL, setSportApiURL] = useState(baseApiURL + 'standings/');
  const [overallStandingsApiURL, setOverallStandingsApiURL] = useState(
    baseApiURL + 'standingsOverall/'
  );
  const [sportApiURL, setSportsApiURL] = useState(baseApiURL + 'sports/');
  const [hostels, setHostels] = useState([]);
  const [sports, setSports] = useState([]);
  const [standings, setStandings] = useState([]);
  const [overallStandings, setOverallStandings] = useState([]);
  const [overallStandingsGirls, setOverallStandingsGirls] = useState([]);
  const [selectedSport, setSelectedSport] = useState('-1');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    axios.get(hostelApiURL).then((response) => {
      console.log(response.data);
      setHostels(response.data);
      setLoading(false);
    });
  }, [hostelApiURL]);

  useEffect(() => {
    setLoading(true);
    axios.get(sportApiURL).then((response) => {
      console.log(response.data);
      setSports(response.data);
      setLoading(false);
    });
  }, [sportApiURL]);
  useEffect(() => {
    console.log('triggered');
    setLoading(true);
    console.log(selectedSport);
    if (selectedSport !== '-1' && selectedSport !== '-2') {
      axios
        .get(standingsApiURL + '?sport=' + selectedSport)
        .then((response) => {
          console.log(response.data);
          setStandings(response.data);
          setLoading(false);
        });
    }
    setLoading(false);
  }, [standingsApiURL, selectedSport]);
  useEffect(() => {
    setLoading(true);
    axios.get(overallStandingsApiURL).then((response) => {
      console.log(response.data.boys);
      setOverallStandings(response.data.boys);
      setOverallStandingsGirls(response.data.girls);
      setLoading(false);
    });
  }, [overallStandingsApiURL]);

  const sportHandler = (event) => {
    console.log(event.target.value);
    setSelectedSport(event.target.value);
  };

  return (
    <div className='p-4'>
      <div className='standings_header d-flex flex-row align-items-center'>
        <div className='standings_text'>STANDINGS</div>
        <select
          onChange={sportHandler}
          className='standings_dropdown'
          name=''
          id=''
        >
          <option value={-1} className='standings_dropdown_text'>
            Overall - Boys
          </option>
          <option value={-2} className='standings_dropdown_text'>
            Overall - Girls
          </option>
          {sports &&
            sports.map((sport, i) => (
              <option value={sport.id} className='standings_dropdown_text'>
                {sport.name}
              </option>
            ))}
        </select>
        {/*  <div className="standings_dropdown_text">Overall</div>
            <FontAwesomeIcon icon={faCaretDown} className="standings_dropdown_icon" size="l"/> */}
      </div>
      <div className='w-100 black_line' />
      <div className='standings_h2'>TABULAR FORM</div>
      {loading ? (
        <p>Loading...</p>
      ) : selectedSport === '-1' ? (
        overallStandings.map((hostel, i) => (
          <StandingsItem
            Name={hostel.name}
            Points={hostel.overall_points}
            Index={i}
            Result={true}
          />
        ))
      ) : selectedSport === '-2' ? (
        overallStandingsGirls.map((hostel, i) => (
          <StandingsItem
            Name={hostel.name}
            Points={hostel.overall_points}
            Index={i}
            Result={true}
          />
        ))
      ) : (
        standings.map((hostel, i) => (
          <StandingsItem
            Name={hostel.hostel}
            Points={hostel.points}
            Index={i}
            Result={true}
          />
        ))
      )}

      {/* {data.map((hostel, i) =>(
            <StandingsItem Name={hostel.name} Points={hostel.points} Index={i}/>
        ))} */}
    </div>
  );
};

export default Standings;
