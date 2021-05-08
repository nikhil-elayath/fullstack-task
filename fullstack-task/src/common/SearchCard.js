import React from "react";
import "../assests/styles/common/SearchCard.css";

export default function SearchCard(props) {
  return (
    <div id="SearchCard__mainContainer">
      <div id="SearchCard__imageContainer">
        <img
          id="SearchCard__image"
          src={
            "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Abilene_Christian_Wildcats_logo.svg/1200px-Abilene_Christian_Wildcats_logo.svg.png"
          }
        ></img>
      </div>
      <div id="SearchCard__headingContainer">{props.universityName}</div>
      <div id="SearchCard__descriptionContainer">
        {props.universityDescription}
      </div>
      <div id="SearchCard__descriptionContainer">{props.webpageUrl}</div>
    </div>
  );
}
