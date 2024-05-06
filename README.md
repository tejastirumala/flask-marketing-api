# Flask Marketing API

Welcome to the Flask Marketing API! This API generates marketing content based on the provided topic and format.

## Endpoint URL
The API endpoint URL for generating marketing content is:
Endpoint URL: http://127.0.0.1:5000/generate-marketing-content


## Instructions for Posting JSON Data

To post JSON data to the Flask API endpoint:

1. Open Postman or any HTTP client tool.
2. Set the request type to POST.
3. Enter the following URL in the request URL field: http://127.0.0.1:5000/generate-marketing-content
4. In the request body, select "raw" format and choose "JSON".
5. Enter the JSON data containing the required parameters, such as "format" and "topic". For example:
```json
{
  "format": "linkedin post",
  "topic": "Generative AI"
}

.
6. Click on the "Send" button to submit the request.

By this, you will get the required output.
