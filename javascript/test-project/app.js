import {createRequire} from 'module';
const require = createRequire(import.meta.url);
const koa = require('koa')
const app = new koa()
const server = require('http').createServer(app.callback())
const io = require('socket.io')(server)

//监听connect事件
io.on('connection', socket => {
//   socket.emit('open');//通知客户端已连接
//   console.log('connected');
socket.on('sayit', (word, callback)=> {
    callback('say123 ' + word);
  });
  
  //监听disconnect事件
  socket.on('disconnect', () => {
    console.log('disconnect')
  });
});
server.listen(3001);

