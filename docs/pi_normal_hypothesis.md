# The Normality Hypothesis for π

This page gives a short overview. See `docs/SCIENTIFIC_NOTES.md` for the more
complete discussion used by the README.

## Definition

A real number is normal in base 10 if every finite block of decimal digits has
the expected limiting frequency. For a block of length `k`, that frequency is
`1 / 10^k`.

Examples:

- each single digit should have limiting frequency `1/10`;
- each two-digit block should have limiting frequency `1/100`;
- each six-digit block should have limiting frequency `1/1,000,000`;
- the requirement applies to every finite block length.

For π, base-10 normality is a conjecture, not a theorem.

## What can be tested here

This repository works with finite prefixes of π. On a finite prefix, the tools
can:

- count empirical digit and block frequencies;
- search for specified target strings;
- compare observed finite counts with simple uniform expectations;
- save plots or command output for inspection.

These checks can be useful and reproducible. They are not proofs of normality.

## Common misunderstanding

If π were normal, every finite decimal block would occur with the expected
limiting frequency. That mathematical statement should not be interpreted as
semantic content. A target string appearing in a finite prefix is a string-search
result over that prefix, nothing more.

## Why this is interesting

Normality is a precise meeting point of number theory, computation, and
probability intuition. The computational challenge is to report finite evidence
accurately while preserving the distinction between empirical summaries and
asymptotic mathematical statements.

## Further reading

See `docs/REFERENCES.md`.
