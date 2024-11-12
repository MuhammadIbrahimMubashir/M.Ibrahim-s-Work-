import Heading from "../../components/heading";
import Paragraph from "../../components/paragraph";
import Navbar from "../../components/navbar";

export default function Homepage(){
  return(
    <div>
      <title>Home Page</title>
      <Heading heading="My WebPage:-"/>
      <Paragraph para = "Hello Everyone! This is my personal WebPage."/>
      <br></br>
      <Navbar/>
    </div>
  )
}