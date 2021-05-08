import React, { useEffect, useState } from "react";
import SearchCard from "../common/SearchCard";
import { useDispatch, useSelector } from "react-redux";
import {
  getAllUniversityData,
  getSearchResults,
} from "../actions/UniversityDetails";
import FilterIcon from "../assests/icons/filter.svg";

import "../assests/styles/components/Homepage.css";

export default function Homepage() {
  const [playerData, setPlayerData] = useState([]);
  const [searchQuery, setSearchQuery] = React.useState("");
  const [showingSearchResults, setShowingSearchResults] = React.useState(false);
  const [selectedCountryCode, setSelectedCountryCode] = React.useState("US");
  const dispatch = useDispatch();
  const store = useSelector((state) => state.universityData);
  const searchSubmit = async (event) => {
    console.log("from searchSubmit");
    // to prevent refreshing of the page
    event.preventDefault();
    console.log("search", searchQuery);
    dispatch(getSearchResults(searchQuery));
    await setShowingSearchResults(true);
  };
  const onTextEnter = (enteredText) => {
    setSearchQuery(enteredText.target.value);
  };

  useEffect(async () => {
    // action call that will get all the user entries
    await dispatch(getAllUniversityData());
  }, []);
  console.log("store from home", store);

  return (
    <div id="Homepage__parentContainer">
      <div id="Homepage__searchBarContainer">
        <form onSubmit={searchSubmit}>
          <input
            id="homepage__inputField"
            placeholder="Enter University name"
            onChange={onTextEnter}
            onSubmit={searchSubmit}
          />
        </form>
      </div>
      {/* filter container */}
      {showingSearchResults == true && (
        <div id="Homepage__filterContainer">
          <h2> Filter</h2>
          <div>
          <img src={FilterIcon} id="Homepage__filterIcon" />
          </div>
        </div>
      )}
      <div id="Homepage__mainContainer">
        {store.allUniversityData && store.allUniversityData.length != 0 ? (
          store.allUniversityData.map((item, index) => {
            return (
              <div>
                <SearchCard
                  countryCode={item.alpha_two_code}
                  country={item.country}
                  domain={item.domain}
                  universityDescription={item.university_description}
                  universityImage={item.university_image}
                  universityName={item.university_name}
                  webpageUrl={item.web_page}
                />
              </div>
            );
          })
        ) : (
          <h2>No results found </h2>
        )}
      </div>
    </div>
  );
}
