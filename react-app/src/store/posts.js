//Constants
const GET_ALL_POSTS = 'posts/GET_ALL_POSTS';
const GET_ONE_POST = 'posts/GET_ONE_POST';
const CREATE_POST = 'posts/CREATE_POST';
const UPDATE_POST = 'posts/UPDATE_POST';
const DELETE_POST = 'posts/DELETE_POST';


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


//READ ALL POSTS THUNK
export const getAllPosts = () => async dispatch => {
  const response = await fetch('/api/posts/');
  const posts = await response.json();
  dispatch(getAllPosts(posts));
}

//Reducer
const initialState = {
  posts: [],
  post: {}
};

export default function reducer(state = initialState, action) {
  let newState;

  switch (action.type) {
    case GET_ALL_POSTS:
      newState = {...state};
      newState.posts = action.posts;
      newState.isLoading = false;
      return newState;
    case GET_ONE_POST:
      newState = {...state};
      newState.post = action.post;
      newState.isLoading = false;
      return newState;
    default:
      return state;
}
}
