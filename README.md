# Docker

[![Lint](https://github.com/rafalski76/docker/actions/workflows/lint.yml/badge.svg)](https://github.com/rafalski76/docker/actions/workflows/lint.yml)

Przykłady tworzenia obrazów Dockera, uruchamiania aplikacji w Docker Compose oraz klastra Docker Swarm.

## Wymagania

- [Docker Engine / Docker Desktop](https://docs.docker.com/get-docker/) z wtyczką Compose v2 (`docker compose`)
- (dla `swarm/`) Vagrant + VirtualBox

## Przykłady

| Katalog | Opis | Obraz bazowy |
| --- | --- | --- |
| [`java/`](java/README.md) | Aplikacja Spring Boot z gotowego JAR-a | `eclipse-temurin:25-jre-alpine` |
| [`php/`](php/README.md) | Strona PHP w Apache | `php:8.5-apache` |
| [`python/`](python/README.md) | Aplikacja Flask 3 | `python:3.14-alpine` |
| [`lms/`](lms/README.md) | [LMS](https://github.com/chilek/lms) + MySQL 8.4 (Docker Compose) | `debian:13-slim` |
| [`swarm/`](swarm/README.md) | Klaster Docker Swarm (Vagrant) i stosy: Portainer, Swarmpit, MySQL + phpMyAdmin, NFS, przykładowa aplikacja z nginx | – |

## Użycie

```shell
cd python
docker build -t python-app:1.0 .
docker run -d -p 8085:9085 python-app:1.0
curl http://localhost:8085
```

Szczegóły (porty, polecenia) znajdziesz w README każdego katalogu.

## Lint / CI

Workflow [`lint.yml`](.github/workflows/lint.yml) uruchamia `hadolint`, `yamllint`, `docker compose config`,
`shellcheck` oraz buduje wszystkie obrazy.
