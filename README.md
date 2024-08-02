# Resti
`Cтатус: В разработке`


Simplified CRM on Django for small businesses in the catering industry

Данная платформа будет включать в себя упрощенную версию CRM. Функционал позволит администрации  заведения значительно облегчить жизнь одним приложением, избавив его от таблиц Excel и 1C и калькулятора на телефоне

## Функционал:

- [x]  **users**: Регистрация администратора или управлющего заведением.
- [x] **businesses**: Создание карточки бизнеса.
- [x] **workers**: Создание карточки работника.
- [ ] **professions**: Список доступных профессий исходя из категории бизнеса (С возможностью добавления уникальной позиции.)
- [ ] **shifts**: Управление сменами и графиком.
- [ ] **salary**: Расчет заработной платы.  (Рассылка чеков лично сотруднику через Телеграмм бота.)
- [ ] **plans**: Постановка планов на месяц и отслеживание их выполненя.
- [ ] **statistics**: Статистика кассы, плана и продаж.
- [ ] **closing**: Алгоритм для закрытия смен.
- [x] **api**: Открытое API  функционала приложения. 


## Стек технологий:

- ЯП - [Python](https://www.python.org/)
- База данных - [PostgreSQL](https://www.postgresql.org/)
- Фреймворк - [Django](https://www.djangoproject.com/) , [DRF](https://www.django-rest-framework.org/)
- Стили - [Bootstrap](https://getbootstrap.com/)
- API
- Вспомогательные инструменты - [Docker](https://www.docker.com/) , [Celery](https://docs.celeryq.dev/en/stable/), [Redis](https://redis.io/), [Nginx](https://nginx.org/ru/)

## Улучшения и оптимизация

- test coverage
- flake8
- poetry
