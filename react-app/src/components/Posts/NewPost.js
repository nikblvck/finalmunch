import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import Select from "react-select";
import { useHistory } from "react-router";
import { addPost } from "../../../store/posts";
import { getCategories } from "../../../store/categories";
import "./NewPost.css";

function NewPost() {
	const dispatch = useDispatch();
	const history = useHistory();
	const user = useSelector((state) => state?.session?.user);
	const [images, setImages] = useState([]);
	const [caption, setCaption] = useState("");
	const [category_ids, setCategoryIds] = useState([]);
	const [isLoaded, setIsLoaded] = useState(false);
	const [errors, setErrors] = useState([]);
	const categories = useSelector((state) => state?.categories);
	console.log(categories);
	const categoriesArray = Object?.values(categories);

	useEffect(() => {
		dispatch(getCategories()).then(() => setIsLoaded(true));
	}, [dispatch, isLoaded]);

	const handleSubmit = async (e) => {
		e.preventDefault();
		const newPost = {
			images,
			caption,
			category_ids,
			user_id: user.id,
		};
		if (newPost) {
			const data = await dispatch(addPost(newPost));
			if (data) {
				setErrors(data);
			} else {
				history.push("/posts");
			}
		}
	};

	return (
		<>
			<div className="home_feed_container">
				<div className="post_form_container">
					<div className="post_form_header">
						<p>New Post</p>
					</div>
					<div className="post_form_content">
						<div className="post_form_image">
							<img src={image_url} alt={caption} className="post_form_image" />
						</div>
						<div className="post_form_inputs">
							<div className="form_errors">
								{!errors.length ? null : (
									<div>
										{errors.map((error) => (
											<div key={error}>{error}</div>
										))}
									</div>
								)}
							</div>
							<form className="post_form" onSubmit={handleSubmit}>
								<label htmlFor="image_url">Image URL *</label>
								<input
									type="text"
									name="image_url"
									value={image_url}
									onChange={(e) => setImage_url(e.target.value)}
								/>
								<label htmlFor="caption">Caption</label>
								<input
									className="caption_input"
									type="text"
									name="caption"
									value={caption}
									placholder="Caption [optional]"
									onChange={(e) => setCaption(e.target.value)}
								/>
								<label htmlFor="category_id">Category *</label>
								<select
									className="category_select"
									value={category_id}
									onChange={(e) => setCategoryId(e.target.value)}
								>
									<option> --Select a Category-- </option>
									{categoriesArray?.map((category) => (
										<option key={category?.id} value={category?.id}>
											{category?.name}
										</option>
									))}
								</select>
								<div className="new_post_btns">
									<button className="delete_btn" type="submit ">
										{" "}
										Save
									</button>
									<button
										className="delete_btn"
										type="cancel"
										onClick={() => history.push("/posts")}
									>
										Cancel
									</button>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</>
	);
}

export default NewPost;
