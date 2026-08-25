FROM python:3.10-alpine AS builder

COPY requirements.txt /tmp
RUN pip install --no-cache-dir --prefix=/install -r /tmp/requirements.txt

FROM python:3.10-alpine AS runtime

COPY --from=builder /install /usr/local

COPY ./src/ src

USER 1000:1000

ENV PORT=5000

CMD ["python", "/src/app.py"]