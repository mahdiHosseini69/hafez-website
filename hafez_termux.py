
import os
import random
from flask import Flask, request, render_template_string

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "local-development-key-change-in-production"
)

poems = [
    {
        "title": "غزل اول",
        "verses": [
            "الا یا ایها الساقی ادر کاسا و ناولها",
            "که عشق آسان نمود اول ولی افتاد مشکل‌ها",
            "به بوی نافه‌ای کآخر صبا زان طره بگشاید",
            "ز تاب جعد مشکینش چه خون افتاد در دل‌ها"
        ],
        "interpretation": "راهی که در پیش داری شاید آسان نباشد، اما با صبر و امید به نتیجه خواهی رسید."
    },
    {
        "title": "غزل دوم",
        "verses": [
            "دوش دیدم که ملائک در میخانه زدند",
            "گل آدم بسرشتند و به پیمانه زدند",
            "ساکنان حرم ستر و عفاف ملکوت",
            "با من راه‌نشین باده مستانه زدند"
        ],
        "interpretation": "نشانه‌های خوبی در مسیر زندگی‌ات وجود دارد. امیدت را از دست نده."
    },
    {
        "title": "غزل سوم",
        "verses": [
            "یوسف گمگشته بازآید به کنعان غم مخور",
            "کلبه احزان شود روزی گلستان غم مخور",
            "ای دل غمدیده حالت به شود دل بد مکن",
            "وین سر شوریده بازآید به سامان غم مخور"
        ],
        "interpretation": "دوران سختی ماندگار نیست. صبر داشته باش و به آینده امیدوار بمان."
    },
    {
        "title": "غزل چهارم",
        "verses": [
            "بر سر آنم که گر ز دست برآید",
            "دست به کاری زنم که غصه سرآید",
            "خلوت دل نیست جای صحبت اضداد",
            "دیو چو بیرون رود فرشته درآید"
        ],
        "interpretation": "زمان آن رسیده که با اراده و تصمیم درست، برای تغییر شرایط اقدام کنی."
    },
    {
        "title": "غزل پنجم",
        "verses": [
            "رسید مژده که ایام غم نخواهد ماند",
            "چنان نماند و چنین نیز هم نخواهد ماند",
            "من ار چه در نظر یار خاکسار شدم",
            "رقیب نیز چنین محترم نخواهد ماند"
        ],
        "interpretation": "شرایط فعلی همیشگی نیست. روزهای بهتر در راه‌اند."
    }
]

HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>فال حافظ</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    padding: 20px;
    min-height: 100vh;
    background: linear-gradient(135deg, #153b32, #27634b);
    font-family: Tahoma, sans-serif;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container {
    background: #fffaf0;
    width: 100%;
    max-width: 540px;
    padding: 30px 22px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 8px 30px #0004;
}
h1 { color: #8b642b; }
.subtitle { color: #666; }
button {
    background: #9b7134;
    color: white;
    border: 0;
    border-radius: 10px;
    padding: 14px 28px;
    font-size: 17px;
    cursor: pointer;
    margin-top: 20px;
}
button:hover { background: #755126; }
.verses {
    line-height: 2.5;
    font-size: 19px;
    color: #254b39;
    margin: 25px 0;
}
.interpretation {
    background: #f2ead8;
    padding: 16px;
    border-radius: 12px;
    line-height: 2;
}
.footer {
    margin-top: 25px;
    color: #888;
    font-size: 12px;
}
</style>
</head>
<body>
<div class="container">
    <h1>🌹 فال حافظ 🌹</h1>
    <p class="subtitle">دلت را به حافظ بسپار و نیت کن</p>

    {% if poem %}
        <h3>{{ poem.title }}</h3>
        <div class="verses">
            {% for verse in poem.verses %}
                {{ verse }}<br>
            {% endfor %}
        </div>
        <div class="interpretation">
            <strong>تعبیر فال:</strong><br>
            {{ poem.interpretation }}
        </div>
    {% else %}
        <p>چشمانت را ببند، نیت کن و روی دکمه زیر بزن.</p>
    {% endif %}

    <form method="POST">
        <button type="submit">گرفتن فال حافظ</button>
    </form>

    <div class="footer">با عشق به شعر و ادب فارسی</div>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    poem = None

    if request.method == "POST":
        poem = random.choice(poems)

    return render_template_string(HTML, poem=poem)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

