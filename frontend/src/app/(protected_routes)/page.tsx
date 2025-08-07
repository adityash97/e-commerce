"use client"
import Footer from "./footer";
import Header from "./header"
import Item from "./items_card"
import {getAPI} from "@/app/_client_api"
import { useEffect } from "react";
import {useState} from "react"
import {ProductType} from "./models"
// import TestDesign from "./test_design";
export default  function Home() {
  const [products , setProducts] = useState<ProductType[]>([])
  useEffect(()=>{
    getAPI("https://fakestoreapi.com/products",true).then(data =>setProducts(data))
  .catch(err => console.log(err))
  },[])
  console.log("products",products)
  
  return <>
    <div className="flex flex-col min-h-screen bg-[#F2F2F2]">
      <Header />
      
      <main className="flex-grow">
          <div className="flex flex-row items-center flex-wrap justify-start gap-4 mt-2">
            {Array.isArray(products) &&
              products.map(product => <Item
              key={product.id}
              title={product.title}
              price={product.price}
              description={product.description}
              category={product.category}
              image={product.image}

              />)
            }
           

                 
          </div>
        </main>

      <Footer />
    </div>
  </>
    
     
  ;
}
