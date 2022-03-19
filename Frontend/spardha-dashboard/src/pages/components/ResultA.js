import React from 'react';

const ResultA = (props) => {

    const unixTimeZero = Date.parse(props.Date_time);

return (
    <div className="result_A">
        <div className="d-flex flex-row justify-content-between">
            <div className="result_sport"><span>{props.Sport}</span> <span>5v5</span></div>
            <div><span className="result_date">5 Mar</span> <span className="vertical_line">|</span> <span className="result_date">9:00pm</span></div>
        </div>
        <div className="result_details">
            <div className="d-flex flex-row justify-content-between">
                <div className="result_hostel d-flex flex-row align-items-center">
                    <div className="standings_item_circle"></div>
                    <div className="standings_item_name">{props.Team1}</div>
                </div>
                <div className="result_score_winner">3</div>
            </div>
            <div className="d-flex flex-row justify-content-between">
                <div className="result_hostel d-flex flex-row align-items-center">
                    <div className="standings_item_circle"></div>
                    <div className="standings_item_name">{props.Team2}</div>
                </div>
                <div className="result_score_loser">1</div>
            </div>
        </div>
        <div className="d-flex flex-row justify-content-between">
            <div className="result_stage">Group Stage</div>
            <div className="result_final_text">Kameng won</div>
        </div>

        
    </div>
  )
};

export default ResultA;