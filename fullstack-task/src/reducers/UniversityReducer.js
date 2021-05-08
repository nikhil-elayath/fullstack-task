import {
    GET_ALL_UNIVERSITY_DATA,
   
  } from '../actions/Types';
  
  const initalState = {
   allUniversityData:[]
  };
  
  export default function (state = initalState, action) {
    switch (action.type) {
      case GET_ALL_UNIVERSITY_DATA:
        return {
          ...state,
          allUniversityData: action.payload,
        };
     
      default:
        return state;
    }
  }
  