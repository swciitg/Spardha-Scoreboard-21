import React from 'react';
import StandingsItem from './StandingsItem';

const ResultB = (props) => {

    //console.log(props.scores);

    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    var date = new Date(props.date);
    var date_of_month = date.getDate();
    var month = monthNames[date.getMonth()];

    var time = toDateWithOutTimeZone(props.time);
    // console.log(props.hostels)
    var standings = [];
    var i = 0;
    for (const key in props.scores) {
        // console.log(`${key}: ${props.scores[key]}`);
        standings.push(<StandingsItem Name={props.scores[key].hostel} Points={props.scores[key].score} Index={i} Result = {props.result} Image={props.hostels.find(o => o.name === props.scores[key].hostel)?.logo || "alt"}/>)
        i++;
    }

    return (
        <div className="result_A">
            <div className="d-flex flex-row justify-content-between align-items-center">
                <div className="d-flex flex-column">
                    <div className="result_sport">{props.sport}</div>
                    {/* <div className="result_sport_detail">{props.sport}</div> */}
                </div>
                <div><span className="result_date">{date_of_month} {month}</span> <span className="vertical_line">|</span> <span className="result_date">{formatAMPM(time)}</span></div>
            </div>
            <div className="result_details">
                {standings}
            </div>
            <div className="d-flex flex-row justify-content-between mt-1 align-items-center">
                <div className="result_stage">{props.round}</div>
                {props.result && 
                <div className="result_final_text">{props.scores[0].hostel} won</div>
                }
            </div>
        </div>
    )
};

function toDateWithOutTimeZone(date) {
    let tempTime = date.split(":");
    let dt = new Date();
    dt.setHours(tempTime[0]);
    dt.setMinutes(tempTime[1]);
    dt.setSeconds(tempTime[2]);
    return dt;
  }


function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + " " + ampm;
    return strTime;
}

export default ResultB;