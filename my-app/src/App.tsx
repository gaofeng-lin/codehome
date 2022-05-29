import React from 'react';
import logo from './logo.svg';
import './App.css';
import Form from "@rjsf/core";
import axios from 'axios';
import { JSONSchema7 } from "json-schema";






interface isState {
  schema: JSONSchema7
}




const schema = {
  "type": "object",
  "properties": {
    "湍流模型": {
      "type": "string"
    },
    "粘性控制": {
      "type": "string"
    },
    "最大迭代步数": {
      "type": "number"
    }
  }
};
const onSubmit = ({formData} ) => {
  axios({
    headers: {
      "Content-Type": "application/octet-stream",
      "Access-Control-Allow-Origin": "*",
    },
    url: 'http://127.0.0.1:8100/api/test',
    method: 'POST',
    data: formData
  })
}


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
      }
    }

  }

  componentDidMount() {
    axios({url:'https://63cc3e21-7c75-4507-8414-11dde227bc60.mock.pstmn.io/test'}).then((data) => {
      this.setState({schema:data.data});
    })
  }


    render(){
      return(
  <Form schema={schema as JSONSchema7}
        onSubmit={onSubmit} />
      )
    }

}



export default App;
