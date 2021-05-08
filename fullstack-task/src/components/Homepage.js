import React, { useEffect, useState, useMemo } from "react";
import SearchCard from "../common/SearchCard";
import { useDispatch, useSelector } from "react-redux";
import countryList from "react-select-country-list";
import Select from "react-select";

import {
  getAllUniversityData,
  getSearchResults,
} from "../actions/UniversityDetails";
import FilterIcon from "../assests/icons/filter.svg";

import "../assests/styles/components/Homepage.css";

export default function Homepage() {
  const [searchQuery, setSearchQuery] = React.useState("");
  const [showingSearchResults, setShowingSearchResults] = React.useState(false);
  const [value, setValue] = useState("");
  const options = useMemo(() => countryList().getData(), []);
  // handles change for the drop down
  // updates the state with the selected value and makes an api call
  const changeHandler = (value) => {
    setValue(value);
    let searchData={
      searchQuery:searchQuery,
      // the counterey code
      country:value.value
    }
    dispatch(getSearchResults(searchData));

  };

  const dispatch = useDispatch();
  const store = useSelector((state) => state.universityData);
  // function that handles the search submit

  const searchSubmit = async (event) => {
    // to prevent refreshing of the page
    event.preventDefault();
    let searchData={
      searchQuery:searchQuery,
      country:"US"
    }
    // passes the search query and the country code to the api
    dispatch(getSearchResults(searchData));
    // sets setShowingSearchResults = true to show the filter division
    // User should be allowed to filter through the only the search results
    await setShowingSearchResults(true);
    // setting the value of the country code to '' so that there is no default country set
    await setValue('');
  };

  // handling the text entered by the user
  const onTextEnter = (enteredText) => {
    setSearchQuery(enteredText.target.value);
  };

  useEffect(async () => {
    // action call that will get all the university entries
    await dispatch(getAllUniversityData());
  }, []);

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
          {/* <h2> Filter</h2> */}
            <img src={FilterIcon} id="Homepage__filterIcon" />
          <div id="Homepage__dropdown">
            <Select options={options} value={value} onChange={changeHandler}  styles={{width:"100px"}} placeholder={"Filter by country"}/>

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
          <div id="Homepage__noResultsContainer">
          <h2>No results found </h2>
          </div>
        )}
      </div>
    </div>
  );
}
