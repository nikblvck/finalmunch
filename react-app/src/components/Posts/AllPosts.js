import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAllPosts } from '../../store/posts';

function AllPosts() {
  const user = useSelector(state => state?.session?.user);
  const dispatch = useDispatch();
  const posts = useSelector((state) => state?.posts?.posts);
  const[ isLoaded, setIsLoaded ]= useState(false);



  return (
    <>
      <h1>All Posts</h1>
      <h1>{user.username}</h1>

    </>
  )

}


export default AllPosts;
