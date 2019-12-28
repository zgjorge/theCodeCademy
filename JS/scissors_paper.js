// Getting user input
const getUserChoice = userInput =>{
  userInput = userInput.toLowerCase();
  if(userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb'){
     return userInput;
     }
 console.log("The input is not accepted")
}

//console.log(getUserChoice("ROCK"));

// Generating Computer choice
const getComputerChoice = () => {
  randomNumber = Math.floor(Math.random() * 3);
  if(randomNumber === 0){
    return 'rock';
  } else if (randomNumber === 1){
    return 'paper';
  } else{
    return 'scissors';
  }
}

//console.log(getComputerChoice());
// Finding the winner
function determineWinner(userChoice, computerChoice){
  if (userChoice === computerChoice){
    return 'The game is a tie!';
  }
  if (userChoice === 'bomb'){
    return 'Kabooom, user won!';
  }
  if (userChoice === 'rock'){
    if(computerChoice === 'paper'){
      return 'The computer won';
    } else {
      return 'The user won!';
    }
  }
  if (userChoice === 'paper'){
    if(computerChoice === 'scissors'){
      return 'The computer won';
    } else {
      return 'The user won!';
    }
  }
  if (userChoice === 'scissors'){
    if(computerChoice === 'rock'){
      return 'The computer won';
    } else {
      return 'The user won!';
    }
  }
}

// Starting the game
function playGame(){
  let userChoice = getUserChoice('bomb');
  let computerChoice = getComputerChoice()
  console.log(`You selected ${userChoice}`);
  console.log(`Computer choose ${computerChoice}`);
  console.log(determineWinner(userChoice,computerChoice));
}

playGame();
