# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Ankur Mathur
- Jerry 

## Lab Question Answers

Answer for Question 1: 
They are scalable because they are stateless, which means that calls toy the server are independent because the information that is in the request sent by the client is enough for the server to act on it. This means that the server does not need to retain past client request information. 

Answer for Question 2:
Resources are the information that applications provide to the client and they can be any type of data. The server stores the data of the inboxes and sends the information when the client calls for it.

Answer for Question 3:
The put method was not used in the server. Instead the post method was used. Since multiple calls of the put command give the same result, it can be used in the main function and get called everytime. That way the server will update everytime the program runs.

Answer for Question 4:
API keys are a form of security. The client uses the key to verify itself to the server. They are used in RESTful APIs to block anonymous traffic and to control the number of calls made to the API. 

Source:https://cloud.google.com/endpoints/docs/openapi/when-why-api-key
...
