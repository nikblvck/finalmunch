//Constants
const GET_ALL_POSTS = 'posts/GET_ALL_POSTS';
const GET_ONE_POST = 'posts/GET_ONE_POST';
const CREATE_POST = 'posts/CREATE_POST';
const UPDATE_POST = 'posts/UPDATE_POST';
const DELETE_POST = 'posts/DELETE_POST';

const getAllPosts = posts => ({
  type: GET_ALL_POSTS,
  posts,
});

const getOnePost = post => ({
  type: GET_ONE_POST,
  post,
});

const createPost = post => ({
  type: CREATE_POST,
  post,
});

const updatePost = post => ({
  type: UPDATE_POST,
  post,
});

const deletePost = post => ({
  type: DELETE_POST,
  post,
});

export const getAllPostsThunk = () => async dispatch => {
  const response = await fetch('/api/posts/');
  const posts = await response.json();
  dispatch(getAllPosts(posts));
}
