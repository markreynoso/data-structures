'use strict'

let Stack = require('../stack')
let chai = require('chai')
let expect = chai.expect

describe('stack.js tests', function() {
  it('stack should exist', function(){
    let stack = new Stack()
    expect(stack.size()).to.equal(0)
  })
  it('insert 5, pop is 5', function(){
    let stack = new Stack()
    stack.push(5)
    expect(stack.pop()).to.equal(5)
  })
  it('pop after push 6 and 5', function(){
    let stack = new Stack()
    stack.push(6)
    stack.push(5)
    expect(stack.pop()).to.equal(5)
  })
  it('push 0-9, 8th should be 2', function(){
    let stack = new Stack()
    for(let i = 0; i < 10; i++){
      stack.push(i)
    }
    let output
    for(let j = 0; j < 8; j++){
      output = stack.pop()
    }
    expect(output).to.equal(2)
  })
  it('push 5 nums, pop 5 times', function(){
    let stack = new Stack()
    for(let i = 0; i < 5; i++){
      stack.push(i)
    }
    for(let i = 4; i > 5; i--){
      expect(stack.pop()).to.equal(i)
    }
  })
  it('pop empty list returns error', function(){
    let stack = new Stack()
    expect(stack.pop()).to.equal('There are no nodes in this list.')
  })
  it('push iterable', function(){
    let stack = new Stack([0, 1, 2, 3, 4])
    for(let i = 4; i >= 0; i--){
      expect(stack.pop()).to.equal(i)
    }
    expect(stack.pop()).to.equal('There are no nodes in this list.')
  })
})
