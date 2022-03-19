import React from 'react';

const ResultB = (props) => {

    const unixTimeZero = Date.parse(props.Date_time);

    const data = [{
        name: "Brahmaputra",
        points: 800,
      }, {
        name: "Lohit",
        points: 700,
      }, {
        name: "Siang",
        points: 700,
      }, {
        name: "Manas",
        points: 600,
      }, {
        name: "Kapili",
        points: 500,
      }, {
        name: "Disang",
        points: 400,
      },];

return (
    <div className="result_A">
        <div className="d-flex flex-row justify-content-between align-items-center">
            <div className="d-flex flex-column">
                <div className="result_sport">{props.Sport}</div>
                <div className="result_sport_detail">{props.Sport}</div>
            </div>
            <div><span className="result_date">5 Mar</span> <span className="vertical_line">|</span> <span className="result_date">9:00pm</span></div>
        </div>
        <div className="result_details">
            {
                data.map((item, index) => (
                        <div className="d-flex flex-row justify-content-between align-items-center pt-1 pb-1">
                            <div className="d-flex flex-row">
                                <div className="standings_item_circle"></div>
                                <div className="standings_item_name">{item.name}</div>
                            </div>
                            <div className="result_score_winner">{item.points}</div>
                        </div>
                    ))
            }
        </div>
        <div className="d-flex flex-row justify-content-between mt-1">
            <div className="result_stage">Group Stage</div>
            <div className="result_final_text">Kameng won</div>
        </div>

        
    </div>
  )
};

export default ResultB;