#!/usr/bin/env bash
gunicorn server.api:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:10000
