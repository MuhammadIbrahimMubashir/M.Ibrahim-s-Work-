import Image from "next/image";

{/*Grid*/}
export default function Home() {
  return (
    <div className="bg-white h-screen">
      <div className="grid grid-cols-[1fr,1fr,1fr]">
      <div className="bg-blue-500">1</div>
      <div className="bg-blue-600">2</div>
      <div className="bg-blue-700">3</div>
      </div>
      <br/>
      <div className="grid grid-cols-[auto,1fr,auto]">
      <div className="bg-blue-500">1</div>
      <div className="bg-blue-600">2</div>
      <div className="bg-blue-700">3</div>
      </div>
      <br/>
      <div className="grid grid-cols-[100px,200px,100px]">
      <div className="bg-blue-500">1</div>
      <div className="bg-blue-600">2</div>
      <div className="bg-blue-700">3</div>
      </div>
      <br/>
      <HomePage/>
    </div>
  );
}

function HomePage() {
  return(
    <div>
    <div className="grid grid-cols-3 gap-2">
      <div className="bg-blue-300">Logo</div>
      <div className="bg-blue-400">Navbar</div>
      <div className="bg-blue-500">Search Bar</div>
    </div>
    <div className="bg-blue-600 text-center grid grid-cols-1">
      Logos
    </div>
    <div className="text-center grid grid-cols-[200px,1fr] gap-1 h-96">
      <div className="bg-blue-700">SideBar</div>
      <div className="bg-blue-800">Inbox</div>
    </div>
    <div className="bg-blue-950 grid grid-rows-1 h-24">
      <div className="text-center mt-9">Footer</div>
    </div>
    </div>
  )
}