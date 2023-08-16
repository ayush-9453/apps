import NavBar from './components/NavBar';
import TextForm from './components/TextForm';
 //import About from './components/About';

import './App.css';
function App() {
  return (
  <>
<NavBar title="Mr.Word" aboutText="About Us"/>
<div className="container my-3">
<TextForm heading="Enter the text to the Box"/> 
{/*<About/>*/}
</div>

  </>
  );
}

export default App;
