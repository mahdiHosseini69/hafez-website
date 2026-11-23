
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
        "verses": [
            "الا یا ایها الساقی ادر کاسا و ناولها",
            "که عشق آسان نمود اول ولی افتاد مشکل‌ها",
            "به بوی نافه‌ای کآخر صبا زان طره بگشاید",
            "ز تاب جعد مشکینش چه خون افتاد در دل‌ها"
        ],
        "meaning": "راهی که در پیش داری شاید آسان نباشد، اما با صبر و امید به نتیجه خواهی رسید."
    },
    {
        "verses": [
            "دوش دیدم که ملائک در میخانه زدند",
            "گل آدم بسرشتند و به پیمانه زدند",
            "ساکنان حرم ستر و عفاف ملکوت",
            "با من راه‌نشین باده مستانه زدند"
        ],
        "meaning": "نشانه‌های خوبی در مسیر زندگی‌ات وجود دارد. امیدت را از دست نده."
    },
    {
        "verses": [
            "یوسف گمگشته بازآید به کنعان غم مخور",
            "کلبه احزان شود روزی گلستان غم مخور",
            "ای دل غمدیده حالت به شود دل بد مکن",
            "وین سر شوریده بازآید به سامان غم مخور"
        ],
        "meaning": "دوران سختی ماندگار نیست. صبر داشته باش و به آینده امیدوار بمان."
    },
    {
        "verses": [
            "بر سر آنم که گر ز دست برآید",
            "دست به کاری زنم که غصه سرآید",
            "خلوت دل نیست جای صحبت اضداد",
            "دیو چو بیرون رود فرشته درآید"
        ],
        "meaning": "زمان آن رسیده که با اراده و تصمیم درست، برای تغییر شرایط اقدام کنی."
    },
    {
        "verses": [
            "رسید مژده که ایام غم نخواهد ماند",
            "چنان نماند و چنین نیز هم نخواهد ماند",
            "من ار چه در نظر یار خاکسار شدم",
            "رقیب نیز چنین محترم نخواهد ماند"
        ],
        "meaning": "شرایط فعلی همیشگی نیست. روزهای بهتر در راه‌اند."
    }
]

HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#123b30">
<title>فال حافظ | باغ شعر پارسی</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    padding: 30px 16px;
    font-family: Tahoma, sans-serif;
    color: #f8f0dc;
    background:
        radial-gradient(ellipse at top, #28604a 0%, transparent 60%),
        linear-gradient(145deg, #0c2922, #174637 55%, #0b261f);
    display: flex;
    justify-content: center;
    align-items: center;
}

.page {
    width: 100%;
    max-width: 650px;
    text-align: center;
}

.top-symbol {
    color: #d9b66b;
    font-size: 42px;
    margin-bottom: 5px;
}

h1 {
    font-size: clamp(32px, 8vw, 48px);
    color: #f2d28c;
    margin: 8px 0;
    letter-spacing: 1px;
}

.subtitle {
    color: #d9d1b9;
    font-size: 15px;
    line-height: 2;
    margin-bottom: 28px;
}

.card {
    background: linear-gradient(145deg, #fff9e9, #eee1c2);
    color: #294b39;
    border: 2px solid #c5a45f;
    border-radius: 20px;
    padding: 30px 20px;
    box-shadow: 0 15px 45px #0005;
    position: relative;
}

.card:before {
    content: "✦";
    color: #b38a3d;
    font-size: 24px;
    display: block;
    margin-bottom: 10px;
}

.card-title {
    color: #9a7131;
    font-size: 21px;
    margin-bottom: 18px;
}

.poem {
    font-size: clamp(16px, 4vw, 20px);
    line-height: 2.5;
    color: #244d38;
    padding: 10px 0;
}

.meaning {
    margin-top: 22px;
    padding: 18px;
    background: #e9dfc5;
    border-right: 4px solid #b38a3d;
    border-radius: 10px;
    line-height: 2.2;
    text-align: right;
    color: #394d3e;
}

.meaning strong {
    display: block;
    color: #936a2c;
    margin-bottom: 8px;
    font-size: 17px;
}

.start-text {
    line-height: 2.2;
    color: #52624f;
    padding: 20px 5px;
}

button {
    border: 1px solid #e7c77e;
    background: linear-gradient(135deg, #d8b66c, #a97b32);
    color: #183b2d;
    border-radius: 12px;
    padding: 15px 35px;
    margin-top: 25px;
    font-family: inherit;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 5px 15px #0002;
    transition: 0.2s;
}

button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px #0003;
}

.bottom {
    color: #d6c69f;
    font-size: 13px;
    line-height: 2;
    margin-top: 24px;
}

@media (max-width: 450px) {
    body {
        padding: 20px 12px;
    }

    .card {
        padding: 25px 15px;
    }

    button {
        width: 100%;
    }
}
</style>
</head>

<body>
<main class="page">

    <div class="top-symbol">❀</div>

    <h1>فال حافظ</h1>

    <div class="subtitle">
        به دنیای شعر و رازهای حافظ خوش آمدی
        <br>
        نیت کن، دلت را آرام کن و فال بگیر
    </div>

    <section class="card">

        {% if poem %}
            <div class="card-title">🌹 غزل امروز تو 🌹</div>

            <div class="poem">
                {% for verse in poem.verses %}
                    {{ verse }}<br>
                {% endfor %}
            </div>

            <div class="meaning">
                <strong>✨ تعبیر فال تو</strong>
                {{ poem.meaning }}
            </div>

        {% else %}
            <div class="card-title">کتاب عشق و معرفت</div>
            <div class="start-text">
                چشمانت را ببند و نیت کن...
                <br>
                بگذار حافظ با زبان شعر با دلت سخن بگوید.
            </div>
        {% endif %}

        <form method="POST">
            <button type="submit">
                ✨ نیت کردم، فال بگیر
            </button>
        </form>

    </section>

    <div class="bottom">
        به یاد خواجه شمس‌الدین محمد حافظ شیرازی
        <br>
        🌿 با عشق به شعر و ادب پارسی 🌿
    </div>

</main>
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
