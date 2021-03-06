import React, {useEffect, useLayoutEffect} from 'react';


export default function App() {
  const [state, setState] = React.useState(0);
  console.log("我是1.0的打印语句");
  useEffect(() => {
    console.log("第一次render时执行");
  }, []);
  useEffect(() => {
    if (state > 0) {
      // console.log("第二次之后render时执行");
      console.log('第 %i 次之后render时执行',state);
    }
  }, [state]);
  useLayoutEffect(() => {
    console.log("我比useEffect先执行");
  });
  console.log("我是2.0的打印语句");
  console.log("我是3.0的打印语句");
  return (
    <div className="App">
      <h1>{state}</h1>
      <button
        onClick={() => {
          setState((x) => x + 1);
        }}
      >
        按钮+1
      </button>
    </div>
  );
}
