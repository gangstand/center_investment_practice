FROM python:3.10-slim-buster as builder
EXPOSE 80
EXPOSE 443
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
COPY .env .
COPY manage.py .
COPY /settings ./settings
COPY /internship ./internship
COPY /users ./users
COPY /templates ./templates
COPY /static ./static
COPY /chat ./chat
COPY /chat ./chat
COPY /practicum ./practicum
RUN pip install --upgrade pip && pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
FROM python:3.10-slim-buster
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
COPY --from=builder /app/.env .
COPY --from=builder /app/manage.py .
COPY --from=builder /app/settings ./settings
COPY --from=builder /app/internship ./internship
COPY --from=builder /app/users ./users
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/static ./static
COPY --from=builder /app/chat ./chat
COPY --from=builder /app/practicum ./practicum
RUN pip install --no-cache /wheels/* && python manage.py collectstatic --noinput