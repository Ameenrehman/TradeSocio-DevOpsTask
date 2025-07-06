import os
from flask import Flask, request
from prometheus_client import generate_latest, Counter, Gauge

# --- Prometheus Metrics ---
# Counter for total requests
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status_code']
)

# Gauge for a hypothetical resource usage (e.g., current connections)
# GAUGE_CONNECTIONS = Gauge(
#     'current_connections',
#     'Current number of active connections'
# )
# In a real app, this would be incremented/decremented around connection establishment/teardown.
# For this simple demo, we'll just expose it.

# --- Flask Application ---
app = Flask(__name__)

# Get port from environment variable, default to 5000
PORT = int(os.environ.get('PORT', 5000))

@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_details():
    """
    Endpoint that prints request header, method, and body.
    """
    headers_str = "\n".join([f"{k}: {v}" for k, v in request.headers.items()])
    method = request.method
    body = request.get_data(as_text=True)

    # Increment Prometheus counter
    # Note: status_code is added later, after the response is generated
    # This is a simplified approach for demonstration.
    # In production, you might use a decorator or a Flask after_request hook.
    REQUEST_COUNT.labels(method=method, endpoint='/api', status_code='200').inc()

    response_content = f"""Welcome to our demo API, here are the details of your request:

***Headers***:
{headers_str}

***Method***:
{method}

***Body***:
{body}
"""
    return response_content, 200 # Return 200 OK status explicitly

@app.route('/metrics')
def metrics():
    """
    Endpoint to expose Prometheus metrics.
    """
    #GAUGE_CONNECTIONS.set(10) # Just setting a dummy value for demonstration
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
