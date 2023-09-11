import Head from "next/head"

import { useAuth } from "@/contexts/auth"
import useResource from "@/hooks/useResource"

export default function Home() {

  // const user = null
  // const user = {
  //   username: "Rania",
  //   password: "123"
  // }
  const {login, user,logout}= useAuth() // destructuring 
  const {response,createResource,deleteResource} = useResource()

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
     <CreateCooki  createResource={createResource}/>
     <CookiesList response={response} handleDelete={deleteResource}/>
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

function CookiesList({response,handleDelete}){
  {response && console.log(response)}
  return (
    <>
    {response && response.map(item=>{
      return(
        <>
        <span><li key={item.id}> {item.location}</li></span><span onClick={()=>handleDelete(item.id)}> [ x ] </span>
        </>
      )
    })}
    
    </>
  )
}
function CreateCooki({createResource}){

  function handleSubmit(e){
    e.preventDefault()
    const newLocation={
      location :e.target.location.value,
      minimum_customers_per_hour : e.target.min.value,
      maximum_customers_per_hour:e.target.max.value,
      average_cookies_per_sale:e.target.avg.value
    }
    
    createResource(newLocation)
  }
  

  return (
  <form onSubmit={handleSubmit}>
    <input className="border border-black" type="text" name="location" placeholder="add location" />
    <input className="border border-black" type="text" name="min" placeholder="add min" />
    <input className="border border-black" type="text" name="max" placeholder="add max" />
    <input className="border border-black" type="text" name="avg" placeholder="add avg" />
    <button  className="p-2 text-white bg-gray-500 rounded "> Create</button>

  </form>
    
  )
  
}