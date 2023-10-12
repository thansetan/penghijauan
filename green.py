from datetime import datetime, timedelta

with open("README.md", "w") as f:
    f.write(
        (datetime.utcnow() + timedelta(hours=7)).strftime(
            "🕰️ Updated on %A, %d %B %Y at %I:%M %p WIB"
        )
    )
