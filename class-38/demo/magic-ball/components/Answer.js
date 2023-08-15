
export default function Answer(props) {
  console.log(props.answer)
    return (
      <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
        <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
          {/* short circuts */}
          <p className="text-xl text-center">{props.answer || "waiting ..."}</p> 
        </div>
      </div>
  
    )
  }
  