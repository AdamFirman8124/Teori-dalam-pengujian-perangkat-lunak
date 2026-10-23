# Patches to retained tool sources

## CoverUp 0.6.3

The active `coverup/` directory is compared against the untouched `dataset/coverup/` copy when publishing the replication package.

Additional experiment fixes made on 2026-10-22:

1. `coverup/src/coverup/utils.py` and `testrunner.py`: disable pytest plugin auto-loading only on Windows. Linux requires `pytest-isolate` and `pytest-repeat`, so globally disabling plugins made `--isolate` and `--count` invalid.
2. `coverup/src/coverup/coverup.py`: write checkpoints through a same-directory temporary file and atomically replace the destination.
3. `coverup/src/coverup/coverup.py`: a generated-test coverage timeout no longer reports success, preventing an unfinished segment from being checkpointed as complete.
4. `coverup/tests/test_checkpoint.py`: verifies a valid atomic checkpoint is emitted.

The protocol proxy independently stores complete JSON request/response bodies, returned model IDs, usage, latency, status, and retry wait. Credentials and authorization headers are never logged.

## CodaMOSA

The active `codamosa/` source contains adaptations relative to the original CodaMOSA interface:

1. Chat-completions payloads for custom OpenAI-compatible endpoints while preserving the original CodaMOSA prompt.
2. Explicit request timeout and bounded transport retry controls.
3. API call telemetry including requested/returned model, usage tokens, latency, status, and response details on errors.
4. Optional local pricing and shared rate-gate hooks.

The experiment proxy remains the authoritative raw request/response record because tool-local telemetry is derived and best-effort.
