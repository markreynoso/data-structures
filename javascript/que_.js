'use strict'

const dLL = require('./dll')

class Queue {
  constructor(iterable=null){
    this.func = new dLL.DoublyLL()
    if(Array.isArray(iterable)){
      iterable.map(x => this.enqueue(x));
    }
  }

  enqueue(val){
    return this.func.push(val)
  }

  dequeue(){
    return this.func.shift()
  }

  peek(){
    if (this.func.tail){
      return this.func.tail.data
    }
    else{
      return null
    }
  }

  size(){
    return this.func._size
  }
}

module.exports = Queue
