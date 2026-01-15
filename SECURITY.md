# Security Policy

## Supported Versions

- Only the latest code on `master` receives security updates.
- Historical versions are provided for reference and are unsupported unless the
	issue reproduces on the stack below.

## Ecosystem & Compatibility

| Component            | Version(s) / Tooling                | Notes |
| -------------------- | ---------------------------------- | ----- |
| OS baseline          | WSL (Ubuntu 24.04.3 LTS)           | Matches the README instructions. |
| Ruby CLI utilities   | Ruby 4.0.1 (`.ruby-version`)       | Uses standard library (`CSV`, `FileUtils`). Declare extra gems per script if needed. |
| Python CLI utilities | CPython 3.14.2 (`.python-version`) | Uses Python stdlib (`csv`, `argparse`). Introduce `requirements.txt` if third-party libs are added. |

## Backward Compatibility

- Command-line prompts and delimiter-conversion logic remain stable within Ruby
	4.0.x / Python 3.14.x. Any breaking change will be announced in the README.
- Earlier interpreter majors are not tested and will not receive backports.

## Reporting a Vulnerability

Report vulnerabilities privately through GitHub’s **Security → Report a
vulnerability** workflow or email `security@project.org` with the exact CLI
parameters (`original_extension`, `target_extension`, etc.), sample files, and
environment details. Expect acknowledgement within **3 business days** and
status updates at least every **7 business days**.
