import React from 'react';

const StandingsItem = (props) => {
  var circle;
  if( props.Index===0){
    circle = (
      <div className="standings_item_circle gold_circle">1</div>
    )
  }else if(props.Index===1){
    circle = (
      <div className="standings_item_circle silver_circle">2</div>
    )
  }else if(props.Index===2){
    circle = (
      <div className="standings_item_circle bronze_circle">3</div>
    )
  }else{
    circle = (
      <div className="standings_item_circle"></div>
    )
  }
return (
    <div className="standings_item">
        {circle}
        <div className="standings_item_name">{props.Name}</div>
        <div className="standings_item_points">{props.Points}</div>
    </div>
  )
};

export default StandingsItem;