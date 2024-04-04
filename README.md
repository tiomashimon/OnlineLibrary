# OnlineLibrary

## Requirements
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

## How to Use
### If you need to run application and database/infrastructure.

1. Clone the repository: `git clone https://github.com/tiomashimon/OnlineLibrary`

2. Create an `.env` file and add your own data following the structure and path of the `.env_example` file.
3. Use `make app` command to run application and database infrastructure.
4. Use `make migrate` command to apply migration and create all needed db.
5. Use `make createsuperuser` command to create admin user.
6. Use `make app-logs` command to follow the logs in app container.




### Available commands:
* `make app` - up application and database infrastructure
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure

* `make container-shell` - go to container shell
* `make migrate` - apply all made migrations
* `make makemigrations` - make migrations to models
* `make createsuperuser` - create admin user
* `make collectstatic` - collect static



# Project Overview

## Introduction
The goal of this project is to develop an online library management system. It aims to provide users with a platform to manage book catalogs, handle borrowing and sales, search and filter books, receive notifications, analyze data, and generate reports.



## Features

## Features

### Core Features
- **Authentication**: User registration and authentication for accessing the system.
- **Cataloging Books**: Ability to add, edit, and delete books in the library catalog.
- **Managing Borrowing**: Functionality to handle book borrowing and returns.
- **Sales and Rentals**: Capability to sell and rent books through the platform.
- **Book Search and Filtering**: Users can search for books based on titles, authors, genres, etc., and apply filters for refined searches.
- **Notifications**: System-generated notifications for due dates, returns, and other relevant events.
- **Analytics and Reports**: Tools for analyzing library data, generating reports on book popularity, borrowing trends, etc.

### User Module
- **Sales Count**: Tracking the number of books sold by users.
- **Borrowing Count**: Monitoring the borrowing activity of users.
- **User Rating**: Implementing a user rating system based on their interactions with the library system.

## Technical Specifications

### Backend
- **Programming Language**: Python 3.11+.
- **Framework**: Django REST Framework.
- **Authentication**: JWT tokens for user authentication.
- **Database**: PostgreSQL.
- **Caching**: Redis or similar technology for response time optimization.
- **Hosting**: Scalable hosting solution to be determined.


### Security
- **HTTPS**: Secure connections.
- **Protection**: Measures against XSS, CSRF, and SQL injections.
- **Access Control**: Implementation of user authentication and authorization rules.
- **Testing**: Unit tests for critical components.

## Testing
- **Automated Testing**: For both backend and frontend components.
- **Manual Testing**: Utilizing tools like Postman for API testing.
- **Load Testing**: To assess scalability and robustness.

## Deployment
- **Dockerization**: Simplify deployment and migration processes.

## Documentation
- **Technical Documentation**: Detailed descriptions of the system architecture, data models, and APIs.
- **Developer and User Guides**: Instructions for both developers and end-users.
- **Regular Updates**: Documentation will be updated with each significant system update.

# Using Git 

- Small & frequent commits
- Aim for linear history: Avoid merge-commits - do fast-forward instead
- NEVER: commit secrets

We follow GitHub flow for branching approach ([Read more](https://docs.github.com/en/get-started/quickstart/github-flow)). In a nutshell:

1. Create a feature branch from `main`
2. Make changes
3. Add tests
4. Add documentation
5. Commit changes & `Push` to `origin`
6. Create a `Pull Request` to `main`

![image](https://github.com/ValeriyFromUA/MarketPlace/assets/97425138/7e0e938b-2dc4-4ce2-a0e1-b9678e98d9bc)


Branching scheme (for now, very simple):

|branch|description|
|---|---|
|main|The main branch. Merge feature branches here.|
| 1-fix_some_issue | Feature and fix branches. Include issue number, so that can be tied to a Github issue. |



##  Conventional comments with commits

Examples:

      feat: add ability to login; Closes #4

      feat(de): a scoped feature for German; Closes #4

      fix: login not working; Closes #4

      docs: add documentation for login; Closes #4

      style: fix indentation; Closes #4

      refactor: login; Closes #4

      perf: login; Closes #4

      test: login; Closes #4

      chore: login; Closes #4

      build: login; Closes #4

      ci: login; Closes #4

      revert: login; Closes #4

# UA VERSION:
# Огляд Онлайн Бібліотеки

## Вступ
Мета цього проекту - розробка онлайн системи управління бібліотекою. Вона спрямована на надання користувачам платформи для управління каталогом книг, обробки позичання та продажу, пошуку та фільтрації книг, отримання сповіщень, аналізу даних та генерації звітів.

## Особливості

### Основні функції
- **Автентифікація**: Реєстрація та автентифікація користувачів для доступу до системи.
- **Каталогізація книг**: Можливість додавання, редагування та видалення книг у бібліотечному каталозі.
- **Управління позичанням**: Функціонал для обробки позичання та повернення книг.
- **Продаж та оренда**: Можливість продажу та оренди книг через платформу.
- **Пошук та фільтрація книг**: Користувачі можуть шукати книги за назвою, авторами, жанрами і т. д., та застосовувати фільтри для уточнени

х пошуків.
- **Сповіщення**: Системні сповіщення про терміни позичання, повернення та інші важливі події.
- **Аналітика та звіти**: Інструменти для аналізу даних бібліотеки, генерації звітів про популярність книг, тенденції позичання та ін.

### Модуль користувача
- **Кількість продажів**: Відстеження кількості проданих книг користувачами.
- **Кількість позичань**: Моніторинг активності позичання книг користувачами.
- **Рейтинг користувача**: Реалізація системи рейтингу користувачів на основі їх взаємодії з бібліотечною системою.

## Технічні специфікації

### Бекенд
- **Мова програмування**: Python 3.11+.
- **Фреймворк**: Django REST Framework.
- **Автентифікація**: OAuth 2.0 для інтеграції з Google акаунтами.
- **База даних**: PostgreSQL.
- **Кешування**: Redis або аналогічна технологія для оптимізації часу відповіді.
- **Хостинг**: Рішення для масштабування відповідно до навантаження.


### Безпека
- **HTTPS**: Захищені з'єднання.
- **Захист**: Заходи проти XSS, CSRF та SQL ін'єкцій.
- **Контроль доступу**: Впровадження правил аутентифікації та авторизації користувачів.
- **Тестування**: Unit-тести для критичних компонентів.

## Тестування
- **Автоматизоване тестування**: Для компонентів бекенду та фронтенду.
- **Ручне тестування**: Використання інструментів на кшталт Postman для тестування API.
- **Навантажувальні тести**: Для оцінки масштабованості та стабільності.

## Розгортання
- **Докеризація**: Спрощення процесу розгортання та міграції.

## Документація
- **Технічна документація**: Детальний опис архітектури системи, моделей дани
