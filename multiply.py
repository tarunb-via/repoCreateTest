/**
 * Multiply 6 by 4 and return the result.
 * Can be used as a module or run directly with Node.js.
 */

// Function that multiplies 6 by 4
function multiplySixByFour() {
  return 6 * 4;
}

// Export for use as a module
module.exports = { multiplySixByFour };

// Run directly (print result when executed as a script)
if (require.main === module) {
  const result = multiplySixByFour();
  console.log(`Result: ${result}`);
}