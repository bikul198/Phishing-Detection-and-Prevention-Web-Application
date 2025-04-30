from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# Regular expression for URL validation
URL_REGEX = re.compile(
    r'^(?:http|https)://'
    r'(?:\S+(?::\S*)?@)?'
    r'(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}'
    r'(?::\d{2,5})?(?:/\S*)?$'
)

def is_valid_url(url):
    return re.match(URL_REGEX, url) is not None

def is_phishing(url):
    # List of suspicious keywords
    suspicious_keywords = ['login', 'verify', 'bank', 'account', 'secure', 'update', 'signin']
    return any(keyword in url.lower() for keyword in suspicious_keywords)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_phishing', methods=['GET'])
def check_phishing():
    url = request.args.get('url')
    if not url or not is_valid_url(url):
        return jsonify({'message': '❌ Invalid URL format!', 'status': 'invalid'})

    if is_phishing(url):
        return jsonify({'message': '🚨 Warning! Phishing detected.', 'status': 'phishing'})
    else:
        return jsonify({'message': '✅ Safe! No threats found.', 'status': 'safe'})

if __name__ == '__main__':
    app.run(debug=True)
