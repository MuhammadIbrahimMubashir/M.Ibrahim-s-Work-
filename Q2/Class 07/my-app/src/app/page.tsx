import Image from "next/image";

{/*Tailwindcss Font Styles*/}
export default function Home(){
  return(
    <div className=" sm:bg-green-700 sm:h-fit md:bg-orange-700 md:h-screen lg:bg-blue-800 lg:h-screen xl:bg-amber-950 h-screen">
      <h1 className="text-center py-3">Boy</h1>{/*my-3 margin top-bottom*/}
      <h1 className="font-thin">Thin</h1>
      <h1 className="font-extralight">Extra Light</h1>
      <h1 className="font-light">Light</h1>
      <h1 className="font-semibold">Semi Bold</h1>
      <h1 className="font-bold">Bold</h1>
      <h1 className="font-extrabold">Extra Bold</h1>
      <h1 className="font-sans">Font Sans</h1>
      <h1 className="font-serif">Font Serif</h1>
      <h1 className="font-mono">Font Mono</h1>
      <h1 className="text-xs">XS Size</h1>
      <h1 className="text-sm">SM Size</h1>
      <h1 className="text-base">Base Size</h1>
      <h1 className="text-lg">Lg Size</h1>
      <h1 className="text-3xl">3XL Size</h1>
      <h1 className="text-center lg:text-3xl md:text-xl sm:text-lg">My Heading</h1>
      <p className="lg:text-lg md:text-base sm:text-sm sm:line-clamp-4 md:line-clamp-6 lg:line-clamp-none">A computer <span className="cursor-pointer underline underline-offset-8 italic decoration-red-700 hover:decoration-yellow-700 hover:underline-offset-2">Muhammad Ibrahim Mubashir</span> is a machine that can be programmed to automatically carry 
        out sequences of arithmetic or logical operations. Modern digital 
        electronic computers can perform generic sets of operations known as 
        programs. These programs enable computers to perform a wide range of 
        tasks.It  is a device that accepts information (in the form of digitalized data) 
        and manipulates it for some result based on a program, software, or 
        sequence of instructions on how the data is to be processed.It is an 
        electronic machine that processes raw data to give information as 
        output. An electronic device that accepts data as input, and transforms
        it under the influence of a set of special instructions called Programs, 
        to produce the desired output (referred to as Information).Information
        technology (IT) is the use of computers, storage, networking and other
        physical devices, infrastructure and processes to create, process, 
        store, secure and exchange all forms of electronic data.</p>
        <br/>
        <h1 className="font-serif font-bold italic bg-slate-600 w-12"><a href="/about" target="_blank">More Work</a></h1>
    </div>
  )
}
