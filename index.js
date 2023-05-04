const Database = require('@replit/database');
//const fetch = require('node-fetch');
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const OTHER_DB_URL = 'https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2ODIzMTExODcsImlhdCI6MTY4MjE5OTU4NywiZGF0YWJhc2VfaWQiOiJjMTE1YzBhMC1iNGYzLTQwNTktYjI3NS1hMGFkYWZmMmNjZmYiLCJ1c2VyIjoiTWFyY2lvTWl6dWhhcmEiLCJzbHVnIjoiQWxidW0tQ2hhbGxlbmdlLTUwIn0.flZpDOTE0102nkmq-oJvVyNqLo2jQvNbwoXyI4jf7qNI8ZXVZ7uzi4bSGpeO_28AwLpeai8TCzIGxgDpNbnLfg';

// Initialize the Replit Database client
const db = new Database();

// Function to copy values from Replit Database to another database
async function copyValuesToOtherDatabase() {
  try {
    const keys = await db.list();  
        // Loop through each key and get its corresponding value
    for (const key of keys) {      
      const value = await db.get(key, { raw: true });
      
      // Send the data to the other database specified by the URL
      await fetch(`${OTHER_DB_URL}/${key}=${value}`, {
        method: 'POST',
      });
      console.log(`${OTHER_DB_URL}/${key}`)
    }    
    console.log('Successfully copied values to the other database!');
  } catch (error) {
    console.error('An error occurred while copying values:', error);
  }
}

// Execute the function to start copying values
copyValuesToOtherDatabase();