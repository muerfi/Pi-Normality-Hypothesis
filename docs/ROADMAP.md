# Roadmap

This roadmap focuses on making the project more useful as a careful scientific
computation repository. Items are intentionally framed as improvements, not as
claims that the project can prove normality of π.

## Near-term documentation improvements

- Keep the README focused on purpose, scope, commands, limitations, and
  reproducibility.
- Keep `docs/SCIENTIFIC_NOTES.md` as the main explanation of normality and
  finite-prefix interpretation.
- Keep `docs/REFERENCES.md` limited to sources that have actually been checked
  and used.
- Update notebook text so exploratory examples use the same sober terminology as
  the rest of the project.

## Near-term engineering improvements

- Add command-line options for writing machine-readable frequency results, such
  as CSV or JSON.
- Add metadata sidecar files for generated digit data, including digit count,
  generation method, software versions, timestamp, and checksum.
- Make examples consistently use the package API rather than duplicating logic in
  scripts.
- Rename compatibility examples in a future breaking release so target-string
  search examples do not imply interpretive significance.

## Statistical and computational improvements

- Add prefix-window analyses that report how counts change as `N` grows.
- Add expected-count warnings for block sizes where `10^k` is too large relative
  to the loaded prefix.
- Add optional goodness-of-fit summaries with clear caveats about finite samples
  and multiple testing.
- Add comparison utilities for generated pseudo-random digit strings of the same
  length, clearly labeled as baseline models rather than descriptions of π.
- Add tests for block extraction, file provenance, and reproducibility metadata.

## Reproducibility improvements

- Provide a documented recipe for regenerating committed example data.
- Record checksums for sample data used in tests or examples.
- Add continuous-integration checks for tests, formatting, and documentation
  links where practical.
- Consider preserving exact command output for selected example runs.

## Out of scope

- Claiming a proof of normality for π.
- Treating target-string matches as interpretive content.
- Presenting finite empirical checks as decisive mathematical evidence.
- Running or hosting the Flask interface as a production web service.
