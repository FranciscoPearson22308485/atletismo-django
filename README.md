# Atletismo Django — Exercício 9

Implementação Django MVT de torneios de atletismo.

## Modelos

- Atleta
- Torneio (N:M com Atleta)
- Prova (1:N com Torneio)

## Vistas

- `/torneios/` — lista torneios com provas e atletas
- `/atletas/` — lista atletas com os seus torneios

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Autor:** Francisco Pearson — 22308485 | Universidade Lusófona · PW 2025/26
