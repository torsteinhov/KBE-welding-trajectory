from app import app # treat it like a package
from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/profile.html")