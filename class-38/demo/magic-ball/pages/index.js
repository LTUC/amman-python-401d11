
import Head from "next/head";
import { useState } from "react";
import {replies} from '@/data'

import Header from "@/components/Header";
import Form from "@/components/Form";
import Footer from "@/components/Footer";
import Answer from "@/components/Answer";
import History from "@/components/History";


export default function Home() {

  const [questions, serQuestions ] = useState([])
  const [color,setColor] = useState('gray')
  // const [answer, setAnswer] = useState('waiting ... ')


  function submitHandler(event){
    event.preventDefault()
    // alert (event.target.question.value)
    // serQuestion(event.target.question.value)
  //  console.log(question)

  const randomNum = Math.floor(Math.random()*replies.length)
  // setAnswer(replies[randomNum])
  
  const questionObj={
    id :questions.length +1,
    question : event.target.question.value,
    answer : replies[randomNum]
  }
  
  serQuestions([...questions,questionObj]) // spread operator 
  
  // console.log(questions)
}
const handleAnswer=()=>{
  if(questions.length){
    return questions[questions.length-1].answer
  // }else{
  //   return "waiting ..."
  }
}
// console.log(color)
const colorHandler= (color)=>{
 
  setColor(color)
  // console.log(color)
}


  return (
    <>
      <Head>
        <title>Home</title>
      </Head>
      <div className="flex flex-col min-h-screen">
        {/* Header*/}
        <Header  counter={questions.length} color={color}/>
        <main className="flex flex-col items-center flex-grow py-4 space-y-8">
          {/* form */}
          <Form  handler={submitHandler}/>
          {/* question section  */}
          <Answer  answer={handleAnswer()}/>
      
          <History questions= {questions}/>
        </main>
        <Footer colorHandler={colorHandler} color={color}/>
      
      </div >

    </>
  )


}







// export default Home;