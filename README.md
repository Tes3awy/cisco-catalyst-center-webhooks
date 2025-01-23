# Webhook Testing with Cisco Catalyst Center (a.k.a DNA Center)

This project is a PoC for the use of webhooks with Cisco SDN solutions, specifically integrating with Cisco Catalyst Center. It leverages a Flask application to receive and process webhook notifications in real-time, showcasing how events from the Catalyst Center can be handled programmatically.

# Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Security Considerations/Improvements](#security-considerationsimprovements)
- [Debugging Tips](#debugging-tips)
- [Contributing](#contributing)

## Features

- **Webhook Integration**: Receive and process notifications from Cisco Catalyst Center.
- **Websockets**: Enable ongoing, full-duplex, bidirectional communication between client and server.
- **Real-time Updates**: Display incoming notifications in a dynamically updating dashboard web page.
- **Authentication**: Secure webhook endpoints with basic authentication.
- **Notification Sound**: Play a sound when a new notification is received.

## Prerequisites

- Python 3.9+
- Flask
- Cisco Catalyst Center with webhook enabled

## Installation

1. Clone the repo

```bash
$ git clone https://github.com/Tes3awy/cisco-catalyst-center-webhooks.git
$ cd cisco-catalyst-center-webhooks
```

2. Setup a virtual environment (Optional but recommended)

```bash
$ python -m venv .venv
$ source .venv/bin/activate . # On Windows, use `.\.venv\Scripts\Activate.ps1` in powershell
(.venv)$ 
```

3. Install dependencies

```bash
(.venv)$ pip install -r requirements.txt
```

4. Update configuration (if required)

Open `config.py` file and change 

```py
BASIC_AUTH_USERNAME
BASIC_AUTH_PASSWORD
```

5. Run the application

```bash
(.venv)$ flask run
 * Serving Flask app 'run'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on https://127.0.0.1:5443
Press CTRL+C to quit   
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 419-253-304
***** Copy Headers for Cisco Catalyst Center Webhook *****
 Authorization: Basic YWRtaW46Q2lzY28hMjM0NQ==
 Content-Type: application/json
***** Copy Headers for Cisco Catalyst Center Webhook *****
```

6. Configure Cisco Catalyst Center

- Navigate to **System > Webhooks** in the Catalyst Center dashboard.
- Add a new POST webhook with the Webhook URL `https://<ip_address>:5443/api/v1/webhook`.
- Set the required headers: `Authorization: Basic <BASE64 of username:password>` and `Content-Type: application/json`.

## Security Considerations/Improvements

- Use HTTPs to secure webhook communications.
- Validate all incoming requests using a custom authentication token.

## Debugging Tips

Check the Flask application logs in the terminal for errors and/or warnings.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.
