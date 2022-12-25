import io from 'socket.io-client';

//建立websocket连接
const socket = io('http://127.0.0.1:3001');

//收到server的连接确认
// socket.on('open', () => {
//     // showTip('socket io is open !');
//     // init();
//     console.log("hello")
// });

socket.emit('sayit', 'wow', data => { 
    console.log(data); // say wow
  });
