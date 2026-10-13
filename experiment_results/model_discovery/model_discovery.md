# Model Discovery Report

- **Run time (UTC):** 2026-10-13T04:22:03Z
- **Provider:** https://router.octalabs.id/v1
- **Models endpoint:** https://router.octalabs.id/v1/models
- **Models listed:** 58
- **Available now:** 14
- **Unavailable:** 5
- **List succeeded:** True

## Available models

- `claude-fable-5-1`
- `claude-opus-4-6`
- `claude-opus-4-7`
- `claude-opus-4-8`
- `claude-opus-5`
- `claude-sonnet-5`
- `gpt-5.5`
- `gpt-5.6-luna`
- `gpt-5.6-sol`
- `gpt-5.6-terra`
- `gpt-6-astra`
- `gpt-6-luna`
- `gpt-6-sol`
- `gpt-6.1-sol`

## Unavailable models

- `claude-fable-5` - HTTP 503: {"error":{"code":"upstream_unavailable","message":"all combo providers are temporarily unavailable","param":null,"type":"server_error"}}
- `claude-opus-5-5` - HTTP 502: error code: 502
- `claude-sonnet-4-6` - HTTP 402: {"error":{"code":"upstream_error","message":"The upstream service could not complete the request.","param":null,"type":"server_error"}}
- `claude-sonnet-5-5` - HTTP 502: error code: 502
- `gpt-image-1.5` - HTTP 503: {"error":{"code":"upstream_error","message":"The upstream service could not complete the request.","param":null,"type":"server_error"}}

## Notes

- Configured models: claude-sonnet-5, gpt-5.5
- Using GPT/Claude models (cap=none): claude-fable-5-1, claude-opus-4-6, claude-opus-4-7, claude-opus-4-8, claude-opus-5, claude-sonnet-5, gpt-5.5, gpt-5.6-luna, gpt-5.6-sol, gpt-5.6-terra, gpt-6-astra, gpt-6-luna, gpt-6-sol, gpt-6.1-sol
