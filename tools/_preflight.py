import os, litellm
print('key present', bool(os.environ.get('OPENAI_API_KEY')))
for m in ["openai/claude-sonnet-5","openai/gpt-5.5"]:
    try:
        r=litellm.completion(model=m, messages=[{"role":"user","content":"Reply OK"}], max_tokens=1, timeout=45)
        print(m, "OK", bool(getattr(r,"choices",None)))
    except Exception as e:
        print(m, "ERR", type(e).__name__, str(e)[:200])
