export function Heading(props:any){
    return(
        <div>
            <h1><b><u><i>Respected Sir!</i></u></b></h1>
            <h1><pre>             <b><u><i>{`${props.name}`}</i></u></b></pre></h1>
            <br></br>
            <h1><b>{`You are ${props.age} years old.`}</b></h1>
        </div>
    )
}