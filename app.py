from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)


tasks = []
task_id_control = 1


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    task = Task(
        id=task_id_control,
        title=data.get("title"),
        description=data.get("description", "")
    )
    task_id_control += 1

    tasks.append(task)

    return jsonify({
        "message": "Nova tarefa criada com sucesso!",
        "id": task.id
    }), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }

    return jsonify(output)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_details(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()

    request_fields = ["title", "description", "completed"]
    if not any(data.get(field) for field in request_fields):
        return jsonify({"message": "Informe pelo menos um campo para ser atualizado"}), 400

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.completed = data.get("completed", task.completed)

    return jsonify(task.to_dict())


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)

    return jsonify({"message": "Tarefa removida com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
