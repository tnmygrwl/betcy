pragma solidity ^0.4.10;

contract brutalexa {

  struct bet {
    uint p_id;
    address creator;
    address player;
    string bet_text;
    string date_due;
    address first_witness;
    address sec_witness;
    address third_witness;
    uint validity;
    uint stakedid;
  }
  uint b_id_count = 0;

  mapping (address => bet) addresstobet;
  mapping (address => uint[]) addresstobetidlist;
  mapping (address => uint[]) requestlist;
  mapping (uint => bet) betidtobet;

 function next_id() internal{
  b_id_count+=1;
 }

 function create_promise(address sec, string bettext, string date, address wit1, address wit2, address wit3,uint productid) public {
   next_id();
   betidtobet[b_id_count] = bet(b_id_count,msg.sender,sec,bettext,date,wit1,wit2,wit3,0,productid);
   addresstobet[msg.sender]= bet(b_id_count,msg.sender,sec,bettext,date,wit1,wit2,wit3,0,productid);
   addresstobetidlist[msg.sender].push(b_id_count);
   requestlist[sec].push(b_id_count);
 }

 function show_pending_requests() public view returns(uint[]) {
   return requestlist[msg.sender];
 }

 function show_validity(uint b_id) public view returns(uint) {
   return validity;
 }
 function showbets(uint b_id) public view returns(uint bet_id,address creator,address player,string text,string due_date,address witness1,address witness2,address witness3,uint validity,uint productid) {
   bet_id = b_id;
   creator = betidtobet[b_id].creator;
   player = betidtobet[b_id].player;
   text = betidtobet[b_id].bet_text;
   due_date = betidtobet[b_id].date_due;
   witness1 = betidtobet[b_id].first_witness;
   witness2 = betidtobet[b_id].sec_witness;
   witness3 = betidtobet[b_id].third_witness;
   validity = betidtobet[b_id].validity;
   productid = betidtobet[b_id].stakedid;
 }

 function acceptbet(uint b_id) public {
   require(msg.sender == betidtobet[b_id].player);
   betidtobet[b_id].validity=1;
   addresstobetidlist[msg.sender].push(b_id);
 }

 function showlivebets() view returns(uint[]) {
   return addresstobetidlist[msg.sender];
 }
}
