import UserPage from "./user/[slug]/page";
import UserList from "./user/page";

export default function Home(){
  return(
    <div>
      <title>Users</title>
      <UserPage/>
      <UserList/>
    </div>
  )
}