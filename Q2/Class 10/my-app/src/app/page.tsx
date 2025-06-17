import { client } from "@/sanity/lib/client"

async function getData(){
    const fetchData = await client.fetch(`*[_type == 'student'] `)
    return fetchData
}

export default async function Home(){
    const data = await getData()
    console.log(data)
    return(
        <div>
            <h1>Hello Sanity</h1>
            {
                data.map((val:any,i:number)=>{
                    return(
                        <>
                            <h1>{val.name}</h1>
                        </>
                    )
                })
            }
        </div>
    )
}
