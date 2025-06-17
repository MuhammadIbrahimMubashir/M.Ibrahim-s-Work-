import { Card } from "@/components/ui/card"  
import name from "../app/image/name.png"
import Image from "next/image";

const CardDemo = () => {
  return (
    <Card className="w-[450px] p-6 divide-x-2 divide-yellow-500 flex justify-start items-center">
        <Image src={name} alt="No" width={100} height={100} className="w-[50px] h-[50px] rounded-full mr-3"/>
        <h1 className="pl-3 w-full">My Logo</h1>
    </Card>
  )
}

export default CardDemo