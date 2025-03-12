# Serverless URL Shortener 🚀

This project is a serverless URL shortening service built with AWS Lambda, API Gateway, and DynamoDB. It accepts long URLs, converts them into unique short URLs, and redirects users to the original URL when the short URL is accessed. 🔗✨

---

## Features 🌟

- **Serverless Architecture:** Fully serverless design using AWS Lambda, API Gateway, and DynamoDB.
- **Automatic Scalability:** Scales automatically with traffic 📈.
- **Easy Setup & Deployment:** Quick and hassle-free deployment using the Serverless Framework ⚙️.
- **High Performance:** Secure and fast access thanks to AWS infrastructure ⚡.

---

## Technologies & Requirements 💻

- [AWS Lambda](https://aws.amazon.com/lambda/) 
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
- [Serverless Framework](https://www.serverless.com/)
- [Node.js](https://nodejs.org/en/) (LTS version recommended)
- An AWS account and configured AWS CLI

---

## Project File Structure 📁

1. **serverless.yml:**  
   Defines AWS resources (Lambda functions, API Gateway, DynamoDB table, etc.). 🛠️

2. **handler.js:**  
   Contains the code for the Lambda functions that handle URL shortening and redirection. 🔀

3. **dynamodb-config.json:**  
   (Optional) Contains configuration settings for the DynamoDB table (also defined in `serverless.yml`). ⚙️

---

## Installation Steps 🔧

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ErkanBarann/aws-lambda-serverless-examples.git
   cd aws-lambda-serverless-examples/serverless-url-shortener
