from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/all-exhibitors', methods=['GET'])
def all_exhibitors():
    page = 1
    all_exhibitors = []
    while True:
        response = requests.post(
            "https://exhibitors.intersolar.de/en/ajax/exhibitorsearch",
            json={"searchText": "", "filters": [], "page": page, "lang": "en"},
            headers={"Content-Type": "application/json"}
        )
        data = response.json()
        exhibitors = data.get("data", {}).get("exhibitors", [])
        total_pages = data.get("data", {}).get("totalPages", page)
        all_exhibitors.extend(exhibitors)
        if page >= total_pages:
            break
        page += 1
    return jsonify(all_exhibitors)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
