import React from 'react';
import { NavLink } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowTrendUp, faTrophy, faCalendarDay } from '@fortawesome/free-solid-svg-icons';

const tabs = [{
  route: "/standings",
  icon: faArrowTrendUp,
  label: "Standings"
},{
  route: "/schedule",
  icon: faCalendarDay,
  label: "Schedule"
},{
    route: "/results",
    icon: faTrophy,
    label: " Results "
  }]

const Navigation = (props) => {
    return (
        <div className="fixed-bottom w-100 bottom_navbar pt-1">
            {tabs.map((tab, i) =>(
                <NavLink to={tab.route} className="d-flex flex-column justify-content-center align-items-center p-1 nav_link">
                    <div className="icon_bg">
                        <FontAwesomeIcon size="s" icon={tab.icon} className="fa_icon"/>
                    </div>
                    <div>{tab.label}</div>
                </NavLink>
            ))}
        </div>

    )
};

export default Navigation;
