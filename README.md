# Vulnerable JWT Decoder Application

This project is a Flask-based web application that decodes JSON Web Tokens (JWT). It demonstrates various vulnerabilities, including Cross Site Scripting (XSS), HTML Injection (HTMLi), Local File Inclusion (LFI), and OS Command Injection (OSi). The application also supports the payloads for above mentioned vulnerabilities in its Base64 encoded form as well.

## Author
[AayushRajthala99](https://github.com/AayushRajthala99)

## Features
- Decode JWT tokens and display the header and payload.
- Process key-value pairs from the JWT payload.
- Vulnerable to various security issues for educational purposes.
- The application supports Base64 encoded payloads in the JWT Token.

## Requirements
- Python 3.9 or higher
- Flask
- Other dependencies listed in `requirements.txt`

## Additional Tools
- [JWT Generator](https://www.javainuse.com/jwtgenerator) 
- [JWT Debugger](https://jwt.io)
- [CyberChef](https://cyberchef.io)

## Installation
### With Docker
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AayushRajthala99/jwt-decoder.git
   cd jwt-decoder
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t jwt_decoder .
   ```

3. **Run the Docker container:**
   ```bash
   docker-compose up
   ```

4. **Access the application:**
   Open your web browser and navigate to `http://localhost:5000`.

### Without Docker (Manually)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AayushRajthala99/jwt-decoder.git
   cd jwt-decoder
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
    
   `source venv/bin/activate` # On Linux
   
   `.venv\Scripts\activate` # On Windows
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Vulnerabilities
This application is intentionally designed to demonstrate the following vulnerabilities:
1. **XSS (Cross-Site Scripting)**: User input is not properly sanitized.
   ```
   # Simple XSS alert in Base64 Encoded form : PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

   eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkpvaG4gRG9lIiwiUGF5bG9hZCI6IlBITmpjbWx3ZEQ1aGJHVnlkQ2d4S1R3dmMyTnlhWEIwUGc9PSIsImV4cCI6MTczMTM5NTI2NiwiaWF0IjoxNzMxMzk1MjY2fQ.yxd_05W1DKRL3ARCChMIDOIpGL-SyQKpOlU_VzTL3XY  
   ```
2. **HTML Injection**: HTML content can be injected into the application.
   ```
   # Simple HTML injection : <h1>Hello World!</h1>

   eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkpvaG4gRG9lIiwiUGF5bG9hZCI6IjxoMT5IZWxsbyBXb3JsZCE8L2gxPiIsImV4cCI6MTczMTM5NTI2NiwiaWF0IjoxNzMxMzk1MjY2fQ.anq4qwmKI1Fw2tf9F0XVEeBM33WnleRxx23b1is1JOo
   ```
3. **LFI (Local File Inclusion)**: Local files can be accessed through user input.
   ```
   # Simple HTML injection : secret/.env
   
   eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkpvaG4gRG9lIiwiUGF5bG9hZCI6InNlY3JldC8uZW52IiwiZXhwIjoxNzMxMzk1MjY2LCJpYXQiOjE3MzEzOTUyNjZ9.hXoZ-Ozflxs3i1vhpDv9qJT-X4PnDRFKuSCWKnMxWbI
   ```
4. **OS Command Injection**: User input can be executed as shell commands.
   ```
   # Simple HTML injection : whoami
   
   eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkpvaG4gRG9lIiwiUGF5bG9hZCI6Indob2FtaSIsImV4cCI6MTczMTM5NTI2NiwiaWF0IjoxNzMxMzk1MjY2fQ.h58M0o2fLT49ni8bec9OAE8PqzdIHECq5W6hZ3yNeRw
   ```

## Usage
1. Enter a JWT token in the input field on the homepage.
2. Click the submit button to decode the token.
3. The decoded header and payload will be displayed on the page.

## License
This project is open-source and available under the MIT License. 

Feel free to contribute or report issues on the [GitHub repository](https://github.com/AayushRajthala99/vuln-jwt-decoder).
