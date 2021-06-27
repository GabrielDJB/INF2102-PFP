// -------------------------------------------------------------------
// FILE CHATMESSAGE.JS
// 
// Author: Gabriel D. J. Barbosa
// 
// Description:
//   File containing the class for the ChatMessage section of the user
//   interface. Its parent is the general FocusChatApp class.
// -------------------------------------------------------------------

// Loading initial libraries
import React from 'react';
import './ChatMessage.css'

// Importing Material-UI components
import {Card, CardContent, Typography} from '@material-ui/core';

// ----------------------------------------------------------------------------------
// CLASS ChatMessage
//
// Description:
//   Class for the ChatMessage section of the user interface. Allows for the selection
//   of ChatMessage to be attributed to the sent messages.
// 
// Methods:
//   constructor  - Constructs class, using instance properties for configuration;
//   render       - Renders JSX code into HTML, with relevant information;
// ----------------------------------------------------------------------------------
class ChatMessage extends React.Component {

  // ----------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for ChatMessage class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with relevant properties (initial variables)
  // ----------------------------------------------------------------------------
  constructor(props) {
      super(props);
      this.state = {
        "category": props.category,
        "sender": props.sender,
        "timestamp": props.timestamp,
        "type": props.type,
      };
  }

  // ---------------------------------------------------------------------------------
  // METHOD render()
  // 
  // Description:
  //   Render method for ChatMessage class. Compiles JSX code into HTML (server-side)
  //   for future displays in client-side browsers.
  // ---------------------------------------------------------------------------------
  render() {
    return (
      <div className={"message-display-area ".concat(this.props.type)}>
          <Card className={"message-card ".concat(this.props.type)}>
          <CardContent className="message-card-wrapper">
              <div className="message-card-header"><i>{this.props.category}</i> - <i>{this.props.sender}</i></div>
              <div className="message-card-content">{this.props.content}</div>
              <div className="message-card-footer">{this.props.timestamp}</div>
          </CardContent>
          </Card>
      </div>
    );
  }

}

// Exporting ChatMessage class
export default ChatMessage;