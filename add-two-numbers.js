const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter the first number: ', (input1) => {
  rl.question('Enter the second number: ', (input2) => {
    const num1 = Number(input1);
    const num2 = Number(input2);

    if (!Number.isFinite(num1) || !Number.isFinite(num2)) {
      console.error('Error: Please enter valid numbers.');
      rl.close();
      process.exit(1);
    }

    const sum = num1 + num2;
    console.log(`Result: ${sum}`);
    rl.close();
  });
});