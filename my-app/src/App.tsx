import React from 'react';
import logo from './logo.svg';
import './App.css';
import Form from "@rjsf/core";
import axios from 'axios';
import { JSONSchema7 } from "json-schema";






interface isState {
  schema: JSONSchema7,
  formData: JSON

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
  console.log("Data submitted: ",  formData);
}

class App extends React.Component <any, isState> {



    render(){
      return(
  <Form schema={schema as JSONSchema7}
        onSubmit={onSubmit} />
      )
    }

}



export default App;
