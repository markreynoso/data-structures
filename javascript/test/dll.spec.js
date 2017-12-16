'use strict'

let dLL = require('../dll')
let chai = require('chai')
let expect = chai.expect

describe('dll.js tests', function() {
  it('List should exist', function(){
    let dll = new dLL.DoublyLL()
    expect(dll.head).to.equal(null)
  })
  it('head is 5', function(){
    let dll = new dLL.DoublyLL()
    dll.push(5)
    expect(dll.head.data).to.equal(5)
    expect(dll.tail.data).to.equal(5)
  })
  it('next from head is 6, tail is 5', function(){
    let dll = new dLL.DoublyLL()
    dll.push(6)
    dll.push(5)
    expect(dll.head.next.data).to.equal(6)
    expect(dll.tail.data).to.equal(6)
  })
  it('append 5, head is 5, tail is 5', function(){
    let dll = new dLL.DoublyLL()
    dll.append(5)
    expect(dll.head.data).to.equal(5)
    expect(dll.tail.data).to.equal(5)
  })
  it('push 0-9, 8th should be 2', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 10; i++){
      dll.push(i)
    }
    let output = dll.head
    for(let j = 0; j < 7; j++){
      output = output.next
    }
    expect(output.data).to.equal(2)
    expect(output.prev.data).to.equal(3)
  })
  it('push 5, pop 5', function(){
    let ll = new dLL.DoublyLL()
    ll.push(5)
    let output = ll.pop()
    expect(output).to.equal(5)
  })
  it('push 5 nums, pop 5 times', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 5; i++){
      dll.push(i)
    }
    for(let i = 4; i > 5; i--){
      expect(dll.pop()).to.equal(i)
    }
  })
  it('append 5 nums, pop 5 times', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 5; i++){
      dll.append(i)
    }
    for(let i = 0; i < 5; i++){
      expect(dll.pop()).to.equal(i)
    }
  })
  it('pop empty list returns error', function(){
    let dll = new dLL.DoublyLL()
    expect(dll.pop()).to.equal('There are no nodes in this list.')
  })
  it('push 5 nums, size is 5', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 5; i++){
      dll.append(i)
    }
    expect(dll._size).to.equal(5)
  })
  it('push 5 nums, shift 5 times', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 5; i++){
      dll.push(i)
    }
    for(let i = 0; i < 5; i++){
      expect(dll.shift()).to.equal(i)
    }
  })
  it('push 5 nums, remove 4', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 5; i++){
      dll.push(i)
    }
    expect(dll.head.data).to.equal(4)
    dll.remove(4)
    expect(dll.head.data).to.equal(3)
  })
  it('push 5 nums, remove all', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 5; i++){
      dll.push(i)
    }
    for(let i = 0; i < 5; i++){
      dll.remove(i)
    }
    expect(dll._size).to.equal(0)
  })
  it('push 5 nums, remove 3 two times error', function(){
    let dll = new dLL.DoublyLL()
    for(let i = 0; i < 5; i++){
      dll.push(i)
    }
    dll.remove(3)
    expect(dll.remove(3)).to.equal('Your input value does not exist in this linked list.')
  })
})
