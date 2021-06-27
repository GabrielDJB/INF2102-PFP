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

    // Defining constants and variables
    const currentChatter = this.props.currentChatter
    const chatters = this.props.chatters
    var messages = this.props.messages

    // Determining type of message and changing determining chatterName
    messages.map((value, index) => {
      // Determining whether message was sent or received
      if(value.chatterID == currentChatter) {
        value['type'] = 'sent'
      } else {
        value['type'] = 'received'
      }
      // Determining chatterName
      value['chatterName'] = chatters[value['chatterID']]
      // Converting to message time HH:MM
      const currDate = new Date(parseInt(value['timestamp']))
      value['currentTime'] = currDate.getHours() + ':' + currDate.getMinutes()
    })

    // Returning JSX to be rendered
    return (
      <div className="ChatDisplay">
        {messages.map((value, index) => {
          return <ChatMessage category={value.categoryName} content={value.content} sender={value.chatterName} timestamp={value.currentTime} type={value.type} />
        })}
      </div>
    );
  }

}

// Exporting ChatDisplay class
export default ChatDisplay;