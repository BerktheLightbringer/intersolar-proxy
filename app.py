from flask import Flask, jsonify
import requests
import traceback

app = Flask(__name__)

@app.route('/all-exhibitors', methods=['GET'])
def all_exhibitors():
    page = 1
    all_exhibitors = []

    try:
        while True:
            response = requests.post(
                "https://exhibitors.intersolar.de/en/ajax/exhibitorsearch",
                json={
                    "searchText": "",
                    "filters": [],
                    "page": page,
                    "lang": "en"
                },
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            json_data = response.json()

            if "data" not in json_data or "exhibitors" not in json_data["data"]:
                return jsonify({
                    "error": "API yanıtında 'data' veya 'exhibitors' alanı yok.",
                    "full_response": json_data
                }), 500

            exhibitors = json_data["data"]["exhibitors"]
            total_pages = json_data["data"].get("totalPages", 1)

            all_exhibitors.extend(exhibitors)

            if page >= total_pages:
                break
            page += 1

        return jsonify(all_exhibitors)

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)