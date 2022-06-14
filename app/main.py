from flask import Flask, render_template
import os
import random

app = Flask(__name__)

images = [
    "https://psihoman.ru/uploads/posts/2022-02/1645693769_1.jpg",
    "https://psihoman.ru/uploads/posts/2022-02/1645693738_2.jpg",
    "https://i.pinimg.com/originals/db/b0/8a/dbb08a069d1f24c4b61da740198a59cc.jpg",
    "https://i.pinimg.com/736x/97/bc/e9/97bce9aeb1e32af6f0e0bd7cd735df18--baby-animals-baby-cats.jpg",
    "https://oir.mobi/uploads/posts/2021-03/1616364456_11-p-kotyata-anime-11.jpg",
    "https://i.pinimg.com/originals/c4/52/c3/c452c378ca0ef043af6898d44661bcf4.png",
    "https://kartinkin.net/uploads/posts/2021-07/1625848993_11-kartinkin-com-p-oboi-koti-v-kosmose-krasivie-14.jpg",
    "https://krot.info/uploads/posts/2022-03/1647173777_2-krot-info-p-ispugannii-kot-mem-smeshnie-foto-2.jpg",
    "https://sun9-65.userapi.com/impg/LY5xuC_bQfDHheKk2fjSwA8B0ZDBaN8cSHnrMA/L6Wi2x7iEvo.jpg?size=604x338&quality=96&sign=a2b1dbe5e9b576d1b973f22a5b2653b6&type=album",
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
