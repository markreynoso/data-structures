'use strict'

let Que = require('../que_')
let chai = require('chai')
let expect = chai.expect

describe('q_.js tests', function() {
  it('List should exist, peek is null', function(){
    let q = new Que()
    expect(q.peek()).to.equal(null)
  })
  it('5 enqueue, peek is 5', function(){
    let q = new Que()
    q.enqueue(5)
    expect(q.peek()).to.equal(5)
  })
  it('enqueue two nums, peek is 1st', function(){
    let q = new Que()
    q.enqueue(6)
    q.enqueue(5)
    expect(q.peek()).to.equal(6)
  })
  it('enqueue 0-9, 7th should be 6', function(){
    let q = new Que()
    for(let i = 0; i < 10; i++){
      q.enqueue(i)
    }
    let output
    for(let j = 0; j < 7; j++){
      output = q.dequeue()
    }
    expect(output).to.equal(6)
  })
  it('enqueue 25 nums, size is 25', function(){
    let q = new Que()
    for(let i = 0; i < 25; i++){
      q.enqueue(i)
    }
    expect(q.size()).to.equal(25)
  })
  it('enqueue 25 nums, dequeue 25 times', function(){
    let q = new Que()
    for(let i = 0; i < 25; i++){
      q.enqueue(i)
    }
    for(let i = 0; i < 25; i++){
      expect(q.dequeue()).to.equal(i)
    }
  })
  it('dequeue empty list returns error', function(){
    let q = new Que()
    expect(q.dequeue()).to.equal('This is an empty list. No values to shift.')
  })
  it('initialize queue with iterable', function(){
    let q = new Que([1, 2, 3, 4, 5])
    for(let i = 1; i < 6; i++){
      expect(q.dequeue()).to.equal(i)
    }
  })
})
