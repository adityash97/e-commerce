
import Footer from "./footer";
import Header from "./header"
import Item from "./items_card"

export default function Home() {
  return <>
    <div className="flex flex-col min-h-screen bg-[#F2F2F2]">
      <Header />
      
      <main className="flex-grow">
          <div className="flex flex-row items-center flex-wrap justify-start gap-4 mt-2">
           <Item/>
           <Item/>
           <Item/>
           <Item/>
           <Item/>
           <Item/>

                 
          </div>
        </main>

      <Footer />
    </div>
  </>
    
     
  ;
}
