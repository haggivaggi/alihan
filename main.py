import streamlit as magic
magic.set_page_config(
page_title="мое приложение",
page_icon=":rocket:"
)
magic.write("мой первый сайт на python")

magic.header("Это header")

magic.subheader("это subheader")

text = magic.text_input("Введите что нибудь")

magic.write(text)

calculator = magic.text_input("калькулятор")

if calculator:

    magic.write(eval(calculator))

slider = magic.slider("Выбери число", 0,100)

magic.write(slider)

data = magic.date_input("выберите дату")

digit=magic.number_input(
    "Выберите цифру",
    0,
    10
)

click = magic.button("Нажми меня")

if click:
    magic.write(click)
    magic.snow()
click_img = magic.button(
"Нажми на меня и я покажу каритнку"

)

if click_img:
    magic.image(
"screen-0.webp",
caption="ssss"
    )


magic.video(
"https://www.youtube.com/watch?v=js91jn8nX8o",
    format="video/mp4"
)

with magic.form(key="my_form"):

    name = magic.text_input("Имя")
    password = magic.text_input("Пароль")
    submit = magic.form_submit_button(
"Нажми на меня"


)

if submit:
    magic.success("ураааааааааааа")


picture = magic.camera_input("Take a picture")

if picture:

    magic.image(picture)










