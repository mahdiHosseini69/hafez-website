from flask import Flask, render_template_string, request, redirect, url_for, session
import os


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")import random

POEMS = [
    {
        "poem": "یوسف گمگشته بازآید به کنعان، غم مخور\nکلبه احزان شود روزی گلستان، غم مخور\n\nای دل غمدیده حالت به شود، دل بد مکن\nوین سر شوریده بازآید به سامان، غم مخور",
        "meaning": "این روزها اگر نگرانی یا دوری و دشواری در کارهایت هست، ناامید نشو. اوضاع می‌تواند بهتر شود؛ صبور باش و امیدت را حفظ کن."
    },
    {
        "poem": "دوش وقت سحر از غصه نجاتم دادند\nو اندر آن ظلمت شب آب حیاتم دادند\n\nبیخود از شعشعه پرتو ذاتم کردند\nباده از جام تجلی صفاتم دادند",
        "meaning": "نشانه‌ای از گشایش و روشن‌شدن راه پیش روست. با آرامش به ندای دل و خردت گوش بده و فرصت‌های تازه را جدی بگیر."
    },
    {
        "poem": "رسید مژده که ایام غم نخواهد ماند\nچنان نماند و چنین نیز هم نخواهد ماند\n\nمن ار چه در نظر یار خاکسار شدم\nرقیب نیز چنین محترم نخواهد ماند",
        "meaning": "شرایط سخت همیشگی نیست. با بردباری و اعتمادبه‌نفس از این دوره عبور می‌کنی؛ در تصمیم‌ها عجله نکن."
    },
    {
        "poem": "صلاح کار کجا و من خراب کجا\nببین تفاوت ره کز کجاست تا به کجا\n\nدلم ز صومعه بگرفت و خرقهٔ سالوس\nکجاست دیر مغان و شراب ناب کجا",
        "meaning": "برای رسیدن به خواسته‌ات لازم است راه درست و صادقانه را انتخاب کنی. به جای ظاهر امور، به حقیقت و نیت خود توجه کن."
    },
    {
        "poem": "اگر آن ترک شیرازی به دست آرد دل ما را\nبه خال هندویش بخشم سمرقند و بخارا را\n\nبده ساقی می باقی که در جنت نخواهی یافت\nکنار آب رکن‌آباد و گلگشت مصلا را",
        "meaning": "قدر زیبایی‌ها و فرصت‌های زندگی را بدان. شادی و محبت را در کنار خودت و اطرافیانت بیشتر کن."
    },
]

BASE = r"""
<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ title }} | دفتر من و فال حافظ</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800&display=swap');
:root{--bg:#f4f1e9;--card:#fffdf8;--ink:#24352f;--muted:#68766e;--green:#176b55;--gold:#c49a45;--line:#e8e1d2}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(circle at top right,#e9e0cb,transparent 40%),var(--bg);color:var(--ink);font-family:'Vazirmatn',Tahoma,sans-serif;min-height:100vh;padding:22px}
main{max-width:760px;margin:28px auto}
header{text-align:center;margin-bottom:22px}
.logo{font-size:34px}
h1{font-size:25px;margin:8px 0;color:var(--green)}
.subtitle{color:var(--muted);font-size:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:25px;box-shadow:0 14px 40px #354b3b12}
.steps{display:flex;gap:8px;margin:0 0 20px}
.step{flex:1;text-align:center;border-radius:12px;padding:9px 4px;background:#eeeadd;color:#7b8178;font-size:12px}
.step.active{background:#dcebe3;color:var(--green);font-weight:700}
label{display:block;font-weight:600;margin:13px 0 6px;font-size:14px}
input,textarea{width:100%;border:1px solid #dcd6c8;border-radius:12px;padding:12px 13px;font:inherit;background:#fffefa;color:var(--ink);outline:none}
input:focus,textarea:focus{border-color:var(--green);box-shadow:0 0 0 3px #176b5515}
textarea{min-height:90px;resize:vertical}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:0 14px}
.btn{display:inline-block;border:0;border-radius:12px;padding:12px 19px;background:var(--green);color:white;text-decoration:none;font:600 14px 'Vazirmatn',Tahoma,sans-serif;cursor:pointer}
.btn.secondary{background:#eeeadd;color:var(--ink)}
.btn.gold{background:#a77b2d}
.actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}
.data{width:100%;border-collapse:collapse}
.data td{padding:12px 8px;border-bottom:1px solid var(--line);vertical-align:top}
.data td:first-child{width:34%;color:var(--muted);font-weight:600}
.poem{text-align:center;white-space:pre-line;font-size:20px;line-height:2.2;color:#59452c;padding:20px 10px}
.meaning{background:#f4f0e5;border-right:4px solid var(--gold);padding:15px 17px;border-radius:12px;line-height:2}
footer{text-align:center;color:var(--muted);font-size:12px;margin:18px}
@media(max-width:560px){body{padding:12px}main{margin:12px auto}.card{padding:18px}.grid{grid-template-columns:1fr}h1{font-size:21px}.poem{font-size:17px}}
@media print{body{background:white;padding:0}.card{box-shadow:none;border:0}header,.steps,.actions,footer{display:none!important}main{margin:0}.print-title{display:block!important}}
</style>
</head>
<body>
<main>
<header><div class="logo">🌿 📜</div><h1>دفتر من و فال حافظ</h1><div class="subtitle">مشخصات خودت را ثبت کن و با نیت پاک فال بگیر</div></header>
<div class="steps">
  <div class="step {{ 'active' if step==1 else '' }}">۱. اطلاعات</div>
  <div class="step {{ 'active' if step==2 else '' }}">۲. مشخصات</div>
  <div class="step {{ 'active' if step==3 else '' }}">۳. فال حافظ</div>
</div>
<section class="card">{{ content|safe }}</section>
<footer>این برنامه به‌صورت محلی روی گوشی شما اجرا می‌شود.</footer>
</main>
</body></html>
"""

FORM = r"""
<h2>مشخصات خودت را وارد کن</h2>
<form method="post" action="{{ url_for('save') }}">
<div class="grid">
<div><label>نام و نام خانوادگی *</label><input name="name" required value="{{ data.get('name','') }}" placeholder="مثلاً علی رضایی"></div>
<div><label>سن</label><input name="age" inputmode="numeric" value="{{ data.get('age','') }}" placeholder="مثلاً ۲۵"></div>
<div><label>شماره تماس</label><input name="phone" inputmode="tel" value="{{ data.get('phone','') }}" placeholder="شماره تماس"></div>
<div><label>شهر محل سکونت</label><input name="city" value="{{ data.get('city','') }}" placeholder="نام شهر"></div>
<div style="grid-column:1/-1"><label>شغل یا تحصیلات</label><input name="job" value="{{ data.get('job','') }}" placeholder="شغل یا رشته تحصیلی"></div>
</div>
<label>توضیحات بیشتر</label><textarea name="notes" placeholder="هر توضیحی که دوست داری...">{{ data.get('notes','') }}</textarea>
<div class="actions"><button class="btn" type="submit">ذخیره و ادامه ←</button></div>
</form>
"""

DETAILS = r"""
<h2 class="print-title">مشخصات ثبت‌شده</h2>
<table class="data">
{% for label,key in fields %}
<tr><td>{{ label }}</td><td>{{ data.get(key) or '—' }}</td></tr>
{% endfor %}
</table>
<div class="actions">
<button class="btn gold" onclick="window.print()">چاپ / ذخیره PDF</button>
<a class="btn secondary" href="{{ url_for('home') }}">ویرایش اطلاعات</a>
<a class="btn" href="{{ url_for('hafez') }}">رفتن به فال حافظ ←</a>
</div>
"""

HAFEZ = r"""
<h2 style="text-align:center">🌹 فال حافظ 🌹</h2>
<p style="text-align:center;color:var(--muted)">لحظه‌ای آرام باش، نیت کن و دکمه زیر را بزن.</p>
{% if fal %}
<div class="poem">{{ fal.poem }}</div>
<h3>تعبیر فال</h3><div class="meaning">{{ fal.meaning }}</div>
{% else %}
<div class="poem">✨ نیت کن تا فال تو آشکار شود ✨</div>
{% endif %}
<div class="actions" style="justify-content:center">
<form method="post" action="{{ url_for('draw') }}"><button class="btn gold" type="submit">گرفتن فال حافظ</button></form>
<a class="btn secondary" href="{{ url_for('details') }}">بازگشت به مشخصات</a>
</div>
"""

@app.get("/")
def home():
    data = session.get("profile", {})
    return render_template_string(BASE, title="ورود اطلاعات", step=1,
                                  content=render_template_string(FORM, data=data))

@app.post("/save")
def save():
    session["profile"] = {k: request.form.get(k, "").strip()
                          for k in ("name", "age", "phone", "city", "job", "notes")}
    return redirect(url_for("details"))

@app.get("/details")
def details():
    if not session.get("profile"):
        return redirect(url_for("home"))
    fields = [("نام و نام خانوادگی", "name"), ("سن", "age"),
              ("شماره تماس", "phone"), ("شهر", "city"),
              ("شغل یا تحصیلات", "job"), ("توضیحات", "notes")]
    content = render_template_string(DETAILS, data=session["profile"], fields=fields)
    return render_template_string(BASE, title="مشخصات", step=2, content=content)

@app.get("/hafez")
def hafez():
    content = render_template_string(HAFEZ, fal=session.get("fal"))
    return render_template_string(BASE, title="فال حافظ", step=3, content=content)

@app.post("/draw")
def draw():
    session["fal"] = random.choice(POEMS)
    return redirect(url_for("hafez"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
