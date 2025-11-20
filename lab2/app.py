from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Головна</title></head>
        <body>
            <h1>Ласкаво просимо на сайт новин</h1>
            <ul>
                <li><a href="/latest">Нові новини</a></li>
                <li><a href="/today">Новини дня</a></li>
                <li><a href="/all">Усі новини</a></li>
            </ul>
        </body>
    </html>
    """

@app.get("/latest", response_class=HTMLResponse)
def latest_news():
    return """
    <html>
        <head><title>Нові новини</title></head>
        <body>
            <h1>Останні новини</h1>
            <h3>📌 Україна запустила новий супутник!</h3>
            <h3>📌 Вчені відкрили новий метод збереження енергії.</h3>
            <a href="/">Назад</a>
        </body>
    </html>
    """

@app.get("/today", response_class=HTMLResponse)
def today_news():
    return """
    <html>
        <head><title>Новини дня</title></head>
        <body>
            <h1>Головні новини дня</h1>
            <h3>✅ Курс гривні стабільний.</h3>
            <h3>✅ У Києві відкрили новий парк.</h3>
            <a href="/">Назад</a>
        </body>
    </html>
    """

@app.get("/all", response_class=HTMLResponse)
def all_news():
    return """
    <html>
        <head><title>Усі новини</title></head>
        <body>
            <h1>Усі новини</h1>
            <h3>- Україна запустила новий супутник.</h3>
            <h3>- Вчені відкрили новий метод збереження енергії.</h3>
            <h3>- Курс гривні стабільний.</h3>
            <h3>- У Києві відкрили новий парк.</h3>
            <a href="/">Назад</a>
        </body>
    </html>
    """
