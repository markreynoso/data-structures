'use strict'

let linkedList = require('../linked_list')
let chai = require('chai')
let expect = chai.expect

describe('linked_list.js tests', function() {
  it('List should exist', function(){
    let ll = new linkedList.LinkedList()
    expect(ll.head).to.equal(null)
  })
  it('head is 5', function(){
    let ll = new linkedList.LinkedList()
    ll.push(5)
    expect(ll.head.data).to.equal(5)
  })
  it('next from head is 6', function(){
    let ll = new linkedList.LinkedList()
    ll.push(6)
    ll.push(5)
    expect(ll.head.next.data).to.equal(6)
  })
  it('push 0-9, 8th should be 2', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 10; i++){
      ll.push(i)
    }
    let output = ll.head
    for(let j = 0; j < 7; j++){
      output = output.next
    }
    expect(output.data).to.equal(2)
  })
  it('push 5, pop 5', function(){
    let ll = new linkedList.LinkedList()
    ll.push(5)
    let output = ll.pop()
    expect(output).to.equal(5)
  })
  it('push 5 nums, pop 5 times', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 5; i++){
      ll.push(i)
    }
    for(let i = 4; i > 5; i--){
      let output
      expect(output).to.equal(i)
    }
  })
  it('pop empty list returns error', function(){
    let ll = new linkedList.LinkedList()
    expect(ll.pop()).to.equal('There are no nodes in this list.')
  })
  it('push 5 nums, size is 5', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 5; i++){
      ll.push(i)
    }
    expect(ll.size()).to.equal(5)
  })
  it('push 25, search 10', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 25; i++){
      ll.push(i)
    }
    let output = ll.search(10)
    expect(output.data).to.equal(10)
  })
  it('push 25, search 100', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 25; i++){
      ll.push(i)
    }
    let output = ll.search(100)
    expect(output).to.equal('This node is not in the linked list.')
  })
  it('push 5 nums, remove 4', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 5; i++){
      ll.push(i)
    }
    let output = ll.search(4)
    ll.remove(output)
    expect(ll.head.data).to.equal(3)
  })
  it('push 5 nums, remove all', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 5; i++){
      ll.push(i)
    }
    for(let i = 0; i < 5; i++){
      let output = ll.search(i)
      ll.remove(output)
    }
    expect(ll.size()).to.equal(0)
  })
  it('push 5 nums, remove 3, seach 3', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 5; i++){
      ll.push(i)
    }
    let output = ll.search(3)
    ll.remove(output)
    expect(ll.search(3)).to.equal('This node is not in the linked list.')
  })
  it('push 5 nums, display', function(){
    let ll = new linkedList.LinkedList()
    for(let i = 0; i < 5; i++){
      ll.push(i)
    }
    let output = ll.display()
    expect(output).to.equal('(4, 3, 2, 1, 0)')
  })
  it('push 5 nums, display', function(){
    let ll = new linkedList.LinkedList()
    let output = ll.display()
    expect(output).to.equal('()')
  })
})
