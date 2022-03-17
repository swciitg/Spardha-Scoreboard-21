import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { faCaretDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';


const Results = (props) => {
  const [date, setDate] = useState(new Date());
  const baseApiURL = 'http://localhost:8000/spardhaApi/';
  const [hostelApiURL, setHostelApiURL] = useState(baseApiURL+'hostels/');
  const [sportApiURL, setSportApiURL]  = useState(baseApiURL+'sports/');
  const [resultsApiURL, setResultsApiURL] = useState(baseApiURL+'results/');
  const [hostels, setHostels] = useState([]);
  const [sports, setSports] = useState([]);
  const [results, setResults] = useState([]);
  const [selectedHostel, setSelectedHostel] = useState('');
  const [selectedSport, setSelectedSport] = useState('');
  const [selectedDate, setSelectedDate] = useState('');
  const [selectedResults, setSelectedResults] = useState([]);


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
    axios.get(resultsApiURL).then((response) =>{
      console.log(response.data);
      setResults(response.data);
    })
  }, [resultsApiURL]);


  return (
    <div className='p-4'>
      <div className='standings_header d-flex flex-row align-items-center'>
        <div className='standings_text'>RESULTS</div>
      </div>
      <div className='w-100 black_line' />
      <div className='d-flex flex-row align-items-center justify-content-between'>
        <div className='results_h2'>FILTERS</div>
        <div className='d-flex flex-row align-items-center'>
          <div>
            <DatePicker
              className='results_dropdown_date'
              placeholderText='DATE'
              selected={date}
              onChange={(date) => setDate(date)}
            />
          </div>
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
    </div>
  );
};

export default Results;
