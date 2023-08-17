import NavBar from './components/NavBar';
import TextForm from './components/TextForm';
 //import About from './components/About';

import './App.css';
import React ,{ useState } from 'react';
import Alert from './components/Alert';

function App() {
  const [mode, setMode]= useState('light');
  const [alert, setAlert]= useState("hello","null");

  const showAlert =(message, type)=>{
     setAlert({
      msg: message,
      type:type
     })
  }

  const toggleMode =()=>{
    if(mode ==='light'){
      setMode('dark')
      document.body.style.backgroundColor ='#3E454C';
      showAlert("Dark mode has been enabled","success")
    }else{
      setMode('light')
      document.body.style.backgroundColor ='white';
      showAlert("Light mode has been enabled","success")
    }
  }
  return (
  <>
<NavBar title="Mr.Word" mode={mode} toggleMode={toggleMode}/>
 <Alert alert  ={alert} />
 <div className="container my-3">
<TextForm heading="Enter the text to the Box" mode={mode}/> 
{/*<About/>*/}
</div>

  </>
  );
}

export default App;
