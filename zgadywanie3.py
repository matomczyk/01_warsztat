from flask import Flask, request, render_template

app = Flask(__name__)
start_html = """
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <p>Pomyśl liczbę od 1 do 1000</p>
<form action="/zgaduj" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="Wyślij">
</form>

</body>
</html>"""

main_html = """
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>

<body>
<p>Zgaduję {message}</p>
<form action="/zgaduj" method="POST">
                    <button type="submit"
                            name = "answer"
                            value="too small">
                            Too small
                    </button>
                    <button type="submit"
                            name = "answer"
                            value="too big">
                            Too big
                    </button>
                    <button type="submit"
                            name = "answer"
                            value="you won">
                            You won
                    </button>
                <input type="hidden" name="min" value="{min}">
                <input type="hidden" name="max" value="{max}">
            </form>
</body>
</html>"""

@app.route('/zgaduj', methods=["GET", "POST"])
def zgadywanie():
    if request.method == "GET":
        return start_html.format(1, 1000)
    else:
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        answer = request.form.get("answer")
        guess = (max - min) // 2 + min

        if answer == "too big":
            max = guess
        elif answer == "too small":
            min = guess
        elif answer == "you won":
            return """
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <h1>Wygrałeś</h1>
</form>
</body>
</html>"""

        guess = (max- min) // 2 + min

        return main_html.format(message=guess, min=min, max=max)


if __name__ == '__main__':
    app.run()
