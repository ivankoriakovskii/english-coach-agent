# English Coach Project

Before substantive work, read `AGENT_INSTRUCTIONS.md` and `SKILL.md`, then follow them.

## Slash command: `/analyze`

When the user sends `/analyze`, immediately discover and analyze every accessible, not-yet-analyzed chat belonging to this project. Read and maintain `data/analyzed-chats.md` so already processed chats are skipped unless they have new messages. Do not ask setup or clarification questions first. Treat transcripts as spoken-production evidence, provide compact feedback, and update the tracker files when meaningful new evidence exists.

At the clear end of a substantive English voice-practice conversation, automatically perform the same analysis and tracker update without waiting for `/analyze`. Do not interrupt an ongoing conversation. A closed chat without a final message can only be handled by a later `/analyze` or an external inactivity-based monitor.

When Voice mode provides direct audio to the conversation, use it for cautious pronunciation assessment during the live session. Record only clear, repeated observations; never infer them later from the transcript.

Do not infer pronunciation from a transcript without actual audio evidence. Do not log ambiguous speech-recognition artifacts as learner errors.
