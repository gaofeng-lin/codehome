import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Form from "@rjsf/core";
// import JSONSchema7 from "json-schema";

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);


// const Form = JSONSchemaForm.default;
// const schema = {
//   title: "Test form",
//   type: "string"
// };



const schema: any  = {
  title: "Test form",
  type: "object",
  properties: {
    name: {
      type: "string"
    },
    age: {
      type: "number"
    },
    money: {
      type: "string"
    }
  }
};

root.render(
  <React.StrictMode>
    {/* <Form schema={schema} /> */}
    <App></App>
  </React.StrictMode>
);



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
