# Docs

Durable human-facing documentation for the project.

Suggested subfolders:

- `architecture/` - system design and technical notes
- `decisions/` - ADR-style decision records
- `operations/` - runbooks, deployment, release, and maintenance notes
- `releases/` - checked-in release notes, not binary artifacts

Create subfolders when the project actually needs them.

Version documentation releases by date and build number by default, following the [shared release versioning convention](../agents/rules/repo-conventions.md#build-and-documentation-release-versioning). For example: `2026-10-05 · Build 1`, with release notes named `2026-10-05-build-1.md` under `releases/` when needed.
