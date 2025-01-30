[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/Tes3awy/cisco-catalyst-center-webhooks)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Tes3awy/cisco-catalyst-center-webhooks)
![GitHub contributors](https://img.shields.io/github/contributors/Tes3awy/cisco-catalyst-center-webhooks)
![GitHub Issues or Pull Requests by label](https://img.shields.io/github/issues/Tes3awy/cisco-catalyst-center-webhooks/gh)
![GitHub Issues or Pull Requests by label](https://img.shields.io/github/issues-pr/Tes3awy/cisco-catalyst-center-webhooks/gh)
![GitHub License](https://img.shields.io/github/license/Tes3awy/cisco-catalyst-center-webhooks)


# Webhook Testing with Cisco Catalyst Center (a.k.a DNA Center)

This project is a Proof of Concept (PoC) for the use of webhooks with Cisco SDN solutions, specifically integrating with Cisco Catalyst Center. It leverages a Flask application to receive and process webhook notifications in real-time, showcasing how events from the Cisco Catalyst Center can be handled programmatically.

# Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Security Considerations/Improvements](#security-considerationsimprovements)
- [Debugging Tips](#debugging-tips)
- [Preview](#preview)
- [References](#references)
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

3. Install SQLite3

> Linux

```bash
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install sqlite3 -y
$ sqlite3 --version
```

> Windows

Follow this [tutorial](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/SQLite3-How-to-download-and-install-SQLite-on-Windows-version-latest-tutorial)

4. Install dependencies

```bash
(.venv)$ pip install -r requirements.txt
```

5. Set _private_ environment variables

Create a `.env` file in the root directory and add the following:

```env
BASIC_AUTH_USERNAME="USERNAME"
BASIC_AUTH_PASSWORD="PASSWORD"
```

6. Run the application

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

7. Configure Cisco Catalyst Center

- Navigate to **System > Settings > External Services > Destination > Webhook** in the Catalyst Center dashboard.
- Add a new POST webhook with the Webhook URL `https://<ip_address>:5443/api/v1/webhook`.
- For the Trust Certificate radio button, choose **No**.
- For Authentication, choose **Basic** and set the required headers: 
  - `Content-Type: application/json`
  - `Authorization: Basic <BASE64 of username:password>`
- Configure a webhook destination for an event. _(Refer to the references section)_

## Usage

Once the application is running, it will listen for webhook notifications from Cisco Catalyst Center. When a notification is received, it will be displayed on the dashboard in real-time.

## Security Considerations/Improvements

- Use HTTPs to secure webhook communications.
- Validate all incoming requests using a custom authentication token.

## Debugging Tips

Check the Flask application logs in the terminal for errors and/or warnings.

## Preview
![Dashboard](assets/dashboard.png)

## References

- [Configure a Webhook Destination](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center-platform/2-3-7/user-guide/b-dnac-platform-ug-2-3-7/b-dnac-platform-ug-2-3-7-chapter-0101.html#Cisco_Task_in_List_GUI.dita_e24b1b78-ea6e-4aa5-932a-359e04d4122f)
- [Work with Event Notifications](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center-platform/2-3-7/user-guide/b-dnac-platform-ug-2-3-7/b-dnac-platform-ug-2-3-7-chapter-0111.html#Cisco_Task_in_List_GUI.dita_ca236611-5a22-4c83-9a65-22d98a28b98e)
- [Get Webhook'd - How to Build your Cisco DNA Center Integration](https://dcl3wxcscqm28.cloudfront.net/8130338649073540/4521856223995780/TECH%2041%20GetWebhooked.pdf)
- [WebSockets and Webhooks - Embed network intelligence into your applications](https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2024/pdf/DEVNET-1841.pdf)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.
