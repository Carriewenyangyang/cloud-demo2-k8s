# For local development we use Flask directly.
# For production, consider switching to nginx for static file serving:
#   FROM nginx:latest
#   COPY my_index.html /usr/share/nginx/html/index.html
#   EXPOSE 80


FROM python:3.10-slim

WORKDIR /app

# Copy Flask app and static files
COPY app.py /app/
COPY static/ /app/static/

# Install dependencies
RUN pip install flask requests

EXPOSE 80

# Start Flask
CMD ["python", "app.py"]


