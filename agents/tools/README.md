# Agent Tools

Reusable repo-local tools for agents and humans.

Use this folder for executable scripts, command wrappers, validation helpers, generators, small utilities, CLI helpers, and app integrations that support agent work across the project.

## Guidelines

- Prefer small tools with clear inputs and outputs.
- Document how to run each tool.
- Keep destructive actions opt-in and obvious.
- Do not store secrets, tokens, private machine paths, or generated outputs here.
- Put temporary output in `_build/` or another ignored location.
- If a tool becomes project-specific rather than agent-harness-specific, move it closer to the project code under `workspace/` or `packages/`.

## Suggested Layout

```text
agents/tools/
  README.md
  tool-name/
    README.md
    scripts-or-source-files
```

## Privacy Preflight

`privacy_preflight.py` is a dependency-free Python 3.10+ commit and publication gate configured by `agents/privacy-policy.json`. See the root [prerequisites](../../README.md#prerequisites) for Git requirements, Python launchers, and tested environments. History modes inspect full commit messages as well as author/committer identities and file content.

```text
python -m unittest discover -s agents/tools/tests -v
python agents/tools/privacy_preflight.py working
python agents/tools/privacy_preflight.py staged
python agents/tools/privacy_preflight.py push
python agents/tools/privacy_preflight.py install-hooks
```

Hook installation is explicit and refuses to overwrite unrelated hooks. See [Privacy And Publication Safety](../rules/privacy-and-publication.md) for history, remote-ref, local-ref, local-policy, and report commands.
