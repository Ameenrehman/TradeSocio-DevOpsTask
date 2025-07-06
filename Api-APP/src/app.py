import os
from flask import Flask, request
from prometheus_client import generate_latest, Counter, Gauge, Histogram, Summary

# --- Prometheus Metrics ---
# Total HTTP requests by method, endpoint and status
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status_code']
)

# Histogram for request duration in seconds
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'Histogram of request processing time',
    ['method', 'endpoint']
)

# Summary for request size
REQUEST_SIZE = Summary(
    'http_request_size_bytes',
    'Summary of request sizes in bytes'
)

# Gauge for number of in-progress requests
IN_PROGRESS = Gauge(
    'http_requests_in_progress',
    'Number of HTTP requests in progress'
)

# --- Flask Application ---
app = Flask(__name__)

# Get port from environment variable, default to 5000
PORT = int(os.environ.get('PORT', 5000))

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
@IN_PROGRESS.track_inprogress()
def api_details():
    """
    Endpoint that prints request header, method, and body.
    """
    method = request.method
    endpoint = '/api'

    with REQUEST_LATENCY.labels(method=method, endpoint=endpoint).time():
        body = request.get_data(as_text=True)
        headers_str = "\n".join([f"{k}: {v}" for k, v in request.headers.items()])

        # Collect metrics
        REQUEST_COUNT.labels(method=method, endpoint=endpoint, status_code='200').inc()
        REQUEST_SIZE.observe(len(body.encode('utf-8')))

        response_content = f"""Welcome to our demo API, here are the details of your request:

***Headers***:
{headers_str}

***Method***:
{method}

***Body***:
{body}
"""
        return response_content, 200

@app.route('/metrics')
def metrics():
    """
    Endpoint to expose Prometheus metrics.
    """
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

@app.route('/')
def health_check():
    """
    Simple health check endpoint.
    """
    return "API is running!", 200

if __name__ == '__main__':
    # Follow 12-Factor App principle: logs to stdout
    print(f"Starting API service on port {PORT}...")
    app.run(host='0.0.0.0', port=PORT)
