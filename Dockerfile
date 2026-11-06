#Build Stage
FROM python:3.12-slim-bookworm AS builder 

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

COPY app/requirements.txt .

RUN pip install \
    --no-cache-dir \
    --prefix=/install \
    -r requirements.txt

#Runtime Stage
FROM python:3.12-slim-bookworm AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/install/lib/python3.12/site-packages \
    PATH="/install/bin:${PATH}" \
    PORT=5000

WORKDIR /app

COPY --from=builder /install /install

COPY app/app.py .

RUN useradd --no-create-home --uid 10001 python_user \
    && chown -R python_user:python_user /app

USER 10001

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
