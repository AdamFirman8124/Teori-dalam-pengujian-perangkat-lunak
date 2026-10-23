# Source provenance

The retained source directories were copied into the parent repository without nested `.git` metadata. Their original commit hashes cannot be independently recovered from those directories. This must be treated as a reproducibility gap until upstream snapshots are checked against the retained content.

| Component | Required version | Retained path | Provenance status |
| --- | --- | --- | --- |
| CodaMOSA | plasma-umass/codamosa `17a4c2a2ecb40b60e32a7e4a437db03573612f11` | `codamosa/`, `dataset/codamosa/` | Commit claimed by File B/coverup-eval; active copy includes local chat-completions, accounting, timeout, and retry patches |
| CoverUp | 0.6.3, upstream tag commit `c4ad2f13c74c1154761038cf924ae5ece27dffdc` | `coverup/`, `dataset/coverup/` | Version verified in `version.py`; active copy contains local endpoint/logging/timeout patches |
| MT benchmark | coverup-eval `f3173196b90181974b0b684600ffde42ac36672c` | `dataset/coverup-eval/MuTAP-benchmarks/` | 163 task directories present; nested commit metadata absent |
| CM benchmark | coverup-eval CodaMOSA replication suite | `dataset/codamosa/replication/test-apps/` | 425 manifest rows from 24 projects present; commit metadata absent |
| Evaluation | coverage.py 7.16.2 | image to be built | Pending |
| Mutation | Cosmic Ray 8.7.0 | image to be built | Pending |

Parent repository HEAD at protocol preparation: `c9c42f5b59f42c8a7d72db52428711fa6de59d18`.
