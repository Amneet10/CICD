# Flask Dockerized App

This is a simple Flask application Dockerized for demonstration purposes.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/flask-dockerized-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-dockerized-app
    ```

3. Build the Docker image:

    ```bash
    docker build -t my-flask-app .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 5000:5000 my-flask-app
    ```

## Usage

Once the Docker container is running, you can access the Flask application by navigating to `http://localhost:5000` in your web browser.

## Testing

To run the unit tests:

```bash
python test_app.py
