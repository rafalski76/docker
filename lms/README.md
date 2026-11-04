# LMS

```
docker build -t lms-app:1.0 .
docker run -d -p 81:80 lms-app:1.0
```

[LMS](https://github.com/chilek/lms) (system dla ISP) na Debianie 13 + PHP 8.4. Obraz pobiera
najnowsze wydanie z GitHuba. Całość z bazą MySQL 8.4 uruchamia `docker compose up -d`.
