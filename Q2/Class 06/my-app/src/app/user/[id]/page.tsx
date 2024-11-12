import { notFound } from "next/navigation"

export default function UserIdPage(props: any){
    if(Number(props.params.id) > 10){
        notFound()
    }
    return(
        <div>
            <h1>User detail page {props.params.id}</h1>
        </div>
    )
}