

export default function Header({counter,color}) {
    return (
      <header className={`flex items-center justify-between p-4 bg-${color}-500 text-gray-50`}>
  
        <h1 className="text-4xl">Magic Ball</h1>
        <p>{counter} question answered</p>
  
      </header>
  
    )
  }