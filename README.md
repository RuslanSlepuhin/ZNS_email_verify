--------------------------1------------------------------
Регистрация пользователя:
http://https://zns-token.herokuapp.com/auth/users/
JSON 
{
    "email": "oms.ruslan@gmail.com",
    "password": "automobile1902",
    "re_password": "automobile1902"
}
Отправляет письмо на указанный адрес со ссылкой uid/token

--------------------------2------------------------------
Верификация пользователя:
http://https://zns-token.herokuapp.com/auth/users/activation/
JSON
{
    "uid": "MTc",
    "token": "b7oz69-b03076ce074784cfdce4bde74fa6a122"
}
Отправляет письмо об успешной верификации. Но нужна теперь авторизация

--------------------------3------------------------------
Авторизация пользователя:
http://https://zns-token.herokuapp.com/auth/jwt/create/
JSON
{
    "email": "oms.ruslan@gmail.com",
    "password": "automobile1902"
}
Ответом выдает пару JWT токенов

--------------------------4------------------------------
Запрос на access токен на основе refresh
http://https://zns-token.herokuapp.com/auth/jwt/refresh/
JSON
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NjQzMzY0NCwianRpIjoiMWMyZjQzYTBhYzVjNDY5OGFmMmZhMDMzNGVjOGFlMzAiLCJ1c2VyX2lkIjoxN30.NOyH9oKGwmw4OCEpIbf1Ct3eLZhDoD6NvCFGbCIFbVM"
}

--------------------------5------------------------------
Сброс пароля пользователя
http://https://zns-token.herokuapp.com/auth/users/reset_password/
JSON
{
    "email": "oms.ruslan@gmail.com"
}
Ответом приходит письмо со ссылкой на почту с uid,token

--------------------------6------------------------------
Присвоение нового пароля пользователю:
http://https://zns-token.herokuapp.com/auth/users/reset_password_confirm/
JSON
{
    "uid": "MTc",
    "token": "b7p0ev-854e0ccd0469ccd887f3d88c0b60ec7f",
    "new_password": "TheNewPassword",
    "re_new_password": "TheNewPassword"
}
