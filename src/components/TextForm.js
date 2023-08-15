
import React ,{useState}from 'react'

export default function TextForm(props) {
  const handleUpClick = ()=>{
  //   console.log("UpperCase was clicked");
    let newText = text.toUpperCase();
    setText(newText)
  }
  const handleLowClick =()=>{
     let newText = text.toLowerCase();
     setText(newText)
  }

  const handleOnChange = (event)=>{
    setText(event.target.value);
  }
  
  const [text, setText] = useState('');
  return (
    <>
    <div className="container">
    <h1>{props.heading}</h1>
    <div className="mb-3">
    <textarea className="form-control" value={text} id="myBox" onChange={handleOnChange} rows="8"></textarea>
    </div>
    <button className="btn btn-primary mx-1" onClick={handleUpClick}>Convert to uppercase</button>
    <button className="btn btn-primary mx-1" onClick={handleLowClick}>Convert to Lowercase</button>

    </div>
    <div className="container my-4">
      <h3>Your text summary</h3>
      <p >{text.split(" ").length} words, {text.length} characters</p>
      <p>{0.008 * text.split(" ").length} Minutes to read the text</p>
      <h3>Preview</h3>
      <p>{text}</p>
    </div>
    </>
  )
}
