import React from 'react';
import logo from './logo.svg';
import './App.css';
import Form from "@rjsf/core";
import axios from 'axios';

// const schema: any  = {
//   title: "Test form",
//   type: "object",
//   properties: {
//     name: {
//       type: "string"
//     },
//     age: {
//       type: "number"
//     },
//     money: {
//       type: "string"
//     }
//   }
// };






class App extends React.Component{

  schema: any  = axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'})
  // var tmp = JSON.parse(schema)

  render(){
    return(
      // <Form schema={this.schema} />
      <div>
        {this.schema}
      </div>
  
    )
  }
}


// function App() {
//   return (
//     <div className="App">
//       hello,world
//     </div>
//   );
// }

export default App;
