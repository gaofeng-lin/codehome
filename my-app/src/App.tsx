import React from 'react';
import logo from './logo.svg';
import './App.css';
import Form from "@rjsf/core";
import axios from 'axios';
import { JSONSchema7 } from "json-schema";



// const schema = {
//   "title": "Test form",
//   "type": "object",
//   "properties": {
//     "name": {
//       "type": "string"
//     },
//     "age": {
//       "type": "number"
//     },
//     "money": {
//       "type": "string"
//     }
//   }
// };


async function getdata() {
  let data;
  await axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'}).then(
    (res)=>{
      data = res.data;
    }
  ) .catch(err=>{
    console.log(err)
  });

  return data;
}

// const schema = {
//   "title": "Test form",
//   "type": "object",
//   "properties": {
//     "name": {
//       "type": "string"
//     },
//     "age": {
//       "type": "number"
//     },
//     "money": {
//       "type": "string"
//     }
//   }
// };





class App extends React.Component{

  // schema = axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'})
  // var tmp = JSON.parse(schema)


  // render(){


  //   return(
  //     <Form schema = { axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'}).then(
  //       (res)=>{
  //         console.log(res.data)
  //         return res.data
  //       }
  //     ) .catch(err=>{
  //       console.log(err)
  //     }) as JSONSchema7}  />
  //   )
  // }

    render(){
      return(
        <Form schema = {getdata().then(res =>{
            return res
        }) as JSONSchema7}
        ></Form>
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
