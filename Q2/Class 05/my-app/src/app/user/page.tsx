import Image from "next/image"
import abc from "../image/abc.jpeg"


async function UserPage(){
    const url = "https://jsonplaceholder.org/users"
    const fetchdata = await fetch(url)
    const res = await fetchdata.json()
    console.log(res)
    return(
        <div>
            <Image src={abc} alt="No Image"/>
            <h1>{res[0].firstname}</h1>
        </div>
    )
}
export default UserPage;