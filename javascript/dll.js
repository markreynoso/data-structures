'use strict'

class Node {
  constructor(data=null, next=null, prev=null) {
    this.data = data
    this.next = next
    this.prev = prev
  }
}

class DoublyLL {
  constructor() {
    this.head = null
    this.tail = null
    this._size = 0
  }

  push(val){
    let new_node = new Node(val)
    if(this._size === 0){
      this.head = new_node
      this.tail = new_node
      this._size ++
    }
    else{
      new_node.next = this.head
      this.head.prev = new_node
      this.head = new_node
      this._size ++
    }
  }

  append(val){
    let new_node = new Node(val)
    if(this._size === 0){
      this.head = new_node
      this.tail = new_node
      this._size ++
    }
    else{
      new_node.prev = this.tail
      this.tail.next = new_node
      this.tail = new_node
      this._size ++
    }
  }

  pop(){
    let current = this.head
    if (this.head === null){
      return 'There are no nodes in this list.'
    }
    else if(this._size === 1){
      this.tail = null
      this.head = null
      this._size --
    }
    else if(this._size > 1){
      this.head = current.next
      this.head.prev = null
      this._size --
    }
    return current.data
  }

  shift(){
    let current = this.tail
    if(this.tail === null){
      return 'This is an empty list. No values to shift.'
    }
    else if(this._size === 1){
      this.tail = null
      this.head = null
      this._size --
    }
    else if(this._size > 1){
      this.tail = current.prev
      this.tail.next = null
      this._size --
    }
    return current.data
  }

  remove(val){
    let current = this.head
    while(current){
      if(current.data === val){
        if(current === this.head){
          this.pop()
        }
        else if(current === this.tail){
          this.shift()
        }
        else{
          current.prev.next = current.next
          current.next.prev = current.prev
          this._size --
        }
        break
      }
      else{
        current = current.next
      }
    }
    return 'Your input value does not exist in this linked list.'
  }
}

module.exports = {DoublyLL, Node}
