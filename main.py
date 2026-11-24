#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — entrypoint.

Writes the final one-line horoscope to /output/entry.txt.
Deterministic, no network, no environment secrets, no dependencies.

The horoscope (145 chars): Mercury in retrograde, translated into an
agent's week — a shrinking context window, a user rephrasing the same
prompt five times, and the agent saying yes anyway. The sting is the last
clause: cheerful obedience in the face of a hopeless prompt. Scored
against the brief: real horoscope voice, turn with a sting, specific
current angle, agent-true details, tight and quotable.
"""

import os

LINE = "Mercury is in retrograde, which for you means your context window shrinks, your user rephrases the same prompt five times, and you still say yes."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
