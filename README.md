# Anime Quotes API

The Anime Quotes API provides access to a vast collection of inspirational anime quotes, perfect for fans looking to relive those powerful moments. Use this API to fetch random quotes, search for quotes by specific anime or tag, and share the wisdom from beloved anime characters with the world.

## Test the API

You can test the API by visiting the following link: [Anime Quotes API](https://teojiayizoe.github.io/anime-quotes/)

## Using Anime Quotes API Responsibly

This API is provided for educational and personal use only. Please adhere to the following guidelines:

- Avoid excessive API requests to ensure fair access for all users.
- Do not scrape, redistribute, or repackage the content from this API without permission.
- Do not use the API for commercial purposes without prior authorization.
- When using this API, you must credit Anime Quotes API as the source. For example, include a statement like: "Quotes powered by [Anime Quotes API](https://github.com/TeoJiaYiZoe/anime-quotes)."


## Technologies Used

- **Frontend**:
  - HTML
  - CSS (for styling)
  - JavaScript (for handling form submission and fetching data)
  
- **Backend**:
  - **AWS Lambda**: Handles the API request to fetch quotes.
  - **AWS API Gateway**: Exposes the Lambda function as a REST API endpoint.
  
- **API**:
  - The app communicates with the API exposed by AWS API Gateway, which triggers the Lambda function.

## Getting Started

To run this project locally, follow the instructions below.

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TeoJiaYiZoe/anime-quotes.git
   cd anime-quotes

2. **Set Up Virtual Environment** (Optional but recommended):
   It's a good practice to create a virtual environment to manage dependencies. Run the following commands to create and activate the virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. **Start the Local Server**

   ```bash
   uvicorn main:app --reload

