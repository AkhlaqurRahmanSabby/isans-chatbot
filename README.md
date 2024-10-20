# ISANS Chatbot

## Project Overview

The **ISANS Chatbot** was developed as part of the **RBC HubHacks Challenge 2024**, which focused on creating innovative solutions to help immigrants in Nova Scotia access critical programs and services. The chatbot aims to address the challenge of information silos within service organizations, ensuring that newcomers can easily discover the most relevant programs based on their unique needs.

Leveraging **Natural Language Processing (NLP)** and **semantic search** technologies, the chatbot helps ISANS (Immigration and Settlement Agency of Nova Scotia) deliver timely and accurate information, thus enhancing the user experience and ensuring no client is left underserved.

## Features

- **Natural Language Understanding**: Comprehends user queries to provide meaningful responses.
- **Semantic Search**: Utilizes embeddings and similarity search to find relevant programs.
- **Centralized Database**: Employs MongoDB to store and manage program information, reducing information silos.
- **Interactive Frontend**: User-friendly interface for seamless interaction with the chatbot.
- **Basic Conversational Replies**: Handles common greetings and simple inquiries.

## Technologies Used

- **Frontend**:
  - HTML5 & CSS3
  - JavaScript

- **Backend**:
  - FastAPI
  - MongoDB
  - Sentence Transformers (DistilBERT)
  - FAISS (Facebook AI Similarity Search)
  - Python

## Current Status

The project is currently under development with the following components implemented:

- **Backend**:
  - FastAPI setup with CORS middleware.
  - Integration with DistilBERT for generating text embeddings.
  - FAISS indexing for efficient semantic search.
  - Basic conversational reply handling.

- **Frontend**:
  - Basic HTML/CSS interface with a chat window and program filters.
  - JavaScript to handle user interactions and communicate with the backend.

**Note**: The frontend and backend are not yet fully integrated. Some functionalities may not work as intended, and the system is not ready for deployment.

## Future Work

- **Complete Integration**: Ensure seamless communication between frontend and backend.
- **Enhanced NLP Capabilities**: Upgrade to more powerful models for better understanding and response accuracy.
- **Advanced Filtering**: Implement comprehensive program filtering based on multiple criteria.
- **Error Handling**: Improve robustness to handle edge cases and unexpected user inputs gracefully.
- **User Interface Enhancements**: Refine the frontend for a more engaging and intuitive user experience.
- **Deployment**: Prepare the application for deployment on scalable platforms.

*This project is a work in progress, developed for the RBC HubHacks Challenge 2024. Contributions and feedback are welcome to help improve the ISANS Chatbot.*
