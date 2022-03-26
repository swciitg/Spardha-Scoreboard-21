import StandingsItem from './components/StandingsItem';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'react-datepicker/dist/react-datepicker.css';
import Footer from './components/Footer';
import LoadingMask from 'react-loadingmask';
import 'react-loadingmask/dist/react-loadingmask.css';

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
      // console.log(response.data);
      setHostels(response.data);
      setLoading(false);
    });
  }, [hostelApiURL]);

  useEffect(() => {
    setLoading(true);
    axios.get(sportApiURL).then((response) => {
      // console.log(response.data);
      setSports(response.data);
      setLoading(false);
    });
  }, [sportApiURL]);
  useEffect(() => {
    console.log('triggered');
    setLoading(true);
    // console.log(selectedSport);
    if (selectedSport !== '-1' && selectedSport !== '-2') {
      axios
        .get(standingsApiURL + '?sport=' + selectedSport)
        .then((response) => {
          // console.log(response.data);
          setStandings(response.data);
          setLoading(false);
        });
    }
    setLoading(false);
  }, [standingsApiURL, selectedSport]);
  useEffect(() => {
    setLoading(true);
    axios.get(overallStandingsApiURL).then((response) => {
      // console.log(response.data.boys);
      setOverallStandings(response.data.boys);
      setOverallStandingsGirls(response.data.girls);
      setLoading(false);
    });
  }, [overallStandingsApiURL]);

  const sportHandler = (event) => {
    // console.log(event.target.value);
    setSelectedSport(event.target.value);
  };

  return (
    <div className='p-4 standings'>
      <div className='standings_header d-flex flex-row align-items-center justify-content-between'>
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
      </div>
      {/* <div className='w-100 black_line' /> */}
      <div className='standings_h2 px-2'>TABULAR FORM</div>
      <div className='px-2'>
        {loading ? (
          <LoadingMask loading={true} text={'loading...'}>
            <div style={{ width: 200, height: 100 }}></div>
          </LoadingMask>
        ) : selectedSport === '-1' ? (
          overallStandings.map((hostel, i) => (
            <StandingsItem
              Name={hostel.name}
              Points={hostel.overall_points}
              Index={i}
              Result={true}
              Image={hostels.find((o) => o.name === hostel.name)['logo']}
              className='m-2'
            />
          ))
        ) : selectedSport === '-2' ? (
          overallStandingsGirls.map((hostel, i) => (
            <StandingsItem
              Name={hostel.name}
              Points={hostel.overall_points}
              Index={i}
              Result={true}
              Image={hostels.find((o) => o.name === hostel.name)['logo']}
              className='m-2'
            />
          ))
        ) : (
          standings.map((hostel, i) => (
            <StandingsItem
              Name={hostel.hostel}
              Points={hostel.points}
              Index={i}
              Result={true}
              Image={hostels.find((o) => o.name === hostel.hostel)['logo']}
              className='m-2'
            />
          ))
        )}
      </div>
      <div className='pt-2 pb-3'></div>
      <Footer />
    </div>
  );
};

export default Standings;
