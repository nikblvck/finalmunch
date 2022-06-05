import {useEffect, useState} from 'react';
import {useSelector, useDispatch} from 'react-redux';

function NewPost(){
  const [caption, setCaption] = useState('');
  const [images, setImages] = useState([]);
  const [categories, setCategories] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const user = useSelector(state => state.user);
  const dispatch = useDispatch();

  


  return (
    <>
    </>
  );
}
