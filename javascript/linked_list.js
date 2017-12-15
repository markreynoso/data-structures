'use strict'

class Node {
  constructor(data=null, next=null) {
    this.data = data
    this.next = next
  }
}

class LinkedList {
  constructor(iterable=null) {
    this.head = null
    this._size = 0
    if(Array.isArray(iterable)){
      iterable.forEach(x => this.push(x))
    }
  }

  push(val){
    this.head = new Node(val, this.head)
    this._size ++
  }

  pop(){
    if (this.head === null){
      return 'There are no nodes in this list.'
    }
    let current = this.head
    this.head = current.next
    this._size --
    return current.data
  }

  size(){
    return this._size
  }

  search(val){
    let current = this.head
    while(current){
      if(val === current.data){
        return current
      }
      else{
        current = current.next
        if(current === null){
          return 'This node is not in the linked list.'
        }
      }
    }
  }

  remove(node){
    let current = this.head
    let prev = null
    while(current){
      if(current === node){
        if(current === this.head){
          this.head = current.next
          this._size --
        }
        else{
          if(current.next === null){
            prev.next = null
          }
          else{
            prev.next = current.next
          }
          this._size --
        }
        break
      }
      else{
        prev = current
        current = current.next
      }
    }
    return 'Your node does not exist in this linked list.'
  }

  display(){
    if(this._size > 0){
      let print_list = '('
      let current = this.head
      while(current){
        if(current.next){
          print_list = print_list + current.data + ', '
        }
        else{
          print_list = print_list + current.data + ')'
          return print_list
        }
        current = current.next
      }
    }
    else{
      return '()'
    }
  }
}

module.exports = {LinkedList, Node}
