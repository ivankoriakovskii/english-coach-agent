# English Coach Agent

A file-backed English coaching system for long-term tracking of recurring mistakes.

## Goal

The agent should not merely correct the current message. It should maintain a durable model of the learner's English weaknesses and progress over time.

The canonical state lives in Markdown files under `data/`.

## Recommended operating model

Use this package inside a persistent workspace/project where the agent is allowed to read and modify files.

At the beginning of a session:

1. Read `SKILL.md`.
2. Read `data/profile.md`.
3. Read `data/error-registry.md`.
4. Read the relevant specialist files:
   - `data/pronunciation.md`
   - `data/vocabulary.md`
   - `data/fluency.md`
   - `data/progress.md`
5. Read `data/session-index.md` and, when useful, recent session notes.

At the end of a meaningful practice session:

1. Extract observed errors.
2. Merge them into existing patterns when possible.
3. Update counts and evidence.
4. Recalculate status/severity where appropriate.
5. Append a session record.
6. Update progress summaries.
7. Never erase historical evidence merely because a problem improved.

## Core files

- `SKILL.md` — executable behavior/protocol for the agent.
- `AGENT_INSTRUCTIONS.md` — project-level behavior and teaching style.
- `config.yaml` — thresholds and tracking settings.
- `data/profile.md` — learner goals and stable context.
- `data/error-registry.md` — canonical recurring-error database.
- `data/pronunciation.md` — pronunciation-specific observations.
- `data/vocabulary.md` — lexical and collocation issues.
- `data/fluency.md` — spoken fluency issues.
- `data/progress.md` — current high-level assessment and trends.
- `data/session-index.md` — compact index of completed sessions.
- `data/sessions/` — detailed session notes.

## Important design rule

`data/error-registry.md` is the source of truth for recurring language problems.

Specialist files may contain extra detail, but they must reference the same `error_id` rather than creating competing identities.
