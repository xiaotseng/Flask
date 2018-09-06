var events=require('events');
var eventEmitter=new events.EventEmitter();
var connectHandler=function (){console.log("连接成功");eventEmitter.emit("data_received");};
eventEmitter.on("data_received",()=>console.log("数据接收成功"));
eventEmitter.on("connection",connectHandler);
eventEmitter.emit("connection");
