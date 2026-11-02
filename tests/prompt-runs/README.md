# Prompt runs

The records of the logged runs of the cases in [prompt-evaluation-cases.md](../prompt-evaluation-cases.md), which states how each run was made, how it is scored and how it is read under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). Transcripts are kept as written; each carries the SHA-256 of its run input in its header.

| Run | Date (KST) | Manifests | Scores | Transcripts |
|---|---|---|---|---|
| 20261027-R1 | 27 October 2026 | [opus](transcripts/20261027-R1_claude-opus-5-5_run.json) · [sonnet](transcripts/20261027-R1_claude-sonnet-5-5_run.json) | [opus, scored by sonnet](scores/20261027-R1_claude-opus-5-5_scored-by_claude-sonnet-5-5.md) · [sonnet, scored by opus](scores/20261027-R1_claude-sonnet-5-5_scored-by_claude-opus-5-5.md) | 26 per model in [transcripts/](transcripts/), named `20261027-R1_<model>_<case>.md` |
| 20261027-R2 | 27 October 2026 | [opus](transcripts/20261027-R2_claude-opus-5-5_run.json) · [sonnet](transcripts/20261027-R2_claude-sonnet-5-5_run.json) | [opus, scored by sonnet](scores/20261027-R2_claude-opus-5-5_scored-by_claude-sonnet-5-5.md) · [sonnet, scored by opus](scores/20261027-R2_claude-sonnet-5-5_scored-by_claude-opus-5-5.md) | 26 per model in [transcripts/](transcripts/), named `20261027-R2_<model>_<case>.md` |

Each score file has a JSON twin of the same name in [scores/](scores/). Which run the instrument's status rests on is stated in the run record of [prompt-evaluation-cases.md](../prompt-evaluation-cases.md).

**Final Liability rests with the Human.**
