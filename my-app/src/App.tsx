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
  body: BodyInit

}

const formData = "a";


class App extends React.Component <any, isState> {

  constructor(props:any) {
    super(props);
    this.state = {
      schema:{
        "title": "Test form",
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "age": {
            "type": "number"
          },
          "money": {
            "type": "string"
          }
        }
      },
      body: "hello"
  
    }

  }

  componentDidMount() {
    axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'}).then((data) => {
      this.setState({schema:data.data});
    })
  }




//   onSubmit=()=>{
//     let queryStringRequest = new Request('http://127.0.0.1:8000/api/test', {
//       method: 'post',
//       body: this.state.body
//     })
//     fetch(queryStringRequest).then(res => {
//           console.log(res)
//     })
//  }

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
