# The Normality Hypothesis for π

## Definition

A real number is **normal in base 10** if every finite block of digits appears with the expected limiting frequency.

Examples:
- each single digit appears with frequency `1/10`,
- each 2-digit block appears with frequency `1/100`,
- and so on for blocks of any length.

For π, this is a conjecture, not a theorem.

## What can be tested here

This repository works with a finite prefix of π (for example, the first million digits). On finite data you can:

- measure empirical digit frequencies,
- search for specific strings,
- compare observations with what you would expect from a random-looking sequence.

These checks are useful, but they are not proofs of normality.

## Common misunderstanding

If π were normal, then any finite sequence would eventually occur somewhere in its digits. That does **not** mean those occurrences are meaningful messages; it only reflects combinatorics on an infinite expansion.

## Why this is interesting

The topic sits between number theory, probability intuition, and information theory:

- **Number theory:** normality is a precise asymptotic property.
- **Statistics:** finite samples can look balanced without implying a theorem.
- **Information:** "all finite patterns occur" does not automatically create usable structure.

## References

- Normal number (overview): <https://en.wikipedia.org/wiki/Normal_number>
- Bailey and Borwein, *Normal Numbers* (survey): <https://www.davidhbailey.com/dhbpapers/normality.pdf>
- Pi search utility (example finite lookup): <http://www.angio.net/pi/>
