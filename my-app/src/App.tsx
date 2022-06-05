import React from 'react';
import './App.css';
import Form from "@rjsf/core";
import axios from 'axios';
import { JSONSchema7 } from "json-schema";




interface isState {
  schema: JSONSchema7
}




// const schema = {
//   "type": "object",
//   "properties": {
//     "湍流模型": {
//       "type": "string"
//     },
//     "粘性控制": {
//       "type": "string"
//     },
//     "最大迭代步数": {
//       "type": "number"
//     }
//   }
// };
const onSubmit = ({formData}) => {

  // var jsonobj = JSON.parse(formData);
  console.log(formData)

  var obj = {'properties':''};
  obj.properties = formData;
  console.log(obj)

  axios({
    headers: {
      "Content-Type": "application/octet-stream",
      "Access-Control-Allow-Origin": "*",
    },
    url: 'http://127.0.0.1:8100/api/test',
    method: 'POST',
    data: obj
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
          "name123": {
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

  // componentDidMount() {
  //   axios({url:'http://localhost:5000/api/v1/books'}).then((data) => {
  //     console.log(data.data);
  //     this.setState({schema:data.data});
  //   })
  // }


    render(){
      return(
  <Form schema={this.state.schema as JSONSchema7}
        onSubmit={onSubmit} />
      )
    }

}



export default App;
