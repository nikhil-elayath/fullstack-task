
//Reuseable srearch card
// @params->
// universityImage,universityName,universityDescription,webpageUrl
import React from "react";
import "../assests/styles/common/SearchCard.css";
export default function SearchCard(props) {
  return (
    <div id="SearchCard__mainContainer">
      <div id="SearchCard__imageContainer">
        <img id="SearchCard__image" src={props.universityImage}></img>
      </div>
      <div id="SearchCard__headingContainer">{props.universityName}</div>
      <div id="SearchCard__descriptionContainer">
        {props.universityDescription}
      </div>
      <div id="SearchCard__descriptionContainer">{props.webpageUrl}</div>
    </div>
  );
}
