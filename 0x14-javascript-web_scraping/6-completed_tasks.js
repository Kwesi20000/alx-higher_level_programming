#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      todos.forEach(todo => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });

      for (const userId in completedTasksByUser) {
        console.log(`User ${userId} completed ${completedTasksByUser[userId]} tasks.`);
      }
    } else {
      console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    }
  }
});
