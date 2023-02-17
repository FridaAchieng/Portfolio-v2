from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
      {"id" :1,
      "title" : "Python",
      "desc" :" EDA"
      },
  {"id" :1,
      "title" : "Excel",
      "desc" :" Dashboard"
      },
  {"id" :1,
      "title" : "Tableau",
      "desc" :" Dashboard"
      },
  {"id" :1,
      "title" : "SQL",
      "desc" :"Data Exploration"
      }

]


@app.route("/")
def hello_world():
  return render_template("home.html",projects= PROJECTS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
