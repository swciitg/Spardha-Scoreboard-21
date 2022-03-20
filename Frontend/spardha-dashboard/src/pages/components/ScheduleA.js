import React from 'react';

const ScheduleA = (props) => {

return (
    <div className="result_A">
        <div className="d-flex flex-row justify-content-between">
            <div className="result_sport"><span>{props.sport}</span> <span>{/* "<" +props.type + ">" */}</span></div>
            <div><span className="result_date">{props.date}</span> <span className="vertical_line">|</span> <span className="result_date">{props.time}</span></div>
        </div>
        <div className="result_details">
            <div className="d-flex flex-row justify-content-between result_list_item">
                <div className="result_hostel d-flex flex-row align-items-center">
                    <div className="standings_item_circle"></div>
                    <div className="standings_item_name">{props.team1}</div>
                </div>
            </div>
            <div className="d-flex flex-row justify-content-between result_list_item">
                <div className="result_hostel d-flex flex-row align-items-center">
                    <div className="standings_item_circle"></div>
                    <div className="standings_item_name">{props.team2}</div>
                </div>
            </div>
        </div>
        <div className="d-flex flex-row justify-content-between">
            <div className="result_stage">Stage {props.stage}</div>
        </div>
    </div>
  )
};

export default ScheduleA;