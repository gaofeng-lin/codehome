// ./src/store/actions/counter.tsx
import * as types from "../action-types";
export default {
  add(){
    // 需要返回一个action对象
    // type为动作的类型
    return { type: types.ADD}
  },
  subtract(){
    // 需要返回一个action对象
    // type为动作的类型
    return { type: types.SUBTRACT}
  }
}