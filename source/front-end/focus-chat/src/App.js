// -------------------------------------------------------------------
// FILE APP.JS
// 
// Author: Gabriel D. J. Barbosa
// 
// Description:
//   File containing React Javascript code for the application's top
//   component. Renders to HTML via front-end Node server.
// -------------------------------------------------------------------

// Loading initial libraries
import React from 'react';
import ReactDom from 'react-dom';
import logo from './logo.svg';
import './App.css';


// ----------------------------------------------------------------------------------
// CLASS App
//
// Description:
//   Basic class for application. Contains all other relevant components.
//   Top layer for data retrieval and communication.
// 
// Methods:
//   constructor  - Constructs class, using instance properties for configuration;
//   render       - Renders JSX code into HTML, with relevant information;
// ----------------------------------------------------------------------------------
class App extends React.Component {

  // ----------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for App class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with relevant properties (initial variables)
  // ----------------------------------------------------------------------------
  constructor(props) {
    super(props);

    this.state = {
      "text": "Test Text 2"
    };
  }

  // --------------------------
  // METHOD componentDidMount()
  // 
  // Description:
  //   Method that is called right after the component is built. Useful
  //   for data loading.
  // ---------------------------
  componentDidMount() {
    
    // Fetching information from database
    fetch("http://127.0.0.1:5000/").then(
      response => response.json()
    ).then(
      data => this.setState({"text": data["text"]})
    )
    
    this.render(); // Call for render method, re-configuring displayed information
  }

  // ----------------------------------------------------------------------------
  // METHOD render()
  // 
  // Description:
  //   Render method for App class. Compiles JSX code into HTML (server-side)
  //   for future displays in client-side browsers.
  // ----------------------------------------------------------------------------
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {this.state.text}
          </p>
          <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
            Learn React
          </a>
        </header>
      </div>
    );
  }

}

// Exporting App class
export default App;
