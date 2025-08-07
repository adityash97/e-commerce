import {ProductType} from "./models"

export default function Item({title,price , description, category, image}:ProductType){
    return<>
    
        <div className="max-w-xs bg-white border border-solid rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700 m-3 h-[350px] flex flex-col">
        <figure className="flex justify-center">
            <img className="w-48 h-48 object-contain rounded-lg" src={image} alt="image description" />
        </figure>

        <div className="flex flex-row bg-[#F2F2F2] flex-1">
            <div className="flex flex-col flex-1 p-5 overflow-hidden">
            <h5 className="text-xl font-bold tracking-tight text-gray-900 dark:text-black line-clamp-1">{title}</h5>
            <small className="ms-2 font-semibold text-gray-500 dark:text-gray-400">${price}</small>
            <small className="text-sm text-gray-500 line-clamp-3">{description}</small>
            </div>

            <div className="flex justify-between flex-col p-2">
            <span className="bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-sm dark:bg-blue-900 dark:text-blue-300 whitespace-nowrap">
                {category}
            </span>
            <a href="#" className="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4">
                Cart
                 <svg className="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                    </svg>
            </a>
            </div>
        </div>
        </div>


    
    
    </>
}