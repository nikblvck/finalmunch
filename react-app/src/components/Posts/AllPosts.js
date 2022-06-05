import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getAllPosts } from '../../store/posts';
import { getAllCategories } from '../../store/categories';
import './AllPosts.css';

function AllPosts() {
  const user = useSelector(state => state?.session?.user);
  const dispatch = useDispatch();
  const posts = useSelector((state) => state?.posts?.posts?.posts);
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
			<div className="home-container">
				<div>
					<p>Home Container</p>
				</div>
				<div className="all-posts-container">
					{posts?.map((post) => (
						<div key={post.id}>
							<h1>{post.caption}</h1>
							{post?.images?.map((image) => (
								<img
									src={image.url}
									alt={image.caption}
									className="post_img_home"
								/>
							))}
							{post?.has_categories?.map((category) => (
								<h3>{category}</h3>
							))}
						</div>
					))}
				</div>
			</div>
		</>
	);

}


export default AllPosts;
