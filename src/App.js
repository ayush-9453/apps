import NavBar from './components/NavBar';
import TextForm from './components/TextForm';
 //import About from './components/About';

import './App.css';
import { useState } from 'react';

function App() {
  const [mode, setMode]= useState("light");
  const toggleMode =()=>{
    if(mode =='dark'){
      setMode('light')
    }else{
      setMode('dark')
    }
  }
  return (
  <>
<NavBar title="Mr.Word" mode={mode} toggleMode={toggleMode}/>
<div className="container my-3">
<TextForm heading="Enter the text to the Box"/> 
{/*<About/>*/}
</div>

  </>
  );
}

export default App;
