# PR_Trial

Тестовое задание для PRодвижения.

"""
Алиса очень любит Twitter, но после всех попыток Труди вмешаться в её переписку с Бобом, она переживает о своей безопасности и не хочет использовать сторонние сервисы для сокращения ссылок (например, https://goo.gl). Помогите Алисе написать такой сервис на Django.

1) Алиса не любит сложные интерфейсы, поэтому весь сервис должен представлять собой поле ввода ссылки и кнопку отправки формы. Алиса предпочитает Bootstrap, но не принципиальна в этом вопросе.
2) Алиса боится, что Труди может начать сокращать ссылки на её сервисе, поэтому доступ к сервису должен осуществляться только по связке логин/пароль. Алиса планирует заводить учётные записи через админку.
3) Если Труди всё же удастся воспользоваться сервисом, то Алиса не хочет, чтобы Труди могла сокращать потенциально вредоносные ссылки с относительными путями и протоколами отличными от HTTP(S).
4) Алиса хочет видеть как часто люди переходят по её ссылкам, поэтому количество уникальных переходов по ссылке должно сохраняться и отображаться в админке.
5) Алиса хочет дать доступ к сервису Бобу и иметь возможность отфильтровать в админке её ссылки от ссылок Боба.
"""

Заведенные пользователи:
 - alice - администратор (пароль: strongpassword)
 - bob - пользователь (пароль: bobspassword)

Принятые критерии уникальности перехода:
  - Один IP-адрес - один переход.
  - Если последний переход с IP-адреса был позже суток с текущего момента, то переход с этого адреса вновь считается уникальным.
