FROM python:3.10-slim

# Pynguin requires this to acknowledge executing third-party code.
# Evaluation (pytest/coverage/mutation) runs on the host pipeline, so the image
# only needs Pynguin itself with its own pinned dependency set.
ENV PYNGUIN_DANGER_AWARE=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=0 \
    PIP_NO_CACHE_DIR=1

RUN pip install --upgrade pip && pip install "pynguin==0.47.0"

COPY pynguin-entrypoint.sh /pynguin-entrypoint.sh
RUN chmod 0755 /pynguin-entrypoint.sh

ENTRYPOINT ["/pynguin-entrypoint.sh"]