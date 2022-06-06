//Categories
const GET_CATEGORIES = "categories/GET_CATEGORIES";
//CATEGORIES
//READ ALL CATEGORIES ACTION CREATOR
const getCategories = categories => ({
	type: GET_CATEGORIES,
	categories,
});


export const getAllCategories = () => async (dispatch) => {
	const response = await fetch("/api/categories/", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const categories = await response.json();
		dispatch(getCategories(categories));
	}
};


const initialState = {};

export default function reducer(state = initialState, action) {
  let newState;

  switch(action.type){
    case GET_CATEGORIES:
      newState = {...state};
      newState = action.categories;
      return newState;
    default:
      return state;
  }
}
