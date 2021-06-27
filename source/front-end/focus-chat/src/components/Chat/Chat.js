// -------------------------------------------------------------------
// FILE CHAT.JS
// 
// Author: Gabriel D. J. Barbosa
// 
// Description:
//   File containing the class for the chat section of the user
//   interface. Its parent is the general FocusChatApp class.
// -------------------------------------------------------------------

// Loading initial libraries
import React from 'react';
import './Chat.css'

// Loading components
import ChatDisplay from './ChatDisplay/ChatDisplay';
import ChatInput from './ChatInput/ChatInput';

// ----------------------------------------------------------------------------------
// CLASS Chat
//
// Description:
//   Class for the Chat section of the user interface. Allows for the selection
//   of Chat to be attributed to the sent messages.
// 
// Methods:
//   constructor  - Constructs class, using instance properties for configuration;
//   render       - Renders JSX code into HTML, with relevant information;
// ----------------------------------------------------------------------------------
class Chat extends React.Component {

  // ----------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for Chat class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with relevant properties (initial variables)
  // ----------------------------------------------------------------------------
  constructor(props) {
      super(props);
      this.state = {
        "categories": this.props.categories,
        "chatters": this.props.chatters,
        "currentChatter": this.props.currentChatter,
        "messages": this.props.messages,
      };
  }

  // ---------------------------------------------------------------------------------
  // METHOD render()
  // 
  // Description:
  //   Render method for Chat class. Compiles JSX code into HTML (server-side)
  //   for future displays in client-side browsers.
  // ---------------------------------------------------------------------------------
  render() {
    return (
      <div className="Chat">
          <ChatDisplay
            chatters={this.props.chatters}
            currentChatter = {this.props.currentChatter}
            messages={this.props.messages}
          />
          <ChatInput
            categories={this.props.categories}
            currentCategory={this.props.currentCategory}
            categoryChangeHandler={this.props.categoryChangeHandler}
            sendMessageHandler={this.props.sendMessageHandler}
          />
      </div>
    );
  }

}

// Exporting Chat class
export default Chat;