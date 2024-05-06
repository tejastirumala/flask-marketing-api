from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to generate marketing content based on topic and format
def generate_content(topic, format):
    if format == "linkedin post":
        content = f"Excited to share insights on {topic}! 🚀 With its innovative capabilities, {topic} is revolutionising various industries, from creative arts to healthcare. Its potential to generate realistic images, text, and even music is reshaping the way we create and interact with technology. Let's explore the endless possibilities and opportunities this cutting-edge technology offers. #{topic.replace(' ', '')} #Innovation #TechRevolution 🤖💡"
        return content
    # Add more formats and their respective content generation logic here
    else:
        return "Format not supported."

# API endpoint for generating marketing content
@app.route('/generate-marketing-content', methods=['POST'])
def generate_marketing_content():
    data = request.get_json()
    topic = data.get('topic')
    format = data.get('format')

    if not topic or not format:
        return jsonify({"error": "Topic and format are required."}), 400

    content = generate_content(topic, format)
    return jsonify({"text": content})

if __name__ == '__main__':
    app.run(debug=True)
