let username = "Jane";
let userQuestion = "Is the sky blue?";
let randomNumber = Math.floor(Math.random()*8);
let eightBall = "";

// If username is Jane will greet by name
username === 'Jane' ? console.log(`Hello ${username}!`): console.log("Hello!")

//Printing the question
console.log(`${userQuestion} by ${username}`)
//console.log(randomNumber)

// Assigning values to answer
switch(randomNumber){
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidedly so';
    break;
  case 2:
    eightBall = 'Reply hazy try again';
    break;
  case 3:
   eightBall = 'Cannot predict now';
    break;
  case 4:
    eightBall = 'Do not count on it';
    break;
  case 5:
   eightBall = 'My sources say no';
    break;
  case 6:
    eightBall = 'Outlook not so good';
    break;
  case 7:
    eightBall = 'Signs point to yes';
    break; 
}

// Priting the answer
console.log(eightBall);
