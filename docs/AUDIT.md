# Repository Audit

Date: 2026-05-07
Repository: `muerfi/Pi-Normality-Hypothesis`

This audit note records the documentation posture expected for the project after
the documentation rewrite.

## Summary

The repository is best understood as a finite-prefix exploration toolkit for the
decimal expansion of π. Its appropriate claims are computational and limited:
generate a prefix, search target strings, count digit blocks, plot simple
frequencies, and document the exact conditions of each run.

The documentation should consistently state that base-10 normality of π is
unproven and that finite experiments cannot establish an asymptotic theorem.
Search results should be described as target-string matches over a loaded file.
Frequency results should be described as finite descriptive summaries.

## Documentation standards

- Explain normality as a limiting-frequency property for every finite block
  length.
- Distinguish single-digit balance from full normality.
- State that all command output depends on the selected finite prefix.
- Record commands, software versions, data provenance, and checksums when
  presenting results.
- Use primary or stable mathematical references where possible.

## Language to avoid

Avoid wording that says or implies that:

- finite experiments prove normality;
- π's digits are produced by a random source;
- a target-string occurrence carries interpretive content;
- absence from a finite prefix is absence from π;
- single-digit frequency plots settle the normality question.

## Current documentation map

- `README.md` provides project purpose, scope, quick start, structure,
  limitations, and reproducibility notes.
- `docs/SCIENTIFIC_NOTES.md` gives the main scientific interpretation guide.
- `docs/ROADMAP.md` lists future documentation, engineering, statistical, and
  reproducibility work.
- `docs/REFERENCES.md` lists checked background sources used by the project
  documentation.
- `docs/user_guide.md` gives concise usage instructions.
