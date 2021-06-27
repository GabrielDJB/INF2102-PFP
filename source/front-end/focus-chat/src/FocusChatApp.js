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



  // ----------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for FocusChatApp class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with relevant properties (initial variables)
  // ----------------------------------------------------------------------------
  constructor(props) {
    // Initializing superclass
    super(props);
    // Setting current state
    this.state = {
      "chatID": "test-chat",
      "chatterID": "test-chatter",
      "categorization": "test-categorization",
      "categories":[
        {"categoryName": "Analysis-1", "categoryDescription": "What do I know or don't know about (all of) you and how?"},
        {"categoryName": "Analysis-2", "categoryDescription": "What do I know or don't know about affected others and how?"},
        {"categoryName": "Analysis-3", "categoryDescription": "What do I know or don't know about the intended (and other anticipated) contexts of use?"},
        {"categoryName": "Analysis-4", "categoryDescription": "What ethical questions can be raised by what I have learned?"},
        {"categoryName": "Design-1", "categoryDescription": "What have I designed for you?"},
        {"categoryName": "Design-2", "categoryDescription": "Which of your goals have I designed the system to support?"},
        {"categoryName": "Design-3", "categoryDescription": "In what situations/contexts do I intend/accept you will use the system to achieve each goal? Why?"},
        {"categoryName": "Design-4", "categoryDescription": "How should you use the system to achieve each goal, according to my design?"},
        {"categoryName": "Design-5", "categoryDescription": "For what purpose do I not want you to use the system?"},
        {"categoryName": "Design-6", "categoryDescription": "What ethical principles influenced my design decisions?"},
        {"categoryName": "Design-7", "categoryDescription": "How is the system I designed for you aligned with those ethical considerations?"},
        {"categoryName": "Implementation-1", "categoryDescription": "How have I built the system to support my design vision?"},
        {"categoryName": "Implementation-2", "categoryDescription": "What have I built into the system to prevent undesirable uses and consequences?"},
        {"categoryName": "Implementation-3", "categoryDescription": "What have I built into the system to help identify and remedy unanticipated effects?"},
        {"categoryName": "Implementation-4", "categoryDescription": "What ethical scenarios have I used to evaluate the system?"},
        {"categoryName": "Evaluation-1", "categoryDescription": "How much of my vision is reflected in the system's actual use?"},
        {"categoryName": "Evaluation-2", "categoryDescription": "What unanticipated uses have been made? By whom? Why?"},
        {"categoryName": "Evaluation-3", "categoryDescription": "What anticipated and unanticipated effects have resulted from its use? Whom do they affect? Why?"},
        {"categoryName": "Evaluation-4", "categoryDescription": "What ethical issues need to be handled through system redesign, redevelopment, policy or even decommisioning?"},
      ],
      "currentCategory": "Analysis-1",
      "messages":[
        {"category":"Category-1", "sender":"Gabriel", "type":"sent"},
        {"category":"Category-2", "sender":"Diniz", "type":"received"},
        {"category":"Category-3", "sender":"Barbosa", "type":"sent"},
      ],
    };
    // Binding methods to allow for state change
    this.changeCategory = this.changeCategory.bind(this)
    this.sendMessage = this.sendMessage.bind(this)
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
      "chatterID": this.state.chatterID,
      "content": content,
      "timestamp": Date.now(),
      "categorizationName": this.state.categorization,
      "categoryName": this.state.currentCategory,
      "replyID": ""
    };
    // Displaying message structure
    console.log(message);
    // Sending message to back-end
    // -- Request code --
  }



  // --------------------------
  // METHOD componentDidMount()
  // 
  // Description:
  //   Method that is called right after the component is built. Useful
  //   for data loading.
  // ---------------------------
  componentDidMount() {
    // Loading initialization data

    // Setting message refresh procedure
    // setInterval(() => console.log("I have been called!"), 10000);
    // fetch("http://127.0.0.1:5000/").then(
    //   response => response.json()
    // ).then(
    //   data => this.setState({"text": data["text"]})
    // )
    
    // Calling rendering method
    this.render();
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
          currentCategory={this.state.currentCategory}
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
