export default function Item(){
    return<>
    

<div className="w-full max-w-xs">
   

    <a href="#">
        <img className="rounded-t-lg" src="https://flowbite.com/docs/images/blog/image-1.jpg" alt="" />
    </a>
    <div className="flex flex-row bg-[#F2F2F2]">
    

        <div className="flex-col ">
            <div className="p-5">
            <a href="#">
                <h5 className=" text-xlfont-bold tracking-tight text-gray-900 dark:text-black">Item name With Link</h5>
            </a>
            <div className="row">

                <small className="ms-2 font-semibold text-gray-500 dark:text-gray-400">Item code</small>
            </div>
            
            <div className="row">
                <small className="ms-2 font-semibold text-gray-500 dark:text-gray-400">$10</small>
            </div>

             <div className="row">
                <small className="ms-2 font-semibold text-gray-500 dark:text-gray-400">Item color options  +</small>
            </div>
            
            <span>  </span>
            
            

        </div>
        
        </div>
        <div className=" flex justify-center h-40 flex-col ">

                <a href="#" className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Cart
                        <svg className="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                    </svg>
                </a>

        </div>

    </div>
   
</div>



{/* </div> */}

    
    
    </>
}