import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import ResultA from './components/ResultA';

const Results = (props) => {
  const [date, setDate] = useState(new Date());
  const baseApiURL = 'https://swc.iitg.ac.in/spardhaApi/';
  const [hostelApiURL, setHostelApiURL] = useState(baseApiURL + 'hostels/');
  const [sportApiURL, setSportApiURL] = useState(baseApiURL + 'sports/');
  const [matchesApiURL, setMatchesApiURL] = useState(baseApiURL + 'matches/');
  const [hostels, setHostels] = useState([]);
  const [sports, setSports] = useState([]);
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedHostel, setSelectedHostel] = useState('-1');
  const [selectedSport, setSelectedSport] = useState('-1');
  const [selectedDate, setSelectedDate] = useState('-1');

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
    console.log(selectedHostel1);
    console.log(selectedHostel2);
    console.log(selectedSport);
    if (
      selectedHostel1 !== '-1' &&
      selectedHostel2 !== '-1' &&
      selectedSport !== '-1'
    ) {
      axios
        .get(
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
          setMatches(response.data);
          
          setLoading(false);
        });
    }
    setLoading(false);
  }, [matchesApiURL, selectedHostel1, selectedHostel2, selectedSport]);

  const hostel1handleChange = (e) => {
    setSelectedHostel1(e.target.value);
  };
  const hostel2handleChange = (e) => {
    setSelectedHostel2(e.target.value);
  };
  const sporthandleChange = (e) => {
    setSelectedSport(e.target.value);
  };


  return (
    <div className='p-4'>
      <div className='standings_header d-flex flex-row align-items-center'>
        <div className='standings_text'>RESULTS</div>
      </div>
      <div className='w-100 black_line' />
      <div className='d-flex flex-row align-items-center justify-content-between'>
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
          <select className='results_dropdown w-2' name='' id=''>
            <option hidden>SPORT</option>
            {sports.map((sport, i) => (
              <option value={i}>{sport.name}</option>
            ))}
          </select>
          <select className='results_dropdown w-2' name='' id=''>
            <option hidden>HOSTEL</option>
            {hostels.map((hostel, i) => (
              <option value={i}>{hostel.name}</option>
            ))}
          </select>
        </div>
      </div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ResultA
          Team1={selectedHostel1.name}
          Team2={selectedHostel2.name}
          Sport={selectedSport.name}
          Stage={1}
          Status={false}
          Date_time='2022-03-19T04:25:52Z'
        />
      )}
    </div>
  );
};

export default Results;
