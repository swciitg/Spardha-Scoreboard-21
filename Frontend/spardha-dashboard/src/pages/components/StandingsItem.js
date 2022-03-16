import React from 'react';

const StandingsItem = (props) => {
return (
    <div className="standings_item">
        <div className="standings_item_circle"></div>
        <div className="standings_item_name">{props.Name}</div>
        <div className="standings_item_points">{props.Points}</div>
    </div>
  )
};

export default StandingsItem;