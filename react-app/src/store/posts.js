//Constants
//Posts
const GET_ALL_POSTS = 'posts/GET_ALL_POSTS';
const GET_ONE_POST = 'posts/GET_ONE_POST';
const CREATE_POST = 'posts/CREATE_POST';
const UPDATE_POST = 'posts/UPDATE_POST';
const DELETE_POST = 'posts/DELETE_POST';
//Categories
const GET_CATEGORIES = 'categories/GET_CATEGORIES';


//POSTS
//READ ALL POSTS ACTION CREATOR
const getPosts = posts => ({
  type: GET_ALL_POSTS,
  posts,
});

//READ ONE POST ACTION CREATOR
const getPost = post => ({
  type: GET_ONE_POST,
  post,
});

//CREATE POST ACTION CREATOR
const createPost = post => ({
  type: CREATE_POST,
  post,
});

//UPDATE POST ACTION CREATOR
const updatePost = post => ({
  type: UPDATE_POST,
  post,
});
//DELETE POST ACTION CREATOR
const deletePost = post => ({
  type: DELETE_POST,
  post,
});

//CATEGORIES
//READ ALL CATEGORIES ACTION CREATOR
const getCategories = categories => ({
	type: GET_CATEGORIES,
	categories,
});


//CREATE POST THUNK
export const addPost = (post) => async (dispatch) => {
	const response = await fetch("/api/posts/new/", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(post),
	});
	if (response.ok) {
		const newPost = await response.json();
		dispatch(createPost(newPost));
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};


//READ ALL POSTS THUNK
export const getAllPosts = () => async (dispatch) => {
	const response = await fetch("/api/posts/", {
		headers: {
			"Content-Type": "application/json",
		},
	});

	if (response.ok) {
		const posts = await response.json();
		dispatch(getPosts(posts));
	}
};

//READ ALL CATEGORIES THUNK
// export const getAllCategories = () => async (dispatch) => {
// 	const response = await fetch("/api/categories/", {
// 		headers: {
// 			"Content-Type": "application/json",
// 		},
// 	});

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

//Reducer
const initialState = {
  posts: [],
  post: {},
	categories: [],
};

export default function reducer(state = initialState, action) {
  let newState;

  switch (action.type) {
    case GET_ALL_POSTS:
      newState = {...state};
      newState.posts = action.posts;
      return newState;
    case GET_ONE_POST:
      newState = {...state};
      newState.post = action.post;
      newState.isLoading = false;
      return newState;
		case GET_CATEGORIES:
			newState = {...state};
			newState.categories = action.categories;
			return newState;
    default:
      return state;
}
}
