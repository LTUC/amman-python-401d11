import Head from "next/head"

import { useAuth } from "@/contexts/auth"

export default function Home() {

  // const user = null
  // const user = {
  //   username: "Rania",
  //   password: "123"
  // }
  const {login, user,logout}= useAuth() // destructuring 

  return (
   <div>
    <Head>
      <title>cookie stand demo</title>
    </Head>
    <main className="p-4 space-y-8 text-center">
     <h1 className = "text-4xl">Fetching data from Authenticated API</h1>
     
     { user ? (
      <>
     <h2>welcome {user.username} your email is : {user.email} and your id is :  {user.id}</h2>
     <button className="p-2 text-white bg-gray-500 rounded" onClick={()=>logout()}>Logout</button>
      </>
     ) : 
     (<>
     <h2>needs to login</h2>
     <button className="p-2 text-white bg-gray-500 rounded" onClick={()=>login("elon","123456elon")}>Login</button>
     </>
     )
      
     }
    </main>
   </div>
  )
}