import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import CardA from './components/CardA';
import CardB from './components/CardB';
import CardC from './components/CardC';
import CardD from './components/CardD';

const Schedule = (props) => {
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
          matchesApiURL
        )
        .then((response) => {
          console.log(response.data);
          setMatches(response.data.data);
          setLoading(false);
        });
  }, [matchesApiURL, selectedHostel, selectedSport]);

  const handleHostelChange = (e) => {
    setSelectedHostel(e.target.value);
  };
  const handleSportChange = (e) => {
    setSelectedSport(e.target.value);
  };

  return (
    <div className='p-4 results'>
      <div className='results_header d-flex flex-row align-items-center'>
        <div className='results_text'>SCHEDULE</div>
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
        {
          'A': match.status === false && <CardA {...match} result={false}/>,
          'B': match.status === false && <CardB {...match} result={false}/>,
          'C': match.status === false && <CardC {...match} result={false}/>,
          'D': match.status === false && <CardD {...match} result={false}/>
        }[match.type]
      ))
      )} 
    </div>
  );
};

export default Schedule;
