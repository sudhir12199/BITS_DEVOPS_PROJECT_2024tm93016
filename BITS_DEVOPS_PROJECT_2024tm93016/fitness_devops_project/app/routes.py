from flask import Blueprint, jsonify, request

bp = Blueprint("routes", __name__)

# In-memory "database"
workouts = []

@bp.get("/")
def index():
    return jsonify({"message": "Welcome to ACEest_Fitness API", "status": "running"}), 200

@bp.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@bp.post("/add_workout")
def add_workout():
    data = request.get_json(force=True)
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or not duration:
        return jsonify({"error": "Workout and duration required"}), 400

    try:
        duration = int(duration)
    except ValueError:
        return jsonify({"error": "Duration must be a number"}), 400

    workouts.append({"workout": workout, "duration": duration})
    return jsonify({"message": f"{workout} added successfully!", "count": len(workouts)}), 201

@bp.get("/workouts")
def get_workouts():
    return jsonify({"workouts": workouts, "count": len(workouts)}), 200


