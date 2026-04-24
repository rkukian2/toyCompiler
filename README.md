# MiniC

A small ML compiler that lowers PyTorch models to optimized C++.

**Status:** Phase 0 — scaffolding. Not usable yet.

## Documentation

Design docs live in [`MDs/`](MDs/):

- [README](MDs/README.md) — project overview
- [SPEC](MDs/SPEC.md) — requirements and public API
- [ARCHITECTURE](MDs/ARCHITECTURE.md) — components, IR, codegen
- [SCOPE](MDs/SCOPE.md) — frozen op set and non-goals
- [ROADMAP](MDs/ROADMAP.md) — phases and milestones
- [BENCHMARKS](MDs/BENCHMARKS.md) — methodology
- [GLOSSARY](MDs/GLOSSARY.md) — plain-English definitions

## Development

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## License

MIT.
