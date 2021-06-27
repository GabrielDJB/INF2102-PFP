// -------------------------------------------------------------------
// FILE CATEGORIES.JS
// 
// Author: Gabriel D. J. Barbosa
// 
// Description:
//   File containing the class for the categories section of the user
//   interface. Its parent is the general FocusChatApp class.
// -------------------------------------------------------------------

// Loading initial libraries
import React from 'react';
import './Categories.css'

// Importing Material-UI components
import {List, ListItem, Typography} from '@material-ui/core';

// ----------------------------------------------------------------------------------
// CLASS Categories
//
// Description:
//   Class for the Categories section of the user interface. Allows for the selection
//   of categories to be attributed to the sent messages.
// 
// Methods:
//   constructor  - Constructs class, using instance properties for configuration;
//   render       - Renders JSX code into HTML, with relevant information;
// ----------------------------------------------------------------------------------
class Categories extends React.Component {

  // ----------------------------------------------------------------------------
  // METHOD constructor()
  // 
  // Description:
  //   Constructor method for Categories class. Instantiates class and defines
  //   initial state and available properties.
  // 
  // Inputs:
  //   props - Dictionary (object) with relevant properties (initial variables)
  // ----------------------------------------------------------------------------
  constructor(props) {
      super(props);
      this.state = {
        "categories": this.props.categories,
      };
  }

  // ---------------------------------------------------------------------------------
  // METHOD render()
  // 
  // Description:
  //   Render method for Categories class. Compiles JSX code into HTML (server-side)
  //   for future displays in client-side browsers.
  // ---------------------------------------------------------------------------------
  render() {
    
    // Creating reference to event handlers
    const currentCategory = this.props.categoryChangeHandler

    // Returning JSX elements
    return (
      <div className="Categories">
        <Typography className="category-title" variant="h4">Categories</Typography>
        <List className="category-list">
          {this.state.categories.map((value, index) => {
            // Checking whether the option is the currently selected one
            if(value.categoryName == this.props.currentCategory){
              return <ListItem button className="category-list-item selected" onClick={(e) => currentCategory(value.categoryName)}>[{value.categoryName}]: {value.categoryDescription}</ListItem>
            // Returning regular option button otherwise
            } else {
              return <ListItem button className="category-list-item" onClick={(e) => currentCategory(value.categoryName)}>[{value.categoryName}]: {value.categoryDescription}</ListItem>
            }
          })}
        </List>
      </div>
    );
  }

}

// Exporting Categories class
export default Categories;