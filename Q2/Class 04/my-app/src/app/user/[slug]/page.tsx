import Heading from "@/app/components/heading"

async function UserPage(props:any){
    const url =`https://jsonplaceholder.typicode.com/users/${props.params.slug}`
    const fetchData = await fetch(url)
    const res = await fetchData.json()
    return(
        <div>

            <Heading text={`Name:${res.name}`}/>
            <Heading text={`Email:${res.email}`}/>
            <Heading text={`ID:${res.id}`}/>
        </div>
    )
}

export default UserPage