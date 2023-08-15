import NavBar from './components/NavBar';
import TextForm from './components/TextForm';

import './App.css';
function App() {
  return (
  <>
<NavBar title="Mr.Panner" aboutText="About Us"/>
<div className="container my-3">
<TextForm heading="Enter the text to the Box"/>
</div>

  </>
  );
}

export default App;
