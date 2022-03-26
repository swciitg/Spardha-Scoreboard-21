import React from 'react';

const ResultA = (props) => {

    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    var date = new Date(props.date);
    var date_of_month = date.getDate();
    var month = monthNames[date.getMonth()];

    var time = toDateWithOutTimeZone(props.time);

    var team1_winner = true;
    if(props.result && props.winner === 2){team1_winner = false;}
    const isTie = props.score1 == props.score2;

    // console.log(props.image1);

    

return (
    <div className="result_A">
        <div className="d-flex flex-row justify-content-between">
            <div className="result_sport"><span>{props.sport}</span> <span>{/* "<" +props.type + ">" */}</span></div>
            <div><span className="result_date">{date_of_month} {month}</span> <span className="vertical_line">|</span> <span className="result_date">{formatAMPM(time)}</span></div>
        </div>
        <div className="result_details">
            <div className="d-flex flex-row justify-content-between result_list_item">
                <div className="result_hostel d-flex flex-row align-items-center">
                    <div className="standings_item_circle blank_circle" style={{backgroundImage: `url(${team1_winner ? props.image1 : props.image2})`}}></div>
                    <div className="standings_item_name">{team1_winner ? props.team1 : props.team2}</div>
                </div>
                {props.result && 
                <div className={"d-flex flex-row align-items-center"+(isTie?" loser_div":"")}>
                    <div className={isTie?"result_score_loser standings_item_name" :"result_score_winner standings_item_name"}>{team1_winner ? props.score1 : props.score2}</div>
			{!isTie &&<img src="./left_arrow.png" alt="arrow" className="arrow_img" /> }
                </div>}
            </div>
            <div className="d-flex flex-row justify-content-between result_list_item">
                <div className="result_hostel d-flex flex-row align-items-center">
                    <div className="standings_item_circle blank_circle" style={{backgroundImage: `url(${team1_winner ? props.image2 : props.image1})`}}></div>
                    <div className="standings_item_name">{team1_winner ? props.team2 : props.team1}</div>
                </div>
                {props.result && 
                <div className="d-flex flex-row align-items-center loser_div">
                    <div className="result_score_loser standings_item_name">{team1_winner ? props.score2 : props.score1}</div>
                </div>
                
                }
            </div>
        </div>
        <div className="d-flex flex-row justify-content-between align-items-center">
            <div className="result_stage">{props.stage}</div>
            {props.result && !isTie && 
            <div className="result_final_text">{team1_winner ? props.team1 : props.team2} won</div>
            }
            {props.result && isTie && <div className="result_final_text">Tie</div>}
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
export default ResultA;
