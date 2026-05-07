# Scientific Notes

This project studies finite prefixes of the decimal expansion of π. The goal is
computational exploration with careful language, not a proof of a theorem about
π.

## Normality in base 10

Let `x` be a real number with a decimal expansion. Informally, `x` is normal in
base 10 if every finite decimal block appears with the frequency expected from a
uniform digit model.

More concretely, for every block length `k >= 1` and every decimal block `b` of
length `k`, the limiting frequency of `b` among overlapping length-`k` blocks in
the decimal expansion must be:

```text
1 / 10^k
```

Examples:

- for `k = 1`, each digit `0` through `9` must have limiting frequency `1/10`;
- for `k = 2`, each block from `00` through `99` must have limiting frequency
  `1/100`;
- for `k = 6`, each six-digit block must have limiting frequency `1/1,000,000`;
- the condition must hold for every finite `k`.

The word "limiting" is essential. Normality is a statement about behavior as the
number of inspected digits tends to infinity.

## What is known about π

It is widely conjectured that π is normal in base 10. It is also widely
conjectured that π is normal in other integer bases. These conjectures are
consistent with extensive computations, but they are not theorems.

No proof is currently known that π is normal in base 10.

## What finite experiments can show

Finite experiments can show accurate, reproducible facts about a chosen prefix.
For example, this repository can report:

- counts of each digit in the first `N` stored characters;
- counts of overlapping blocks of a selected length;
- the first position of a specified target string if it appears in the loaded
  file;
- absence of a specified target string from the loaded file.

These are legitimate computational results. They become scientifically useful
when the digit source, prefix length, commands, software versions, and checksums
are recorded.

## What finite experiments cannot show

Finite experiments cannot prove normality of π. The reason is structural:
normality concerns infinitely many limiting frequency statements, one for every
block length. Any computation checks only finitely many digits and finitely many
block sizes.

Finite experiments also cannot disprove normality unless they reveal an actual
mathematical inconsistency in the digits being studied. An unusual finite prefix
may be surprising under a simple random model, but a normal number can still
have irregular finite prefixes.

## Single-digit frequencies are only a first diagnostic

Counting digits `0` through `9` is a useful sanity check, but it is much weaker
than normality. A number can have balanced single-digit frequencies and still
fail to be normal because pairs, triples, or longer blocks occur with the wrong
limiting frequencies.

For this reason, single-digit plots should be described as finite descriptive
summaries, not as evidence that settles the normality question.

## Target-string searches

Searching for a target string is exact string matching over a finite file. The
interpretation should be narrow:

- if the target is found, the result is its position in the loaded prefix;
- if the target is not found, the result is only non-occurrence in that loaded
  prefix;
- occurrence is not semantic evidence;
- non-occurrence is not evidence that the target never appears in π.

Short strings are expected to occur often in long digit sequences. Long strings
may be absent simply because the inspected prefix is too short. Any search over
many targets should account for multiple comparisons when statistical language
is used.

## Random models are comparisons, not descriptions of π

It is often useful to compare finite digit counts with the behavior expected from
independent uniformly distributed decimal digits. That comparison gives a
baseline for intuition.

The comparison does not mean that π is generated randomly. π is deterministic.
Normality, if true for π, would be a precise limiting-frequency property, not a
statement that the digits were produced by a random source.

## Recommended reporting style

Prefer language such as:

- "In the first `N` stored characters, block `b` occurs `c` times."
- "The observed counts are close to the uniform finite-sample expectation for
  this prefix."
- "This result is consistent with normality but does not prove it."
- "The target string appears at zero-based position `p` in the loaded file."

Avoid language such as:

- "This proves π is normal."
- "The digits are random."
- "This occurrence has interpretive content because it appears in π."
- "The target does not exist in π" when only a finite prefix was searched.
