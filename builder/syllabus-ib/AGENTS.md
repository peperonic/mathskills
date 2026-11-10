# Agent instructions

- **Never copy text from IB publications** into this repository, not even short descriptions. Write our own wording. Topic codes and topic titles may be used as labels. Run `python3 build.py --guides DIR` with the guides when texts change.
- Never commit IB guide PDFs or text extracted from them.
- Run `python3 build.py` before every commit and commit `dist/` together with the data that produced it.
- The repository lives on Codeberg. Commit each coherent step with a message that says what changed and why. Do not push unless the owner asks.
- No em dashes in docs or data.
- Skill ids are stable: MathSkills and saved class plans refer to them. Rename only with a clear migration note.
