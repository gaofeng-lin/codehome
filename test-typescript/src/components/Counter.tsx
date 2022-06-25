// ./src/components/Counter.tsx
// import React from "react"; // 之前的写法
// 在ts中引入的写法
import * as React from "react";


interface IProps {
    name: string,
}

interface IState {
    number: number,
}


export default class CounterComponent extends React.Component <IProps, IState> {
  // 状态state
  state = {
    number:0
  }
  render(){
    return(
      <div>
        <p>{this.state.number}</p>
        <p>{this.props.name}</p>
        <button onClick={()=>this.setState({number:this.state.number + 1})}>+</button>
      </div>
    )
  }
}