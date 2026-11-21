FROM python:3.12-slim-bookworm AS prepared
WORKDIR /app
COPY . .
RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]
FROM prepared AS test
RUN ["python", "-m", "pytest"]
FROM prepared AS runtime
USER 10001:10001
EXPOSE 8201
ENTRYPOINT []
CMD ["uvicorn", "unit_converter.app:app", "--host", "0.0.0.0", "--port", "8201"]
