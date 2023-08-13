import Head from "next/head"
import { useState } from "react"
import {replies} from '@/data'





export default function Home() {

  const [question, serQuestion ] = useState('no question yet ')
  const [answer, setAnswer] = useState('no answer yet ')


  function submitHandler(event){
    event.preventDefault()
    // alert (event.target.question.value)
    serQuestion(event.target.question.value)
  //  console.log(question)

  const randomNum = Math.floor(Math.random()*replies.length)
  setAnswer(replies[randomNum])
    


  }


  return (
    <>
      <head>
        <title>Home</title>
      </head>
      <body className="flex flex-col min-h-screen">
        {/* Header*/}
        <Header />
        <main className="flex flex-col items-center py-4 space-y-8 flex-grow">
          {/* form */}
          <Form  handler={submitHandler}/>
          {/* question section  */}
          <Question  question={question}/>
          <p>{answer}</p>

        </main>
        <footer className="p-4 mt-8 bg-gray-500 text-gray-50" >
          &copy; ASAC 2023
        </footer>
      </body >

    </>
  )


}

function Header() {
  return (
    <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">

      <h1 className="text-4xl">Magic Ball</h1>
      <p>1 question answered</p>

    </header>

  )
}

function Form(props) {
  return (
    <form className="flex w-1/2 p-2  mx-auto my-4 bg-gray-200" onSubmit={props.handler}>
      <input name='question' className="flex-auto pl-1" />
      <button className="px-2 py-1 bg-gray-500 text-gray-50 " >Ask</button>
    </form>
  )
}

function Question(props) {
  return (
    <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
      <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
        <p className="text-xl text-center">{props.question}</p>
      </div>
    </div>

  )
}


// export default Home;