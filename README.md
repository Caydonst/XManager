# XManager: A Password Storage App
### Instructor: Prof. Rahat Rafiq
### Created for CIS 350 03
## Made by:
### Caydon Thomas
### Kyle Maitner
### Mathew Lindahl

# Abstract
This app works as a password manager that will take a master password and uses encryption to protect and store your passwords for other apps or websites that you can use. This was an exploration into how encryption would look and work as well as a test of our coding skills.


# Introduction
This app is a password manager app. With the growth of technology over the decades, account hacking is becoming more prevalent. People need to start creating more abstract and unique passwords but these passwords aren’t exactly easy to rememeber. That’s where our password manager app helps out. Once downloaded, the user will be prompted to create an account or login. Once logged into their account, they will have access to all of their records and they will have the options to create, edit, copy, or delete records. When creating a record, they will be prompted to enter the name of the record and the password that they want to store. Once the record is created they will be able to click on the record from the records window and have the option to copy the password.

# Diagrams
### Use Case

<figure>
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1159534457338998804/image.png?ex=65315f9d&is=651eea9d&hm=fd49eac7cbe4fba7f6ed3185e82a1020e66b7dd816fe514abe57ac40d5e495a2&" alt="Trulli"
    style="width:40%">
  <figcaption align = "center"><b>Use Case Diagram
    
</b></figcaption>
</figure>

### Sequence

<figure>
<img src="https://cdn.discordapp.com/attachments/486014885080334367/1159313205026357268/image.png?ex=6530918f&is=651e1c8f&hm=89601473fb0065837f4b49c21eba22853c68522e13d2af6effa7ebf9034aa1b7&" alt="Trulli"
style="width:50%">
<figcaption align = "center"><b>Sequence Diagram

</b></figcaption>
</figure>

### Class

<figure>
<img src="https://cdn.discordapp.com/attachments/1147261091508932728/1159542198233202738/image.png?ex=653166d3&is=651ef1d3&hm=7849b6dad71e3888a375d55eee50b53929518c309ea31ff9ffd993de6177cd18&" alt="Trulli"
style="width:70%">
<figcaption align = "center"><b>Class Diagram

</b></figcaption>
</figure>

# User Guide

## Home window

<figure>
<img src="https://cdn.discordapp.com/attachments/486014885080334367/1178714493384130670/image.png?ex=6577266a&is=6564b16a&hm=aa5d64d366648127773c96244dfd052e822e2e5beeed372d9881ccf95f1a12c9&" alt="Trulli"
style="width:50%">
<figcaption align = "center"><b>

</b></figcaption>
</figure>

## Registration

User is requirement to create an account when using the app. The username may only contain letters and numbers. The passwords needs to be at least 8 characters in length, and must contain at least 1 letter, number and special character. If some requirements are not met, the app will display a pop-up to show what requirements still need to be met.

<p align="center>

  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1178769433225875587/image.png?ex=65775995&is=6564e495&hm=6e44145e6d9c6e0a621bc272509fb5d198031fb9c77bf1d239208bc1a004bd29&" alt="Trulli"
  style="width:45%"> 
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1179609344594153502/cac31cb0ad900953858438e88f076bae.png?ex=657a67cf&is=6567f2cf&hm=e4cf238d9bc0b5df036b6b4b1afba43e2a1144a97c71976a05ed67d74beb8099&" alt="Trulli"
  style="width:45%"> 

</p>

## Home window with user account

When an account has been successfully created, it will navigate the user back to the home window and the user may select the account to log in.

<figure>
<img src="https://cdn.discordapp.com/attachments/486014885080334367/1178752884800761957/image.png?ex=65774a2b&is=6564d52b&hm=021bd9df228927f8821760b65bd3bc6a4fd19ce3be730947e5294cd4df750730&" alt="Trulli"
style="width:50%">
<figcaption align = "center"><b>

</b></figcaption>
</figure>

## Log in

When logging into an account the user is required to input the password to log in. There is a toggle button next to the text box that allows the user to show or hide the password.

<p align="center">
  
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1178753345289211996/image.png?ex=65774a99&is=6564d599&hm=d54e9e36cb982852c237b92e93d6ef28afa94fff6867d863af6368013dd878a5&" alt="Trulli"
  style="width:45%">
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1178753426222497822/image.png?ex=65774aac&is=6564d5ac&hm=9455c7c4437207c7159909fdfc5fb42b23dc3766814edb73ada33436ea963c2e&" alt="Trulli"
  style="width:45%">

</p>

## Records

When the user logs in they will be navigated to the records window. If the user has no records, that window will be emtpy.

<figure>
<img src="https://cdn.discordapp.com/attachments/486014885080334367/1178753572930859028/image.png?ex=65774acf&is=6564d5cf&hm=323fa3d00cce8da145cbb202d3fdd0442eb8e4d71b1cd442ca258c15d8c20fea&" alt="Trulli"
style="width:50%">
<figcaption align = "center"><b>

</b></figcaption>
</figure>

## Creating a record

When the user clicks the add button, a window pops up allowing the user to input the record information. Each record must have a title to display what the record is. The username and passwords fields are the account information you are storing. For example, if the user wants to store an email record, they will input the email and email password into the username and password fields respectively.

<p align="center">
  
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1179648011299725434/b22fb5835afc8d34f90d6319bfdd4a08.png?ex=657a8bd2&is=656816d2&hm=a9e9b6180f3535ef4dfb9dbef7855386bf5077dce8c7d0f1e773d9fd743d0375&" alt="Trulli"
  style="width:45%">
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1179648358399348776/796d95b05b567b64af0e6cbeeda708ee.png?ex=657a8c25&is=65681725&hm=769c9044d078ac0a768c4a1898762ead2d73d07b18b2c09679596db3a8df882f&" alt="Trulli"
  style="width:45%">

</p>

## Accessing a record

When a record is successfuly created, it will be displayed at the top of the screen. When the user clicks on a record, they will be required to type in their account password to get access to the record information.

<p align="center">
  
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1178753818339586078/image.png?ex=65774b0a&is=6564d60a&hm=0d01271f434db071ab71298dad5510cd6046faafffc0a0693e7a03e7c84fbdec&" alt="Trulli"
  style="width:45%">
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1179648807324110868/4fb6e8dc8958ec2ed0c939c5e2114262.png?ex=657a8c90&is=65681790&hm=8fe341a8928ac7589c078dc38b16a587cc9267387dc5ecb5bfe5bea76e40df3a&" alt="Trulli"
  style="width:45%">

</p>

When the user inputs their account password, the record information will be displayed for them to copy, edit, or delete.

<figure>
<img src="https://cdn.discordapp.com/attachments/486014885080334367/1178767794213507183/image.png?ex=6577580e&is=6564e30e&hm=8825af72e60ddec8f6bd122ba0c5c6125032366344a550970e483fa9efc4d5b2&" alt="Trulli"
style="width:50%">
<figcaption align = "center"><b>

## Profile

When the user clicks on the profile icon, the profile window will be displayed. The user may set a profile picture, logout, or delete their account.

</b></figcaption>
</figure>

<p align="center">
  
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1179651899637649408/3c91553e365ebfaf71a155621a9f87c2.png?ex=657a8f71&is=65681a71&hm=ca24b543952241edf103cdbe3adef22df132024b6debf2070417a8ac31fa85d1&" alt="Trulli"
  style="width:45%">
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1179651932399353906/7658fe6dcfa2eb0f486cd1cfa008cd62.png?ex=657a8f79&is=65681a79&hm=c265bf057bed2fd14822238ede447447cd1a80db3389766051794393f84955e9&" alt="Trulli"
  style="width:45%">
  <img src="https://cdn.discordapp.com/attachments/486014885080334367/1179651961218416710/47cad2a27c4599205fa9fa7b6253f32b.png?ex=657a8f80&is=65681a80&hm=872118adebd7a2e5844b47f5726c7c936ae0dbca7560e6bd6962822d9e9fa4e0&" alt="Trulli"
  style="width:45%">
  

</p>

