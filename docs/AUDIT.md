# Repository Audit

Date: 2026-05-07
Repository: `muerfi/Pi-Normality-Hypothesis`
Scope: audit only. No code, data, notebook, or documentation files other than this audit were intentionally changed.

## Executive summary

The repository has a clear educational core: generate or load a finite decimal prefix of π, search for digit strings, and plot simple digit frequencies. The current README is notably careful about the central scientific limitation: it says that the project does not prove normality and warns against treating found strings as meaningful messages. That tone should be preserved.

The main problems are engineering maturity and consistency rather than the basic idea. The project is currently a collection of runnable scripts plus a small Flask app, not yet a reproducible scientific Python package. Imports depend on executing commands from the repository root, data paths are hardcoded, tests depend on a checked-in data file, the generated-data story is inconsistent, the notebook appears to be invalid JSON, and the visualizations referenced by documentation do not match the files currently committed.

Scientifically, the highest-risk material is in the notebook and in names such as `meaningful_sequences.py`. The README and `docs/pi_normal_hypothesis.md` mostly avoid overclaiming, but the notebook contains stronger language such as finite frequencies “supporting the hypothesis,” π digits varying “due to randomness,” and “significant sequences.” A serious version of the project should consistently distinguish finite empirical observations from asymptotic normality and should frame sequence hits as pattern-search examples, not evidence of semantic content.

## Current repository state

### Observed structure

```text
.
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── data/
│   ├── pi_decimals.txt
│   └── test_sequences.txt
├── docs/
│   ├── AUDIT.md
│   ├── pi_normal_hypothesis.md
│   └── user_guide.md
├── notebooks/
│   └── PiSequence.ipynb
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── frequency_analysis.py
│   ├── meaningful_sequences.py
│   ├── pi_generator.py
│   ├── sequence_search.py
│   └── utils.py
├── tests/
│   ├── conftest.py
│   └── test_search.py
├── visualizations/
│   ├── digit_frequency_pi.png
│   └── sequence_positions_pi.png
└── web/
    ├── app.py
    ├── static/
    │   └── style.css
    └── templates/
        ├── index.html
        └── result.html
```

### What currently works

- The existing `unittest` suite passes in the current checkout.
- The Python files in `src/`, `web/`, and `tests/` compile with the local Python interpreter.
- The README states a restrained project scope and explicitly says that the project does not prove normality.
- `docs/pi_normal_hypothesis.md` gives a concise and mostly appropriate finite-data warning.
- The minimal Flask app is understandable and keeps user-facing claims narrow.

### Important inconsistencies

- `README.md` and `docs/user_guide.md` describe generation of 1,000,000 digits, but `data/pi_decimals.txt` currently contains only 150 bytes.
- `frequency_analysis.py` writes `visualizations/digit_frequency.png`, while committed files include `visualizations/digit_frequency_pi.png` and `visualizations/sequence_positions_pi.png`.
- `web/app.py` expects `visualizations/digit_frequency.png`, so the frequency page will not show a plot unless that exact file is generated later.
- `notebooks/PiSequence.ipynb` could not be parsed as JSON by Python's standard `json` module because of an unescaped quote in one markdown string. This means the notebook is likely unusable until repaired.
- The notebook mentions a GitHub repository name/path that differs from the current repository name.
- `src/__init__.py` exists but is empty, and `src` is used as an import package even though the project is not installable as a package.

## Main technical problems

### 1. Script collection rather than package

The code under `src/` is organized as top-level scripts. Imports such as `from src.utils import load_pi_decimals` work when the repository root is on `sys.path`, but this is fragile outside the current working directory or test harness. The project should eventually move to a proper package name such as `pi_sequence` or `pi_normality_explorer` under a `src/` layout.

Current symptoms:

- No `pyproject.toml` or package metadata.
- No console entry points.
- Tests patch `sys.path` in `tests/conftest.py` instead of importing an installed package.
- CLI scripts assume execution from the repository root.

### 2. Duplicated search implementation

`src/sequence_search.py` defines `search_sequence`, and `src/meaningful_sequences.py` defines another function with the same name and nearly the same implementation. This duplication is small but important: it is a sign that examples are not using the shared library API.

Suggested future direction: keep exactly one search function in the library, then make demonstrations import it.

### 3. Hardcoded paths and current-working-directory dependence

Several modules hardcode relative paths such as `data/pi_decimals.txt` and `visualizations/digit_frequency.png`. These paths only work reliably from the repository root.

Affected areas:

- `src/pi_generator.py` reads and writes `data/pi_decimals.txt`.
- `src/utils.py` loads `data/pi_decimals.txt`.
- `src/frequency_analysis.py` saves `visualizations/digit_frequency.png`.
- `web/app.py` computes repository-root paths more robustly, but it still depends on a specific generated filename.

Suggested future direction: centralize path handling in a configuration or I/O module, use `pathlib.Path`, and let CLIs accept explicit input/output paths.

### 4. π generation semantics are unclear

`generate_pi_decimals(num_decimals=1000000)` removes the decimal point from `str(mp.pi)` and writes `pi_str[:num_decimals]`. Because `str(mp.pi)` starts with `3.`, the stored string starts with the integer digit `3`, not with digits strictly after the decimal point. The docs call the output “decimals,” and tests treat position 0 as `314159`, so the intended convention appears to be “digits of π with the decimal point removed.” That convention needs to be named clearly.

Other generation issues:

- The function refuses to regenerate if `data/pi_decimals.txt` already exists, even when a caller asks for a different length.
- There is no provenance metadata: no generation length, precision, method, mpmath version, timestamp, or checksum.
- There is no validation that the existing data file contains only digits or has the expected prefix/length.
- Very large generation requests are not protected by resource checks or progress reporting.

### 5. Tests are too few and data-dependent

Only two tests currently exist, both for sequence search. They load `data/pi_decimals.txt`, so they depend on repository state rather than using controlled fixtures.

Problems:

- No tests for input validation.
- No tests for missing data files.
- No tests for frequency counting.
- No tests for CLI behavior.
- No tests for web routes.
- `test_non_existent_sequence` uses `999999999`, which is not a logically non-existent sequence; it is only absent from the current short data file. That test would fail against a longer prefix if the sequence appears.

Suggested future direction: test pure functions with small explicit strings; reserve generated π data for optional integration tests.

### 6. Plotting and analysis are coupled

`analyze_frequency(pi_decimals)` both computes counts and writes a plot. It does not return counts or percentages. This makes testing and scientific reporting harder.

Suggested future direction:

- Separate `count_digits`, `digit_frequencies`, `chi_square_uniform`, and `plot_digit_counts`.
- Return data structures from analysis functions.
- Make plotting an optional presentation layer.

### 7. Notebook integrity and portability problems

The notebook has several issues that should be addressed before it is treated as a serious scientific artifact:

- It is not valid JSON in the current checkout.
- It hardcodes a Windows path (`D:\Coding\PiSequence\notebooks`).
- It includes outdated repository naming.
- It duplicates logic already present in scripts.
- It includes stronger scientific language than the README and docs.
- It appears to describe files such as `visualizations/digit_frequency.png` and `visualizations/sequence_positions.png`, while the repository currently contains differently named PNG files.

Suggested future direction: repair it only after the package API stabilizes, then clear outputs, remove machine-specific paths, and make it a lightweight reproducible walkthrough.

### 8. Web app is fragile for local/demo use

The Flask app is intentionally minimal, which is fine for this project. It still has technical issues:

- `debug=True` is hardcoded for direct execution.
- A missing `data/pi_decimals.txt` will likely surface as a server error rather than a helpful page.
- `ensure_frequency_plot_link()` uses symlinks, which may behave differently on Windows or restricted filesystems.
- The web UI can only search a loaded local prefix and does not display which prefix length is loaded.
- The frequency page looks for a generated filename that does not match committed visualization filenames.

### 9. Dependency and tooling gaps

`requirements.txt` lists only runtime dependencies and no versions. There is no separation of runtime, development, testing, and notebook dependencies.

Missing project infrastructure:

- `pyproject.toml` with package metadata and tool configuration.
- Formatter/linter/type-checker configuration.
- Test runner configuration.
- Continuous integration.
- Reproducibility instructions for generated artifacts.
- Data policy for checked-in generated files.

## Main scientific and documentation problems

### 1. README and docs overclaim check

The current README is mostly appropriately cautious. It explicitly says:

- the project does not try to prove that π is normal;
- finite-prefix experiments do not establish statistical normality;
- sequence occurrence does not imply semantic meaning;
- the normality of π in base 10 is unproven.

`docs/pi_normal_hypothesis.md` is also mostly careful. It defines normality as an asymptotic property, says π normality is a conjecture, and states that finite checks are not proofs.

The audit finding is therefore not that the README currently overclaims. The main concern is consistency: other repository material, especially the notebook and names such as `meaningful_sequences.py`, is less careful.

### 2. Notebook contains scientifically risky language

The notebook includes statements that should be softened or corrected in a future documentation pass:

- Finite digit counts are described as “supporting the hypothesis that π is normal.” A safer formulation is: “consistent with what uniform single-digit frequencies would predict for this finite prefix.”
- π's decimals are described as varying “due to randomness.” π is deterministic; random-sequence models can be useful comparators, but π digits are not random draws.
- The phrase “meaningful sequences” and claims about “significant sequences” risk inviting numerological interpretation.
- The summary says that if π is normal, its decimals are “completely random.” Normality is weaker than algorithmic randomness and should not be described that way.
- Questions such as whether π “contains all knowledge” should be framed as philosophical metaphors, not mathematical consequences.

### 3. Single-digit frequency is too narrow for normality discussion

The current analysis checks only digit frequencies. Base-10 normality requires limiting frequencies for every finite block length. A serious educational project should explain that single-digit balance is only the first and weakest diagnostic.

Suggested future additions:

- block-frequency counts for `k=1, 2, 3, ...` over finite prefixes;
- expected-count warnings when `10**k` is large relative to the prefix length;
- simple goodness-of-fit statistics with careful caveats;
- comparison against generated pseudo-random digit strings of the same length;
- repeated-prefix analyses showing convergence behavior without implying proof.

### 4. Sequence search needs probability context

Searching for birthdays, short primes, or binary strings is educational, but the current project should explain expected waiting times and multiple-comparison effects. Short strings are expected to appear early in any long digit sequence; longer strings may be absent simply because the sampled prefix is too short.

Recommended framing:

- call these “target strings” or “example queries,” not “meaningful sequences”;
- show approximate expected occurrences under an independent uniform digit model;
- explicitly distinguish “found in the prefix” from “mathematically guaranteed to occur.”

### 5. References are minimal

The existing references are not fake, which is good. However, a serious project should prefer stable primary or survey references over casual links where possible. The Bailey and Borwein survey is appropriate. Wikipedia and online pi-search utilities can remain as introductory resources, but they should not be the backbone of the scientific explanation.

## Suggested target architecture

A future package could preserve the lightweight spirit while separating reusable computation from scripts, documentation, examples, and web presentation.

```text
Pi-Normality-Hypothesis/
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
├── docs/
│   ├── AUDIT.md
│   ├── scientific_background.md
│   ├── methodology.md
│   ├── user_guide.md
│   └── limitations.md
├── examples/
│   ├── search_targets.py
│   ├── digit_frequency_report.py
│   └── block_frequency_report.py
├── notebooks/
│   └── finite_prefix_exploration.ipynb
├── src/
│   └── pi_normality_explorer/
│       ├── __init__.py
│       ├── constants.py
│       ├── io.py
│       ├── pi_digits.py
│       ├── search.py
│       ├── frequencies.py
│       ├── statistics.py
│       ├── plotting.py
│       ├── cli.py
│       └── web/
│           ├── app.py
│           ├── templates/
│           └── static/
├── tests/
│   ├── test_io.py
│   ├── test_pi_digits.py
│   ├── test_search.py
│   ├── test_frequencies.py
│   ├── test_statistics.py
│   ├── test_cli.py
│   └── test_web.py
├── data/
│   ├── README.md
│   └── sample_pi_digits.txt
└── outputs/
    ├── README.md
    └── .gitkeep
```

### Proposed module responsibilities

- `pi_digits.py`: generation and validation of π digit strings; clear convention about whether the leading `3` is included.
- `io.py`: read/write paths, metadata sidecars, checksums, and repository-relative defaults.
- `search.py`: pure sequence-search functions, optional batch search, input validation.
- `frequencies.py`: pure digit and block counting functions.
- `statistics.py`: finite-sample comparisons, expected counts, chi-square-style diagnostics, simulation helpers with caveats.
- `plotting.py`: plotting only; no hidden data loading.
- `cli.py`: argparse or Typer-based entry points.
- `web/app.py`: thin UI layer that calls library functions and handles missing data gracefully.

## Suggested PR roadmap

### PR 1: Audit and planning

- Add this audit.
- Make no code changes.
- Agree on target package name and scientific scope.

### PR 2: Packaging foundation

- Add `pyproject.toml`.
- Choose supported Python versions.
- Move from ad hoc `src` imports to an installable package.
- Add formatter/linter/test configuration.
- Keep compatibility wrappers if needed so existing commands do not break immediately.

### PR 3: Pure core functions and tests

- Extract pure search, digit-count, and block-count functions.
- Remove duplicated `search_sequence` implementation.
- Add tests using small explicit strings.
- Add validation tests for non-digit input and empty sequences.

### PR 4: Data and reproducibility policy

- Decide whether to commit a small sample prefix only, generate larger data on demand, or support externally downloaded/generated datasets.
- Add data provenance metadata and checksums.
- Clarify the “digits of π” convention.
- Make generation length configurable and safe.

### PR 5: Scientific analysis layer

- Add finite-prefix frequency reports for block lengths.
- Add expected-count warnings and simple statistical diagnostics.
- Add random-model comparison examples without implying π is random.
- Document all limitations.

### PR 6: Documentation rewrite

- Keep the current README's cautious tone.
- Rewrite the notebook or replace it with a cleaner tutorial.
- Rename or reframe “meaningful sequences” material.
- Expand scientific background with supported references.

### PR 7: CLI and web polish

- Add robust CLI entry points.
- Improve missing-file handling.
- Show loaded prefix length and data source in outputs.
- Make web plotting portable without symlink assumptions.

### PR 8: Generated artifacts and examples

- Move generated plots to an ignored `outputs/` directory or document exactly which artifacts are intentionally committed.
- Regenerate example figures from reproducible commands.
- Add smoke tests for examples.

## Files that should be preserved

These files should be preserved in spirit, even if some are later renamed, moved, or rewritten:

- `README.md`: cautious framing is valuable and should guide the rest of the project.
- `LICENSE`: keep the current MIT license unless the owner decides otherwise.
- `CONTRIBUTING.md`: keep and later update for new tooling.
- `docs/pi_normal_hypothesis.md`: preserve as the seed of a scientific-background page.
- `docs/user_guide.md`: preserve as the seed of user documentation.
- `src/sequence_search.py`: preserve the core search behavior, likely under a package module.
- `src/frequency_analysis.py`: preserve the digit-frequency idea, but split computation from plotting.
- `src/pi_generator.py`: preserve the local generation idea, but clarify semantics and add metadata.
- `web/app.py` and templates: preserve the lightweight educational UI if the project still wants a web demo.
- `tests/test_search.py`: preserve the intention of basic search tests, but replace data-dependent assertions with fixture-based tests.
- `data/test_sequences.txt`: preserve as example input after cleaning comments and scientific framing.

## Files that may need deletion, replacement, or major rewrite

No files should be deleted in this audit-only PR. The following files are candidates for future removal, replacement, or substantial rewrite after manual review:

- `notebooks/PiSequence.ipynb`: likely needs repair or replacement because it is invalid JSON, machine-specific, and scientifically overstates some interpretations.
- `src/meaningful_sequences.py`: should probably be renamed and rewritten as an example script using shared search functions.
- `data/pi_decimals.txt`: current file is a tiny sample despite documentation describing 1,000,000 digits; decide whether it is a fixture, sample data, or generated artifact.
- `visualizations/digit_frequency_pi.png` and `visualizations/sequence_positions_pi.png`: clarify whether these are source-controlled examples or stale generated outputs. Current docs and web code expect different filenames.
- `requirements.txt`: may be replaced or supplemented by `pyproject.toml` dependency groups.
- `tests/conftest.py`: may become unnecessary after installing the package in editable mode for tests.
- `src/__init__.py`: should move under the real package path once packaging is introduced.

## Risks and manual review points

### Scientific risks

- Do not claim, imply, or rhetorically suggest that the project proves π is normal.
- Avoid describing π digits as random. Use “random-model comparison,” “random-looking,” or “consistent with a uniform model for this finite prefix” where appropriate.
- Avoid saying that a found target string is meaningful because it appears in π.
- Distinguish base-10 normality from stronger ideas such as algorithmic randomness.
- Explain that finite samples can be consistent with normality while still proving nothing about the limiting property.

### Engineering risks

- Package renaming can break existing commands and notebooks; add compatibility shims or document migration steps.
- Regenerating large π files can be slow and memory-intensive; generation should be explicit and bounded.
- Symlink behavior in the web app may fail on some platforms.
- If generated data or plots are removed from version control, quick-start instructions must regenerate them reliably.
- If generated data remains in version control, provenance and size policy must be clear.

### Manual review questions

1. What should the canonical package name be: `pi_sequence`, `pi_normality_explorer`, or something else?
2. Should the stored digit string include the leading integer digit `3`, or only digits after the decimal point?
3. Should the repository commit any generated π digits beyond a tiny test fixture?
4. Should the Flask app remain part of the core project, move to `examples/`, or be optional?
5. Should notebooks be maintained as first-class reproducible artifacts, or should examples be plain Python scripts?
6. Which scientific references should be treated as canonical for the documentation?
7. What level of statistical analysis is appropriate for the educational scope without encouraging overinterpretation?

## Commands used during audit

The following local commands informed this audit:

```bash
find . -maxdepth 2 -type f | sort
find . -maxdepth 3 -type d | sort
find . -path ./.git -prune -o -type f -print | sort
sed -n '1,240p' README.md
sed -n '1,240p' docs/pi_normal_hypothesis.md
sed -n '1,240p' docs/user_guide.md
nl -ba src/frequency_analysis.py
nl -ba src/meaningful_sequences.py
nl -ba src/pi_generator.py
nl -ba src/sequence_search.py
nl -ba src/utils.py
nl -ba web/app.py
nl -ba web/templates/index.html
nl -ba web/templates/result.html
nl -ba web/static/style.css
nl -ba tests/test_search.py
nl -ba tests/conftest.py
wc -c data/pi_decimals.txt data/test_sequences.txt
python -m unittest discover tests
python -m compileall src web tests
rg -n "from src|import src|def search_sequence|normal|Normal|proof|prove|random|meaningful|hypothesis|supporting|confirm" . --glob '!docs/AUDIT.md'
```
