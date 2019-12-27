let raceNumber = Math.floor(Math.random() * 1000);
let earlyRunner = false;
let runnerAge = 18;

// Checking if runner is an Adult and registered early
if (runnerAge > 18 && earlyRunner === true){
  raceNumber+=1000;
}

//checking age and registration time to determine race time
if (runnerAge > 18 && earlyRunner === true){
  console.log(`Race will start at 9:30 am. Race Number: ${raceNumber}`);
} else if (runnerAge > 18 && earlyRunner === false) {
  console.log(`Race starts at 11:00 am. Race Number: ${raceNumber}` );
}
else if(runnerAge < 18){
  console.log(`Race starts at 12:30 pm. Race Number: ${raceNumber}`);
} else{
  console.log("Got to registration desk, please.");
}
