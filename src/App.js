import NavBar from './components/NavBar';
import TextForm from './components/TextForm';
 //import About from './components/About';

import './App.css';
import { useState } from 'react';

function App() {
  const [mode, setMode]= useState('light');
  const toggleMode =()=>{
    if(mode =='light'){
      setMode('dark')
      document.body.style.backgroundColor ='#3E454C';
    }else{
      setMode('light')
      document.body.style.backgroundColor ='white';
    }
  }
  return (
  <>
<NavBar title="Mr.Word" mode={mode} toggleMode={toggleMode}/>
<div className="container my-3">
<TextForm heading="Enter the text to the Box" mode={mode}/> 
{/*<About/>*/}
</div>

  </>
  );
}

export default App;
