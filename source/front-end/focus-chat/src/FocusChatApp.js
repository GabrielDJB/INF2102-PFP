// -------------------------------------------------------------------
// FILE FOCUSCHATAPP.JS
// 
// Author: Gabriel D. J. Barbosa
// 
// Description:
//   File containing React Javascript code for the application's top
//   component. Renders to HTML via front-end Node server.
// -------------------------------------------------------------------

// Loading initial libraries
import React from 'react';
import './FocusChatApp.css';

// Loading components
import Chat from './components/Chat/Chat'
import Categories from './components/Categories/Categories'





// ----------------------------------------------------------------------------------
// CLASS FocusChatApp
//
// Description:
//   Basic class for application. Contains all other relevant components.
//   Top layer for data retrieval and communication.
// 
// Methods:
//   constructor  - Constructs class, using instance properties for configuration;
//   render       - Renders JSX code into HTML, with relevant information;
// ----------------------------------------------------------------------------------
class FocusChatApp extends React.Component {



  // -----------------------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for FocusChatApp class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with properties provided to component (initial variables)
  // -----------------------------------------------------------------------------------------
  constructor(props) {
    // Initializing superclass
    super(props);
    // Setting current state
    this.state = {
      "chatID": "60d7c635e753bbe49edef57a",
      "categorization": "ExtendedMetacommunicationTemplate",
      "categories":[],
      'chatters':{
        '60d7c5d3e753bbe49edef578': 'Joãozinho',
        '60d7c5ede753bbe49edef579': 'Mariazinha'
      },
      "currentCategory": "Analysis-1",
      "currentChatter": "60d7c5d3e753bbe49edef578",
      "messages":[],
    };
    // Binding methods to allow for state change
    this.changeCategory = this.changeCategory.bind(this)
    this.sendMessage = this.sendMessage.bind(this)
    this.componentDidMount = this.componentDidMount.bind(this)
    // Access strings
    // http://localhost:3000/60d8e55aa97777e5636d8365 (Joaozinho)
    // http://localhost:3000/60d8e5caa97777e5636d8366 (Mariazinha)
  }



  // -------------------------------------------------------------------------------------
  // METHOD changeCategory()
  // 
  // Description:
  //   Method that is called by child components to change the current overall category.
  // 
  // Inputs:
  //   newCategory - New current category to be set and filtered down.
  // -------------------------------------------------------------------------------------
  changeCategory(newCategory) {
    // Changing state current category attribute
    var newState = this.state;
    newState.currentCategory = newCategory;
    this.setState(newState);
    // Calling rendering method
    this.render();
  }



  // ---------------------------------------------------------------------
  // ASYNC METHOD fetchCategories()
  //
  // Description:
  //   Asynchronous function for fetching categories and updating state.
  // ---------------------------------------------------------------------
  async fetchCategories(categorizationName) {
    // Fetching categorization's categories through GET request to back end
    fetch("http://127.0.0.1:5000/category/retrieve_categorization/?categorizationName=" + categorizationName, {
      method: 'GET',
    }).then(
      response => {
        // Checking if response is OK and structuring into JSON if so
        if (!response.ok) {
          console.log("There was an error with the categorization fetch request.")
        } else {
          return response.json()
        }
      }
    ).then(
      // Setting categories in the current state
      data => {
        var currState = this.state
        currState['categories'] = data['categories']
        this.setState(currState)
      }
    )
  }



  // ---------------------------------------------------------------------
  // ASYNC METHOD fetchMessages()
  //
  // Description:
  //   Asynchronous function for fetching messages and updating state.
  // ---------------------------------------------------------------------
  async fetchMessages(chatID) {
    // Fetching chat's messages
    fetch("http://127.0.0.1:5000/message/retrieve_chat/?chatID=" + chatID, {
      method: 'GET',
    }).then(
      response => {
        // Checking if response is OK and structuring into JSON if so
        if (!response.ok) {
          console.log("There was an error with the chat messages fetch request.")
        } else {
          return response.json()
        }
      }
    ).then(
      // Setting messages in the current state
      data => {
        var currState = this.state
        currState['messages'] = data['messages']
        this.setState(currState)
      }
    )
  }



  // -------------------------------------------------------------------------------------
  // METHOD sendMessage()
  // 
  // Description:
  //   Method that is called when submitting a message from the ChatInput component.
  // -------------------------------------------------------------------------------------
  sendMessage(content) {
    // Constructing message element
    const message = {
      "chatID": this.state.chatID,
      "chatterID": this.state.currentChatter,
      "content": content,
      "timestamp": Date.now(),
      "categorizationName": this.state.categorization,
      "categoryName": this.state.currentCategory,
      "replyID": ""
    };
    // Displaying message structure
    // console.log(message);
    
    // Sending message to back-end
    fetch('http://127.0.0.1:5000/message/create/', {
      method: 'POST',
      headers: {
        'Accept': 'application/x-www-form-urlencoded',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams(message),
    }).then(
      response => {
        // Checking if response is OK and structuring into JSON if so
        if (!response.ok) {
          console.log("There was an error with the message POST fetch request.")
        } else {
          return response.json()
        }
      }
    ).then(
      // Setting messages in the current state
      data => {
        // console.log(data)
      }
    )
  }



  // ---------------------------------------------------------------------
  // METHOD componentDidMount()
  // 
  // Description:
  //   Method that is called right after the component is built. Useful
  //   for data loading.
  // ---------------------------------------------------------------------
  async componentDidMount() {

    var categorizationName = ''
    var chatID = ''
    var chatterID = ''
    const instanceID = window.location.pathname.substring(1)

    // Loading initialization data
    await fetch("http://127.0.0.1:5000/login/?instanceID=" + instanceID, {
      method: 'GET',
    }).then(
      response => {
        // Checking if response is OK and structuring into JSON if so
        if (!response.ok) {
          console.log("There was an error with the login fetch request.")
        } else {
          return response.json()
        }
      }
    ).then(
      // Setting messages in the current state
      data => {
        // Setting function variables for the rest of function
        categorizationName = data['categorizationName']
        chatID = data['chatID']
        chatterID = data['chatterID']
        // Updating state
        var currState = this.state
        currState['categorization'] = data['categorizationName']
        currState['chatID'] = data['chatID']
        currState['currentChatter'] = data['chatterID']
        this.setState(currState)
      }
    )

    // Fetching the rest of the information
    await this.fetchCategories(categorizationName)
    await this.fetchMessages(chatID)

    // Setting message refresh procedure
    setInterval(() => this.fetchMessages(chatID), 1000);

  }



  // ----------------------------------------------------------------------------
  // METHOD render()
  // 
  // Description:
  //   Render method for FocusChatApp class. Compiles JSX code into HTML (server-side)
  //   for future displays in client-side browsers.
  // ----------------------------------------------------------------------------
  render() {

    return (
      <div className="FocusChatApp">  
        <Chat
          categories={this.state.categories}
          chatters={this.state.chatters}
          currentCategory={this.state.currentCategory}
          currentChatter={this.state.currentChatter}
          categoryChangeHandler={this.changeCategory}
          messages={this.state.messages}
          sendMessageHandler={this.sendMessage}
        />
        <Categories
          categories={this.state.categories}
          currentCategory={this.state.currentCategory}
          categoryChangeHandler={this.changeCategory}
        />
      </div>
    );
  }
}

// Exporting App class
export default FocusChatApp;
