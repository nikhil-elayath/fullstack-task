import { combineReducers } from "redux";
import universityData from "./UniversityReducer";
export default combineReducers({
    universityData: universityData,
});
