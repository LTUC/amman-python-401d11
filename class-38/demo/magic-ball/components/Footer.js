import Link from 'next/link';

import React from 'react';

const Footer = ({colorHandler,color}) => {
    return (

        <footer className={`flex justify-between p-4 mt-8 bg-${color}-500 text-gray-50`} >
            <p>&copy; ASAC 2023</p>
            
            <button onClick={()=>colorHandler('orange')}
               className='px-4 py-2 m-2 text-sm font-medium text-white bg-orange-500 border border-transparent rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2'>
                change theme
            </button>

            <button className='p-2 m-1 bg-gray-700'>
                <Link href={'/assets/careers'}>
                    careers
                </Link>
            </button>
        </footer>

    );
}

export default Footer;
