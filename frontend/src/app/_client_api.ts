const baseurl = 'http://127.0.0.1:8000/' //change base url for backend call on prod

export const postAPI = async(url: string, payload : object,doNotIncludeBaseUrl:boolean = false) =>{
  let actualUrl; 
  if (doNotIncludeBaseUrl){

         actualUrl = url
      }else{
         actualUrl = baseurl + url
      } 
  try{
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


export const getAPI = async(url: string="",doNotIncludeBaseUrl:boolean = false) =>{
    let actualUrl;  
    if (doNotIncludeBaseUrl){
        actualUrl = url
    }else{
        actualUrl = baseurl + url
    }

    try{
      
    const resposne  = await fetch(actualUrl, 
          { 
            method:'GET',
            headers:{"Content-Type":"application/json"}
          });
        const data = await resposne.json()
        return data
    }catch(error ){
      console.log("Error ", error)
      return error
    }
  }