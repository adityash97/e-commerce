
import Footer from "./footer";
import Header from "./header"
import Item from "./items_card"

export default function Home() {
  return <>
    <div className="flex flex-col min-h-screen">
      <Header />
      
      <main className="flex-grow flex items-center justify-center">
        <Item/>
      </main>

      <Footer />
    </div>
  </>
    
     
  ;
}
