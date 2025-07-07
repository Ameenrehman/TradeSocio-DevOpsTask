import os
from flask import Flask, request, jsonify
from prometheus_client import generate_latest, Counter, Gauge, Histogram, Summary

# --- Prometheus Metrics ---
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'Histogram of request processing time',
    ['method', 'endpoint']
)

REQUEST_SIZE = Summary(
    'http_request_size_bytes',
    'Summary of request sizes in bytes'
)

IN_PROGRESS = Gauge(
    'http_requests_in_progress',
    'Number of HTTP requests in progress'
)

# --- Flask Application ---
app = Flask(__name__)

PORT = int(os.environ.get('PORT', 5000))

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
@IN_PROGRESS.track_inprogress()
def api_details():
    method = request.method
    endpoint = '/api'

    with REQUEST_LATENCY.labels(method=method, endpoint=endpoint).time():
        headers_str = "\n".join([f"{k}: {v}" for k, v in request.headers.items()])
        status_code = 200
        response_body = ""

        try:
            body = request.get_json(force=True)
            username = body.get('username', 'N/A')
            password = body.get('password', 'N/A')

            response_body = f"""Welcome to our demo API, here are the details of your request:

***Headers***:
{headers_str}

***Method***:
{method}

***Body***:
{{"username": "{username}", "password": "{password}"}}
"""
        except Exception as e:
            response_body = f"Invalid JSON or missing fields. Error: {str(e)}"
            status_code = 400

        # Prometheus metrics
        REQUEST_COUNT.labels(method=method, endpoint=endpoint, status_code=str(status_code)).inc()
        REQUEST_SIZE.observe(len(request.data))

        return response_body, status_code

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

@app.route('/')
def health_check():
    return "API is running!", 200

if __name__ == '__main__':
    print(f"Starting API service on port {PORT}...")
    app.run(host='0.0.0.0', port=PORT)
