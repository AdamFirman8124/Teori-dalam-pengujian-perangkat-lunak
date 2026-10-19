import typing as T
import openai
import logging
import asyncio
import warnings
import textwrap
import json
import time
import traceback
import os
from aiolimiter import AsyncLimiter

with warnings.catch_warnings():
    # ignore pydantic warnings https://github.com/BerriAI/litellm/issues/2832
    warnings.simplefilter('ignore')
    import litellm  # type: ignore

# Turn off most logging
litellm.set_verbose = False
litellm.suppress_debug_info = True
logging.getLogger().setLevel(logging.ERROR)
# Ignore unavailable parameters
litellm.drop_params = True

# Tier 5 rate limits for models; tuples indicate limit and interval in seconds
# Extracted from https://platform.openai.com/account/limits on 8/30/2024
MODEL_RATE_LIMITS = {
    'gpt-3.5-turbo': {'token': (50_000_000, 60), 'request': (10_000, 60)},
    'gpt-3.5-turbo-0125': {'token': (50_000_000, 60), 'request': (10_000, 60)},
    'gpt-3.5-turbo-1106': {'token': (50_000_000, 60), 'request': (10_000, 60)},
    'gpt-3.5-turbo-16k': {'token': (50_000_000, 60), 'request': (10_000, 60)},
    'gpt-3.5-turbo-instruct': {'token': (90_000, 60), 'request': (3_500, 60)},
    'gpt-3.5-turbo-instruct-0914': {'token': (90_000, 60), 'request': (3_500, 60)},
    'gpt-4': {'token': (1_000_000, 60), 'request': (10_000, 60)},
    'gpt-4-0314': {'token': (1_000_000, 60), 'request': (10_000, 60)},
    'gpt-4-0613': {'token': (1_000_000, 60), 'request': (10_000, 60)},
    'gpt-4-32k-0314': {'token': (150_000, 60), 'request': (1_000, 60)},
    'gpt-4-turbo': {'token': (2_000_000, 60), 'request': (10_000, 60)},
    'gpt-4-turbo-2024-04-09': {'token': (2_000_000, 60), 'request': (10_000, 60)},
    'gpt-4-turbo-preview': {'token': (2_000_000, 60), 'request': (10_000, 60)},
    'gpt-4-0125-preview': {'token': (2_000_000, 60), 'request': (10_000, 60)},
    'gpt-4-1106-preview': {'token': (2_000_000, 60), 'request': (10_000, 60)},
    'gpt-4o': {'token': (30_000_000, 60), 'request': (10_000, 60)},
    'gpt-4o-2024-05-13': {'token': (30_000_000, 60), 'request': (10_000, 60)},
    'gpt-4o-2024-08-06': {'token': (30_000_000, 60), 'request': (10_000, 60)},
    'gpt-4o-mini': {'token': (150_000_000, 60), 'request': (30_000, 60)},
    'gpt-4o-mini-2024-07-18': {'token': (150_000_000, 60), 'request': (30_000, 60)},
    'bedrock/anthropic.claude-3-haiku-20240307-v1:0': {'token': (1_000_000, 60), 'request': (10_000, 60)},
    'bedrock/anthropic.claude-3-sonnet-20240229-v1:0': {'token': (1_000_000, 60), 'request': (10_000, 60)},
    'bedrock/anthropic.claude-3-opus-20240229-v1:0': {'token': (1_000_000, 60), 'request': (10_000, 60)},
    'anthropic.claude-3-5-sonnet-20241022-v2:0': {'token': (400_000, 50), 'request': (10_000, 50)},
    'us.anthropic.claude-3-5-sonnet-20241022-v2:0': {'token': (400_000, 50), 'request': (10_000, 50)},
    'us.anthropic.claude-3-7-sonnet-20250219-v1:0': {'token': (400_000, 50), 'request': (10_000, 50)},
}

def _model_supports_function_calling(model_name: str) -> bool:
    """Capability gate that tolerates OpenAI-compatible custom endpoints.

    For `openai/<bare>` models routed through OPENAI_BASE_URL, LiteLLM looks
    up the *provider-prefixed* registry entry, whose capability flags may be
    absent. The actual provider call uses the bare model id after the prefix,
    which we already validated supports function calling.

    A custom endpoint may also expose router aliases (e.g. ``auto``) that are
    not in LiteLLM's registry at all.  For those, the registry check is
    meaningless: the provider is the only authority, and CoverUp already sends
    the tool schema on every request, so the call itself is the real test.
    """
    if litellm.supports_function_calling(model_name):
        return True
    if os.environ.get("OPENAI_BASE_URL") and model_name.startswith("openai/"):
        bare = model_name[len("openai/"):]
        try:
            if litellm.supports_function_calling(bare):
                return True
        except Exception:
            pass
        # Unknown alias on a custom OpenAI-compatible gateway: defer to the
        # provider instead of blocking the whole run up front.
        if model_name not in litellm.model_cost and bare not in litellm.model_cost:
            return True
    return False


def token_rate_limit_for_model(model_name: str) -> T.Tuple[int, int] | None:
    if model_name.startswith('openai/'):
        model_name = model_name[7:]

    if (model_limits := MODEL_RATE_LIMITS.get(model_name)):
        limit = model_limits.get('token')

        if not "anthropic" in model_name:
            try:
                import tiktoken
                tiktoken.encoding_for_model(model_name)
            except KeyError:
                warnings.warn(f"Unable to get encoding for {model_name}; will ignore rate limit")
                return None

        return limit

    return None

def compute_cost(usage: dict, model_name: str) -> float | None:
    from math import ceil

    if model_name.startswith('openai/'):
        model_name = model_name[7:]

    if 'prompt_tokens' in usage and 'completion_tokens' in usage:
        if (cost := litellm.model_cost.get(model_name)):
            return usage['prompt_tokens'] * cost['input_cost_per_token'] + \
                   usage['completion_tokens'] * cost['output_cost_per_token']

    return None

_token_encoding_cache: dict[str, T.Any] = dict()

def count_tokens(model_name: str, completion: dict):
    """Counts the number of tokens in a chat completion request."""
    from litellm import token_counter

    count = token_counter(model=model_name, messages=completion['messages'])

    return count

class ChatterError(Exception):
    pass

# --------------------------------------------------------------------------- #
# Per-call LLM accounting
# --------------------------------------------------------------------------- #
# Every provider round-trip appends one JSON line to this file so the experiment
# can report, per call: wall time, prompt text + prompt tokens, output text +
# completion tokens, and cost in USD.  The path comes from
# COVERUP_LLM_CALLS_LOG, which the experiment notebook sets per task/model.
def _llm_calls_log(entry: dict) -> None:
    """Append one per-call record. Never raises: logging is best-effort.

    The path is resolved absolutely on first use: CoverUp may run with its
    working directory set to a task workdir while `COVERUP_LLM_CALLS_LOG` was
    written from the notebook's cwd, so a relative path would land elsewhere.
    """
    path = os.environ.get("COVERUP_LLM_CALLS_LOG", "")
    if not path:
        return
    try:
        with open(os.path.abspath(path), "a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError:
        pass


class Chatter:
    """Chats with an LLM."""
    def __init__(self, model: str) -> None:
        Chatter._validate_model(model)

        self._model = model
        self._model_temperature: float | None = None
        self._max_backoff = 64 # seconds
        self._rpm_gate_state = os.environ.get("RPM_GATE_STATE", "")
        try:
            self._rpm_limit = max(0, int(os.environ.get("RPM_LIMIT", "0")))
        except ValueError:
            self._rpm_limit = 0
        # Provider calls are billed even when they end in an error or a cache
        # hit.  Retrying the same request therefore costs tokens repeatedly for
        # the same (often identical) answer.  Default is 0 retries: record what
        # the provider returned instead of re-buying it.  Raise
        # COVERUP_MAX_TRANSPORT_RETRIES if a flaky endpoint needs more attempts.
        try:
            self._max_connection_retries = max(
                0, int(os.environ.get("COVERUP_MAX_TRANSPORT_RETRIES", "0"))
            )
        except ValueError:
            self._max_connection_retries = 0
        self.token_rate_limit: AsyncLimiter | None
        self.set_token_rate_limit(token_rate_limit_for_model(model))
        self._add_cost = lambda cost: None
        self._add_usage = lambda pt, ct, tt: None
        self._log_msg = lambda ctx, msg: None
        self._log_json = lambda ctx, j: None
        self._signal_retry = lambda: None
        self._functions: dict[str, dict[str, T.Any]] = dict()
        self._max_func_calls_per_chat = 50
        self._extra_request_pars: dict[str, T.Any] | None = None
        # Token accounting.  Custom OpenAI-compatible providers may omit
        # `usage`; we accumulate whatever is reported so a run can be costed
        # exactly instead of guessed.
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_tokens = 0
        self.usage_reported = 0

    @staticmethod
    def _validate_model(model) -> None:
        try:
            _, provider, _, _ = litellm.get_llm_provider(model)
        except litellm.exceptions.BadRequestError:
            raise ChatterError(textwrap.dedent("""
                Unknown or unsupported model.
                Please see https://docs.litellm.ai/docs/providers for supported models."""))

        result = litellm.validate_environment(model)
        if result['missing_keys']:
            if provider == 'openai':
                raise ChatterError(textwrap.dedent("""
                    You need an OpenAI key to use {model}.

                    You can get a key here: https://platform.openai.com/api-keys
                    Set the environment variable OPENAI_API_KEY to your key value
                        export OPENAI_API_KEY=<your key>"""))
            elif provider == 'bedrock':
                raise ChatterError(textwrap.dedent("""
                    To use Bedrock, you need an AWS account. Set the following environment variables:
                       export AWS_ACCESS_KEY_ID=<your key id>
                       export AWS_SECRET_ACCESS_KEY=<your secret key>
                       export AWS_REGION_NAME=us-west-2

                    You also need to request access to Claude:
                       https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#manage-model-access"""))
            else:
                raise ChatterError(textwrap.dedent(f"""
                    You need a key (or keys) from {provider} to use {model}.
                    Set the following environment variables:
                        {', '.join(result['missing_keys'])}"""))

    def set_model_temperature(self, temperature: T.Optional[float]) -> None:
        self._model_temperature = temperature

    def set_token_rate_limit(self, limit: T.Union[T.Tuple[int, int], None]) -> None:
        if limit:
            self.token_rate_limit = AsyncLimiter(*limit)
        else:
            self.token_rate_limit = None

    def set_max_backoff(self, max_backoff: int) -> None:
        self._max_backoff = max_backoff

    def set_add_cost(self, add_cost: T.Callable) -> None:
        """Sets up a callback to indicate additional costs."""
        self._add_cost = add_cost

    def set_add_usage(self, add_usage: T.Callable) -> None:
        """Sets up a callback to accumulate prompt/completion/total tokens."""
        self._add_usage = add_usage

    def set_log_msg(self, log_msg: T.Callable[[str, str], None]) -> None:
        """Sets up a callback to write a message to the log."""
        self._log_msg = log_msg

    def set_log_json(self, log_json: T.Callable[[str, dict], None]) -> None:
        """Sets up a callback to write a json exchange to the log."""
        self._log_json = log_json

    def set_signal_retry(self, signal_retry: T.Callable) -> None:
        """Sets up a callback to indicate a retry."""
        self._signal_retry = signal_retry

    def set_extra_request_pars(self, request_pars: dict[str, T.Any] | None) -> None:
        """Sets additional parameters to pass into the LLM request."""
        self._extra_request_pars = request_pars

    def add_function(self, function: T.Callable) -> None:
        """Makes a function availabe to the LLM."""
        if not _model_supports_function_calling(self._model):
            raise ChatterError(f"The {self._model} model does not support function calling.")

        try:
            schema = json.loads(getattr(function, "__doc__", ""))
            if 'name' not in schema:
                raise ChatterError(f"Name missing from function {function} schema.")
        except json.decoder.JSONDecodeError as e:
            raise ChatterError(f"Invalid JSON in function docstring: {e}")

        assert schema['name'] not in self._functions, f"Duplicated function name {schema['name']}"
        self._functions[schema['name']] = {"function": function, "schema": schema}

    def _request(self, messages: T.List[dict]) -> dict:
        return {
            'model': self._model,
            **({'temperature': self._model_temperature} if self._model_temperature is not None else {}),
            'messages': messages,
            **({'tools': [{'type': 'function', 'function': f['schema']} for f in self._functions.values()]} if self._functions else {}),
            **(self._extra_request_pars if self._extra_request_pars else {})
        }

    async def _send_request(self, request: dict, ctx: object) -> litellm.ModelResponse | None:
        """Sends the LLM chat request, handling common failures and returning the response."""
        sleep = 1
        attempts = 0
        while True:
            try:
                # TODO also add request limit; could use 'await asyncio.gather(t.acquire(tokens), r.acquire())'
                # to acquire both
                # Cross-process request budget (shared with CodaMOSA).  The
                # provider enforces 50 RPM; without this gate every CoverUp
                # worker fires immediately and burns a whole task on HTTP 429.
                _gate_state = os.environ.get("RPM_GATE_STATE", "")
                try:
                    _gate_limit = max(0, int(os.environ.get("RPM_LIMIT", "0")))
                except ValueError:
                    _gate_limit = 0
                if _gate_state and _gate_limit:
                    try:
                        import rate_gate as _rate_gate
                        _waited = _rate_gate.acquire(_gate_state, _gate_limit)
                        if _waited > 1.0:
                            self._log_msg(ctx, f"RPM gate: waited {_waited:.1f}s")
                    except Exception:
                        pass

                if self.token_rate_limit:
                    try:
                        await self.token_rate_limit.acquire(count_tokens(self._model, request))
                    except ValueError as e:
                        self._log_msg(ctx, f"Error: too many tokens for rate limit ({e})")
                        return None # gives up this segment

                return await litellm.acreate(**request)

            except (litellm.exceptions.ServiceUnavailableError,
                    openai.RateLimitError,
                    openai.APITimeoutError) as e:

                # This message usually indicates out of money in account
                if 'You exceeded your current quota' in str(e):
                    self._log_msg(ctx, f"Failed: {type(e)} {e}")
                    raise

                import random
                sleep = min(sleep * 2, self._max_backoff)
                sleep_time = random.uniform(sleep / 2, sleep)

                self._log_msg(ctx, f"Error: {type(e)} {e} {sleep=} {sleep_time=}")

                self._signal_retry()
                await asyncio.sleep(sleep_time)

            except openai.BadRequestError as e:
                # Two very different causes reach this branch:
                #   1. A genuine request-shape problem such as exceeding the
                #      maximum context length - retrying cannot help.
                #   2. An OpenAI-compatible gateway (e.g. OctaLabs) returning
                #      HTTP 400 "The upstream service could not complete the
                #      request" for a transient upstream hiccup - retrying with
                #      backoff recovers it.
                # Previously every BadRequestError gave up immediately, so a
                # momentary upstream 400 killed the segment and the task was
                # reported BLOCKED even though the model was fine.
                message = str(e).lower()
                permanent = (
                    "maximum context length" in message
                    or "context length" in message
                    or "too many tokens" in message
                    or "invalid api key" in message
                    or "invalid_request_error" in message and "upstream" not in message
                )
                if permanent:
                    self._log_msg(ctx, f"Error (permanent): {type(e)} {e}")
                    return None  # gives up this segment

                attempts += 1
                if attempts > self._max_connection_retries:
                    self._log_msg(
                        ctx,
                        f"Giving up after {attempts} upstream 400 errors: {type(e)} {e}",
                    )
                    return None  # gives up this segment
                import random
                sleep = min(sleep * 2, self._max_backoff)
                sleep_time = random.uniform(sleep / 2, sleep)
                self._log_msg(ctx, f"Error: {type(e)} {e} {sleep=} {sleep_time=}")
                self._signal_retry()
                await asyncio.sleep(sleep_time)

            except openai.AuthenticationError as e:
                self._log_msg(ctx, f"Failed: {type(e)} {e}")
                raise

            except (openai.APIConnectionError,
                    litellm.exceptions.InternalServerError,
                    openai.InternalServerError) as e:
                # OpenAI-compatible routers (e.g. OctaLabs) commonly wrap a
                # transient connection reset as a 5xx/APIConnectionError.  Retry
                # with bounded exponential backoff; previously an
                # InternalServerError fell through to the generic APIError
                # handler and CoverUp logged "giving up" immediately -- even
                # right after a valid completion was received.
                attempts += 1
                if attempts > self._max_connection_retries:
                    self._log_msg(
                        ctx,
                        f"Giving up after {attempts} transport errors: {type(e)} {e}",
                    )
                    return None # gives up this segment
                import random
                sleep = min(sleep * 2, self._max_backoff)
                sleep_time = random.uniform(sleep / 2, sleep)
                self._log_msg(ctx, f"Error: {type(e)} {e} {sleep=} {sleep_time=}")
                self._signal_retry()
                await asyncio.sleep(sleep_time)

            except openai.APIError as e:
                # APIError is the base class for all API errors. Unknown API
                # errors remain fail-fast so authentication/request-shape bugs
                # are not retried indefinitely.
                print(f"Error: {type(e)} {e}; missing handler?")
                self._log_msg(ctx, f"Error: {type(e)} {e}")
                return None # gives up this segment

    def _call_function(self, ctx: object, tool_call: litellm.ModelResponse) -> str:
        # Providers occasionally return malformed or empty `arguments` (e.g.
        # trailing text after the JSON object, or a bare empty string for a
        # no-arg function).  A JSONDecodeError here would propagate out of
        # asyncio.gather and abort the entire task, so a bad tool call is
        # reported back to the model as a tool error instead.
        raw_args = getattr(tool_call.function, "arguments", None)
        try:
            if raw_args is None or raw_args == "":
                args = {}
            else:
                args = json.loads(raw_args)
        except (json.JSONDecodeError, TypeError) as e:
            self._log_msg(ctx, f"Invalid tool-call arguments from model: {e}\nraw={raw_args!r}")
            return f"Error executing function: invalid arguments JSON ({e})"

        function = self._functions.get(tool_call.function.name)
        if function is None:
            self._log_msg(ctx, f"Unknown tool function requested: {tool_call.function.name}")
            return f"Error executing function: unknown function {tool_call.function.name}"

        try:
            return str(function['function'](ctx=ctx, **args))
        except Exception as e:
            self._log_msg(ctx, f"""
Error executing function \"{tool_call.function.name}\": {e}
args:{args}

{traceback.format_exc()}
""")
            return f'Error executing function: {e}'

    async def chat(self, messages: list, *, ctx: T.Optional[object] = None) -> dict | None:
        """Chats with the LLM, sending the given messages, handling common failures and returning the response.
           Automatically calls any tool functions requested."""
        func_calls = 0
        while func_calls <= self._max_func_calls_per_chat:
            request = self._request(messages)
            self._log_json(ctx, request)

            _req_t0 = time.time()
            if not (response := await self._send_request(request, ctx=ctx)):
                return None

            self._log_json(ctx, response.json())
            try:
                self._add_cost(litellm.completion_cost(response))
            except Exception:
                # Custom models may not be in LiteLLM cost map; skip cost tracking
                pass

            # Per-call LLM accounting (time, prompt, tokens, output, cost).
            try:
                usage = getattr(response, "usage", None)
                pt = int(getattr(usage, "prompt_tokens", 0) or 0)
                ct = int(getattr(usage, "completion_tokens", 0) or 0)
                tt = int(getattr(usage, "total_tokens", 0) or pt + ct)
                try:
                    call_cost = float(litellm.completion_cost(response))
                except Exception:
                    call_cost = None
                choice = response.choices[0] if getattr(response, "choices", None) else None
                out_text = ""
                if choice is not None:
                    msg = getattr(choice, "message", None)
                    out_text = (getattr(msg, "content", None) or "")
                    for tc in (getattr(msg, "tool_calls", None) or []):
                        out_text += "\n[tool_call] " + getattr(getattr(tc, "function", None), "name", "?") + "(" + str(getattr(getattr(tc, "function", None), "arguments", "")) + ")"
                _llm_calls_log({
                    "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "latency_s": round(time.time() - _req_t0, 3),
                    "model": self._model,
                    "requested_model": self._model,
                    "returned_model": getattr(response, "model", None),
                    "prompt": "\n".join(
                        (m.get("content") or "") if isinstance(m, dict) else str(m)
                        for m in messages
                    ),
                    "prompt_tokens": pt,
                    "output": out_text,
                    "completion_tokens": ct,
                    "total_tokens": tt,
                    "cost_usd": call_cost,
                    "finish_reason": getattr(choice, "finish_reason", None),
                    # Raw provider outcome so consolidated logs can separate
                    # errors, cache hits, and genuine completions.
                    "response_headers": dict(getattr(response, "headers", None) or {}),
                    "status_code": getattr(response, "status_code", None),
                })
            except Exception:
                pass  # logging must never break the run

            # Accumulate token usage when the provider reports it.
            usage = getattr(response, "usage", None)
            if usage is not None:
                pt = getattr(usage, "prompt_tokens", None)
                ct = getattr(usage, "completion_tokens", None)
                tt = getattr(usage, "total_tokens", None)
                if pt is not None:
                    self.prompt_tokens += int(pt)
                if ct is not None:
                    self.completion_tokens += int(ct)
                if tt is not None:
                    self.total_tokens += int(tt)
                self.usage_reported += 1
                self._add_usage(pt, ct, tt)

            if response.choices[0].finish_reason != "tool_calls":
                return response.json()

            tool_message = response.choices[0].message.json()
            tool_message["content"] = "" # it's typically set to null, which upsets count_tokens
            messages.append(tool_message)

            for call in response.choices[0].message.tool_calls:
                func_calls += 1
                messages.append({
                    'tool_call_id': call.id,
                    'role': 'tool',
                    'name': call.function.name,
                    'content': self._call_function(ctx, call)
                })

        self._log_msg(ctx, f"Too many function call requests, giving up")
        return None
