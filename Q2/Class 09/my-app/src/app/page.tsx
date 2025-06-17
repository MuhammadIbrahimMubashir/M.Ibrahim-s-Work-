import Hero from "@/components/hero";
import { InputWithButton } from "@/components/mybutton";
import { DialogDemo } from "@/components/mydialog";
import Image from "next/image";
import CardDemo from "./card";
import CalendarDemo from "@/components/mycalendar";
import { ComboboxDemo } from "@/components/mycombobox";
import { SheetDemo } from "@/components/mysheet";
import { CommandDemo } from "@/components/mycommand";
import { TableDemo } from "@/components/mytable";

export default function Home() {
  return (
    <div className="h-full bg-yellow-300">
      <h1 className="text-3xl text-center pt-4">Hello</h1>
      <br/>
      <hr/>
      <br/>
      {/*Dialog Box*/}
      <div>
      <DialogDemo/>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Hero*/}
      <div>
      <Hero/>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Input And Button*/}
      <div>
      <InputWithButton/>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Card*/}
      <div className="w-screen flex justify-center">
        <CardDemo/>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Calender*/}
      <div className="grid grid-cols-2 gap-4 p-5 m-7">
        <div className="bg-blue-700 rounded-2xl">
          <p className="mt-32 font-extrabold font-serif text-3xl italic underline text-lime-500 flex justify-center">Heading</p>
        </div>
        <div className="bg-cyan-500 rounded-2xl">
          <CalendarDemo/>
        </div>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Combo Box*/}
      <div className="flex justify-center">
        <ComboboxDemo/>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Sheet*/}
      <div>
        <SheetDemo/>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Command*/}
      <div>
        <CommandDemo/>
      </div>
      <br/>
      <hr/>
      <br/>
      {/*Table*/}
      <div>
        <TableDemo/>
      </div>
    </div>
  );
}
