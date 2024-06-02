# Flask MongoDB CRUD

This is a simple CRUD (Create, Read, Update, Delete) application built using Flask, Python, MongoDB Atlas, and Postman for testing. The application allows you to perform basic CRUD operations on a MongoDB database.

## Prerequisites

- Python 3.x
- Flask
- PyMongo
- MongoDB Atlas account
- Postman


# Setting Up MongoDB Atlas

## Creating a MongoDB Atlas Cluster

1. **Sign Up or Log In to MongoDB Atlas**:
   - Go to the [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) website.
   - Sign up for a new account or log in to your existing account.

3. **Get the Connection String**:
   - Once your cluster is created, go to the "Clusters" view.
   - Click the "Connect" button for your cluster.
   - In the "Connect to your Cluster" dialog, choose "Connect your application".
   - You will see a connection string. It will look something like this:
     ```
     mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
     ```

4. **Update the Connection String**:
   - Replace `<username>` with your MongoDB Atlas username.
   - Replace `<password>` with your MongoDB Atlas user's password.
   - Replace `<dbname>` with the name of the database you want to connect to.

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/IanSreya/flask-mongodb-crud.git
cd flask-mongodb-crud
```
## Install postman

**Open Postman and perform CRUD operations using the following endpoints**:

   1. **Create an Item**:
      - URL: '/add'
      - Method: 'POST'

   2. **Get All Items**:
      - URL : '/items'
      - Method: 'GET'

   3. **Get Single Item**:
      - URL : '/item/_id'
      - Method: 'GET'

   4. **Update an Item**:
      - URL : '/update/_id'
      - Method: 'PUT'

   5. **Delete an Item**:
      - URL : '/delete/_id'
      - Method: 'DELETE'
   



