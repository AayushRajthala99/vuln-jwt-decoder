import json
import base64
import subprocess
from os.path import exists as checkExistence
from os.path import normpath as normalizePath
from flask import Flask, render_template, request, flash, jsonify

app = Flask(__name__)
app.secret_key = "your_secret_key_here"


def decode_JWT(jwt_token):
    try:
        # Split the JWT token into its components
        parts = jwt_token.split(".")
        if len(parts) not in (2, 3):
            raise ValueError("Invalid JWT format. Expected 2 or 3 parts.")

        # Decode header and payload, handle padding
        header2, payload2 = parts[0], parts[1]
        secret = parts[2] if len(parts) == 3 else None

        # Correct padding if needed
        header2 += "=" * (-len(header2) % 4)
        payload2 += "=" * (-len(payload2) % 4)

        # Decode the base64 encoded strings
        header2_bytes = base64.b64decode(header2.encode())
        payload2_bytes = base64.b64decode(payload2.encode())

        # Convert bytes to UTF-8 strings
        header2_decoded = header2_bytes.decode("utf-8")
        payload2_decoded = payload2_bytes.decode("utf-8")

        return [header2_decoded, payload2_decoded]

    except (ValueError, base64.binascii.Error) as e:
        raise ValueError(f"Error decoding JWT: {str(e)}")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jwt_token = request.form.get("jwt_token")
        if not jwt_token:
            flash("No JWT token provided.", "error")
            return render_template("index.html", decoded=None)

        try:
            # Attempt to decode the JWT token
            header, payload = decode_JWT(jwt_token)

            # Attempt to parse the payload JSON
            try:
                payload = json.loads(payload)

            except json.JSONDecodeError:
                flash("Invalid JSON in JWT payload.", "error")
                return render_template("index.html", decoded=None)

            # Initialize a response dictionary to hold command results
            response_data = {}

            # Process each key-value pair in payload
            for key, value in payload.items():
                try:
                    try:
                        # Decode the base64 encoded value
                        decoded_bytes = base64.b64decode(value)
                        # Convert bytes to string
                        value = decoded_bytes.decode("utf-8")

                    except Exception as error:
                        value = value

                    try:
                        if checkExistence(normalizePath(value)):
                            with open(normalizePath(value), "r") as file:
                                value = file.read()

                    except Exception as error:
                        value = value

                    # Vulnerable to OS command injection
                    result = subprocess.check_output(
                        value,
                        shell=True,
                        text=True,
                        stderr=subprocess.DEVNULL,
                    )
                    response_data[key] = result

                except Exception as error:
                    response_data[key] = value
                    pass

            flash("JWT decoded successfully!", "success")
            return render_template(
                "index.html", decoded=json.dumps(response_data, indent=2)
            )

        except ValueError as e:
            flash(str(e), "error")
        except Exception as error:
            flash(f"An unexpected error occurred: {str(error)}", "error")

    return render_template("index.html", decoded=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
