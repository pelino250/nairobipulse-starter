def register_routes(app):
    @app.route("/health")
    def health():
        return jsonify({"status": "ok", "service": "nairobipulse"})

    @app.route("/districts")
    def districts():
        return jsonify({
            "districts": ["Westlands", "Kibera", "Karen", "Eastleigh", "Kasarani"]
        })
