import {
    GET_ALL_UNIVERSITY_DATA,
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