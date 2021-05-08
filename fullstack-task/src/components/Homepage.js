import React, { useEffect, useState } from "react";
import SearchCard from "../common/SearchCard";
import { useDispatch, useSelector } from "react-redux";
import { getAllUniversityData, getSearchResults } from "../actions/UniversityDetails";

import "../assests/styles/components/Homepage.css";

export default function Homepage() {
  const [playerData, setPlayerData] = useState([]);
  const [searchQuery, setSearchQuery] = React.useState("");
  const dispatch = useDispatch();
  const store = useSelector((state) => state.universityData);
  const searchSubmit = (event) => {
    console.log("from searchSubmit")
    // to prevent refreshing of the page
    event.preventDefault();
    console.log("search",searchQuery)
    dispatch(getSearchResults(searchQuery))

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
      <div id="Homepage__mainContainer">
      {store.allUniversityData &&
        store.allUniversityData.length != 0 &&
        store.allUniversityData.map((item, index) => {
          return (
            <SearchCard
              countryCode={item.alpha_two_code}
              country={item.country}
              domain={item.domain}
              universityDescription={item.university_description}
              universityImage={item.university_image}
              universityName={item.university_name}
              webpageUrl={item.web_page}
            />
          );
        })}
        </div>
    </div>
  );
}
