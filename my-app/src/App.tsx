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


// async function getdata() {
//   let data;
//   await axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'}).then(
//     (res)=>{
//       data = res.data;
//     }
//   ) .catch(err=>{
//     console.log(err)
//   });

//   return data;
// }

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


interface isState {
  schema: JSONSchema7,
  formData: JSON

}

const formData = "a";


class App extends React.Component <any, isState> {

  constructor(props:any) {
    super(props);
    this.state = {
      schema:{
        "title": "A registration form",
        "description": "A simple form example.",
        "type": "object",
        "required": [
          "firstName",
          "lastName"
        ],
        "properties": {
          "firstName": {
            "type": "string",
            "title": "First name",
            "default": "Chuck"
          },
          "lastName": {
            "type": "string",
            "title": "Last name"
          },
          "telephone": {
            "type": "string",
            "title": "Telephone",
            "minLength": 10
          }
        }
      },
      formData:{
        "firstName": "A",
        "lastName": "志有",
        "age": 75,
        "bio": "Roundhouse kicking asses since 1940",
        "password": "noneed",
        "telephone": "15308085505"
      }

  
    }

  }

  componentDidMount() {
    axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'}).then((data) => {
      this.setState({schema:data.data});
    })
  }



    onSubmit=()=>{
      axios({
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/octet-stream",
        },
        url: 'http://localhost:8100/api/test',
        method: 'POST',
        data: this.state.schema
      })
    }


    render(){
      return(
        <Form schema = {this.state.schema}  formData={formData}
        >
          <button onClick={this.onSubmit}>计算</button>
        </Form>
      )
    }

}



export default App;
