// -------------------------------------------------------------------
// FILE CHATDISPLAY.JS
// 
// Author: Gabriel D. J. Barbosa
// 
// Description:
//   File containing the class for the ChatDisplay section of the user
//   interface. Its parent is the general FocusChatApp class.
// -------------------------------------------------------------------

// Loading initial libraries
import React, { useDebugValue } from 'react';
import './ChatDisplay.css'

// Importing components
import ChatMessage from './ChatMessage/ChatMessage';

// Importing Material-UI components
import {Card, CardContent, Typography} from '@material-ui/core';

// ----------------------------------------------------------------------------------
// CLASS ChatDisplay
//
// Description:
//   Class for the ChatDisplay section of the user interface. Allows for the selection
//   of ChatDisplay to be attributed to the sent messages.
// 
// Methods:
//   constructor  - Constructs class, using instance properties for configuration;
//   render       - Renders JSX code into HTML, with relevant information;
// ----------------------------------------------------------------------------------
class ChatDisplay extends React.Component {

  // ----------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for ChatDisplay class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with relevant properties (initial variables)
  // ----------------------------------------------------------------------------
  constructor(props) {
      super(props);
      this.state = {
        "messages": this.props.messages,
      };
  }

  // ---------------------------------------------------------------------------------
  // METHOD render()
  // 
  // Description:
  //   Render method for ChatDisplay class. Compiles JSX code into HTML (server-side)
  //   for future displays in client-side browsers.
  // ---------------------------------------------------------------------------------
  render() {
    return (
      <div className="ChatDisplay">
        {this.state.messages.map((value, index) => {
          return <ChatMessage category={value.category} sender={value.sender} type={value.type} />
        })}
      </div>
    );
  }

}

// Exporting ChatDisplay class
export default ChatDisplay;