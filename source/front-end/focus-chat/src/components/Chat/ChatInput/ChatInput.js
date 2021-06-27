// -------------------------------------------------------------------
// FILE CHATINPUT.JS
// 
// Author: Gabriel D. J. Barbosa
// 
// Description:
//   File containing the class for the ChatInput section of the user
//   interface. Its parent is the general FocusChatApp class.
// -------------------------------------------------------------------

// Loading initial libraries
import React from 'react';
import './ChatInput.css'

import {FormControl, Select, TextField, MenuItem, InputLabel} from '@material-ui/core';

// ----------------------------------------------------------------------------------
// CLASS ChatInput
//
// Description:
//   Class for the ChatInput section of the user interface. Allows for the selection
//   of ChatInput to be attributed to the sent messages.
// 
// Methods:
//   constructor  - Constructs class, using instance properties for configuration;
//   render       - Renders JSX code into HTML, with relevant information;
// ----------------------------------------------------------------------------------
class ChatInput extends React.Component {

  // ----------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for ChatInput class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with relevant properties (initial variables)
  // ----------------------------------------------------------------------------
  constructor(props) {
    
    // Creating component
    super(props);
    
    // Defines state variables
    this.state = {
      "categories": this.props.categories,
      "message": "",
    };

    // Binding methods
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

  }



  // ----------------------------------------------------------------------------
  // METHOD handleChange()
  // 
  // Description:
  //   Method for handling TextInput changes.
  // 
  // Inputs:
  //   event - Reference to the event that triggered handler.
  // ----------------------------------------------------------------------------
  handleChange(event){
    // Updating message value in component state
    var newState = this.state;
    newState.message = event.target.value;
    this.setState(newState);
  }



  // ----------------------------------------------------------------------------
  // METHOD handleChange()
  // 
  // Description:
  //   Method for handling form submition.
  // 
  // Inputs:
  //   event - Reference to the event that triggered handler.
  // ----------------------------------------------------------------------------
  handleSubmit(event){
    // Stopping page refresh
    event.preventDefault();
    // Submitting message data
    this.props.sendMessageHandler("Message submitted: " + this.state.message);
    // Resetting message input content
    var newState = this.state;
    newState.message = "";
    this.setState(newState);
  }



  // ---------------------------------------------------------------------------------
  // METHOD render()
  // 
  // Description:
  //   Render method for ChatInput class. Compiles JSX code into HTML (server-side)
  //   for future displays in client-side browsers.
  // ---------------------------------------------------------------------------------
  render() {

    // Creating reference for event handlers
    const changeCategory = this.props.categoryChangeHandler

    // Returning JSX elements
    return (
      <div className="ChatInput">
        <div id="message-input" className="message-input">
          
          <Select id="message-input-select" className="message-input-select" labelId="message-input-select-label" value={this.props.currentCategory} placeholder={this.props.currentCategory} variant="outlined">
            {this.state.categories.map((value, index) => {
              return <MenuItem value={value.categoryName} onClick={(e) => changeCategory(value.categoryName, e)}>{value.categoryName}</MenuItem>
            })}
          </Select>

          <form className="message-input-text-wrapper" onSubmit={this.handleSubmit}>
            <TextField id="message-input-text" className="message-input-text" label="Mensagem" onChange={this.handleChange} value={this.state.message} variant="outlined"/>
          </form>
          
        </div>
      </div>
    );
  }

}

// Exporting ChatInput class
export default ChatInput;