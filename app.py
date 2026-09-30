from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("my_template.html") # Only the filename, not full path
print(template.render(params={"wv_command": "echo Hello"}))

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
