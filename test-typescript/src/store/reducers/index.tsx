// ./src/store/reducers/index.tsx
// 导入类型校验的接口
// 用来约束state的
import { Store } from "../../types/index"
// 我们需要给number赋予默认值
let initState:Store = { number:0 }
// 把接口写在state:Store
export default function (state:Store=initState,action) {
  // 拿到老的状态state和新的状态action
  // action是一个动作行为，而这个动作行为，在计数器中是具备 加 或 减 两个功能
}