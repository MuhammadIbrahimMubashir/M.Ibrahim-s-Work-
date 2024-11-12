import Heading from "@/app/components/heading";
import Link from "next/link";

const UserList = async () => {
    const url: string = "https://jsonplaceholder.typicode.com/users"
    const fetchData = await fetch(url)
    const res = await fetchData.json()
    return(
        <div>
            <title>Users</title>
            <Heading text="User List:-"/>
            <ol>
                {res.map((val:{name:string;id:string},index:number) => {
                    return(
                        <Link href={`/user/${val.id}`} key={index}>
                            <li>{`${index + 1} ${val.name}`}</li>
                        </Link>
                    )
                })}
            </ol>
        </div>
    )
}

export default UserList