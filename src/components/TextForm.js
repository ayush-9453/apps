
import React ,{useState}from 'react'

export default function TextForm(props) {
  const handleUpClick = ()=>{
  //   console.log("UpperCase was clicked");
    let newText = text.toUpperCase();
    setText(newText)
    props.showAlert("Converted to UpperCase","success")
  } 

  const handleLowClick =()=>{
     let newText = text.toLowerCase();
     setText(newText)
     props.showAlert("Converted to LowerCase","success")
  }

  const handleClrClick = ()=>{
    //   console.log("UpperCase was clicked");
      let newText = '';
      setText(newText)
    }
    const speak = () => {
      let msg = new SpeechSynthesisUtterance();
      msg.text = text;
      window.speechSynthesis.speak(msg);
    }    
    const replacecasefunc = () => {
      let existing_text = prompt("Enter which word to replace : ");
      let replaced_text = prompt("Enter New Text");
      setText(text.replaceAll(existing_text, replaced_text))
    }
  const handleOnChange = (event)=>{
    setText(event.target.value);
  }

  
  const [text, setText] = useState('');
  return (
    <>
    <div className="container" style={{color: props.mode ==="dark"?"white":"#3E454C" }}>
    <h1>{props.heading}</h1>
    <div className="mb-3">
    <textarea className="form-control" value={text} style={{backgroundColor: props.mode ==="dark"?"grey":"white",color: props.mode ==="dark"?"white":"#3E454C" }} id="myBox" onChange={handleOnChange} rows="8"></textarea>
    </div>
    <button className="btn btn-primary mx-1" onClick={handleUpClick}>Convert to uppercase</button>
    <button className="btn btn-primary mx-1" onClick={handleLowClick}>Convert to Lowercase</button>
    <button className="btn btn-primary mx-1" onClick={handleClrClick}>Clear Text</button>
    <button className="btn btn-primary mx-1" onClick={replacecasefunc}>Replace Text</button>
    <button type="submit" onClick={speak} className="btn btn-warning mx-2 my-2">Speak</button>

    </div>
    <div className="container my-4" style={{color: props.mode ==="dark"?"white":"#3E454C" }}>
      <h3>Your text summary</h3>
      <p >{text.split(" ").length} words, {text.length} characters</p>
      <p>{0.008 * text.split(" ").length} Minutes to read the text</p>
      <h3>Preview</h3>
      <p>{text.length>0?text:"Enter the text to previ"}</p>
    </div>
    </>
  )
}
