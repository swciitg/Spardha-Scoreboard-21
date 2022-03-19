import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import ResultA from './components/ResultA';
import ResultB from './components/ResultB';

const Results = (props) => {
  // const [date, setDate] = useState(new Date());
  const baseApiURL = 'https://swc.iitg.ac.in/spardhaApi/';
  const [hostelApiURL, setHostelApiURL] = useState(baseApiURL + 'hostels/');
  const [sportApiURL, setSportApiURL] = useState(baseApiURL + 'sports/');
  const [matchesApiURL, setMatchesApiURL] = useState(baseApiURL + 'matches/');
  const [hostels, setHostels] = useState([]);
  const [sports, setSports] = useState([]);
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedHostel, setSelectedHostel] = useState('');
  const [selectedSport, setSelectedSport] = useState('');
  // const [selectedDate, setSelectedDate] = useState('-1');

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
    console.log(selectedHostel);
    console.log(selectedSport);
    axios.get(
          matchesApiURL +
            '?team1=' +
            selectedHostel +
            '&team2=' +
            '' +
            '&sport=' +
            selectedSport
        )
        .then((response) => {
          console.log(response.data);
          let matches1 = response.data;
          axios.get(
            matchesApiURL +
              '?team1=' +
              '' +
              '&team2=' +
              selectedHostel +
              '&sport=' +
              selectedSport
          ).then((response)=>{
            matches1 = matches1.concat(response.data);
            console.log("all matches are here");
            console.log(matches1);
            setMatches(matches1);
            setLoading(false);
          })
          
        });
  }, [matchesApiURL, selectedHostel, selectedSport]);

  const handleHostelChange = (e) => {
    setSelectedHostel(e.target.value);
  };
  const handleSportChange = (e) => {
    setSelectedSport(e.target.value);
  };


  return (
    <div className='p-4'>
      <div className='results_header d-flex flex-row align-items-center'>
        <div className='results_text'>RESULTS</div>
      </div>
      <div className='d-flex flex-row align-items-center justify-content-between mb-2'>
        <div className='results_h2'>FILTERS</div>
        <div className='d-flex flex-row align-items-center'>
          {/* <div>
            <DatePicker
              className='results_dropdown_date'
              placeholderText='DATE'
              selected={date}
              onChange={(date) => setDate(date)}
            />
          </div> */}
          <select onChange={handleSportChange} className='results_dropdown w-2' name='' id=''>
            <option value=''>SPORT</option>
            {sports.map((sport, i) => (
              <option value={sport.id}>{sport.name}</option>
            ))}
          </select>
          <select onChange={handleHostelChange} className='results_dropdown w-2' name='' id=''>
            <option value=''>HOSTEL</option>
            {hostels.map((hostel, i) => (
              <option value={hostel.id}>{hostel.name}</option>
            ))}
          </select>
        </div>
      </div>
      {loading ? (
        <p>Loading...</p>
      ) : (matches.map((match, i) => (
        <ResultA
          Team1={match.team1}
          Team2={match.team2}
          Sport={match.sport}
          Stage={match.stage}
          Status={match.status}
          Date_time={match.datetime}
        />
      ))
        
      )}
      
      <ResultB Sport = 'Basketball' Stage = {1} Status = {false} Date_time = '2022-03-19T04:25:52Z'/>
    </div>
  );
};

export default Results;
