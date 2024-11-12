"use client"
import { useState,useEffect } from "react"
export default function Home(){

  const [name, setName]= useState("Muhammad Ibrahim Mubashir")
  const [age, setAge]= useState("14")
  const [count, setCount]= useState(0)
  const [count2, setCount2]= useState(0)


  useEffect(()=>{
    console.log("1")
  },[])

  //useEffect(()=>{
  //  console.log("2")
  //},[count])

  useEffect(()=>{
    console.log("3")
  },[count,count2])


  const changeName = ()=>{
    setName("Ratan Lal")
    setAge("20")
  }

  return(
    <div>
      <h3>Route Group</h3>
      <h2>use state</h2>
      <h3>React Hook</h3>
      <br/>
      <p>{name} is {age} years old.</p>
      <button onClick={changeName}>Click Button</button>
      <br/>
      <button onClick={()=>setCount(count2+1)}>Counter 1 = {count}</button>
      <br/>
      <button onClick={()=>setCount2(count2+1)}>Counter 2 = {count2}</button>

    </div>
  )
}
