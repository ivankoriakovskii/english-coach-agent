# Analyzed Chat Registry

Use learner-message coverage, not assistant/tool activity, to determine whether new evidence exists. After the recorded boundary, analyze only new learner speech; overlapping realtime deltas must be matched against the previous covered utterances before incrementing counts.

| chat_id | chat title | last message analyzed | analyzed at | result |
|---|---|---|---|---|
| 01a09707-bf57-7841-ad54-0d9530e197c9 | AI Agents for Career Growth | 01a09730-9097-7432-9b34-3f42d6872a3e (tail flush); final learner request 01a0972f-75a3-7613-a61c-68dfbabcba40, replay 01a09730-7ce9-7803-8421-f125af981a26 | 2026-09-12 19:56 UTC | Both history pages / 11 turns inspected; one practice session 2026-09-12-2125-ai-agents; setup excluded from counts; input/delta replays deduplicated |
| 01a09701-d300-7d90-a1c0-40a892e9632b | Проанализировать English Coach | User message 01a09702-acd9-73b0-baed-3c2942391f86; analysis delegation turn 01a09730-7c14-7332-9849-32c8e5ab6eeb inspected | 2026-09-12 19:56 UTC | Russian setup/project review; delegated English quotes are not new learner production |

## Discovery coverage

list_threads(limit=50) returned these two tasks for project 65eba7f4-5ff0-4efa-a899-7cae8ce6a41b / C:\Users\korya\Desktop\agents\english-coach-agent. No unavailable sources/hosts were reported. Local archived-task listing was empty. Other listed ChatGPT conversations have a different or null project ID; they were not presumed part of this project based on their titles. This records accessible discovery coverage, not a guarantee about unexposed history.

## Reprocessing rule for this baseline

E01–E11 are already counted. Repeated quotation in feedback, reports, setup chats or overlapping deltas is not new evidence. The final learner request begins "I think it's enough... for today"; its replay is covered. Pronunciation was not assessed.

