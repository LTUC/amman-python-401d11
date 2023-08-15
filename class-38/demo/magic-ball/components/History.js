import React from 'react';

const History = ({questions}) => {
    console.log(questions)
    return (
       <>
       { questions.length > 0 ?(
        
       <table className='w-1/2 mx-auto my-8 text-xl center'>
        <thead>
            <tr key="">
                <th className='border border-black '>No</th>
                <th className='border border-black ' >Question</th>
                <th className='border border-black ' >Answer</th>

            </tr>
        </thead>
        {/* table body */}
        <tbody>
            {questions.map(obj =>(
                <tr key={obj.id}>
                    <td className='border border-black '>{obj.id}</td>
                    <td className='border border-black '>{obj.question}</td>
                    <td className='border border-black '>{obj.answer}</td>

                </tr>
            ))}
        </tbody>
       </table>
       ) : null
       }
       </>
    );
}

export default History;
