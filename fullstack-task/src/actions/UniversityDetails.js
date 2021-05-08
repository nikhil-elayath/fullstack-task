import {
    GET_ALL_UNIVERSITY_DATA,
    GET_SEARCH_RESULTS
    } from './Types';
  
  import axios from 'axios';
  import config from '../config';
  const url = config.url;

  export const getAllUniversityData = () => async dispatch => {
    return axios
      .get(url + '/get-university-details')
      .then(res => {
        dispatch({
          type: GET_ALL_UNIVERSITY_DATA,
          payload: res.data,
        });
      })
      .catch(err => {
        // dispatch({type: ERROR, payload: err});
      });
  };
//   search
  export const getSearchResults = (searchQuery) => async dispatch => {
      console.log("searchQuery from actions",searchQuery)
    return axios
      .post(url + '/search',searchQuery)
      .then(res => {
        dispatch({
          type: GET_SEARCH_RESULTS,
          payload: res.data,
        });
      })
      .catch(err => {
          console.log("error from action",err)
        // dispatch({type: ERROR, payload: err});
      });
  };