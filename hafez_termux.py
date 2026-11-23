import os
import random
from flask import (
    Flask, render_template, request,
    redirect, url_for, session
)

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "local-development-key-change-before-production"
)

POEMS = [
    {
        "poem": "یوسف گمگشته بازآید به کنعان، غم مخور\n"
                "کلبه احزان شود روزی گلستان، غم مخور\n\n"
                "ای دل غمدیده حالت به شود، دل بد مکن\n"
                "وین سر شوریده بازآید به سامان، غم مخور",
        "meaning": "این روزها اگر نگرانی یا دشواری در کارهایت هست، "
                   "ناامید نشو. با صبر و امید می‌توانی از روزهای سخت عبور کنی."
    },
    {
        "poem": "دوش وقت سحر از غصه نجاتم دادند\n"
                "و اندر آن ظلمت شب آب حیاتم دادند\n\n"
                "بیخود از شعشعه پرتو ذاتم کردند\n"
                "باده از جام تجلی صفاتم دادند",
        "meaning": "نشانه‌ای از گشایش و روشن‌شدن راه پیش روست. "
                   "با آرامش به ندای دل و خردت گوش بده."
    },
    {
        "poem": "رسید مژده که ایام غم نخواهد ماند\n"
                "چنان نماند و چنین نیز هم نخواهد ماند\n\n"
                "من ار چه در نظر یار خاکسار شدم\n"
                "رقیب نیز چنین محترم نخواهد ماند",
        "meaning": "شرایط سخت همیشگی نیست. با بردباری و اعتمادبه‌نفس "
                   "از این دوره عبور خواهی کرد."
    },
    {
        "poem": "صلاح کار کجا و من خراب کجا\n"
                "ببین تفاوت ره کز کجاست تا به کجا\n\n"
                "دلم ز صومعه بگرفت و خرقهٔ سالوس\n"
                "کجاست دیر مغان و شراب ناب کجا",
        "meaning": "برای رسیدن به خواسته‌ات، راه درست و صادقانه را "
                   "انتخاب کن و به حقیقت نیت خود توجه داشته باش."
    },
    {
        "poem": "اگر آن ترک شیرازی به دست آرد دل ما را\n"
                "به خال هندویش بخشم سمرقند و بخارا را\n\n"
                "بده ساقی می باقی که در جنت نخواهی یافت\n"
                "کنار آب رکن‌آباد و گلگشت مصلا را",
        "meaning": "قدر زیبایی‌ها و فرصت‌های زندگی را بدان. "
                   "شادی و محبت را در زندگی بیشتر کن."
    }
]

PROFILE_FIELDS = (
    "name", "age", "phone", "city", "job", "notes"
)


@app.get("/")
def home():
    return render_template(
        "index.html",
        profile=session.get("profile", {})
    )


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name:
            return render_template(
                "profile.html",
                data=request.form,
                error="لطفاً نام و نام خانوادگی را وارد کن."
            )

        session["profile"] = {
            key: request.form.get(key, "").strip()
            for key in PROFILE_FIELDS
        }

        return redirect(url_for("details"))

    return render_template(
        "profile.html",
        data=session.get("profile", {}),
        error=None
    )


@app.get("/details")
def details():
    data = session.get("profile")

    if not data:
        return redirect(url_for("profile"))

    return render_template(
        "details.html",
        data=data
    )


@app.get("/hafez")
def hafez():
    if not session.get("profile"):
        return redirect(url_for("profile"))

    return render_template(
        "hafez.html",
        fal=session.get("fal")
    )


@app.post("/draw")
def draw():
    if not session.get("profile"):
        return redirect(url_for("profile"))

    session["fal"] = random.choice(POEMS)
    return redirect(url_for("hafez"))


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
