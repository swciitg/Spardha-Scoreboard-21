import React from 'react';
import StandingsItem from './StandingsItem';

const ScheduleB = (props) => {

    console.log(props.scores);

    var standings = [];
    var i = 0;
    for (const key in props.scores) {
        console.log(`${key}: ${props.scores[key]}`);
        standings.push(<StandingsItem Name={key} Index={i} />)
        i++;
    }

    return (
        <div className="result_A">
            <div className="d-flex flex-row justify-content-between align-items-center">
                <div className="d-flex flex-column">
                    <div className="result_sport">Athletics</div>
                    <div className="result_sport_detail">{props.sport}</div>
                </div>
                <div><span className="result_date">{props.date}</span> <span className="vertical_line">|</span> <span className="result_date">{props.time}</span></div>
            </div>
            <div className="result_details">
                {standings}
            </div>
            <div className="d-flex flex-row justify-content-between mt-1">
                <div className="result_stage">Group Stage</div>
            </div>
        </div>
    )
};

export default ScheduleB;