import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAllPosts, getAllCategories } from '../../store/posts';
import './AllPosts.css';

function AllPosts() {
  const user = useSelector(state => state?.session?.user);
  const dispatch = useDispatch();
  const posts = useSelector((state) => state?.posts?.posts);
  const[ isLoaded, setIsLoaded ]= useState(false);
  console.log(posts)
  useEffect(() => {
    if (!isLoaded) {
      dispatch(getAllPosts());
      dispatch(getAllCategories());
      setIsLoaded(true);
    }
  }, [dispatch, isLoaded]);


  return (
    <>
      <h1>All Posts</h1>
      {posts?.map((post) => (
        <div key={post.id}>
          <h1>{post.caption}</h1>
          {post?.images?.map((image) => (
            <img src={image.url} alt={image.caption} className="post_img_home"/>
          ))}
          {post?.has_categories?.map((category) => (
            <h3>{category}</h3>
          ))}
          </div>
      ))}



    </>
  )

}


export default AllPosts;
