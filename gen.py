#!/usr/bin/env python3
import os

classes = ["cs220"]
notes = {}

for c in classes:
    notes[c] = list(filter(lambda x: x.endswith('.pdf'), os.listdir(c)))

print(notes)

content = ""

for course in notes:
    content += f"<h1>{course}</h1>"
    for doc in notes[course]:
        content += f"<a href='{course}/{doc}'>{doc}</a>"

print(content)

template = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="max-snippet:20, max-image-preview:large">
    <script src="https://fib.rip/scripts/main.js"></script>
    <link rel="icon" href="k.svg">
    <link rel="stylesheet" href="https://fib.rip/styles/main.css">
    <title>fib.rip</title>

    <script src="https://kit.fontawesome.com/c1a1de4c32.js" crossorigin="anonymous"></script>
</head>

<body class="preload">
    <div id="main">
        <div id="header">
            <span id="title">fib.rip</span>
            <span id="nav">
                <a href="#">projects</a>
                <a href="#">notes</a>
            </span>
        </div>
        <p>
            {content}
        </p>
    </div>
</body>

</html>
"""

with open('./index.html', 'w') as f:
    f.write(template.format(content=content))