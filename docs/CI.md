# CI/CD — лабораторная №5

**Автор:** Ананенко Дмитрий Сергеевич, М3215  
**Репозиторий:** https://github.com/K0DDO/geometric_lib

## Что сделано

Файл `.github/workflows/main.yml`:
- запускается на `push` / `pull_request` в `main` и вручную (`workflow_dispatch`)
- job `build` на `ubuntu-latest`
- гоняет тесты ЛР4: `python -m unittest discover tests -v`
- у шага с тестами стоит `continue-on-error: true`

## Как посмотреть результат

1. Открыть репозиторий на GitHub
2. Вкладка **Actions**
3. Выбрать последний workflow **CI**
4. Сделать скриншот для отчёта

## Как писать такой файл (по материалам из лабы)

Полезные ссылки из задания:

- [Beginner's guide to CI/CD on GitHub](https://github.blog/2022-06-03-a-beginners-guide-to-ci-cd-and-automation-on-github/)
- [Хабр: GitHub Actions для начинающих](https://habr.com/ru/articles/711278/)

Коротко по шагам:

1. **CI** — проверка кода на сервере после изменений.  
   **CD** — дальше уже выкладка; в этой лабе нужен только CI.

2. В корне репозитория создаёшь папки:  
   `.github/workflows/`

3. Внутри кладёшь YAML-файл. В лабе имя фиксированное: **`main.yml`**.

4. В файле обычно есть блоки:
   - `name` — название workflow (видно во вкладке Actions)
   - `on` — когда запускать (`push`, `pull_request`, …)
   - `jobs` — что именно делать
   - `runs-on` — на какой машине (`ubuntu-latest`, `windows-latest`, …)
   - `steps` — шаги по порядку

5. Типичные шаги для Python-тестов:
   - `actions/checkout` — скачать код репозитория
   - `actions/setup-python` — поставить Python
   - `run: ...` — команда запуска тестов

6. Чтобы гонять на двух ОС сразу, используют `strategy.matrix` со списком `os`.

7. После `git push` GitHub сам подхватывает workflow.  
   Смотри результат: **Actions** → нужный запуск → зелёная/красная галочка.

8. Для отчёта по лабе приложи:
   - сам `main.yml`
   - скриншот из **Actions**
