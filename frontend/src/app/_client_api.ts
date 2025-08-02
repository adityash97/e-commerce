const baseurl = 'http://127.0.0.1:8000/'
export const postAPI = async(url: string, payload : object) =>{
    try{
    const actualUrl = baseurl + url
    const resposne  = await fetch(actualUrl, 
          { 
            method:'POST',
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(payload)
          });
        const data = await resposne.json()
        return data
    }catch(error ){
      console.log("Error ", error)
      return error
    }
  }


export const getAPI = async(url: string, payload : object) =>{
    const actualUrl = baseurl + url
    try{
    const resposne  = await fetch(actualUrl, 
          { 
            method:'GET',
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(payload)
          });
        const data = await resposne.json()
        return data
    }catch(error ){
      console.log("Error ", error)
      return error
    }
  }