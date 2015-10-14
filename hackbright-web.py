from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", first=first, last=last, github=github)
    print "%s is the GitHub account for %s %s" % (github, first, last)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Add a student to the database."""
    
    return render_template("student_add.html")



@app.route("/student-display", methods=['POST'])
def student_display():
    """Confirmation page of added student. """

    fname = request.form.get("first_name")
    lname = request.form.get("last_name")
    github = request.form.get("github")
    html = render_template("student_info.html", first=fname, last=lname, github=github)
    hackbright.make_new_student(fname, lname, github)
    print "%s is the GitHub account for %s %s" % (github, fname, lname)
    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
